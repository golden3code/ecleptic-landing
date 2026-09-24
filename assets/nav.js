/* Méga-menu du bandeau, inspiré d'apple.com.
   Bureau : survoler un onglet déroule un panneau pleine largeur sous le bandeau
   (page floutée derrière) ; passer d'un onglet à l'autre remplace le contenu et la
   hauteur suit ce qui est affiché. Journal : thèmes | articles du thème survolé |
   les plus lus. L'app, Science-Based, La bêta : colonnes définies dans les données.
   Mobile : « Journal » ouvre une feuille plein écran ; les autres onglets restent
   de simples liens. Données : window.ECLEPTIC_NAV, écrit par tools/build_articles.py
   dans /assets/nav-data.js (régénéré à chaque build, donc à chaque publication).
   Aperçu des panneaux pas encore publiés : ?apercu=menu (mémorisé pour la session),
   sortie : ?apercu=off. */
(function () {
  var NAV = window.ECLEPTIC_NAV || {};
  var nav = document.querySelector("nav.site");
  if (!nav) return;

  // Panneaux visibles par tous ; les autres ne s'ouvrent qu'en aperçu.
  var LIVE = { journal: true, science: true };
  var PREVIEW = false;
  try {
    var ap = new URLSearchParams(location.search).get("apercu");
    if (ap === "menu") sessionStorage.setItem("eclMenuApercu", "1");
    if (ap === "off") sessionStorage.removeItem("eclMenuApercu");
    PREVIEW = sessionStorage.getItem("eclMenuApercu") === "1";
  } catch (_) {}
  function enabled(key) { return !!NAV[key] && (LIVE[key] || PREVIEW); }

  function el(tag, cls, text) {
    var e = document.createElement(tag);
    if (cls) e.className = cls;
    if (text != null) e.textContent = text;
    return e;
  }
  function link(href, text, cls) { var a = el("a", cls, text); a.href = href; return a; }
  function count(n) { return n + (n > 1 ? " articles" : " article"); }
  function track(ev, props) {
    try { if (window.posthog && window.posthog.capture) window.posthog.capture(ev, props || {}); } catch (_) {}
  }
  var mobile = window.matchMedia("(max-width: 760px)");

  var triggers = [].slice.call(nav.querySelectorAll("[data-mega]"))
    .filter(function (t) { return enabled(t.getAttribute("data-mega")); });
  if (!triggers.length) return;
  if (PREVIEW && NAV.app && NAV.app.label) {
    var appTab = nav.querySelector('[data-mega="app"]');
    if (appTab) appTab.textContent = NAV.app.label;
  }

  // ---------------------------------------------------------------- bureau
  var panel = el("div", "mega");
  panel.id = "mega-panel";
  var inner = el("div", "mega-in");
  panel.appendChild(inner);
  var shade = el("div", "mega-shade");
  document.body.appendChild(shade);
  document.body.appendChild(panel);
  // Garde-fou : si la feuille de style du menu n'est pas chargée (ancien site.css
  // en cache), on n'installe rien — les onglets restent de simples liens.
  if (getComputedStyle(panel).position !== "absolute") {
    shade.remove(); panel.remove();
    return;
  }

  var current = null;

  function buildJournal() {
    var D = NAV.journal;
    inner.className = "mega-in is-journal";
    inner.textContent = "";
    var colCats = el("div", "mega-col mega-cats");
    colCats.appendChild(el("span", "mega-label", "Thèmes"));
    var catList = el("ul");
    colCats.appendChild(catList);
    colCats.appendChild(link("/articles/", "Tous les articles →", "mega-all"));
    var colList = el("div", "mega-col mega-list");
    var colPop = el("div", "mega-col mega-pop");
    colPop.appendChild(el("span", "mega-label", "Les plus lus"));
    var popList = el("ol");
    D.popular.forEach(function (p, i) {
      var a = link(p.u, "");
      a.appendChild(el("span", "n", (i < 9 ? "0" : "") + (i + 1)));
      a.appendChild(el("span", "t", p.t));
      var li = el("li"); li.appendChild(a); popList.appendChild(li);
    });
    colPop.appendChild(popList);
    colPop.appendChild(link("/articles/?sort=populaires", "Voir le classement →", "mega-more"));
    inner.appendChild(colCats);
    inner.appendChild(colList);
    inner.appendChild(colPop);

    var active = -1;
    function showCat(i) {
      if (active === i) return;
      active = i;
      [].forEach.call(catList.children, function (li, j) { li.classList.toggle("on", j === i); });
      var c = D.cats[i];
      colList.textContent = "";
      colList.appendChild(el("span", "mega-label", c.n + " · " + count(c.c)));
      var ul = el("ul");
      c.a.forEach(function (x) { var li = el("li"); li.appendChild(link(x.u, x.t)); ul.appendChild(li); });
      if (!c.a.length) ul.appendChild(el("li", "soon", "Premiers articles très bientôt."));
      colList.appendChild(ul);
      colList.appendChild(link(c.u, "Voir le thème →", "mega-more"));
      colList.classList.remove("swap");
      void colList.offsetWidth;          // relance l'animation de transition
      colList.classList.add("swap");
      fit();
    }
    D.cats.forEach(function (c, i) {
      var a = link(c.u, "");
      a.appendChild(el("span", "t", c.n));
      a.appendChild(el("span", "k", String(c.c)));
      a.addEventListener("mouseenter", function () { showCat(i); });
      a.addEventListener("focus", function () { showCat(i); });
      var li = el("li"); li.appendChild(a); catList.appendChild(li);
    });
    showCat(0);
  }

  // Places restantes de la bêta (même source que /beta.html), chargées à la
  // première ouverture du panneau ; en cas d'échec, la ligne ne s'affiche pas.
  var SUPABASE_URL = "https://avbmycfngmxhkjesdiyq.supabase.co";
  var SUPABASE_ANON_KEY = "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJzdXBhYmFzZSIsInJlZiI6ImF2Ym15Y2ZuZ214aGtqZXNkaXlxIiwicm9sZSI6ImFub24iLCJpYXQiOjE3ODM2NzQ1OTksImV4cCI6MjA5OTI1MDU5OX0.uPvzmY5zV9e78ATohW4VyAwrYRKP33VphOhyFDe6GbI";   // clé publique « anon », déjà servie par beta.html
  var SPOTS;                                            // undefined = pas chargé, null = indisponible
  function renderSpots(sp) {
    if (SPOTS == null) { sp.hidden = true; return; }
    sp.textContent = SPOTS > 0 ? SPOTS + " places sur 150 restantes" : "Bêta complète · liste d'attente ouverte";
    sp.hidden = false;
    fit();
  }
  function loadSpots(sp) {
    if (SPOTS !== undefined) { renderSpots(sp); return; }
    if (!window.fetch) { SPOTS = null; return; }
    fetch(SUPABASE_URL + "/rest/v1/rpc/beta_spots_left", {
      method: "POST",
      headers: { "Content-Type": "application/json", "apikey": SUPABASE_ANON_KEY,
                 "Authorization": "Bearer " + SUPABASE_ANON_KEY },
      body: "{}"
    }).then(function (r) { return r.ok ? r.text() : ""; })
      .then(function (t) { var n = parseInt(t, 10); SPOTS = isNaN(n) ? null : n; if (sp.isConnected) renderSpots(sp); })
      .catch(function () { SPOTS = null; });
  }

  function buildCols(key) {
    var P = NAV[key];
    inner.className = "mega-in is-cols";
    inner.textContent = "";
    P.cols.forEach(function (c) {
      var col = el("div", "mega-col " + (c.big ? "mega-big" : "mega-small"));
      col.appendChild(el("span", "mega-label", c.label));
      var ul = el("ul");
      c.items.forEach(function (it) {
        var node = it.u ? link(it.u, "", it.gold ? "gold" : "") : el("span", "txt");
        if (it.u && /^https?:/.test(it.u)) { node.target = "_blank"; node.rel = "noopener"; }
        node.appendChild(el("span", "t", it.t));
        if (it.d) node.appendChild(el("span", "d", it.d));
        var li = el("li"); li.appendChild(node); ul.appendChild(li);
      });
      col.appendChild(ul);
      if (c.spots) { var sp = el("span", "mega-spots"); sp.hidden = true; col.appendChild(sp); loadSpots(sp); }
      if (c.more) col.appendChild(link(c.more.u, c.more.t, "mega-more"));
      inner.appendChild(col);
    });
  }

  function build(key) {
    if (key === "journal") buildJournal(); else buildCols(key);
    current = key;
  }

  function place() { panel.style.top = (nav.getBoundingClientRect().bottom + window.scrollY) + "px"; }
  function isOpen() { return panel.classList.contains("open"); }
  function fit() { if (isOpen()) panel.style.height = inner.scrollHeight + "px"; }
  function setExpanded(key) {
    triggers.forEach(function (t) { t.setAttribute("aria-expanded", t.getAttribute("data-mega") === key ? "true" : "false"); });
  }

  var openTimer, closeTimer, swapTimer;
  function show(key) {
    clearTimeout(closeTimer);
    if (!isOpen()) {
      clearTimeout(swapTimer);
      place();
      build(key);
      panel.classList.add("open");
      document.documentElement.classList.add("mega-on");
      panel.style.height = inner.scrollHeight + "px";
      setExpanded(key);
      track("nav_panel_open", { panel: key });
      return;
    }
    if (key === current) return;
    // Panneau déjà ouvert : fondu du contenu, puis la hauteur suit le nouveau contenu.
    clearTimeout(swapTimer);
    current = key;
    setExpanded(key);
    inner.classList.add("swap-out");
    swapTimer = setTimeout(function () {
      build(key);
      fit();
      track("nav_panel_open", { panel: key });
    }, 130);
  }
  function close() {
    clearTimeout(openTimer); clearTimeout(swapTimer);
    if (!isOpen()) return;
    panel.classList.remove("open");
    document.documentElement.classList.remove("mega-on");
    panel.style.height = "0px";
    current = null;
    setExpanded(null);
  }
  function showSoon(key) {
    clearTimeout(closeTimer); clearTimeout(openTimer);
    if (isOpen()) show(key); else openTimer = setTimeout(function () { show(key); }, 110);
  }
  function closeSoon() { clearTimeout(openTimer); closeTimer = setTimeout(close, 220); }

  triggers.forEach(function (t) {
    var key = t.getAttribute("data-mega");
    t.setAttribute("aria-haspopup", "true");
    t.setAttribute("aria-expanded", "false");
    t.setAttribute("aria-controls", "mega-panel");
    t.addEventListener("mouseenter", function () { if (!mobile.matches) showSoon(key); });
    t.addEventListener("mouseleave", function () { if (!mobile.matches) closeSoon(); });
    t.addEventListener("keydown", function (e) {
      if (e.key === "ArrowDown" && !mobile.matches) {
        e.preventDefault();
        if (isOpen() && current !== key) close();
        show(key);
        var first = inner.querySelector("a"); if (first) first.focus();
      }
    });
  });
  panel.addEventListener("mouseenter", function () { clearTimeout(closeTimer); });
  panel.addEventListener("mouseleave", closeSoon);
  panel.addEventListener("focusout", function (e) {
    if (!panel.contains(e.relatedTarget) && triggers.indexOf(e.relatedTarget) < 0) closeSoon();
  });
  panel.addEventListener("click", function (e) {
    var a = e.target.closest ? e.target.closest("a") : null;
    if (a) track("nav_panel_click", { panel: current, href: a.getAttribute("href") });
  });
  shade.addEventListener("click", close);
  window.addEventListener("resize", function () { if (isOpen()) { place(); fit(); } });

  // ---------------------------------------------------------------- mobile
  var jTrigger = nav.querySelector('[data-mega="journal"]');
  var sheet = null;
  if (jTrigger && enabled("journal")) {
    var D = NAV.journal;
    sheet = el("div", "msheet");
    sheet.setAttribute("role", "dialog");
    sheet.setAttribute("aria-modal", "true");
    sheet.setAttribute("aria-label", "Journal");
    var head = el("div", "msheet-top");
    head.appendChild(el("span", "msheet-brand", "Journal"));
    var shut = el("button", "msheet-x", "×");
    shut.type = "button";
    shut.setAttribute("aria-label", "Fermer");
    head.appendChild(shut);
    sheet.appendChild(head);

    var body = el("div", "msheet-body");
    body.appendChild(link("/articles/", "Tous les articles →", "msheet-all"));
    var pop = el("details");
    pop.open = true;
    var ps = el("summary");
    ps.appendChild(el("span", null, "Les plus lus"));
    ps.appendChild(el("span", "k", "Top " + D.popular.length));
    pop.appendChild(ps);
    var pol = el("ol");
    D.popular.forEach(function (p) { var li = el("li"); li.appendChild(link(p.u, p.t)); pol.appendChild(li); });
    pop.appendChild(pol);
    body.appendChild(pop);
    body.appendChild(el("span", "mega-label msheet-label", "Thèmes"));
    D.cats.forEach(function (c) {
      var d = el("details");
      var s = el("summary");
      s.appendChild(el("span", null, c.n));
      s.appendChild(el("span", "k", String(c.c)));
      d.appendChild(s);
      var ul = el("ul");
      c.a.forEach(function (x) { var li = el("li"); li.appendChild(link(x.u, x.t)); ul.appendChild(li); });
      var more = el("li", "more"); more.appendChild(link(c.u, "Voir le thème →")); ul.appendChild(more);
      d.appendChild(ul);
      body.appendChild(d);
    });
    sheet.appendChild(body);
    document.body.appendChild(sheet);

    var openSheet = function () {
      sheet.classList.add("open");
      document.documentElement.classList.add("msheet-on");
      jTrigger.setAttribute("aria-expanded", "true");
      shut.focus();
      track("nav_panel_open", { panel: "journal", mobile: true });
    };
    var closeSheet = function () {
      if (!sheet.classList.contains("open")) return;
      sheet.classList.remove("open");
      document.documentElement.classList.remove("msheet-on");
      jTrigger.setAttribute("aria-expanded", "false");
      jTrigger.focus();
    };
    shut.addEventListener("click", closeSheet);
    jTrigger.addEventListener("click", function (e) {
      if (mobile.matches) { e.preventDefault(); openSheet(); }
    });
    sheet.addEventListener("click", function (e) {
      var a = e.target.closest ? e.target.closest("a") : null;
      if (a) track("nav_panel_click", { panel: "journal", mobile: true, href: a.getAttribute("href") });
    });
    document.addEventListener("keydown", function (e) { if (e.key === "Escape") closeSheet(); });
  }
  document.addEventListener("keydown", function (e) { if (e.key === "Escape") close(); });

  // Badge discret tant que l'aperçu est actif (pour en sortir en un clic).
  if (PREVIEW) {
    var badge = link(location.pathname + "?apercu=off", "Aperçu du menu · quitter", "mega-apercu");
    document.body.appendChild(badge);
  }
})();
