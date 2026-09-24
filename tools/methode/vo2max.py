# -*- coding: utf-8 -*-
"""La méthode · Fiche — la VO₂max.

Chargé par tools/build_articles.py (_load_methode) → /methode/vo2max.html.
Faits vérifiés dans le code de l'app (lib/bioAge/*, lib/readiness/*) le 24/09/2026 :
ancre de l'âge biologique, sources par ordre de priorité (forme cardio Apple Santé,
VDOT de Daniels en relèvement prudent, équation HUNT de Nes, équation de Jackson/IMC),
demi-largeurs de départ 3 / 4 / 6 / 6,5 ans ; la VO₂max n'entre pas dans le
Readiness Score.
"""

PAGE = {
    "slug": "vo2max",
    "kind": "fiche",
    "num": None,
    "order": 3,
    "label": "La VO₂max",
    "title": "La VO₂max, ta capacité cardiorespiratoire",
    "seo_title": "VO₂max : définition, mesure et lien avec la longévité — Ecleptic",
    "description": "La VO₂max mesure l'oxygène maximal que ton corps utilise à l'effort. Définition, mesure en labo ou par la montre, repères, et son rôle dans ton âge biologique.",
    "date": "2026-09-24",
    "lead": "C'est le chiffre qui résume le mieux ton moteur aérobie, et l'un de ceux que la recherche relie le plus fortement à la longévité. Voici ce qu'elle mesure, comment l'estimer sans laboratoire et comment Ecleptic s'en sert pour calculer ton <strong>âge biologique</strong>.",
    "body": """
<h2>Ce que mesure la VO₂max</h2>
<p>La VO₂max, c'est le <strong>volume maximal d'oxygène que ton organisme peut utiliser par minute pendant un effort maximal</strong>. Elle s'exprime en millilitres par kilo de poids de corps et par minute (ml/kg/min), ce qui permet de comparer des gabarits différents.</p>
<p>Ce chiffre résume toute la chaîne de l'oxygène : tes <strong>poumons</strong> le font passer dans le sang, ton <strong>cœur</strong> le pompe, tes <strong>vaisseaux</strong> le distribuent et tes <strong>muscles</strong> l'utilisent pour produire de l'énergie. Chez une personne en bonne santé, c'est surtout la capacité du cœur à pomper qui fixe le plafond.</p>

<h2>Pourquoi elle compte autant</h2>
<p>La capacité cardiorespiratoire est l'un des plus puissants prédicteurs de la mortalité toutes causes. Les grandes études qui l'ont mesurée chez des dizaines de milliers de personnes vont dans le même sens : plus elle est haute, plus le risque est bas. Et <strong>ce sont les moins en forme qui ont le plus à gagner</strong> : sortir du groupe le plus bas est le pas qui rapporte le plus.</p>

<h2>Comment on la mesure</h2>
<ul>
<li><strong>En laboratoire :</strong> l'épreuve d'effort avec analyse des gaz respirés reste la référence. Sur tapis ou sur vélo, l'intensité monte jusqu'à l'épuisement pendant qu'un masque mesure l'oxygène consommé.</li>
<li><strong>Avec une montre :</strong> elle l'estime pendant un effort en extérieur, à partir de ta fréquence cardiaque et de ton allure mesurée par GPS.</li>
<li><strong>Sans effort :</strong> des équations l'estiment à partir de données simples. Celle de Nes et al. (2011), établie sur la cohorte norvégienne HUNT, utilise le tour de taille, la fréquence cardiaque au repos et le niveau d'activité ; celle de Jackson et al. (1990) s'appuie notamment sur l'IMC.</li>
<li><strong>Par tes courses :</strong> la formule VDOT de Jack Daniels déduit une VO₂max d'un temps réalisé sur une distance, à condition que l'effort ait été vraiment maximal.</li>
</ul>

<h2>Des valeurs très personnelles</h2>
<p>Il n'existe pas de bonne VO₂max dans l'absolu. Elle culmine chez le jeune adulte, puis baisse avec l'âge. À âge égal, elle est en moyenne plus basse chez la femme, notamment parce que son sang contient moins d'hémoglobine et que sa part de masse grasse est plus élevée. La génétique compte aussi : à entraînement égal, tout le monde ne progresse pas au même rythme. Chez les meilleurs athlètes d'endurance, elle peut dépasser 80 ml/kg/min.</p>
<p>Une VO₂max ne se lit donc jamais seule, mais <strong>face aux valeurs de référence de ton âge et de ton sexe</strong>. C'est exactement ce que fait Ecleptic.</p>

<h2>Ce qui la fait bouger</h2>
<ul>
<li><strong>L'endurance en zone 2 :</strong> du volume à allure facile, où tu peux encore parler, construit la base, avec un cœur qui éjecte plus de sang à chaque battement et plus de capillaires et de mitochondries dans les muscles. Le détail : <a href="/articles/zone-2-cardio-cest-quoi.html">la zone 2, c'est quoi</a>.</li>
<li><strong>Les intervalles :</strong> de courtes répétitions proches de ton maximum poussent le plafond lui-même. Une à deux séances par semaine, posées sur cette base, suffisent. Le dosage : <a href="/articles/hiit-combien-de-fois-par-semaine.html">combien de séances de HIIT par semaine</a>.</li>
<li><strong>Le poids :</strong> comme elle se calcule par kilo, perdre de la masse grasse fait monter ta VO₂max relative.</li>
<li><strong>L'inactivité :</strong> quelques semaines sans entraînement suffisent à la faire reculer. Elle s'entretient.</li>
<li><strong>L'altitude :</strong> l'air y apporte moins d'oxygène, et ta VO₂max baisse tant que tu y restes.</li>
</ul>
<p>Surtout, elle s'entraîne à tout âge. Passé 40 ans, la progression reste réelle, à condition de soigner davantage la <a href="/articles/recuperation-apres-40-ans.html">récupération</a>. Le plan complet : <a href="/articles/vo2max-comment-l-ameliorer.html">comment améliorer ta VO₂max</a>.</p>

<h2>Comment Ecleptic la lit et l'utilise</h2>
<p>Dans l'app, la VO₂max est <strong>l'ancre de ton <a href="/methode/age-biologique.html">âge biologique</a></strong> : elle donne un âge de forme, que tes habitudes ajustent ensuite. L'app la prend à la meilleure source disponible, et la marge d'incertitude de départ de ton âge biologique en dépend :</p>
<ul>
<li><strong>Mesurée par ta montre, ±3 ans :</strong> la « forme cardio » lue dans Apple Santé.</li>
<li><strong>Calculée depuis tes courses, ±4 ans :</strong> avec la formule VDOT.</li>
<li><strong>Estimée sans effort, ±6 ans :</strong> par l'équation HUNT, à partir de ton tour de taille, de ta <a href="/methode/frequence-cardiaque-repos.html">fréquence cardiaque au repos</a> et de ton niveau d'activité.</li>
<li><strong>À défaut, ±6,5 ans :</strong> par l'équation de Jackson, à partir de ton IMC.</li>
</ul>
<p>Une règle de prudence encadre les courses : comme une course n'est pas forcément un effort maximal, <strong>la VDOT ne peut que relever l'estimation sans effort, jamais la faire baisser</strong>. Sans estimation de base, une VDOT inférieure à la valeur attendue pour ton âge est ignorée : un simple footing ne doit pas te vieillir.</p>
<p>Contrairement à ta <a href="/methode/variabilite-cardiaque.html">variabilité cardiaque</a>, la VO₂max n'entre pas dans le <a href="/methode/readiness-score.html">Readiness Score</a> : elle décrit ta capacité, qui évolue sur des semaines, pas ton état du jour.</p>

<h2>Les limites de la mesure</h2>
<p>Hors laboratoire, toute VO₂max est une <strong>estimation</strong>. Celle de la montre n'est calculée que sur certains efforts en extérieur et dépend de leurs conditions, comme le dénivelé ou la chaleur. Les équations sans effort visent juste en moyenne, mais peuvent se tromper nettement pour une personne donnée. La VDOT suppose un effort maximal. Et un traitement qui ralentit le cœur peut fausser les estimations fondées sur la fréquence cardiaque.</p>
<p>La bonne lecture est donc la <strong>tendance sur plusieurs semaines</strong>, pas une valeur isolée. C'est aussi pour cela qu'Ecleptic calcule ton âge biologique avec une marge d'incertitude et lisse sa valeur dans le temps.</p>

<h2>Quand consulter</h2>
<p>Ecleptic est une app de bien-être, pas un dispositif médical : ta VO₂max n'y sert à poser aucun diagnostic. Consulte un médecin si elle baisse nettement et durablement sans raison apparente, ou si l'effort s'accompagne d'un essoufflement anormal, d'une douleur thoracique, de palpitations ou d'un malaise. En cas d'urgence, appelle le 15 ou le 112.</p>
<p>Avant de reprendre un entraînement intense après une longue pause, surtout avec des facteurs de risque cardiovasculaire, demande un avis médical. Une épreuve d'effort, idéalement avec analyse des gaz, vérifie que ton cœur suit et mesure ta VO₂max pour de bon.</p>
""",
    "refs": [
        "Kodama S. et al. (2009), la capacité cardiorespiratoire comme prédicteur de la mortalité toutes causes, <em>JAMA</em>.",
        "Mandsager K. et al. (2018), capacité cardiorespiratoire et mortalité à long terme, <em>JAMA Network Open</em>.",
        "Nes B. M. et al. (2011), estimation de la VO₂pic sans test d'effort : l'étude HUNT, <em>Medicine &amp; Science in Sports &amp; Exercise</em>.",
        "Jackson A. S. et al. (1990), prédiction de la capacité aérobie sans test d'effort, <em>Medicine &amp; Science in Sports &amp; Exercise</em>.",
        "Daniels J. et Gilbert J. (1979), tables de performance VDOT, <em>Oxygen Power</em>.",
    ],
    "faq": [
        {"q": "Qu'est-ce qu'une bonne VO₂max pour son âge ?",
         "a": "Il n'y a pas de seuil universel : la VO₂max se lit selon l'âge et le sexe, car elle baisse avec les années et reste en moyenne plus basse chez la femme. Ce qui compte, c'est ta position face aux valeurs de référence de ton âge et ta progression dans le temps ; les meilleurs athlètes d'endurance peuvent dépasser 80 ml/kg/min."},
        {"q": "La VO₂max de l'Apple Watch est-elle fiable ?",
         "a": "C'est une estimation, pas une mesure de laboratoire : la montre la déduit notamment de ta fréquence cardiaque et de ton allure pendant un effort en extérieur. Elle est surtout utile pour suivre ta tendance sur plusieurs semaines ; seule une épreuve d'effort avec analyse des gaz donne une mesure directe."},
        {"q": "Comment augmenter sa VO₂max après 40 ans ?",
         "a": "Elle s'entraîne à tout âge : combine beaucoup d'endurance facile en zone 2, où tu peux encore parler, avec une à deux séances d'intervalles par semaine, en laissant des jours de récupération entre elles. Les progrès se mesurent en mois. Si tu reprends après une longue pause ou si tu as des facteurs de risque cardiovasculaire, demande d'abord un avis médical."},
    ],
    "related": ["age-biologique", "frequence-cardiaque-repos", "variabilite-cardiaque", "readiness-score"],
    "journal": ["vo2max-comment-l-ameliorer", "zone-2-cardio-cest-quoi", "hiit-combien-de-fois-par-semaine", "sport-en-altitude-effets"],
}
