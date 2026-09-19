#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Génère les pages articles + l'index /articles/ + sitemap.xml.

Pour ajouter un article : ajouter une entrée dans ARTICLES puis lancer
    python3 tools/build_articles.py
depuis la racine du repo landing, et commiter les fichiers générés.
"""
import os, html

SITE = "https://ecleptic.health"
TF_LINK = "https://testflight.apple.com/join/H5CQgDa7"
POSTHOG_KEY = "phc_wzjqudiS3KH7MeMii8h6HmUR2onfQR5iasjhAs53AL2B"

# slug, title (H1 + <title>), description (meta), date ISO, body HTML
ARTICLES = [
    {
        "slug": "readiness-score-definition",
        "title": "Readiness score : c'est quoi, et comment l'utiliser au quotidien",
        "description": "Le readiness score (score de préparation) croise sommeil, HRV et charge d'entraînement pour te dire chaque matin si tu dois pousser ou récupérer. Explications.",
        "date": "2026-09-19",
        "body": """
<p>Le <strong>readiness score</strong> — ou score de préparation — est devenu la métrique centrale des apps de santé comme Whoop, Oura ou Ecleptic. L'idée : condenser en un seul chiffre, chaque matin, la capacité réelle de ton corps à encaisser la journée.</p>
<h2>Ce que le score mesure vraiment</h2>
<p>Un bon readiness score croise au minimum quatre familles de signaux :</p>
<ul>
<li><strong>Le sommeil</strong> : durée, régularité, proportion de sommeil profond.</li>
<li><strong>Le système nerveux</strong> : variabilité de la fréquence cardiaque (HRV) et fréquence cardiaque au repos, comparées à ta propre base.</li>
<li><strong>La charge d'entraînement</strong> : ce que tu as encaissé sur les derniers jours par rapport à ton habitude.</li>
<li><strong>Les tendances</strong> : un mauvais jour isolé n'a pas le même sens qu'une dérive sur une semaine.</li>
</ul>
<h2>Comment l'utiliser sans en devenir esclave</h2>
<p>Le score n'est pas un ordre, c'est un éclairage. Trois règles simples :</p>
<p><strong>1. Score vert</strong> → c'est le jour où placer ta séance dure de la semaine. Ton corps a les ressources pour surcompenser.</p>
<p><strong>2. Score orange</strong> → entraîne-toi, mais garde l'intensité sous contrôle : technique, zone 2, mobilité.</p>
<p><strong>3. Score rouge plusieurs jours de suite</strong> → le signal ne vient probablement pas de l'entraînement, mais du sommeil, du stress ou d'un début d'infection. C'est là que le score a le plus de valeur.</p>
<h2>Pourquoi un chiffre unique change le comportement</h2>
<p>On pourrait suivre chaque métrique séparément. En pratique, personne ne le fait durablement. Le mérite du score unique, c'est de transformer dix courbes en une décision : <em>aujourd'hui, je pousse ou je récupère ?</em> C'est cette décision, répétée des centaines de fois dans l'année, qui sépare la progression du surplace.</p>
""",
    },
    {
        "slug": "hrv-variabilite-cardiaque",
        "title": "HRV (variabilité cardiaque) : le signal le plus honnête de ton corps",
        "description": "La HRV mesure l'équilibre de ton système nerveux. Comment la lire, ce qui la fait chuter, et comment l'améliorer concrètement.",
        "date": "2026-09-19",
        "body": """
<p>Ton cœur ne bat pas comme un métronome — et c'est une excellente nouvelle. L'intervalle entre deux battements varie en permanence, et cette variation, la <strong>HRV</strong> (heart rate variability, ou VFC en français), reflète directement l'état de ton système nerveux autonome.</p>
<h2>Le principe en 30 secondes</h2>
<p>Deux branches se partagent le pilotage automatique de ton corps : le sympathique (accélérateur, stress, effort) et le parasympathique (frein, récupération, digestion). Une HRV haute signifie que le frein fonctionne bien — ton corps récupère. Une HRV qui chute signale que l'accélérateur domine : stress, dette de sommeil, entraînement mal digéré, alcool, maladie qui couve.</p>
<h2>La règle d'or : compare-toi à toi-même</h2>
<p>Une HRV de 45 ms peut être excellente pour une personne et faible pour une autre. La valeur absolue ne veut presque rien dire ; ce qui compte, c'est <strong>ta tendance par rapport à ta propre moyenne</strong> sur les 30 à 60 derniers jours. C'est pour ça que les comparaisons entre amis n'ont aucun sens.</p>
<h2>Ce qui fait chuter la HRV (dans l'ordre d'impact)</h2>
<ul>
<li><strong>L'alcool</strong> — même deux verres se voient la nuit même, souvent −15 à −25 %.</li>
<li><strong>La dette de sommeil</strong> et les couchers irréguliers.</li>
<li><strong>Une séance très intense</strong> — normal pendant 24-48 h, c'est la surcompensation qui suit qui compte.</li>
<li><strong>Le stress psychologique</strong> — souvent invisible pour toi, jamais pour ta HRV.</li>
<li><strong>Une infection</strong> — la HRV chute fréquemment 1 à 2 jours avant les symptômes.</li>
</ul>
<h2>Comment l'améliorer</h2>
<p>Pas de hack magique : régularité de sommeil, cardio en zone 2, exposition à la lumière du matin, réduction de l'alcool, respiration lente (5-6 respirations/minute pendant 5 min le soir). La HRV est un thermomètre — on l'améliore en soignant ce qu'elle mesure, pas en soufflant dessus.</p>
""",
    },
    {
        "slug": "proteines-par-jour",
        "title": "Combien de protéines par jour ? Le chiffre qui fait consensus",
        "description": "1,6 à 2,2 g de protéines par kilo de poids de corps : pourquoi cette fourchette, comment l'atteindre concrètement, et les erreurs classiques.",
        "date": "2026-09-19",
        "body": """
<p>C'est probablement la question nutrition la plus posée — et l'une des rares où la science a une réponse claire : <strong>1,6 à 2,2 g de protéines par kilo de poids de corps et par jour</strong> pour quelqu'un qui s'entraîne.</p>
<h2>Pourquoi cette fourchette</h2>
<p>Les méta-analyses convergent : en dessous de 1,6 g/kg, un pratiquant de musculation laisse du progrès sur la table ; au-dessus de 2,2 g/kg, le bénéfice supplémentaire devient négligeable. En perte de poids, viser le haut de la fourchette protège la masse musculaire pendant le déficit calorique.</p>
<h2>Concrètement, ça donne quoi ?</h2>
<p>Pour 75 kg : entre 120 et 165 g de protéines par jour. Repères utiles :</p>
<ul>
<li>Un blanc de poulet (150 g) ≈ 35 g</li>
<li>Un pavé de saumon ≈ 30 g</li>
<li>3 œufs ≈ 19 g</li>
<li>Un pot de skyr (150 g) ≈ 16 g</li>
<li>Une portion de lentilles cuites (200 g) ≈ 18 g</li>
</ul>
<h2>Les trois erreurs classiques</h2>
<p><strong>1. Tout concentrer sur le dîner.</strong> La synthèse protéique répond mieux à des apports répartis : vise ~25-40 g par repas, petit-déjeuner compris — c'est presque toujours lui le maillon faible.</p>
<p><strong>2. Compter au feeling.</strong> La plupart des gens surestiment leur apport de 30 à 50 %. Compter précisément pendant deux semaines suffit à recalibrer l'œil.</p>
<p><strong>3. Négliger les protéines en sèche.</strong> C'est exactement l'inverse : moins tu manges de calories, plus la part protéique doit monter.</p>
<h2>Et les protéines en poudre ?</h2>
<p>Un outil pratique, rien de plus : la whey est une protéine laitière tout à fait ordinaire. Si tu atteins ta cible avec de la vraie nourriture, elle est inutile ; si ton petit-déjeuner plafonne à 8 g de protéines, un shake règle le problème en 30 secondes.</p>
""",
    },
    {
        "slug": "sommeil-profond-ameliorer",
        "title": "Sommeil profond : 6 leviers concrets pour en avoir plus",
        "description": "Le sommeil profond pilote la récupération physique, la mémoire et les hormones. Six leviers appuyés par la recherche pour l'augmenter dès cette semaine.",
        "date": "2026-09-19",
        "body": """
<p>Le sommeil profond (sommeil lent profond, ou <em>deep sleep</em>) ne représente que 15 à 25 % de la nuit, mais c'est lui qui fait le gros du travail : sécrétion d'hormone de croissance, réparation musculaire, nettoyage du cerveau, consolidation de la mémoire. On ne peut pas le forcer — mais on peut créer les conditions pour qu'il vienne.</p>
<h2>1. Refroidis la chambre</h2>
<p>Ton corps doit perdre environ 1 °C de température interne pour plonger en sommeil profond. Vise 17-19 °C. Une douche chaude 1 à 2 h avant le coucher aide paradoxalement : elle déclenche la chute de température qui suit.</p>
<h2>2. Couche-toi à heure fixe</h2>
<p>Le sommeil profond se concentre en début de nuit, à l'heure où ton horloge interne l'attend. Décaler ton coucher de deux heures, c'est rater le train : tu dormiras, mais avec moins de profond. La régularité (±30 min, week-end compris) est le levier le plus rentable de cette liste.</p>
<h2>3. Coupe l'alcool</h2>
<p>L'alcool est le pire ennemi du sommeil profond et du sommeil paradoxal : il assomme (endormissement rapide) puis fragmente toute la seconde moitié de nuit. Même deux verres se voient clairement dans les données.</p>
<h2>4. Arrête la caféine 8 à 10 h avant</h2>
<p>Demi-vie de ~5 h : un café à 16 h, c'est l'équivalent d'un demi-café dans ton sang à 21 h. Beaucoup de « mauvais dormeurs » sont simplement des buveurs de café tardifs.</p>
<h2>5. Bouge dans la journée</h2>
<p>L'exercice physique — surtout le cardio et les séances de force — augmente la pression de sommeil et la part de sommeil profond la nuit suivante. Évite juste les séances très intenses dans les 2-3 h avant le coucher.</p>
<h2>6. Dîne léger et tôt</h2>
<p>Une digestion lourde en cours d'endormissement maintient la température corporelle et la fréquence cardiaque hautes — exactement ce que le sommeil profond n'aime pas. Idéal : dernier vrai repas 3 h avant le coucher.</p>
<p>Le point commun de ces six leviers : aucun ne s'achète. Le sommeil profond ne répond ni aux gadgets ni aux compléments à la mode — il répond à la physiologie.</p>
""",
    },
    {
        "slug": "cardio-zone-2",
        "title": "Zone 2 : pourquoi le cardio « trop facile » est le plus rentable",
        "description": "La zone 2 construit tes mitochondries, ta base aérobie et ta longévité. Comment la trouver sans capteur, et combien en faire par semaine.",
        "date": "2026-09-19",
        "body": """
<p>Les athlètes d'endurance de haut niveau passent environ 80 % de leur volume cardio à basse intensité. Pas parce qu'ils manquent de courage — parce que c'est là que se construit le moteur.</p>
<h2>C'est quoi, la zone 2 ?</h2>
<p>C'est l'intensité maximale à laquelle ton corps fonctionne encore essentiellement à l'aérobie, en brûlant majoritairement des graisses. Physiologiquement : juste sous ton premier seuil ventilatoire. En pratique, le test le plus fiable ne coûte rien : <strong>tu dois pouvoir tenir une conversation en phrases complètes</strong>. Si tu ne peux lâcher que quelques mots, tu es au-dessus.</p>
<h2>Ce que ça construit</h2>
<ul>
<li><strong>Des mitochondries</strong> — les centrales énergétiques de tes cellules — en nombre et en efficacité.</li>
<li><strong>Une base aérobie</strong> qui rend tout le reste plus facile : tu récupères plus vite entre les séries, entre les séances, et ta fréquence cardiaque au repos baisse.</li>
<li><strong>De la VO₂max sur le long terme</strong> — le meilleur prédicteur mesurable de longévité selon les grandes cohortes.</li>
</ul>
<h2>L'erreur classique : la « zone grise »</h2>
<p>La plupart des gens courent trop vite pour la zone 2 et trop lentement pour du vrai fractionné. Résultat : de la fatigue sans les adaptations ni de l'un ni de l'autre. Si ta sortie « facile » te laisse rincé, elle n'était pas facile.</p>
<h2>La dose qui marche</h2>
<p><strong>2 à 4 séances de 30 à 60 minutes par semaine.</strong> Le support importe peu : marche rapide en côte, vélo, rameur, course lente. Pour un débutant, la marche rapide suffit largement à être en zone 2. Et oui, ça paraîtra trop facile pendant les premières semaines — c'est le signe que tu fais juste.</p>
<p>Ajoute par-dessus une séance d'intensité par semaine (fractionné court ou côtes), et tu as le schéma 80/20 qui fait consensus de la recherche au terrain.</p>
""",
    },
    {
        "slug": "cafeine-sommeil-timing",
        "title": "Café et sommeil : à quelle heure boire son dernier café",
        "description": "La caféine a une demi-vie de 5 heures : ton café de 16 h travaille encore contre toi à minuit. Les horaires qui préservent ton sommeil sans renoncer au café.",
        "date": "2026-09-19",
        "body": """
<p>La caféine est la molécule psychoactive la plus consommée au monde — et la plus sous-estimée dans les problèmes de sommeil. Le point clé tient en un chiffre : <strong>sa demi-vie est d'environ 5 heures</strong>.</p>
<h2>Faites le calcul</h2>
<p>Un double expresso à 16 h (~130 mg de caféine) laisse ~65 mg dans ton sang à 21 h et encore ~33 mg à 2 h du matin. Tu t'endormiras peut-être quand même — la caféine n'empêche pas toujours l'endormissement — mais elle dégrade la qualité du sommeil, notamment le sommeil profond, souvent sans que tu t'en rendes compte.</p>
<h2>Le mécanisme : l'adénosine</h2>
<p>Toute la journée, ton cerveau accumule de l'adénosine, la molécule de la pression de sommeil. La caféine ne l'élimine pas : elle en bloque les récepteurs. L'adénosine continue de s'accumuler derrière la porte — et quand la caféine se dissipe, tout arrive d'un coup. C'est le coup de barre de 14 h du café de 8 h.</p>
<h2>Les trois règles qui changent tout</h2>
<p><strong>1. Dernier café 8 à 10 h avant le coucher.</strong> Coucher à 23 h → dernier café entre 13 h et 15 h. C'est la règle la plus rentable de cet article.</p>
<p><strong>2. Premier café 90 minutes après le réveil.</strong> Au réveil, ton cortisol est déjà au pic : le café n'y ajoute presque rien. Le retarder lisse ton énergie sur la matinée et réduit le creux de l'après-midi.</p>
<p><strong>3. Connais ta sensibilité.</strong> On métabolise la caféine à des vitesses très différentes selon les gènes. Si tu dors mal, teste deux semaines avec un dernier café à midi : tes propres données de sommeil trancheront mieux que n'importe quel article.</p>
<h2>Et le déca en soirée ?</h2>
<p>Bonne option : 3 à 15 mg de caféine par tasse, négligeable pour la plupart des gens. Le rituel sans la molécule.</p>
""",
    },
    {
        "slug": "lumiere-matin-rythme-circadien",
        "title": "10 minutes de lumière le matin : le levier santé le plus sous-coté",
        "description": "La lumière naturelle du matin règle ton horloge circadienne : sommeil, énergie, humeur, hormones. Pourquoi ça marche et comment le faire même en hiver.",
        "date": "2026-09-19",
        "body": """
<p>Si un seul geste quotidien devait résumer le biohacking, ce serait celui-là : <strong>s'exposer à la lumière naturelle dans l'heure qui suit le réveil</strong>. Gratuit, sans effort, et l'effet touche presque tout : endormissement, énergie, humeur, appétit.</p>
<h2>Pourquoi la lumière du matin est un « réglage d'horloge »</h2>
<p>Ton horloge circadienne — le chef d'orchestre de tes hormones — dérive naturellement. Ce qui la remet à l'heure chaque jour, ce sont des cellules spécialisées de la rétine, sensibles à la lumière bleue du ciel. Une exposition matinale envoie le signal « le jour commence » : le cortisol fait son pic au bon moment, et surtout, un compte à rebours se lance — environ 14 à 16 heures plus tard, la mélatonine sera sécrétée. <strong>Ta facilité d'endormissement ce soir se joue ce matin.</strong></p>
<h2>Pourquoi la fenêtre ne suffit pas</h2>
<p>Les ordres de grandeur surprennent : un plafonnier fournit ~300-500 lux, une journée couverte dehors ~5 000-10 000 lux, un ciel dégagé 50 000 lux et plus. Une vitre filtre en outre une bonne partie du signal. Dix minutes dehors valent des heures derrière une fenêtre.</p>
<h2>Le protocole</h2>
<ul>
<li><strong>Ciel dégagé :</strong> 5 à 10 minutes dehors dans l'heure suivant le réveil.</li>
<li><strong>Ciel couvert :</strong> 15 à 20 minutes — ça compte tout autant.</li>
<li>Sans lunettes de soleil (ne regarde jamais le soleil directement, la lumière indirecte suffit).</li>
<li>Combine avec un geste existant : café sur le balcon, un arrêt de bus à pied, sortir le chien.</li>
</ul>
<h2>Le pendant du soir</h2>
<p>Le même système fonctionne en sens inverse : la lumière vive entre 22 h et 4 h retarde ton horloge et supprime la mélatonine. Le soir, baisse les lumières, passe en éclairage chaud et indirect. Lumière forte le matin, faible le soir : c'est tout le contrat.</p>
""",
    },
    {
        "slug": "surentrainement-signes",
        "title": "Surentraînement : 7 signes que ton corps réclame du repos",
        "description": "Fatigue qui ne part pas, perfs en baisse, sommeil dégradé, HRV en chute : les signaux du surentraînement et comment réagir avant de creuser le trou.",
        "date": "2026-09-19",
        "body": """
<p>Le progrès ne vient pas de l'entraînement — il vient de la récupération qui le suit. Quand la charge dépasse durablement ta capacité à récupérer, le corps envoie des signaux. Les voici, du plus précoce au plus sérieux.</p>
<h2>1. Ta fréquence cardiaque au repos monte</h2>
<p>+5 battements ou plus au réveil par rapport à ta moyenne, plusieurs jours de suite : ton système nerveux travaille en heures supplémentaires. C'est souvent le tout premier signal mesurable.</p>
<h2>2. Ta HRV chute et reste basse</h2>
<p>Une chute de variabilité cardiaque après une grosse séance est normale — elle doit remonter en 24-48 h. Une HRV qui reste sous ta base une semaine entière raconte autre chose.</p>
<h2>3. Les mêmes séances te coûtent plus cher</h2>
<p>Ta fréquence cardiaque grimpe plus haut pour la même allure, tes charges habituelles semblent lourdes, tes temps se dégradent malgré l'entraînement. C'est le paradoxe signature : <em>plus tu forces, moins ça avance</em>.</p>
<h2>4. Ton sommeil se dégrade — alors que tu es épuisé</h2>
<p>Fatigué mais incapable de bien dormir, réveils nocturnes, réveil à 4 h : le système nerveux sympathique refuse de rendre les clés. Signal très fiable.</p>
<h2>5. Ton humeur change</h2>
<p>Irritabilité, motivation en berne, l'entraînement devenu corvée. Les questionnaires d'humeur détectent le surentraînement plus tôt que la plupart des marqueurs sanguins.</p>
<h2>6. Tu retombes malade en boucle</h2>
<p>Rhumes à répétition, petite plaie qui traîne : l'immunité est l'un des premiers postes que le corps sacrifie quand le budget récupération est à sec.</p>
<h2>7. Appétit et poids déraillent</h2>
<p>Faim disparue malgré la charge, ou fringales de sucre permanentes : les hormones de régulation (cortisol, leptine, ghréline) sont sorties de leur rythme.</p>
<h2>Que faire ?</h2>
<p>Deux ou trois signes qui durent plus d'une semaine : <strong>coupe l'intensité, pas forcément le mouvement</strong>. Une semaine de zone 2 légère, de sommeil prioritaire et d'alimentation complète suffit souvent à tout relancer — et tu reviendras plus fort qu'en t'obstinant. S'obstiner, c'est transformer une semaine de décharge en deux mois de trou.</p>
""",
    },
    {
        "slug": "calculer-besoins-caloriques-tdee",
        "title": "Calculer ses besoins caloriques (TDEE) : la méthode honnête",
        "description": "Formules, niveaux d'activité, et pourquoi la vraie réponse vient de la balance : comment estimer puis ajuster ta dépense énergétique totale.",
        "date": "2026-09-19",
        "body": """
<p>Le TDEE (<em>Total Daily Energy Expenditure</em>) est ta dépense énergétique totale sur 24 h : le chiffre autour duquel se décide toute prise de masse ou perte de poids. Voici comment l'estimer — et surtout comment le corriger, parce que toutes les formules se trompent.</p>
<h2>Étape 1 : le métabolisme de base</h2>
<p>La formule de Mifflin-St Jeor reste la référence :</p>
<ul>
<li><strong>Hommes :</strong> 10 × poids (kg) + 6,25 × taille (cm) − 5 × âge + 5</li>
<li><strong>Femmes :</strong> 10 × poids (kg) + 6,25 × taille (cm) − 5 × âge − 161</li>
</ul>
<p>Exemple : homme, 75 kg, 180 cm, 30 ans → 750 + 1 125 − 150 + 5 = <strong>1 730 kcal</strong> de métabolisme de base.</p>
<h2>Étape 2 : le multiplicateur d'activité</h2>
<ul>
<li>Sédentaire (bureau, peu de marche) : × 1,3-1,4</li>
<li>Actif léger (2-3 séances/sem.) : × 1,5</li>
<li>Actif (4-5 séances + marche quotidienne) : × 1,6-1,7</li>
<li>Très actif (entraînement quotidien ou métier physique) : × 1,8-2,0</li>
</ul>
<p>Notre exemple, actif : 1 730 × 1,6 ≈ <strong>2 770 kcal/jour</strong>. Piège classique : presque tout le monde surestime son niveau d'activité d'un cran.</p>
<h2>Étape 3 : la seule vérité, c'est la balance</h2>
<p>Ces formules ont ±10-15 % d'erreur — jusqu'à 400 kcal/jour. La méthode honnête : mange ton TDEE estimé pendant deux semaines en pesant chaque matin (même heure, à jeun), et compare les <strong>moyennes hebdomadaires</strong> — jamais les pesées isolées, qui varient de ±1 kg avec l'eau. Poids stable → estimation juste. Sinon : ~7 700 kcal ≈ 1 kg, donc +0,3 kg/semaine ≈ 330 kcal de surplus quotidien à retrancher de l'estimation.</p>
<h2>Ensuite seulement, la cible</h2>
<p>Perte de poids : TDEE − 300 à 500 kcal. Prise de masse : TDEE + 200 à 300 kcal (au-delà, c'est du gras). Et le TDEE bouge — poids, saison d'entraînement, quotidien : recalibre à chaque changement de phase.</p>
""",
    },
    {
        "slug": "vo2max-ameliorer",
        "title": "VO₂max : pourquoi c'est le meilleur marqueur de longévité, et comment l'améliorer",
        "description": "La VO₂max prédit la longévité mieux que le tabac ou le diabète dans les grandes cohortes. Le protocole 80/20 pour la faire monter à tout âge.",
        "date": "2026-09-19",
        "body": """
<p>Si tu ne devais suivre qu'un seul chiffre de santé sur le long terme, les grandes études de cohorte sont formelles : ce serait la <strong>VO₂max</strong> — ta capacité maximale à consommer de l'oxygène à l'effort, en ml/kg/min.</p>
<h2>Pourquoi elle prédit autant</h2>
<p>Dans les cohortes (dont l'étude HUNT et les travaux de la Cleveland Clinic sur plus de 120 000 patients), passer du bas de la distribution à un niveau simplement « au-dessus de la moyenne » est associé à une réduction de mortalité comparable ou supérieure à l'arrêt du tabac. La logique : la VO₂max résume l'état de toute la chaîne — cœur, poumons, vaisseaux, mitochondries. C'est un bilan de santé intégral déguisé en chiffre de sportif.</p>
<h2>Où te situer</h2>
<p>Un homme de 30-39 ans est « moyen » autour de 40-44 ml/kg/min, une femme autour de 34-38. Les montres l'estiment correctement à ±5 % dès lors que tu fais du cardio régulièrement avec la fréquence cardiaque. La VO₂max décline de ~10 % par décennie après 30 ans si tu ne fais rien — c'est précisément ce déclin que l'entraînement ralentit, à tout âge.</p>
<h2>Le protocole 80/20</h2>
<p><strong>La base (80 % du volume) : zone 2.</strong> 2 à 4 sorties de 30-60 min par semaine en aisance respiratoire. C'est elle qui construit le réseau — capillaires, mitochondries, cœur.</p>
<p><strong>Le sommet (20 %) : une séance d'intervalles par semaine.</strong> Le format le plus étudié : le 4×4 norvégien — 4 minutes à intensité dure (respiration très difficile, ~90 % FC max), 3 minutes de récupération active, quatre fois. Une seule séance de ce type par semaine suffit à faire monter la VO₂max de manière mesurable en 8 à 12 semaines.</p>
<h2>L'erreur à éviter</h2>
<p>Tout faire « moyennement dur ». La zone grise fatigue sans construire ni la base ni le sommet. Facile vraiment facile, dur vraiment dur — c'est la polarisation qui paie.</p>
""",
    },
]

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
@media(max-width:560px){nav.site{flex-direction:column;align-items:flex-start;gap:16px;padding:22px 24px}nav.site .links{gap:14px;font-size:10px;letter-spacing:.16em;flex-wrap:wrap}nav.site .logo{font-size:13px;letter-spacing:.35em}}
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
article h2{font-size:13px;letter-spacing:.22em;text-transform:uppercase;font-weight:500;color:var(--gold);margin:44px 0 14px}
article p{margin:0 0 16px;font-size:16.5px;color:var(--ink)}
article ul{margin:0 0 16px 20px}
article li{margin-bottom:8px;font-size:16.5px}
article strong{font-weight:600}
article em{color:var(--gold);font-style:normal}
/* fin d'article : la beta comme recompense */
.reward{border-top:1px solid var(--line);border-bottom:1px solid var(--line);margin:64px 0 8px;padding:52px 0;text-align:center}
.reward .label{display:block;margin-bottom:20px}
.reward h2{font-size:clamp(20px,3.6vw,28px);font-weight:200;text-transform:uppercase;letter-spacing:0;color:var(--ink);margin:0 0 14px;line-height:1.2}
.reward p{color:var(--muted);font-size:15px;max-width:420px;margin:0 auto 28px}
.next{padding:40px 0 8px}
.next .label{display:block;margin-bottom:18px}
.next a{display:block;text-decoration:none;padding:16px 0;border-bottom:1px solid var(--line);font-weight:300;
        font-size:16px;text-transform:uppercase;letter-spacing:.02em;color:var(--ink)}
.next a:first-of-type{border-top:1px solid var(--line)}
.next a:hover{color:var(--gold)}
/* INDEX ARTICLES : liste editoriale */
.pagehead{padding:72px 0 24px}
.pagehead h1{font-size:clamp(34px,7vw,60px)}
.pagehead p{color:var(--muted);margin-top:22px;font-size:16px;max-width:480px}
.journal{margin:36px 0 0}
.journal a.entry{display:block;text-decoration:none;padding:30px 0;border-top:1px solid var(--line)}
.journal a.entry:last-child{border-bottom:1px solid var(--line)}
.journal .label{display:block;margin-bottom:12px}
.journal h2{font-size:clamp(19px,3.4vw,25px);font-weight:250;text-transform:uppercase;letter-spacing:.01em;color:var(--ink);line-height:1.25;transition:color .2s}
.journal a.entry:hover h2{color:var(--gold)}
.journal p.desc{color:var(--muted);font-size:14.5px;margin-top:10px;max-width:540px}
footer.site{border-top:1px solid var(--line);margin-top:96px;padding:40px 0 64px;text-align:center}
footer.site .flinks{font-size:11px;letter-spacing:.22em;text-transform:uppercase}
footer.site a{color:var(--muted);text-decoration:none}
footer.site a:hover{color:var(--gold)}
.disclaimer{max-width:520px;margin:22px auto 0;color:var(--muted);font-size:12.5px;line-height:1.7}
"""

POSTHOG = """<script>
  var POSTHOG_KEY="%s";
  if(POSTHOG_KEY){!function(t,e){var o,n,p,r;e.__SV||(window.posthog=e,e._i=[],e.init=function(i,s,a){function g(t,e){var o=e.split(".");2==o.length&&(t=t[o[0]],e=o[1]),t[e]=function(){t.push([e].concat(Array.prototype.slice.call(arguments,0)))}}(p=t.createElement("script")).type="text/javascript",p.async=!0,p.src=s.api_host+"/static/array.js",(r=t.getElementsByTagName("script")[0]).parentNode.insertBefore(p,r);var u=e;for(void 0!==a?u=e[a]=[]:a="posthog",u.people=u.people||[],u.toString=function(t){var e="posthog";return"posthog"!==a&&(e+="."+a),t||(e+=" (stub)"),e},u.people.toString=function(){return u.toString(1)+".people (stub)"},o="capture identify alias people.set people.set_once set_config register register_once unregister opt_out_capturing has_opted_out_capturing opt_in_capturing reset".split(" "),n=0;n<o.length;n++)g(u,o[n]);e._i.push([i,s,a])},e.__SV=1)}(document,window.posthog||[]);posthog.init(POSTHOG_KEY,{api_host:"https://eu.i.posthog.com"});}
  function track(ev,props){if(window.posthog&&POSTHOG_KEY)posthog.capture(ev,props||{});}
</script>""" % POSTHOG_KEY

NAV = """<nav class="site">
  <a class="logo" href="/">Ecleptic</a>
  <div class="links">
    <a href="/" %(on_home)s>Accueil</a>
    <a href="/articles/" %(on_articles)s>Journal</a>
    <a href="/guide.html">Guide</a>
    <a href="/beta.html">La b&ecirc;ta</a>
  </div>
</nav>"""

FOOTER = """<footer class="site">
  <div class="wrap">
    <p class="flinks"><a href="/confidentialite.html">Confidentialit&eacute;</a> &nbsp;&middot;&nbsp; <a href="mailto:contact@ecleptic.app">Contact</a> &nbsp;&middot;&nbsp; <a href="/beta.html">La b&ecirc;ta</a></p>
    <p class="disclaimer">Ecleptic est une application de bien-&ecirc;tre. Ses contenus ne remplacent pas un avis m&eacute;dical et ne constituent pas un dispositif m&eacute;dical.</p>
  </div>
</footer>"""


def nav(section):
    return NAV % {
        "on_home": 'class="on"' if section == "home" else "",
        "on_articles": 'class="on"' if section == "articles" else "",
    }


CATS = {
    "readiness-score-definition": "Signal",
    "hrv-variabilite-cardiaque": "Signal",
    "proteines-par-jour": "Nutrition",
    "sommeil-profond-ameliorer": "Sommeil",
    "cardio-zone-2": "Entraînement",
    "cafeine-sommeil-timing": "Sommeil",
    "lumiere-matin-rythme-circadien": "Rythme",
    "surentrainement-signes": "Récupération",
    "calculer-besoins-caloriques-tdee": "Nutrition",
    "vo2max-ameliorer": "Longévité",
}


def cat(a):
    return CATS.get(a["slug"], "Journal")


def article_page(a, others):
    url = "%s/articles/%s.html" % (SITE, a["slug"])
    more = "\n".join(
        '<a href="/articles/%s.html">%s</a>' % (o["slug"], html.escape(o["title"]))
        for o in others[:3]
    )
    jsonld = (
        '{"@context":"https://schema.org","@type":"Article","headline":%s,'
        '"description":%s,"datePublished":"%s","inLanguage":"fr",'
        '"author":{"@type":"Organization","name":"Ecleptic","url":"%s"},'
        '"publisher":{"@type":"Organization","name":"Ecleptic","url":"%s"},'
        '"mainEntityOfPage":"%s"}'
    ) % (
        __import__("json").dumps(a["title"], ensure_ascii=False),
        __import__("json").dumps(a["description"], ensure_ascii=False),
        a["date"], SITE, SITE, url,
    )
    return """<!doctype html>
<html lang="fr">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>%(title)s — Ecleptic</title>
<meta name="description" content="%(desc)s">
<link rel="canonical" href="%(url)s">
<meta property="og:title" content="%(title)s">
<meta property="og:description" content="%(desc)s">
<meta property="og:type" content="article">
<meta property="og:url" content="%(url)s">
<script type="application/ld+json">%(jsonld)s</script>
<link rel="stylesheet" href="/assets/site.css">
</head>
<body>
%(nav)s
<main class="wrap">
<article>
  <header>
    <span class="label"><span class="gold">%(cat)s</span> &nbsp;&middot;&nbsp; %(date)s</span>
    <h1>%(title)s</h1>
    <p class="standfirst">%(desc)s</p>
  </header>
  %(body)s
  <div class="reward">
    <span class="label">Pour aller plus loin</span>
    <h2>Ce que cet article explique,<br>l'app le mesure chez toi.</h2>
    <p>Ecleptic croise ton sommeil, ton alimentation et ton entraînement en un seul score, chaque matin. La bêta iOS est ouverte à un petit cercle.</p>
    <a class="btn gold" href="/beta.html" onclick="track('article_cta_click',{article:'%(slug)s'})">Demander l'accès</a>
  </div>
  <div class="next">
    <span class="label">À lire ensuite</span>
%(more)s
  </div>
</article>
</main>
%(footer)s
%(posthog)s
<script>track('article_view',{article:'%(slug)s'});</script>
</body>
</html>
""" % {
        "title": html.escape(a["title"]), "desc": html.escape(a["description"], quote=True),
        "url": url, "jsonld": jsonld, "nav": nav("articles"), "date": a["date"], "cat": html.escape(cat(a)),
        "body": a["body"].strip(), "tf": TF_LINK, "slug": a["slug"], "more": more,
        "footer": FOOTER, "posthog": POSTHOG,
    }


def index_page():
    cards = "\n".join(
        """<a class="entry" href="/articles/%s.html"><span class="label"><span class="gold">%s</span></span><h2>%s</h2><p class="desc">%s</p></a>"""
        % (a["slug"], html.escape(cat(a)), html.escape(a["title"]), html.escape(a["description"]))
        for a in ARTICLES
    )
    return """<!doctype html>
<html lang="fr">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>Articles — Ecleptic</title>
<meta name="description" content="Sommeil, nutrition, entraînement, récupération : des articles courts, scientifiques et actionnables pour optimiser ta santé au quotidien.">
<link rel="canonical" href="%(site)s/articles/">
<meta property="og:title" content="Articles — Ecleptic">
<meta property="og:description" content="Sommeil, nutrition, entraînement, récupération : des conseils scientifiques et actionnables.">
<meta property="og:type" content="website">
<link rel="stylesheet" href="/assets/site.css">
</head>
<body>
%(nav)s
<main class="wrap">
  <div class="pagehead">
    <span class="label">Journal Ecleptic</span>
    <h1 class="display" style="margin-top:22px">Des conseils<br>qui <span class="gold">s'appliquent</span>.</h1>
    <p>Sommeil, nutrition, entraînement, récupération. Court, sourcé, actionnable — la même exigence que dans l'app.</p>
  </div>
  <div class="journal">
%(cards)s
  </div>
  <div class="reward" style="border-bottom:0">
    <span class="label">Et ensuite</span>
    <h2>Lire, c'est bien.<br>Mesurer, c'est mieux.</h2>
    <p>Tout ce que le journal explique, l'app le suit automatiquement, sur tes propres données. La bêta iOS est ouverte à un petit cercle.</p>
    <a class="btn gold" href="/beta.html" onclick="track('article_cta_click',{article:'index'})">Demander l'accès</a>
  </div>
</main>
%(footer)s
%(posthog)s
<script>track('articles_index_view');</script>
</body>
</html>
""" % {"site": SITE, "nav": nav("articles"), "cards": cards, "tf": TF_LINK,
       "footer": FOOTER, "posthog": POSTHOG}


def sitemap():
    urls = ["%s/" % SITE, "%s/beta.html" % SITE, "%s/guide.html" % SITE, "%s/articles/" % SITE]
    urls += ["%s/articles/%s.html" % (SITE, a["slug"]) for a in ARTICLES]
    items = "\n".join("  <url><loc>%s</loc></url>" % u for u in urls)
    return '<?xml version="1.0" encoding="UTF-8"?>\n<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">\n%s\n</urlset>\n' % items


def main():
    root = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    os.makedirs(os.path.join(root, "articles"), exist_ok=True)
    os.makedirs(os.path.join(root, "assets"), exist_ok=True)
    with open(os.path.join(root, "assets", "site.css"), "w") as f:
        f.write(CSS)
    for i, a in enumerate(ARTICLES):
        others = ARTICLES[i + 1:] + ARTICLES[:i]
        with open(os.path.join(root, "articles", a["slug"] + ".html"), "w") as f:
            f.write(article_page(a, others))
    with open(os.path.join(root, "articles", "index.html"), "w") as f:
        f.write(index_page())
    with open(os.path.join(root, "sitemap.xml"), "w") as f:
        f.write(sitemap())
    print("OK — %d articles + index + sitemap + css" % len(ARTICLES))


if __name__ == "__main__":
    main()
