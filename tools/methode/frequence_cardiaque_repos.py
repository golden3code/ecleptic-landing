# -*- coding: utf-8 -*-
"""La méthode · Fiche — la fréquence cardiaque au repos.

Chargé par tools/build_articles.py (_load_methode) → /methode/frequence-cardiaque-repos.html.
Faits vérifiés dans le code de l'app (lib/readiness/physio.ts, baseline.ts) le
24/09/2026 : FC repos lue dans Apple Santé (bpm), 30 % du pilier vitaux
(42 points), plus basse = mieux, ligne de base 42 j (jour exclu, min 7, confiance
pleine 28), 0 point au-delà de 2 écarts-types au-dessus de la normale ;
modificateur de l'âge biologique (référence ~60 ± 9 bpm, jusqu'à ±2 ans) quand
elle n'entre pas déjà dans l'équation de VO₂max.
"""

PAGE = {
    "slug": "frequence-cardiaque-repos",
    "kind": "fiche",
    "num": None,
    "order": 2,
    "label": "La fréquence cardiaque au repos",
    "title": "La fréquence cardiaque au repos, le ralenti de ton moteur",
    "seo_title": "Fréquence cardiaque au repos : normale, élevée, basse — Ecleptic",
    "description": "Fréquence cardiaque au repos : ce qu'elle reflète, les valeurs normales, ce qui la fait monter, quand consulter, et comment l'app la compare à ta normale.",
    "date": "2026-09-24",
    "lead": "Le nombre de battements dont ton cœur a besoin quand tu ne fais rien, c'est <strong>le ralenti de ton moteur</strong>. Quelques battements de plus plusieurs matins de suite, et ton corps te dit déjà quelque chose, souvent avant que tu ne le sentes.",
    "body": """
<h2>La définition, en une phrase</h2>
<p>La fréquence cardiaque au repos, c'est <strong>le nombre de battements de ton cœur par minute quand tu es complètement au repos</strong> : éveillé mais calme et immobile, ou endormi. Elle s'exprime en battements par minute, les bpm.</p>
<p>C'est l'un des chiffres les plus simples de la physiologie, et l'un des plus parlants, à condition de le mesurer toujours dans les mêmes conditions.</p>

<h2>Ce qu'elle reflète</h2>
<p>Elle raconte deux histoires à la fois.</p>
<ul>
<li><strong>Ta forme, sur des mois :</strong> un cœur entraîné éjecte plus de sang à chaque contraction. Il a donc besoin de battre moins souvent pour assurer le même débit. C'est pour ça que l'endurance fait baisser la fréquence au repos, lentement, au fil des semaines.</li>
<li><strong>Ton état, au jour le jour :</strong> au repos, le système nerveux parasympathique freine le cœur. Quand la fatigue ou le stress relâchent ce frein, ou quand ton corps lutte contre une infection ou manque d'eau, la fréquence remonte de quelques battements.</li>
</ul>
<p>C'est ce double visage qui la rend précieuse. C'est aussi pourquoi elle se lit avec la <a href="/methode/variabilite-cardiaque.html">variabilité cardiaque</a> : les deux reflètent le même équilibre nerveux, vu sous deux angles.</p>

<h2>Comment on la mesure</h2>
<p>Chez le médecin, on la relève au calme, après quelques minutes de repos, en prenant le pouls ou par électrocardiogramme. Chez toi, le plus simple est de compter ton pouls <strong>au réveil, avant de te lever</strong>.</p>
<p>Ta montre, elle, la suit avec son capteur optique au poignet, la photopléthysmographie. C'est moins précis qu'un électrocardiogramme, mais fiable en tendance quand la montre est bien portée. Le bon moment reste le même : <strong>au réveil ou pendant le sommeil</strong>, quand les conditions se répètent d'un jour à l'autre. Une mesure prise juste après un escalier ou une discussion animée ne se compare à rien.</p>

<h2>Les valeurs de repère</h2>
<p>Chez l'adulte, la fréquence cardiaque au repos se situe en général <strong>entre 60 et 100 bpm</strong>. Chez les sportifs d'endurance, elle descend souvent <strong>entre 40 et 60</strong>. La condition physique, la génétique, le sexe, la chaleur ou certains traitements la font varier d'une personne à l'autre.</p>
<p>Sur le long terme, de grandes études associent une fréquence de repos basse à une meilleure condition physique, et une fréquence durablement élevée à un risque cardiovasculaire plus important. Mais au quotidien, le chiffre absolu compte moins que <strong>son écart à ta propre normale</strong> : 58 bpm peut être parfait pour ton voisin et, pour toi qui tournes d'habitude à 50, le signe d'une nuit difficile. Tout ce qui fait une <a href="/articles/frequence-cardiaque-repos-normale.html">fréquence cardiaque au repos normale</a> tient dans cet écart.</p>

<h2>Ce qui la fait monter</h2>
<p>Un battement de plus un matin ne veut rien dire. <strong>Plusieurs battements de plus, plusieurs jours de suite</strong>, si. Les causes les plus fréquentes :</p>
<ul>
<li><strong>La fatigue :</strong> une charge d'entraînement qui s'accumule plus vite que tu ne récupères.</li>
<li><strong>L'alcool :</strong> il accélère le cœur pendant la nuit qui suit.</li>
<li><strong>Le stress :</strong> une période tendue garde ton système nerveux en alerte, même au repos.</li>
<li><strong>La déshydratation :</strong> moins de volume sanguin, donc plus de battements pour le même débit.</li>
<li><strong>Une infection qui démarre :</strong> ton corps mobilise ses défenses et le cœur accélère, parfois avant que tu ne te sentes malade.</li>
</ul>
<p>Si ta fréquence reste <a href="/articles/frequence-cardiaque-repos-elevee.html">élevée plusieurs jours de suite</a>, commence par passer ces causes en revue avant de pousser l'entraînement.</p>

<h2>Comment Ecleptic la lit</h2>
<p>Dans l'app, la fréquence cardiaque au repos est le deuxième signal du pilier vitaux du <a href="/methode/readiness-score.html">Readiness Score</a> : <strong>30 % de ses 42 points</strong>, soit près de 13 points sur 100 quand toutes les données sont là. Avec la HRV, elle fait les trois quarts du pilier.</p>
<div class="figs">
  <div><span class="v">30 %</span><span class="u">du pilier vitaux</span></div>
  <div><span class="v">≈ 13</span><span class="u">points du score sur 100</span></div>
  <div><span class="v">42 j</span><span class="u">de ligne de base</span></div>
  <div><span class="v">± 2 ans</span><span class="u">d'âge biologique, au plus</span></div>
</div>
<p>L'app la lit dans Apple Santé, en bpm, puis la compare à ta <a href="/methode/ligne-de-base.html">ligne de base</a> : ta moyenne et ton écart-type des 42 derniers jours, jour évalué exclu, avec 7 jours minimum pour démarrer et 28 pour une confiance pleine. <strong>Plus elle est basse par rapport à ta normale, mieux c'est</strong> ; au-delà de deux écarts-types au-dessus, elle ne rapporte plus aucun point. Le détail des cinq signaux est sur la page <a href="/methode/vitaux.html">Les vitaux</a>.</p>
<p>Elle compte aussi dans ton <a href="/methode/age-biologique.html">âge biologique</a>, face à une référence d'environ 60 ± 9 bpm, avec un effet de 2 ans au plus dans un sens ou dans l'autre. Sauf quand elle entre déjà dans l'estimation de ta <a href="/methode/vo2max.html">VO₂max</a>, dont elle est l'une des données dans certains modèles sans test d'effort : elle n'est jamais comptée deux fois.</p>

<h2>Les limites de la mesure</h2>
<ul>
<li><strong>Le capteur optique :</strong> une montre trop lâche ou mal placée dégrade la mesure. Bien portée, elle est fiable en tendance.</li>
<li><strong>Les traitements :</strong> un traitement qui ralentit le cœur, comme un bêtabloquant, change la lecture. Ta fréquence au repos ne reflète alors plus seulement ta forme ou ta fatigue.</li>
<li><strong>Le contexte :</strong> une nuit très chaude, un dîner copieux et tardif ou un verre d'alcool peuvent la faire monter sans que ta forme ait changé.</li>
</ul>

<h2>Quand consulter</h2>
<p>Ecleptic n'est pas un dispositif médical et ne pose aucun diagnostic. Certains repères méritent pourtant un avis médical :</p>
<ul>
<li><strong>Au-dessus de 100 bpm :</strong> une fréquence au repos qui y reste, jour après jour, sans explication.</li>
<li><strong>Sous 40 bpm avec des symptômes :</strong> malaises, vertiges ou essoufflement. Sans aucun symptôme, chez un sportif d'endurance, une fréquence basse est souvent le simple reflet de l'entraînement.</li>
<li><strong>Une hausse qui s'installe :</strong> plusieurs jours au-dessus de ta normale malgré le repos, avec une fatigue qui ne passe pas.</li>
</ul>
<p>Si tu ressens des palpitations, une douleur thoracique, un malaise ou un essoufflement anormal, consulte un médecin. En cas d'urgence, appelle le 15 ou le 112.</p>
""",
    "refs": [
        "Fox K. et al. (2007), la fréquence cardiaque de repos dans les maladies cardiovasculaires, <em>Journal of the American College of Cardiology</em>.",
        "Jensen M. T. et al. (2013), fréquence cardiaque de repos, condition physique et mortalité (Copenhagen Male Study), <em>Heart</em>.",
        "Buchheit M. (2014), suivi de l'état d'entraînement par les mesures de fréquence cardiaque, <em>Frontiers in Physiology</em>.",
        "Nes B. M. et al. (2011), estimation de la VO₂pic sans test d'effort : l'étude HUNT, <em>Medicine &amp; Science in Sports &amp; Exercise</em>.",
    ],
    "faq": [
        {"q": "Quelle est une fréquence cardiaque au repos normale ?",
         "a": "Chez l'adulte, elle se situe en général entre 60 et 100 battements par minute, et souvent entre 40 et 60 chez les sportifs d'endurance. Au quotidien, l'écart à ta propre normale en dit plus que le chiffre absolu."},
        {"q": "Pourquoi ma fréquence cardiaque au repos augmente-t-elle ?",
         "a": "Une hausse de plusieurs battements plusieurs jours de suite vient le plus souvent de la fatigue, de l'alcool, du stress, d'un manque d'hydratation ou d'une infection qui démarre. Si elle reste au-dessus de 100 bpm au repos, ou s'accompagne de symptômes inhabituels, consulte un médecin."},
        {"q": "Une fréquence cardiaque au repos de 45, est-ce dangereux ?",
         "a": "Chez un sportif d'endurance sans aucun symptôme, une fréquence aussi basse est souvent le simple reflet de l'entraînement. En revanche, une fréquence sous 40 accompagnée de malaises, de vertiges ou d'essoufflement mérite un avis médical. Et si tu prends un traitement qui ralentit le cœur, ta fréquence basse ne reflète plus seulement ta forme."},
    ],
    "related": ["vitaux", "variabilite-cardiaque", "ligne-de-base", "readiness-score", "age-biologique"],
    "journal": ["frequence-cardiaque-repos-normale", "frequence-cardiaque-repos-elevee", "comment-savoir-si-on-est-bien-recupere"],
}
