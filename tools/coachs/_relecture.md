# Relecture indépendante des guides coachs

Tu n'as pas écrit ces guides. Ton travail est de trouver ce qui est faux avant qu'un professionnel ou un juriste ne le trouve. Tu pars du principe que chaque affirmation peut être fausse.

Travaille dans /Users/augustephilypriou/Desktop/Auros/landing-coachs. Tu modifies UNIQUEMENT tes fichiers de lot. Pas de build, pas de git.

## Méthode
1. Lis tools/coachs/_cahier-coachs.md et les fiches tools/coachs/_faits-sport.md et _faits-fiscal.md. Les fiches peuvent contenir des erreurs : le texte d'origine l'emporte toujours sur elles.
2. Pour chaque guide, relève chaque affirmation vérifiable : numéro d'article, peine, montant, taux, seuil, date, délai, condition, chiffre d'étude, fonction ou prix d'un logiciel. Vérifie-la sur le texte d'origine.
3. Corrige directement le fichier, de façon minimale, dans le même ton. Le slug, le titre, le sujet et les questions de FAQ ne changent pas.
4. Vérifie que chaque attribution du texte correspond bien à une source de la liste, et que la source dit bien cela.
5. Relance les contrôles du cahier jusqu'à zéro erreur.

## Accès aux sources
- Légifrance refuse curl. Utilise WebFetch, ou le navigateur intégré (outils mcp__Claude_Browser__*, charge-les avec ToolSearch, requête "mcp__Claude_Browser__", max_results 40) : ouvre ton propre onglet avec preview_start et une url, puis get_page_text.
- Ne contourne aucun blocage : pas d'en-têtes imitant un navigateur, aucune vérification anti-robots résolue. Si une page reste fermée, garde la formulation prudente de la fiche ou retire l'affirmation, et note-le.
- Ne te connecte à rien. Ne clique pas sur les bandeaux de cookies.

## Écriture
- Remplace le jargon de vérification. « Aucune décision lue ne dit » devient « Je n'ai trouvé aucune décision qui dise ». « Aucune statistique officielle trouvée » devient une phrase complète. Les dates de relevé restent permises dans les légendes de tableau et pour les prix.
- Le fondateur peut écrire « je » pour parler de sa recherche, jamais pour parler d'une expérience de coach.
- Une phrase creuse ou répétée se supprime. Garde 700 à 1000 mots.

## Rapport final, 10 lignes au plus
Nombre d'affirmations vérifiées, corrections faites (avant → après), ce qui n'a pas pu être vérifié, corrections à reporter dans les fiches, puis le résultat des contrôles.
