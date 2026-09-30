#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Génère les pages articles + l'index /articles/ + sitemap.xml.

Pour ajouter un article : ajouter une entrée dans ARTICLES puis lancer
    python3 tools/build_articles.py
depuis la racine du repo landing, et commiter les fichiers générés.
"""
import os, html, re
from datetime import date

SITE = "https://ecleptic.health"
TF_LINK = "https://testflight.apple.com/join/H5CQgDa7"
POSTHOG_KEY = "phc_wzjqudiS3KH7MeMii8h6HmUR2onfQR5iasjhAs53AL2B"

# slug, title (H1 + <title>), description (meta), date ISO, body HTML
# Les articles vivent dans tools/satellites/*.py (liste ENTRIES, même format),
# y compris les 13 premiers (batch_0_piliers.py). Format d'une entrée :
#   slug, cat (un des DOMAINS), title, description (140-160 c.), date ISO,
#   body (HTML), faq [{q, a}] ×3, sources [{t, u}] ×3-6, updated (optionnel).
ARTICLES = []

# Satellites longue traîne : chargés depuis tools/satellites/*.py (chaque fichier
# expose une liste ENTRIES au meme format que ARTICLES). Garde ce fichier lisible
# et permet d'ajouter des lots sans toucher au coeur du generateur.
def _load_satellites():
    import glob as _glob, importlib.util as _ilu
    d = os.path.join(os.path.dirname(os.path.abspath(__file__)), "satellites")
    out = []
    for f in sorted(_glob.glob(os.path.join(d, "*.py"))):
        if os.path.basename(f).startswith("_"):
            continue
        spec = _ilu.spec_from_file_location(os.path.basename(f)[:-3], f)
        mod = _ilu.module_from_spec(spec)
        spec.loader.exec_module(mod)
        out.extend(getattr(mod, "ENTRIES", []))
    return out


ARTICLES = ARTICLES + _load_satellites()


# --- Publication programmée (drip) -----------------------------------------
# tools/schedule.py expose SCHEDULE = {slug: "AAAA-MM-JJ"} : la date à laquelle
# l'article devient public. Un article dont la date est dans le futur n'est PAS
# généré (ni page, ni index, ni sitemap) et les liens internes vers lui sont
# neutralisés — aucun lien mort possible. Le cron GitHub Actions rebuild chaque
# jour : l'article apparaît tout seul le jour venu. Les articles absents de
# SCHEDULE gardent leur propre "date" (publication immédiate — piliers, etc.).
def _load_schedule():
    p = os.path.join(os.path.dirname(os.path.abspath(__file__)), "schedule.py")
    if not os.path.exists(p):
        return {}
    import importlib.util as _ilu
    spec = _ilu.spec_from_file_location("_ecleptic_schedule", p)
    mod = _ilu.module_from_spec(spec)
    spec.loader.exec_module(mod)
    return dict(getattr(mod, "SCHEDULE", {}))


SCHEDULE = _load_schedule()
for _a in ARTICLES:
    if _a["slug"] in SCHEDULE:
        _a["date"] = SCHEDULE[_a["slug"]]  # la date programmée fait foi (byline + gating)

# Date de build : aujourd'hui, ou override ECLEPTIC_BUILD_DATE (tests / rejeu).
_bd = os.environ.get("ECLEPTIC_BUILD_DATE")
TODAY = date.fromisoformat(_bd) if _bd else date.today()

ARTICLES_ALL = ARTICLES  # corpus complet (y compris articles à venir)
ARTICLES = [a for a in ARTICLES_ALL if date.fromisoformat(a["date"]) <= TODAY]
LIVE_SLUGS = {a["slug"] for a in ARTICLES}


# --- La méthode (Science-Based) : pages moteurs et fiches ---------------------
# tools/methode/*.py exposent chacun PAGE (ou PAGES) : slug, kind ("moteur" |
# "fiche"), order, label (nom court), title (h1), seo_title, description,
# lead, body (HTML), refs (liste de textes), related (slugs méthode),
# journal (slugs d'articles, n'apparaissent qu'une fois publiés), faq, date.
# Publiées immédiatement (pas de drip) sous /methode/<slug>.html.
def _load_methode():
    import glob as _glob, importlib.util as _ilu
    d = os.path.join(os.path.dirname(os.path.abspath(__file__)), "methode")
    out = []
    for f in sorted(_glob.glob(os.path.join(d, "*.py"))):
        if os.path.basename(f).startswith("_"):
            continue
        spec = _ilu.spec_from_file_location("methode_" + os.path.basename(f)[:-3], f)
        mod = _ilu.module_from_spec(spec)
        spec.loader.exec_module(mod)
        out.extend(getattr(mod, "PAGES", []) or ([mod.PAGE] if hasattr(mod, "PAGE") else []))
    out.sort(key=lambda p: (0 if p["kind"] == "moteur" else 1, p.get("order", 99), p["slug"]))
    return out


METHODE = _load_methode()
METHODE_IDX = {p["slug"]: p for p in METHODE}


def neutralize_links(body):
    """Retire les hyperliens vers des articles pas encore publiés (garde le texte)."""
    def repl(m):
        return m.group(2) if m.group(1) not in LIVE_SLUGS else m.group(0)
    return re.sub(r'<a href="/articles/([a-z0-9-]+)\.html">(.*?)</a>', repl, body, flags=re.S)


DOMAINS = ["Sommeil", "Readiness", "Sport", "Récupération", "Alimentation",
           "Charge", "Régularité", "Humeur", "Contexte", "Énergie"]

# Pages thème du Journal (/articles/<slug>/) : une page indexable par domaine,
# avec une introduction propre, la liste des articles publiés du thème et les
# pages de la méthode liées. Une page qui n'a pas encore 2 articles en ligne
# sort en noindex et hors sitemap (elle bascule seule avec le drip).
THEMES = {
    "Sommeil": {
        "slug": "sommeil",
        "seo": "Sommeil : nos articles pour mieux dormir — Ecleptic",
        "desc": "Durée idéale, sommeil profond, café, écrans, réveils nocturnes : des articles courts et sourcés pour comprendre ton sommeil et mieux dormir dès ce soir.",
        "intro": "Le sommeil conditionne tout le reste : ta récupération, ton appétit, ton humeur, ta progression à l'entraînement. Ici, on répond aux vraies questions (combien d'heures il te faut, comment gagner du sommeil profond, à quelle heure couper le café, que faire quand tu te réveilles à 3 h du matin) avec des réponses directes, des chiffres issus de la recherche, et ce que tu peux changer dès ce soir.",
        "methode": ["besoin-de-sommeil", "readiness-score"],
    },
    "Readiness": {
        "slug": "readiness",
        "seo": "Readiness score, HRV et cœur au repos : nos articles — Ecleptic",
        "desc": "Score de préparation, fréquence cardiaque au repos, HRV basse, jours de repos : comment lire les signaux de ton corps chaque matin et décider si tu pousses.",
        "intro": "Chaque matin, ton corps envoie des signaux mesurables : ta variabilité cardiaque, ta fréquence cardiaque au repos, la qualité de ta nuit. Lus sur ta propre ligne de base, ils disent si tu peux pousser ou s'il vaut mieux lever le pied. Ces articles t'apprennent à les lire sans te tromper : ce qui est normal, ce qui doit alerter, et comment faire remonter ces chiffres durablement.",
        "methode": ["readiness-score", "variabilite-cardiaque", "frequence-cardiaque-repos", "ligne-de-base"],
    },
    "Sport": {
        "slug": "sport",
        "seo": "Sport et entraînement : progresser, nos articles — Ecleptic",
        "desc": "Séances par semaine, zone 2, VO₂max, répétitions, cardio ou musculation : des articles clairs et sourcés pour t'entraîner mieux, progresser et durer.",
        "intro": "Progresser ne demande pas de t'entraîner plus, mais mieux : la bonne fréquence, la bonne intensité, et assez de variété pour que ton corps s'adapte. Zone 2, VO₂max, nombre de séances, répétitions, cardio ou musculation : chaque article part d'une question concrète et y répond franchement, avec ce que dit la recherche et la façon de l'appliquer à ta semaine.",
        "methode": ["vo2max", "depense-energetique"],
    },
    "Récupération": {
        "slug": "recuperation",
        "seo": "Récupération sportive : nos articles — Ecleptic",
        "desc": "Courbatures, HRV, bain froid, sauna, étirements, massage : ce qui accélère vraiment la récupération après le sport, ce qui ne sert à rien, et pourquoi.",
        "intro": "Tu ne progresses pas pendant la séance, mais pendant la récupération qui la suit. Courbatures, bain froid, sauna, étirements, massage : autour de la récupération circulent beaucoup de promesses. On trie : ce qui accélère vraiment le retour à la forme, ce qui soulage sans changer grand-chose, et ce que ta variabilité cardiaque dit de l'état de ton corps.",
        "methode": ["variabilite-cardiaque", "vitaux"],
    },
    "Alimentation": {
        "slug": "alimentation",
        "seo": "Alimentation et nutrition sportive : nos articles — Ecleptic",
        "desc": "Calories, protéines, déficit calorique, créatine, hydratation, repas autour du sport : des repères chiffrés et sourcés pour bien manger selon ton objectif.",
        "intro": "Bien manger pour ton objectif tient en quelques repères solides : combien de calories, combien de protéines, quoi manger avant et après l'effort, combien boire. Ces articles te donnent les chiffres, tirés des bases officielles et de la recherche en nutrition, et la façon de les adapter à toi, sans régime miracle ni aliment interdit.",
        "methode": ["nutrition", "cibles", "depense-energetique"],
    },
    "Charge": {
        "slug": "charge",
        "seo": "Charge d'entraînement : doser tes séances — Ecleptic",
        "desc": "Surentraînement, surcharge progressive, repos entre les séries, RPE, semaine de décharge : doser ta charge d'entraînement pour progresser sans te blesser.",
        "intro": "La charge d'entraînement, c'est ce que tes séances demandent à ton corps, semaine après semaine. Trop peu, tu stagnes ; trop, tu t'épuises ou tu te blesses. Surcharge progressive, surentraînement, temps de repos, échelle d'effort perçu : ces articles t'aident à doser, à reconnaître les signaux d'alerte et à construire une progression qui dure.",
        "methode": ["readiness-score"],
    },
    "Régularité": {
        "slug": "regularite",
        "seo": "Régularité et habitudes : nos articles — Ecleptic",
        "desc": "Horaires de coucher, routine du soir, décalage horaire, habitudes qui durent : pourquoi la régularité compte autant que la durée, et comment la construire.",
        "intro": "Ton corps fonctionne sur une horloge. Te coucher, te lever, manger et t'entraîner à des heures régulières la garde bien réglée, et tout le reste en profite : sommeil, énergie, appétit. Ces articles expliquent pourquoi la régularité compte parfois plus que la durée, et comment la tenir malgré un décalage horaire, des horaires de nuit ou des semaines chargées.",
        "methode": ["besoin-de-sommeil", "ligne-de-base"],
    },
    "Humeur": {
        "slug": "humeur",
        "seo": "Stress, humeur et récupération : nos articles — Ecleptic",
        "desc": "Stress, anxiété, cortisol, cohérence cardiaque, irritabilité : ce que le mental fait à ta récupération, et les leviers simples qui aident vraiment au quotidien.",
        "intro": "Ton système nerveux ne fait pas la différence entre une semaine de rush au travail et une semaine de gros entraînement : le stress mental se paie aussi en récupération. Ces articles parlent de stress, d'anxiété, de cortisol et d'humeur, et des leviers simples qui aident, du sport à la respiration. Ils ne remplacent pas un professionnel : si tu traverses une période difficile, parles-en à ton médecin ; en cas de détresse, le 3114 répond jour et nuit.",
        "methode": ["variabilite-cardiaque"],
    },
    "Contexte": {
        "slug": "contexte",
        "seo": "Alcool, âge, cycle, chaleur : le contexte compte — Ecleptic",
        "desc": "Alcool, maladie, cycle menstruel, âge, tabac, chaleur, altitude : les facteurs qui changent ta récupération et tes performances, et comment t'y adapter.",
        "intro": "Les mêmes séances et les mêmes nuits ne donnent pas les mêmes résultats selon ton contexte : un verre la veille, une maladie qui couve, ton cycle, ton âge, la chaleur, l'altitude. Ces articles expliquent comment chacun de ces facteurs pèse sur ton corps, et comment ajuster ton entraînement et ta récupération au lieu de lutter contre.",
        "methode": ["temperature-poignet", "ligne-de-base"],
    },
    "Énergie": {
        "slug": "energie",
        "seo": "Fatigue et énergie : nos articles — Ecleptic",
        "desc": "Fatigue constante, coup de barre après manger, sieste, carence en fer, glycémie : comprendre d'où vient ta fatigue et retrouver une énergie stable toute la journée.",
        "intro": "Une fatigue qui dure a presque toujours une cause identifiable : des nuits trop courtes, des horaires irréguliers, des repas mal calés, un manque de fer, trop de charge. Ces articles t'aident à remonter la piste, du coup de barre de 14 h à la fatigue qui s'installe, et à retrouver une énergie stable. Si la fatigue persiste malgré tout, un bilan chez ton médecin s'impose.",
        "methode": ["besoin-de-sommeil", "depense-energetique"],
    },
}
THEME_MIN_INDEX = 2  # articles en ligne requis pour qu'une page thème soit indexable


def theme_url(d):
    return "/articles/%s/" % THEMES[d]["slug"]


# Auteur (E-E-A-T) : signature des articles et des pages de la méthode, page /a-propos.html.
AUTHOR = {
    "name": "Auguste Phily-Priou",
    "role": "fondateur d'Ecleptic",
    "url": SITE + "/a-propos.html",
    "instagram": "https://www.instagram.com/_optimisateur/",
}
AUTHOR_LD = {"@type": "Person", "@id": SITE + "/a-propos.html#auguste", "name": AUTHOR["name"],
             "jobTitle": "Fondateur d'Ecleptic", "url": AUTHOR["url"], "sameAs": [AUTHOR["instagram"]]}
PUBLISHER_LD = {"@type": "Organization", "@id": SITE + "/#organization", "name": "Ecleptic", "url": SITE + "/",
                "logo": {"@type": "ImageObject", "url": SITE + "/assets/icons/icon-512.png", "width": 512, "height": 512}}
ABOUT_UPDATED = "2026-09-30"   # date affichée et lastmod de /a-propos.html et /mentions-legales.html

# Titres Google (<title>) : Google coupe vers 60 caractères. Le suffixe « — Ecleptic »
# n'est ajouté que s'il tient ; au-delà de 60 sans suffixe, un titre court dédié.
SEO_TITLES = {
    "lumiere-bleue-ecrans-avant-de-dormir": "Écrans avant de dormir : la lumière bleue, vrai problème ?",
    "frequence-cardiaque-repos-elevee": "Fréquence cardiaque au repos élevée : les causes fréquentes",
    "manque-de-sommeil-irritabilite": "Manque de sommeil et irritabilité : pourquoi tu t'énerves",
    "sommeil-et-recuperation-musculaire": "Sommeil et récupération musculaire : tout se joue la nuit",
    "magnesium-sport-fatigue": "Magnésium : son rôle pour le sport, le sommeil et la fatigue",
    "rpe-echelle-effort-percu": "RPE : l'échelle d'effort perçu pour doser tes séances",
    "glucides-et-sport-combien": "Glucides et sport : combien en manger selon ta séance ?",
    "cafe-et-sommeil-combien-de-temps-avant": "Café : combien de temps avant de dormir faut-il l'arrêter ?",
    "sommeil-paradoxal-role": "Sommeil paradoxal : à quoi sert-il, comment en avoir plus ?",
    "cycle-menstruel-et-sport": "Cycle menstruel et sport : faut-il adapter l'entraînement ?",
}


def title_tag(t):
    """<title> : « t — Ecleptic » si ça tient dans 60 caractères, sinon t seul."""
    suffix = " — Ecleptic"
    if t.endswith(suffix):
        t = t[:-len(suffix)]
    return t + suffix if len(t) + len(suffix) <= 60 else t

# Classement « Les plus lus » (/articles/?sort=populaires).
# Actualisation automatique : `python3 tools/update_popular.py` interroge
# PostHog (article_view, 90 j) et écrit tools/popular.json, prioritaire sur
# la liste par défaut ci-dessous ; les slugs absents du json (articles trop
# récents) sont ajoutés à la suite, dans l'ordre par défaut.
POPULAR_DEFAULT = [
    "combien-heures-sommeil-par-nuit",
    "toujours-fatigue-causes",
    "proteines-par-jour-prise-de-muscle",
    "readiness-score-comment-ca-marche",
    "hrv-variabilite-frequence-cardiaque",
    "alcool-sommeil-effets",
    "combien-seances-sport-par-semaine",
    "surentrainement-signes",
    "se-coucher-meme-heure-regularite",
    "stress-recuperation-sport",
]


def load_popular():
    path = os.path.join(os.path.dirname(os.path.abspath(__file__)), "popular.json")
    order = []
    if os.path.exists(path):
        try:
            import json
            order = [s for s in json.load(open(path)) if isinstance(s, str)]
        except Exception:
            order = []
    known = {a["slug"] for a in ARTICLES}
    order = [s for s in order if s in known]
    return order + [s for s in POPULAR_DEFAULT if s not in order]


POPULAR = load_popular()

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
/* Mega-menu du bandeau (facon apple.com), construit par /assets/nav.js :
   panneau pleine largeur sous le bandeau, hauteur animee selon le contenu,
   page floutee derriere. Mobile (<=760px) : feuille plein ecran. */
nav.site{position:relative;z-index:80}
.mega{position:absolute;left:0;right:0;height:0;overflow:hidden;z-index:75;background:var(--bg);
      border-bottom:1px solid var(--line);visibility:hidden;
      transition:height .38s cubic-bezier(.4,0,.2,1),visibility 0s linear .38s}
.mega.open{visibility:visible;transition:height .38s cubic-bezier(.4,0,.2,1),visibility 0s}
.mega-in{max-width:1080px;margin:0 auto;padding:30px 24px 46px;display:grid;gap:56px;
         opacity:0;transform:translateY(-6px);transition:opacity .28s ease,transform .28s ease}
.mega-in.is-journal{grid-template-columns:210px minmax(0,1fr) 380px}
.mega-in.is-cols{grid-template-columns:minmax(0,1.25fr) minmax(0,1fr) minmax(0,1fr)}
.mega.open .mega-in{opacity:1;transform:none;transition-delay:.08s}
.mega.open .mega-in.swap-out{opacity:0;transform:none;transition:opacity .12s ease;transition-delay:0s}
.mega-label{display:block;font-size:10.5px;letter-spacing:.3em;text-transform:uppercase;color:var(--muted);margin-bottom:14px}
.mega ul,.mega ol{list-style:none}
.mega-cats a{display:flex;justify-content:space-between;align-items:baseline;gap:12px;padding:4px 0;
             font-size:17px;font-weight:300;color:var(--ink);text-decoration:none}
.mega-cats .k{font-size:10.5px;letter-spacing:.2em;color:var(--muted)}
.mega-cats li.on a,.mega-cats a:hover{color:var(--gold)}
.mega-all,.mega-more{display:inline-block;margin-top:18px;font-size:10.5px;letter-spacing:.24em;
                     text-transform:uppercase;color:var(--gold);text-decoration:none}
.mega-list li a,.mega-pop li a{display:block;padding:6px 0;font-size:13.5px;line-height:1.45;
                               color:var(--ink);text-decoration:none;opacity:.86}
.mega-list li a:hover,.mega-pop li a:hover{color:var(--gold);opacity:1}
.mega-list .soon{font-size:13.5px;color:var(--muted);padding:6px 0}
.mega-list.swap{animation:megaswap .28s ease}
@keyframes megaswap{from{opacity:0;transform:translateX(-4px)}to{opacity:1;transform:none}}
.mega-pop li a{display:grid;grid-template-columns:28px 1fr;padding:4px 0;font-size:13px}
.mega-pop .n{font-size:10.5px;letter-spacing:.15em;color:var(--gold);padding-top:2px}
.mega-shade{position:fixed;inset:0;z-index:70;background:rgba(11,10,8,.5);
            -webkit-backdrop-filter:blur(10px);backdrop-filter:blur(10px);
            opacity:0;visibility:hidden;transition:opacity .3s,visibility 0s linear .3s}
.mega-on .mega-shade{opacity:1;visibility:visible;transition:opacity .3s,visibility 0s}
.msheet{position:fixed;inset:0;z-index:90;background:var(--bg);overflow-y:auto;-webkit-overflow-scrolling:touch;
        transform:translateY(-100%);visibility:hidden;
        transition:transform .38s cubic-bezier(.4,0,.2,1),visibility 0s linear .38s}
.msheet.open{transform:none;visibility:visible;transition:transform .38s cubic-bezier(.4,0,.2,1),visibility 0s}
.msheet-on,.msheet-on body{overflow:hidden}
.msheet-top{position:sticky;top:0;display:flex;justify-content:space-between;align-items:center;
            padding:18px 24px;background:var(--bg);border-bottom:1px solid var(--line)}
.msheet-brand{font-size:12px;letter-spacing:.35em;text-transform:uppercase;font-weight:300}
.msheet-x{background:none;border:0;color:var(--ink);font-size:30px;line-height:1;cursor:pointer;padding:0 4px}
.msheet-body{padding:8px 24px 64px}
.msheet-all{display:block;padding:18px 0;font-size:11px;letter-spacing:.25em;text-transform:uppercase;
            color:var(--gold);text-decoration:none;border-bottom:1px solid var(--line)}
.msheet-label{margin:30px 0 4px}
.msheet details{border-bottom:1px solid var(--line)}
.msheet summary{list-style:none;display:flex;justify-content:space-between;align-items:baseline;
                padding:16px 0;font-size:18px;font-weight:300;cursor:pointer}
.msheet summary::-webkit-details-marker{display:none}
.msheet summary .k{font-size:11px;letter-spacing:.2em;color:var(--muted)}
.msheet details[open] summary{color:var(--gold)}
.msheet ul,.msheet ol{list-style:none;padding:0 0 14px}
.msheet li a{display:block;padding:8px 0;font-size:14.5px;line-height:1.45;color:var(--ink);text-decoration:none;opacity:.88}
.msheet li.more a{color:var(--gold);font-size:11px;letter-spacing:.22em;text-transform:uppercase}
.msheet ol{counter-reset:p}
.msheet ol li{counter-increment:p;display:grid;grid-template-columns:30px 1fr}
.msheet ol li::before{content:counter(p,decimal-leading-zero);font-size:10.5px;color:var(--gold);padding-top:11px;letter-spacing:.12em}
/* panneaux en colonnes (L'app, Science-Based, La beta) : grands liens + liens courts */
.mega-big li{margin:0 0 16px}
.mega-big a,.mega-big .txt{display:block;text-decoration:none}
.mega-big .t{display:block;font-size:19px;font-weight:300;line-height:1.3;color:var(--ink);transition:color .2s}
.mega-big .d{display:block;margin-top:4px;font-size:12.5px;line-height:1.5;color:var(--muted)}
.mega-big a:hover .t,.mega-big a.gold .t{color:var(--gold)}
.mega-small li a,.mega-small li .txt{display:block;padding:6px 0;font-size:13.5px;line-height:1.45;color:var(--ink);text-decoration:none;opacity:.86}
.mega-small li .txt{opacity:.72}
.mega-small li a:hover{color:var(--gold);opacity:1}
.mega-small li a.gold{color:var(--gold);opacity:1}
.mega-small .d{display:block;font-size:12px;color:var(--muted)}
.mega-spots{display:inline-block;margin-top:2px;padding:7px 12px;border:1px solid var(--gold);color:var(--gold);
            font-size:10.5px;letter-spacing:.2em;text-transform:uppercase}
.mega-apercu{position:fixed;left:16px;bottom:16px;z-index:95;padding:8px 12px;border:1px solid var(--gold);
             background:var(--bg);color:var(--gold);font-size:10.5px;letter-spacing:.2em;text-transform:uppercase;text-decoration:none}
@media(max-width:760px){.mega,.mega-shade{display:none}}
@media (prefers-reduced-motion:reduce){.mega,.mega-in,.msheet,.mega-shade{transition:none}.mega-list.swap{animation:none}}
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
article h2{font-size:13px;letter-spacing:.22em;text-transform:uppercase;font-weight:500;color:var(--gold);margin:52px 0 16px;padding-top:26px;position:relative}
article h2::before{content:"";position:absolute;top:0;left:6%;right:6%;border-top:1px solid var(--line)}
article p{margin:0 0 18px;font-size:16.5px;color:var(--ink);line-height:1.8}
article ul{margin:0 0 18px 22px}
article li{margin-bottom:11px;font-size:16.5px;line-height:1.75}
article li::marker{color:var(--gold)}
article strong{font-weight:600}
article em{color:var(--gold);font-style:normal}
article h1 .w{display:inline-block;white-space:nowrap}
article h1 .ch{display:inline-block;opacity:0;transform:translateY(.05em);transition:opacity .5s ease-out,transform .5s ease-out}
article h1 .ch.in{opacity:1;transform:none}
@media (prefers-reduced-motion:reduce){article h1 .ch{opacity:1;transform:none;transition:none}}
article .hero{margin:40px 0 10px}
article .hero img{width:100%;height:auto;display:block;border:1px solid var(--line);filter:saturate(.85) brightness(.92)}
/* FAQ : questions frequentes (balisees FAQPage en JSON-LD) */
article .faq h3{font-size:16.5px;font-weight:600;color:var(--ink);margin:26px 0 8px;line-height:1.4}
article .faq p{color:var(--muted);font-size:15.5px;margin-bottom:0}
/* fin d'article : la beta comme recompense */
.reward{margin:64px 0 8px;padding:52px 0;text-align:center;position:relative}
.reward::before{content:"";position:absolute;top:0;left:6%;right:6%;border-top:1px solid var(--line)}
.reward::after{content:"";position:absolute;bottom:0;left:6%;right:6%;border-top:1px solid var(--line)}
.reward.noafter::after{content:none}
.reward .label{display:block;margin-bottom:20px}
.reward h2{font-size:clamp(20px,3.6vw,28px);font-weight:200;text-transform:uppercase;letter-spacing:0;color:var(--ink);margin:0 0 14px;line-height:1.2}
.reward p{color:var(--muted);font-size:15px;max-width:420px;margin:0 auto 28px}
.next{padding:40px 0 8px}
.next .label{display:block;margin-bottom:18px}
.next a{display:block;text-decoration:none;padding:16px 0;font-weight:300;position:relative;
        font-size:16px;text-transform:uppercase;letter-spacing:.02em;color:var(--ink)}
.next a::after{content:"";position:absolute;bottom:0;left:6%;right:6%;border-top:1px solid var(--line)}
.next a:first-of-type::before{content:"";position:absolute;top:0;left:6%;right:6%;border-top:1px solid var(--line)}
.next a:hover{color:var(--gold)}
/* INDEX ARTICLES : liste editoriale */
.pagehead{padding:72px 0 24px}
.pagehead h1{font-size:clamp(34px,7vw,60px)}
.pagehead p{color:var(--muted);margin-top:22px;font-size:16px;max-width:480px}
.journal{margin:92px 0 0}
/* filets a 88 % de la largeur, centres (comme le cadre Derniers repas de l'app) */
.journal a.entry{display:flex;gap:32px;align-items:center;justify-content:space-between;text-decoration:none;padding:60px 0;position:relative}
.journal a.entry::before{content:"";position:absolute;top:0;left:6%;right:6%;border-top:1px solid var(--line)}
.journal a.entry:last-child::after{content:"";position:absolute;bottom:0;left:6%;right:6%;border-top:1px solid var(--line)}
.entry .etext{flex:1;min-width:0}
.entry .ethumb{flex:0 0 210px}
.entry .ethumb img{width:100%;height:auto;aspect-ratio:1.9;object-fit:cover;display:block;border:1px solid var(--line);filter:saturate(.85) brightness(.9);transition:filter .25s}
.journal a.entry:hover .ethumb img{filter:saturate(1) brightness(1)}
@media(max-width:640px){.journal a.entry{flex-direction:column-reverse;align-items:stretch;gap:18px}.entry .ethumb{flex:none}}
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
.themescroll{max-height:264px;overflow-y:auto;overscroll-behavior:contain;
             scrollbar-width:thin;scrollbar-color:rgba(154,142,119,.4) transparent}
.themescroll::-webkit-scrollbar{width:4px}
.themescroll::-webkit-scrollbar-thumb{background:rgba(154,142,119,.4)}
.theme{display:flex;justify-content:space-between;align-items:center;width:100%;text-align:left;
       background:none;border:0;border-left:2px solid rgba(154,142,119,.45);color:var(--muted);
       height:52px;padding:0 18px;font-size:11.5px;letter-spacing:.25em;text-transform:uppercase;
       cursor:pointer;transition:color .2s,border-color .2s;font-family:inherit}
.theme{position:relative}
.theme+.theme::after{content:"";position:absolute;top:0;left:6%;right:6%;border-top:1px solid var(--line)}
.theme .count{font-size:13px;letter-spacing:0;font-weight:300}
.theme:hover{color:var(--ink)}
.theme.on{color:var(--ink);border-left-color:var(--gold)}
.quote{margin:54px 0 10px;text-align:left}
.quote p{font-size:clamp(17px,2.8vw,21px);font-weight:300;font-style:italic;color:var(--ink)}
.quote .label{display:block;margin-top:14px}
.entry .meta{display:block;margin-bottom:12px}
.entry .readmore{display:inline-block;margin-top:14px;font-size:10.5px;letter-spacing:.28em;text-transform:uppercase;color:var(--gold)}
.empty{border-top:1px solid var(--line);border-bottom:1px solid var(--line);padding:56px 0;text-align:center;color:var(--muted);font-size:15px}
/* METHODE (Science-Based) : pages moteurs et fiches */
.crumbs{display:flex;flex-wrap:wrap;gap:10px;align-items:center;margin-bottom:26px;font-size:10.5px;letter-spacing:.25em;text-transform:uppercase;color:var(--muted)}
.crumbs a{color:var(--muted);text-decoration:none}
.crumbs a:hover{color:var(--gold)}
.methode p a,.methode li a{color:var(--ink);text-decoration:underline;text-decoration-color:rgba(217,164,65,.55);text-underline-offset:3px}
.methode p a:hover,.methode li a:hover{color:var(--gold)}
.methode .figs{display:grid;grid-template-columns:repeat(auto-fit,minmax(140px,1fr));gap:26px 22px;margin:34px 0 30px;padding:28px 0;position:relative}
.methode .figs::before,.methode .figs::after{content:"";position:absolute;left:6%;right:6%;border-top:1px solid var(--line)}
.methode .figs::before{top:0}
.methode .figs::after{bottom:0}
.methode .figs .v{display:block;font-size:clamp(34px,6vw,46px);font-weight:200;line-height:1;color:var(--gold);letter-spacing:-.02em}
.methode .figs .u{display:block;margin-top:10px;font-size:10.5px;letter-spacing:.22em;text-transform:uppercase;color:var(--muted);line-height:1.5}
.methode .refs ul{list-style:none;margin:0}
.methode .refs li{font-size:14px;color:var(--muted);margin-bottom:10px;line-height:1.6}
/* Signature (auteur), liens de catégorie, pages thème, À propos et mentions légales */
article .byline{margin-top:18px;font-size:13px;color:var(--muted);line-height:1.6}
article .byline a,.prose p a,.prose li a{color:var(--ink);text-decoration:underline;text-decoration-color:rgba(217,164,65,.55);text-underline-offset:3px}
article .byline a:hover,.prose p a:hover,.prose li a:hover{color:var(--gold)}
.label a{color:inherit;text-decoration:none}
article header .label a.gold{text-decoration:underline;text-decoration-color:rgba(217,164,65,.45);text-underline-offset:4px;text-decoration-thickness:1px}
.label a:hover{color:var(--gold)}
a.theme{text-decoration:none}
.pagehead .crumbs{margin-bottom:26px}
.prose h2{margin-top:44px}
.prose .updated{margin-top:44px;font-size:13px;color:var(--muted)}
/* Sources des articles + tableaux de données */
article .refs ol{margin:0 0 0 22px}
article .refs li{font-size:14px;color:var(--muted);margin-bottom:10px;line-height:1.6}
article .refs li::marker{color:var(--muted)}
article .refs a{color:var(--muted);text-decoration:underline;text-decoration-color:rgba(217,164,65,.45);text-underline-offset:3px;word-break:break-all}
article .refs a:hover{color:var(--gold)}
.tablewrap{overflow-x:auto;margin:6px 0 24px;-webkit-overflow-scrolling:touch}
article table{width:100%;border-collapse:collapse;font-size:15px;line-height:1.5}
article caption{caption-side:bottom;text-align:left;font-size:12.5px;color:var(--muted);padding-top:10px}
article th{font-size:10.5px;letter-spacing:.2em;text-transform:uppercase;font-weight:500;color:var(--gold);text-align:left;padding:10px 12px 10px 0;border-bottom:1px solid var(--line);white-space:nowrap}
article td{padding:11px 12px 11px 0;border-bottom:1px solid var(--line);vertical-align:top}
article td.n,article th.n{text-align:right;font-variant-numeric:tabular-nums;white-space:nowrap}
"""

# Visites venant d'un assistant IA (ChatGPT, Perplexity, Claude, Gemini, Copilot…) :
# événement PostHog « ai_referral » + propriété « first_ai_source » gardée sur la
# personne (attribue une inscription bêta à l'IA qui a amené le visiteur).
# Même bloc, recopié tel quel, dans index/science/beta/guide (pages écrites à la main).
AI_REFERRAL_JS = r"""  (function(){try{var r=(document.referrer||'').toLowerCase(),m=location.search.match(/[?&]utm_source=([^&#]+)/),u=m?decodeURIComponent(m[1]).toLowerCase():'',s=r+' '+u,src=/chatgpt|openai/.test(s)?'chatgpt':/perplexity/.test(s)?'perplexity':/claude\.ai|anthropic/.test(s)?'claude':/gemini\.google|bard\.google/.test(s)?'gemini':/copilot|bing\.com\/chat/.test(s)?'copilot':/chat\.mistral|mistral\.ai/.test(s)?'mistral':/you\.com/.test(s)?'you':/deepseek/.test(s)?'deepseek':/meta\.ai/.test(s)?'meta':'';if(src){if(window.posthog&&posthog.register_once)posthog.register_once({first_ai_source:src});track('ai_referral',{source:src,page:location.pathname});}}catch(e){}})();"""

POSTHOG = """<script>
  var POSTHOG_KEY="%s";
  if(POSTHOG_KEY){!function(t,e){var o,n,p,r;e.__SV||(window.posthog=e,e._i=[],e.init=function(i,s,a){function g(t,e){var o=e.split(".");2==o.length&&(t=t[o[0]],e=o[1]),t[e]=function(){t.push([e].concat(Array.prototype.slice.call(arguments,0)))}}(p=t.createElement("script")).type="text/javascript",p.async=!0,p.src=s.api_host+"/static/array.js",(r=t.getElementsByTagName("script")[0]).parentNode.insertBefore(p,r);var u=e;for(void 0!==a?u=e[a]=[]:a="posthog",u.people=u.people||[],u.toString=function(t){var e="posthog";return"posthog"!==a&&(e+="."+a),t||(e+=" (stub)"),e},u.people.toString=function(){return u.toString(1)+".people (stub)"},o="capture identify alias people.set people.set_once set_config register register_once unregister opt_out_capturing has_opted_out_capturing opt_in_capturing reset".split(" "),n=0;n<o.length;n++)g(u,o[n]);e._i.push([i,s,a])},e.__SV=1)}(document,window.posthog||[]);posthog.init(POSTHOG_KEY,{api_host:"https://eu.i.posthog.com",disable_surveys:true});}
  function track(ev,props){if(window.posthog&&POSTHOG_KEY)posthog.capture(ev,props||{});}
%s
</script>""" % (POSTHOG_KEY, AI_REFERRAL_JS)

# Pages indexables : extraits longs et grandes images autorisés (Google, AI Overviews, Bing).
META_ROBOTS = '<meta name="robots" content="index, follow, max-snippet:-1, max-image-preview:large, max-video-preview:-1">'

# Icônes (favicon Google, onglet, écran d'accueil iOS) : dans le <head> de chaque page.
HEAD_ICONS = """<link rel="icon" href="/favicon.ico" sizes="48x48">
<link rel="icon" href="/assets/icons/icon-192.png" type="image/png" sizes="192x192">
<link rel="apple-touch-icon" href="/apple-touch-icon.png">"""

CSP = """<meta http-equiv="Content-Security-Policy" content="default-src 'self'; script-src 'self' 'unsafe-inline' https://eu.i.posthog.com https://eu-assets.i.posthog.com; connect-src 'self' https://eu.i.posthog.com https://eu-assets.i.posthog.com https://avbmycfngmxhkjesdiyq.supabase.co; img-src 'self' data:; style-src 'self' 'unsafe-inline'; font-src 'self'; worker-src 'self' blob:; object-src 'none'; base-uri 'self'; form-action 'self'; upgrade-insecure-requests">"""


def og_image_tags(path):
    """og:image + carte Twitter/X grand format pour une image du site (chemin absolu /…)."""
    return ('<meta property="og:image" content="%s%s">\n'
            '<meta name="twitter:card" content="summary_large_image">\n'
            '<meta name="twitter:image" content="%s%s">' % (SITE, path, SITE, path))


def ld(obj):
    import json as _json
    return '<script type="application/ld+json">%s</script>' % _json.dumps(obj, ensure_ascii=False)


def byline(date_iso=None, updated_iso=None):
    """Signature visible : « Par Auguste Phily-Priou, fondateur d'Ecleptic · mis à jour le … »."""
    upd = ""
    if updated_iso and (not date_iso or updated_iso > date_iso):
        upd = " &nbsp;&middot;&nbsp; mis à jour le %s" % fr_date(updated_iso)
    return ('<p class="byline">Par <a href="/a-propos.html" rel="author">%s</a>, %s%s</p>'
            % (AUTHOR["name"], AUTHOR["role"], upd))


def modified(a):
    """Date de dernière modification : « updated » seulement s'il est postérieur à la
    publication (un article programmé relu avant sa sortie garde sa date de sortie)."""
    u = a.get("updated")
    return u if u and u > a["date"] else a["date"]


def sources_block(srcs):
    """Section « Sources » : références vérifiées (tools/check_sources.py), liens sortants."""
    if not srcs:
        return ""
    items = "\n".join('      <li>%s <a href="%s" rel="noopener" target="_blank">%s</a></li>'
                      % (s["t"], html.escape(s["u"], quote=True), html.escape(source_label(s["u"])))
                      for s in srcs)
    return '\n  <section class="refs">\n    <h2>Sources</h2>\n    <ol>\n%s\n    </ol>\n  </section>' % items


def source_label(u):
    """Libellé court du lien d'une source : doi:…, PubMed …, ou le domaine."""
    m = re.match(r"https?://(?:dx\.)?doi\.org/(.+)", u)
    if m:
        return "doi:" + m.group(1)
    m = re.match(r"https?://pubmed\.ncbi\.nlm\.nih\.gov/(\d+)", u)
    if m:
        return "PubMed " + m.group(1)
    return re.sub(r"^https?://(www\.)?", "", u).split("/")[0]


def citation_ld(srcs):
    return [{"@type": "CreativeWork", "name": html.unescape(re.sub(r"<[^>]+>", "", s["t"])), "url": s["u"]}
            for s in (srcs or [])]

def journal_menu():
    # Le panneau déroulant (méga-menu) est construit par /assets/nav.js à partir de
    # /assets/nav-data.js, écrit par nav_data() à chaque build.
    return """<span class="navjournal">
    <a href="/articles/" data-mega="journal" %(on_articles)s>Journal</a>
    </span>"""


# Scripts du méga-menu, à inclure en fin de <body> de chaque page qui a le bandeau.
NAV_SCRIPTS = """<script src="/assets/nav-data.js" defer></script>
<script src="/assets/nav.js" defer></script>"""


def nav_data():
    """Données du méga-menu Journal : articles publiés par thème (5 plus récents,
    le compteur garde le total) et les 5 plus lus. Déterministe : identique d'un build à l'autre tant
    qu'aucun article n'est publié (le cron ne commite rien les jours creux)."""
    import json as _json
    by_cat = {d: [] for d in DOMAINS}
    for a in sorted(ARTICLES, key=lambda a: a["date"], reverse=True):
        by_cat.setdefault(cat(a), []).append({"t": a["title"], "u": "/articles/%s.html" % a["slug"]})
    cats = [{"n": d, "u": theme_url(d), "c": len(by_cat[d]), "a": by_cat[d][:5]}
            for d in DOMAINS]
    idx = {a["slug"]: a for a in ARTICLES}
    pop = [{"t": idx[s]["title"], "u": "/articles/%s.html" % s} for s in POPULAR if s in idx][:5]
    data = {"journal": {"cats": cats, "popular": pop, "total": len(ARTICLES)}}
    data.update(nav_panels(idx))
    return ("/* Genere par tools/build_articles.py (nav_data) - ne pas editer a la main. */\n"
            "window.ECLEPTIC_NAV=%s;\n" % _json.dumps(data, ensure_ascii=False, separators=(",", ":")))


def nav_panels(idx):
    """Panneaux du bandeau hors Journal (L'app, Science-Based, La bêta) : trois
    colonnes chacun, la première en grands liens. Les articles cités ne sont
    retenus que s'ils sont publiés (idx = articles en ligne) ; les pages de la
    méthode que si elles existent (repli sur l'ancre de /science.html)."""
    def mp(slug, anchor):
        return "/methode/%s.html" % slug if slug in METHODE_IDX else "/science.html#" + anchor
    contact = {"t": "Nous écrire", "u": "mailto:contact@ecleptic.app"}
    fiches = [{"t": p["label"], "u": "/methode/%s.html" % p["slug"]} for p in METHODE if p["kind"] == "fiche"]
    science_cols = [
        {"label": "La méthode, moteur par moteur", "big": True,
         "more": {"t": "Toute la méthode →", "u": "/science.html"}, "items": [
            {"t": "Le Readiness Score", "d": "Quatre piliers croisés chaque matin.", "u": mp("readiness-score", "readiness")},
            {"t": "L'âge biologique", "d": "Ancré sur ta VO₂max et la cohorte HUNT.", "u": mp("age-biologique", "age-biologique")},
            {"t": "La nutrition", "d": "438 000 références issues des bases officielles.", "u": mp("nutrition", "nutrition")},
            {"t": "Les vitaux", "d": "Ta ligne de base, pas celle d'un autre.", "u": mp("vitaux", "vitaux")},
            {"t": "Les cibles", "d": "Un métabolisme mesuré, pas estimé.", "u": mp("cibles", "cibles")}]}]
    if fiches:
        science_cols.append({"label": "Les mesures, expliquées", "items": fiches})
    science_cols.append({"label": "Nos sources", "items": [
        {"t": "ANSES · table Ciqual", "u": mp("nutrition", "nutrition")},
        {"t": "USDA · FoodData Central", "u": mp("nutrition", "nutrition")},
        {"t": "Open Food Facts", "u": mp("nutrition", "nutrition")},
        {"t": "Cohorte HUNT (Norvège)", "u": mp("age-biologique", "age-biologique")},
        {"t": "Tables VDOT de Jack Daniels", "u": mp("age-biologique", "age-biologique")},
        {"t": "National Sleep Foundation", "u": mp("besoin-de-sommeil", "readiness")}]})
    return {
        "app": {"cols": [
            {"label": "L'app en trois temps", "big": True, "items": [
                {"t": "Mesurer", "d": "Ta nuit, tes vitaux, ta charge. Sans saisie.", "u": "/#mesurer"},
                {"t": "Comprendre", "d": "Sommeil, repas et séances, enfin croisés.", "u": "/#comprendre"},
                {"t": "Agir", "d": "Un chiffre, une direction, chaque matin.", "u": "/#agir"}]},
            {"label": "Ce qu'elle calcule pour toi", "items": [
                {"t": "Ton Readiness Score, chaque matin", "u": mp("readiness-score", "readiness")},
                {"t": "Ton âge biologique, dès le premier jour", "u": mp("age-biologique", "age-biologique")},
                {"t": "Tes repas, analysés en une photo", "u": mp("nutrition", "nutrition")},
                {"t": "Tes vitaux, lus sur ta ligne de base", "u": mp("vitaux", "vitaux")},
                {"t": "Tes cibles, recalibrées en continu", "u": mp("cibles", "cibles")}]},
            {"label": "Commencer", "items": [
                {"t": "Demander l'accès à la bêta", "u": "/beta.html", "gold": True},
                {"t": "Lire le Journal", "u": "/articles/"},
                {"t": "La méthode scientifique", "u": "/science.html"},
                contact]}]},
        "science": {"cols": science_cols},
        "beta": {"cols": [
            {"label": "Rejoindre la bêta", "big": True, "spots": True, "items": [
                {"t": "Demander l'accès", "d": "45 secondes de questions, puis le lien d'installation.",
                 "u": "/beta.html", "gold": True}]},
            {"label": "Ce qui t'attend", "items": [
                {"t": "Toutes les fonctionnalités Golden, offertes aux testeurs"},
                {"t": "Sur iPhone, iOS 16.4 ou plus récent"},
                {"t": "Installation via TestFlight, l'app de bêtas d'Apple"},
                {"t": "Un bug ? Une capture d'écran suffit à nous le signaler"}]},
            {"label": "Questions", "items": [
                {"t": "TestFlight, c'est quoi ?", "u": "https://testflight.apple.com/"},
                {"t": "Confidentialité", "u": "/confidentialite.html"},
                contact]}]},
    }


NAV = """<nav class="site">
  <a class="logo" href="/">Ecleptic</a>
  <div class="links">
    <a href="/" data-mega="app" %%(on_home)s>Accueil</a>
    %s
    <a href="/science.html" data-mega="science" %%(on_science)s>Science-Based</a>
    <a href="/beta.html" data-mega="beta">La b&ecirc;ta</a>
  </div>
</nav>"""
NAV = NAV % journal_menu()

FOOTER = """<footer class="site">
  <div class="wrap">
    <p class="flinks"><a href="/a-propos.html">&Agrave; propos</a> &nbsp;&middot;&nbsp; <a href="/mentions-legales.html">Mentions l&eacute;gales</a> &nbsp;&middot;&nbsp; <a href="/confidentialite.html">Confidentialit&eacute;</a> &nbsp;&middot;&nbsp; <a href="mailto:contact@ecleptic.app">Contact</a> &nbsp;&middot;&nbsp; <a href="/beta.html">La b&ecirc;ta</a></p>
    <p class="disclaimer">Ecleptic est une application de bien-&ecirc;tre. Ses contenus ne remplacent pas un avis m&eacute;dical et ne constituent pas un dispositif m&eacute;dical.</p>
  </div>
</footer>"""


def nav(section):
    return NAV % {
        "on_home": 'class="on"' if section == "home" else "",
        "on_articles": 'class="on"' if section == "articles" else "",
        "on_science": 'class="on"' if section == "science" else "",
    }


def cat(a):
    return a.get("cat", "Journal")


MONTHS_FR = ["janvier", "février", "mars", "avril", "mai", "juin", "juillet",
             "août", "septembre", "octobre", "novembre", "décembre"]


def fr_date(iso):
    y, m, d = iso.split("-")
    return "%d %s %s" % (int(d), MONTHS_FR[int(m) - 1], y)


def img_path(a):
    """Chemin web de l'image de l'article, ou None si elle n'existe pas.
    Convention : assets/articles/<slug>.jpg (1600x840)."""
    root = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    rel = "assets/articles/%s.jpg" % a["slug"]
    return "/" + rel if os.path.exists(os.path.join(root, rel)) else None


def img_srcset(a):
    """srcset de la photo : variantes 640/1200 (tools/image_variants.py) si elles
    existent, puis l'original 1600. Chaîne vide si l'article n'a pas de photo."""
    img = img_path(a)
    if not img:
        return ""
    root = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    parts = ["/assets/articles/%d/%s.jpg %dw" % (w, a["slug"], w) for w in (640, 1200)
             if os.path.exists(os.path.join(root, "assets", "articles", str(w), a["slug"] + ".jpg"))]
    return ", ".join(parts + ["%s 1600w" % img])


def thumb_img(a):
    """Vignette du Journal : 640 px par défaut (affichée en 210 px), 1200 px en
    pleine largeur sur mobile."""
    img = img_path(a)
    if not img:
        return ""
    return ('\n  <span class="ethumb"><img src="%s" srcset="%s" sizes="(max-width: 640px) calc(100vw - 48px), 210px" '
            'width="1600" height="840" alt="" loading="lazy" decoding="async"></span>'
            % (img, img_srcset(a)))


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
    img = img_path(a)
    og_image = ("\n" + og_image_tags(img)) if img else ""
    # Photo = élément LCP sur mobile : chargée en priorité, version adaptée à l'écran.
    hero = ('\n  <figure class="hero"><img src="%s" srcset="%s" sizes="(max-width: 640px) calc(100vw - 48px), 592px" '
            'alt="%s" width="1600" height="840" fetchpriority="high" decoding="async"></figure>'
            % (img, img_srcset(a), html.escape(a["title"], quote=True))) if img else ""
    # Titres « Préfixe : suite » : le préfixe (jusqu'aux deux-points inclus)
    # apparaît tel quel, la suite est animée caractère par caractère — même
    # animation que « s'aligne. » sur l'accueil (délais en i², 100→1100 ms,
    # translateY .05em). Les titres-questions simples ne sont PAS animés.
    # Script inline juste après le header = anti-flash (split avant le 1er paint).
    reveal = """
<script>
(function(){
  var h = document.querySelector('article h1');
  if (!h) return;
  var reduce = window.matchMedia && window.matchMedia('(prefers-reduced-motion: reduce)').matches;
  var BASE = 100, SPREAD = 1000, P = 2;
  var text = h.textContent.replace(/ ([?!:;\\u00bb])/g, '\\u00a0$1');
  var cut = text.indexOf(':') + 1;
  if (cut <= 0) return;
  var anim = Array.from(text.slice(cut));
  var denom = Math.max(1, anim.length - 1);
  h.setAttribute('aria-label', text);
  h.textContent = '';
  h.appendChild(document.createTextNode(text.slice(0, cut)));
  var spans = [], w = null, idx = 0;
  anim.forEach(function(c){
    if (c === ' '){ h.appendChild(document.createTextNode(' ')); w = null; idx++; return; }
    if (!w){ w = document.createElement('span'); w.className = 'w'; w.setAttribute('aria-hidden','true'); h.appendChild(w); }
    var s = document.createElement('span');
    s.className = 'ch';
    s.textContent = c;
    if (!reduce) s.style.transitionDelay = (BASE + SPREAD*Math.pow(idx/denom, P)).toFixed(0)+'ms';
    idx++; w.appendChild(s); spans.push(s);
  });
  if (reduce){ spans.forEach(function(s){ s.classList.add('in'); }); return; }
  requestAnimationFrame(function(){ requestAnimationFrame(function(){
    spans.forEach(function(s){ s.classList.add('in'); });
  });});
})();
</script>""" if " : " in a["title"] else ""
    # FAQ optionnelle : section visible + JSON-LD FAQPage (Google exige que le
    # contenu balise soit affiche sur la page).
    faq = a.get("faq") or []
    faqblock = ""
    faqjsonld = ""
    if faq:
        _json = __import__("json")
        faqblock = (
            '\n  <section class="faq">\n    <h2>Questions fréquentes</h2>\n'
            + "\n".join(
                "    <h3>%s</h3>\n    <p>%s</p>" % (html.escape(q["q"]), html.escape(q["a"]))
                for q in faq
            )
            + "\n  </section>"
        )
        faqjsonld = '\n<script type="application/ld+json">' + _json.dumps(
            {
                "@context": "https://schema.org",
                "@type": "FAQPage",
                "mainEntity": [
                    {
                        "@type": "Question",
                        "name": q["q"],
                        "acceptedAnswer": {"@type": "Answer", "text": q["a"]},
                    }
                    for q in faq
                ],
            },
            ensure_ascii=False,
        ) + "</script>"
    art = {"@context": "https://schema.org", "@type": "Article", "headline": a["title"],
           "description": a["description"]}
    if img:
        art["image"] = SITE + img
    art.update({"datePublished": a["date"], "dateModified": modified(a),
                "inLanguage": "fr", "author": AUTHOR_LD, "publisher": PUBLISHER_LD,
                "mainEntityOfPage": url})
    if a.get("sources"):
        art["citation"] = citation_ld(a["sources"])
    crumbs = {"@context": "https://schema.org", "@type": "BreadcrumbList", "itemListElement": [
        {"@type": "ListItem", "position": 1, "name": "Journal", "item": SITE + "/articles/"},
        {"@type": "ListItem", "position": 2, "name": cat(a), "item": SITE + theme_url(cat(a))},
        {"@type": "ListItem", "position": 3, "name": a["title"], "item": url}]} if cat(a) in THEMES else None
    jsonld = __import__("json").dumps([x for x in (art, crumbs) if x], ensure_ascii=False)
    catlink = ('<a class="gold" href="%s">%s</a>' % (theme_url(cat(a)), html.escape(cat(a)))
               if cat(a) in THEMES else '<span class="gold">%s</span>' % html.escape(cat(a)))
    return """<!doctype html>
<html lang="fr">
<head>
<meta charset="utf-8">
<meta http-equiv="Content-Security-Policy" content="default-src 'self'; script-src 'self' 'unsafe-inline' https://eu.i.posthog.com https://eu-assets.i.posthog.com; connect-src 'self' https://eu.i.posthog.com https://eu-assets.i.posthog.com https://avbmycfngmxhkjesdiyq.supabase.co; img-src 'self' data:; style-src 'self' 'unsafe-inline'; font-src 'self'; worker-src 'self' blob:; object-src 'none'; base-uri 'self'; form-action 'self'; upgrade-insecure-requests">
<meta name="referrer" content="strict-origin-when-cross-origin">
<meta name="viewport" content="width=device-width, initial-scale=1">
%(icons)s
%(metarobots)s
<title>%(seo)s</title>
<meta name="description" content="%(desc)s">
<link rel="canonical" href="%(url)s">
<meta property="og:title" content="%(title)s">
<meta property="og:description" content="%(desc)s">
<meta property="og:type" content="article">
<meta property="og:url" content="%(url)s">%(og_image)s
<script type="application/ld+json">%(jsonld)s</script>%(faqjsonld)s
<link rel="stylesheet" href="/assets/site.css">
</head>
<body>
%(nav)s
<main class="wrap">
<article>
  <header>
    <span class="label">%(catlink)s &nbsp;&middot;&nbsp; %(date)s &nbsp;&middot;&nbsp; %(mins)s min</span>
    <h1>%(title)s</h1>
    <p class="standfirst">%(desc)s</p>
    %(byline)s
  </header>%(reveal)s%(hero)s
  %(body)s%(faqblock)s%(sources)s
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
%(navscripts)s
</body>
</html>
""" % {
        "title": html.escape(a["title"]), "desc": html.escape(a["description"], quote=True),
        "seo": html.escape(title_tag(SEO_TITLES.get(a["slug"], a["title"]))),
        "icons": HEAD_ICONS, "metarobots": META_ROBOTS, "catlink": catlink, "byline": byline(a["date"], modified(a)), "sources": sources_block(a.get("sources")),
        "url": url, "jsonld": jsonld, "faqjsonld": faqjsonld, "faqblock": faqblock,
        "og_image": og_image, "hero": hero, "reveal": reveal,
        "nav": nav("articles"), "date": fr_date(a["date"]),
        "mins": read_min(a),
        "body": neutralize_links(a["body"].strip()), "tf": TF_LINK, "slug": a["slug"], "more": more,
        "footer": FOOTER, "posthog": POSTHOG, "navscripts": NAV_SCRIPTS,
    }


def methode_page(p):
    """Page de la méthode (moteur ou fiche) sous /methode/<slug>.html : même
    typographie que les articles, fil d'Ariane vers Science-Based, références,
    FAQ balisée, liens vers les autres pages de la méthode et le Journal."""
    import re as _re, json as _json
    url = "%s/methode/%s.html" % (SITE, p["slug"])
    body = neutralize_links(p["body"].strip())
    # Un lien vers une page de la méthode inexistante casse le build (jamais de 404).
    for target in _re.findall(r'href="/methode/([a-z0-9-]+)\.html"', body + p.get("lead", "")):
        if target not in METHODE_IDX:
            raise ValueError("lien méthode inconnu dans %s : %s" % (p["slug"], target))
    kicker = ("Moteur %s &nbsp;&middot;&nbsp; La méthode" % p["num"]) if p["kind"] == "moteur" \
        else "La mesure &nbsp;&middot;&nbsp; Fiche"
    refs = p.get("refs") or []
    refsblock = ('\n  <section class="refs">\n    <h2>Références</h2>\n    <ul>\n%s\n    </ul>\n  </section>'
                 % "\n".join("      <li>%s</li>" % r for r in refs)) if refs else ""
    faq = p.get("faq") or []
    faqblock = faqjsonld = ""
    if faq:
        faqblock = ('\n  <section class="faq">\n    <h2>Questions fréquentes</h2>\n'
                    + "\n".join("    <h3>%s</h3>\n    <p>%s</p>" % (html.escape(q["q"]), html.escape(q["a"])) for q in faq)
                    + "\n  </section>")
        faqjsonld = '\n<script type="application/ld+json">' + _json.dumps({
            "@context": "https://schema.org", "@type": "FAQPage",
            "mainEntity": [{"@type": "Question", "name": q["q"],
                            "acceptedAnswer": {"@type": "Answer", "text": q["a"]}} for q in faq],
        }, ensure_ascii=False) + "</script>"
    links = []
    for s in p.get("related", []):
        if s in METHODE_IDX and s != p["slug"]:
            q = METHODE_IDX[s]
            links.append('<a href="/methode/%s.html">%s</a>' % (s, html.escape(q["label"])))
    idx = {a["slug"]: a for a in ARTICLES}
    for s in p.get("journal", []):
        if s in idx:
            links.append('<a href="/articles/%s.html">%s</a>' % (s, html.escape(idx[s]["title"])))
    more = ('\n  <div class="next">\n    <span class="label">Pour aller plus loin</span>\n%s\n  </div>'
            % "\n".join(links[:6])) if links else ""
    jsonld = _json.dumps([
        {"@context": "https://schema.org", "@type": "TechArticle", "headline": p["title"],
         "description": p["description"], "datePublished": p["date"],
         "dateModified": p.get("updated", p["date"]), "inLanguage": "fr",
         "image": SITE + "/assets/science/file-d-etoiles-og.jpg",
         "author": AUTHOR_LD, "publisher": PUBLISHER_LD,
         "mainEntityOfPage": url},
        {"@context": "https://schema.org", "@type": "BreadcrumbList", "itemListElement": [
            {"@type": "ListItem", "position": 1, "name": "Accueil", "item": SITE + "/"},
            {"@type": "ListItem", "position": 2, "name": "Science-Based", "item": SITE + "/science.html"},
            {"@type": "ListItem", "position": 3, "name": p["label"], "item": url}]},
    ], ensure_ascii=False)
    return """<!doctype html>
<html lang="fr">
<head>
<meta charset="utf-8">
<meta http-equiv="Content-Security-Policy" content="default-src 'self'; script-src 'self' 'unsafe-inline' https://eu.i.posthog.com https://eu-assets.i.posthog.com; connect-src 'self' https://eu.i.posthog.com https://eu-assets.i.posthog.com https://avbmycfngmxhkjesdiyq.supabase.co; img-src 'self' data:; style-src 'self' 'unsafe-inline'; font-src 'self'; worker-src 'self' blob:; object-src 'none'; base-uri 'self'; form-action 'self'; upgrade-insecure-requests">
<meta name="referrer" content="strict-origin-when-cross-origin">
<meta name="viewport" content="width=device-width, initial-scale=1">
%(icons)s
%(metarobots)s
<title>%(seo)s</title>
<meta name="description" content="%(desc)s">
<link rel="canonical" href="%(url)s">
<meta property="og:title" content="%(title)s">
<meta property="og:description" content="%(desc)s">
<meta property="og:type" content="article">
<meta property="og:url" content="%(url)s">
%(ogimg)s
<script type="application/ld+json">%(jsonld)s</script>%(faqjsonld)s
<link rel="stylesheet" href="/assets/site.css">
</head>
<body>
%(nav)s
<main class="wrap">
<article class="methode">
  <header>
    <nav class="crumbs" aria-label="Fil d'Ariane"><a href="/science.html">Science-Based</a><span aria-hidden="true">/</span><span>%(label)s</span></nav>
    <span class="label"><span class="gold">%(kicker)s</span></span>
    <h1>%(title)s</h1>
    <p class="standfirst">%(lead)s</p>
    %(byline)s
  </header>
  %(body)s%(refsblock)s%(faqblock)s
  <div class="reward">
    <span class="label">La suite logique</span>
    <h2>Tu viens de lire la méthode.<br>L'app l'applique à toi.</h2>
    <p>Ecleptic croise ton sommeil, ton alimentation et ton entraînement en un seul score, chaque matin. La bêta iOS est ouverte à un petit cercle.</p>
    <a class="btn gold" href="/beta.html" onclick="track('methode_cta_click',{page:'%(slug)s'})">Demander l'accès</a>
  </div>%(more)s
</article>
</main>
%(footer)s
%(posthog)s
<script>track('methode_view',{page:'%(slug)s'});</script>
%(navscripts)s
</body>
</html>
""" % {
        "seo": html.escape(title_tag(p.get("seo_title") or p["title"])),
        "icons": HEAD_ICONS, "metarobots": META_ROBOTS, "ogimg": og_image_tags("/assets/science/file-d-etoiles-og.jpg"),
        "byline": byline(p["date"], p.get("updated")),
        "title": html.escape(p["title"]), "desc": html.escape(p["description"], quote=True),
        "url": url, "site": SITE, "jsonld": jsonld, "faqjsonld": faqjsonld,
        "nav": nav("science"), "label": html.escape(p["label"]), "kicker": kicker,
        "lead": p["lead"].strip(), "body": body, "refsblock": refsblock, "faqblock": faqblock,
        "slug": p["slug"], "more": more, "footer": FOOTER, "posthog": POSTHOG, "navscripts": NAV_SCRIPTS,
    }


def entry_card(a):
    """Carte d'article du Journal (index et pages thème)."""
    return """<a class="entry" href="/articles/%s.html" data-slug="%s" data-cat="%s">
  <span class="etext">
  <span class="label meta"><span class="gold">%s</span> &nbsp;&middot;&nbsp; %s &nbsp;&middot;&nbsp; %s min</span>
  <h2>%s</h2>
  <p class="desc">%s</p>
  <span class="readmore">Lire l'article →</span>
  </span>%s
</a>""" % (a["slug"], a["slug"], html.escape(cat(a)), html.escape(cat(a)), fr_date(a["date"]),
           read_min(a), html.escape(a["title"]), html.escape(a["description"]), thumb_img(a))


def index_page():
    cards = "\n".join(entry_card(a) for a in sorted(ARTICLES, key=lambda x: x["date"], reverse=True))
    counts = {d: sum(1 for a in ARTICLES if cat(a) == d) for d in DOMAINS}
    # Liens réels vers les pages thème (explorables par Google) ; au clic, le
    # Journal filtre sur place comme avant (JS plus bas).
    themes = "\n".join(
        """<a class="theme" href="%s" data-filter="%s"><span>%s</span><span class="count">%d</span></a>"""
        % (theme_url(d), html.escape(d), html.escape(d), counts[d])
        for d in DOMAINS
    )
    empty = "" if ARTICLES else """<div class="empty">Les premiers textes sont en préparation.<br>La station ouvre bientôt son journal.</div>"""
    return """<!doctype html>
<html lang="fr">
<head>
<meta charset="utf-8">
<meta http-equiv="Content-Security-Policy" content="default-src 'self'; script-src 'self' 'unsafe-inline' https://eu.i.posthog.com https://eu-assets.i.posthog.com; connect-src 'self' https://eu.i.posthog.com https://eu-assets.i.posthog.com https://avbmycfngmxhkjesdiyq.supabase.co; img-src 'self' data:; style-src 'self' 'unsafe-inline'; font-src 'self'; worker-src 'self' blob:; object-src 'none'; base-uri 'self'; form-action 'self'; upgrade-insecure-requests">
<meta name="referrer" content="strict-origin-when-cross-origin">
<meta name="viewport" content="width=device-width, initial-scale=1">
%(icons)s
%(metarobots)s
<title>Le Journal : sommeil, nutrition, sport — Ecleptic</title>
<meta name="description" content="Sommeil, nutrition, entraînement, récupération : des articles courts, scientifiques et actionnables pour optimiser ta santé au quotidien.">
<link rel="canonical" href="%(site)s/articles/">
<meta property="og:title" content="Le Journal : sommeil, nutrition, sport — Ecleptic">
<meta property="og:description" content="Sommeil, nutrition, entraînement, récupération : des conseils scientifiques et actionnables.">
<meta property="og:type" content="website">
<meta property="og:url" content="%(site)s/articles/">
%(ogimg)s
%(jsonld)s
<link rel="stylesheet" href="/assets/site.css">
</head>
<body>
%(nav)s
<main class="wrap">
  <div class="pagehead">
    <span class="label">Journal de l'ISS</span>
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
    <a class="theme on" href="/articles/" data-filter="*"><span>Tout le journal</span><span class="count">%(narticles)d</span></a>
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
  <div class="reward noafter">
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
  function applyFilter(f){
    btns.forEach(function(x){ x.classList.toggle('on', x.getAttribute('data-filter') === f); });
    entries.forEach(function(e){
      e.style.display = (f === '*' || e.getAttribute('data-cat') === f) ? '' : 'none';
    });
  }
  btns.forEach(function(b){
    b.addEventListener('click', function(e){
      e.preventDefault();
      applyFilter(b.getAttribute('data-filter'));
      track('journal_theme_click', {theme: b.getAttribute('data-filter')});
    });
  });
  // Parametres d'URL (menu Journal de la nav) :
  //   ?theme=Sommeil    -> filtre active
  //   ?sort=populaires  -> reordonne selon POPULAR (sinon : plus recent -> plus ancien)
  var POPULAR = %(popular)s;
  try {
    var q = new URLSearchParams(location.search);
    var theme = q.get('theme');
    if (theme) applyFilter(theme);
    if (q.get('sort') === 'populaires'){
      var list = document.getElementById('entries');
      Array.from(entries)
        .sort(function(a, b){
          return POPULAR.indexOf(a.getAttribute('data-slug')) - POPULAR.indexOf(b.getAttribute('data-slug'));
        })
        .forEach(function(e){ list.appendChild(e); });
      track('journal_sort_popular');
    }
  } catch(_) {}
})();
</script>
<script src="/assets/nav-data.js" defer></script>
<script src="/assets/nav.js" defer></script>
</body>
</html>
""" % {"site": SITE, "nav": nav("articles"), "cards": cards, "themes": themes,
       "icons": HEAD_ICONS, "metarobots": META_ROBOTS, "ogimg": og_image_tags("/assets/og/journal.jpg"),
       "jsonld": ld({"@context": "https://schema.org", "@type": "CollectionPage",
                     "name": "Le Journal d'Ecleptic", "url": SITE + "/articles/", "inLanguage": "fr",
                     "description": "Sommeil, nutrition, entraînement, récupération : des articles courts, scientifiques et actionnables.",
                     "publisher": PUBLISHER_LD}),
       "empty": empty, "narticles": len(ARTICLES), "nthemes": len(DOMAINS),
       "popular": __import__("json").dumps(POPULAR),
       "footer": FOOTER, "posthog": POSTHOG}


def theme_articles(d):
    return sorted([a for a in ARTICLES if cat(a) == d], key=lambda x: x["date"], reverse=True)


def theme_page(d):
    """Page thème /articles/<slug>/ : introduction, articles publiés du thème,
    pages de la méthode liées, autres thèmes. noindex tant que < THEME_MIN_INDEX."""
    t = THEMES[d]
    url = SITE + theme_url(d)
    arts = theme_articles(d)
    robots = META_ROBOTS if len(arts) >= THEME_MIN_INDEX else '<meta name="robots" content="noindex, follow">'
    cards = "\n".join(entry_card(a) for a in arts)
    empty = "" if arts else '<div class="empty">Les premiers textes de ce thème arrivent bientôt.</div>'
    og = (img_path(arts[0]) if arts else None) or "/assets/og/journal.jpg"
    methode = [METHODE_IDX[s] for s in t["methode"] if s in METHODE_IDX]
    mblock = ('\n  <div class="next">\n    <span class="label">La méthode, côté app</span>\n%s\n  </div>'
              % "\n".join('<a href="/methode/%s.html">%s</a>' % (p["slug"], html.escape(p["label"])) for p in methode)
              ) if methode else ""
    others = "\n".join('<a href="%s">%s</a>' % (theme_url(o), html.escape(o)) for o in DOMAINS if o != d)
    jsonld = [
        {"@context": "https://schema.org", "@type": "CollectionPage", "name": "%s — Le Journal d'Ecleptic" % d,
         "description": t["desc"], "url": url, "inLanguage": "fr", "publisher": PUBLISHER_LD,
         "mainEntity": {"@type": "ItemList", "itemListElement": [
             {"@type": "ListItem", "position": i + 1, "url": "%s/articles/%s.html" % (SITE, a["slug"])}
             for i, a in enumerate(arts)]}},
        {"@context": "https://schema.org", "@type": "BreadcrumbList", "itemListElement": [
            {"@type": "ListItem", "position": 1, "name": "Journal", "item": SITE + "/articles/"},
            {"@type": "ListItem", "position": 2, "name": d, "item": url}]},
    ]
    n = len(arts)
    return """<!doctype html>
<html lang="fr">
<head>
<meta charset="utf-8">
%(csp)s
<meta name="referrer" content="strict-origin-when-cross-origin">
<meta name="viewport" content="width=device-width, initial-scale=1">
%(icons)s
%(metarobots)s
<title>%(seo)s</title>
<meta name="description" content="%(desc)s">
<link rel="canonical" href="%(url)s">
<meta property="og:title" content="%(seo)s">
<meta property="og:description" content="%(desc)s">
<meta property="og:type" content="website">
<meta property="og:url" content="%(url)s">
%(ogimg)s
%(jsonld)s
<link rel="stylesheet" href="/assets/site.css">
</head>
<body>
%(nav)s
<main class="wrap">
  <div class="pagehead">
    <nav class="crumbs" aria-label="Fil d'Ariane"><a href="/articles/">Journal</a><span aria-hidden="true">/</span><span>%(name)s</span></nav>
    <span class="label">Le Journal &nbsp;&middot;&nbsp; Thème</span>
    <h1 class="display" style="margin-top:22px">%(name)s<span class="gold">.</span></h1>
    <p>%(intro)s</p>
    <div class="stats">
      <div><span class="n">%(n)d</span><span class="l label">%(nlabel)s</span></div>
    </div>
  </div>
  <div class="journal">
%(cards)s
  </div>
%(empty)s%(mblock)s
  <div class="next">
    <span class="label">Les autres thèmes</span>
%(others)s
  </div>
  <div class="reward noafter">
    <span class="label">Et ensuite</span>
    <h2>Lire, c'est bien.<br>Mesurer, c'est mieux.</h2>
    <p>Tout ce que le journal explique, l'app le suit automatiquement, sur tes propres données. La bêta iOS est ouverte à un petit cercle.</p>
    <a class="btn gold" href="/beta.html" onclick="track('article_cta_click',{article:'theme-%(slug)s'})">Demander l'accès</a>
  </div>
</main>
%(footer)s
%(posthog)s
<script>track('journal_theme_view',{theme:'%(slug)s'});</script>
%(navscripts)s
</body>
</html>
""" % {"csp": CSP, "metarobots": robots, "icons": HEAD_ICONS, "seo": html.escape(title_tag(t["seo"])),
       "desc": html.escape(t["desc"], quote=True), "url": url, "ogimg": og_image_tags(og),
       "jsonld": ld(jsonld), "nav": nav("articles"), "name": html.escape(d), "intro": html.escape(t["intro"]),
       "n": n, "nlabel": "Article" if n == 1 else "Articles", "cards": cards, "empty": empty,
       "mblock": mblock, "others": others, "slug": t["slug"], "footer": FOOTER, "posthog": POSTHOG,
       "navscripts": NAV_SCRIPTS}


def prose_page(path, seo, desc, label, h1, body, jsonld, og, track_event):
    """Page de texte simple (À propos, mentions légales) : même typographie que les articles."""
    url = SITE + "/" + path
    return """<!doctype html>
<html lang="fr">
<head>
<meta charset="utf-8">
%(csp)s
<meta name="referrer" content="strict-origin-when-cross-origin">
<meta name="viewport" content="width=device-width, initial-scale=1">
%(icons)s
%(metarobots)s
<title>%(seo)s</title>
<meta name="description" content="%(desc)s">
<link rel="canonical" href="%(url)s">
<meta property="og:title" content="%(seo)s">
<meta property="og:description" content="%(desc)s">
<meta property="og:type" content="website">
<meta property="og:url" content="%(url)s">
%(ogimg)s
%(jsonld)s
<link rel="stylesheet" href="/assets/site.css">
</head>
<body>
%(nav)s
<main class="wrap">
<article class="prose">
  <header>
    <span class="label">%(label)s</span>
    <h1>%(h1)s</h1>
  </header>
%(body)s
  <p class="updated">Dernière mise à jour : %(updated)s</p>
</article>
</main>
%(footer)s
%(posthog)s
<script>track('%(track)s');</script>
%(navscripts)s
</body>
</html>
""" % {"csp": CSP, "icons": HEAD_ICONS, "metarobots": META_ROBOTS, "seo": html.escape(seo), "desc": html.escape(desc, quote=True),
       "url": url, "ogimg": og_image_tags(og), "jsonld": ld(jsonld), "nav": nav(""), "label": label,
       "h1": h1, "body": body.strip(), "updated": fr_date(ABOUT_UPDATED), "footer": FOOTER,
       "posthog": POSTHOG, "track": track_event, "navscripts": NAV_SCRIPTS}


def about_page():
    body = """
  <h2>Auguste Phily-Priou, fondateur</h2>
  <p>Je m'appelle Auguste, j'ai 27 ans, et je construis Ecleptic quasiment seul. Je ne suis pas médecin : je suis quelqu'un qui a repris sa santé en main, et qui a voulu comprendre ce qui marche vraiment.</p>
  <p>J'ai fumé pendant onze ans, de 14 à 25 ans, et j'ai arrêté fin 2024. En 2025, j'ai repris le sport de façon régulière, sans chercher l'intensité, j'ai appris à mieux manger, et j'ai commencé à optimiser à peu près tous les aspects de ma vie. C'est de là que vient mon pseudo sur Instagram, <a href="%(ig)s" rel="me noopener" target="_blank">@_optimisateur</a>.</p>
  <p>Ecleptic est né de cette démarche : relier ce qui est d'habitude suivi séparément, le sommeil, l'alimentation et l'entraînement, pour comprendre comment chacun agit sur les autres, et savoir chaque matin ce qui compte vraiment.</p>

  <h2>Comment les articles sont écrits</h2>
  <ul>
  <li><strong>Une vraie question, une réponse directe.</strong> Chaque article part d'une question que les gens se posent vraiment, et y répond dès la première phrase.</li>
  <li><strong>Des chiffres sourcés.</strong> Les repères viennent de sources publiées : sociétés savantes (National Sleep Foundation, American Academy of Sleep Medicine…), études et méta-analyses, bases officielles comme la table Ciqual de l'ANSES ou FoodData Central de l'USDA. Les pages de <a href="/science.html">la méthode</a> listent leurs références.</li>
  <li><strong>Des garde-fous santé.</strong> Aucun diagnostic, aucune posologie. Dès qu'un sujet devient médical (cœur, carences, santé mentale, grossesse), l'article renvoie vers un professionnel de santé.</li>
  <li><strong>Des mises à jour datées.</strong> Quand un article change sur le fond, sa date de mise à jour s'affiche sous le titre.</li>
  </ul>
  <p>Une erreur, une étude plus récente, un point à préciser ? Écris-moi à <a href="mailto:contact@ecleptic.app">contact@ecleptic.app</a> : je vérifie, je corrige, et la correction est datée.</p>

  <h2>Ecleptic en bref</h2>
  <p>Ecleptic est une application iOS de bien-être, en bêta privée. Elle croise ton sommeil, ton alimentation et ton entraînement en un seul score, chaque matin. Elle ne remplace pas un avis médical et n'est pas un dispositif médical. L'éditeur et l'hébergeur du site sont indiqués dans les <a href="/mentions-legales.html">mentions légales</a>.</p>
""" % {"ig": AUTHOR["instagram"]}
    person = dict(AUTHOR_LD, worksFor={"@id": PUBLISHER_LD["@id"]})
    jsonld = {"@context": "https://schema.org", "@type": "AboutPage", "url": SITE + "/a-propos.html",
              "name": "À propos d'Ecleptic", "inLanguage": "fr", "mainEntity": person,
              "publisher": PUBLISHER_LD}
    return prose_page("a-propos.html", "À propos : qui écrit sur Ecleptic — Ecleptic",
                      "Auguste Phily-Priou, fondateur d'Ecleptic : son parcours, pourquoi il construit l'app, et comment les articles du Journal sont écrits, sourcés et mis à jour.",
                      "À propos", "Qui écrit<br><span class=\"gold\">ici</span>.", body, jsonld,
                      "/assets/og/accueil.jpg", "about_view")


def legal_page():
    body = """
  <h2>Éditeur du site</h2>
  <p>Le site ecleptic.health est édité par <strong>Auguste Phily-Priou</strong>, entrepreneur individuel (EI).<br>
  Adresse : 10 Rue du Commerce, 86400 Civray, France<br>
  E-mail : <a href="mailto:contact@ecleptic.app">contact@ecleptic.app</a><br>
  SIREN : immatriculation en cours, le numéro sera ajouté ici dès son obtention.</p>

  <h2>Directeur de la publication</h2>
  <p>Auguste Phily-Priou.</p>

  <h2>Hébergement</h2>
  <p>GitHub, Inc. (service GitHub Pages), 88 Colin P. Kelly Jr. Street, San Francisco, CA 94107, États-Unis — <a href="https://github.com" rel="noopener" target="_blank">github.com</a>.</p>

  <h2>Propriété intellectuelle</h2>
  <p>« Ecleptic » fait l'objet d'un dépôt de marque de l'Union européenne auprès de l'EUIPO (demande nº 019418299, déposée le 4 septembre 2026). Les textes du site sont la propriété de l'éditeur : toute reproduction sans autorisation est interdite. Les photographies d'illustration proviennent pour la plupart d'<a href="https://unsplash.com" rel="noopener" target="_blank">Unsplash</a>, sous licence Unsplash.</p>

  <h2>Données personnelles</h2>
  <p>Le site mesure son audience avec PostHog, sur des serveurs situés dans l'Union européenne. Le traitement des données de l'application est décrit dans la <a href="/confidentialite.html">politique de confidentialité</a>.</p>

  <h2>Avertissement santé</h2>
  <p>Les contenus du site sont informatifs. Ils ne remplacent pas un avis médical, un diagnostic ou un traitement. Ecleptic est une application de bien-être, pas un dispositif médical.</p>

  <h2>Contact</h2>
  <p><a href="mailto:contact@ecleptic.app">contact@ecleptic.app</a></p>
"""
    jsonld = {"@context": "https://schema.org", "@type": "WebPage", "url": SITE + "/mentions-legales.html",
              "name": "Mentions légales", "inLanguage": "fr", "publisher": PUBLISHER_LD}
    return prose_page("mentions-legales.html", "Mentions légales — Ecleptic",
                      "Mentions légales du site ecleptic.health : éditeur, directeur de la publication, hébergeur, propriété intellectuelle et contact.",
                      "Informations légales", "Mentions légales", body, jsonld,
                      "/assets/og/accueil.jpg", "legal_view")


def html_to_md(h):
    """HTML maison des articles → Markdown lisible (llms-full.txt)."""
    h = neutralize_links(h)
    h = re.sub(r'<a href="(/[^"]*)"[^>]*>(.*?)</a>', lambda m: "[%s](%s%s)" % (m.group(2), SITE, m.group(1)), h, flags=re.S)
    h = re.sub(r'<a href="(https?://[^"]*)"[^>]*>(.*?)</a>', r"[\2](\1)", h, flags=re.S)
    h = re.sub(r"<h2[^>]*>(.*?)</h2>", r"\n## \1\n", h, flags=re.S)
    h = re.sub(r"<h3[^>]*>(.*?)</h3>", r"\n### \1\n", h, flags=re.S)
    h = re.sub(r"<(strong|b)>(.*?)</\1>", r"**\2**", h, flags=re.S)
    h = re.sub(r"<em>(.*?)</em>", r"*\1*", h, flags=re.S)
    h = re.sub(r"<li[^>]*>(.*?)</li>", r"- \1\n", h, flags=re.S)
    h = re.sub(r"<tr[^>]*>(.*?)</tr>", lambda m: "| " + " | ".join(
        c.strip() for c in re.findall(r"<t[hd][^>]*>(.*?)</t[hd]>", m.group(1), re.S)) + " |\n", h, flags=re.S)
    h = re.sub(r"</p>|<br\s*/?>", "\n", h)
    h = re.sub(r"<[^>]+>", "", h)
    h = html.unescape(h)
    return re.sub(r"\n{3,}", "\n\n", h).strip()


LLMS_INTRO = """# Ecleptic

> Ecleptic est une application iOS de bien-être qui croise le sommeil, l'alimentation et l'entraînement en un seul score quotidien, le Readiness Score. Ce site publie la méthode de calcul de l'application (formules, cohortes et bases de données citées) et le Journal, des articles sourcés qui répondent aux questions les plus posées sur le sommeil, la nutrition, l'entraînement et la récupération.

- Auteur et éditeur : Auguste Phily-Priou, fondateur d'Ecleptic ({site}/a-propos.html)
- Langue : français
- Les contenus sont informatifs : ils ne remplacent pas un avis médical, et Ecleptic n'est pas un dispositif médical.
- Citation : merci de citer la page utilisée et de lier son URL.
"""


def llms_txt():
    """/llms.txt (format llmstxt.org) : sommaire du site pour les assistants IA."""
    out = [LLMS_INTRO.format(site=SITE)]
    out.append("## La méthode : comment l'application calcule\n")
    out += ["- [%s](%s/methode/%s.html): %s" % (p["title"], SITE, p["slug"], p["description"]) for p in METHODE]
    out.append("\n## Le Journal\n")
    out.append("- [Tous les articles](%s/articles/): articles courts et sourcés, classés par thème." % SITE)
    for d in DOMAINS:
        arts = theme_articles(d)
        if not arts:
            continue
        out.append("\n### %s\n" % d)
        out.append("- [Thème %s](%s%s): %s" % (d, SITE, theme_url(d), THEMES[d]["desc"]))
        out += ["- [%s](%s/articles/%s.html): %s" % (a["title"], SITE, a["slug"], a["description"]) for a in arts]
    out.append("\n## À propos\n")
    out.append("- [À propos](%s/a-propos.html): qui écrit, comment les articles sont sourcés et mis à jour." % SITE)
    out.append("- [Science-Based](%s/science.html): vue d'ensemble de la méthode et des sources." % SITE)
    out.append("- [Mentions légales](%s/mentions-legales.html)" % SITE)
    out.append("\n## Optional\n")
    out.append("- [Texte intégral du site](%s/llms-full.txt): tous les articles et pages de la méthode en Markdown." % SITE)
    return "\n".join(out) + "\n"


def llms_full():
    """/llms-full.txt : texte intégral (Markdown) des pages de la méthode et des articles publiés."""
    parts = [LLMS_INTRO.format(site=SITE)]
    for p in METHODE:
        parts.append("\n---\n\n# %s\n\nURL : %s/methode/%s.html\nAuteur : %s · Publié le %s\n\n%s\n\n%s" % (
            p["title"], SITE, p["slug"], AUTHOR["name"], p["date"], html_to_md(p["lead"]), html_to_md(p["body"])))
        if p.get("refs"):
            parts.append("\n## Références\n\n" + "\n".join("- " + html_to_md(r) for r in p["refs"]))
    for a in sorted(ARTICLES, key=lambda x: x["date"], reverse=True):
        upd = modified(a) if modified(a) != a["date"] else None
        parts.append("\n---\n\n# %s\n\nURL : %s/articles/%s.html\nThème : %s · Auteur : %s · Publié le %s%s\n\n%s\n\n%s" % (
            a["title"], SITE, a["slug"], cat(a), AUTHOR["name"], a["date"],
            " · Mis à jour le %s" % upd if upd else "", a["description"], html_to_md(a["body"])))
        if a.get("faq"):
            parts.append("\n## Questions fréquentes\n\n" + "\n\n".join("### %s\n\n%s" % (q["q"], q["a"]) for q in a["faq"]))
        if a.get("sources"):
            parts.append("\n## Sources\n\n" + "\n".join("- %s — %s" % (html_to_md(x["t"]), x["u"]) for x in a["sources"]))
    return "\n".join(parts) + "\n"


def git_lastmod(rel):
    """Date (YYYY-MM-DD) du dernier commit touchant `rel`, ou None."""
    try:
        import subprocess
        root = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
        out = subprocess.run(
            ["git", "-C", root, "log", "-1", "--format=%cs", "--", rel],
            capture_output=True, text=True, timeout=5,
        ).stdout.strip()
        return out or None
    except Exception:
        return None


def sitemap():
    # Pages statiques : lastmod = dernier commit git du fichier.
    # Articles : cle "updated" si presente, sinon "date".
    entries = [("%s/" % SITE, git_lastmod("index.html")),
               ("%s/beta.html" % SITE, git_lastmod("beta.html")),
               ("%s/science.html" % SITE, git_lastmod("science.html")),
               ("%s/articles/" % SITE, git_lastmod("articles/index.html"))]
    entries += [("%s/articles/%s.html" % (SITE, a["slug"]), modified(a))
                for a in ARTICLES]
    entries += [("%s/methode/%s.html" % (SITE, p["slug"]), p.get("updated", p["date"]))
                for p in METHODE]
    # Pages thème indexables (>= THEME_MIN_INDEX articles) : lastmod = article le plus récent.
    for d in DOMAINS:
        arts = theme_articles(d)
        if len(arts) >= THEME_MIN_INDEX:
            entries.append((SITE + theme_url(d), max(modified(a) for a in arts)))
    entries.append(("%s/a-propos.html" % SITE, ABOUT_UPDATED))
    items = "\n".join(
        "  <url><loc>%s</loc>%s</url>" % (u, "<lastmod>%s</lastmod>" % d if d else "")
        for u, d in entries
    )
    return '<?xml version="1.0" encoding="UTF-8"?>\n<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">\n%s\n</urlset>\n' % items


def main():
    root = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    unknown = [s for s in SEO_TITLES if s not in {a["slug"] for a in ARTICLES_ALL}]
    if unknown:
        raise ValueError("SEO_TITLES : slugs inconnus %s" % unknown)
    if set(THEMES) != set(DOMAINS):
        raise ValueError("THEMES doit couvrir exactement DOMAINS")
    os.makedirs(os.path.join(root, "articles"), exist_ok=True)
    os.makedirs(os.path.join(root, "assets"), exist_ok=True)
    with open(os.path.join(root, "assets", "site.css"), "w") as f:
        f.write(CSS)
    adir = os.path.join(root, "articles")
    # Purge les pages d'articles qui ne sont plus publiés (repassés en programmé,
    # ou slug renommé) : sinon l'ancien HTML resterait servable et indexable.
    live_files = {a["slug"] + ".html" for a in ARTICLES} | {"index.html"}
    for fn in os.listdir(adir):
        if fn.endswith(".html") and fn not in live_files:
            os.remove(os.path.join(adir, fn))
    for i, a in enumerate(ARTICLES):
        others = ARTICLES[i + 1:] + ARTICLES[:i]
        with open(os.path.join(adir, a["slug"] + ".html"), "w") as f:
            f.write(article_page(a, others))
    with open(os.path.join(adir, "index.html"), "w") as f:
        f.write(index_page())
    with open(os.path.join(root, "sitemap.xml"), "w") as f:
        f.write(sitemap())
    mdir = os.path.join(root, "methode")
    os.makedirs(mdir, exist_ok=True)
    keep = {p["slug"] + ".html" for p in METHODE}
    for fn in os.listdir(mdir):
        if fn.endswith(".html") and fn not in keep:
            os.remove(os.path.join(mdir, fn))
    for p in METHODE:
        with open(os.path.join(mdir, p["slug"] + ".html"), "w") as f:
            f.write(methode_page(p))
    for d in DOMAINS:
        tdir = os.path.join(adir, THEMES[d]["slug"])
        os.makedirs(tdir, exist_ok=True)
        with open(os.path.join(tdir, "index.html"), "w") as f:
            f.write(theme_page(d))
    with open(os.path.join(root, "a-propos.html"), "w") as f:
        f.write(about_page())
    with open(os.path.join(root, "mentions-legales.html"), "w") as f:
        f.write(legal_page())
    with open(os.path.join(root, "llms.txt"), "w") as f:
        f.write(llms_txt())
    with open(os.path.join(root, "llms-full.txt"), "w") as f:
        f.write(llms_full())
    with open(os.path.join(root, "assets", "nav-data.js"), "w") as f:
        f.write(nav_data())
    scheduled = len(ARTICLES_ALL) - len(ARTICLES)
    print("OK — %d articles publiés (%d programmés à venir) + index + sitemap + css + menu"
          % (len(ARTICLES), scheduled))


if __name__ == "__main__":
    main()
