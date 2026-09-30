# -*- coding: utf-8 -*-
"""Site bilingue : textes d'interface, adresses FR/EN, routage par pays, contenus anglais.

Règle (demande du 30/09/2026) : un visiteur des pays francophones voit le site en
français, tous les autres le voient en anglais. Côté navigateur, sans appel réseau :
  1. choix mémorisé (bouton FR/EN → localStorage « ecleptic.lang ») ou ?lang=fr|en ;
  2. sinon langue du téléphone en français → français ;
  3. sinon fuseau horaire d'un pays francophone (France et outre-mer, Monaco, Maghreb,
     Afrique francophone, Haïti) → français ; Belgique, Suisse, Luxembourg et Canada
     sont multilingues : seule la langue du téléphone y décide ;
  4. sinon → anglais.
Les robots (Google, Bing, IA, aperçus de liens) ne sont jamais redirigés : chaque
version est indexée séparément, reliée à l'autre par hreflang (x-default = anglais).

Contenus anglais : tools/en/articles/*.py (ENTRIES, clé "fr" = slug français) et
tools/en/methode/*.py (PAGE, clé "fr"). Une page anglaise n'existe que si sa
version française est publiée ; les liens internes écrits en chemins français
sont réécrits vers leurs équivalents anglais au build.
"""
import glob, importlib.util, os, re

TOOLS = os.path.dirname(os.path.abspath(__file__))
LANGS = ("fr", "en")

# --- Interface ---------------------------------------------------------------
UI = {
    "fr": {
        "nav_home": "Accueil", "nav_journal": "Journal", "nav_science": "Science-Based", "nav_beta": "La b&ecirc;ta",
        "f_about": "&Agrave; propos", "f_legal": "Mentions l&eacute;gales", "f_privacy": "Confidentialit&eacute;",
        "f_contact": "Contact", "f_beta": "La b&ecirc;ta",
        "disclaimer": "Ecleptic est une application de bien-&ecirc;tre. Ses contenus ne remplacent pas un avis m&eacute;dical et ne constituent pas un dispositif m&eacute;dical.",
        "reward_label": "Pour aller plus loin",
        "reward_h2": "Ce que cet article explique,<br>l'app le mesure chez toi.",
        "reward_p": "Ecleptic croise ton sommeil, ton alimentation et ton entraînement en un seul score, chaque matin. La bêta iOS est ouverte à un petit cercle.",
        "cta": "Demander l'accès", "next": "À lire ensuite", "faq": "Questions fréquentes", "sources": "Sources",
        "refs": "Références", "min": "min",
        "by": "Par", "role": "fondateur d'Ecleptic", "updated": "mis à jour le",
        "m_kicker_engine": "Moteur %s &nbsp;&middot;&nbsp; La méthode", "m_kicker_fiche": "La mesure &nbsp;&middot;&nbsp; Fiche",
        "m_reward_label": "La suite logique", "m_reward_h2": "Tu viens de lire la méthode.<br>L'app l'applique à toi.",
        "m_more": "Pour aller plus loin", "crumbs_aria": "Fil d'Ariane",
        "j_title": "Le Journal : sommeil, nutrition, sport — Ecleptic",
        "j_desc": "Sommeil, nutrition, entraînement, récupération : des articles courts, scientifiques et actionnables pour optimiser ta santé au quotidien.",
        "j_ogdesc": "Sommeil, nutrition, entraînement, récupération : des conseils scientifiques et actionnables.",
        "j_label": "Journal de l'ISS", "j_h1": "Des jours<br>autrement<br><span class=\"gold\">pensés</span>.",
        "j_p": "Des textes sur le sommeil, l'alimentation, l'entraînement et l'art de construire des journées qui méritent d'être vécues.",
        "j_articles": "Articles", "j_themes": "Thèmes", "j_themes_label": "Thèmes du journal", "j_all": "Tout le journal",
        "j_quote": "« Chaque décision que tu prends — de ce que tu manges à ce que tu fais de ta soirée — fait de toi qui tu seras demain. »",
        "j_quote_by": "Chris Hadfield &nbsp;·&nbsp; Astronaute, commandant de l'ISS",
        "j_read": "Lire l'article →", "j_reward_label": "Et ensuite", "j_reward_h2": "Lire, c'est bien.<br>Mesurer, c'est mieux.",
        "j_reward_p": "Tout ce que le journal explique, l'app le suit automatiquement, sur tes propres données. La bêta iOS est ouverte à un petit cercle.",
        "j_empty": "Les premiers textes sont en préparation.<br>La station ouvre bientôt son journal.",
        "j_collection": "Le Journal d'Ecleptic",
        "t_label": "Le Journal &nbsp;&middot;&nbsp; Thème", "t_article": "Article", "t_articles": "Articles",
        "t_methode": "La méthode, côté app", "t_others": "Les autres thèmes",
        "t_empty": "Les premiers textes de ce thème arrivent bientôt.",
        "last_updated": "Dernière mise à jour : %s",
        "lang_name": "Français",
    },
    "en": {
        "nav_home": "Home", "nav_journal": "Journal", "nav_science": "Science-Based", "nav_beta": "The beta",
        "f_about": "About", "f_legal": "Legal notice", "f_privacy": "Privacy", "f_contact": "Contact", "f_beta": "The beta",
        "disclaimer": "Ecleptic is a wellness app. Its content does not replace medical advice, and it is not a medical device.",
        "reward_label": "Go further",
        "reward_h2": "What this article explains,<br>the app measures for you.",
        "reward_p": "Ecleptic brings your sleep, nutrition and training together in one score, every morning. The iOS beta is open to a small circle.",
        "cta": "Request access", "next": "Read next", "faq": "Frequently asked questions", "sources": "Sources",
        "refs": "References", "min": "min",
        "by": "By", "role": "founder of Ecleptic", "updated": "updated",
        "m_kicker_engine": "Engine %s &nbsp;&middot;&nbsp; The method", "m_kicker_fiche": "The measure &nbsp;&middot;&nbsp; Explainer",
        "m_reward_label": "The next step", "m_reward_h2": "You just read the method.<br>The app applies it to you.",
        "m_more": "Go further", "crumbs_aria": "Breadcrumb",
        "j_title": "The Journal: sleep, nutrition, training — Ecleptic",
        "j_desc": "Sleep, nutrition, training, recovery: short, science-based, actionable articles to improve your health day to day.",
        "j_ogdesc": "Sleep, nutrition, training, recovery: science-based, actionable advice.",
        "j_label": "The ISS Journal", "j_h1": "Days,<br>thought<br><span class=\"gold\">differently</span>.",
        "j_p": "Writing on sleep, food, training, and the craft of building days worth living.",
        "j_articles": "Articles", "j_themes": "Themes", "j_themes_label": "Journal themes", "j_all": "The whole journal",
        "j_quote": "", "j_quote_by": "",
        "j_read": "Read the article →", "j_reward_label": "What's next", "j_reward_h2": "Reading is good.<br>Measuring is better.",
        "j_reward_p": "Everything the journal explains, the app tracks automatically, on your own data. The iOS beta is open to a small circle.",
        "j_empty": "The first articles are on their way.",
        "j_collection": "The Ecleptic Journal",
        "t_label": "The Journal &nbsp;&middot;&nbsp; Theme", "t_article": "Article", "t_articles": "Articles",
        "t_methode": "The method, in the app", "t_others": "Other themes",
        "t_empty": "The first articles in this theme are coming soon.",
        "last_updated": "Last updated: %s",
        "lang_name": "English",
    },
}

MONTHS = {
    "fr": ["janvier", "février", "mars", "avril", "mai", "juin", "juillet", "août", "septembre", "octobre", "novembre", "décembre"],
    "en": ["January", "February", "March", "April", "May", "June", "July", "August", "September", "October", "November", "December"],
}


def date_label(iso, lang):
    y, m, d = iso.split("-")
    if lang == "en":
        return "%s %d, %s" % (MONTHS["en"][int(m) - 1], int(d), y)
    return "%d %s %s" % (int(d), MONTHS["fr"][int(m) - 1], y)


# --- Thèmes en anglais (clé = nom français du domaine) --------------------------
THEMES_EN = {
    "Sommeil": {"name": "Sleep", "slug": "sleep",
                "seo": "Sleep: our articles to sleep better — Ecleptic",
                "desc": "Sleep duration, deep sleep, caffeine, screens, waking at night: short, science-based articles to understand your sleep and sleep better tonight.",
                "intro": "Sleep drives everything else: your recovery, your appetite, your mood, your progress in training. Here we answer the real questions (how many hours you need, how to get more deep sleep, when to stop caffeine, what to do when you wake at 3 a.m.) with straight answers, numbers from the research, and what you can change tonight."},
    "Readiness": {"name": "Readiness", "slug": "readiness",
                  "seo": "Readiness score, HRV and resting heart rate — Ecleptic",
                  "desc": "Readiness score, resting heart rate, low HRV, rest days: how to read your body's signals every morning and decide whether to push or recover.",
                  "intro": "Every morning your body sends measurable signals: your heart rate variability, your resting heart rate, the quality of your night. Read against your own baseline, they tell you whether you can push or should back off. These articles teach you to read them without getting fooled: what is normal, what should worry you, and how to bring the numbers up for good."},
    "Sport": {"name": "Training", "slug": "training",
              "seo": "Training: how to make progress, our articles — Ecleptic",
              "desc": "Sessions per week, zone 2, VO2 max, reps, cardio or weights: clear, science-based articles to train smarter, make progress and stay consistent.",
              "intro": "Progress does not come from training more, but from training better: the right frequency, the right intensity, and enough variety for your body to adapt. Zone 2, VO2 max, number of sessions, reps, cardio or weights: each article starts from a concrete question and answers it straight, with what the research says and how to apply it to your week."},
    "Récupération": {"name": "Recovery", "slug": "recovery",
                     "seo": "Recovery after exercise: our articles — Ecleptic",
                     "desc": "Sore muscles, HRV, cold baths, sauna, stretching, massage: what really speeds up recovery after exercise, what does nothing, and why.",
                     "intro": "You do not get fitter during the session, but during the recovery that follows it. Soreness, cold baths, sauna, stretching, massage: recovery is full of promises. We sort them out: what really speeds up your return to form, what soothes without changing much, and what your heart rate variability says about the state of your body."},
    "Alimentation": {"name": "Nutrition", "slug": "nutrition",
                     "seo": "Nutrition for training: our articles — Ecleptic",
                     "desc": "Calories, protein, calorie deficit, creatine, hydration, meals around training: clear numbers, with sources, to eat well for your goal.",
                     "intro": "Eating well for your goal comes down to a few solid benchmarks: how many calories, how much protein, what to eat before and after training, how much to drink. These articles give you the numbers, drawn from official databases and nutrition research, and how to adapt them to you, with no miracle diet and no forbidden food."},
    "Charge": {"name": "Training load", "slug": "training-load",
               "seo": "Training load: how to dose your sessions — Ecleptic",
               "desc": "Overtraining, progressive overload, rest between sets, RPE, deload weeks: how to dose your training load to make progress without getting injured.",
               "intro": "Training load is what your sessions ask of your body, week after week. Too little and you stall; too much and you burn out or get injured. Progressive overload, overtraining, rest times, perceived exertion: these articles help you dose it, spot the warning signs and build progress that lasts."},
    "Régularité": {"name": "Consistency", "slug": "consistency",
                   "seo": "Consistency and habits: our articles — Ecleptic",
                   "desc": "Bedtimes, evening routine, jet lag, habits that stick: why consistency matters as much as duration, and how to build it into your days.",
                   "intro": "Your body runs on a clock. Going to bed, waking up, eating and training at regular times keeps it well set, and everything else benefits: sleep, energy, appetite. These articles explain why consistency sometimes matters more than duration, and how to keep it despite jet lag, night shifts or busy weeks."},
    "Humeur": {"name": "Mood", "slug": "mood",
               "seo": "Stress, mood and recovery: our articles — Ecleptic",
               "desc": "Stress, anxiety, cortisol, breathing, irritability: what your mind does to your recovery, and the simple levers that genuinely help every day.",
               "intro": "Your nervous system cannot tell a crunch week at work from a heavy training week: mental stress is paid for in recovery too. These articles cover stress, anxiety, cortisol and mood, and the simple levers that help, from exercise to breathing. They are no substitute for a professional: if you are going through a hard time, talk to your doctor; in a crisis, call your local emergency number or a crisis line (988 in the US, 116 123 in the UK and Ireland)."},
    "Contexte": {"name": "Context", "slug": "context",
                 "seo": "Alcohol, age, cycle, heat: context matters — Ecleptic",
                 "desc": "Alcohol, illness, menstrual cycle, age, smoking, heat, altitude: the factors that change your recovery and performance, and how to adapt to them.",
                 "intro": "The same sessions and the same nights do not give the same results depending on your context: a drink the night before, an illness coming on, your cycle, your age, heat, altitude. These articles explain how each of these weighs on your body, and how to adjust your training and recovery instead of fighting it."},
    "Énergie": {"name": "Energy", "slug": "energy",
                "seo": "Fatigue and energy: our articles — Ecleptic",
                "desc": "Constant fatigue, the afternoon slump, naps, iron deficiency, blood sugar: where your tiredness comes from and how to get steady energy all day.",
                "intro": "Fatigue that lasts almost always has a cause you can find: nights that are too short, irregular hours, badly timed meals, a lack of iron, too much training load. These articles help you trace it, from the 2 p.m. slump to tiredness that settles in, and get back to steady energy. If the fatigue persists anyway, see your doctor for a check-up."},
}

METHODE_EN_SLUG = {
    "readiness-score": "readiness-score", "age-biologique": "biological-age", "nutrition": "nutrition",
    "vitaux": "vitals", "cibles": "targets", "variabilite-cardiaque": "heart-rate-variability",
    "frequence-cardiaque-repos": "resting-heart-rate", "vo2max": "vo2max", "frequence-respiratoire": "respiratory-rate",
    "saturation-oxygene": "blood-oxygen", "temperature-poignet": "wrist-temperature", "ligne-de-base": "baseline",
    "besoin-de-sommeil": "sleep-need", "depense-energetique": "energy-expenditure",
}

# Pages fixes : chemin français → chemin anglais (hreflang, bouton FR/EN, réécriture des liens).
STATIC = {
    "/": "/en/", "/science.html": "/en/science.html", "/articles/": "/en/journal/",
    "/a-propos.html": "/en/about.html", "/mentions-legales.html": "/en/legal-notice.html",
    "/confidentialite.html": "/en/privacy.html", "/guide": "/en/guide", "/guide.html": "/en/guide",
    "/donnees/": "/en/data/", "/comparatifs/": "/en/compare/",
}


# --- Contenus anglais --------------------------------------------------------
def _load_dir(sub, attr):
    out = []
    for f in sorted(glob.glob(os.path.join(TOOLS, "en", sub, "*.py"))):
        if os.path.basename(f).startswith("_"):
            continue
        spec = importlib.util.spec_from_file_location("en_%s_%s" % (sub, os.path.basename(f)[:-3]), f)
        mod = importlib.util.module_from_spec(spec)
        spec.loader.exec_module(mod)
        val = getattr(mod, attr, None)
        if attr == "PAGE" and val is None:
            val = getattr(mod, "PAGES", [])
        out.extend(val if isinstance(val, list) else [val] if val else [])
    return out


EN_ARTICLES = {e["fr"]: e for e in _load_dir("articles", "ENTRIES")}
EN_METHODE = {p["fr"]: p for p in _load_dir("methode", "PAGE")}


# --- Routage et sélecteur de langue ------------------------------------------
FRANCOPHONE_TZ = [
    # France, Monaco et outre-mer
    "Europe/Paris", "Europe/Monaco", "America/Martinique", "America/Guadeloupe", "America/Cayenne",
    "America/St_Barthelemy", "America/Marigot", "America/Miquelon", "Indian/Reunion", "Indian/Mayotte",
    "Pacific/Noumea", "Pacific/Tahiti", "Pacific/Marquesas", "Pacific/Gambier", "Pacific/Wallis", "Indian/Kerguelen",
    # Maghreb
    "Africa/Casablanca", "Africa/El_Aaiun", "Africa/Algiers", "Africa/Tunis",
    # Afrique francophone, océan Indien, Haïti
    "Africa/Abidjan", "Africa/Dakar", "Africa/Bamako", "Africa/Ouagadougou", "Africa/Niamey", "Africa/Conakry",
    "Africa/Lome", "Africa/Porto-Novo", "Africa/Douala", "Africa/Libreville", "Africa/Brazzaville", "Africa/Kinshasa",
    "Africa/Lubumbashi", "Africa/Bangui", "Africa/Ndjamena", "Africa/Nouakchott", "Africa/Djibouti", "Africa/Kigali",
    "Africa/Bujumbura", "Indian/Antananarivo", "Indian/Comoro", "Indian/Mahe", "Indian/Mauritius", "America/Port-au-Prince",
]

# Script en fin de <head> : redirige un visiteur (jamais un robot) vers la version de
# sa langue, à partir des <link rel="alternate" hreflang> de la page. Garde ?utm_… et #.
ROUTER_JS = r"""<script>
(function(){try{
  var d=document.documentElement,page=d.lang,ls=window.localStorage,ua=navigator.userAgent||'';
  document.addEventListener('click',function(e){var a=e.target.closest&&e.target.closest('[data-setlang]');if(a){try{ls.setItem('ecleptic.lang',a.getAttribute('data-setlang'))}catch(_){}}});
  if(/bot|crawl|spider|slurp|google|bing|yandex|baidu|duckduck|facebook|whatsapp|telegram|twitter|linkedin|slack|discord|embed|preview|lighthouse|headless|pagespeed|gtmetrix|semrush|ahrefs|gpt|openai|oai-|perplexity|claude|anthropic|ccbot|applebot|amazonbot|bytespider|petal|mistral|cohere/i.test(ua))return;
  var m=location.search.match(/[?&]lang=(fr|en)\b/),want=m?m[1]:null;
  if(want){try{ls.setItem('ecleptic.lang',want)}catch(_){}}
  if(!want){try{want=ls.getItem('ecleptic.lang')}catch(_){}}
  if(!want){
    var langs=(navigator.languages&&navigator.languages.length?navigator.languages:[navigator.language||'']);
    var tz='';try{tz=Intl.DateTimeFormat().resolvedOptions().timeZone||''}catch(_){}
    want=(/^fr\b/i.test(langs[0]||'')||%s.indexOf(tz)>=0)?'fr':'en';
  }
  if(want===page)return;
  var alt=document.querySelector('link[rel="alternate"][hreflang="'+want+'"]');
  if(!alt)return;
  var q=location.search.replace(/([?&])lang=(fr|en)\b&?/,'$1').replace(/[?&]$/,'');
  location.replace(alt.href+q+location.hash);
}catch(e){}})();
</script>""" % ("[" + ",".join("'%s'" % z for z in FRANCOPHONE_TZ) + "]")


def alt_links(fr_path, en_path, site):
    """<link rel="alternate" hreflang> pour une page qui existe dans les deux langues."""
    if not (fr_path and en_path):
        return ""
    return ('<link rel="alternate" hreflang="fr" href="%s%s">\n'
            '<link rel="alternate" hreflang="en" href="%s%s">\n'
            '<link rel="alternate" hreflang="x-default" href="%s%s">' % (site, fr_path, site, en_path, site, en_path))


def switcher(lang, fr_path, en_path):
    """Bouton FR · EN du bandeau (vers la page équivalente, sinon l'accueil de l'autre langue)."""
    fr = fr_path or "/"
    en = en_path or "/en/"
    return ('<span class="langsw"><a href="%s" hreflang="fr" lang="fr" data-setlang="fr"%s>FR</a>'
            '<a href="%s" hreflang="en" lang="en" data-setlang="en"%s>EN</a></span>'
            % (fr, ' class="on" aria-current="true"' if lang == "fr" else "",
               en, ' class="on" aria-current="true"' if lang == "en" else ""))
