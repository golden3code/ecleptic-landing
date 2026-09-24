# -*- coding: utf-8 -*-
"""La méthode · Moteur I — le Readiness Score (page modèle des pages méthode).

Chargé par tools/build_articles.py (_load_methode) → /methode/readiness-score.html.
Faits vérifiés dans le code de l'app (lib/readiness/*) le 24/09/2026 : poids des
piliers 42/21/21/16, sous-facteurs, ligne de base 42 j (min 7, confiance pleine 28),
redistribution des poids manquants, plafond alcool 80.
"""

PAGE = {
    "slug": "readiness-score",
    "kind": "moteur",
    "num": "I",
    "order": 1,
    "label": "Le Readiness Score",
    "title": "Le Readiness Score, pilier par pilier",
    "seo_title": "Readiness Score : comment il est calculé, pilier par pilier — Ecleptic",
    "description": "Le Readiness Score croise tes vitaux de la nuit, ton sommeil, ta nutrition et ton rythme. Ses 4 piliers, leurs poids et la méthode, sans boîte noire.",
    "date": "2026-09-24",
    "lead": "Chaque matin, un chiffre sur 100 te dit si ton corps est prêt à pousser ou s'il a besoin de récupérer. Voici exactement comment il est construit : quatre piliers, dix-sept signaux, et une règle qui change tout : tes vitaux ne sont comparés qu'à toi-même.",
    "body": """
<h2>Ce que le score mesure vraiment</h2>
<p>Le Readiness Score répond à une seule question : <strong>aujourd'hui, ton corps est-il en état d'encaisser une charge ?</strong> Ce n'est ni une note de forme physique, ni une note de santé. C'est une lecture de ton état de récupération à un instant donné, construite à partir de tout ce que l'app sait de ta nuit, de tes repas et de tes séances.</p>
<p>Le score est calculé à partir de ta nuit dès ton réveil, puis se met à jour au fil de la journée à mesure que tu enregistres tes repas et tes séances. Il repose sur quatre piliers, pondérés selon leur poids dans la récupération :</p>
<div class="figs">
  <div><span class="v">42</span><span class="u">Vitaux de la nuit</span></div>
  <div><span class="v">21</span><span class="u">Sommeil</span></div>
  <div><span class="v">21</span><span class="u">Nutrition</span></div>
  <div><span class="v">16</span><span class="u">Rythme et charge</span></div>
</div>

<h2>Pilier 1 · Les vitaux de la nuit (42 points)</h2>
<p>C'est le pilier le plus lourd, parce que c'est le reflet le plus direct et le plus objectif de l'état de ton système nerveux autonome. Cinq signaux, mesurés par ta montre au repos, pour l'essentiel pendant ton sommeil, et lus via Apple Santé :</p>
<ul>
<li><strong>La <a href="/methode/variabilite-cardiaque.html">variabilité cardiaque (HRV)</a> — 45 % du pilier.</strong> Plus elle est haute par rapport à ta normale, mieux tu as récupéré.</li>
<li><strong>La <a href="/methode/frequence-cardiaque-repos.html">fréquence cardiaque au repos</a> — 30 %.</strong> Plus elle est basse par rapport à ta normale, mieux c'est.</li>
<li><strong>La <a href="/methode/frequence-respiratoire.html">fréquence respiratoire</a> — 12 %.</strong> Une hausse inhabituelle est souvent le premier signe d'une fatigue ou d'une infection qui démarre.</li>
<li><strong>La <a href="/methode/saturation-oxygene.html">saturation en oxygène</a> — 7 %.</strong></li>
<li><strong>La <a href="/methode/temperature-poignet.html">température du poignet</a> — 6 %.</strong> Ici, c'est l'écart qui compte, dans un sens comme dans l'autre.</li>
</ul>
<p>Le détail de chaque signal est sur la page <a href="/methode/vitaux.html">Les vitaux</a>.</p>

<h2>Pilier 2 · Le sommeil (21 points)</h2>
<ul>
<li><strong>La durée face à ton besoin — 40 %.</strong> Ton besoin part des repères de la National Sleep Foundation pour ton âge, puis s'ajuste à la longueur de tes propres cycles dès qu'elle est connue. Le détail : <a href="/methode/besoin-de-sommeil.html">ton besoin de sommeil</a>.</li>
<li><strong>Les phases profondes et paradoxales — 25 %.</strong> Uniquement quand ta montre les a réellement mesurées : l'app n'invente jamais de phases pour une nuit saisie à la main.</li>
<li><strong>L'efficacité — 20 %.</strong> La part du temps passé au lit où tu dormais vraiment.</li>
<li><strong>La régularité — 15 %.</strong> Des heures de coucher et de lever stables, le facteur le plus sous-estimé du sommeil.</li>
</ul>

<h2>Pilier 3 · La nutrition (21 points)</h2>
<ul>
<li><strong>L'adéquation à tes cibles — 40 %.</strong> Calories et macronutriments de la journée, face aux cibles calculées par le moteur <a href="/methode/cibles.html">Les cibles</a>.</li>
<li><strong>Le refuel après l'effort — 25 %.</strong> Les protéines prises après une séance. Les jours de repos, ce critère disparaît et son poids passe aux autres.</li>
<li><strong>Les micronutriments — 20 %.</strong> La couverture de tes besoins, calculée à partir des valeurs mesurées de la <a href="/methode/nutrition.html">table Ciqual de l'ANSES</a>.</li>
<li><strong>L'hydratation — 15 %.</strong> Ce que tu as bu face à ce qui est recommandé pour toi.</li>
</ul>
<p>Une règle à part : <strong>si tu as bu de l'alcool la veille, le pilier nutrition est plafonné à 80</strong>, quelle que soit la qualité du reste. L'alcool pèse sur la récupération, et aucun repas parfait ne l'efface.</p>

<h2>Pilier 4 · Le rythme et la charge (16 points)</h2>
<ul>
<li><strong>La charge d'entraînement — 40 %.</strong> L'équilibre entre ta charge récente et ta charge habituelle. Une hausse brutale fait baisser le score : une séance dure se paie en général 24 à 72 heures.</li>
<li><strong>La régularité de tes rythmes — 30 %.</strong> Coucher, lever et repas à heures stables.</li>
<li><strong>La cadence — 20 %.</strong> Tes jours actifs face à ta norme, et la dérive du week-end.</li>
<li><strong>Les courbatures — 10 %.</strong> Ce que tu ressens au réveil, quand tu le renseignes.</li>
</ul>

<h2>Toi contre toi : la ligne de base</h2>
<p>C'est le cœur de la méthode. <strong>Tes vitaux ne sont jamais comparés à une norme de population.</strong> Une HRV de 45 ms peut être excellente pour toi et basse pour quelqu'un d'autre : ce qui compte, c'est l'écart à ta propre normale.</p>
<p>Pour chacun des cinq vitaux, l'app calcule ta moyenne et ta variabilité habituelle sur les <strong>42 derniers jours</strong> (environ six semaines), sans compter le jour évalué, puis mesure de combien la valeur du matin s'en écarte. Il faut au moins 7 jours de données pour qu'une ligne de base existe, et 28 jours pour qu'elle soit pleinement fiable. Le fonctionnement complet : <a href="/methode/ligne-de-base.html">ta ligne de base</a>.</p>
<p>Les autres piliers suivent la même logique personnelle, avec leur propre référence : ton sommeil est jugé face à ton besoin, ta nutrition face à tes cibles, ta charge face à ta charge habituelle.</p>

<h2>Sans montre, le score s'adapte</h2>
<p>Quand un pilier n'a pas de données, il n'est pas remplacé par une valeur inventée : il est retiré, et <strong>son poids est redistribué entre les autres</strong>. Sans montre, pas de vitaux : le sommeil, la nutrition et le rythme se partagent alors les 100 points. Le même principe s'applique à l'intérieur de chaque pilier.</p>
<p>En parallèle, un indice de confiance indique sur quelle quantité de données repose le score du jour. Un score construit sur trois jours d'historique ne se lit pas comme un score construit sur deux mois.</p>

<h2>Ce que tu vois dans l'app</h2>
<ul>
<li><strong>Le score du jour</strong> sur l'écran d'accueil ; un toucher l'ouvre en détail, avec un verdict pour ta journée.</li>
<li><strong>Le détail des quatre piliers</strong>, avec en rouge celui qui te tire vers le bas, et le sous-facteur précis à surveiller.</li>
<li><strong>Tes tendances</strong> sur plusieurs semaines, pour le score et pour chaque pilier.</li>
<li><strong>Les croisements du Labo</strong>, qui montrent par exemple l'effet d'un verre d'alcool ou d'un dîner tardif sur ton score du lendemain, chez toi.</li>
</ul>

<h2>Ce que le score n'est pas</h2>
<p>Le Readiness Score est un outil de bien-être pour doser ton effort. Ce n'est pas un dispositif médical et il ne pose aucun diagnostic. Une journée basse n'est pas une alerte : c'est la tendance sur plusieurs jours qui compte. Si tu ressens des symptômes inhabituels, c'est un médecin qu'il faut consulter, pas un score.</p>
""",
    "refs": [
        "Hirshkowitz M. et al. (2015), recommandations de durée de sommeil de la National Sleep Foundation, <em>Sleep Health</em>.",
        "Plews D. J. et al. (2013), suivi de la variabilité cardiaque et adaptation à l'entraînement chez l'athlète d'endurance, <em>Sports Medicine</em>.",
        "Buchheit M. (2014), suivi de l'état d'entraînement par les mesures de fréquence cardiaque, <em>Frontiers in Physiology</em>.",
    ],
    "faq": [
        {"q": "Comment est calculé le Readiness Score d'Ecleptic ?",
         "a": "Il combine quatre piliers : les vitaux de la nuit (42 points), le sommeil (21), la nutrition (21) et le rythme avec la charge d'entraînement (16). Tes vitaux sont comparés à ta propre moyenne des 42 derniers jours, jamais à une norme de population ; ton sommeil est jugé face à ton besoin, ta nutrition face à tes cibles."},
        {"q": "Faut-il une montre connectée pour avoir un Readiness Score ?",
         "a": "Non. Sans montre, les vitaux ne sont pas mesurés : leur poids est redistribué entre le sommeil, la nutrition et le rythme, et un indice de confiance indique sur combien de données repose le score. Avec une montre, le score gagne son pilier le plus précis."},
        {"q": "Pourquoi mon Readiness Score est-il bas alors que je me sens bien ?",
         "a": "Le score compare tes vitaux à ta propre normale : une variabilité cardiaque ou une fréquence au repos qui s'écarte de tes habitudes peut précéder la sensation de fatigue. Regarde le pilier en rouge et le sous-facteur à surveiller, puis la tendance des jours suivants."},
    ],
    "related": ["variabilite-cardiaque", "frequence-cardiaque-repos", "ligne-de-base", "besoin-de-sommeil", "vitaux", "cibles"],
    "journal": ["readiness-score-comment-ca-marche", "comment-savoir-si-on-est-bien-recupere", "hrv-variabilite-frequence-cardiaque", "surentrainement-signes"],
}
