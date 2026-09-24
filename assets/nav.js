/* Méga-menu du bandeau, inspiré d'apple.com.
   Bureau : le survol de « Journal » déroule un panneau pleine largeur sous le
   bandeau (page floutée derrière) — thèmes à gauche, articles du thème survolé au
   centre, « Les plus lus » à droite ; la hauteur suit le contenu affiché.
   Mobile : toucher « Journal » ouvre une feuille plein écran (thèmes dépliables).
   Données : window.ECLEPTIC_NAV, écrit par tools/build_articles.py dans
   /assets/nav-data.js (régénéré à chaque build, donc à chaque publication). */
(function () {
  var D = window.ECLEPTIC_NAV && window.ECLEPTIC_NAV.journal;
  var nav = document.querySelector("nav.site");
  var trigger = nav && nav.querySelector('[data-mega="journal"]');
  if (!D || !trigger) return;

  function el(tag, cls, text) {
    var e = document.createElement(tag);
    if (cls) e.className = cls;
    if (text != null) e.textContent = text;
    return e;
  }
  function link(href, text, cls) { var a = el("a", cls, text); a.href = href; return a; }
  function count(n) { return n + (n > 1 ? " articles" : " article"); }
  var mobile = window.matchMedia("(max-width: 760px)");

  // ---------------------------------------------------------------- bureau
  var panel = el("div", "mega");
  panel.id = "mega-journal";
  var inner = el("div", "mega-in");
  panel.appendChild(inner);

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

  var shade = el("div", "mega-shade");
  document.body.appendChild(shade);
  document.body.appendChild(panel);
  // Garde-fou : si la feuille de style du menu n'est pas chargée (ancien site.css
  // en cache), on n'installe rien — « Journal » reste un simple lien.
  if (getComputedStyle(panel).position !== "absolute") {
    shade.remove(); panel.remove();
    return;
  }

  function place() { panel.style.top = (nav.getBoundingClientRect().bottom + window.scrollY) + "px"; }
  function isOpen() { return panel.classList.contains("open"); }
  function fit() { if (isOpen()) panel.style.height = inner.scrollHeight + "px"; }

  var openTimer, closeTimer;
  function open() {
    clearTimeout(closeTimer);
    if (isOpen()) return;
    place();
    if (active < 0) showCat(0);
    panel.classList.add("open");
    document.documentElement.classList.add("mega-on");
    trigger.setAttribute("aria-expanded", "true");
    panel.style.height = inner.scrollHeight + "px";
  }
  function close() {
    clearTimeout(openTimer);
    if (!isOpen()) return;
    panel.classList.remove("open");
    document.documentElement.classList.remove("mega-on");
    trigger.setAttribute("aria-expanded", "false");
    panel.style.height = "0px";
  }
  function openSoon() { clearTimeout(closeTimer); openTimer = setTimeout(open, 110); }
  function closeSoon() { clearTimeout(openTimer); closeTimer = setTimeout(close, 220); }

  trigger.setAttribute("aria-haspopup", "true");
  trigger.setAttribute("aria-expanded", "false");
  trigger.setAttribute("aria-controls", "mega-journal");
  trigger.addEventListener("mouseenter", function () { if (!mobile.matches) openSoon(); });
  trigger.addEventListener("mouseleave", function () { if (!mobile.matches) closeSoon(); });
  trigger.addEventListener("keydown", function (e) {
    if (e.key === "ArrowDown" && !mobile.matches) {
      e.preventDefault(); open();
      var first = catList.querySelector("a"); if (first) first.focus();
    }
  });
  panel.addEventListener("mouseenter", function () { clearTimeout(closeTimer); });
  panel.addEventListener("mouseleave", closeSoon);
  panel.addEventListener("focusout", function (e) {
    if (!panel.contains(e.relatedTarget) && e.relatedTarget !== trigger) closeSoon();
  });
  shade.addEventListener("click", close);
  window.addEventListener("resize", function () { if (isOpen()) { place(); fit(); } });

  // ---------------------------------------------------------------- mobile
  var sheet = el("div", "msheet");
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

  function openSheet() {
    sheet.classList.add("open");
    document.documentElement.classList.add("msheet-on");
    trigger.setAttribute("aria-expanded", "true");
    shut.focus();
  }
  function closeSheet() {
    if (!sheet.classList.contains("open")) return;
    sheet.classList.remove("open");
    document.documentElement.classList.remove("msheet-on");
    trigger.setAttribute("aria-expanded", "false");
    trigger.focus();
  }
  shut.addEventListener("click", closeSheet);
  trigger.addEventListener("click", function (e) {
    if (mobile.matches) { e.preventDefault(); openSheet(); }
  });
  document.addEventListener("keydown", function (e) {
    if (e.key === "Escape") { close(); closeSheet(); }
  });
})();
