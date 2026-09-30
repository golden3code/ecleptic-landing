#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Génère les pages articles + l'index /articles/ + sitemap.xml.

Pour ajouter un article : ajouter une entrée dans ARTICLES puis lancer
    python3 tools/build_articles.py
depuis la racine du repo landing, et commiter les fichiers générés.
"""
import os, html, re, sys
from datetime import date

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import i18n as I  # noqa: E402  (site bilingue : textes, chemins, routage)

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
ARTICLE_IDX = {a["slug"]: a for a in ARTICLES_ALL}


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
THEME_BY_SLUG = {t["slug"]: d for d, t in THEMES.items()}


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
nav.site .langsw{display:inline-flex;gap:10px;padding-left:18px;border-left:1px solid var(--line)}
nav.site .langsw a{color:var(--muted)}
nav.site .langsw a.on{color:var(--gold)}
@media(max-width:560px){nav.site .langsw{padding-left:12px}nav.site{flex-direction:column;align-items:flex-start;gap:16px;padding:22px 24px}nav.site .links{gap:14px;font-size:10px;letter-spacing:.16em;flex-wrap:wrap}nav.site .logo{font-size:13px;letter-spacing:.35em}}
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
@media(max-width:640px){article .grp{display:none}article.data th,article.data td{font-size:14px}article.data th{white-space:normal;letter-spacing:.12em}}
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



def modified(a):
    """Date de dernière modification : « updated » seulement s'il est postérieur à la
    publication (un article programmé relu avant sa sortie garde sa date de sortie)."""
    u = a.get("updated")
    return u if u and u > a["date"] else a["date"]



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

# ============================================================================
# Site bilingue (tools/i18n.py) : chemins, vues par langue, bandeau, pied de page
# ============================================================================

def U(lang, key):
    return I.UI[lang][key]


def theme_name(d, lang):
    return d if lang == "fr" else I.THEMES_EN[d]["name"]


def theme_path(d, lang="fr"):
    return ("/articles/%s/" % THEMES[d]["slug"]) if lang == "fr" else ("/en/journal/%s/" % I.THEMES_EN[d]["slug"])


def en_entry(a):
    return I.EN_ARTICLES.get(a["slug"])


def article_path(a, lang):
    if lang == "fr":
        return "/articles/%s.html" % a["slug"]
    e = en_entry(a)
    return ("/en/journal/%s.html" % e["slug"]) if e else None


def methode_path(p, lang):
    if lang == "fr":
        return "/methode/%s.html" % p["slug"]
    e = I.EN_METHODE.get(p["slug"])
    return ("/en/method/%s.html" % e["slug"]) if e else None


def live_articles(lang):
    return ARTICLES if lang == "fr" else [a for a in ARTICLES if en_entry(a)]


def journal_path(lang):
    return "/articles/" if lang == "fr" else "/en/journal/"


def home_path(lang):
    return "/" if lang == "fr" else "/en/"


def localize_href(href, lang):
    """Lien interne écrit en chemin français → chemin de la langue demandée.
    Renvoie None si la cible n'existe pas (pas encore publiée ou pas traduite)."""
    m = re.match(r"^/articles/([a-z0-9-]+)\.html(#.*)?$", href)
    if m:
        a = ARTICLE_IDX.get(m.group(1))
        if not a or a["slug"] not in LIVE_SLUGS:
            return None
        p = article_path(a, lang)
        return (p + (m.group(2) or "")) if p else None
    m = re.match(r"^/methode/([a-z0-9-]+)\.html(#.*)?$", href)
    if m:
        p = METHODE_IDX.get(m.group(1))
        q = methode_path(p, lang) if p else None
        return (q + (m.group(2) or "")) if q else None
    m = re.match(r"^/articles/([a-z0-9-]+)/$", href)
    if m:
        d = THEME_BY_SLUG.get(m.group(1))
        return theme_path(d, lang) if d else None
    m = re.match(r"^/donnees/([a-z0-9-]+)\.html$", href)
    if m:
        return data_path(m.group(1)[len("aliments-riches-en-"):], lang) if m.group(1).startswith("aliments-riches-en-") else None
    base, _, frag = href.partition("#")
    if lang == "en" and base in I.STATIC:
        return I.STATIC[base] + ("#" + frag if frag else "")
    return href


def localize_links(body, lang):
    """Réécrit les liens internes du corps (chemins français) ; retire le lien et garde
    le texte quand la cible n'existe pas dans cette langue."""
    def repl(m):
        target = localize_href(m.group(1), lang)
        return '<a href="%s"%s>%s</a>' % (target, m.group(2), m.group(3)) if target else m.group(3)
    return re.sub(r'<a href="(/[^"]*)"([^>]*)>(.*?)</a>', repl, body, flags=re.S)


def article_view(a, lang):
    """Article prêt à rendre dans une langue (le slug français reste la clé des photos)."""
    if lang == "fr":
        return dict(a, path=article_path(a, "fr"), cat_name=cat(a), lang="fr",
                    seo=SEO_TITLES.get(a["slug"], a["title"]), body=localize_links(a["body"].strip(), "fr"))
    e = en_entry(a)
    v = dict(a)
    v.update({"title": e["title"], "description": e["description"], "faq": e.get("faq") or [],
              "sources": e.get("sources") or a.get("sources"), "seo": e.get("seo_title") or e["title"],
              "path": article_path(a, "en"), "cat_name": theme_name(cat(a), "en"), "lang": "en",
              "body": localize_links(e["body"].strip(), "en"),
              "updated": e.get("updated") or a.get("updated")})
    return v


def methode_view(p, lang):
    if lang == "fr":
        return dict(p, path=methode_path(p, "fr"), lang="fr")
    e = I.EN_METHODE[p["slug"]]
    v = dict(p)
    for k in ("title", "seo_title", "description", "lead", "body", "refs", "faq", "label", "updated"):
        if k in e:
            v[k] = e[k]
    v.update({"path": methode_path(p, "en"), "lang": "en"})
    return v


def head_i18n(fr_path, en_path):
    """hreflang + routage par pays, à placer en fin de <head>. Rien n'est annoncé
    tant que la version anglaise n'est pas générée (jamais de hreflang vers une 404)."""
    if "en" not in LANGS_BUILT():
        en_path = None
    alt = I.alt_links(fr_path, en_path, SITE)
    return (alt + "\n" + I.ROUTER_JS) if alt else I.ROUTER_JS


def nav_scripts(lang="fr"):
    return """<script src="/assets/%s" defer></script>
<script src="/assets/nav.js" defer></script>""" % ("nav-data.js" if lang == "fr" else "nav-data-en.js")


NAV_SCRIPTS = nav_scripts("fr")


def nav(section, lang="fr", fr_path=None, en_path=None):
    return """<nav class="site">
  <a class="logo" href="%(home)s">Ecleptic</a>
  <div class="links">
    <a href="%(home)s" data-mega="app" %(on_home)s>%(l_home)s</a>
    <span class="navjournal">
    <a href="%(journal)s" data-mega="journal" %(on_articles)s>%(l_journal)s</a>
    </span>
    <a href="%(science)s" data-mega="science" %(on_science)s>Science-Based</a>
    <a href="/beta.html" data-mega="beta">%(l_beta)s</a>
    %(switch)s
  </div>
</nav>""" % {
        "home": home_path(lang), "journal": journal_path(lang),
        "science": "/science.html" if lang == "fr" else "/en/science.html",
        "on_home": 'class="on"' if section == "home" else "",
        "on_articles": 'class="on"' if section == "articles" else "",
        "on_science": 'class="on"' if section == "science" else "",
        "l_home": U(lang, "nav_home"), "l_journal": U(lang, "nav_journal"), "l_beta": U(lang, "nav_beta"),
        "switch": I.switcher(lang, fr_path, en_path) if "en" in LANGS_BUILT() else "",
    }


def footer(lang="fr"):
    p = {"fr": ("/a-propos.html", "/mentions-legales.html", "/confidentialite.html"),
         "en": ("/en/about.html", "/en/legal-notice.html", "/en/privacy.html")}[lang]
    return """<footer class="site">
  <div class="wrap">
    <p class="flinks"><a href="%s">%s</a> &nbsp;&middot;&nbsp; <a href="%s">%s</a> &nbsp;&middot;&nbsp; <a href="%s">%s</a> &nbsp;&middot;&nbsp; <a href="mailto:contact@ecleptic.app">%s</a> &nbsp;&middot;&nbsp; <a href="/beta.html">%s</a></p>
    <p class="disclaimer">%s</p>
  </div>
</footer>""" % (p[0], U(lang, "f_about"), p[1], U(lang, "f_legal"), p[2], U(lang, "f_privacy"),
                 U(lang, "f_contact"), U(lang, "f_beta"), U(lang, "disclaimer"))


FOOTER = footer("fr")


def nav_data(lang="fr"):
    """Données du méga-menu : articles publiés par thème (5 plus récents, le compteur
    garde le total), 5 plus lus, panneaux L'app / Science / Bêta. Déterministe."""
    import json as _json
    arts = live_articles(lang)
    by_cat = {d: [] for d in DOMAINS}
    for a in sorted(arts, key=lambda a: a["date"], reverse=True):
        v = article_view(a, lang)
        by_cat.setdefault(cat(a), []).append({"t": v["title"], "u": v["path"]})
    cats = [{"n": theme_name(d, lang), "u": theme_path(d, lang), "c": len(by_cat[d]), "a": by_cat[d][:5]}
            for d in DOMAINS]
    idx = {a["slug"]: a for a in arts}
    pop = [{"t": article_view(idx[s], lang)["title"], "u": article_path(idx[s], lang)} for s in POPULAR if s in idx][:5]
    data = {"journal": {"cats": cats, "popular": pop, "total": len(arts)}}
    data.update(nav_panels(idx, lang))
    return ("/* Genere par tools/build_articles.py (nav_data) - ne pas editer a la main. */\n"
            "window.ECLEPTIC_NAV=%s;\n" % _json.dumps(data, ensure_ascii=False, separators=(",", ":")))


def nav_panels(idx, lang="fr"):
    """Panneaux du bandeau hors Journal (L'app, Science-Based, La bêta) : trois
    colonnes chacun, la première en grands liens. Pages de la méthode seulement si
    elles existent dans la langue (repli sur l'ancre de la page Science)."""
    en = lang == "en"
    science = "/en/science.html" if en else "/science.html"

    def mp(slug, anchor):
        p = METHODE_IDX.get(slug)
        q = methode_path(p, lang) if p else None
        return q or (science + "#" + anchor)
    home = home_path(lang)
    contact = {"t": "Write to us" if en else "Nous écrire", "u": "mailto:contact@ecleptic.app"}
    fiches = [{"t": methode_view(p, lang)["label"], "u": methode_path(p, lang)} for p in METHODE
              if p["kind"] == "fiche" and methode_path(p, lang)]
    T = (lambda f, e: e if en else f)
    science_cols = [
        {"label": T("La méthode, moteur par moteur", "The method, engine by engine"), "big": True,
         "more": {"t": T("Toute la méthode →", "The whole method →"), "u": science}, "items": [
            {"t": "Le Readiness Score" if not en else "The Readiness Score",
             "d": T("Quatre piliers croisés chaque matin.", "Four pillars combined every morning."), "u": mp("readiness-score", "readiness")},
            {"t": T("L'âge biologique", "Biological age"), "d": T("Ancré sur ta VO₂max et la cohorte HUNT.", "Anchored on your VO₂max and the HUNT cohort."), "u": mp("age-biologique", "age-biologique")},
            {"t": T("La nutrition", "Nutrition"), "d": T("438 000 références issues des bases officielles.", "438,000 entries from official databases."), "u": mp("nutrition", "nutrition")},
            {"t": T("Les vitaux", "Vitals"), "d": T("Ta ligne de base, pas celle d'un autre.", "Your baseline, not someone else's."), "u": mp("vitaux", "vitaux")},
            {"t": T("Les cibles", "Targets"), "d": T("Un métabolisme mesuré, pas estimé.", "A metabolism measured, not guessed."), "u": mp("cibles", "cibles")}]}]
    if fiches:
        science_cols.append({"label": T("Les mesures, expliquées", "The measures, explained"), "items": fiches})
    science_cols.append({"label": T("Nos sources", "Our sources"), "items": [
        {"t": T("ANSES · table Ciqual", "ANSES · Ciqual table"), "u": data_hub_path(lang) if DATA_PAGES else mp("nutrition", "nutrition")},
        {"t": "USDA · FoodData Central", "u": mp("nutrition", "nutrition")},
        {"t": "Open Food Facts", "u": mp("nutrition", "nutrition")},
        {"t": T("Cohorte HUNT (Norvège)", "HUNT cohort (Norway)"), "u": mp("age-biologique", "age-biologique")},
        {"t": T("Tables VDOT de Jack Daniels", "Jack Daniels' VDOT tables"), "u": mp("age-biologique", "age-biologique")},
        {"t": "National Sleep Foundation", "u": mp("besoin-de-sommeil", "readiness")}]})
    return {
        "app": {"cols": [
            {"label": T("L'app en trois temps", "The app in three steps"), "big": True, "items": [
                {"t": T("Mesurer", "Measure"), "d": T("Ta nuit, tes vitaux, ta charge. Sans saisie.", "Your night, your vitals, your load. No typing."), "u": home + "#" + T("mesurer", "measure")},
                {"t": T("Comprendre", "Understand"), "d": T("Sommeil, repas et séances, enfin croisés.", "Sleep, meals and sessions, finally connected."), "u": home + "#" + T("comprendre", "understand")},
                {"t": T("Agir", "Act"), "d": T("Un chiffre, une direction, chaque matin.", "One number, one direction, every morning."), "u": home + "#" + T("agir", "act")}]},
            {"label": T("Ce qu'elle calcule pour toi", "What it works out for you"), "items": [
                {"t": T("Ton Readiness Score, chaque matin", "Your Readiness Score, every morning"), "u": mp("readiness-score", "readiness")},
                {"t": T("Ton âge biologique, dès le premier jour", "Your biological age, from day one"), "u": mp("age-biologique", "age-biologique")},
                {"t": T("Tes repas, analysés en une photo", "Your meals, analysed from one photo"), "u": mp("nutrition", "nutrition")},
                {"t": T("Tes vitaux, lus sur ta ligne de base", "Your vitals, read against your baseline"), "u": mp("vitaux", "vitaux")},
                {"t": T("Tes cibles, recalibrées en continu", "Your targets, recalibrated continuously"), "u": mp("cibles", "cibles")}]},
            {"label": T("Commencer", "Get started"), "items": [
                {"t": T("Demander l'accès à la bêta", "Request beta access"), "u": "/beta.html", "gold": True},
                {"t": T("Lire le Journal", "Read the Journal"), "u": journal_path(lang)},
                {"t": T("La méthode scientifique", "The scientific method"), "u": science},
                contact]}]},
        "science": {"cols": science_cols},
        "beta": {"cols": [
            {"label": T("Rejoindre la bêta", "Join the beta"), "big": True, "spots": True, "items": [
                {"t": T("Demander l'accès", "Request access"), "d": T("45 secondes de questions, puis le lien d'installation.", "45 seconds of questions, then the install link."),
                 "u": "/beta.html", "gold": True}]},
            {"label": T("Ce qui t'attend", "What you get"), "items": [
                {"t": T("Toutes les fonctionnalités Golden, offertes aux testeurs", "Every Golden feature, free for testers")},
                {"t": T("Sur iPhone, iOS 16.4 ou plus récent", "On iPhone, iOS 16.4 or later")},
                {"t": T("Installation via TestFlight, l'app de bêtas d'Apple", "Installed through TestFlight, Apple's beta app")},
                {"t": T("Un bug ? Une capture d'écran suffit à nous le signaler", "A bug? A screenshot is all it takes to report it")}]},
            {"label": T("Questions", "Questions"), "items": [
                {"t": T("TestFlight, c'est quoi ?", "What is TestFlight?"), "u": "https://testflight.apple.com/"},
                {"t": T("Confidentialité", "Privacy"), "u": "/en/privacy.html" if en else "/confidentialite.html"},
                contact]}]},
    }


def cat(a):
    return a.get("cat", "Journal")


MONTHS_FR = I.MONTHS["fr"]


def fr_date(iso):
    return I.date_label(iso, "fr")


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
    words = len(re.sub(r"<[^>]+>", " ", a["body"]).split())
    return max(2, round(words / 220))


REVEAL_JS = """
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
</script>"""


def faq_parts(faq, lang):
    """Section FAQ visible + JSON-LD FAQPage (Google exige que le balisé soit affiché)."""
    import json as _json
    if not faq:
        return "", ""
    block = ('\n  <section class="faq">\n    <h2>%s</h2>\n' % U(lang, "faq")
             + "\n".join("    <h3>%s</h3>\n    <p>%s</p>" % (html.escape(q["q"]), html.escape(q["a"])) for q in faq)
             + "\n  </section>")
    js = '\n<script type="application/ld+json">' + _json.dumps({
        "@context": "https://schema.org", "@type": "FAQPage",
        "mainEntity": [{"@type": "Question", "name": q["q"], "acceptedAnswer": {"@type": "Answer", "text": q["a"]}}
                       for q in faq]}, ensure_ascii=False) + "</script>"
    return block, js


def author_line(lang, date_iso=None, updated_iso=None):
    upd = ""
    if updated_iso and (not date_iso or updated_iso > date_iso):
        upd = " &nbsp;&middot;&nbsp; %s %s" % (U(lang, "updated"), I.date_label(updated_iso, lang))
    about = "/a-propos.html" if lang == "fr" else "/en/about.html"
    return ('<p class="byline">%s <a href="%s" rel="author">%s</a>, %s%s</p>'
            % (U(lang, "by"), about, AUTHOR["name"], U(lang, "role"), upd))


def byline(date_iso=None, updated_iso=None):
    return author_line("fr", date_iso, updated_iso)


def sources_block(srcs, lang="fr"):
    """Section « Sources » : références vérifiées (tools/check_sources.py), liens sortants."""
    if not srcs:
        return ""
    items = "\n".join('      <li>%s <a href="%s" rel="noopener" target="_blank">%s</a></li>'
                      % (s["t"], html.escape(s["u"], quote=True), html.escape(source_label(s["u"])))
                      for s in srcs)
    return '\n  <section class="refs">\n    <h2>%s</h2>\n    <ol>\n%s\n    </ol>\n  </section>' % (U(lang, "sources"), items)


def article_page(a, others, lang="fr"):
    v = article_view(a, lang)
    alt_fr, alt_en = article_path(a, "fr"), article_path(a, "en")
    url = SITE + v["path"]
    data_links = ['<a href="%s">%s</a>' % (data_path(k, lang), html.escape(DATA_TEXTES[k][lang]["title"].split(":")[0].strip()))
                  for k in DATA_PAGES if a["slug"] in DATA_TEXTES[k].get("articles", [])][:1]
    more = "\n".join(data_links + ['<a href="%s">%s</a>' % (article_path(o, lang), html.escape(article_view(o, lang)["title"]))
                                   for o in others[:3 - len(data_links)]])
    img = img_path(a)
    og_image = ("\n" + og_image_tags(img)) if img else ""
    # Photo = élément LCP sur mobile : chargée en priorité, version adaptée à l'écran.
    hero = ('\n  <figure class="hero"><img src="%s" srcset="%s" sizes="(max-width: 640px) calc(100vw - 48px), 592px" '
            'alt="%s" width="1600" height="840" fetchpriority="high" decoding="async"></figure>'
            % (img, img_srcset(a), html.escape(v["title"], quote=True))) if img else ""
    # Titres « Préfixe : suite » : la suite est animée caractère par caractère (même
    # animation que « s'aligne. » sur l'accueil) ; les titres-questions simples non.
    sep = " : " if lang == "fr" else ": "
    reveal = REVEAL_JS if sep in v["title"] else ""
    faqblock, faqjsonld = faq_parts(v.get("faq") or [], lang)
    art = {"@context": "https://schema.org", "@type": "Article", "headline": v["title"],
           "description": v["description"]}
    if img:
        art["image"] = SITE + img
    art.update({"datePublished": a["date"], "dateModified": modified(v),
                "inLanguage": lang, "author": AUTHOR_LD, "publisher": PUBLISHER_LD,
                "mainEntityOfPage": url})
    if v.get("sources"):
        art["citation"] = citation_ld(v["sources"])
    crumbs = {"@context": "https://schema.org", "@type": "BreadcrumbList", "itemListElement": [
        {"@type": "ListItem", "position": 1, "name": "Journal", "item": SITE + journal_path(lang)},
        {"@type": "ListItem", "position": 2, "name": v["cat_name"], "item": SITE + theme_path(cat(a), lang)},
        {"@type": "ListItem", "position": 3, "name": v["title"], "item": url}]} if cat(a) in THEMES else None
    jsonld = __import__("json").dumps([x for x in (art, crumbs) if x], ensure_ascii=False)
    catlink = ('<a class="gold" href="%s">%s</a>' % (theme_path(cat(a), lang), html.escape(v["cat_name"]))
               if cat(a) in THEMES else '<span class="gold">%s</span>' % html.escape(v["cat_name"]))
    return """<!doctype html>
<html lang="%(lang)s">
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
<meta property="og:title" content="%(title)s">
<meta property="og:description" content="%(desc)s">
<meta property="og:type" content="article">
<meta property="og:url" content="%(url)s">%(og_image)s
<script type="application/ld+json">%(jsonld)s</script>%(faqjsonld)s
%(i18n)s
<link rel="stylesheet" href="/assets/site.css">
</head>
<body>
%(nav)s
<main class="wrap">
<article>
  <header>
    <span class="label">%(catlink)s &nbsp;&middot;&nbsp; %(date)s &nbsp;&middot;&nbsp; %(mins)s %(min)s</span>
    <h1>%(title)s</h1>
    <p class="standfirst">%(desc)s</p>
    %(byline)s
  </header>%(reveal)s%(hero)s
  %(body)s%(faqblock)s%(sources)s
  <div class="reward">
    <span class="label">%(u_rl)s</span>
    <h2>%(u_rh)s</h2>
    <p>%(u_rp)s</p>
    <a class="btn gold" href="/beta.html" onclick="track('article_cta_click',{article:'%(slug)s',lang:'%(lang)s'})">%(u_cta)s</a>
  </div>
  <div class="next">
    <span class="label">%(u_next)s</span>
%(more)s
  </div>
</article>
</main>
%(footer)s
%(posthog)s
<script>track('article_view',{article:'%(slug)s',lang:'%(lang)s'});</script>
%(navscripts)s
</body>
</html>
""" % {
        "lang": lang, "csp": CSP, "title": html.escape(v["title"]), "desc": html.escape(v["description"], quote=True),
        "seo": html.escape(title_tag(v["seo"])),
        "icons": HEAD_ICONS, "metarobots": META_ROBOTS, "catlink": catlink,
        "byline": author_line(lang, a["date"], modified(v)), "sources": sources_block(v.get("sources"), lang),
        "url": url, "jsonld": jsonld, "faqjsonld": faqjsonld, "faqblock": faqblock,
        "og_image": og_image, "hero": hero, "reveal": reveal, "i18n": head_i18n(alt_fr, alt_en),
        "nav": nav("articles", lang, alt_fr, alt_en), "date": I.date_label(a["date"], lang),
        "mins": read_min(v), "min": U(lang, "min"),
        "body": v["body"], "slug": a["slug"], "more": more,
        "u_rl": U(lang, "reward_label"), "u_rh": U(lang, "reward_h2"), "u_rp": U(lang, "reward_p"),
        "u_cta": U(lang, "cta"), "u_next": U(lang, "next"),
        "footer": footer(lang), "posthog": POSTHOG, "navscripts": nav_scripts(lang),
    }


def methode_page(p, lang="fr"):
    """Page de la méthode (moteur ou fiche) : même typographie que les articles, fil
    d'Ariane vers Science-Based, références, FAQ balisée, liens méthode et Journal."""
    import json as _json
    v = methode_view(p, lang)
    alt_fr, alt_en = methode_path(p, "fr"), methode_path(p, "en")
    url = SITE + v["path"]
    science = "/science.html" if lang == "fr" else "/en/science.html"
    # Un lien vers une page de la méthode inexistante casse le build (jamais de 404).
    for target in re.findall(r'href="/methode/([a-z0-9-]+)\.html"', p["body"] + p.get("lead", "")):
        if target not in METHODE_IDX:
            raise ValueError("lien méthode inconnu dans %s : %s" % (p["slug"], target))
    body = localize_links(v["body"].strip(), lang)
    lead = localize_links(v["lead"].strip(), lang)
    kicker = (U(lang, "m_kicker_engine") % p["num"]) if p["kind"] == "moteur" else U(lang, "m_kicker_fiche")
    refs = v.get("refs") or []
    refsblock = ('\n  <section class="refs">\n    <h2>%s</h2>\n    <ul>\n%s\n    </ul>\n  </section>'
                 % (U(lang, "refs"), "\n".join("      <li>%s</li>" % r for r in refs))) if refs else ""
    faqblock, faqjsonld = faq_parts(v.get("faq") or [], lang)
    links = []
    for s in p.get("related", []):
        if s in METHODE_IDX and s != p["slug"]:
            q = METHODE_IDX[s]
            path = methode_path(q, lang)
            if path:
                links.append('<a href="%s">%s</a>' % (path, html.escape(methode_view(q, lang)["label"])))
    idx = {a["slug"]: a for a in live_articles(lang)}
    for s in p.get("journal", []):
        if s in idx:
            links.append('<a href="%s">%s</a>' % (article_path(idx[s], lang), html.escape(article_view(idx[s], lang)["title"])))
    more = ('\n  <div class="next">\n    <span class="label">%s</span>\n%s\n  </div>'
            % (U(lang, "m_more"), "\n".join(links[:6]))) if links else ""
    jsonld = _json.dumps([
        {"@context": "https://schema.org", "@type": "TechArticle", "headline": v["title"],
         "description": v["description"], "datePublished": p["date"],
         "dateModified": v.get("updated", p["date"]), "inLanguage": lang,
         "image": SITE + "/assets/science/file-d-etoiles-og.jpg",
         "author": AUTHOR_LD, "publisher": PUBLISHER_LD,
         "mainEntityOfPage": url},
        {"@context": "https://schema.org", "@type": "BreadcrumbList", "itemListElement": [
            {"@type": "ListItem", "position": 1, "name": U(lang, "nav_home"), "item": SITE + home_path(lang)},
            {"@type": "ListItem", "position": 2, "name": "Science-Based", "item": SITE + science},
            {"@type": "ListItem", "position": 3, "name": v["label"], "item": url}]},
    ], ensure_ascii=False)
    return """<!doctype html>
<html lang="%(lang)s">
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
<meta property="og:title" content="%(title)s">
<meta property="og:description" content="%(desc)s">
<meta property="og:type" content="article">
<meta property="og:url" content="%(url)s">
%(ogimg)s
<script type="application/ld+json">%(jsonld)s</script>%(faqjsonld)s
%(i18n)s
<link rel="stylesheet" href="/assets/site.css">
</head>
<body>
%(nav)s
<main class="wrap">
<article class="methode">
  <header>
    <nav class="crumbs" aria-label="%(crumbs_aria)s"><a href="%(science)s">Science-Based</a><span aria-hidden="true">/</span><span>%(label)s</span></nav>
    <span class="label"><span class="gold">%(kicker)s</span></span>
    <h1>%(title)s</h1>
    <p class="standfirst">%(lead)s</p>
    %(byline)s
  </header>
  %(body)s%(refsblock)s%(faqblock)s
  <div class="reward">
    <span class="label">%(u_rl)s</span>
    <h2>%(u_rh)s</h2>
    <p>%(u_rp)s</p>
    <a class="btn gold" href="/beta.html" onclick="track('methode_cta_click',{page:'%(slug)s',lang:'%(lang)s'})">%(u_cta)s</a>
  </div>%(more)s
</article>
</main>
%(footer)s
%(posthog)s
<script>track('methode_view',{page:'%(slug)s',lang:'%(lang)s'});</script>
%(navscripts)s
</body>
</html>
""" % {
        "lang": lang, "csp": CSP, "seo": html.escape(title_tag(v.get("seo_title") or v["title"])),
        "icons": HEAD_ICONS, "metarobots": META_ROBOTS, "ogimg": og_image_tags("/assets/science/file-d-etoiles-og.jpg"),
        "byline": author_line(lang, p["date"], v.get("updated")), "i18n": head_i18n(alt_fr, alt_en),
        "title": html.escape(v["title"]), "desc": html.escape(v["description"], quote=True),
        "url": url, "jsonld": jsonld, "faqjsonld": faqjsonld, "crumbs_aria": U(lang, "crumbs_aria"),
        "science": science, "nav": nav("science", lang, alt_fr, alt_en), "label": html.escape(v["label"]), "kicker": kicker,
        "lead": lead, "body": body, "refsblock": refsblock, "faqblock": faqblock,
        "u_rl": U(lang, "m_reward_label"), "u_rh": U(lang, "m_reward_h2"), "u_rp": U(lang, "reward_p"), "u_cta": U(lang, "cta"),
        "slug": p["slug"], "more": more, "footer": footer(lang), "posthog": POSTHOG, "navscripts": nav_scripts(lang),
    }


def entry_card(a, lang="fr"):
    """Carte d'article du Journal (index et pages thème)."""
    v = article_view(a, lang)
    return """<a class="entry" href="%s" data-slug="%s" data-cat="%s">
  <span class="etext">
  <span class="label meta"><span class="gold">%s</span> &nbsp;&middot;&nbsp; %s &nbsp;&middot;&nbsp; %s %s</span>
  <h2>%s</h2>
  <p class="desc">%s</p>
  <span class="readmore">%s</span>
  </span>%s
</a>""" % (v["path"], a["slug"], html.escape(v["cat_name"]), html.escape(v["cat_name"]), I.date_label(a["date"], lang),
           read_min(v), U(lang, "min"), html.escape(v["title"]), html.escape(v["description"]), U(lang, "j_read"), thumb_img(a))


def index_page(lang="fr"):
    arts = live_articles(lang)
    cards = "\n".join(entry_card(a, lang) for a in sorted(arts, key=lambda x: x["date"], reverse=True))
    counts = {d: sum(1 for a in arts if cat(a) == d) for d in DOMAINS}
    # Liens réels vers les pages thème (explorables par Google) ; au clic, le
    # Journal filtre sur place (JS plus bas). data-filter = nom affiché du thème.
    themes = "\n".join(
        """<a class="theme" href="%s" data-filter="%s"><span>%s</span><span class="count">%d</span></a>"""
        % (theme_path(d, lang), html.escape(theme_name(d, lang)), html.escape(theme_name(d, lang)), counts[d])
        for d in DOMAINS
    )
    empty = "" if arts else """<div class="empty">%s</div>""" % U(lang, "j_empty")
    quote = ("""
  <div class="quote">
    <p>%s</p>
    <span class="label">%s</span>
  </div>""" % (U(lang, "j_quote"), U(lang, "j_quote_by"))) if U(lang, "j_quote") else ""
    pop = [s for s in POPULAR if s in {a["slug"] for a in arts}]
    return """<!doctype html>
<html lang="%(lang)s">
<head>
<meta charset="utf-8">
%(csp)s
<meta name="referrer" content="strict-origin-when-cross-origin">
<meta name="viewport" content="width=device-width, initial-scale=1">
%(icons)s
%(metarobots)s
<title>%(j_title)s</title>
<meta name="description" content="%(j_desc)s">
<link rel="canonical" href="%(site)s%(jpath)s">
<meta property="og:title" content="%(j_title)s">
<meta property="og:description" content="%(j_ogdesc)s">
<meta property="og:type" content="website">
<meta property="og:url" content="%(site)s%(jpath)s">
%(ogimg)s
%(jsonld)s
%(i18n)s
<link rel="stylesheet" href="/assets/site.css">
</head>
<body>
%(nav)s
<main class="wrap">
  <div class="pagehead">
    <span class="label">%(j_label)s</span>
    <h1 class="display" style="margin-top:22px">%(j_h1)s</h1>
    <p>%(j_p)s</p>
    <div class="stats">
      <div><span class="n">%(narticles)d</span><span class="l label">%(j_articles)s</span></div>
      <div><span class="n">%(nthemes)d</span><span class="l label">%(j_themes)s</span></div>
    </div>
  </div>
  <div class="themes">
    <span class="label">%(j_themes_label)s</span>
    <div class="themescroll">
    <a class="theme on" href="%(jpath)s" data-filter="*"><span>%(j_all)s</span><span class="count">%(narticles)d</span></a>
%(themes)s
    </div>
  </div>%(quote)s
  <div class="journal" id="entries">
%(cards)s
  </div>
%(empty)s
  <div class="reward noafter">
    <span class="label">%(j_rl)s</span>
    <h2>%(j_rh)s</h2>
    <p>%(j_rp)s</p>
    <a class="btn gold" href="/beta.html" onclick="track('article_cta_click',{article:'index',lang:'%(lang)s'})">%(cta)s</a>
  </div>
</main>
%(footer)s
%(posthog)s
<script>
track('articles_index_view',{lang:'%(lang)s'});
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
    if (q.get('sort') === 'populaires' || q.get('sort') === 'popular'){
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
%(navscripts)s
</body>
</html>
""" % {"lang": lang, "csp": CSP, "site": SITE, "jpath": journal_path(lang), "nav": nav("articles", lang, "/articles/", "/en/journal/"),
       "cards": cards, "themes": themes, "quote": quote,
       "icons": HEAD_ICONS, "metarobots": META_ROBOTS, "ogimg": og_image_tags("/assets/og/journal.jpg"),
       "i18n": head_i18n("/articles/", "/en/journal/"),
       "jsonld": ld({"@context": "https://schema.org", "@type": "CollectionPage",
                     "name": U(lang, "j_collection"), "url": SITE + journal_path(lang), "inLanguage": lang,
                     "description": ("Sommeil, nutrition, entraînement, récupération : des articles courts, scientifiques et actionnables."
                                     if lang == "fr" else "Sleep, nutrition, training, recovery: short, science-based, actionable articles."),
                     "publisher": PUBLISHER_LD}),
       "empty": empty, "narticles": len(arts), "nthemes": len(DOMAINS),
       "popular": __import__("json").dumps(pop), "cta": U(lang, "cta"),
       "j_title": U(lang, "j_title"), "j_desc": U(lang, "j_desc"), "j_ogdesc": U(lang, "j_ogdesc"),
       "j_label": U(lang, "j_label"), "j_h1": U(lang, "j_h1"), "j_p": U(lang, "j_p"),
       "j_articles": U(lang, "j_articles"), "j_themes": U(lang, "j_themes"), "j_themes_label": U(lang, "j_themes_label"),
       "j_all": U(lang, "j_all"), "j_rl": U(lang, "j_reward_label"), "j_rh": U(lang, "j_reward_h2"), "j_rp": U(lang, "j_reward_p"),
       "footer": footer(lang), "posthog": POSTHOG, "navscripts": nav_scripts(lang)}


def theme_articles(d, lang="fr"):
    return sorted([a for a in live_articles(lang) if cat(a) == d], key=lambda x: x["date"], reverse=True)


def theme_meta(d, lang):
    return THEMES[d] if lang == "fr" else I.THEMES_EN[d]


def theme_page(d, lang="fr"):
    """Page thème : introduction, articles publiés du thème, pages de la méthode
    liées, autres thèmes. noindex tant que < THEME_MIN_INDEX articles en ligne."""
    t = theme_meta(d, lang)
    path = theme_path(d, lang)
    url = SITE + path
    arts = theme_articles(d, lang)
    robots = META_ROBOTS if len(arts) >= THEME_MIN_INDEX else '<meta name="robots" content="noindex, follow">'
    cards = "\n".join(entry_card(a, lang) for a in arts)
    empty = "" if arts else '<div class="empty">%s</div>' % U(lang, "t_empty")
    og = (img_path(arts[0]) if arts else None) or "/assets/og/journal.jpg"
    methode = [METHODE_IDX[s] for s in THEMES[d]["methode"] if s in METHODE_IDX and methode_path(METHODE_IDX[s], lang)]
    mblock = ('\n  <div class="next">\n    <span class="label">%s</span>\n%s\n  </div>'
              % (U(lang, "t_methode"), "\n".join('<a href="%s">%s</a>' % (methode_path(p, lang), html.escape(methode_view(p, lang)["label"]))
                                                   for p in methode))) if methode else ""
    others = "\n".join('<a href="%s">%s</a>' % (theme_path(o, lang), html.escape(theme_name(o, lang))) for o in DOMAINS if o != d)
    name = theme_name(d, lang)
    jsonld = [
        {"@context": "https://schema.org", "@type": "CollectionPage", "name": "%s — %s" % (name, U(lang, "j_collection")),
         "description": t["desc"], "url": url, "inLanguage": lang, "publisher": PUBLISHER_LD,
         "mainEntity": {"@type": "ItemList", "itemListElement": [
             {"@type": "ListItem", "position": i + 1, "url": SITE + article_path(a, lang)}
             for i, a in enumerate(arts)]}},
        {"@context": "https://schema.org", "@type": "BreadcrumbList", "itemListElement": [
            {"@type": "ListItem", "position": 1, "name": "Journal", "item": SITE + journal_path(lang)},
            {"@type": "ListItem", "position": 2, "name": name, "item": url}]},
    ]
    n = len(arts)
    return """<!doctype html>
<html lang="%(lang)s">
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
%(i18n)s
<link rel="stylesheet" href="/assets/site.css">
</head>
<body>
%(nav)s
<main class="wrap">
  <div class="pagehead">
    <nav class="crumbs" aria-label="%(crumbs_aria)s"><a href="%(jpath)s">Journal</a><span aria-hidden="true">/</span><span>%(name)s</span></nav>
    <span class="label">%(t_label)s</span>
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
    <span class="label">%(t_others)s</span>
%(others)s
  </div>
  <div class="reward noafter">
    <span class="label">%(j_rl)s</span>
    <h2>%(j_rh)s</h2>
    <p>%(j_rp)s</p>
    <a class="btn gold" href="/beta.html" onclick="track('article_cta_click',{article:'theme-%(slug)s',lang:'%(lang)s'})">%(cta)s</a>
  </div>
</main>
%(footer)s
%(posthog)s
<script>track('journal_theme_view',{theme:'%(slug)s',lang:'%(lang)s'});</script>
%(navscripts)s
</body>
</html>
""" % {"lang": lang, "csp": CSP, "metarobots": robots, "icons": HEAD_ICONS, "seo": html.escape(title_tag(t["seo"])),
       "desc": html.escape(t["desc"], quote=True), "url": url, "ogimg": og_image_tags(og),
       "jsonld": ld(jsonld), "i18n": head_i18n(theme_path(d, "fr"), theme_path(d, "en")),
       "nav": nav("articles", lang, theme_path(d, "fr"), theme_path(d, "en")),
       "crumbs_aria": U(lang, "crumbs_aria"), "jpath": journal_path(lang),
       "name": html.escape(name), "intro": html.escape(t["intro"]), "t_label": U(lang, "t_label"),
       "n": n, "nlabel": U(lang, "t_article") if n == 1 else U(lang, "t_articles"), "cards": cards, "empty": empty,
       "mblock": mblock, "others": others, "t_others": U(lang, "t_others"), "slug": THEMES[d]["slug"],
       "j_rl": U(lang, "j_reward_label"), "j_rh": U(lang, "j_reward_h2"), "j_rp": U(lang, "j_reward_p"), "cta": U(lang, "cta"),
       "footer": footer(lang), "posthog": POSTHOG, "navscripts": nav_scripts(lang)}


def prose_page(path, seo, desc, label, h1, body, jsonld, og, track_event, lang="fr", alt=(None, None)):
    """Page de texte simple (À propos, mentions légales) : même typographie que les articles."""
    url = SITE + "/" + path
    return """<!doctype html>
<html lang="%(lang)s">
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
%(i18n)s
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
  <p class="updated">%(updated)s</p>
</article>
</main>
%(footer)s
%(posthog)s
<script>track('%(track)s',{lang:'%(lang)s'});</script>
%(navscripts)s
</body>
</html>
""" % {"lang": lang, "csp": CSP, "icons": HEAD_ICONS, "metarobots": META_ROBOTS, "seo": html.escape(seo),
       "desc": html.escape(desc, quote=True), "url": url, "ogimg": og_image_tags(og), "jsonld": ld(jsonld),
       "i18n": head_i18n(*alt), "nav": nav("", lang, *alt), "label": label,
       "h1": h1, "body": body.strip(), "updated": U(lang, "last_updated") % I.date_label(ABOUT_UPDATED, lang),
       "footer": footer(lang), "posthog": POSTHOG, "track": track_event, "navscripts": nav_scripts(lang)}


ALT_ABOUT = ("/a-propos.html", "/en/about.html")
ALT_LEGAL = ("/mentions-legales.html", "/en/legal-notice.html")


def about_page(lang="fr"):
    if lang == "en":
        body = """
  <h2>Auguste Phily-Priou, founder</h2>
  <p>I'm Auguste, I'm 27, and I'm building Ecleptic almost single-handedly. I'm not a doctor: I'm someone who took his health back into his own hands and wanted to understand what actually works.</p>
  <p>I smoked for eleven years, from 14 to 25, and quit at the end of 2024. In 2025 I went back to regular exercise, without chasing intensity, learned to eat better, and started optimising pretty much every part of my life. That's where my Instagram handle comes from: <a href="%(ig)s" rel="me noopener" target="_blank">@_optimisateur</a>.</p>
  <p>Ecleptic grew out of that: connecting what is usually tracked separately, sleep, food and training, to understand how each one affects the others, and to know every morning what really matters.</p>

  <h2>How the articles are written</h2>
  <ul>
  <li><strong>A real question, a straight answer.</strong> Every article starts from a question people actually ask, and answers it in the first sentence.</li>
  <li><strong>Sourced numbers.</strong> Benchmarks come from published sources: learned societies (National Sleep Foundation, American Academy of Sleep Medicine…), studies and meta-analyses, official databases such as the ANSES Ciqual table or USDA FoodData Central. Every article lists its sources, and the <a href="/en/science.html">method</a> pages list their references.</li>
  <li><strong>Health guardrails.</strong> No diagnosis, no dosing. As soon as a topic becomes medical (heart, deficiencies, mental health, pregnancy), the article points you to a health professional.</li>
  <li><strong>Dated updates.</strong> When an article changes in substance, its update date appears under the title.</li>
  </ul>
  <p>Spotted an error, a more recent study, something to clarify? Write to me at <a href="mailto:contact@ecleptic.app">contact@ecleptic.app</a>: I check, I correct, and the correction is dated.</p>

  <h2>Ecleptic in brief</h2>
  <p>Ecleptic is an iOS wellness app, in private beta. It brings your sleep, nutrition and training together into one score, every morning. It does not replace medical advice and is not a medical device. The publisher and host of this website are listed in the <a href="/en/legal-notice.html">legal notice</a>.</p>
""" % {"ig": AUTHOR["instagram"]}
        person = dict(AUTHOR_LD, worksFor={"@id": PUBLISHER_LD["@id"]})
        jsonld = {"@context": "https://schema.org", "@type": "AboutPage", "url": SITE + "/en/about.html",
                  "name": "About Ecleptic", "inLanguage": "en", "mainEntity": person, "publisher": PUBLISHER_LD}
        return prose_page("en/about.html", "About: who writes for Ecleptic — Ecleptic",
                          "Auguste Phily-Priou, founder of Ecleptic: his story, why he is building the app, and how the Journal articles are written, sourced and updated.",
                          "About", "Who writes<br><span class=\"gold\">here</span>.", body, jsonld,
                          "/assets/og/accueil.jpg", "about_view", "en", ALT_ABOUT)
    body = """
  <h2>Auguste Phily-Priou, fondateur</h2>
  <p>Je m'appelle Auguste, j'ai 27 ans, et je construis Ecleptic quasiment seul. Je ne suis pas médecin : je suis quelqu'un qui a repris sa santé en main, et qui a voulu comprendre ce qui marche vraiment.</p>
  <p>J'ai fumé pendant onze ans, de 14 à 25 ans, et j'ai arrêté fin 2024. En 2025, j'ai repris le sport de façon régulière, sans chercher l'intensité, j'ai appris à mieux manger, et j'ai commencé à optimiser à peu près tous les aspects de ma vie. C'est de là que vient mon pseudo sur Instagram, <a href="%(ig)s" rel="me noopener" target="_blank">@_optimisateur</a>.</p>
  <p>Ecleptic est né de cette démarche : relier ce qui est d'habitude suivi séparément, le sommeil, l'alimentation et l'entraînement, pour comprendre comment chacun agit sur les autres, et savoir chaque matin ce qui compte vraiment.</p>

  <h2>Comment les articles sont écrits</h2>
  <ul>
  <li><strong>Une vraie question, une réponse directe.</strong> Chaque article part d'une question que les gens se posent vraiment, et y répond dès la première phrase.</li>
  <li><strong>Des chiffres sourcés.</strong> Les repères viennent de sources publiées : sociétés savantes (National Sleep Foundation, American Academy of Sleep Medicine…), études et méta-analyses, bases officielles comme la table Ciqual de l'ANSES ou FoodData Central de l'USDA. Chaque article liste ses sources, et les pages de <a href="/science.html">la méthode</a> leurs références.</li>
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
                      "/assets/og/accueil.jpg", "about_view", "fr", ALT_ABOUT)


def legal_page(lang="fr"):
    if lang == "en":
        body = """
  <h2>Website publisher</h2>
  <p>The website ecleptic.health is published by <strong>Auguste Phily-Priou</strong>, sole trader (entrepreneur individuel, EI, under French law).<br>
  Address: 10 Rue du Commerce, 86400 Civray, France<br>
  Email: <a href="mailto:contact@ecleptic.app">contact@ecleptic.app</a><br>
  SIREN (French business registration number): registration in progress; the number will be added here as soon as it is issued.</p>

  <h2>Publication director</h2>
  <p>Auguste Phily-Priou.</p>

  <h2>Hosting</h2>
  <p>GitHub, Inc. (GitHub Pages service), 88 Colin P. Kelly Jr. Street, San Francisco, CA 94107, United States — <a href="https://github.com" rel="noopener" target="_blank">github.com</a>.</p>

  <h2>Intellectual property</h2>
  <p>“Ecleptic” is the subject of a European Union trade mark application filed with the EUIPO (application no. 019418299, filed on 4 September 2026). The texts on this website are the property of the publisher: any reproduction without permission is prohibited. Illustrative photographs come mostly from <a href="https://unsplash.com" rel="noopener" target="_blank">Unsplash</a>, under the Unsplash licence.</p>

  <h2>Personal data</h2>
  <p>This website measures its audience with PostHog, on servers located in the European Union. How the app processes data is described in the <a href="/en/privacy.html">privacy policy</a>.</p>

  <h2>Health disclaimer</h2>
  <p>The content of this website is for information only. It does not replace medical advice, diagnosis or treatment. Ecleptic is a wellness app, not a medical device.</p>

  <h2>Contact</h2>
  <p><a href="mailto:contact@ecleptic.app">contact@ecleptic.app</a></p>

  <p>This notice is a translation; the <a href="/mentions-legales.html">French version</a> prevails.</p>
"""
        jsonld = {"@context": "https://schema.org", "@type": "WebPage", "url": SITE + "/en/legal-notice.html",
                  "name": "Legal notice", "inLanguage": "en", "publisher": PUBLISHER_LD}
        return prose_page("en/legal-notice.html", "Legal notice — Ecleptic",
                          "Legal notice for ecleptic.health: publisher, publication director, host, intellectual property and contact details.",
                          "Legal information", "Legal notice", body, jsonld,
                          "/assets/og/accueil.jpg", "legal_view", "en", ALT_LEGAL)
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
                      "/assets/og/accueil.jpg", "legal_view", "fr", ALT_LEGAL)


# ============================================================================
# Données nutritionnelles (table Ciqual 2025 de l'ANSES) : /donnees/ et /en/data/
# Classements : tools/donnees/ciqual.json (build_ciqual_data.py) ; textes :
# tools/donnees/textes.py (TEXTES[clé][fr|en], sources, articles, methode).
# ============================================================================

def _load_data():
    import json as _json, importlib.util as _ilu
    d = os.path.join(os.path.dirname(os.path.abspath(__file__)), "donnees")
    data = _json.load(open(os.path.join(d, "ciqual.json"), encoding="utf-8")) if os.path.exists(os.path.join(d, "ciqual.json")) else None
    textes = {}
    if os.path.exists(os.path.join(d, "textes.py")):
        spec = _ilu.spec_from_file_location("donnees_textes", os.path.join(d, "textes.py"))
        mod = _ilu.module_from_spec(spec)
        spec.loader.exec_module(mod)
        textes = mod.TEXTES
    return data, textes


CIQUAL, DATA_TEXTES = _load_data()
DATA_ORDER = ["proteines", "fer", "magnesium", "calcium", "fibres", "omega-3", "vitamine-d",
              "vitamine-c", "vitamine-b12", "potassium", "zinc"]
DATA_EN_SLUG = {"proteines": "protein", "fer": "iron", "magnesium": "magnesium", "calcium": "calcium",
                "fibres": "fiber", "vitamine-c": "vitamin-c", "vitamine-d": "vitamin-d", "potassium": "potassium",
                "zinc": "zinc", "vitamine-b12": "vitamin-b12", "omega-3": "omega-3"}
DATA_PAGES = [k for k in DATA_ORDER if CIQUAL and k in CIQUAL["nutrients"] and k in DATA_TEXTES]
DATA_DATE = "2026-09-30"


def data_path(key, lang="fr"):
    if key not in DATA_PAGES:
        return None
    return ("/donnees/aliments-riches-en-%s.html" % key) if lang == "fr" else ("/en/data/foods-high-in-%s.html" % DATA_EN_SLUG[key])


def data_hub_path(lang="fr"):
    return "/donnees/" if lang == "fr" else "/en/data/"


def fmt_num(x, lang):
    """1260 → « 1 260 » / « 1,260 » ; 22.8 → « 22,8 » / « 22.8 » ; 0.35 → « 0,35 »."""
    if x >= 100:
        s = "{:,.0f}".format(x)
    elif x >= 10:
        s = ("%.1f" % x).rstrip("0").rstrip(".")
    else:
        s = ("%.2f" % x).rstrip("0").rstrip(".")
    if lang == "fr":
        s = s.replace(",", " ").replace(".", ",")
    return s


def food_name(f, lang):
    return f["fr"] if lang == "fr" else f["en"]


def short_food(f, lang):
    """Nom officiel complet (couper à la virgule fausserait le sens : « Oeuf, blanc, en
    poudre » n'est pas un œuf), entre guillemets pour signaler la dénomination Ciqual."""
    n = food_name(f, lang).strip()
    return ("« %s »" % n) if lang == "fr" else ("“%s”" % n)


DATA_UI = {
    "fr": {"label": "Données nutritionnelles &nbsp;&middot;&nbsp; Table Ciqual 2025", "crumb": "Données",
           "role": "Son rôle", "needs": "Tes besoins", "tips": "Nos conseils",
           "rank_h": "Le classement : les %d aliments du quotidien les plus riches en %s",
           "fam_h": "Les meilleures sources, famille par famille",
           "dens_h": "Les plus riches en protéines pour 100 kcal",
           "dens_p": "Utile en sèche ou à calories comptées : grammes de protéines apportés pour 100 kcal de l'aliment (aliments d'au moins 40 kcal/100 g).",
           "epa_h": "EPA + DHA : les poissons et produits de la mer les plus riches",
           "ala_h": "ALA : les sources végétales les plus riches",
           "c_rank": "Rang", "c_food": "Aliment", "c_grp": "Groupe", "c_val": "Pour 100 g", "c_nrv": "% VNR",
           "c_fam": "Famille", "c_dens": "g / 100 kcal",
           "record": "Hors classement, les records absolus de la table sont des aliments consommés en très petites quantités : %s.",
           "method_h": "Comment ce classement est construit",
           "method": ("Valeurs pour 100 g d'aliment tel que décrit (cru, cuit, égoutté…), telles que publiées par l'ANSES dans la table Ciqual 2025 (%d aliments ; teneur en %s connue pour %d d'entre eux). "
                      "Le classement « au quotidien » écarte les épices, herbes, algues et condiments, les compléments et aliments destinés à une alimentation particulière, les aliments infantiles, l'alcool et les viandes ou poissons crus (leur version cuite est gardée). "
                      "Pour varier les exemples, un seul aliment est gardé par nom principal (le plus riche). "
                      "Les valeurs « traces » comptent pour zéro ; les valeurs inférieures au seuil de quantification ne sont pas classées.%s"),
           "nrv_note": " Le %% VNR rapporte la teneur pour 100 g à la valeur nutritionnelle de référence européenne (%s %s par jour, règlement UE nº 1169/2011), celle des étiquettes : c'est un repère, pas ton besoin personnel.",
           "atyp": " Une valeur manifestement atypique a été écartée : %s.",
           "attribution": "Source des données : Anses. 2025. Table de composition nutritionnelle des aliments Ciqual (version du 3 novembre 2025), licence CC BY 4.0. Classement et mise en forme : Ecleptic.",
           "faq_q": "Quel aliment contient le plus de %s ?",
           "faq_a": "En tête des aliments du quotidien de la table Ciqual 2025 de l'ANSES : %s, avec %s %s pour 100 g, devant %s (%s %s) et %s (%s %s).",
           "lead": "Selon la table Ciqual 2025 de l'ANSES, le trio de tête des aliments du quotidien les plus riches en %s : %s (%s %s pour 100 g), %s (%s %s) et %s (%s %s).",
           "reward_h2": "Ce que ce tableau recense,<br>l'app le compte pour toi.",
           "reward_p": "Scanne ton repas : Ecleptic retrouve chaque aliment dans les bases officielles et suit tes apports en micronutriments, jour après jour. La bêta iOS est ouverte à un petit cercle.",
           "more": "Pour aller plus loin", "others": "Les autres classements",
           "hub_title": "Données nutritionnelles : les aliments les plus riches en… — Ecleptic",
           "hub_seo": "Aliments les plus riches en protéines, fer… : données Ciqual",
           "hub_desc": "Protéines, fer, magnésium, calcium, fibres, oméga-3, vitamines : les aliments les plus riches, classés à partir de la table officielle Ciqual 2025 de l'ANSES.",
           "hub_label": "Données nutritionnelles", "hub_h1": "Les chiffres<br><span class=\"gold\">officiels</span>.",
           "hub_p": "Onze classements tirés de la table Ciqual 2025 de l'ANSES, la référence française de la composition des aliments : pour chaque nutriment, les aliments du quotidien qui en apportent le plus, pour 100 g, avec la méthode et la source.",
           "hub_top": "En tête : %s (%s %s pour 100 g)", "hub_n": "Classements", "hub_foods": "Aliments dans la table"},
    "en": {"label": "Nutrition data &nbsp;&middot;&nbsp; Ciqual table 2025", "crumb": "Data",
           "role": "What it does", "needs": "How much you need", "tips": "Practical tips",
           "rank_h": "The ranking: the %d everyday foods highest in %s",
           "fam_h": "Best sources, food group by food group",
           "dens_h": "Highest in protein per 100 kcal",
           "dens_p": "Useful when you are cutting or counting calories: grams of protein per 100 kcal of the food (foods with at least 40 kcal per 100 g).",
           "epa_h": "EPA + DHA: the richest fish and seafood",
           "ala_h": "ALA: the richest plant sources",
           "c_rank": "Rank", "c_food": "Food", "c_grp": "Group", "c_val": "Per 100 g", "c_nrv": "% NRV",
           "c_fam": "Food group", "c_dens": "g / 100 kcal",
           "record": "Outside the ranking, the absolute record-holders in the table are foods eaten in very small amounts: %s.",
           "method_h": "How this ranking is built",
           "method": ("Values per 100 g of the food as described (raw, cooked, drained…), as published by ANSES, France's food safety agency, in the 2025 Ciqual table (%d foods; %s content known for %d of them). "
                      "The everyday ranking leaves out spices, herbs, seaweed and condiments, supplements and foods for special medical purposes, baby foods, alcohol, and raw meat or fish (the cooked version is kept). "
                      "To keep the examples varied, only one food per main name is kept (the richest). "
                      "Values listed as “traces” count as zero; values below the quantification limit are not ranked.%s"),
           "nrv_note": " %% NRV compares the content per 100 g with the EU nutrient reference value (%s %s per day, Regulation (EU) No 1169/2011), the one used on food labels: a benchmark, not your personal requirement.",
           "atyp": " One clearly atypical value was set aside: %s.",
           "attribution": "Data source: Anses. 2025. Ciqual French food composition table (version of 3 November 2025), CC BY 4.0 licence. Ranking and layout: Ecleptic.",
           "faq_q": "Which food has the most %s?",
           "faq_a": "Top of the everyday foods in the 2025 Ciqual table from ANSES: %s, with %s %s per 100 g, ahead of %s (%s %s) and %s (%s %s).",
           "lead": "According to the 2025 Ciqual table from ANSES, France's food safety agency, the top three everyday foods highest in %s: %s (%s %s per 100 g), %s (%s %s) and %s (%s %s).",
           "reward_h2": "What this table lists,<br>the app counts for you.",
           "reward_p": "Scan your meal: Ecleptic matches every food against official databases and tracks your micronutrient intake, day after day. The iOS beta is open to a small circle.",
           "more": "Go further", "others": "Other rankings",
           "hub_title": "Nutrition data: foods highest in protein, iron and more — Ecleptic",
           "hub_seo": "Foods highest in protein, iron and more: Ciqual data",
           "hub_desc": "Protein, iron, magnesium, calcium, fiber, omega-3, vitamins: the richest foods, ranked from the official 2025 Ciqual food composition table by ANSES.",
           "hub_label": "Nutrition data", "hub_h1": "The official<br><span class=\"gold\">numbers</span>.",
           "hub_p": "Eleven rankings drawn from the 2025 Ciqual table by ANSES, the French reference for food composition: for each nutrient, the everyday foods that provide the most per 100 g, with the method and the source.",
           "hub_top": "Top: %s (%s %s per 100 g)", "hub_n": "Rankings", "hub_foods": "Foods in the table"},
}


def DU(lang, k):
    return DATA_UI[lang][k]


def data_table(rows, lang, unit, nrv=None, value_label=None, show_group=True, numbered=True, caption=None):
    head = ((("<th class=\"n\">%s</th>" % DU(lang, "c_rank")) if numbered else "")
            + "<th>%s</th>" % DU(lang, "c_food")
            + (("<th class=\"grp\">%s</th>" % DU(lang, "c_grp")) if show_group else "")
            + "<th class=\"n\">%s</th>" % (value_label or ("%s / 100 g" % unit))
            + (("<th class=\"n\">%s</th>" % DU(lang, "c_nrv")) if nrv else ""))
    body = []
    for i, f in enumerate(rows):
        body.append("<tr>" + (("<td class=\"n\">%d</td>" % (i + 1)) if numbered else "")
                    + "<td>%s</td>" % html.escape(food_name(f, lang))
                    + (("<td class=\"grp\">%s</td>" % html.escape(f["grp_" + lang].capitalize())) if show_group else "")
                    + "<td class=\"n\">%s</td>" % fmt_num(f["v"], lang)
                    + (("<td class=\"n\">%d %%</td>" % round(f["v"] / nrv * 100)) if nrv else "") + "</tr>")
    cap = "\n<caption>%s</caption>" % caption if caption else ""
    return ('<div class="tablewrap"><table>%s\n<thead><tr>%s</tr></thead>\n<tbody>\n%s\n</tbody>\n</table></div>'
            % (cap, head, "\n".join(body)))


def data_page(key, lang="fr"):
    import json as _json
    n = CIQUAL["nutrients"][key]
    t = DATA_TEXTES[key][lang]
    unit, nrv, top = n["unit"], n.get("nrv"), n["top"]
    path, alt_fr, alt_en = data_path(key, lang), data_path(key, "fr"), data_path(key, "en")
    url = SITE + path
    nom = t["nom"]
    u = unit
    lead = DU(lang, "lead") % (nom, short_food(top[0], lang), fmt_num(top[0]["v"], lang), u,
                               short_food(top[1], lang), fmt_num(top[1]["v"], lang), u,
                               short_food(top[2], lang), fmt_num(top[2]["v"], lang), u)
    faq = [{"q": DU(lang, "faq_q") % nom,
            "a": DU(lang, "faq_a") % (short_food(top[0], lang), fmt_num(top[0]["v"], lang), u,
                                      short_food(top[1], lang), fmt_num(top[1]["v"], lang), u,
                                      short_food(top[2], lang), fmt_num(top[2]["v"], lang), u)}] + list(t.get("faq", []))
    faqblock, faqjsonld = faq_parts(faq, lang)
    cap = DU(lang, "attribution")
    tables = []
    if key == "omega-3":
        tables.append("<h2>%s</h2>\n%s" % (DU(lang, "epa_h"), data_table(top, lang, "g", caption=cap)))
        tables.append("<h2>%s</h2>\n%s" % (DU(lang, "ala_h"), data_table(n["ala"], lang, "g", caption=cap)))
    else:
        tables.append("<h2>%s</h2>\n%s" % (DU(lang, "rank_h") % (len(top), nom), data_table(top, lang, unit, nrv, caption=cap)))
        fam_rows = []
        for fam in n.get("families", []):
            for i, f in enumerate(fam["items"]):
                fam_rows.append("<tr><td>%s</td><td>%s</td><td class=\"n\">%s</td></tr>" % (
                    html.escape(fam[lang]) if i == 0 else "", html.escape(food_name(f, lang)), fmt_num(f["v"], lang)))
        if fam_rows:
            tables.append('<h2>%s</h2>\n<div class="tablewrap"><table>\n<caption>%s</caption>\n<thead><tr><th>%s</th><th>%s</th><th class="n">%s / 100 g</th></tr></thead>\n<tbody>\n%s\n</tbody>\n</table></div>'
                          % (DU(lang, "fam_h"), cap, DU(lang, "c_fam"), DU(lang, "c_food"), unit, "\n".join(fam_rows)))
        if key == "proteines" and n.get("density"):
            tables.append("<h2>%s</h2>\n<p>%s</p>\n%s" % (DU(lang, "dens_h"), DU(lang, "dens_p"),
                                                          data_table(n["density"], lang, unit, value_label=DU(lang, "c_dens"), caption=cap)))
    record = ""
    cond = n.get("condiments") or []
    if cond and top and cond[0]["v"] > top[0]["v"]:
        record = "<p>%s</p>" % (DU(lang, "record") % ", ".join(
            "%s (%s %s/100 g)" % (html.escape(short_food(c, lang)), fmt_num(c["v"], lang), unit) for c in cond[:3]))
    atyp = [why for k, why in CIQUAL.get("atypical", {}).items() if k.startswith(key + ":")]
    method = DU(lang, "method") % (CIQUAL["n_foods"], nom, n["n_known"],
                                   ((DU(lang, "nrv_note") % (fmt_num(nrv, lang), unit)) if nrv else "")
                                   + ((DU(lang, "atyp") % html.escape(atyp[0])) if atyp else ""))
    body = "\n".join([
        "<h2>%s</h2>\n%s" % (DU(lang, "role"), t["role"]),
        tables[0],
        record,
        "<h2>%s</h2>\n%s" % (DU(lang, "needs"), t["besoins"]),
    ] + tables[1:] + [
        "<h2>%s</h2>\n%s" % (DU(lang, "tips"), t["conseils"]),
        "<h2>%s</h2>\n<p>%s</p>" % (DU(lang, "method_h"), method),
    ])
    # Liens : articles liés, pages méthode liées, autres classements
    links = []
    idx = {a["slug"]: a for a in live_articles(lang)}
    for s in DATA_TEXTES[key].get("articles", []):
        if s in idx:
            links.append('<a href="%s">%s</a>' % (article_path(idx[s], lang), html.escape(article_view(idx[s], lang)["title"])))
    for s in DATA_TEXTES[key].get("methode", []):
        p = METHODE_IDX.get(s)
        if p and methode_path(p, lang):
            links.append('<a href="%s">%s</a>' % (methode_path(p, lang), html.escape(methode_view(p, lang)["label"])))
    more = ('\n  <div class="next">\n    <span class="label">%s</span>\n%s\n  </div>' % (DU(lang, "more"), "\n".join(links))) if links else ""
    others = "\n".join('<a href="%s">%s</a>' % (data_path(k, lang), html.escape(DATA_TEXTES[k][lang]["title"].split(":")[0].strip()))
                       for k in DATA_PAGES if k != key)
    og = None
    for s in DATA_TEXTES[key].get("articles", []):
        if s in ARTICLE_IDX and img_path(ARTICLE_IDX[s]):
            og = img_path(ARTICLE_IDX[s])
            break
    og = og or "/assets/og/journal.jpg"
    srcs = DATA_TEXTES[key].get("sources", [])
    jsonld = _json.dumps([
        {"@context": "https://schema.org", "@type": "Article", "headline": t["title"], "description": t["description"],
         "image": SITE + og, "datePublished": DATA_DATE, "dateModified": DATA_DATE, "inLanguage": lang,
         "author": AUTHOR_LD, "publisher": PUBLISHER_LD, "mainEntityOfPage": url,
         "isBasedOn": {"@type": "Dataset", "name": "Ciqual French food composition table 2025", "url": CIQUAL["doi"],
                       "creator": {"@type": "Organization", "name": "Anses"},
                       "license": "https://creativecommons.org/licenses/by/4.0/"},
         "citation": citation_ld(srcs)},
        {"@context": "https://schema.org", "@type": "BreadcrumbList", "itemListElement": [
            {"@type": "ListItem", "position": 1, "name": DU(lang, "crumb"), "item": SITE + data_hub_path(lang)},
            {"@type": "ListItem", "position": 2, "name": t["title"].split(":")[0].strip(), "item": url}]},
    ], ensure_ascii=False)
    return """<!doctype html>
<html lang="%(lang)s">
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
<meta property="og:title" content="%(title)s">
<meta property="og:description" content="%(desc)s">
<meta property="og:type" content="article">
<meta property="og:url" content="%(url)s">
%(ogimg)s
<script type="application/ld+json">%(jsonld)s</script>%(faqjsonld)s
%(i18n)s
<link rel="stylesheet" href="/assets/site.css">
</head>
<body>
%(nav)s
<main class="wrap">
<article class="methode data">
  <header>
    <nav class="crumbs" aria-label="%(crumbs_aria)s"><a href="%(hub)s">%(crumb)s</a><span aria-hidden="true">/</span><span>%(short)s</span></nav>
    <span class="label"><span class="gold">%(label)s</span></span>
    <h1>%(title)s</h1>
    <p class="standfirst">%(lead)s</p>
    %(byline)s
  </header>
%(body)s%(faqblock)s%(sources)s
  <div class="reward">
    <span class="label">%(u_rl)s</span>
    <h2>%(u_rh)s</h2>
    <p>%(u_rp)s</p>
    <a class="btn gold" href="/beta.html" onclick="track('data_cta_click',{page:'%(key)s',lang:'%(lang)s'})">%(u_cta)s</a>
  </div>%(more)s
  <div class="next">
    <span class="label">%(u_others)s</span>
%(others)s
  </div>
</article>
</main>
%(footer)s
%(posthog)s
<script>track('data_view',{page:'%(key)s',lang:'%(lang)s'});</script>
%(navscripts)s
</body>
</html>
""" % {"lang": lang, "csp": CSP, "icons": HEAD_ICONS, "metarobots": META_ROBOTS,
       "seo": html.escape(title_tag(t["seo_title"])), "desc": html.escape(t["description"], quote=True),
       "url": url, "title": html.escape(t["title"]), "ogimg": og_image_tags(og), "jsonld": jsonld,
       "faqjsonld": faqjsonld, "i18n": head_i18n(alt_fr, alt_en), "nav": nav("science", lang, alt_fr, alt_en),
       "crumbs_aria": U(lang, "crumbs_aria"), "hub": data_hub_path(lang), "crumb": DU(lang, "crumb"),
       "short": html.escape(t["title"].split(":")[0].strip()), "label": DU(lang, "label"), "lead": html.escape(lead),
       "byline": author_line(lang, DATA_DATE, None), "body": body, "faqblock": faqblock,
       "sources": sources_block(srcs, lang), "u_rl": U(lang, "reward_label"), "u_rh": DU(lang, "reward_h2"),
       "u_rp": DU(lang, "reward_p"), "u_cta": U(lang, "cta"), "key": key, "more": more,
       "u_others": DU(lang, "others"), "others": others,
       "footer": footer(lang), "posthog": POSTHOG, "navscripts": nav_scripts(lang)}


def data_hub(lang="fr"):
    items = []
    for k in DATA_PAGES:
        n, t = CIQUAL["nutrients"][k], DATA_TEXTES[k][lang]
        f = n["top"][0]
        items.append('<a class="entry" href="%s"><span class="etext"><span class="label meta"><span class="gold">%s</span></span>'
                     '<h2>%s</h2><p class="desc">%s</p><span class="readmore">%s</span></span></a>' % (
                         data_path(k, lang), DU(lang, "hub_label"), html.escape(t["title"]),
                         html.escape(DU(lang, "hub_top") % (food_name(f, lang), fmt_num(f["v"], lang), n["unit"])),
                         "Voir le classement →" if lang == "fr" else "See the ranking →"))
    path = data_hub_path(lang)
    jsonld = {"@context": "https://schema.org", "@type": "CollectionPage", "name": DU(lang, "hub_label"),
              "url": SITE + path, "inLanguage": lang, "description": DU(lang, "hub_desc"), "publisher": PUBLISHER_LD,
              "isBasedOn": {"@type": "Dataset", "name": "Ciqual French food composition table 2025", "url": CIQUAL["doi"],
                            "license": "https://creativecommons.org/licenses/by/4.0/"},
              "mainEntity": {"@type": "ItemList", "itemListElement": [
                  {"@type": "ListItem", "position": i + 1, "url": SITE + data_path(k, lang)} for i, k in enumerate(DATA_PAGES)]}}
    return """<!doctype html>
<html lang="%(lang)s">
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
%(i18n)s
<link rel="stylesheet" href="/assets/site.css">
</head>
<body>
%(nav)s
<main class="wrap">
  <div class="pagehead">
    <span class="label">%(label)s</span>
    <h1 class="display" style="margin-top:22px">%(h1)s</h1>
    <p>%(p)s</p>
    <div class="stats">
      <div><span class="n">%(n)d</span><span class="l label">%(n_l)s</span></div>
      <div><span class="n">%(foods)s</span><span class="l label">%(foods_l)s</span></div>
    </div>
  </div>
  <div class="journal">
%(items)s
  </div>
  <p class="disclaimer" style="text-align:left;margin:40px 0 0;max-width:none">%(attr)s</p>
</main>
%(footer)s
%(posthog)s
<script>track('data_hub_view',{lang:'%(lang)s'});</script>
%(navscripts)s
</body>
</html>
""" % {"lang": lang, "csp": CSP, "icons": HEAD_ICONS, "metarobots": META_ROBOTS,
       "seo": html.escape(title_tag(DU(lang, "hub_seo"))), "desc": html.escape(DU(lang, "hub_desc"), quote=True),
       "url": SITE + path, "ogimg": og_image_tags("/assets/og/journal.jpg"), "jsonld": ld(jsonld),
       "i18n": head_i18n(data_hub_path("fr"), data_hub_path("en")),
       "nav": nav("science", lang, data_hub_path("fr"), data_hub_path("en")),
       "label": DU(lang, "hub_label"), "h1": DU(lang, "hub_h1"), "p": DU(lang, "hub_p"),
       "n": len(DATA_PAGES), "n_l": DU(lang, "hub_n"), "foods": fmt_num(CIQUAL["n_foods"], lang), "foods_l": DU(lang, "hub_foods"),
       "items": "\n".join(items), "attr": DU(lang, "attribution"),
       "footer": footer(lang), "posthog": POSTHOG, "navscripts": nav_scripts(lang)}


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
    # Articles : clé "updated" si postérieure à la publication, sinon "date".
    root = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    entries = [("%s/" % SITE, git_lastmod("index.html")),
               ("%s/beta.html" % SITE, git_lastmod("beta.html")),
               ("%s/science.html" % SITE, git_lastmod("science.html")),
               ("%s/articles/" % SITE, git_lastmod("articles/index.html"))]
    for lang in LANGS_BUILT():
        if lang == "en":
            for rel, path in (("en/index.html", "/en/"), ("en/science.html", "/en/science.html"),
                              ("en/journal/index.html", "/en/journal/")):
                if os.path.exists(os.path.join(root, rel)):
                    entries.append((SITE + path, git_lastmod(rel)))
        entries += [(SITE + article_path(a, lang), modified(article_view(a, lang))) for a in live_articles(lang)]
        entries += [(SITE + methode_path(p, lang), methode_view(p, lang).get("updated", p["date"]))
                    for p in METHODE if methode_path(p, lang)]
        # Pages thème indexables (>= THEME_MIN_INDEX articles) : lastmod = article le plus récent.
        for d in DOMAINS:
            arts = theme_articles(d, lang)
            if len(arts) >= THEME_MIN_INDEX:
                entries.append((SITE + theme_path(d, lang), max(modified(article_view(a, lang)) for a in arts)))
        entries.append((SITE + ALT_ABOUT[0 if lang == "fr" else 1], ABOUT_UPDATED))
        if DATA_PAGES:
            entries.append((SITE + data_hub_path(lang), DATA_DATE))
            entries += [(SITE + data_path(k, lang), DATA_DATE) for k in DATA_PAGES]
    items = "\n".join(
        "  <url><loc>%s</loc>%s</url>" % (u, "<lastmod>%s</lastmod>" % d if d else "")
        for u, d in entries
    )
    return '<?xml version="1.0" encoding="UTF-8"?>\n<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">\n%s\n</urlset>\n' % items


def LANGS_BUILT():
    """Le français toujours ; l'anglais seulement quand i18n.EN_LIVE est vrai."""
    return ("fr", "en") if I.EN_LIVE else ("fr",)


def _write(root, rel, content):
    path = os.path.join(root, rel)
    os.makedirs(os.path.dirname(path), exist_ok=True)
    with open(path, "w") as f:
        f.write(content)


def _purge(dirpath, keep):
    """Retire les pages .html d'un dossier qui ne sont plus générées (article repassé
    en programmé, slug renommé) : sinon l'ancien HTML resterait servable et indexable."""
    if os.path.isdir(dirpath):
        for fn in os.listdir(dirpath):
            if fn.endswith(".html") and fn not in keep:
                os.remove(os.path.join(dirpath, fn))


def main():
    root = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    unknown = [s for s in SEO_TITLES if s not in {a["slug"] for a in ARTICLES_ALL}]
    if unknown:
        raise ValueError("SEO_TITLES : slugs inconnus %s" % unknown)
    if set(THEMES) != set(DOMAINS) or set(I.THEMES_EN) != set(DOMAINS):
        raise ValueError("THEMES et i18n.THEMES_EN doivent couvrir exactement DOMAINS")
    orphans = [s for s in I.EN_ARTICLES if s not in ARTICLE_IDX] + [s for s in I.EN_METHODE if s not in METHODE_IDX]
    if orphans:
        raise ValueError("pages anglaises sans version française : %s" % orphans)
    _write(root, "assets/site.css", CSS)
    for lang in LANGS_BUILT():
        arts = live_articles(lang)
        adir = os.path.join(root, "articles" if lang == "fr" else "en/journal")
        _purge(adir, {os.path.basename(article_path(a, lang)) for a in arts} | {"index.html"})
        for i, a in enumerate(arts):
            others = arts[i + 1:] + arts[:i]
            _write(root, article_path(a, lang).lstrip("/"), article_page(a, others, lang))
        _write(root, journal_path(lang).lstrip("/") + "index.html", index_page(lang))
        for d in DOMAINS:
            _write(root, theme_path(d, lang).lstrip("/") + "index.html", theme_page(d, lang))
        mps = [p for p in METHODE if methode_path(p, lang)]
        _purge(os.path.join(root, "methode" if lang == "fr" else "en/method"),
               {os.path.basename(methode_path(p, lang)) for p in mps})
        for p in mps:
            _write(root, methode_path(p, lang).lstrip("/"), methode_page(p, lang))
        _write(root, ALT_ABOUT[0 if lang == "fr" else 1].lstrip("/"), about_page(lang))
        _write(root, ALT_LEGAL[0 if lang == "fr" else 1].lstrip("/"), legal_page(lang))
        if DATA_PAGES:
            _purge(os.path.join(root, data_hub_path(lang).strip("/")),
                   {os.path.basename(data_path(k, lang)) for k in DATA_PAGES} | {"index.html"})
            _write(root, data_hub_path(lang).lstrip("/") + "index.html", data_hub(lang))
            for k in DATA_PAGES:
                _write(root, data_path(k, lang).lstrip("/"), data_page(k, lang))
        _write(root, "assets/" + ("nav-data.js" if lang == "fr" else "nav-data-en.js"), nav_data(lang))
    _write(root, "sitemap.xml", sitemap())
    _write(root, "llms.txt", llms_txt())
    _write(root, "llms-full.txt", llms_full())
    scheduled = len(ARTICLES_ALL) - len(ARTICLES)
    print("OK — %d articles publiés (%d programmés à venir), %d en anglais, %d pages méthode (%d en anglais), "
          "%d pages de données + index, sitemap, css, menus"
          % (len(ARTICLES), scheduled, len(live_articles("en")), len(METHODE),
             sum(1 for p in METHODE if methode_path(p, "en")), len(DATA_PAGES)))


if __name__ == "__main__":
    main()
