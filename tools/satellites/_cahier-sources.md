# Cahier des charges — sources des articles du Journal

Objectif : que chaque article d'ecleptic.health soit **citable** par Google, ChatGPT, Perplexity et Claude.
Les moteurs génératifs reprennent en priorité les pages qui donnent des chiffres attribués et des
sources vérifiables. Chaque article reçoit donc 3 à 6 sources réelles, vérifiées une par une, et ses
chiffres clés sont attribués dans le texte.

## Ton périmètre
- Tu édites **uniquement** le fichier de lot qu'on t'a confié : `tools/satellites/batch_<x>.py`
  (liste `ENTRIES`, un dict par article, `body` en HTML dans une chaîne `"""…"""`).
- Tu ne lances **pas** `tools/build_articles.py` (il réécrit le site ; d'autres rédacteurs travaillent en
  même temps). Pas de commit, pas de git. Aucun autre fichier.

## À faire pour chaque article
1. **Lire l'article** et relever les affirmations chiffrées ou scientifiques (durées, doses, pourcentages,
   études citées, recommandations officielles).
2. **Trouver les sources** qui les soutiennent, par ordre de préférence :
   recommandations et consensus de sociétés savantes ou d'agences (AASM, National Sleep Foundation, ACSM,
   ISSN, OMS/WHO, EFSA, ANSES, HAS, CDC, NHS…), méta-analyses et revues systématiques, grands essais
   randomisés ou cohortes. Pas de blog, pas de presse, pas de site commercial, pas de Wikipédia.
   Outils (curl, sans clé) :
   - PubMed : `https://eutils.ncbi.nlm.nih.gov/entrez/eutils/esearch.fcgi?db=pubmed&retmode=json&term=…`
     puis `esummary.fcgi?db=pubmed&retmode=json&id=…` et le résumé :
     `efetch.fcgi?db=pubmed&rettype=abstract&retmode=text&id=…` (max 3 requêtes/s : `sleep 0.4`).
   - Crossref : `https://api.crossref.org/works?rows=5&query.bibliographic=…` et `https://api.crossref.org/works/<doi>`.
   **Lis le résumé** : la source doit dire ce que l'article lui fait dire.
3. **Corriger** toute affirmation que les sources contredisent (chiffre faux, étude mal résumée), et le
   signaler dans ton rapport. Si une affirmation n'a aucune source solide, reformule-la prudemment ou
   retire-la. Aucun chiffre inventé, aucune étude inventée.
4. **Attribuer 2 à 4 chiffres clés dans le texte**, sans lien : « selon l'American Academy of Sleep
   Medicine », « une méta-analyse de 2018 (49 essais, 1 863 participants) montre que… ». L'attribution
   doit correspondre exactement à une des sources de la liste.
5. **Un tableau au plus**, seulement si la réponse est naturellement tabulaire (repères par âge, par
   objectif, par durée…), 7 lignes max, chiffres sourcés, avec ce balisage exact :
   ```html
   <div class="tablewrap"><table>
   <caption>Source : American Academy of Sleep Medicine (2016).</caption>
   <thead><tr><th>Âge</th><th class="n">Sommeil recommandé</th></tr></thead>
   <tbody>
   <tr><td>Adolescents (13-18 ans)</td><td class="n">8 à 10 h</td></tr>
   </tbody>
   </table></div>
   ```
6. **Ajouter la clé `"sources"`** (après `"faq"`) : 3 à 6 entrées, chacune
   `{"t": "…", "u": "https://…"}`.
   - `t` = référence dans sa langue d'origine : `Auteur1 AB, Auteur2 CD, et al. Titre original. Revue abrégée. Année.`
     Organisme : `American Academy of Sleep Medicine. Titre du document. Année.`
     Italique de la revue permis : `<em>Sleep</em>`.
   - `u` = `https://doi.org/<doi>` si un DOI existe, sinon `https://pubmed.ncbi.nlm.nih.gov/<pmid>/`,
     sinon la page officielle stable de l'organisme.
   - Pas deux fois la même source.

## Ce qui ne bouge pas
- `slug`, `cat`, `title`, `description`, `date`, et les **questions** de la FAQ (les réponses peuvent
  être corrigées si un chiffre l'est dans le corps).
- La structure : « La réponse courte : … » en premier paragraphe, h2 = sous-questions, « Ce qu'il faut
  retenir » (3 puces) en fin de corps, liens internes existants.
- Le ton : tutoiement, voix du fondateur, phrases directes. Jamais « Ecleptic » dans le corps.
- Pas de lien externe dans le corps : les liens sortants vont dans `sources`.
- Garde-fous santé : aucun diagnostic, aucune posologie de médicament, renvoi vers un médecin dès que le
  sujet devient médical ; santé mentale : garder la mention du 3114 si elle existe.
- Longueur : +160 mots au plus par article (le contrôleur refuse au-delà), total 400-1150 mots.
- Ne touche pas à la clé `updated` (gérée à la publication).

## Contrôles à lancer jusqu'à zéro erreur
```bash
python3 -c "import ast,sys; ast.parse(open(sys.argv[1]).read())" tools/satellites/batch_<x>.py
python3 tools/check_articles.py tools/satellites/batch_<x>.py   # gabarit, liens, champs figés
python3 tools/check_sources.py tools/satellites/batch_<x>.py    # chaque source existe et concorde
```
`check_sources.py` : « ÉCHEC » = à corriger obligatoirement ; « À VÉRIFIER » (page protégée par un
anti-robot) = ouvre-la autrement (curl avec un user-agent de navigateur, ou remplace par un DOI/PubMed).

## Ton rapport final (court)
Par article : nombre de sources, chiffres **corrigés** (avant → après, avec la source), tableau ajouté
ou non, points restés incertains. Puis le résultat des trois contrôles.
