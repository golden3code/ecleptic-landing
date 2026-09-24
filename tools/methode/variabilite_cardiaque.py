# -*- coding: utf-8 -*-
"""La méthode · Fiche — la variabilité cardiaque (HRV).

Chargé par tools/build_articles.py (_load_methode) → /methode/variabilite-cardiaque.html.
Faits vérifiés dans le code de l'app (lib/readiness/physio.ts, baseline.ts) le
24/09/2026 : HRV lue dans Apple Santé au format SDNN (ms), 45 % du pilier vitaux
(42 points), plus haute = mieux, ligne de base 42 j (jour exclu, min 7, confiance
pleine 28), 0 point au-delà de 2 écarts-types sous la normale ; modificateur de
l'âge biologique jusqu'à ±3 ans, demi-poids sous traitement qui ralentit le cœur.
"""

PAGE = {
    "slug": "variabilite-cardiaque",
    "kind": "fiche",
    "num": None,
    "order": 1,
    "label": "La variabilité cardiaque (HRV)",
    "title": "La variabilité cardiaque (HRV), battement par battement",
    "seo_title": "Variabilité cardiaque (HRV) : définition, valeurs, lecture — Ecleptic",
    "description": "Variabilité cardiaque (HRV) : ce qu'elle mesure, pourquoi elle varie d'une personne à l'autre, ce qui la fait baisser et comment l'app la lit.",
    "date": "2026-09-24",
    "lead": "Ton cœur ne bat pas comme un métronome, et c'est une excellente nouvelle. Cet écart d'un battement à l'autre, la <strong>variabilité cardiaque</strong>, est l'un des témoins les plus fins de ta récupération, à condition de la comparer à toi-même et jamais aux autres.",
    "body": """
<h2>La définition, en une phrase</h2>
<p>La variabilité cardiaque, ou HRV (<em>heart rate variability</em>), c'est <strong>la variation du temps qui sépare deux battements successifs</strong>. Elle s'exprime en millisecondes.</p>
<p>Même à 60 battements par minute, ton cœur ne bat pas une fois par seconde pile : un intervalle dure 980 millisecondes, le suivant 1030, le troisième 1005. Cette irrégularité n'est pas un défaut. C'est la signature d'un cœur qui s'ajuste en permanence à ce que ton corps lui demande.</p>

<h2>Ce qu'elle reflète : ton système nerveux autonome</h2>
<p>Deux systèmes pilotent ton cœur, sans que tu y penses :</p>
<ul>
<li><strong>Le sympathique, l'accélérateur :</strong> il prend la main face au stress, à l'effort ou à une menace. Les battements deviennent plus réguliers, la HRV baisse.</li>
<li><strong>Le parasympathique, le frein :</strong> porté en grande partie par le nerf vague, il domine au repos, pendant la digestion et la récupération. Le cœur s'ajuste battement par battement, la HRV monte.</li>
</ul>
<p>Une HRV haute par rapport à ta normale signale un corps en mode récupération ; une HRV basse, un corps encore mobilisé. Le même équilibre pilote ta <a href="/methode/frequence-cardiaque-repos.html">fréquence cardiaque au repos</a>, et ta respiration s'en mêle : le cœur accélère un peu à l'inspiration et ralentit à l'expiration, d'où le lien étroit avec ta <a href="/methode/frequence-respiratoire.html">fréquence respiratoire</a>.</p>

<h2>Comment on la mesure : électrocardiogramme ou montre</h2>
<p>En laboratoire, la référence est l'<strong>électrocardiogramme</strong>. Il repère chaque battement et mesure les intervalles, selon des normes internationales fixées dès 1996.</p>
<p>Ta montre procède autrement. Son capteur optique au poignet, la <strong>photopléthysmographie</strong>, détecte l'onde de pouls à travers la peau. C'est moins précis qu'un électrocardiogramme, mais fiable en tendance quand la montre est bien portée et que tu ne bouges pas. La nuit réunit ces deux conditions.</p>
<p>Reste la question du format. Apple Santé enregistre la HRV en <strong>SDNN</strong>, l'écart-type des intervalles entre battements : c'est ce que mesure l'Apple Watch. Beaucoup d'études et d'autres appareils utilisent le <strong>RMSSD</strong>, calculé sur les différences entre battements successifs. Les deux ne se comparent pas directement : un chiffre lu sur un forum, ou sur la montre d'un ami, ne dit rien du tien.</p>

<h2>Pourquoi la tienne ne ressemble à aucune autre</h2>
<p>La HRV est l'une des mesures <strong>les plus individuelles</strong> qui soient. Selon l'âge, la génétique et la condition physique, elle va d'une vingtaine à plus de 100 millisecondes. Elle baisse avec les années, et l'entraînement d'endurance tend à la faire monter.</p>
<p>Conséquence directe : comparer ta HRV à un tableau trouvé en ligne n'a presque aucun sens. Deux personnes du même âge, aussi en forme l'une que l'autre, peuvent afficher des valeurs très éloignées. <strong>La seule comparaison qui compte, c'est toi contre toi</strong>, sur plusieurs semaines, avec le même appareil.</p>

<h2>Ce qui la fait baisser, ce qui l'aide</h2>
<ul>
<li><strong>Le manque de sommeil :</strong> une nuit courte ou hachée laisse ton système nerveux en alerte.</li>
<li><strong>L'alcool :</strong> même en petite quantité, un verre le soir fait souvent baisser la HRV de la nuit qui suit.</li>
<li><strong>Le stress :</strong> une période tendue garde l'accélérateur enfoncé, même au repos.</li>
<li><strong>La charge d'entraînement :</strong> une séance dure, ou des semaines qui s'enchaînent sans récupération suffisante.</li>
<li><strong>Une infection qui démarre :</strong> ton corps mobilise ses défenses, parfois avant que tu ne te sentes malade.</li>
</ul>
<p>À l'inverse, ce qui l'aide est connu : un <strong>sommeil régulier</strong>, un entraînement d'<strong>endurance</strong> progressif, la <strong>respiration lente</strong>, dont la <a href="/articles/coherence-cardiaque-respiration.html">cohérence cardiaque</a> est la forme la plus simple, et <strong>moins d'alcool</strong>.</p>

<h2>Comment Ecleptic la lit</h2>
<p>Dans l'app, la HRV est le signal le plus lourd du pilier vitaux du <a href="/methode/readiness-score.html">Readiness Score</a> : <strong>45 % de ses 42 points</strong>, soit près de 19 points sur 100 quand toutes les données sont là.</p>
<div class="figs">
  <div><span class="v">45 %</span><span class="u">du pilier vitaux</span></div>
  <div><span class="v">≈ 19</span><span class="u">points du score sur 100</span></div>
  <div><span class="v">42 j</span><span class="u">de ligne de base</span></div>
  <div><span class="v">± 3 ans</span><span class="u">d'âge biologique, au plus</span></div>
</div>
<p>L'app la lit dans Apple Santé, au format SDNN, puis la compare à ta <a href="/methode/ligne-de-base.html">ligne de base</a> : ta moyenne et ton écart-type des 42 derniers jours, jour évalué exclu. Il faut 7 jours de données pour démarrer, 28 pour une confiance pleine. Plus ta HRV est haute par rapport à ta normale, plus elle rapporte de points ; au-delà de deux écarts-types sous ta moyenne, elle n'en rapporte plus aucun. Le détail des cinq signaux : <a href="/methode/vitaux.html">Les vitaux</a>.</p>
<p>Une nuit basse fait baisser ton score du jour, c'est normal. Mais <strong>une HRV qui chute une nuit, c'est du bruit ; une semaine sous ta ligne de base, c'est un signal.</strong></p>
<p>Elle compte aussi dans ton <a href="/methode/age-biologique.html">âge biologique</a> : comparée aux valeurs attendues pour ton âge, elle peut le déplacer jusqu'à 3 ans dans un sens ou dans l'autre, et n'y compte qu'à moitié si tu prends un traitement qui ralentit le cœur.</p>

<h2>Les limites de la mesure</h2>
<ul>
<li><strong>Le capteur optique :</strong> une montre trop lâche ou un bras qui bouge, et la mesure se dégrade. Porte-la bien ajustée, toute la nuit.</li>
<li><strong>Le rythme lui-même :</strong> des battements irréguliers, comme des extrasystoles, faussent le calcul de la HRV.</li>
<li><strong>Les traitements :</strong> un traitement qui ralentit le cœur modifie la lecture de ta HRV.</li>
<li><strong>Le changement d'appareil :</strong> changer de montre, c'est changer d'instrument. Pendant les six semaines qui suivent, ta ligne de base mêle encore les nuits des deux appareils.</li>
</ul>

<h2>Quand consulter</h2>
<p>La HRV n'est pas un outil de diagnostic, et Ecleptic n'est pas un dispositif médical. Une HRV basse, même plusieurs jours de suite, n'est pas une maladie : c'est une invitation à <a href="/articles/hrv-basse-que-faire.html">agir sur ce qui la fait baisser</a>, à mieux dormir, à alléger l'entraînement.</p>
<p>En revanche, si une baisse s'installe sans raison apparente avec une fatigue inhabituelle, ou si tu ressens des palpitations, un malaise, une douleur thoracique ou un essoufflement anormal, consulte un médecin. En cas d'urgence, appelle le 15 ou le 112.</p>
""",
    "refs": [
        "Task Force de la Société européenne de cardiologie et de la NASPE (1996), normes de mesure de la variabilité cardiaque, <em>Circulation</em>.",
        "Shaffer F. et Ginsberg J. P. (2017), panorama des indicateurs et des normes de variabilité cardiaque, <em>Frontiers in Public Health</em>.",
        "Nunan D. et al. (2010), valeurs normales de la variabilité cardiaque de courte durée chez l'adulte sain, <em>Pacing and Clinical Electrophysiology</em>.",
        "Plews D. J. et al. (2013), suivi de la variabilité cardiaque et adaptation à l'entraînement chez l'athlète d'endurance, <em>Sports Medicine</em>.",
    ],
    "faq": [
        {"q": "Quelle est une bonne HRV pour mon âge ?",
         "a": "Il n'existe pas de bonne valeur universelle : selon l'âge, la génétique et la condition physique, la HRV va d'une vingtaine à plus de 100 millisecondes, et elle baisse avec les années. Le bon repère, c'est ta propre moyenne sur plusieurs semaines, mesurée avec le même appareil."},
        {"q": "Pourquoi ma HRV a-t-elle chuté cette nuit ?",
         "a": "Les causes les plus courantes sont une nuit trop courte, de l'alcool la veille, une période de stress, une séance dure ou une infection qui démarre. Une seule nuit basse relève souvent du bruit ; plusieurs jours sous ta ligne de base sont un vrai signal pour lever le pied. Si des symptômes inhabituels l'accompagnent, consulte un médecin."},
        {"q": "La HRV de l'Apple Watch est-elle fiable ?",
         "a": "La montre suit ton pouls avec un capteur optique, moins précis qu'un électrocardiogramme mais fiable en tendance quand elle est bien portée et que tu es au repos, comme la nuit. Elle exprime la HRV au format SDNN, qui ne se compare pas directement au RMSSD d'autres appareils : compare-toi à toi-même, sur la même montre."},
    ],
    "related": ["vitaux", "frequence-cardiaque-repos", "ligne-de-base", "readiness-score", "age-biologique"],
    "journal": ["hrv-variabilite-frequence-cardiaque", "hrv-basse-que-faire", "comment-ameliorer-sa-hrv", "coherence-cardiaque-respiration"],
}
