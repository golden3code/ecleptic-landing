# -*- coding: utf-8 -*-
"""La méthode · Fiche — la dépense énergétique (TDEE).

Chargé par tools/build_articles.py (_load_methode) → /methode/depense-energetique.html.
Faits app vérifiés dans le code (supabase/functions/compute-expenditure) le
24/09/2026 : départ Mifflin-St Jeor × 1,3/1,4/1,55/1,7, tendance de poids lissée
(demi-vie 10 j, pesées écrêtées), apports 14 j, ≥ 10 j de repas + ≥ 3 pesées,
7 700 kcal/kg (5 500 si objectif prise de masse), garde-fous de plausibilité,
réestimation nocturne. Physiologie : composantes consensuelles (repos 60-70 %,
effet thermique ≈ 10 %), 7 700 kcal/kg = approximation (Hall 2011).
"""

PAGE = {
    "slug": "depense-energetique",
    "kind": "fiche",
    "num": None,
    "order": 9,
    "label": "La dépense énergétique (TDEE)",
    "title": "La dépense énergétique, mesurée plutôt que devinée",
    "seo_title": "Dépense énergétique (TDEE) : comment la mesurer vraiment — Ecleptic",
    "description": "Dépense énergétique (TDEE) : ses trois composantes, pourquoi les formules se trompent de plusieurs centaines de kcal, et comment Ecleptic la mesure sur toi.",
    "date": "2026-09-24",
    "lead": "Ta dépense énergétique, c'est tout ce que ton corps brûle en 24 heures. <strong>Aucune formule ne la connaît vraiment</strong> : au quotidien, la façon la plus fiable de l'approcher, c'est de la lire dans l'évolution de ton poids face à ce que tu manges.",
    "body": """
<h2>Ce que recouvre ta dépense énergétique</h2>
<p>La dépense énergétique totale, ou <strong>TDEE</strong> (pour <em>total daily energy expenditure</em>), c'est toute l'énergie que ton corps brûle en 24 heures. Elle se répartit en trois postes :</p>
<ul>
<li><strong>Le métabolisme de repos :</strong> ce que coûtent ton cœur, ton cerveau, tes organes et le maintien de ta température, même immobile. C'est la plus grosse part, souvent 60 à 70 % du total.</li>
<li><strong>L'effet thermique des aliments :</strong> l'énergie dépensée pour digérer et assimiler ce que tu manges, environ 10 %.</li>
<li><strong>L'activité :</strong> le sport et toute l'activité spontanée du quotidien. C'est la part la plus variable, d'un jour à l'autre comme d'une personne à l'autre.</li>
</ul>

<h2>Comment on la mesure</h2>
<p>En laboratoire, on la mesure par <strong>calorimétrie indirecte</strong> : l'oxygène consommé et le gaz carbonique rejeté disent combien d'énergie ton corps produit. Sur plusieurs jours, la référence est l'eau doublement marquée, précise mais réservée à la recherche. Au quotidien, il reste trois approches :</p>
<ul>
<li><strong>Les formules :</strong> ton métabolisme de repos calculé d'après ton poids, ta taille, ton âge et ton sexe, multiplié par un facteur d'activité.</li>
<li><strong>Les montres :</strong> tes calories actives, estimées d'après ton cœur et tes mouvements. Utile pour comparer tes journées, beaucoup moins pour connaître ton total.</li>
<li><strong>Le bilan observé :</strong> ce que tu manges, comparé à l'évolution de ton poids.</li>
</ul>

<h2>Pourquoi deux personnes ne dépensent pas pareil</h2>
<p>Les formules les plus connues — Harris-Benedict, la plus ancienne, puis Mifflin-St Jeor en 1990 — ont été construites sur des groupes de personnes. Elles donnent une <strong>moyenne de population</strong>, pas ta valeur : pour un individu, l'erreur peut dépasser plusieurs centaines de kilocalories par jour.</p>
<p>Un repère : pour une femme de 30 ans, 61 kg, 1,68 m, avec une activité occasionnelle, la formule donne environ 1 350 kcal au repos et 1 890 kcal par jour. Une autre femme du même gabarit peut pourtant dépenser plus, ou moins, pour deux raisons que la formule ignore :</p>
<ul>
<li><strong>La composition corporelle :</strong> à poids égal, plus de muscle signifie un métabolisme de repos plus élevé.</li>
<li><strong>L'activité spontanée :</strong> se lever souvent, marcher en téléphonant, bouger en travaillant. Elle varie énormément d'une personne à l'autre.</li>
</ul>
<p>Pour un premier ordre de grandeur selon ton profil : <a href="/articles/combien-de-calories-par-jour.html">combien de calories par jour</a>.</p>

<h2>Ce qui la fait bouger</h2>
<ul>
<li><strong>Ton activité :</strong> une séance, mais aussi la somme de tes pas et de tout ce que tu fais debout. Repères : <a href="/articles/combien-de-pas-par-jour.html">combien de pas par jour</a> et <a href="/articles/cardio-ou-muscu-pour-maigrir.html">cardio ou muscu pour maigrir</a>.</li>
<li><strong>Ton poids :</strong> un corps plus léger dépense moins. Quand tu maigris, ta dépense baisse avec toi, et en déficit on bouge souvent un peu moins sans s'en rendre compte. Une cible fixée une fois pour toutes finit donc par se tromper.</li>
<li><strong>Ton alimentation :</strong> plus tu manges, plus la digestion coûte, et les protéines coûtent un peu plus à digérer que les glucides ou les lipides.</li>
</ul>

<h2>Le bilan observé : mesurer plutôt que deviner</h2>
<p>Si ton poids est stable sur plusieurs semaines, tu manges à peu près ce que tu dépenses. S'il baisse ou monte, l'écart entre tes apports et ta dépense se lit dans la pente. Au lieu de deviner ta dépense, on la <strong>déduit de ce que ton corps fait réellement</strong> : c'est la seule approche du quotidien qui converge vers ton métabolisme, et pas vers celui d'une moyenne.</p>
<p>Pour convertir des kilos en énergie, on utilise en général <strong>7 700 kcal par kilo</strong>. C'est une approximation utile sur quelques semaines, pas une loi exacte : sur le long terme, elle surestime la perte, parce que la dépense baisse à mesure que le poids diminue, comme l'ont montré des modèles publiés dans <em>The Lancet</em> en 2011.</p>
<p>Autre piège : d'un jour à l'autre, la balance bouge surtout avec l'<strong>eau et le glycogène</strong>, les réserves de sucre de tes muscles et de ton foie, stockées avec de l'eau. Un dîner salé ou riche en glucides suffit à la faire monter le lendemain, sans un gramme de graisse en plus. D'où l'intérêt d'une tendance lissée plutôt que de la pesée du jour.</p>

<h2>Comment Ecleptic la lit</h2>
<p>L'app applique exactement ce principe, en deux temps. Au départ, faute de données, elle estime ta dépense avec l'équation de Mifflin-St Jeor, multipliée par un facteur d'activité selon ton niveau sportif : 1,3 débutant, 1,4 occasionnel, 1,55 régulier, 1,7 intensif.</p>
<p>Ensuite, elle croise la tendance de ton poids, lissée et débarrassée des pesées aberrantes, avec tes apports réellement enregistrés (voir <a href="/methode/nutrition.html">La nutrition</a>) :</p>
<div class="figs">
  <div><span class="v">14 j</span><span class="u">D'apports croisés avec ton poids</span></div>
  <div><span class="v">10 j</span><span class="u">Demi-vie de la tendance de poids</span></div>
  <div><span class="v">10 / 14</span><span class="u">Jours de repas enregistrés, au minimum</span></div>
  <div><span class="v">3</span><span class="u">Pesées minimum sur la période</span></div>
</div>
<p>La conversion retient 7 700 kcal par kilo, ou 5 500 quand ton objectif est la prise de masse. Le passage de la formule à ta mesure est progressif et amorti, et les estimations invraisemblables, trahies par des repas oubliés, sont écartées. Ta dépense est réestimée chaque nuit, et tes cibles de calories et de macros en découlent : tout le détail sur <a href="/methode/cibles.html">Les cibles</a>. Ces cibles comptent à leur tour dans le pilier nutrition du <a href="/methode/readiness-score.html">Readiness Score</a>.</p>

<h2>Limites, et quand consulter</h2>
<p>Le bilan observé ne vaut que ce que valent tes données : des repas oubliés font croire à une dépense plus basse, des pesées rares retardent la mesure.</p>
<p>Ecleptic est un outil de bien-être, pas un dispositif médical : il ne pose aucun diagnostic. Une perte ou une prise de poids inexpliquée, sans changement de tes habitudes, mérite l'avis d'un médecin. Même chose si tu es enceinte, si tu as une maladie chronique ou des antécédents de troubles du comportement alimentaire : c'est à un professionnel de fixer tes apports. Et si tu fais des malaises, ressens des palpitations ou un essoufflement anormal en réduisant tes apports, arrête et consulte ; en urgence, appelle le 15 ou le 112.</p>
""",
    "refs": [
        "Mifflin M. D., St Jeor S. T. et al. (1990), nouvelle équation du métabolisme de repos chez l'adulte sain, <em>American Journal of Clinical Nutrition</em>.",
        "Hall K. D. et al. (2011), quantification de l'effet d'un déséquilibre énergétique sur le poids, <em>The Lancet</em>.",
    ],
    "faq": [
        {"q": "Comment calculer sa dépense énergétique journalière ?",
         "a": "Une formule comme Mifflin-St Jeor estime ton métabolisme de repos à partir de ton poids, de ta taille, de ton âge et de ton sexe ; multipliée par un facteur d'activité, elle donne un point de départ. Pour connaître ta dépense réelle, le plus fiable reste de comparer tes apports à l'évolution de ton poids sur au moins deux semaines."},
        {"q": "La règle des 7 700 kcal pour perdre un kilo est-elle vraie ?",
         "a": "C'est une approximation utile sur quelques semaines, pas une loi exacte. Sur le long terme, elle surestime la perte, parce que ta dépense baisse à mesure que ton poids diminue, et d'un jour à l'autre, l'eau et le glycogène font varier la balance bien plus que la graisse."},
        {"q": "Pourquoi je ne perds pas de poids alors que je suis en déficit calorique ?",
         "a": "Souvent, le déficit n'existe que sur le papier : une formule peut surestimer ta dépense de plusieurs centaines de kilocalories par jour, et des repas oubliés faussent le compte. L'eau retenue peut aussi masquer une perte réelle pendant quelques jours : juge la tendance sur deux semaines ou plus, et parles-en à un médecin si ton poids évolue sans explication."},
    ],
    "related": ["cibles", "nutrition", "readiness-score"],
    "journal": ["combien-de-calories-par-jour", "deficit-calorique-comment-calculer", "cardio-ou-muscu-pour-maigrir", "combien-de-pas-par-jour"],
}
