# -*- coding: utf-8 -*-
"""La méthode · Fiche — la température du poignet (pilier vitaux du Readiness Score).

Chargé par tools/build_articles.py (_load_methode) → /methode/temperature-poignet.html.
Faits vérifiés dans le code de l'app (lib/readiness/physio.ts, baseline.ts) le 24/09/2026 :
poids interne 6 % du pilier vitaux (42 pts), score d'ÉCART (tout écart à la normale
pénalise, dans les deux sens ; 0 point au-delà de 2 écarts-types), ligne de base 42 j
jour exclu (min 7, confiance pleine 28), signal absent → poids redistribué.
Poids faible = choix (signal bruité, moins directement lié à la récupération).
"""

PAGE = {
    "slug": "temperature-poignet",
    "kind": "fiche",
    "num": None,
    "order": 6,
    "label": "La température du poignet",
    "title": "La température du poignet, un écart plutôt qu'un chiffre",
    "seo_title": "Température du poignet la nuit : que signifie l'écart ? — Ecleptic",
    "description": "La température du poignet mesurée la nuit est un écart à ta propre normale, pas une fièvre. Ce qui la fait varier, et comment Ecleptic l'intègre à ton score.",
    "date": "2026-09-24",
    "lead": "Ta montre ne prend pas ta température : elle suit, nuit après nuit, <strong>l'écart de ton poignet par rapport à ta propre normale</strong>. Un signal discret, qui réagit à ton cycle, à un virus, à un verre de vin comme à une couette trop chaude.",
    "body": """
<h2>Ce que mesure la montre, exactement</h2>
<p>La température du poignet, telle que ta montre la suit, c'est <strong>l'écart entre la température de ta peau au poignet pendant ton sommeil et ta propre normale</strong>. Ce n'est pas ta température corporelle, et ta montre n'est pas un thermomètre : c'est un repère relatif, qui dit si ta nuit a été plus chaude ou plus fraîche que d'habitude.</p>
<p>Dans Ecleptic, c'est le plus léger des cinq signaux du pilier « vitaux » du <a href="/methode/readiness-score.html">Readiness Score</a>, et le seul qui se lit dans les deux sens.</p>

<h2>Ce que ça reflète dans ton corps</h2>
<p>Ta température interne n'est pas fixe : elle suit un rythme sur 24 heures. Le soir, elle baisse pour préparer l'endormissement, et atteint son point bas en fin de nuit. Pour se refroidir, ton corps évacue de la chaleur par la peau, surtout par les mains et les pieds, dont les vaisseaux se dilatent.</p>
<p>Ton poignet se trouve au carrefour : sa température dépend à la fois de ce qui se passe à l'intérieur (ton rythme, tes hormones, une fièvre qui monte) et de ce qui l'entoure (la chambre, la couette). C'est ce qui rend ce signal riche, et difficile à interpréter seul.</p>

<h2>Thermomètre et montre, deux mesures différentes</h2>
<p>Un thermomètre médical mesure ta température interne, dans la bouche, l'oreille ou le rectum ; chez l'adulte, elle tourne autour de 37 °C. La montre, elle, mesure la surface de ta peau, plus fraîche et bien plus sensible à l'environnement. Sa valeur brute n'a donc pas de norme universelle : c'est pour ça qu'on raisonne en écart, par rapport à une référence qui t'est propre.</p>
<p>Il faut à ta montre <strong>quelques nuits pour établir cette référence</strong>, avant de pouvoir te donner un écart. Et tous les modèles ne mesurent pas ce signal : c'est une fonction des Apple Watch récentes. Ecleptic lit ensuite ces données dans Apple Santé.</p>
<div class="figs">
  <div><span class="v">6 %</span><span class="u">Du pilier vitaux</span></div>
  <div><span class="v">±2</span><span class="u">Écarts-types : 0 point</span></div>
  <div><span class="v">42</span><span class="u">Jours de ligne de base</span></div>
  <div><span class="v">7</span><span class="u">Jours pour démarrer</span></div>
</div>

<h2>Ce qui la fait bouger</h2>
<ul>
<li><strong>Le cycle menstruel :</strong> après l'ovulation, la température de base monte de quelques dixièmes de degré et reste plus haute jusqu'aux règles suivantes. Si tu as des règles, ton écart ondule donc au fil du mois, et c'est normal. Pour adapter l'entraînement : <a href="/articles/cycle-menstruel-et-sport.html">cycle menstruel et sport</a>.</li>
<li><strong>La fièvre ou une infection :</strong> la température monte, et la <a href="/methode/frequence-respiratoire.html">fréquence respiratoire</a> grimpe souvent avec elle.</li>
<li><strong>L'alcool :</strong> il dilate les vaisseaux de la peau, ton poignet chauffe, et ta nuit s'en ressent. Le détail dans <a href="/articles/alcool-sommeil-effets.html">alcool et sommeil</a>.</li>
<li><strong>Un repas tardif :</strong> la digestion produit de la chaleur au moment où ton corps cherche à se refroidir.</li>
<li><strong>La chambre et la literie :</strong> une pièce chaude, une couette épaisse, et l'écart grimpe ; une chambre froide, et il baisse. Les bons repères : <a href="/articles/temperature-ideale-chambre-dormir.html">la température idéale pour dormir</a>.</li>
</ul>

<h2>Comment Ecleptic l'utilise</h2>
<p>Ecleptic récupère dans Apple Santé la température du poignet mesurée pendant ton sommeil, et la compare à <a href="/methode/ligne-de-base.html">ta ligne de base</a> : ta moyenne et ton écart-type sur les 42 derniers jours, sans compter le jour évalué. Il faut au moins 7 jours de données pour que le signal compte, et 28 jours pour que sa confiance soit pleine. Avec les quelques nuits dont ta montre a besoin au départ, ce signal demande donc un peu de patience.</p>
<ul>
<li><strong>Le sens :</strong> ici, il n'y a pas de « mieux ». Tout écart à ta normale, vers le chaud comme vers le froid, fait perdre des points.</li>
<li><strong>Le seuil :</strong> au-delà de 2 écarts-types, dans un sens ou dans l'autre, ce signal ne rapporte plus aucun point.</li>
<li><strong>Le poids :</strong> 6 % du pilier <a href="/methode/vitaux.html">vitaux</a>, qui vaut 42 points sur 100. Une journée où toutes les données sont là, la température pèse donc environ 2,5 points du score.</li>
</ul>
<p>Pourquoi si peu ? C'est un choix. La température est utile pour repérer une nuit qui sort de l'ordinaire, mais elle est plus bruitée et moins directement liée à ta récupération que la variabilité cardiaque ou la fréquence cardiaque au repos : une chambre surchauffée ou une couette trop épaisse la font bouger sans rapport avec ta forme. Si ta montre ne la mesure pas, son poids est réparti entre les autres vitaux ; sans montre, c'est tout le pilier qui est redistribué.</p>

<h2>Les limites de la mesure</h2>
<ul>
<li><strong>Ce n'est pas un thermomètre :</strong> la montre ne sert pas à diagnostiquer une fièvre. Si tu te sens fiévreux, prends ta température avec un vrai thermomètre.</li>
<li><strong>L'environnement brouille le signal :</strong> une nuit ailleurs, une fenêtre ouverte, un bras sous la couette ou par-dessus, autant de nuances que la montre ne distingue pas d'un changement interne.</li>
<li><strong>Le score constate, il n'explique pas :</strong> Ecleptic voit que ta température s'écarte de ta normale, pas pourquoi. Virus, verre de vin, cycle ou radiateur : c'est à toi de faire le lien.</li>
</ul>

<h2>Quand consulter</h2>
<p>Un écart isolé, surtout après une soirée arrosée ou dans une chambre surchauffée, n'a en général rien d'inquiétant. En revanche, si tu te sens fiévreux, vérifie avec un thermomètre, et consulte un médecin si la fièvre persiste plusieurs jours ou s'accompagne de symptômes qui t'inquiètent. Laisse aussi ton corps guérir avant de t'entraîner à nouveau : les règles sont dans <a href="/articles/reprendre-le-sport-apres-maladie.html">reprendre le sport après une maladie</a>.</p>
<p>Un malaise, une douleur dans la poitrine, un essoufflement anormal ou des palpitations ne se surveillent pas avec une montre : consulte sans attendre et, en cas d'urgence, appelle le 15 ou le 112. Ecleptic est un outil de bien-être, pas un dispositif médical.</p>
""",
    "refs": [
        "Buchheit M. (2014), suivi de l'état d'entraînement par les mesures de fréquence cardiaque, <em>Frontiers in Physiology</em>.",
        "Miller D. J. et al. (2020), variations de la fréquence respiratoire nocturne et détection précoce d'une infection, <em>PLOS ONE</em>.",
    ],
    "faq": [
        {"q": "À quoi sert la température du poignet sur l'Apple Watch ?",
         "a": "Elle suit, pendant ton sommeil, l'écart de la température de ton poignet par rapport à ta propre normale, établie sur quelques nuits. Ce n'est pas une température corporelle : elle sert à repérer une nuit qui sort de tes habitudes, pas à mesurer une fièvre."},
        {"q": "Pourquoi ma température du poignet est-elle plus élevée que d'habitude ?",
         "a": "Elle peut monter pour des raisons banales : chambre ou couette trop chaude, alcool, repas tardif, ou seconde moitié du cycle menstruel, après l'ovulation. Une fièvre ou une infection peuvent aussi la faire grimper : si tu te sens mal, vérifie avec un vrai thermomètre."},
        {"q": "Une montre connectée peut-elle détecter la fièvre ?",
         "a": "Non : elle mesure la peau du poignet, influencée par la chambre et la literie, et non ta température interne. Un écart peut t'inviter à vérifier, mais seul un thermomètre confirme une fièvre ; si elle persiste ou s'accompagne de symptômes inquiétants, consulte un médecin."},
    ],
    "related": ["vitaux", "readiness-score", "ligne-de-base", "frequence-respiratoire", "saturation-oxygene"],
    "journal": ["cycle-menstruel-et-sport", "temperature-ideale-chambre-dormir", "alcool-sommeil-effets", "reprendre-le-sport-apres-maladie"],
}
