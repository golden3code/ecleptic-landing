# -*- coding: utf-8 -*-
"""La méthode · Moteur IV — les vitaux de la nuit.

Chargé par tools/build_articles.py (_load_methode) → /methode/vitaux.html.
Faits vérifiés dans le code de l'app (lib/readiness/physio.ts, baseline.ts,
score.ts) le 24/09/2026 : cinq signaux lus dans Apple Santé, poids internes
45/30/12/7/6 du pilier vitaux (42 points), ligne de base 42 j (jour exclu,
min 7, confiance pleine 28), sens de chaque signal, 0 point au-delà de
2 écarts-types, signal absent retiré et poids réparti, pilier retiré sans
montre ; HRV et FC repos = modificateurs de l'âge biologique (chiffres non publiés).
"""

PAGE = {
    "slug": "vitaux",
    "kind": "moteur",
    "num": "IV",
    "order": 4,
    "label": "Les vitaux",
    "title": "Les vitaux de la nuit, signal par signal",
    "seo_title": "Vitaux de la nuit (HRV, FC repos) : comment l'app les lit — Ecleptic",
    "description": "Les vitaux de la nuit pèsent 42 points du Readiness Score : HRV, FC au repos, respiration, SpO₂, température. Comment l'app les compare à ta normale.",
    "date": "2026-09-24",
    "lead": "La nuit, ton corps parle sans filtre : pas de café, pas de réunion, pas d'effort pour brouiller le message. Voici comment l'app lit tes <strong>cinq signaux vitaux</strong>, chacun face à ta propre normale, et pourquoi une seule mauvaise nuit ne suffit jamais à conclure.",
    "body": """
<h2>Ce que le moteur calcule</h2>
<p>Le moteur des vitaux transforme cinq mesures brutes de ta montre en un seul sous-score : le pilier vitaux du <a href="/methode/readiness-score.html">Readiness Score</a>, le plus lourd des quatre avec <strong>42 points sur 100</strong>. Il ne juge pas ta santé. Il mesure une seule chose : <strong>de combien ta nuit s'écarte de ta normale</strong>, et dans quel sens.</p>
<p>Pourquoi lui donner autant de poids ? Parce que ces signaux ne dépendent ni de ce que tu déclares, ni de ce que tu ressens. Ils sont le reflet le plus direct et le plus objectif de ta récupération, à commencer par l'état de ton système nerveux autonome, celui qui décide sans te demander ton avis si ton corps est en mode récupération ou en mode alerte.</p>

<h2>Cinq signaux, lus dans Apple Santé</h2>
<p>L'app lit dans Apple Santé cinq signaux relevés par ta montre, au repos et pour l'essentiel pendant ton sommeil. Chacun a son poids à l'intérieur du pilier :</p>
<div class="figs">
  <div><span class="v">45 %</span><span class="u">Variabilité cardiaque</span></div>
  <div><span class="v">30 %</span><span class="u">FC au repos</span></div>
  <div><span class="v">12 %</span><span class="u">Respiration</span></div>
  <div><span class="v">7 %</span><span class="u">SpO₂</span></div>
  <div><span class="v">6 %</span><span class="u">Température</span></div>
</div>
<ul>
<li><strong>La <a href="/methode/variabilite-cardiaque.html">variabilité cardiaque (HRV)</a> :</strong> la variation du temps entre deux battements, en millisecondes, au format SDNN. Plus haute que ta normale, c'est mieux.</li>
<li><strong>La <a href="/methode/frequence-cardiaque-repos.html">fréquence cardiaque au repos</a> :</strong> en battements par minute. Plus basse que ta normale, c'est mieux.</li>
<li><strong>La <a href="/methode/frequence-respiratoire.html">fréquence respiratoire</a> :</strong> tes respirations par minute. Plus basse, c'est mieux ; une hausse inhabituelle accompagne souvent une fatigue ou une infection qui démarre.</li>
<li><strong>La <a href="/methode/saturation-oxygene.html">saturation en oxygène (SpO₂)</a> :</strong> la part de ton hémoglobine chargée en oxygène. Plus haute, c'est mieux.</li>
<li><strong>La <a href="/methode/temperature-poignet.html">température du poignet</a> :</strong> mesurée pendant ton sommeil. Ici, tout écart pénalise, dans un sens comme dans l'autre.</li>
</ul>
<p>À elles deux, HRV et fréquence cardiaque au repos font <strong>les trois quarts du pilier</strong>. Quand toutes les données sont là, la HRV pèse à elle seule près de 19 points sur les 100 du score : aucun autre signal ne pèse autant.</p>

<h2>Pourquoi la nuit</h2>
<p>La nuit est <strong>le seul moment où les conditions sont comparables d'un jour à l'autre</strong>. Tu es allongé, au repos, loin du café, du stress et de l'effort. Une HRV relevée à 15 heures, après deux cafés et une réunion tendue, raconte ton après-midi, pas ta récupération.</p>
<p>La nuit, le décor se répète : même position, même calme, même montre au même poignet. C'est cette répétition qui rend la comparaison honnête. Sans elle, tu compares des journées différentes, pas l'état de ton corps.</p>

<h2>La méthode, pas à pas</h2>
<ul>
<li><strong>1. Ta ligne de base :</strong> pour chaque signal, l'app calcule ta moyenne et ton écart-type sur les <strong>42 derniers jours</strong>, sans compter le jour évalué. Il faut au moins 7 jours de données pour qu'elle existe, et 28 pour que la confiance soit pleine. Tout le détail : <a href="/methode/ligne-de-base.html">ta ligne de base</a>.</li>
<li><strong>2. L'écart à ta normale :</strong> la valeur de la nuit est traduite en nombre d'écarts-types au-dessus ou au-dessous de ta moyenne. Si ta HRV tourne autour de 50 ms et varie d'habitude de 5 ms, une nuit à 45 ms se situe à un écart-type sous ta normale ; à 40 ms, à deux.</li>
<li><strong>3. Des points, dans le bon sens :</strong> cet écart devient des points selon le sens du signal. HRV et SpO₂ : plus haut, mieux c'est. FC au repos et respiration : plus bas, mieux c'est. Température : tout écart pénalise. Au-delà de deux écarts-types du mauvais côté, le signal ne rapporte plus aucun point.</li>
<li><strong>4. La pondération :</strong> les cinq sous-scores sont combinés selon leurs poids. Si ta montre n'a pas relevé un signal cette nuit-là, ou s'il n'a pas encore 7 jours d'historique, il est retiré et son poids est réparti entre les autres. Rien n'est inventé pour combler le trou.</li>
</ul>

<h2>Une nuit, c'est du bruit ; une semaine, c'est un signal</h2>
<p>Tes vitaux bougent naturellement d'une nuit à l'autre. Une nuit courte, un verre de trop, une journée tendue : ta HRV peut plonger sans que cela veuille dire grand-chose. <strong>Une HRV qui chute une nuit, c'est du bruit. Une semaine sous ta ligne de base, c'est un signal.</strong></p>
<p>La méthode fait déjà une partie du tri. Comme chaque écart est rapporté à ta propre variabilité habituelle, quelqu'un dont la HRV oscille beaucoup doit s'écarter davantage pour perdre des points que quelqu'un de très régulier. Mais une nuit basse fait bel et bien baisser le score du jour : à toi de ne pas en tirer de conclusion hâtive.</p>
<p>Le vrai signal, c'est la <strong>répétition</strong> : plusieurs jours sous ta normale, surtout quand la fréquence cardiaque au repos monte en même temps. C'est le motif d'une fatigue qui s'accumule, d'une charge d'entraînement trop brutale ou d'une infection qui démarre. Voilà pourquoi l'app te montre aussi la tendance de ton score et de chaque pilier sur plusieurs semaines.</p>

<h2>Pourquoi ces choix</h2>
<ul>
<li><strong>Toi contre toi :</strong> la HRV va de 20 à plus de 100 ms selon l'âge, la génétique et la condition physique. La juger sur une norme de population condamnerait certains à paraître fatigués toute leur vie. Seul l'écart à ta propre normale a un sens.</li>
<li><strong>Le même appareil :</strong> Apple Santé enregistre la HRV au format SDNN, celui de l'Apple Watch, alors que beaucoup d'études et d'autres appareils utilisent le RMSSD. Les deux ne se comparent pas directement. Te comparer à toi-même, sur la même montre, règle le problème.</li>
<li><strong>42 jours :</strong> assez long pour que ta normale soit stable, assez court pour suivre un vrai changement de forme. Le jour évalué est exclu du calcul, pour qu'une valeur extrême ne dilue pas sa propre référence.</li>
<li><strong>Des poids inégaux :</strong> HRV et FC au repos sont les fenêtres les plus directes sur ton système nerveux autonome, d'où leurs trois quarts du pilier. Respiration, SpO₂ et température pèsent moins, mais captent autre chose : une infection qui démarre fait souvent grimper la respiration et la température.</li>
</ul>

<h2>Au-delà du score, ton âge biologique</h2>
<p>Deux de ces signaux servent aussi ailleurs. Dans le calcul de ton <a href="/methode/age-biologique.html">âge biologique</a>, la HRV joue le rôle de modificateur : comparée aux valeurs attendues pour ton âge, elle peut le faire bouger dans un sens ou dans l'autre. Elle y compte moins si tu prends un traitement qui ralentit le cœur.</p>
<p>La FC au repos fait de même, face à une valeur de référence, sauf quand elle entre déjà dans l'équation de ta VO₂max. Elle n'est jamais comptée deux fois.</p>

<h2>Sans montre, et les limites de la mesure</h2>
<p><strong>Sans montre, pas de vitaux.</strong> Le pilier est alors retiré et son poids redistribué entre le sommeil, la nutrition et le rythme. Un indice de confiance te l'indique : un score privé de ses vitaux ne se lit pas comme un score complet.</p>
<p>Avec une montre, garde en tête comment elle mesure. Son capteur optique, la photopléthysmographie, suit ton pouls à travers la peau du poignet : c'est moins précis qu'un électrocardiogramme, mais <strong>fiable en tendance quand la montre est bien portée</strong>, ajustée et gardée toute la nuit.</p>
<p>Enfin, ce moteur est un outil de bien-être, pas un dispositif médical : il ne pose aucun diagnostic. Un signal sous ta normale t'invite à lever le pied, pas à t'alarmer. Si une valeur inhabituelle persiste, ou si tu ressens un malaise, une douleur thoracique, un essoufflement anormal ou des palpitations, consulte un médecin. En cas d'urgence, appelle le 15 ou le 112.</p>
""",
    "refs": [
        "Task Force de la Société européenne de cardiologie et de la NASPE (1996), normes de mesure de la variabilité cardiaque, <em>Circulation</em>.",
        "Plews D. J. et al. (2013), suivi de la variabilité cardiaque et adaptation à l'entraînement chez l'athlète d'endurance, <em>Sports Medicine</em>.",
        "Buchheit M. (2014), suivi de l'état d'entraînement par les mesures de fréquence cardiaque, <em>Frontiers in Physiology</em>.",
        "Miller D. J. et al. (2020), variations de la fréquence respiratoire nocturne et détection précoce d'une infection, <em>PLOS ONE</em>.",
        "OMS (2011), manuel de formation à l'oxymétrie de pouls.",
    ],
    "faq": [
        {"q": "Comment savoir si mes vitaux de la nuit sont normaux ?",
         "a": "Le plus fiable est de les comparer à ta propre moyenne des dernières semaines plutôt qu'à une norme générale : c'est ce que fait l'app, sur 42 jours, pour chacun des cinq signaux. Un écart d'une nuit relève souvent du bruit ; un écart qui persiste, ou qui s'accompagne de symptômes inhabituels, mérite l'avis d'un médecin."},
        {"q": "Quelle est la différence entre SDNN et RMSSD ?",
         "a": "Ce sont deux façons de calculer la variabilité cardiaque. Le SDNN, utilisé par Apple Santé et l'Apple Watch, est l'écart-type des intervalles entre battements ; le RMSSD, courant dans les études et sur d'autres appareils, se calcule sur les différences entre battements successifs. Les deux ne se comparent pas directement, d'où l'intérêt de te comparer à toi-même, sur le même appareil."},
        {"q": "Que se passe-t-il si ma montre n'a pas mesuré un signal cette nuit ?",
         "a": "Le signal manquant est retiré pour la nuit et son poids est réparti entre les autres vitaux : rien n'est inventé pour le remplacer. Sans aucun vital, par exemple sans montre, c'est tout le pilier qui est retiré et son poids passe au sommeil, à la nutrition et au rythme, avec un indice de confiance qui le signale."},
    ],
    "related": ["variabilite-cardiaque", "frequence-cardiaque-repos", "frequence-respiratoire", "saturation-oxygene", "temperature-poignet", "ligne-de-base"],
    "journal": ["hrv-variabilite-frequence-cardiaque", "comment-savoir-si-on-est-bien-recupere", "readiness-score-comment-ca-marche", "montre-connectee-fiabilite-sommeil"],
}
