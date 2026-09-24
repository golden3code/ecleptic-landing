# -*- coding: utf-8 -*-
"""La méthode · Moteur II — l'âge biologique.

Chargé par tools/build_articles.py (_load_methode) → /methode/age-biologique.html.
Faits vérifiés dans le code de l'app (lib/bioAge/*) le 24/09/2026 : ancre VO2max
(mesurée > VDOT en relèvement prudent > Nes/HUNT > Jackson/IMC), demi-largeurs de
départ 3 / 4 / 6 / 6,5 ans, 7 modificateurs bornés (HRV ±3, FC repos ±2, taille ±2,
activité ±2, sommeil −0,5 à +1,5, nutrition ±1, hygiène de vie 0 à +3), pas de double
comptage avec l'équation, bornes ±25 ans et 18-95 ans, lissage EWMA.
Volontairement non affirmé : « normes HUNT partout » (la référence neutre mêle
FRIEND et HUNT, HARSHNESS = 0,5), le seuil nuit + repas + activité (retiré du code)
et l'affichage de la fourchette (calculée et stockée, mais rendue par aucun écran).
"""

PAGE = {
    "slug": "age-biologique",
    "kind": "moteur",
    "num": "II",
    "order": 2,
    "label": "L'âge biologique",
    "title": "L'âge biologique, ancré sur ta VO₂max",
    "seo_title": "Âge biologique : comment il est calculé, étape par étape — Ecleptic",
    "description": "Ton âge biologique part de ta VO₂max, convertie en âge de forme, puis sept facteurs de ton quotidien l'ajustent. Sources, bornes, marge d'erreur : la méthode.",
    "date": "2026-09-24",
    "lead": "Ecleptic estime l'âge de ton corps en deux temps : ta VO₂max donne un <strong>âge de forme</strong>, puis sept facteurs tirés de tes habitudes l'ajustent, chacun dans des limites strictes. Voici le calcul exact, avec ses sources et sa marge d'erreur.",
    "body": """
<h2>Ce que le moteur calcule</h2>
<p>Ton âge réel compte les années écoulées. Ton âge biologique estime autre chose : <strong>l'âge qu'a ton corps, à en juger par ta forme et par tes habitudes</strong>. Deux personnes nées la même année peuvent avoir des années d'écart sur ce terrain, et c'est cet écart que le moteur chiffre.</p>
<p>Le calcul se fait en deux temps. D'abord, ta <a href="/methode/vo2max.html">VO₂max</a>, l'indicateur que la recherche associe le plus fortement à la longévité, est convertie en âge de forme. Ensuite, sept modificateurs issus de tes habitudes ajustent cet âge. Chacun est borné et signé : en « + », il te vieillit ; en « − », il te rajeunit.</p>

<h2>Étape 1 · Trouver ta meilleure VO₂max</h2>
<p>La VO₂max, c'est le volume maximal d'oxygène que ton corps peut utiliser par minute pendant un effort maximal. L'app la prend à la <strong>meilleure source disponible</strong>, dans cet ordre :</p>
<ul>
<li><strong>Mesurée par ta montre :</strong> la « forme cardio » enregistrée dans Apple Santé, calculée pendant tes efforts en extérieur.</li>
<li><strong>Calculée depuis tes courses :</strong> avec la formule VDOT de Jack Daniels, standard de l'entraînement d'endurance depuis plus de quarante ans, qui déduit une VO₂max d'une distance et d'un temps.</li>
<li><strong>Estimée sans effort :</strong> avec l'équation de Nes et al., établie sur la cohorte norvégienne HUNT, à partir de ton tour de taille, de ta <a href="/methode/frequence-cardiaque-repos.html">fréquence cardiaque au repos</a> et de ton niveau d'activité.</li>
<li><strong>À défaut :</strong> avec l'équation de Jackson et al. (1990), à partir de ton IMC.</li>
</ul>
<p>Les courses obéissent à une règle de prudence. <strong>Une course n'est pas forcément un effort maximal</strong>, et un footing tranquille sous-estime ta VO₂max. La VDOT ne peut donc que relever l'estimation sans effort, jamais la faire baisser. Sans estimation de base, une VDOT inférieure à la valeur attendue pour ton âge est ignorée : un simple footing ne doit pas te vieillir.</p>
<p>Plus la source est directe, plus le résultat est précis. Voici la demi-largeur de départ de la marge d'incertitude calculée pour ton âge biologique, selon la source :</p>
<div class="figs">
  <div><span class="v">±3</span><span class="u">ans · mesurée par la montre</span></div>
  <div><span class="v">±4</span><span class="u">ans · calculée sur tes courses</span></div>
  <div><span class="v">±6</span><span class="u">ans · équation HUNT</span></div>
  <div><span class="v">±6,5</span><span class="u">ans · équation de Jackson</span></div>
</div>

<h2>Étape 2 · Convertir ta VO₂max en âge de forme</h2>
<p>Une VO₂max seule ne veut pas dire grand-chose : la même valeur peut être excellente à 60 ans et banale à 25. L'app la compare donc à la <strong>valeur de référence pour ton âge et ton sexe</strong>, puis traduit l'écart en années. Au-dessus de la référence, ton âge de forme passe sous ton âge réel ; en dessous, il passe au-dessus.</p>
<p>Cette conversion s'appuie sur les travaux menés sur la cohorte HUNT, une vaste étude de population norvégienne où la VO₂max de milliers d'adultes a été mesurée en laboratoire. C'est l'ancre du calcul : tout le reste vient l'ajuster, jamais la remplacer.</p>

<h2>Étape 3 · Sept modificateurs, bornés et signés</h2>
<p>L'âge de forme est ensuite ajusté par tes habitudes. Chaque facteur a son plafond, pour qu'aucun ne puisse à lui seul emporter le résultat :</p>
<ul>
<li><strong>La variabilité cardiaque — jusqu'à ±3 ans.</strong> Ta <a href="/methode/variabilite-cardiaque.html">HRV</a> est comparée aux valeurs attendues pour ton âge : au-dessus, elle te rajeunit ; en dessous, elle te vieillit. Si tu prends un traitement qui ralentit le cœur, elle peut ne compter qu'à demi-poids.</li>
<li><strong>La fréquence cardiaque au repos — jusqu'à ±2 ans.</strong> Elle est située face à une référence d'environ 60 battements par minute (± 9) : plus basse, elle te rajeunit ; plus haute, elle te vieillit.</li>
<li><strong>Le tour de taille — jusqu'à ±2 ans.</strong> Il est comparé aux seuils de risque de l'OMS : 94 cm chez l'homme, 80 cm chez la femme.</li>
<li><strong>L'activité — jusqu'à ±2 ans.</strong> Tes minutes d'activité par semaine, face aux 150 minutes recommandées par l'OMS.</li>
<li><strong>Le sommeil — de −6 mois à +1,5 an.</strong> Ce facteur n'est pas symétrique : le sommeil peut t'ajouter jusqu'à un an et demi, et te faire gagner au plus six mois. Une durée comprise entre 7 h et 8 h 30 et des heures de coucher régulières jouent en ta faveur ; des nuits hors de ce créneau et des couchers irréguliers pèsent dans l'autre sens. Le détail : <a href="/methode/besoin-de-sommeil.html">ton besoin de sommeil</a>.</li>
<li><strong>L'alimentation — jusqu'à ±1 an.</strong> La qualité de ce que tu manges, telle que la mesure ton <a href="/methode/nutrition.html">score nutrition</a>.</li>
<li><strong>L'hygiène de vie — jusqu'à +3 ans.</strong> Ce que tu déclares : la nicotine ajoute 2 ans, l'alcool jusqu'à 1,5 an selon le nombre de jours par semaine où tu bois. Ce facteur ne peut jamais te rajeunir.</li>
</ul>
<p>Une règle évite de compter deux fois la même chose. <strong>La fréquence cardiaque au repos, le tour de taille et l'activité ne jouent comme modificateurs que si ta VO₂max est mesurée par ta montre ou calculée depuis tes courses.</strong> Quand elle est estimée sans effort, ils sont désactivés : l'équation HUNT les contient déjà tous les trois, et les recompter doublerait leur poids. La variabilité cardiaque, le sommeil, l'alimentation et l'hygiène de vie, qu'aucune équation ne contient, s'appliquent dès que la donnée existe.</p>

<h2>Étape 4 · Borner, lisser, encadrer</h2>
<ul>
<li><strong>Des bornes :</strong> ton âge biologique reste dans une fenêtre de 25 ans de part et d'autre de ton âge réel, et toujours entre 18 et 95 ans. C'est un garde-fou contre les valeurs aberrantes.</li>
<li><strong>Un lissage :</strong> la valeur affichée est une moyenne mobile exponentielle de tes estimations successives. Les plus récentes pèsent davantage, mais une mesure isolée ne fait pas sauter le chiffre.</li>
<li><strong>Une marge d'incertitude :</strong> chaque résultat est calculé avec la sienne, dont la largeur de départ dépend de la source de ta VO₂max.</li>
</ul>

<h2>Pourquoi ces choix</h2>
<ul>
<li><strong>La VO₂max comme ancre :</strong> c'est l'indicateur de forme que la recherche relie le plus fortement à la longévité. Même estimée sans le moindre effort, à partir de quelques données simples, la capacité cardiorespiratoire prédit la mortalité à long terme : l'équipe norvégienne à l'origine de l'équation HUNT l'a montré.</li>
<li><strong>Une ancre et des modificateurs, pas une moyenne de tout :</strong> additionner des facteurs qui se recoupent gonflerait artificiellement leur effet. Chaque donnée compte une fois, et une seule.</li>
<li><strong>La prudence avec les courses :</strong> une sortie lente ne prouve pas une faible capacité. Mieux vaut ignorer une course que d'en tirer un verdict faux.</li>
<li><strong>Un chiffre honnête plutôt que flatteur :</strong> la référence n'est pas choisie pour faire plaisir. Un âge biologique complaisant ne t'apprendrait rien ; un chiffre juste te montre ce qu'il te reste à gagner.</li>
<li><strong>Un résultat dès le premier jour :</strong> les équations sans effort permettent une première estimation dès ton inscription, sans attendre des semaines d'historique. Sa marge d'incertitude, plus large au départ, tient compte de ce que vaut ce premier chiffre.</li>
</ul>

<h2>Ce que tu vois dans l'app</h2>
<ul>
<li><strong>Ton âge biologique</strong>, lissé dans le temps, et son écart avec ton âge réel.</li>
<li><strong>Le détail des facteurs</strong>, chacun avec son effet en années : en « + » s'il te vieillit, en « − » s'il te rajeunit.</li>
<li><strong>Une première estimation dès ton inscription</strong>, qui s'affine à mesure que ta montre, tes séances, tes nuits et tes repas alimentent le calcul.</li>
</ul>
<p>Le levier le plus puissant reste l'ancre : ta VO₂max s'entraîne à tout âge, et chaque progrès se retrouve dans ton âge de forme. La méthode pour la faire monter : <a href="/articles/vo2max-comment-l-ameliorer.html">comment améliorer ta VO₂max</a>.</p>

<h2>Ce que l'âge biologique n'est pas</h2>
<p>C'est un indicateur de bien-être, pas un diagnostic médical, et Ecleptic n'est pas un dispositif médical. Il ne prédit ni ta durée de vie ni ta santé future : c'est une estimation, avec sa marge d'erreur, de l'âge qu'a ton corps à en juger par ta forme et tes habitudes. Vu cette marge, un écart d'un an ne signifie rien en soi ; c'est la tendance sur plusieurs mois qui compte.</p>
<p>Ce n'est pas non plus un indicateur du jour. Pour savoir si tu peux pousser aujourd'hui, regarde ton <a href="/methode/readiness-score.html">Readiness Score</a> ; l'âge biologique, lui, évolue au rythme de tes habitudes. Et si tu ressens un essoufflement inhabituel, une douleur thoracique, des palpitations ou un malaise, c'est un médecin qu'il faut consulter ; en cas d'urgence, appelle le 15 ou le 112.</p>
""",
    "refs": [
        "Nes B. M. et al. (2011), estimation de la VO₂pic sans test d'effort : l'étude HUNT, <em>Medicine &amp; Science in Sports &amp; Exercise</em>.",
        "Nes B. M. et al. (2014), un modèle simple de capacité cardiorespiratoire sans effort prédit la mortalité à long terme, <em>Medicine &amp; Science in Sports &amp; Exercise</em>.",
        "Jackson A. S. et al. (1990), prédiction de la capacité aérobie sans test d'effort, <em>Medicine &amp; Science in Sports &amp; Exercise</em>.",
        "Daniels J. et Gilbert J. (1979), tables de performance VDOT, <em>Oxygen Power</em>.",
        "OMS (2011), tour de taille et rapport taille-hanches : rapport d'une consultation d'experts.",
    ],
    "faq": [
        {"q": "Comment est calculé l'âge biologique dans Ecleptic ?",
         "a": "En deux temps. Ta VO₂max, mesurée par ta montre, calculée depuis tes courses ou estimée sans effort, est convertie en âge de forme ; puis sept facteurs l'ajustent, chacun dans une limite fixe : variabilité cardiaque, fréquence cardiaque au repos, tour de taille, activité, sommeil, alimentation et hygiène de vie."},
        {"q": "Peut-on connaître son âge biologique sans montre connectée ?",
         "a": "Oui. Sans VO₂max mesurée par une montre, Ecleptic l'estime sans effort avec l'équation HUNT (tour de taille, fréquence cardiaque au repos, niveau d'activité) ou celle de Jackson (IMC), et une course soutenue peut relever cette estimation grâce à la formule VDOT. Le résultat est simplement moins précis : sa marge d'incertitude de départ passe de ±3 ans avec une VO₂max mesurée par la montre à ±4, ±6 ou ±6,5 ans selon la source."},
        {"q": "Pourquoi mon âge biologique est-il plus élevé que mon âge réel ?",
         "a": "Soit ta VO₂max, l'ancre du calcul, est sous la valeur de référence pour ton âge et ton sexe, soit certains facteurs te vieillissent, comme des nuits hors du créneau de 7 h à 8 h 30, une variabilité cardiaque basse pour ton âge, la nicotine ou l'alcool. Garde aussi en tête la marge d'incertitude : avec une estimation sans effort, elle est large, et un écart de quelques années peut ne rien signifier."},
    ],
    "related": ["vo2max", "variabilite-cardiaque", "frequence-cardiaque-repos", "besoin-de-sommeil", "nutrition", "readiness-score"],
    "journal": ["vo2max-comment-l-ameliorer", "zone-2-cardio-cest-quoi", "se-coucher-meme-heure-regularite", "tabac-nicotine-et-sport"],
}
