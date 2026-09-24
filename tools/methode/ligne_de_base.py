# -*- coding: utf-8 -*-
"""La méthode · Fiche 7 — Ta ligne de base (la normalisation « toi contre toi »).

Chargé par tools/build_articles.py (_load_methode) → /methode/ligne-de-base.html.
Faits vérifiés dans le code de l'app (lib/readiness/baseline.ts, physio.ts) le
24/09/2026 : fenêtre glissante 42 j, jour évalué exclu, moyenne + écart-type
d'échantillon, z-score converti en points selon le sens du signal (température
= écart dans les deux sens), 0 point à 2 écarts-types du mauvais côté, min 7
jours, confiance pleine à 28 jours. La baseline ne s'applique qu'aux 5 vitaux :
le pilier sommeil a pour référence le besoin de sommeil (fiche 8).
"""

PAGE = {
    "slug": "ligne-de-base",
    "kind": "fiche",
    "num": None,
    "order": 7,
    "label": "Ta ligne de base",
    "title": "Ta ligne de base, toi contre toi",
    "seo_title": "Ligne de base : tes vitaux comparés à toi sur 42 jours — Ecleptic",
    "description": "Ta ligne de base, c'est ta normale sur 42 jours. Comment Ecleptic s'en sert pour juger ta HRV, ta fréquence cardiaque et tes vitaux : calcul, z-score, limites.",
    "date": "2026-09-24",
    "lead": "Une HRV de 45 ms ne veut rien dire tant qu'on ne connaît pas ta normale. Voici comment l'app construit cette normale, jour après jour, et pourquoi te comparer à toi-même est plus juste que te comparer à une moyenne.",
    "body": """
<h2>Ta normale, pas celle de la population</h2>
<p>Ta ligne de base, c'est <strong>la valeur habituelle d'un signal chez toi</strong>, avec l'amplitude normale de ses variations, calculées sur tes dernières semaines. C'est la référence contre laquelle l'app juge chaque matin tes <a href="/methode/vitaux.html">vitaux de la nuit</a> : variabilité cardiaque, fréquence cardiaque au repos, fréquence respiratoire, saturation en oxygène et température du poignet.</p>
<p>Le principe tient en trois mots : <strong>toi contre toi</strong>. Une HRV de 45 ms peut être excellente pour toi et médiocre pour quelqu'un d'autre. Un chiffre isolé ne dit presque rien ; son écart à ta propre normale dit beaucoup. La durée de ton sommeil, elle, a sa propre référence : <a href="/methode/besoin-de-sommeil.html">ton besoin de sommeil</a>, calculé à partir de ton âge et de tes cycles.</p>

<h2>Pourquoi te comparer à toi-même</h2>
<p>Parce que l'écart entre deux personnes est bien plus grand que les variations d'une même personne d'un jour à l'autre. L'âge, la génétique et la condition physique fixent le niveau de tes signaux. La <a href="/methode/variabilite-cardiaque.html">variabilité cardiaque</a> en est l'exemple parfait : ses valeurs normales s'étalent sur une plage très large d'un adulte à l'autre.</p>
<p>Comparer ta HRV à une moyenne de population, c'est surtout mesurer qui tu es. La comparer à ta ligne de base, c'est mesurer <strong>ce qui a changé cette nuit</strong>, et c'est exactement ce qui renseigne sur <a href="/articles/comment-savoir-si-on-est-bien-recupere.html">ta récupération</a>. C'est aussi l'approche défendue par la recherche sur le suivi des athlètes : raisonner par rapport à ses propres valeurs, et en tendance.</p>

<h2>Comment l'app la calcule</h2>
<p>Pour chaque signal, Ecleptic prend <strong>les 42 derniers jours</strong>, soit environ six semaines, et en tire deux chiffres : ta moyenne, et ton écart-type, c'est-à-dire l'amplitude habituelle de tes variations autour de cette moyenne.</p>
<div class="figs">
  <div><span class="v">42</span><span class="u">Jours de fenêtre glissante</span></div>
  <div><span class="v">7</span><span class="u">Jours pour qu'elle existe</span></div>
  <div><span class="v">28</span><span class="u">Jours pour une confiance pleine</span></div>
  <div><span class="v">5</span><span class="u">Vitaux jugés contre ta normale</span></div>
</div>
<ul>
<li><strong>Pourquoi 42 jours :</strong> assez long pour que ta ligne de base soit stable, assez court pour suivre un vrai changement de forme sans trop de retard.</li>
<li><strong>Pourquoi le jour évalué est exclu :</strong> la valeur du matin est comparée à ton passé, jamais à elle-même. Sinon, une nuit extrême tirerait sa propre référence vers elle et paraîtrait moins inhabituelle qu'elle ne l'est.</li>
<li><strong>Pourquoi une fenêtre glissante :</strong> chaque jour, la journée la plus ancienne sort du calcul et la plus récente y entre. Ta ligne de base avance avec toi.</li>
</ul>

<h2>Le z-score, ou l'écart en clair</h2>
<p>La valeur du jour est ensuite exprimée en <strong>z-score</strong> : de combien d'écarts-types elle s'écarte de ta moyenne. Zéro, c'est pile ta normale. Exemple : si ta HRV tourne autour de 50 ms avec un écart-type de 5 ms, une nuit à 40 ms donne un z-score de −2, soit deux écarts-types sous ta normale.</p>
<p>Ce z-score est converti en points selon le sens de chaque signal :</p>
<ul>
<li><strong>HRV et saturation en oxygène :</strong> au-dessus de ta normale, c'est mieux.</li>
<li><strong>Fréquence cardiaque au repos et fréquence respiratoire :</strong> en dessous, c'est mieux. Une <a href="/methode/frequence-cardiaque-repos.html">fréquence cardiaque au repos</a> qui grimpe au-dessus de tes habitudes accompagne souvent la fatigue, le stress ou une infection qui démarre.</li>
<li><strong>Température du poignet :</strong> il n'y a pas de bon côté. Tout écart pénalise, dans un sens comme dans l'autre.</li>
</ul>
<p>À deux écarts-types du mauvais côté, le signal ne rapporte plus aucun point. Les cinq signaux sont ensuite pondérés dans le pilier des vitaux, qui pèse 42 points sur 100 dans le <a href="/methode/readiness-score.html">Readiness Score</a>.</p>

<h2>7 jours pour exister, 28 pour être fiable</h2>
<p>Une ligne de base ne se devine pas : il faut <strong>au moins 7 jours de données</strong> pour qu'elle existe. Avant, le signal n'est pas noté : il est retiré du calcul et son poids redistribué, comme n'importe quelle donnée absente. Les tout premiers jours avec une montre, ton score repose donc sur ton sommeil, ta nutrition et ton rythme.</p>
<p>Ensuite, la confiance monte jour après jour jusqu'à devenir <strong>pleine à 28 jours</strong>. Un indice de confiance accompagne le score : un chiffre construit sur dix jours d'historique ne se lit pas comme un chiffre construit sur six semaines.</p>

<h2>Ce qui déplace ta ligne de base</h2>
<p>Ta normale n'est pas figée, et c'est voulu. Plusieurs choses peuvent la faire glisser :</p>
<ul>
<li><strong>Un bloc d'entraînement :</strong> quelques semaines de charge en hausse, puis l'adaptation qui suit.</li>
<li><strong>Une période de stress :</strong> travail, examens, déménagement, nuits hachées.</li>
<li><strong>Une maladie :</strong> une infection peut décaler plusieurs signaux à la fois, parfois pendant des jours.</li>
<li><strong>Un changement de montre :</strong> un autre capteur, un autre algorithme, et parfois un autre niveau de départ.</li>
</ul>
<p>Grâce à la fenêtre glissante, ta ligne de base suit ces changements en quelques semaines. Pendant la transition, lis tes écarts avec un peu plus de recul.</p>

<h2>Les limites de la méthode</h2>
<ul>
<li><strong>Une nuit n'est pas un signal :</strong> une HRV qui chute une nuit, c'est souvent passager : un verre d'alcool, un dîner tardif, une mesure moins propre. Plusieurs jours d'affilée sous ta ligne de base, c'est un signal. Lis la tendance, pas la nuit.</li>
<li><strong>Normal ne veut pas dire sain :</strong> ta ligne de base dit si tu t'écartes de tes habitudes, pas si tes habitudes sont bonnes.</li>
<li><strong>Une dérive lente passe inaperçue :</strong> si une valeur glisse doucement pendant des semaines, la fenêtre glissante l'absorbe. L'écart du jour paraît banal, alors que ta normale, elle, a bougé.</li>
</ul>

<h2>Quand consulter</h2>
<p>Ecleptic est un outil de bien-être, pas un dispositif médical : ta ligne de base ne pose aucun diagnostic. Si une valeur anormale persiste, même si ta ligne de base finit par l'absorber, ou si tu ressens un malaise, une douleur thoracique, un essoufflement anormal ou des palpitations, consulte un médecin. En cas d'urgence, appelle le 15 ou le 112.</p>
""",
    "refs": [
        "Plews D. J. et al. (2013), suivi de la variabilité cardiaque et adaptation à l'entraînement chez l'athlète d'endurance, <em>Sports Medicine</em>.",
        "Buchheit M. (2014), suivi de l'état d'entraînement par les mesures de fréquence cardiaque, <em>Frontiers in Physiology</em>.",
        "Shaffer F. et Ginsberg J. P. (2017), panorama des indicateurs et des normes de variabilité cardiaque, <em>Frontiers in Public Health</em>.",
    ],
    "faq": [
        {"q": "Qu'est-ce qu'une ligne de base en HRV ?",
         "a": "C'est ta valeur habituelle de variabilité cardiaque, avec l'amplitude normale de ses variations, calculée sur tes dernières semaines. Dans Ecleptic, elle couvre les 42 derniers jours, sans compter le jour évalué, et sert de référence pour juger chaque nuit."},
        {"q": "Combien de temps faut-il pour établir sa ligne de base HRV ?",
         "a": "Dans Ecleptic, il faut au moins 7 jours de données pour qu'une ligne de base existe, et la confiance devient pleine à 28 jours. En attendant, le signal est laissé de côté et son poids redistribué entre les autres."},
        {"q": "Est-ce grave d'avoir une HRV plus basse que la moyenne ?",
         "a": "Pas forcément : la variabilité cardiaque varie énormément d'une personne à l'autre selon l'âge, la génétique et la condition physique. Ce qui renseigne sur ta récupération, c'est l'écart à ta propre normale, surtout s'il dure plusieurs jours. Une valeur durablement inhabituelle ou des symptômes justifient un avis médical."},
    ],
    "related": ["readiness-score", "vitaux", "variabilite-cardiaque", "frequence-cardiaque-repos", "besoin-de-sommeil"],
    "journal": ["hrv-variabilite-frequence-cardiaque", "readiness-score-comment-ca-marche", "comment-savoir-si-on-est-bien-recupere", "frequence-cardiaque-repos-normale"],
}
