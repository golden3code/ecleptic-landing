# -*- coding: utf-8 -*-
"""La méthode · Fiche — la saturation en oxygène, SpO₂ (pilier vitaux du Readiness Score).

Chargé par tools/build_articles.py (_load_methode) → /methode/saturation-oxygene.html.
Faits vérifiés dans le code de l'app (lib/readiness/physio.ts, baseline.ts) le 24/09/2026 :
poids interne 7 % du pilier vitaux (42 pts), sens « plus haute que ta normale = mieux »,
ligne de base 42 j jour exclu (min 7, confiance pleine 28), 0 point à 2 écarts-types
sous la normale, signal absent → poids redistribué. Poids faible = choix (signal bruité).
"""

PAGE = {
    "slug": "saturation-oxygene",
    "kind": "fiche",
    "num": None,
    "order": 5,
    "label": "La saturation en oxygène (SpO₂)",
    "title": "La saturation en oxygène, mesurée au poignet",
    "seo_title": "Saturation en oxygène (SpO₂) normale : repères et limites — Ecleptic",
    "description": "La saturation en oxygène (SpO₂) est en général de 95 à 100 % chez l'adulte sain. Ce qu'elle mesure, les limites de la montre et comment Ecleptic la lit.",
    "date": "2026-09-24",
    "lead": "Chaque nuit, ta montre estime à quel point ton sang est chargé en oxygène. <strong>Un signal précieux quand il décroche, mais bruité au poignet</strong> : voici comment le lire, et pourquoi Ecleptic ne lui donne qu'un petit poids.",
    "body": """
<h2>Ce que mesure la SpO₂</h2>
<p>La saturation en oxygène, c'est <strong>la part de ton hémoglobine qui est chargée en oxygène</strong>. L'hémoglobine, c'est la protéine de tes globules rouges qui transporte l'oxygène de tes poumons jusqu'à tes tissus ; la saturation dit, en pourcentage, à quel point elle fait le plein.</p>
<p>Le « p » de SpO₂ signale une mesure par oxymétrie de pouls, à travers la peau ; quand on la mesure directement dans le sang d'une artère, on parle de SaO₂. Dans Ecleptic, la SpO₂ est l'un des cinq signaux du pilier « vitaux » du <a href="/methode/readiness-score.html">Readiness Score</a>.</p>

<h2>Ce qu'elle reflète dans ton corps</h2>
<p>À chaque passage dans tes poumons, ton sang se recharge en oxygène. La SpO₂ dit si ce chargement est complet : elle dépend de ta respiration, de l'état de tes poumons et de l'air que tu respires. Chez une personne en bonne santé, l'hémoglobine est presque pleine en permanence, et la SpO₂ bouge très peu. C'est pour ça qu'une baisse nette a du sens.</p>
<p>Ne la confonds pas avec la <a href="/methode/vo2max.html">VO₂max</a>, qui mesure la quantité d'oxygène que ton corps sait utiliser à l'effort. Tu peux avoir une saturation parfaite et une VO₂max modeste.</p>

<h2>De la prise de sang au poignet</h2>
<p>La référence, c'est la gazométrie artérielle : une prise de sang dans une artère, analysée en laboratoire. Au quotidien, les soignants utilisent un oxymètre de pouls, la petite pince posée au bout du doigt. Elle fait traverser ton doigt par une lumière rouge et une lumière infrarouge ; l'hémoglobine chargée en oxygène et celle qui ne l'est pas ne les absorbent pas de la même façon, et l'appareil en déduit ta saturation, battement après battement.</p>
<p>Ta montre applique le même principe, mais au poignet, et sans traverser : son capteur lit la lumière renvoyée par tes tissus. Le signal est plus faible, et plus sensible aux mouvements, à la peau et au serrage du bracelet. Résultat : <strong>une mesure moins précise qu'un oxymètre de doigt médical</strong>, qui donne le meilleur d'elle-même quand tu es immobile, c'est-à-dire pendant ton sommeil. Ecleptic lit ensuite ces valeurs dans Apple Santé.</p>

<h2>Les repères chez l'adulte</h2>
<p>Chez l'adulte en bonne santé, la SpO₂ se situe <strong>en général entre 95 et 100 %</strong>. Pendant le sommeil, elle baisse légèrement, parce que tu respires un peu moins profondément : c'est normal.</p>
<div class="figs">
  <div><span class="v">95–100</span><span class="u">% chez l'adulte sain</span></div>
  <div><span class="v">7 %</span><span class="u">Du pilier vitaux</span></div>
  <div><span class="v">42</span><span class="u">Jours de ligne de base</span></div>
  <div><span class="v">28</span><span class="u">Jours pour une confiance pleine</span></div>
</div>
<p>Deux personnes en bonne santé n'ont pas forcément la même valeur habituelle : l'état des poumons et l'altitude où l'on vit comptent, et, pour la mesure au poignet, la peau et la façon dont la montre y repose. C'est pour ça qu'Ecleptic ne te juge pas sur un seuil commun, mais sur <strong>l'écart à ta propre normale</strong>.</p>

<h2>Ce qui la fait baisser</h2>
<ul>
<li><strong>L'altitude :</strong> chaque inspiration y apporte moins d'oxygène, et ta saturation descend. Ton corps compense en respirant davantage, ce qui fait monter ta <a href="/methode/frequence-respiratoire.html">fréquence respiratoire</a>. Le détail : <a href="/articles/sport-en-altitude-effets.html">le sport en altitude</a>.</li>
<li><strong>Les pauses respiratoires pendant le sommeil :</strong> chaque pause fait chuter la saturation, qui remonte quand le souffle reprend. Répétées nuit après nuit, elles peuvent évoquer une apnée du sommeil.</li>
<li><strong>Une infection ou une maladie respiratoire :</strong> quand les poumons échangent moins bien, la saturation baisse.</li>
<li><strong>La mesure elle-même :</strong> un bras qui bouge, un bracelet desserré, un poignet froid ou un tatouage peuvent produire des valeurs aberrantes.</li>
</ul>

<h2>Comment Ecleptic l'utilise</h2>
<p>Ecleptic récupère dans Apple Santé la saturation mesurée par ta montre pendant ton sommeil, et la compare à <a href="/methode/ligne-de-base.html">ta ligne de base</a> : ta moyenne et ton écart-type sur les 42 derniers jours, sans compter le jour évalué. Il faut au moins 7 jours de données pour que le signal compte, et 28 jours pour que sa confiance soit pleine.</p>
<ul>
<li><strong>Le sens :</strong> plus ta SpO₂ est haute par rapport à ta normale, mieux c'est. Une baisse te coûte des points.</li>
<li><strong>Le seuil :</strong> à 2 écarts-types sous ta normale, ce signal ne rapporte plus aucun point.</li>
<li><strong>Le poids :</strong> 7 % du pilier <a href="/methode/vitaux.html">vitaux</a>, qui vaut 42 points sur 100. Une journée où toutes les données sont là, la SpO₂ pèse donc environ 3 points du score.</li>
</ul>
<p>Ce petit poids est un choix. La SpO₂ est un signal utile en alerte, mais plus bruité et moins directement lié à ta récupération que la variabilité cardiaque et la fréquence cardiaque au repos, qui pèsent à elles deux 75 % du pilier. Même logique pour la <a href="/methode/temperature-poignet.html">température du poignet</a>, à 6 %. Si ta montre n'a pas relevé ta saturation, son poids est réparti entre les autres vitaux ; sans montre, c'est tout le pilier qui est redistribué.</p>

<h2>Les limites de la mesure au poignet</h2>
<ul>
<li><strong>Ce n'est pas un outil médical :</strong> la mesure de saturation de ta montre sert au suivi du bien-être, pas au diagnostic, et Ecleptic n'est pas un dispositif médical.</li>
<li><strong>Une valeur isolée ne veut pas dire grand-chose :</strong> c'est la répétition sur plusieurs nuits qui compte.</li>
<li><strong>Le score constate, il n'explique pas :</strong> Ecleptic voit que ta saturation s'écarte de ta normale, pas pourquoi. Nuit en altitude, rhume ou bracelet desserré : c'est toi qui as le contexte.</li>
</ul>

<h2>Quand consulter</h2>
<p>Parle à un médecin si ta SpO₂ est régulièrement basse, si ton entourage remarque des pauses dans ta respiration, ou si tu ronfles fort et te réveilles fatigué malgré des nuits complètes : ces signes peuvent faire suspecter une apnée du sommeil, qui se prend en charge. Seul un examen du sommeil, prescrit par un médecin, permet de trancher.</p>
<p>Un essoufflement inhabituel, des lèvres ou des ongles bleutés, une douleur dans la poitrine ou un malaise : c'est une urgence, appelle le 15 ou le 112. Et ne compte jamais sur une montre pour te rassurer quand tu te sens mal.</p>
""",
    "refs": [
        "OMS (2011), manuel de formation à l'oxymétrie de pouls.",
        "Buchheit M. (2014), suivi de l'état d'entraînement par les mesures de fréquence cardiaque, <em>Frontiers in Physiology</em>.",
    ],
    "faq": [
        {"q": "Quel taux de saturation en oxygène est normal ?",
         "a": "Chez l'adulte en bonne santé, la saturation en oxygène (SpO₂) se situe en général entre 95 et 100 %, avec une légère baisse pendant le sommeil. Une valeur régulièrement plus basse, surtout avec des symptômes, mérite d'être discutée avec un médecin."},
        {"q": "La mesure d'oxygène d'une montre connectée est-elle fiable ?",
         "a": "La montre utilise le même principe qu'un oxymètre, mais au poignet, avec un signal plus faible : elle est moins précise qu'un oxymètre de doigt médical et sensible aux mouvements, au serrage du bracelet et à la peau. Elle sert à suivre une tendance, jamais à poser un diagnostic."},
        {"q": "Pourquoi ma saturation en oxygène baisse-t-elle la nuit ?",
         "a": "Pendant le sommeil, tu respires un peu moins profondément, donc une légère baisse est normale. L'altitude, une infection respiratoire ou des pauses respiratoires peuvent la faire baisser davantage ; des baisses répétées avec ronflements et fatigue au réveil justifient d'en parler à un médecin."},
    ],
    "related": ["vitaux", "readiness-score", "ligne-de-base", "frequence-respiratoire", "temperature-poignet"],
    "journal": ["montre-connectee-fiabilite-sommeil", "sport-en-altitude-effets", "comment-savoir-si-on-est-bien-recupere"],
}
