# Version anglaise des guides pour les coachs

Les guides français (tools/coachs/batch_*.py) parlent à un coach français. La version anglaise parle à un coach indépendant anglophone, partout dans le monde : Royaume-Uni, États-Unis, Canada, Australie, Irlande. Ce n'est pas une traduction : c'est le même guide, réécrit pour que tout y soit vrai et utile pour ce lecteur.

Lis d'abord tools/en/_brief-traduction.md pour le ton, les unités et les structures (« The short answer: », « Key takeaways »). Là où les deux documents divergent, celui-ci prévaut.

## Règle centrale
- Retire tout ce qui ne vaut qu'en France : code du sport, carte professionnelle, BPJEPS, URSSAF, micro-entreprise, TVA, CNIL, DGCCRF, code de la consommation, Insee, CSE, DGFiP.
- Là où le guide français donne une règle française, écris une phrase générale et vraie : « Check the rules where you work: qualification, insurance and consumer law vary by country. » Une fois par guide, pas plus.
- N'invente rien pour remplacer : aucune loi étrangère, aucun taux, aucun organisme, aucun chiffre qui ne soit pas dans le français. Pas de NASM, REPs, ACE ou IRS si le français n'en parle pas.
- Le RGPD peut rester sous la forme « if you work in the EU or the UK, health data is specially protected », sans citer d'autorité française.
- Garde les méthodes, les exemples de calcul présentés comme des exemples, les études et les protocoles, avec leurs chiffres exacts.
- Les règles de Google et de Meta restent : elles valent partout.
- Vocabulaire : « client », « personal trainer » ou « coach », « online coaching ». Titres et h2 = vraies requêtes anglaises. Jamais « Ecleptic » dans le corps.
- Pas de tirets cadratins, pas de « it's not X, it's Y », pas de formules creuses.

## Quand ne pas traduire
Si, après retrait de ce qui ne vaut qu'en France, le guide n'apporte plus assez à un coach anglophone, ne l'écris pas et dis-le dans ton rapport. C'est un bon résultat : un guide faible hors contexte fait plus de mal que de bien. Exemple typique : un guide dont le cœur est une donnée française, ou une comparaison d'outils surtout vendus en France.

## Format, un fichier par traducteur
```python
# -*- coding: utf-8 -*-
ENTRIES = [
    {
        "fr": "tests-physiques-nouveau-client",   # slug français
        "slug": "fitness-tests-for-new-clients",  # celui de tools/en/slugs.py, obligatoire
        "title": "…",                             # garde la forme « Prefix: rest » si le français l'a
        "seo_title": "…",                         # si le titre dépasse 60 caractères, 60 au plus
        "description": "…",                       # 140 à 160 caractères
        "body": """…""",
        "faq": [{"q": "…", "a": "…"}, …],         # 3 questions
        "sources": [{"t": "…", "u": "…"}, …],     # OBLIGATOIRE : au moins 2, seulement celles du français qui soutiennent ce qui reste
    },
]
```

## Liens
Garde les liens du français qui restent pertinents, avec leurs chemins français (/coachs/<slug-fr>.html, /articles/<slug-fr>.html, /methode/<slug-fr>.html). Le générateur les réécrit, et retire ceux dont la cible n'a pas de version anglaise. N'en ajoute aucun.

## Contrôles jusqu'à zéro erreur
Depuis /Users/augustephilypriou/Desktop/Auros/landing-coachs :
```bash
python3 -c "import ast,sys; ast.parse(open(sys.argv[1]).read())" tools/en/coachs/batch_<n>.py
python3 tools/check_en.py tools/en/coachs/batch_<n>.py
```
Le texte adapté peut faire de 55 à 130 % du français.

## Ton périmètre
Tu crées UNIQUEMENT ton fichier tools/en/coachs/batch_<n>.py. Pas de build, pas de git.

## Rapport, 8 lignes au plus
Guides écrits, guides non traduits avec la raison, doutes, résultat du contrôle.
