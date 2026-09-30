# Cahier des charges — version anglaise des articles du Journal

Le site ecleptic.health devient bilingue : un visiteur hors pays francophones voit tout le site
en anglais. Chaque article français (tools/satellites/batch_<x>.py, déjà sourcé) reçoit sa
version anglaise dans tools/en/articles/batch_<x>.py. L'objectif est d'être cité par Google,
ChatGPT, Perplexity et Claude dans les réponses EN ANGLAIS : ce n'est pas une traduction mot à
mot, c'est l'article qu'un rédacteur santé anglophone aurait écrit avec les mêmes faits.

## Format du fichier à créer
```python
# -*- coding: utf-8 -*-
ENTRIES = [
    {
        "fr": "sieste-ideale-duree",                 # slug français (clé de l'article)
        "slug": "ideal-nap-length",                  # OBLIGATOIRE : celui de tools/en/slugs.py (EN_SLUGS)
        "title": "Ideal nap length: how long should you nap?",
        "seo_title": "…",                            # facultatif : seulement si title dépasse 60 caractères
        "description": "…",                          # 140 à 160 caractères
        "body": """…""",                             # HTML, même structure que le français
        "faq": [{"q": "…", "a": "…"}, …],            # même nombre de questions que le français
    },
]
```
Ne mets PAS de clé "sources" : les sources françaises (déjà en langue d'origine, souvent l'anglais)
sont reprises automatiquement. Exception : si une source est un document uniquement en français
(ANSES, HAS, Santé publique France, INSV…), garde-la quand même (elle reste valable) — ne la remplace
pas.

## Langue et ton
- Anglais américain (spelling « fiber, color, program »), naturel, direct ; « you » (le « tu » du
  français), voix du fondateur, phrases courtes. Jamais le mot « Ecleptic » dans le corps.
- Titre et h2 = les vraies requêtes anglaises (« How many hours of sleep do you need? »,
  « What is zone 2 cardio? »). Le h1 garde la forme « Préfixe : suite » quand le français l'a
  (« Ideal nap length: … ») — c'est ce qui déclenche l'animation du titre.
- Structures fixes : « La réponse courte : » → « The short answer: » ; « Ce qu'il faut retenir » →
  « Key takeaways » (3 puces) ; les attributions : « selon l'American Academy of Sleep Medicine » →
  « according to the American Academy of Sleep Medicine », « une méta-analyse de 2018 (49 essais,
  1 863 participants) » → « a 2018 meta-analysis (49 trials, 1,863 participants) ».
- Chiffres : point décimal et virgule des milliers (1.6 g, 1,863) ; unités métriques d'abord, avec
  l'équivalent impérial entre parenthèses quand il aide un lecteur américain (70 kg (154 lb),
  18 °C (64 °F), 2 L (about 68 oz)), une fois par article et par grandeur, pas partout.
- Références françaises : explique-les une fois (« ANSES, France's food safety agency »).
- Aucun fait, chiffre, nuance ou garde-fou ne doit changer, disparaître ou apparaître.

## Garde-fous santé (adaptés au lecteur international)
- 3114 (prévention du suicide, France) → « if you are in crisis, call your local emergency number
  or a crisis line (988 in the US, 116 123 Samaritans in the UK and Ireland) ».
- 15 / SAMU → « your local emergency number (911 in the US, 999 or 112 in the UK and Europe) ».
- « médecin traitant » → « your doctor ».

## Liens internes
- Garde EXACTEMENT les liens du français, avec leurs chemins français (/articles/<slug-fr>.html,
  /methode/<slug-fr>.html) : le générateur les réécrit vers les pages anglaises. N'ajoute ni ne
  retire de lien. Aucun lien externe dans le corps.

## Tableaux
- Même balisage (<div class="tablewrap"><table><caption>…), contenu traduit, même nombre de lignes.

## Ton périmètre
- Tu crées UNIQUEMENT tools/en/articles/batch_<x>.py (le nom du lot français). Ne touche à rien
  d'autre. Ne lance pas tools/build_articles.py. Aucune commande git. Fichiers de travail dans
  ton dossier du scratchpad.

## Contrôles à lancer jusqu'à zéro erreur
```bash
cd /Users/augustephilypriou/Desktop/Auros/landing
python3 -c "import ast,sys; ast.parse(open(sys.argv[1]).read())" tools/en/articles/batch_<x>.py
python3 tools/check_en.py tools/en/articles/batch_<x>.py
```

## Rapport final (court)
Par article : titre anglais, adaptations notables (unités, garde-fous), doutes éventuels ; puis la
sortie du contrôle.
