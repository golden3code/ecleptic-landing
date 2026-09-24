<!-- Cahier des charges des pages /methode/ (Science-Based), utilisé le 24/09/2026 pour rédiger les 13 pages
     via des sous-agents. Non chargé par le build (seuls tools/methode/*.py le sont). Pour ajouter une page :
     écrire tools/methode/<slug>.py au format PAGE, lancer le validateur ci-dessous, puis python3 tools/build_articles.py. -->

# Cahier des charges — pages « La méthode » (Science-Based) d'ecleptic.health

Ecleptic est une app iOS (bien-être, PAS un dispositif médical) qui croise sommeil, alimentation et entraînement. Le site public ecleptic.health a une page hub « Science-Based » (/science.html) qui présente 5 moteurs. Chaque moteur devient une page complète, et les notions clés ont leurs propres « fiches ». Tu rédiges certaines de ces pages.

## Ta sortie
Un fichier Python par page, dans `/Users/augustephilypriou/Desktop/Auros/landing/tools/methode/`, nommé d'après le slug avec des underscores (ex. `variabilite_cardiaque.py`). Chaque fichier expose `PAGE = {...}`.

**AVANT d'écrire, lis en entier la page modèle `tools/methode/readiness_score.py`** : copie sa structure (docstring d'en-tête, champs, HTML), son ton et sa mise en forme.

N'édite AUCUN autre fichier. Pas de commande git. Ne lance pas `tools/build_articles.py` (il échouera tant que toutes les pages liées n'existent pas) : utilise le validateur ci-dessous.

## Champs de PAGE
- `slug` (exactement celui donné), `kind` ("moteur" ou "fiche"), `num` (chiffre romain, moteurs uniquement ; pour une fiche : `None`), `order` (entier donné), `label` (nom court donné, exact), `date`: "2026-09-24".
- `title` : le H1, affiché en capitales. Court, clair (≤ 60 caractères). Pas de deux-points.
- `seo_title` : titre de l'onglet et de Google, ≤ 70 caractères, qui finit par « — Ecleptic ».
- `description` : 140 à 160 caractères, contient le mot-clé principal, promet ce que la page explique.
- `lead` : 1 à 2 phrases d'accroche, texte brut (tu peux mettre du `<strong>`), SANS `<p>`.
- `body` : HTML entre triple guillemets. Uniquement `<h2>`, `<p>`, `<ul><li>`, `<strong>`, `<em>` (rare), `<a href>`, et au plus un bloc chiffres-clés :
  `<div class="figs">` + 3 à 5 `<div><span class="v">CHIFFRE</span><span class="u">légende courte</span></div>` + `</div>`.
- `refs` : 2 à 5 références, UNIQUEMENT dans la liste blanche ci-dessous, au format « Auteur X. et al. (année), sujet en français, <em>Revue</em>. »
- `faq` : 3 dicts `{"q": ..., "a": ...}` — questions formulées comme de vraies recherches Google (différentes des h2), réponses de 2 à 3 phrases autonomes.
- `related` : 3 à 6 slugs d'autres pages « méthode » (liste ci-dessous).
- `journal` : 2 à 4 slugs d'articles du Journal (liste ci-dessous) — ils n'apparaissent qu'une fois publiés.

## Ton et style
- Français, tutoiement, voix d'un fondateur passionné mais rigoureux. Précis, concret, zéro remplissage.
- À la différence des articles du Journal, ces pages PARLENT de l'app : dis « l'app » ou « Ecleptic » et explique exactement ce qu'elle fait, avec les chiffres réels de la fiche de faits. C'est la promesse de la section : « Rien n'est inventé. »
- Paragraphes courts, 5 à 8 `<h2>`, listes `<li><strong>Repère :</strong> explication</li>`.
- Longueur du body (texte hors balises) : **moteur 900 à 1 400 mots**, **fiche 650 à 1 000 mots**.
- Structure conseillée d'une FICHE : définition en une phrase → ce que ça reflète dans le corps → comment on la mesure (labo vs montre) → valeurs de repère et pourquoi elles varient d'une personne à l'autre → ce qui la fait bouger → comment Ecleptic la lit et l'utilise (chiffres réels) → limites de la mesure → quand consulter.
- Structure conseillée d'un MOTEUR : ce que le moteur calcule → les données d'entrée → la méthode pas à pas (chiffres réels) → pourquoi ces choix → ce que tu vois dans l'app → limites / ce que ce n'est pas.

## Exactitude (non négociable)
- Tout ce qui concerne l'app vient de TA fiche de faits (dans ton prompt). N'invente aucune fonctionnalité, aucun chiffre, aucun écran. En cas de doute, reste général.
- Physiologie générale : faits consensuels et chiffres ronds établis uniquement ; aucune étude, aucun auteur, aucune statistique inventée.
- Garde-fous : aucun diagnostic, aucune posologie ; Ecleptic n'est pas un dispositif médical ; valeur anormale qui persiste ou symptômes (malaise, douleur thoracique, essoufflement anormal, palpitations…) → consulter un médecin ; urgence → 15 ou 112.

## Liens autorisés
- Pages méthode (`/methode/<slug>.html`) — slug · label · kind · order :
  readiness-score · Le Readiness Score · moteur I · 1
  age-biologique · L'âge biologique · moteur II · 2
  nutrition · La nutrition · moteur III · 3
  vitaux · Les vitaux · moteur IV · 4
  cibles · Les cibles · moteur V · 5
  variabilite-cardiaque · La variabilité cardiaque (HRV) · fiche · 1
  frequence-cardiaque-repos · La fréquence cardiaque au repos · fiche · 2
  vo2max · La VO₂max · fiche · 3
  frequence-respiratoire · La fréquence respiratoire · fiche · 4
  saturation-oxygene · La saturation en oxygène (SpO₂) · fiche · 5
  temperature-poignet · La température du poignet · fiche · 6
  ligne-de-base · Ta ligne de base · fiche · 7
  besoin-de-sommeil · Ton besoin de sommeil · fiche · 8
  depense-energetique · La dépense énergétique (TDEE) · fiche · 9
- Articles du Journal (`/articles/<slug>.html`) : tous les slugs de `tools/build_articles.py` et de `tools/satellites/*.py` (publiés ou programmés : un lien vers un article pas encore publié est neutralisé au build jusqu'à sa date).
- 3 à 8 liens internes dans le body, naturellement intégrés. Relie les fiches à leur moteur et inversement.

## Faits communs sur l'app (vérifiés dans le code)
- **Readiness Score** (moteur I) : 4 piliers — vitaux de la nuit 42 pts (HRV 45 %, FC repos 30 %, fréquence respiratoire 12 %, SpO₂ 7 %, température du poignet 6 %), sommeil 21 (durée vs besoin 40 %, phases profond+paradoxal 25 %, efficacité 20 %, régularité 15 %), nutrition 21 (adéquation aux cibles 40 %, refuel post-séance 25 %, micronutriments 20 %, hydratation 15 % ; alcool la veille → pilier plafonné à 80), rythme et charge 16 (charge aiguë/chronique 40 %, régularité des rythmes 30 %, cadence 20 %, courbatures 10 %). Donnée absente → retirée et son poids redistribué + indice de confiance. Score calculé au réveil puis mis à jour au fil de la journée.
- **Ligne de base** : pour chaque signal, moyenne et écart-type sur les 42 derniers jours (~6 semaines), jour évalué EXCLU ; minimum 7 jours pour exister, confiance pleine à 28 jours ; la valeur du jour est convertie en écart à ta normale (en écarts-types, « z-score ») puis en points. Sens : HRV et SpO₂ plus hautes = mieux ; FC repos et fréquence respiratoire plus basses = mieux ; température : tout écart, dans un sens ou dans l'autre, pénalise (au-delà de 2 écarts-types, 0 point pour ce signal).
- **Mesures lues dans Apple Santé** (données de la montre) : variabilité cardiaque (SDNN, en ms), fréquence cardiaque au repos, fréquence respiratoire, saturation en oxygène, température du poignet pendant le sommeil, VO₂max (« forme cardio »). Sans montre : pas de vitaux, leur poids est redistribué.
- Le site dit « l'app » ou « Ecleptic ». Bêta iOS sur iPhone via TestFlight.

## Liste blanche des références (n'en cite aucune autre)
- Task Force de la Société européenne de cardiologie et de la NASPE (1996), normes de mesure de la variabilité cardiaque, <em>Circulation</em>.
- Shaffer F. et Ginsberg J. P. (2017), panorama des indicateurs et des normes de variabilité cardiaque, <em>Frontiers in Public Health</em>.
- Nunan D. et al. (2010), valeurs normales de la variabilité cardiaque de courte durée chez l'adulte sain, <em>Pacing and Clinical Electrophysiology</em>.
- Plews D. J. et al. (2013), suivi de la variabilité cardiaque et adaptation à l'entraînement chez l'athlète d'endurance, <em>Sports Medicine</em>.
- Buchheit M. (2014), suivi de l'état d'entraînement par les mesures de fréquence cardiaque, <em>Frontiers in Physiology</em>.
- Fox K. et al. (2007), la fréquence cardiaque de repos dans les maladies cardiovasculaires, <em>Journal of the American College of Cardiology</em>.
- Jensen M. T. et al. (2013), fréquence cardiaque de repos, condition physique et mortalité (Copenhagen Male Study), <em>Heart</em>.
- Nes B. M. et al. (2011), estimation de la VO₂pic sans test d'effort : l'étude HUNT, <em>Medicine &amp; Science in Sports &amp; Exercise</em>.
- Nes B. M. et al. (2014), un modèle simple de capacité cardiorespiratoire sans effort prédit la mortalité à long terme, <em>Medicine &amp; Science in Sports &amp; Exercise</em>.
- Kodama S. et al. (2009), la capacité cardiorespiratoire comme prédicteur de la mortalité toutes causes, <em>JAMA</em>.
- Mandsager K. et al. (2018), capacité cardiorespiratoire et mortalité à long terme, <em>JAMA Network Open</em>.
- Jackson A. S. et al. (1990), prédiction de la capacité aérobie sans test d'effort, <em>Medicine &amp; Science in Sports &amp; Exercise</em>.
- Daniels J. et Gilbert J. (1979), tables de performance VDOT, <em>Oxygen Power</em>.
- Mifflin M. D., St Jeor S. T. et al. (1990), nouvelle équation du métabolisme de repos chez l'adulte sain, <em>American Journal of Clinical Nutrition</em>.
- Hall K. D. et al. (2011), quantification de l'effet d'un déséquilibre énergétique sur le poids, <em>The Lancet</em>.
- Hirshkowitz M. et al. (2015), recommandations de durée de sommeil de la National Sleep Foundation, <em>Sleep Health</em>.
- Windred D. P. et al. (2024), la régularité du sommeil prédit mieux la mortalité que sa durée, <em>Sleep</em>.
- Miller D. J. et al. (2020), variations de la fréquence respiratoire nocturne et détection précoce d'une infection, <em>PLOS ONE</em>.
- OMS (2011), tour de taille et rapport taille-hanches : rapport d'une consultation d'experts.
- OMS (2020), lignes directrices sur l'activité physique et la sédentarité.
- OMS (2011), manuel de formation à l'oxymétrie de pouls.
- ANSES, table de composition nutritionnelle des aliments Ciqual.
- USDA, base de données FoodData Central.
- Open Food Facts, base collaborative de produits alimentaires.

## Validateur (à lancer, corriger jusqu'à « OK » sur chacune de tes pages)
```
cd /Users/augustephilypriou/Desktop/Auros/landing && PYTHONDONTWRITEBYTECODE=1 python3 - FICHIER1.py FICHIER2.py <<'PY'
import sys, re, importlib.util
import glob as _g
JOURNAL = set()
for _f in ["tools/build_articles.py"] + _g.glob("tools/satellites/*.py"):
    JOURNAL |= set(re.findall(r'"slug": "([a-z0-9-]+)"', open(_f).read()))
METH = set("readiness-score age-biologique nutrition vitaux cibles variabilite-cardiaque frequence-cardiaque-repos vo2max frequence-respiratoire saturation-oxygene temperature-poignet ligne-de-base besoin-de-sommeil depense-energetique".split())
for f in sys.argv[1:]:
    spec = importlib.util.spec_from_file_location("m", "tools/methode/" + f); m = importlib.util.module_from_spec(spec); spec.loader.exec_module(m)
    p = m.PAGE; pb = []
    for k in ("slug","kind","num","order","label","title","seo_title","description","lead","body","refs","faq","related","journal","date"):
        if k not in p: pb.append("champ manquant " + k)
    w = len(re.sub(r"<[^>]+>", " ", p["body"]).split())
    lo, hi = (900, 1400) if p["kind"] == "moteur" else (650, 1000)
    if not lo <= w <= hi: pb.append("mots %d hors [%d-%d]" % (w, lo, hi))
    if not 140 <= len(p["description"]) <= 160: pb.append("description %d car." % len(p["description"]))
    if len(p["seo_title"]) > 70 or not p["seo_title"].endswith("— Ecleptic"): pb.append("seo_title")
    if len(p["title"]) > 60 or ":" in p["title"]: pb.append("title")
    if "<p" in p["lead"]: pb.append("lead contient <p>")
    if len(p["faq"]) != 3: pb.append("faq != 3")
    if not 2 <= len(p["refs"]) <= 5: pb.append("refs")
    ml = re.findall(r'href="/methode/([a-z0-9-]+)\.html"', p["body"]); al = re.findall(r'href="/articles/([a-z0-9-]+)\.html"', p["body"])
    bad = [x for x in ml if x not in METH] + [x for x in al if x not in JOURNAL] + [x for x in p["related"] if x not in METH] + [x for x in p["journal"] if x not in JOURNAL]
    if bad: pb.append("liens inconnus %s" % bad)
    if not 3 <= len(ml) + len(al) <= 8: pb.append("liens internes %d" % (len(ml) + len(al)))
    if re.search(r"<(?!/?(h2|p|ul|li|strong|em|a|div|span)\b)[a-z]", p["body"]): pb.append("balise non autorisée")
    print(f, p["slug"], "| mots", w, "| desc", len(p["description"]), "| liens", len(ml) + len(al), "|", "OK" if not pb else pb)
PY
```
Termine par un compte rendu bref : pour chaque page, slug, mots, description, et les faits de l'app que tu as utilisés.
