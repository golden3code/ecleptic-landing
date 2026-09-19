#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Génère les pages articles + l'index /articles/ + sitemap.xml.

Pour ajouter un article : ajouter une entrée dans ARTICLES puis lancer
    python3 tools/build_articles.py
depuis la racine du repo landing, et commiter les fichiers générés.
"""
import os, html

SITE = "https://ecleptic.health"
TF_LINK = "https://testflight.apple.com/join/H5CQgDa7"
POSTHOG_KEY = "phc_wzjqudiS3KH7MeMii8h6HmUR2onfQR5iasjhAs53AL2B"

# slug, title (H1 + <title>), description (meta), date ISO, body HTML
ARTICLES = [
    # Pour ajouter un article :
    # {
    #     "slug": "mon-slug-seo",
    #     "cat": "Sommeil",  # un des DOMAINS ci-dessous
    #     "title": "Titre de l'article",
    #     "description": "Meta description 140-160 caractères.",
    #     "date": "2026-09-19",
    #     "body": """<p>...</p><h2>...</h2>""",
    # },
    {
        "slug": "combien-heures-sommeil-par-nuit",
        "cat": "Sommeil",
        "title": "Combien d'heures de sommeil faut-il vraiment par nuit ?",
        "description": "7 à 9 heures pour la plupart des adultes — mais la vraie réponse dépend de toi. Ce que disent les données, et comment trouver ton besoin réel en deux semaines.",
        "date": "2026-09-19",
        "body": """
<p>La réponse courte : <strong>entre 7 et 9 heures</strong> pour la quasi-totalité des adultes. C'est la fourchette retenue par la National Sleep Foundation et par l'American Academy of Sleep Medicine, sur la base de centaines d'études. En dessous de 7 heures de façon répétée, les risques mesurables augmentent — métabolisme, immunité, humeur, accidents. Au-delà de 9 heures chez un adulte en bonne santé, c'est rarement un besoin : c'est souvent le signe d'une dette qui se rembourse, ou d'un sommeil de mauvaise qualité qui se compense en quantité.</p>
<p>La réponse honnête : <em>ça dépend de toi</em>, et la variation est plus grande qu'on ne le croit. Ton besoin réel est largement génétique. Certaines personnes fonctionnent parfaitement avec 7 heures. D'autres ont besoin de 9 heures pour être au même niveau. Les vrais « courts dormeurs » naturels — moins de 6 heures sans aucun déficit — existent, mais ils sont rarissimes : quelques personnes sur mille. Statistiquement, ce n'est pas toi.</p>

<h2>Pourquoi « 8 heures » est un malentendu</h2>
<p>Le chiffre de 8 heures n'est pas faux, il est mal compris. C'est une <strong>moyenne de population</strong>, pas une prescription individuelle. Dire « il faut dormir 8 heures » revient à dire « il faut chausser du 42 » : c'est vrai en moyenne et faux pour la moitié des gens.</p>
<p>Ce que la recherche montre de façon robuste, c'est la forme de la courbe : les risques pour la santé dessinent un U. Ils montent nettement sous 6 heures, restent bas entre 7 et 9, et remontent au-delà — probablement parce que dormir très longtemps est plus souvent un symptôme qu'une cause. Ta cible personnelle se trouve quelque part dans ce creux, et elle bouge selon les périodes de ta vie : charge d'entraînement, stress, maladie, sommeil en retard à rattraper.</p>

<h2>Si tu t'entraînes, vise le haut de la fourchette</h2>
<p>L'exercice augmente le besoin de sommeil, parce que c'est pendant la nuit que l'essentiel de la réparation se produit : sécrétion d'hormone de croissance en sommeil profond, synthèse protéique, consolidation des apprentissages moteurs.</p>
<p>Les études d'« extension de sommeil » chez les sportifs sont parlantes : quand des basketteurs universitaires sont passés à 10 heures au lit par nuit pendant plusieurs semaines, leurs sprints se sont améliorés, leur précision au tir a gagné environ 9 points de pourcentage, et leur temps de réaction a chuté. À l'inverse, une seule nuit courte dégrade la force maximale modestement — mais dégrade nettement l'endurance, la motivation et la tolérance à l'effort dès le lendemain.</p>
<ul>
<li><strong>Tu t'entraînes 3-4 fois par semaine :</strong> vise 7 h 30 – 8 h 30 de sommeil réel.</li>
<li><strong>Tu t'entraînes 5 fois ou plus, ou tu es en préparation :</strong> vise 8 – 9 heures, sieste comprise.</li>
<li><strong>Période de sèche ou de déficit calorique :</strong> le manque de sommeil fait fondre le muscle en priorité — dans une étude célèbre, à déficit égal, les participants qui dormaient 5 h 30 perdaient 60 % de masse maigre en plus que ceux qui dormaient 8 h 30.</li>
</ul>

<h2>Temps au lit ≠ temps de sommeil</h2>
<p>Détail qui change tout : ces chiffres parlent de <strong>sommeil réel</strong>, pas de temps passé au lit. Avec une efficacité de sommeil normale de 85-92 %, il faut environ 8 h 30 au lit pour dormir 7 h 45. Si tu te couches à minuit et te lèves à 7 h en croyant « dormir 7 heures », tu en dors probablement 6 h 15. C'est l'erreur de calcul la plus répandue — et elle suffit à créer une dette chronique invisible.</p>

<h2>Les signes que tu ne dors pas assez</h2>
<p>Ton corps répond à la question mieux qu'aucune règle générale. Les signaux fiables :</p>
<ul>
<li>Tu as <strong>besoin d'un réveil</strong> pour émerger, tous les jours, et il t'arrache au sommeil profond.</li>
<li>Tu dors <strong>1 h 30 de plus ou davantage le week-end</strong> : c'est une dette qui se rembourse, pas de la paresse.</li>
<li>Tu t'endors <strong>en moins de 5 minutes</strong> le soir — s'endormir instantanément n'est pas un talent, c'est un symptôme de privation.</li>
<li>Coup de barre marqué en début d'après-midi, café indispensable pour tenir la matinée, irritabilité sans raison claire.</li>
</ul>
<p>Aucun de ces signes isolé n'est une preuve. Les quatre ensemble, si.</p>

<h2>Trouver ton chiffre : le protocole des deux semaines</h2>
<p>La méthode la plus fiable ne demande aucun matériel, juste une période calme (vacances, ou deux semaines sans grosses échéances) :</p>
<ul>
<li>Couche-toi chaque soir à la même heure, choisie pour te laisser au moins 8 h 30 devant toi.</li>
<li><strong>Pas de réveil.</strong> Laisse ton corps se lever seul.</li>
<li>Ignore les premières nuits : tu rembourses d'abord ta dette, les durées seront gonflées.</li>
<li>Au bout de 10 à 14 jours, ta durée de réveil spontané se stabilise. <em>Ce chiffre-là est ton besoin réel.</em></li>
</ul>
<p>Ensuite, le travail consiste à protéger ce volume en semaine — et c'est là que la régularité des horaires compte presque autant que la durée elle-même : se coucher et se lever à heures fixes stabilise l'horloge circadienne, et améliore la qualité du sommeil à durée égale.</p>

<h2>Ce qu'il faut retenir</h2>
<ul>
<li>7 à 9 heures de <strong>sommeil réel</strong> pour presque tout le monde ; le haut de la fourchette si tu t'entraînes sérieusement.</li>
<li>« 8 heures » est une moyenne, pas ta prescription : ton besoin est personnel et se mesure.</li>
<li>Compte 30 à 60 minutes de plus au lit que ta cible de sommeil.</li>
<li>Réveil spontané, énergie stable en journée, pas de rattrapage massif le week-end : voilà à quoi ressemble un sommeil suffisant.</li>
</ul>
""",
    },
]

DOMAINS = ["Sommeil", "Readiness", "Sport", "Récupération", "Alimentation",
           "Charge", "Régularité", "Humeur", "Contexte", "Énergie"]

# ---------------------------------------------------------------------------

CSS = """:root{--gold:#D9A441;--gold-soft:#B07A2A;--ink:#F2EBDD;--muted:#9A8E77;--bg:#0B0A08;--card:#12100C;--line:rgba(242,235,221,.14);color-scheme:dark}
*{box-sizing:border-box;margin:0;padding:0}
body{font-family:-apple-system,BlinkMacSystemFont,"Segoe UI",sans-serif;background:var(--bg);color:var(--ink);line-height:1.75;font-weight:400;-webkit-font-smoothing:antialiased}
a{color:inherit}
.wrap{max-width:640px;margin:0 auto;padding:0 24px}
.wrap-wide{max-width:1080px;margin:0 auto;padding:0 24px}
.label{font-size:11px;letter-spacing:.35em;text-transform:uppercase;color:var(--muted);font-weight:400}
.label .gold{color:var(--gold)}
nav.site{display:flex;align-items:center;justify-content:space-between;max-width:1080px;margin:0 auto;padding:28px 24px}
nav.site .logo{font-size:16px;letter-spacing:.45em;text-transform:uppercase;color:var(--ink);font-weight:300;text-decoration:none}
nav.site .links{display:flex;gap:26px;font-size:11px;letter-spacing:.22em;text-transform:uppercase}
nav.site .links a{color:var(--muted);text-decoration:none;font-weight:400}
nav.site .links a.on{color:var(--ink)}
nav.site .links a:hover{color:var(--gold)}
@media(max-width:560px){nav.site{flex-direction:column;align-items:flex-start;gap:16px;padding:22px 24px}nav.site .links{gap:14px;font-size:10px;letter-spacing:.16em;flex-wrap:wrap}nav.site .logo{font-size:13px;letter-spacing:.35em}}
.display{font-weight:200;text-transform:uppercase;letter-spacing:-.01em;line-height:1.02}
.display .gold{color:var(--gold)}
.display .dim{color:var(--muted)}
.btn{display:inline-block;border:1px solid var(--line);color:var(--ink);text-decoration:none;
     padding:17px 36px;font-size:11.5px;font-weight:400;letter-spacing:.25em;text-transform:uppercase;
     transition:border-color .25s,color .25s;background:none;cursor:pointer}
.btn:hover{border-color:var(--gold);color:var(--gold)}
.btn.gold{border-color:var(--gold);color:var(--gold)}
.btn.gold:hover{background:var(--gold);color:#1C1710}
.hr{border:0;border-top:1px solid var(--line)}
/* ARTICLE */
article header{padding:64px 0 28px}
article header .label{display:block;margin-bottom:22px}
article h1{font-size:clamp(28px,5.4vw,44px);font-weight:200;text-transform:uppercase;letter-spacing:-.01em;line-height:1.08}
article .standfirst{color:var(--muted);font-size:16px;margin-top:20px;line-height:1.7}
article h2{font-size:13px;letter-spacing:.22em;text-transform:uppercase;font-weight:500;color:var(--gold);margin:44px 0 14px}
article p{margin:0 0 16px;font-size:16.5px;color:var(--ink)}
article ul{margin:0 0 16px 20px}
article li{margin-bottom:8px;font-size:16.5px}
article strong{font-weight:600}
article em{color:var(--gold);font-style:normal}
/* fin d'article : la beta comme recompense */
.reward{border-top:1px solid var(--line);border-bottom:1px solid var(--line);margin:64px 0 8px;padding:52px 0;text-align:center}
.reward .label{display:block;margin-bottom:20px}
.reward h2{font-size:clamp(20px,3.6vw,28px);font-weight:200;text-transform:uppercase;letter-spacing:0;color:var(--ink);margin:0 0 14px;line-height:1.2}
.reward p{color:var(--muted);font-size:15px;max-width:420px;margin:0 auto 28px}
.next{padding:40px 0 8px}
.next .label{display:block;margin-bottom:18px}
.next a{display:block;text-decoration:none;padding:16px 0;border-bottom:1px solid var(--line);font-weight:300;
        font-size:16px;text-transform:uppercase;letter-spacing:.02em;color:var(--ink)}
.next a:first-of-type{border-top:1px solid var(--line)}
.next a:hover{color:var(--gold)}
/* INDEX ARTICLES : liste editoriale */
.pagehead{padding:72px 0 24px}
.pagehead h1{font-size:clamp(34px,7vw,60px)}
.pagehead p{color:var(--muted);margin-top:22px;font-size:16px;max-width:480px}
.journal{margin:36px 0 0}
.journal a.entry{display:block;text-decoration:none;padding:30px 0;border-top:1px solid var(--line)}
.journal a.entry:last-child{border-bottom:1px solid var(--line)}
.journal .label{display:block;margin-bottom:12px}
.journal h2{font-size:clamp(19px,3.4vw,25px);font-weight:250;text-transform:uppercase;letter-spacing:.01em;color:var(--ink);line-height:1.25;transition:color .2s}
.journal a.entry:hover h2{color:var(--gold)}
.journal p.desc{color:var(--muted);font-size:14.5px;margin-top:10px;max-width:540px}
footer.site{border-top:1px solid var(--line);margin-top:96px;padding:40px 0 64px;text-align:center}
footer.site .flinks{font-size:11px;letter-spacing:.22em;text-transform:uppercase}
footer.site a{color:var(--muted);text-decoration:none}
footer.site a:hover{color:var(--gold)}
.disclaimer{max-width:520px;margin:22px auto 0;color:var(--muted);font-size:12.5px;line-height:1.7}
/* JOURNAL : compteurs, themes, citation */
.stats{display:flex;gap:56px;margin:44px 0 10px}
.stats .n{font-size:clamp(30px,5vw,44px);font-weight:200;line-height:1}
.stats .l{display:block;margin-top:10px}
.themes{margin:40px 0 8px}
.themes .label{display:block;margin-bottom:16px}
.themescroll{border:1px solid var(--line);max-height:264px;overflow-y:auto;overscroll-behavior:contain;
             scrollbar-width:thin;scrollbar-color:rgba(154,142,119,.4) transparent}
.themescroll::-webkit-scrollbar{width:4px}
.themescroll::-webkit-scrollbar-thumb{background:rgba(154,142,119,.4)}
.theme{display:flex;justify-content:space-between;align-items:center;width:100%;text-align:left;
       background:none;border:0;border-left:2px solid rgba(154,142,119,.45);color:var(--muted);
       height:52px;padding:0 18px;font-size:11.5px;letter-spacing:.25em;text-transform:uppercase;
       cursor:pointer;transition:color .2s,border-color .2s;font-family:inherit}
.theme+.theme{border-top:1px solid var(--line)}
.theme .count{font-size:13px;letter-spacing:0;font-weight:300}
.theme:hover{color:var(--ink)}
.theme.on{color:var(--ink);border-left-color:var(--gold)}
.quote{margin:54px 0 10px;text-align:left}
.quote p{font-size:clamp(17px,2.8vw,21px);font-weight:300;font-style:italic;color:var(--ink)}
.quote .label{display:block;margin-top:14px}
.entry .meta{display:block;margin-bottom:12px}
.entry .readmore{display:inline-block;margin-top:14px;font-size:10.5px;letter-spacing:.28em;text-transform:uppercase;color:var(--gold)}
.empty{border-top:1px solid var(--line);border-bottom:1px solid var(--line);padding:56px 0;text-align:center;color:var(--muted);font-size:15px}
"""

POSTHOG = """<script>
  var POSTHOG_KEY="%s";
  if(POSTHOG_KEY){!function(t,e){var o,n,p,r;e.__SV||(window.posthog=e,e._i=[],e.init=function(i,s,a){function g(t,e){var o=e.split(".");2==o.length&&(t=t[o[0]],e=o[1]),t[e]=function(){t.push([e].concat(Array.prototype.slice.call(arguments,0)))}}(p=t.createElement("script")).type="text/javascript",p.async=!0,p.src=s.api_host+"/static/array.js",(r=t.getElementsByTagName("script")[0]).parentNode.insertBefore(p,r);var u=e;for(void 0!==a?u=e[a]=[]:a="posthog",u.people=u.people||[],u.toString=function(t){var e="posthog";return"posthog"!==a&&(e+="."+a),t||(e+=" (stub)"),e},u.people.toString=function(){return u.toString(1)+".people (stub)"},o="capture identify alias people.set people.set_once set_config register register_once unregister opt_out_capturing has_opted_out_capturing opt_in_capturing reset".split(" "),n=0;n<o.length;n++)g(u,o[n]);e._i.push([i,s,a])},e.__SV=1)}(document,window.posthog||[]);posthog.init(POSTHOG_KEY,{api_host:"https://eu.i.posthog.com"});}
  function track(ev,props){if(window.posthog&&POSTHOG_KEY)posthog.capture(ev,props||{});}
</script>""" % POSTHOG_KEY

NAV = """<nav class="site">
  <a class="logo" href="/">Ecleptic</a>
  <div class="links">
    <a href="/" %(on_home)s>Accueil</a>
    <a href="/articles/" %(on_articles)s>Journal</a>
    <a href="/guide.html">Guide</a>
    <a href="/beta.html">La b&ecirc;ta</a>
  </div>
</nav>"""

FOOTER = """<footer class="site">
  <div class="wrap">
    <p class="flinks"><a href="/confidentialite.html">Confidentialit&eacute;</a> &nbsp;&middot;&nbsp; <a href="mailto:contact@ecleptic.app">Contact</a> &nbsp;&middot;&nbsp; <a href="/beta.html">La b&ecirc;ta</a></p>
    <p class="disclaimer">Ecleptic est une application de bien-&ecirc;tre. Ses contenus ne remplacent pas un avis m&eacute;dical et ne constituent pas un dispositif m&eacute;dical.</p>
  </div>
</footer>"""


def nav(section):
    return NAV % {
        "on_home": 'class="on"' if section == "home" else "",
        "on_articles": 'class="on"' if section == "articles" else "",
    }


def cat(a):
    return a.get("cat", "Journal")


MONTHS_FR = ["janvier", "février", "mars", "avril", "mai", "juin", "juillet",
             "août", "septembre", "octobre", "novembre", "décembre"]


def fr_date(iso):
    y, m, d = iso.split("-")
    return "%d %s %s" % (int(d), MONTHS_FR[int(m) - 1], y)


def read_min(a):
    import re
    words = len(re.sub(r"<[^>]+>", " ", a["body"]).split())
    return max(2, round(words / 220))


def article_page(a, others):
    url = "%s/articles/%s.html" % (SITE, a["slug"])
    more = "\n".join(
        '<a href="/articles/%s.html">%s</a>' % (o["slug"], html.escape(o["title"]))
        for o in others[:3]
    )
    jsonld = (
        '{"@context":"https://schema.org","@type":"Article","headline":%s,'
        '"description":%s,"datePublished":"%s","inLanguage":"fr",'
        '"author":{"@type":"Organization","name":"Ecleptic","url":"%s"},'
        '"publisher":{"@type":"Organization","name":"Ecleptic","url":"%s"},'
        '"mainEntityOfPage":"%s"}'
    ) % (
        __import__("json").dumps(a["title"], ensure_ascii=False),
        __import__("json").dumps(a["description"], ensure_ascii=False),
        a["date"], SITE, SITE, url,
    )
    return """<!doctype html>
<html lang="fr">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>%(title)s — Ecleptic</title>
<meta name="description" content="%(desc)s">
<link rel="canonical" href="%(url)s">
<meta property="og:title" content="%(title)s">
<meta property="og:description" content="%(desc)s">
<meta property="og:type" content="article">
<meta property="og:url" content="%(url)s">
<script type="application/ld+json">%(jsonld)s</script>
<link rel="stylesheet" href="/assets/site.css">
</head>
<body>
%(nav)s
<main class="wrap">
<article>
  <header>
    <span class="label"><span class="gold">%(cat)s</span> &nbsp;&middot;&nbsp; %(date)s &nbsp;&middot;&nbsp; %(mins)s min</span>
    <h1>%(title)s</h1>
    <p class="standfirst">%(desc)s</p>
  </header>
  %(body)s
  <div class="reward">
    <span class="label">Pour aller plus loin</span>
    <h2>Ce que cet article explique,<br>l'app le mesure chez toi.</h2>
    <p>Ecleptic croise ton sommeil, ton alimentation et ton entraînement en un seul score, chaque matin. La bêta iOS est ouverte à un petit cercle.</p>
    <a class="btn gold" href="/beta.html" onclick="track('article_cta_click',{article:'%(slug)s'})">Demander l'accès</a>
  </div>
  <div class="next">
    <span class="label">À lire ensuite</span>
%(more)s
  </div>
</article>
</main>
%(footer)s
%(posthog)s
<script>track('article_view',{article:'%(slug)s'});</script>
</body>
</html>
""" % {
        "title": html.escape(a["title"]), "desc": html.escape(a["description"], quote=True),
        "url": url, "jsonld": jsonld, "nav": nav("articles"), "date": fr_date(a["date"]),
        "cat": html.escape(cat(a)), "mins": read_min(a),
        "body": a["body"].strip(), "tf": TF_LINK, "slug": a["slug"], "more": more,
        "footer": FOOTER, "posthog": POSTHOG,
    }


def index_page():
    cards = "\n".join(
        """<a class="entry" href="/articles/%s.html" data-cat="%s">
  <span class="label meta"><span class="gold">%s</span> &nbsp;&middot;&nbsp; %s &nbsp;&middot;&nbsp; %s min</span>
  <h2>%s</h2>
  <p class="desc">%s</p>
  <span class="readmore">Lire l'article →</span>
</a>"""
        % (a["slug"], html.escape(cat(a)), html.escape(cat(a)), fr_date(a["date"]),
           read_min(a), html.escape(a["title"]), html.escape(a["description"]))
        for a in sorted(ARTICLES, key=lambda x: x["date"], reverse=True)
    )
    counts = {d: sum(1 for a in ARTICLES if cat(a) == d) for d in DOMAINS}
    themes = "\n".join(
        """<button class="theme" data-filter="%s"><span>%s</span><span class="count">%d</span></button>"""
        % (html.escape(d), html.escape(d), counts[d])
        for d in DOMAINS
    )
    empty = "" if ARTICLES else """<div class="empty">Les premiers textes sont en préparation.<br>La station ouvre bientôt son journal.</div>"""
    return """<!doctype html>
<html lang="fr">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>Le Journal de la station spatiale — Ecleptic</title>
<meta name="description" content="Sommeil, nutrition, entraînement, récupération : des articles courts, scientifiques et actionnables pour optimiser ta santé au quotidien.">
<link rel="canonical" href="%(site)s/articles/">
<meta property="og:title" content="Le Journal de la station spatiale — Ecleptic">
<meta property="og:description" content="Sommeil, nutrition, entraînement, récupération : des conseils scientifiques et actionnables.">
<meta property="og:type" content="website">
<link rel="stylesheet" href="/assets/site.css">
</head>
<body>
%(nav)s
<main class="wrap">
  <div class="pagehead">
    <span class="label">Journal de la station spatiale</span>
    <h1 class="display" style="margin-top:22px">Des jours<br>autrement<br><span class="gold">pensés</span>.</h1>
    <p>Des textes sur le sommeil, l'alimentation, l'entraînement et l'art de construire des journées qui méritent d'être vécues.</p>
    <div class="stats">
      <div><span class="n">%(narticles)d</span><span class="l label">Articles</span></div>
      <div><span class="n">%(nthemes)d</span><span class="l label">Thèmes</span></div>
    </div>
  </div>
  <div class="themes">
    <span class="label">Thèmes du journal</span>
    <div class="themescroll">
    <button class="theme on" data-filter="*"><span>Tout le journal</span><span class="count">%(narticles)d</span></button>
%(themes)s
    </div>
  </div>
  <div class="quote">
    <p>« Chaque décision que tu prends — de ce que tu manges à ce que tu fais de ta soirée — fait de toi qui tu seras demain. »</p>
    <span class="label">Chris Hadfield &nbsp;·&nbsp; Astronaute, commandant de l'ISS</span>
  </div>
  <div class="journal" id="entries">
%(cards)s
  </div>
%(empty)s
  <div class="reward" style="border-bottom:0">
    <span class="label">Et ensuite</span>
    <h2>Lire, c'est bien.<br>Mesurer, c'est mieux.</h2>
    <p>Tout ce que le journal explique, l'app le suit automatiquement, sur tes propres données. La bêta iOS est ouverte à un petit cercle.</p>
    <a class="btn gold" href="/beta.html" onclick="track('article_cta_click',{article:'index'})">Demander l'accès</a>
  </div>
</main>
%(footer)s
%(posthog)s
<script>
track('articles_index_view');
(function(){
  var btns = document.querySelectorAll('.theme');
  var entries = document.querySelectorAll('#entries .entry');
  btns.forEach(function(b){
    b.addEventListener('click', function(){
      btns.forEach(function(x){ x.classList.remove('on'); });
      b.classList.add('on');
      var f = b.getAttribute('data-filter');
      entries.forEach(function(e){
        e.style.display = (f === '*' || e.getAttribute('data-cat') === f) ? '' : 'none';
      });
      track('journal_theme_click', {theme: f});
    });
  });
})();
</script>
</body>
</html>
""" % {"site": SITE, "nav": nav("articles"), "cards": cards, "themes": themes,
       "empty": empty, "narticles": len(ARTICLES), "nthemes": len(DOMAINS),
       "footer": FOOTER, "posthog": POSTHOG}


def sitemap():
    urls = ["%s/" % SITE, "%s/beta.html" % SITE, "%s/guide.html" % SITE, "%s/articles/" % SITE]
    urls += ["%s/articles/%s.html" % (SITE, a["slug"]) for a in ARTICLES]
    items = "\n".join("  <url><loc>%s</loc></url>" % u for u in urls)
    return '<?xml version="1.0" encoding="UTF-8"?>\n<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">\n%s\n</urlset>\n' % items


def main():
    root = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    os.makedirs(os.path.join(root, "articles"), exist_ok=True)
    os.makedirs(os.path.join(root, "assets"), exist_ok=True)
    with open(os.path.join(root, "assets", "site.css"), "w") as f:
        f.write(CSS)
    for i, a in enumerate(ARTICLES):
        others = ARTICLES[i + 1:] + ARTICLES[:i]
        with open(os.path.join(root, "articles", a["slug"] + ".html"), "w") as f:
            f.write(article_page(a, others))
    with open(os.path.join(root, "articles", "index.html"), "w") as f:
        f.write(index_page())
    with open(os.path.join(root, "sitemap.xml"), "w") as f:
        f.write(sitemap())
    print("OK — %d articles + index + sitemap + css" % len(ARTICLES))


if __name__ == "__main__":
    main()
