# Cahier des charges — articles pour les coachs

Objectif : aller chercher sur Google les coachs sportifs indépendants français, surtout ceux qui ont moins de 15 clients. Chaque article répond à une vraie requête mieux que ce qui existe, avec des faits vérifiés. Les articles sortent à partir du 02/12/2026 dans la rubrique `/coachs/` d'ecleptic.health, un tous les 2 jours.

## Ton périmètre
- Tu écris **uniquement** ton fichier de lot : `tools/coachs/batch_<x>.py`, liste `ENTRIES`, un dict par article, `body` en HTML dans une chaîne `"""…"""`.
- Tu ne lances **pas** `tools/build_articles.py`. Pas de git. Aucun autre fichier.
- Tu lis d'abord `tools/coachs/_faits-sport.md` et `tools/coachs/_faits-fiscal.md`. Ces fiches font foi. Leur section « Points à ne jamais écrire » est une interdiction. Un fait marqué INCERTAIN s'écrit comme incertain, avec la formulation sûre donnée.
- Lis un exemple du ton du site : les deux premiers articles de `tools/satellites/batch_g.py`.

## Format d'une entrée
```python
{
    "slug": "…",            # tel que dans la liste
    "cat": "…",             # le Sujet de la liste, à l'identique
    "title": "…",           # le Titre de la liste, à l'identique, validé par le fondateur
    "seo_title": "…",       # OBLIGATOIRE si le titre dépasse 60 caractères : 60 caractères au plus
    "description": "…",     # 140 à 160 caractères, contient la requête principale
    "date": "2026-12-02",   # laisse cette valeur, le calendrier décide
    "body": """…""",
    "faq": [{"q": "…", "a": "…"}, …],   # exactement 3, questions = vraies requêtes
    "sources": [{"t": "…", "u": "https://…"}, …],   # 3 à 6
    "a_revoir": ["…"],      # chaque chiffre daté qui peut changer (taux, seuil, prix, calendrier). [] si aucun
}
```

## Structure du corps
1. Premier paragraphe : « La réponse courte : … », 2 à 4 phrases, la requête principale en `<strong>`, la vraie réponse tout de suite.
2. 3 à 5 `<h2>` formulés comme des sous-questions réelles.
3. Dernier `<h2>` : « Ce qu'il faut retenir », 3 puces.
4. 700 à 950 mots. Un tableau au plus, seulement si la réponse est tabulaire, 7 lignes max, avec ce balisage :
```html
<div class="tablewrap"><table>
<caption>Source : …</caption>
<thead><tr><th>…</th><th class="n">…</th></tr></thead>
<tbody>
<tr><td>…</td><td class="n">…</td></tr>
</tbody>
</table></div>
```
Balises admises : p, ul, ol, li, h2, h3, strong, em, a, table et ses enfants.

## Liens internes
3 à 4 liens dans le corps, avec une ancre naturelle :
- au moins 2 vers d'autres guides de la liste : `<a href="/coachs/<slug>.html">…</a>`. Un guide pas encore sorti est neutralisé automatiquement, n'y pense pas ;
- quand c'est pertinent, 1 vers le Journal (`/articles/<slug>.html`, slugs dans `tools/coachs/_journal-slugs.txt`) ou la Méthode (`/methode/<slug>.html` : age-biologique besoin-de-sommeil cibles depense-energetique frequence-cardiaque-repos frequence-respiratoire ligne-de-base nutrition readiness-score saturation-oxygene temperature-poignet variabilite-cardiaque vitaux vo2max).
Aucun lien externe dans le corps : ils vont dans `sources`.
Reste sur ta requête : si un point est traité par un autre guide, résume-le en une phrase et mets le lien, sans le refaire.

## Voix
- Tutoiement, phrases courtes, direct, utile. On parle à un professionnel : pas de pédagogie condescendante.
- Le site est signé par le fondateur d'une app de santé, qui construit un outil pour les coachs. **Il n'est pas coach.** Jamais « mes clients », « dans ma salle », « quand je coachais ». Aucune anecdote, aucun témoignage, aucun cas client inventé. Un exemple chiffré est présenté comme un exemple de calcul.
- Tu peux être franc sur les excuses et les idées reçues du métier, jamais sur le corps des gens.
- Pas de tirets cadratins, pas de « ce n'est pas X, c'est Y », pas de formules creuses (« dans un monde où », « il est crucial de »).

## Interdits
- Le mot « Ecleptic » dans le corps, la FAQ ou les sources. Le produit n'apparaît que dans le bloc de fin, généré à part.
- Tout prix ou fonction de notre offre coach, toute mention de l'IA.
- Promesse de revenus ou de résultat (« 10 000 € par mois », « remplis ton agenda en 30 jours »).
- Chiffre sans source. Pas de statistique marketing de blog (taux de conversion, « 80 % des clients… »). Si le chiffre n'existe pas, dis-le et donne une méthode de calcul.
- Tarifs de marché : il n'existe pas de barème officiel. Ne cite une fourchette que si la fiche de faits la donne. Sinon, méthode de calcul présentée comme exemple.
- Laisser croire qu'on peut coacher contre rémunération sans qualification ni carte, y compris en ligne.
- Diagnostic, conseil médical, régime prescrit. Renvoi vers un médecin ou un diététicien dès que ça le demande. Le PAR-Q+ est protégé : ne reproduis pas ses questions.

## Sources
- 3 à 6 sources réelles, ouvertes et lues. Priorité : Légifrance, BOFiP, impots.gouv, URSSAF, service-public, sports.gouv.fr, CNIL, DGCCRF, INSEE, sociétés savantes, méta-analyses (DOI ou PubMed). Pour Google et Meta : leurs pages d'aide officielles.
- Pas de blog, de presse, de site commercial, de Wikipédia. Exception lots i et j : la page officielle de tarifs ou de fonctions d'un logiciel, pour décrire ce logiciel.
- Format de `t` : `Code du sport, article L. 212-1.` ; `Urssaf. Titre de la page. 2026.` ; `Auteur AB, Auteur CD, et al. Titre. Revue. Année.`. `u` = `https://doi.org/…`, sinon PubMed, sinon la page officielle.
- Si un site refuse l'accès, ne contourne pas le blocage : pas d'en-têtes imitant un navigateur, pas de changement d'identité. Prends une autre page officielle, ou la référence déjà donnée par une fiche de faits.
- Attribue 2 à 4 faits clés dans le texte : « selon l'Urssaf », « l'article L. 212-8 du code du sport prévoit… ». Chaque attribution correspond à une source de la liste.

## Articles de droit, de fiscalité et de statut
- Date tes chiffres dans le texte : « en 2026 ». Note-les dans `a_revoir`.
- Termine le corps, juste avant « Ce qu'il faut retenir », par : « Ce guide informe, il ne remplace pas l'avis d'un expert-comptable ou d'un avocat. » (adapte le professionnel au sujet).
- Un point non tranché par les textes est présenté comme tel. N'invente aucun numéro d'article : cite seulement ceux de la fiche ou ceux que tu as lus.

## Articles qui nomment des logiciels (lots i et j)
- Lis `~/Desktop/Auros/reports/Logiciels pour coachs sportifs.md`, sections « Comparatif des prix et abonnements » et « Comment être meilleur ». C'est une étude interne : ne la cite pas, revérifie chaque fait sur la page officielle du logiciel et date-le (« tarifs relevés le 01/11/2026 »).
- Comparaison loyale : mêmes critères pour chaque outil, faits vérifiables, aucun dénigrement (code de la consommation, L. 122-1 et suivants). Présente les avis comme des avis, avec leur plateforme, leur date et leur nombre. Pas de pourcentage tiré d'un petit échantillon présenté comme une vérité générale.
- Ne dis pas quel outil est « le meilleur » dans l'absolu : dis pour quel coach chacun convient.

## Contrôles à lancer jusqu'à zéro erreur
```bash
python3 -c "import ast,sys; ast.parse(open(sys.argv[1]).read())" tools/coachs/batch_<x>.py
python3 tools/check_articles.py tools/coachs/batch_<x>.py
python3 tools/check_sources.py tools/coachs/batch_<x>.py
```
`check_sources.py` : « ÉCHEC » = à corriger. « À VÉRIFIER » = page protégée contre les robots : garde-la seulement si elle figure dans une fiche de faits, sinon remplace-la.

## Ton rapport final (court)
Par article : mots, nombre de sources, points restés incertains. Puis le résultat des contrôles. Rien d'autre.

## La liste des 50
| N° | Lot | Slug | Titre (ne pas changer) | Sujet (`cat`) | Requêtes visées | Anglais |
|---|---|---|---|---|---|---|
| 1 | a | `coach-sportif-auto-entrepreneur` | Coach sportif auto-entrepreneur : le guide pour bien démarrer | Statut et droit | coach sportif auto entrepreneur ; coach sportif micro entreprise | non |
| 2 | d | `fiche-client-coach-sportif` | Fiche client de coach sportif : ce qu'elle doit contenir | Métier | fiche client coach sportif | oui |
| 3 | f | `trouver-des-clients-coach-sportif` | Comment trouver des clients quand on est coach sportif | Clients | comment trouver des clients coach sportif | oui |
| 4 | h | `tarif-coach-sportif-independant` | Quel tarif fixer quand on est coach sportif ? | Tarifs et revenus | tarif coach sportif auto entrepreneur ; coach sportif tarif horaire | oui |
| 5 | b | `coach-sportif-sans-diplome` | Coach sportif sans diplôme : ce que dit la loi et ce que tu risques | Statut et droit | coach sportif sans diplome ; coach sportif en ligne sans diplome ; coach sportif sans carte professionnelle | non |
| 6 | d | `bilan-forme-premier-rendez-vous` | Bilan forme : comment mener le premier rendez-vous avec un client | Métier | bilan forme coach sportif ; coach sportif bilan | oui |
| 7 | g | `coaching-sportif-en-ligne-comment-faire` | Comment faire du coaching sportif en ligne ? | En ligne | comment faire du coaching sportif en ligne ; coaching en ligne sportif | oui |
| 8 | a | `coach-sportif-bic-ou-bnc` | Coach sportif : BIC ou BNC ? | Statut et droit | coach sportif auto entrepreneur bic ou bnc ; coach sportif urssaf bic ou bnc | non |
| 9 | d | `questionnaire-sante-avant-le-sport-client` | Questionnaire de santé avant le sport : que demander à un client ? | Métier | questionnaire coach sportif ; questionnaire santé sport adulte ; par-q+ | oui |
| 10 | f | `coach-sportif-google-fiche-etablissement` | Coach sportif : comment être trouvé sur Google dans ta ville | Clients | coach sportif + ville (fiche Google) | oui |
| 11 | b | `carte-professionnelle-educateur-sportif` | Carte professionnelle d'éducateur sportif : l'obtenir, la renouveler, la vérifier | Statut et droit | carte professionnelle éducateur sportif ; educateur sportif renouvellement carte pro ; déclaration éducateur sportif | non |
| 12 | h | `combien-gagne-coach-sportif-independant` | Combien gagne un coach sportif indépendant ? | Tarifs et revenus | coach sportif gagne combien par mois ; coach sportif indépendant salaire | oui |
| 13 | d | `tests-physiques-nouveau-client` | Tests physiques : lesquels faire passer à un nouveau client ? | Métier | test physique coach sportif | oui |
| 14 | f | `instagram-coach-sportif` | Instagram pour coach sportif : ce qui amène vraiment des clients | Clients | coach sportif instagram | oui |
| 15 | a | `coach-sportif-tva` | Coach sportif et TVA : franchise, seuils et taux | Statut et droit | coach sportif tva ; coach sportif exonération tva ; auto entrepreneur coach sportif tva | non |
| 16 | h | `tarif-coaching-en-ligne` | Tarif du coaching en ligne : combien facturer ? | Tarifs et revenus | tarif coaching en ligne ; prix moyen coach en ligne ; tarif coaching sportif en ligne | oui |
| 17 | d | `creer-programme-personnalise-client` | Créer un programme personnalisé pour un client : la méthode | Métier | coach sportif programme personnalisé ; programme pour coach sportif | oui |
| 18 | a | `facture-coach-sportif` | Facture de coach sportif : mentions obligatoires et facture électronique | Statut et droit | coach sportif facture ; facture coach sportif auto entrepreneur ; coach sportif facture electronique | non |
| 19 | f | `site-internet-coach-sportif` | Site internet de coach sportif : ce qu'il doit contenir | Clients | coach sportif site internet ; site internet coach sportif | oui |
| 20 | i | `vendre-programme-sportif-en-ligne` | Vendre un programme sportif en ligne : comment s'y prendre | En ligne | vendre programme sportif en ligne ; vendre coaching en ligne | oui |
| 21 | b | `assurance-coach-sportif` | Assurance de coach sportif : ce qui est obligatoire | Statut et droit | coach sportif assurance obligatoire ; assurance coach sportif auto entrepreneur | non |
| 22 | e | `fideliser-clients-coaching-sportif` | Pourquoi tes clients arrêtent : fidéliser en coaching sportif | Métier | à tester : fidéliser clients coach sportif | oui |
| 23 | h | `packs-abonnement-seance-coach-sportif` | Packs, abonnement ou séance à l'unité : quelle formule choisir ? | Tarifs et revenus | coach sportif tarif mensuel ; coach sportif prix par mois | oui |
| 24 | f | `seance-essai-coach-sportif` | Séance d'essai : gratuite ou payante, et comment la transformer | Clients | à tester : séance d'essai coach sportif | oui |
| 25 | c | `cgv-coach-sportif` | CGV de coach sportif : ce qu'elles doivent prévoir | Statut et droit | cgv coach sportif | non |
| 26 | c | `reglementation-vente-programme-sportif` | Vente de programmes sportifs : ce que dit la réglementation | En ligne | réglementation vente programme sportif | non |
| 27 | e | `suivre-client-a-distance` | Suivre un client à distance sans y passer tes soirées | En ligne | coach sportif à distance ; suivi coach sportif | oui |
| 28 | c | `contrat-coach-sportif-client` | Contrat entre un coach sportif et son client : les clauses utiles | Statut et droit | coach sportif contrat ; contrat coach sportif modèle | non |
| 29 | b | `comment-devenir-coach-sportif` | Comment devenir coach sportif en France | Formation | comment devenir coach sportif en france ; devenir coach sportif | non |
| 30 | g | `coach-independant-en-salle` | Travailler en salle quand on est coach indépendant | Clients | coach sportif en salle ; coach sportif indépendant offre d'emploi ; contrat coach sportif basic fit | non |
| 31 | h | `augmenter-ses-tarifs-coach` | Augmenter ses tarifs de coach sans perdre ses clients | Tarifs et revenus | à tester : augmenter ses tarifs coach sportif | oui |
| 32 | c | `rgpd-donnees-sante-coach-sportif` | Données de santé de tes clients : ce que le RGPD t'impose | Statut et droit | à tester : coach sportif rgpd | non |
| 33 | e | `bilan-mensuel-client-coaching` | Bilan mensuel d'un client : quoi lui montrer | Métier | à tester : bilan mensuel client coach sportif | oui |
| 34 | b | `bpjeps-af-ou-cqp` | BPJEPS AF ou CQP : quel diplôme pour devenir coach ? | Formation | bpjeps af ; cqp instructeur fitness ; devenir coach sportif quel diplome | non |
| 35 | g | `coaching-sportif-en-entreprise` | Coaching sportif en entreprise : comment décrocher un contrat | Clients | devenir coach sportif en entreprise ; tarif coaching sportif en entreprise | oui |
| 36 | c | `coach-sportif-nutrition-droit` | Coach sportif et nutrition : ce que tu as le droit de dire | Statut et droit | coach sportif nutritionniste ; devenir coach sportif et nutrition ; tarif coach sportif et nutrition | non |
| 37 | g | `avis-recommandations-coach-sportif` | Recommandations et avis : faire parler tes clients de toi | Clients | à tester : avis clients coach sportif ; parrainage coach sportif | oui |
| 38 | e | `lire-etat-de-forme-client` | Sommeil, fatigue, charge : lire l'état d'un client avant la séance | Métier | à tester : suivi fatigue client coach sportif | oui |
| 39 | g | `coaching-en-visio` | Coaching en visio : matériel et déroulé d'une séance | En ligne | coach sportif visio | oui |
| 40 | a | `statut-juridique-coach-sportif` | Micro, EI ou SASU : quel statut pour un coach sportif ? | Statut et droit | coach sportif statut juridique ; coach sportif quel statut | non |
| 41 | e | `seance-annulee-regles-coach` | Séance annulée, retard, absence : les règles à poser | Métier | à tester : annulation séance coach sportif | oui |
| 42 | i | `logiciel-coach-sportif-comment-choisir` | Logiciel de coach sportif : comment choisir | Logiciels | logiciel coach sportif ; logiciel pour coach sportif ; logiciel de coaching sportif | oui |
| 43 | i | `application-coach-sportif-gratuite-ou-payante` | Application pour coach sportif : gratuite ou payante ? | Logiciels | application pour coach sportif gratuit ; logiciel pour coach sportif gratuit | oui |
| 44 | i | `excel-whatsapp-logiciel-coaching` | Excel, WhatsApp, PDF : quand passer à un vrai logiciel de coaching | Logiciels | logiciel gestion coach sportif ; application gestion coach sportif | oui |
| 45 | i | `application-suivi-client-coach` | Application de suivi : ce que ton client utilise vraiment | Logiciels | application suivi coach sportif | oui |
| 46 | j | `meilleures-applications-coach-sportif` | Meilleures applications pour coach sportif : le comparatif | Logiciels | meilleur application pour coach sportif ; comparatif application coach sportif | oui |
| 47 | j | `alternative-trainerize-francais` | Alternative à Trainerize en français : les options | Logiciels | abc trainerize alternative | non |
| 48 | j | `hexfit-everfit-my-pt-hub-avis` | Hexfit, Everfit, My PT Hub : avis et différences | Logiciels | hexfit avis ; everfit avis ; everfit francais | oui |
| 49 | j | `changer-logiciel-coaching` | Changer de logiciel de coaching sans perdre ses clients | Logiciels | à tester : changer de logiciel coaching | oui |
| 50 | j | `verifier-logiciel-coaching-avant-de-choisir` | Support, résiliation, bugs : quoi vérifier avant de choisir un logiciel | Logiciels | à tester : avis logiciel coaching sportif | oui |
