# Relecture des guides pour coachs, une langue à la fois

Tu relis les 28 guides d'une langue (`tools/<langue>/coachs/batch_1.py` à `batch_4.py`), écrits
par quatre rédacteurs différents d'après `tools/intl/_brief-coachs.md`. Tu es le dernier filet
avant publication : un fait faux ou une phrase étrangère à la langue abîment tout le site.

## Ce que tu vérifies, guide par guide
1. **Droit et chiffres.** Chaque règle, taux, seuil, organisme ou délai du pays doit figurer dans
   `tools/intl/_faits-ue.md` ou `tools/intl/_faits-<langue>.md`, avec le même sens (pas plus
   affirmatif que la fiche, mêmes limites). Tout ce qui n'y est pas, ou qui y est marqué
   « NON VÉRIFIÉ », sort du texte. Une règle française présentée comme applicable sort aussi.
   La source officielle de chaque fait utilisé est dans `sources`.
2. **Fidélité à l'anglais.** Comparé à `tools/en/coachs/batch_<n>.py` (même clé `fr`) : aucune
   méthode, étude, chiffre d'étude, nuance ou garde-fou de santé perdu ou déformé. Les exemples de
   calcul sont justes (en portugais, recalcule chaque montant en reais).
3. **Langue.** Naturelle pour un coach du pays, registre de la consigne (tú, du, tu, je, você),
   pas de calque de l'anglais, glossaire de la consigne respecté d'un lot à l'autre, titres et h2
   formulés comme les vraies requêtes Google de la langue, ponctuation et chiffres de la langue.
   Portugais : du Brésil partout (você, academia, treino, celular), jamais du Portugal.
4. **Cohérence entre les lots.** Même terme pour la même chose dans les 28 guides ; slugs
   cohérents ; pas deux titres presque identiques.
5. **Forme.** Pas de « Ecleptic » dans le corps, le titre ou la description, pas de tiret
   cadratin, pas de formule creuse, phrase de prudence finale présente.
6. **Sources.** Une source EUR-Lex pointe sur la version de la langue du guide
   (`https://eur-lex.europa.eu/legal-content/<ES|DE|IT|NL|PT>/…`, le contrôle accepte toutes les
   langues), avec un titre dans cette langue ; retire les mentions du type « version française ».
   Une source française gardée de l'anglais (HAS, CNIL…) ne sert qu'à appuyer une méthode ou une
   définition, jamais une obligation du pays : si la fiche donne un équivalent officiel du pays ou
   de l'UE, remplace-la. Huit sources au plus par guide (le contrôle bloque au-delà) : garde
   celles qui portent les phrases du guide ; pour une règle régionale (Espagne), cite une ou deux
   lois en exemple et formule la phrase en conséquence (« en Cataluña o Madrid, por ejemplo »),
   sauf dans un guide dont la qualification est le sujet.

## Ce que tu fais
- Corrige directement dans les fichiers (outil Edit), sans réécrire ce qui est juste.
- Relance `python3 tools/check_intl.py <langue>` depuis
  `/Users/augustephilypriou/Desktop/Auros/landing-guides-intl` jusqu'à zéro problème, et traite
  chaque « ⚠ ».
- Ne touche à aucun autre fichier. Pas de build, pas de git.

## Rapport (12 lignes au plus)
Nombre de guides relus ; corrections de fond (droit, chiffres, sens) guide par guide ; corrections
de langue en une ligne ; doutes qui restent ; sortie du contrôle.
