# Fiches de faits par pays, pour adapter les guides coachs (09/11/2026)

## Contexte
Le site ecleptic.health publie 28 guides pour coachs sportifs indépendants en anglais
(`tools/en/coachs/batch_1.py` à `batch_4.py`). On les adapte en espagnol, allemand, italien,
néerlandais et portugais du Brésil. Les versions anglaises ont retiré tout le droit national et
le remplacent par des phrases générales (« Check the rules where you work: qualification,
insurance and consumer law vary by country », « if you work in the EU or the UK, health data is
specially protected », numéros d'urgence américains et britanniques, « example rate of 25.8% »
pour les cotisations, une recommandation de la Commission française des clauses abusives).
Les nouvelles versions doivent dire ce qui est vrai DANS LE PAYS du lecteur. Ta fiche donne aux
rédacteurs les faits vérifiés, prêts à l'emploi. Un fait faux abîme tout le site : la prudence
prime sur l'exhaustivité.

## Règles
1. Sources officielles seulement pour ce qui est cité : journal officiel et bases de lois
   (EUR-Lex, BOE, gesetze-im-internet.de, RIS, Fedlex, Normattiva, Gazzetta Ufficiale,
   wetten.overheid.nl, Diário da República, planalto.gov.br), sites d'administrations,
   d'autorités de contrôle (AEPD, Garante, AP, CNPD, ANPD, BfDI, EDÖB…), d'ordres ou de conseils
   professionnels légaux (CONFEF/CREF, IPDJ…), chambres officielles (KVK, WKO). Un blog, un
   cabinet d'avocats, un éditeur de logiciel ou Wikipédia peuvent t'aider à TROUVER le texte,
   jamais servir de source.
2. Lis la page toi-même (outil de recherche web et de lecture de page). Ne cite rien de mémoire.
   Si une page officielle refuse l'accès, essaie une autre page officielle qui dit la même chose ;
   ne contourne aucun blocage.
3. Ce que tu ne peux pas vérifier : écris « NON VÉRIFIÉ, ne pas l'écrire » et passe. Un point
   incertain n'est jamais présenté comme tranché. Un point qui varie (région, statut) est dit
   comme tel.
4. Chiffres (taux, seuils, montants) : l'année de validité et la page qui le donne. Pour 2026 et
   2027, le chiffre en vigueur au 09/11/2026 et ce qui est déjà voté pour 2027 s'il existe.
5. Citations : 15 mots au plus par extrait, entre guillemets.
6. Pas de conseil personnel : ce sont des faits pour un article d'information.

## Format de sortie (un fichier Markdown, en français)
Pour chaque fait, un bloc :

```
### <code du fait> · <titre court>
- Fait : une à trois phrases en français, exactes et prudentes.
- Phrase prête (<langue du pays>) : une phrase que le rédacteur peut reprendre telle quelle,
  au tutoiement (tú / du / tu / je / você), sans jargon inutile.
- Référence : texte exact (loi, article, alinéa) ou nom de la page.
- URL officielle : https://…   (celle que tu as lue)
- Lu le 09/11/2026 : ce que dit la page, en un extrait court.
- Limites : ce que le fait ne dit pas, cas particuliers, ce qu'il ne faut pas écrire.
```
Commence le fichier par un tableau récapitulatif (code, vérifié oui/non, une ligne).
Termine par « Pièges » : les idées reçues fausses que tu as croisées.

## Les faits à établir (codes communs à tous les pays)
- F1 Qualification : faut-il un diplôme, un titre, une carte ou une inscription à un registre
  pour encadrer contre rémunération en tant que coach / entraîneur personnel ? Selon la région
  si besoin. Le coaching en ligne est-il visé ? Ce qui est permis sans diplôme.
- F2 Assurance : une assurance responsabilité civile professionnelle est-elle obligatoire pour ce
  métier ? Par quel texte ?
- F3 Données de santé : loi nationale qui complète le RGPD (ou loi du pays hors UE), nom exact
  de l'autorité de contrôle, page officielle de l'autorité sur les données de santé si elle
  existe.
- F4 Droits d'accès : délai de réponse à une demande d'accès d'un client (hors UE surtout).
- F5 Registre des traitements : obligation pour un indépendant seul qui traite des données de
  santé (hors UE surtout ; pour l'UE, la fiche UE le traite).
- F6 Rétractation : délai pour un contrat conclu à distance ou hors établissement avec un
  particulier (services), début de la prestation pendant le délai, montant dû si le client se
  rétracte après avoir commencé. Obligation nationale d'un bouton ou d'un moyen de résiliation en
  ligne pour les abonnements souscrits en ligne (Allemagne : § 312k BGB, par exemple).
- F7 Clauses abusives : texte national ; une recommandation ou une décision officielle sur les
  contrats de salle de sport ou de coaching si elle existe (autorité de la concurrence et de la
  consommation, ministère, juridiction suprême).
- F8 Reconduction tacite des contrats de consommation : règles (durée initiale maximale,
  préavis, information du client).
- F9 Hausse de prix dans un contrat en cours avec un particulier : ce que la loi permet.
- F10 Prospection : consentement préalable pour l'e-mail, le SMS et l'appel commercial à un
  particulier ; exception pour les clients existants.
- F11 Faux avis et témoignages : règle nationale, et règle sur les avantages offerts contre un
  avis ou une recommandation (parrainage).
- F12 Droit à l'image : consentement écrit pour publier la photo ou la vidéo d'un client.
- F13 TVA (ou taxe sur les services) : taux normal applicable à une séance de coaching sportif
  individuel (et taux réduit ou exonération éventuels, précisément), et régime de franchise des
  petites entreprises : seuil exact en 2026.
- F14 Cotisations et impôt de l'indépendant : sur quelle base (chiffre d'affaires ou bénéfice,
  forfait mensuel par tranches…), avec les montants ou taux 2026 de la page officielle. Les
  statuts courants d'un coach indépendant (nom exact du statut) et l'immatriculation exigée.
- F15 Numéro d'urgence à appeler (malaise d'un client).
- F16 Durée de conservation des factures et pièces comptables pour un indépendant.
- F17 (facultatif) Avantage fiscal ou social pour un employeur qui offre des séances de sport à
  ses salariés (coaching en entreprise).
- F18 (facultatif) Questionnaire ou certificat médical imposé par la loi avant une activité
  physique encadrée (par exemple : certificat médical italien, PAR-Q imposé par une loi d'État au
  Brésil). S'il n'existe pas, dis-le.

## Ce qui reste à la fiche UE (ne le refais pas dans les fiches pays)
RGPD (données de santé, accès sous un mois, registre, sous-traitant, portabilité), directive
2011/83/UE (14 jours, début anticipé, montant proportionnel, fonction de rétractation de la
directive 2023/2673 au 19 juin 2026), directive 93/13/CEE, directive 2005/29/CE modifiée par
2019/2161 (faux avis), directive 2002/58/CE (prospection), 112, directive 2020/285 (franchise de
TVA des PME). Les fiches pays ne donnent que la transposition nationale quand elle change quelque
chose (délai, numéro d'article, règle plus stricte).
