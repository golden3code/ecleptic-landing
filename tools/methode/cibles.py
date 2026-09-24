# -*- coding: utf-8 -*-
"""La méthode · Moteur V — les cibles.

Chargé par tools/build_articles.py (_load_methode) → /methode/cibles.html.
Faits vérifiés dans le code de l'app (supabase/functions/compute-expenditure et
compute-targets) le 24/09/2026 : Mifflin-St Jeor × facteur d'activité 1,3/1,4/1,55/1,7,
tendance de poids lissée (demi-vie 10 j, pesées écrêtées), apports 14 j, ≥ 10 j de
repas + ≥ 3 pesées, fusion jours valides/21 (fenêtre 14 j : jamais 100 % observé),
amortissement −10 %/+25 %, garde-fous BMR et 1,2 × BMR, 7 700 kcal/kg (5 500 si
objectif prise de masse), règles des 6 objectifs sélectionnables, lipides 30 %
(≥ 0,8 g/kg), garde-fous IMC 18,5 / moins de 18 ans / perte rapide (−10 %).
Ajouts du 24/09 (demande du user), vérifiés dans compute-targets et compute-expenditure :
perte rapide = plus de 1,5 % du poids par semaine ; dette de sommeil (≥ 4 nuits sur
7 j, manque cumulé ≥ 300 min sous 7 h/nuit) → déficit limité à −15 % ; déficit ≤ 1 %
du poids par semaine (poids × 0,01 × 7 700 / 7, soit 11 kcal/kg/j) ; planchers dans
l'ordre métabolisme de repos puis 1 200 kcal (femme) / 1 500 kcal (homme ou sexe non
précisé) ; types de
journée (repos 0, très léger ≥ 1, léger ≥ 30, modéré ≥ 60, intense ≥ 105 min actives ;
bonus = minutes moyennes du niveau sur 14 j × 4 kcal, ≤ 600 ; repos ≤ −300 ; écart
porté par les glucides) ; phase lutéale estimée +150 kcal (suivi du cycle activé avec
consentement, hors pilule combinée, ≥ 2 cycles terminés) ; dépense mesurée écartée à
± 3 jours d'un début de règles (rétention d'eau) ; interrupteur Voyage / maladie = gel
de l'estimation de dépense pendant la pause + 7 jours (les cibles, elles, continuent).
Sexe non précisé (correctif de l'app du 24/09/2026, supabase/functions/_shared/profileKeys.ts,
déployé) : constante de Mifflin −78 (moyenne de +5 et −161) et plancher 1 500 kcal ; avant,
la valeur « unspecified » était lue comme une femme.
Non publié : le plafond de déficit à 25 % (présent dans le code, inatteignable à −18 %).
Volontairement absents : Souplesse et Préparation d'un événement (grisés au
launch, lib/energyGoals.ts launchEnabled:false ; event_date jamais écrit côté client).
"""

PAGE = {
    "slug": "cibles",
    "kind": "moteur",
    "num": "V",
    "order": 5,
    "label": "Les cibles",
    "title": "Les cibles, calées sur ta dépense réelle",
    "seo_title": "Cibles caloriques et macros : comment elles sont calculées — Ecleptic",
    "description": "Comment Ecleptic calcule tes cibles de calories et de macros : une dépense recalibrée par tes pesées et tes repas, ton objectif, et des garde-fous stricts.",
    "date": "2026-09-24",
    "lead": "Combien tu dépenses vraiment, et donc combien tu devrais manger : l'app ne le devine pas une fois pour toutes, <strong>elle le mesure sur tes pesées et tes repas réels</strong>. Voici chaque étape du calcul, de la formule de départ à tes cibles de calories et de macros.",
    "body": """
<h2>Ce que le moteur calcule</h2>
<p>Le moteur des cibles répond à deux questions, dans cet ordre. D'abord : <strong>combien dépenses-tu vraiment par jour ?</strong> C'est ta <a href="/methode/depense-energetique.html">dépense énergétique</a>, ou TDEE. Ensuite : <strong>compte tenu de ton objectif, combien dois-tu manger, et avec quelle répartition ?</strong> Ce sont tes cibles de calories, de protéines, de lipides et de glucides.</p>
<p>Une formule remplie le premier jour donne un ordre de grandeur, pas ton métabolisme. Ecleptic s'en sert seulement comme point de départ : ensuite, <strong>ta dépense est recalibrée en continu par tes pesées et tes repas réels</strong>. C'est la méthode des bilans énergétiques observés, la seule qui converge vers ton métabolisme à toi, et pas vers celui d'une moyenne de population.</p>

<h2>Le point de départ : une formule</h2>
<p>Le premier jour, l'app ne connaît ni tes repas ni l'évolution de ton poids. Elle calcule donc ton métabolisme de repos avec l'équation de <strong>Mifflin-St Jeor</strong>, publiée en 1990 pour l'adulte en bonne santé, à partir de ton poids, de ta taille, de ton âge et de ton sexe : 10 × poids (kg) + 6,25 × taille (cm) − 5 × âge, puis + 5 pour un homme, − 161 pour une femme, ou − 78, la moyenne des deux, si tu n'as pas précisé ton sexe.</p>
<p>Ce métabolisme de repos est ensuite multiplié par un facteur d'activité, selon ton niveau sportif :</p>
<ul>
<li><strong>Débutant :</strong> × 1,3.</li>
<li><strong>Occasionnel :</strong> × 1,4.</li>
<li><strong>Régulier :</strong> × 1,55.</li>
<li><strong>Intensif :</strong> × 1,7.</li>
</ul>
<p>Exemple : un homme de 30 ans, 80 kg, 1,80 m, a un métabolisme de repos de 1 780 kcal. S'il s'entraîne régulièrement, sa dépense de départ est d'environ 2 760 kcal par jour. C'est une estimation de population : chez une personne donnée, l'erreur peut dépasser plusieurs centaines de kilocalories par jour. D'où l'étape suivante.</p>

<h2>Ta dépense réelle, lue dans ton propre bilan</h2>
<p>Le principe tient en une phrase : si ton poids est stable, tu manges ce que tu dépenses ; s'il baisse, tu dépenses plus ; s'il monte, moins. En croisant ce que tu manges et l'évolution de ton poids, on remonte donc à ce que tu dépenses vraiment. L'app croise deux séries :</p>
<ul>
<li><strong>La tendance de ton poids :</strong> une moyenne lissée de tes pesées, avec une demi-vie de 10 jours, où les pesées récentes comptent davantage. Les pesées aberrantes sont écrêtées : une balance capricieuse ne fait pas la tendance.</li>
<li><strong>Tes apports réellement enregistrés :</strong> la moyenne de tes repas sur les 14 derniers jours. Comment l'app analyse chaque repas : <a href="/methode/nutrition.html">La nutrition</a>.</li>
</ul>
<p>La dépense observée se calcule alors ainsi : <strong>apports moyens − (variation de poids par semaine × densité énergétique) ÷ 7</strong>. La densité énergétique vaut 7 700 kcal par kilo, ou 5 500 kcal par kilo quand ton objectif est la prise de masse, parce que le poids pris en construisant du muscle est moins riche en énergie. Ces valeurs restent des approximations, discutées sur la fiche <a href="/methode/depense-energetique.html">dépense énergétique</a>.</p>
<p>Exemple : tu enregistres en moyenne 2 200 kcal par jour et ta tendance baisse de 0,4 kg par semaine. Cette perte vaut 0,4 × 7 700 = 3 080 kcal par semaine, soit 440 kcal par jour : ta dépense observée est d'environ 2 640 kcal.</p>
<p>Cette mesure n'entre en jeu que si elle repose sur assez de données : <strong>au moins 10 jours de repas enregistrés sur 14</strong> et <strong>au moins 3 pesées</strong> sur la période. Sinon, la formule fait foi.</p>

<h2>Un passage progressif et surveillé</h2>
<p>La mesure ne remplace pas la formule d'un coup. Son poids dans le calcul est égal au nombre de jours valides, c'est-à-dire tes jours de repas enregistrés, <strong>divisé par 21</strong> ; le reste vient de la formule. Tant que les données manquent, c'est la formule ; ensuite, un mélange qui penche d'autant plus vers ta mesure que tu enregistres tes repas régulièrement.</p>
<p>Chaque nouvelle estimation est ensuite <strong>amortie</strong> par rapport à la précédente : ta dépense ne peut pas baisser de plus de 10 % ni monter de plus de 25 % d'un calcul à l'autre. L'asymétrie est voulue. Une semaine de rétention d'eau ne doit pas faire osciller tes cibles ; en revanche, après une période où tu as moins bien enregistré tes repas, la remontée doit être rapide.</p>
<p>Enfin, deux garde-fous de plausibilité écartent l'estimation observée quand les données racontent une histoire impossible :</p>
<ul>
<li><strong>Sous ton métabolisme de repos :</strong> une dépense totale inférieure à ce que ton corps brûle au repos n'a pas de sens.</li>
<li><strong>Des apports trop bas pour un poids qui ne baisse pas :</strong> sous 1,2 fois ton métabolisme de repos, sans que ton poids diminue, c'est le signe que des repas n'ont pas été enregistrés, pas d'un vrai déficit.</li>
</ul>
<p>Dans ces deux cas, la formule reprend la main. Mieux vaut une estimation honnête qu'une mesure fausse.</p>

<h2>De ta dépense à tes cibles</h2>
<p>Une fois ta dépense estimée, ton objectif fixe l'écart à appliquer :</p>
<div class="figs">
  <div><span class="v">−18 %</span><span class="u">Perte de poids</span></div>
  <div><span class="v">+12 %</span><span class="u">Prise de masse</span></div>
  <div><span class="v">+7 %</span><span class="u">Force</span></div>
  <div><span class="v">0 %</span><span class="u">Maintien, cardio, endurance</span></div>
</div>
<p>Les protéines sont fixées en premier, en grammes par kilo de poids :</p>
<ul>
<li><strong>2,2 g/kg :</strong> perte de poids, prise de masse et développement de la force. En déficit, elles aident à préserver ton muscle ; en surplus, elles fournissent de quoi le construire.</li>
<li><strong>1,6 g/kg :</strong> maintien, amélioration du cardio et endurance.</li>
</ul>
<p>Viennent ensuite les <strong>lipides, à 30 % des calories</strong>, sans jamais descendre sous 0,8 g par kilo : un minimum de graisses reste indispensable, même en déficit. Les <strong>glucides complètent</strong> le reste. Les repères derrière ces choix : <a href="/articles/proteines-par-jour-prise-de-muscle.html">combien de protéines par jour</a> et <a href="/articles/glucides-et-sport-combien.html">combien de glucides quand on fait du sport</a>.</p>
<p>Reprenons notre exemple. En perte de poids, 2 760 kcal × 0,82 donnent une cible d'environ 2 260 kcal : 176 g de protéines (2,2 × 80 kg), 75 g de lipides (30 % des calories) et environ 220 g de glucides.</p>

<h2>Les garde-fous non négociables</h2>
<p>Certaines règles passent avant ton objectif, quel qu'il soit :</p>
<ul>
<li><strong>IMC sous 18,5 :</strong> aucun déficit. Maigrir n'a pas de sens quand ta corpulence est déjà sous la zone normale.</li>
<li><strong>Moins de 18 ans :</strong> aucun déficit. Un corps en croissance n'a pas à être mis au régime par une app.</li>
<li><strong>Perte trop rapide :</strong> si ta perte observée dépasse 1,5 % de ton poids par semaine, le déficit est ralenti à −10 %. Une perte trop rapide se fait davantage aux dépens du muscle.</li>
<li><strong>Dette de sommeil :</strong> si tes nuits de la dernière semaine cumulent au moins 5 heures de manque par rapport à 7 heures par nuit, sur 4 nuits enregistrées au minimum, le déficit est limité à −15 %. Une nuit longue ne rattrape pas une nuit courte. En manque de sommeil, un déficit est plus dur à tenir et plus coûteux pour le muscle.</li>
<li><strong>Un rythme de perte plafonné :</strong> ton déficit ne dépasse jamais l'équivalent d'une perte de 1 % de ton poids par semaine, soit environ 11 kcal par kilo et par jour : 880 kcal au plus à 80 kg.</li>
<li><strong>Un plancher calorique :</strong> ta cible ne descend jamais sous ton métabolisme de repos, ni sous 1 200 kcal pour une femme et 1 500 kcal pour un homme ou si ton sexe n'est pas précisé. Tes protéines restent alors les mêmes ; les lipides sont recalculés et les glucides prennent le reste.</li>
</ul>

<h2>Quand tes cibles bougent</h2>
<p>Ta dépense est réestimée <strong>chaque nuit</strong>, et tes cibles sont aussi recalculées quand tu te pèses ou que tu enregistres tes repas. Elles suivent donc ta réalité, semaine après semaine : si ton poids bouge plus vite ou plus lentement que prévu, elles s'ajustent. Trois situations les modifient aussi :</p>
<ul>
<li><strong>Ta journée :</strong> l'app distingue cinq niveaux selon tes minutes actives, du repos à la journée intense (1 h 45 et plus), en passant par très léger, léger (30 min) et modéré (1 h). Un jour actif reçoit un bonus de 4 kcal par minute active, calculé sur tes journées du même niveau des deux dernières semaines, 600 kcal au plus ; un jour de repos, une baisse qui compense, 300 kcal au plus, pour qu'en moyenne ta semaine reste proche de ta cible. Tout l'écart passe par les glucides : protéines et lipides ne bougent pas. Le niveau du jour se lit sur tes séances et tes pas.</li>
<li><strong>Ton cycle :</strong> si tu suis ton cycle menstruel dans l'app, avec ton accord explicite et hors pilule combinée, ta cible est relevée de 150 kcal pendant ta phase lutéale estimée, dès que deux cycles complets sont enregistrés. Autour du début de tes règles, la mesure de ta dépense est mise de côté et la formule reprend la main : la rétention d'eau fausserait la tendance de ton poids.</li>
<li><strong>Un voyage ou une maladie :</strong> l'interrupteur « Voyage / maladie » gèle l'estimation de ta dépense tant qu'il est activé, puis sept jours encore. Des repas pris au hasard ou un appétit coupé ne doivent pas réécrire ton métabolisme. Seule la mesure est gelée : ton objectif ne change pas.</li>
</ul>
<p>Elles comptent aussi dans ton score : l'adéquation de ta journée à tes cibles pèse <strong>40 % du pilier nutrition</strong> du <a href="/methode/readiness-score.html">Readiness Score</a>. Des cibles fausses fausseraient ce pilier ; c'est une raison de plus pour qu'elles collent à ta dépense réelle.</p>

<h2>Ce que ce moteur n'est pas</h2>
<p>Ce n'est pas une mesure de laboratoire. Tes cibles valent ce que valent tes données : des repas oubliés ou des pesées rares retardent le passage à ta dépense réelle, et la règle des 7 700 kcal par kilo reste une approximation. Le moteur est conçu pour converger vers ta dépense réelle sans à-coups, pas pour être exact à la kilocalorie près.</p>
<p>Ce n'est pas non plus un suivi diététique médical. Ecleptic est un outil de bien-être, pas un dispositif médical : il ne pose aucun diagnostic et ne remplace ni un médecin ni un diététicien. En cas de maladie chronique, de grossesse, d'antécédents de troubles du comportement alimentaire ou de perte de poids inexpliquée, c'est à un professionnel de santé de fixer tes apports.</p>
""",
    "refs": [
        "Mifflin M. D., St Jeor S. T. et al. (1990), nouvelle équation du métabolisme de repos chez l'adulte sain, <em>American Journal of Clinical Nutrition</em>.",
        "Hall K. D. et al. (2011), quantification de l'effet d'un déséquilibre énergétique sur le poids, <em>The Lancet</em>.",
    ],
    "faq": [
        {"q": "Pourquoi mes calories cibles changent-elles d'une semaine à l'autre ?",
         "a": "Parce que ta dépense est réestimée à partir de tes pesées et de tes repas enregistrés : si ton poids bouge plus vite ou plus lentement que prévu, tes cibles suivent. Les variations sont amorties, jamais plus de 10 % à la baisse ni de 25 % à la hausse d'un calcul à l'autre, pour qu'une semaine de rétention d'eau ne les fasse pas osciller."},
        {"q": "Combien de protéines par jour selon son objectif ?",
         "a": "Dans Ecleptic, 2,2 g par kilo de poids pour la perte de poids, la prise de masse et le développement de la force, et 1,6 g par kilo pour le maintien, le cardio et l'endurance. Les lipides couvrent ensuite 30 % des calories, jamais moins de 0,8 g par kilo, et les glucides complètent le reste."},
        {"q": "Faut-il se peser tous les jours pour ajuster ses calories ?",
         "a": "Non, mais il faut des pesées régulières : l'app mesure ta dépense réelle quand elle dispose d'au moins 3 pesées et de 10 jours de repas enregistrés sur les 14 derniers jours. Plus tu te pèses, plus la tendance est fiable, et une pesée isolée pèse peu, car les valeurs aberrantes sont écrêtées."},
    ],
    "related": ["depense-energetique", "nutrition", "readiness-score"],
    "journal": ["combien-de-calories-par-jour", "deficit-calorique-comment-calculer", "proteines-par-jour-prise-de-muscle", "glucides-et-sport-combien"],
}
