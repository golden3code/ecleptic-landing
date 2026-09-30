# -*- coding: utf-8 -*-
"""Lot F — satellites longue traîne (Readiness / Contexte).

Chargé automatiquement par tools/build_articles.py via _load_satellites().
Expose une liste ENTRIES au même format que ARTICLES.
"""

ENTRIES = [
    {
        "slug": "frequence-cardiaque-repos-normale",
        "cat": "Readiness",
        "title": "Fréquence cardiaque au repos : quelle est la normale ?",
        "description": "La fréquence cardiaque au repos normale est de 60 à 100 bpm, et de 40 à 60 chez les sportifs d'endurance. Comment la mesurer au réveil et la lire en tendance.",
        "date": "2026-09-21",
        "updated": "2026-09-30",
        "body": """
<p>La réponse courte : chez l'adulte, une <strong>fréquence cardiaque au repos normale</strong> se situe entre <strong>60 et 100 battements par minute</strong>. Mais si tu t'entraînes en endurance, tu es probablement plus bas — souvent <strong>40 à 60 bpm</strong> —, et c'est parfaitement sain : ton cœur est devenu plus efficace, il envoie plus de sang à chaque battement, donc il lui en faut moins pour faire le même travail.</p>
<p>Une FC de repos basse est <em>en moyenne</em> le signe d'une bonne condition cardiovasculaire : une méta-analyse de 2016 (46 études, plus de 1,2 million de personnes) associe chaque tranche de 10 bpm supplémentaire au repos à un risque de décès toutes causes augmenté de 9 %. Mais deux personnes en pleine forme peuvent avoir quinze battements d'écart pour une simple raison génétique. Une étude de 2020 sur 92 457 adultes équipés d'un bracelet l'illustre : 65 bpm en moyenne, mais de 40 à 109 bpm selon les individus, alors que chez une même personne le chiffre reste remarquablement stable. Le chiffre absolu compte donc moins que tu ne crois : ce qui parle vraiment, c'est <strong>ta tendance à toi</strong>, jour après jour.</p>

<h2>Ce qui est normal, et pourquoi ça varie autant</h2>
<ul>
<li><strong>Adulte non sportif :</strong> 60 à 100 bpm, la fourchette standard retenue par la National Library of Medicine américaine.</li>
<li><strong>Sportif d'endurance entraîné :</strong> 40 à 60 bpm selon la même source, parfois moins chez les coureurs et cyclistes aguerris. Un cœur puissant qui bat lentement au repos, c'est le résultat recherché de l'entraînement, pas une anomalie.</li>
<li><strong>La génétique pèse lourd :</strong> à condition physique égale, certains sont naturellement à 50, d'autres à 68. Ne fais pas de ton voisin ta référence.</li>
</ul>
<p>D'autres facteurs bougent le chiffre au quotidien : la caféine, la chaleur, le stress, la déshydratation et une nuit trop courte le font monter ; le calme et une bonne récupération le font descendre. D'où l'intérêt de toujours mesurer dans les mêmes conditions.</p>
<p>Et ne confonds pas <strong>fréquence de repos</strong> et <strong>fréquence maximale</strong> : la première se mesure au calme total et descend avec l'entraînement ; la seconde, atteinte à l'effort maximal, dépend surtout de l'âge et ne se travaille quasiment pas — une méta-analyse de 2001 la trouve indépendante du niveau d'activité habituel. Deux chiffres différents, deux histoires différentes — c'est bien la fréquence de <em>repos</em> qui parle de ta récupération.</p>

<h2>Comment la mesurer correctement</h2>
<p>La seule mesure qui vaut vraiment quelque chose, c'est celle du matin, à froid :</p>
<ul>
<li><strong>Au réveil</strong>, avant même de te lever — le simple fait de te mettre debout fait déjà grimper le chiffre.</li>
<li><strong>Allongé, immobile</strong>, après quelques secondes de calme.</li>
<li><strong>Tous les jours si possible</strong>, pour construire ta ligne de base. Une montre ou un capteur au poignet mesurent ça très bien pendant la nuit et te donnent la valeur la plus stable, celle du sommeil.</li>
</ul>
<p>Une mesure isolée ne dit presque rien. C'est la <strong>répétition</strong> qui transforme un chiffre en information.</p>

<h2>Lis-la en tendance, pas en photo</h2>
<p>Voilà le vrai usage. Une fois que tu connais ta normale — disons 52 bpm —, ce qui compte, c'est l'<strong>écart</strong>. Une FC de repos qui grimpe de <strong>plusieurs battements plusieurs matins d'affilée</strong> est un signal sérieux que quelque chose ponctionne ta récupération :</p>
<ul>
<li>Une <strong>fatigue accumulée</strong> ou un début de <a href="/articles/surentrainement-signes.html">surmenage</a> — ton corps réclame du repos.</li>
<li>Une <strong>infection qui couve</strong> : la FC de repos peut monter avant même les premiers symptômes. Une étude de 2020 sur des porteurs de montre connectée estime que 63 % des cas de Covid-19 auraient pu être repérés ainsi avant les symptômes.</li>
<li>De l'<strong>alcool la veille</strong>, qui perturbe la nuit et fait grimper le cœur au repos, d'autant plus que la dose est forte — une étude finlandaise de 2018 sur 4 098 salariés le montre dès les premières heures de sommeil. Un effet <a href="/articles/alcool-sommeil-effets.html">très visible sur les données du matin</a>.</li>
<li>Un <strong>stress</strong> important ou un manque de sommeil.</li>
</ul>
<p>Attention à l'échelle : un ou deux battements de plus ne veulent rien dire, c'est le bruit normal d'un jour à l'autre — c'est un décalage <em>net et répété</em>, de l'ordre de cinq battements sur plusieurs matins, qui doit t'alerter. À l'inverse, une FC de repos qui redescend vers ta base signe une bonne récupération. C'est exactement ce genre de lecture qu'un <a href="/articles/readiness-score-comment-ca-marche.html">score de préparation</a> combine chaque matin avec ta <a href="/articles/hrv-variabilite-frequence-cardiaque.html">variabilité cardiaque</a> pour te dire, en un coup d'œil, si la journée est faite pour pousser ou pour lever le pied.</p>

<h2>Quand consulter</h2>
<p>Cet article parle de bien-être, pas de médecine — mais quelques situations méritent l'avis d'un médecin, sans dramatiser. Une FC de repos <strong>durablement au-dessus de 100</strong> au calme, une <strong>bradycardie sous 40</strong> accompagnée de malaises, de vertiges ou d'essoufflement, ou des <strong>palpitations et un rythme irrégulier</strong> ne s'expliquent pas par l'entraînement et doivent être vérifiés. Un coureur bien entraîné à 42 bpm sans aucun symptôme, en revanche, n'a le plus souvent aucune raison de s'inquiéter. La règle : c'est l'association d'un chiffre extrême <em>et</em> de symptômes qui doit t'amener à consulter.</p>

<h2>Ce qu'il faut retenir</h2>
<ul>
<li>Normale adulte : 60-100 bpm ; sportifs d'endurance souvent 40-60, signe d'un cœur efficace.</li>
<li>Mesure au réveil, allongé, avant de te lever — et lis ta FC de repos en tendance, jamais en valeur isolée.</li>
<li>Une hausse de plusieurs battements sur plusieurs matins signale fatigue, alcool, stress ou infection ; sous 40 avec malaises, consulte.</li>
</ul>
""",
        "faq": [
            {"q": "Quelle est la fréquence cardiaque au repos normale ?",
             "a": "Chez l'adulte, entre 60 et 100 battements par minute. Les sportifs d'endurance sont souvent plus bas, entre 40 et 60 bpm, car leur cœur est plus efficace. La génétique joue aussi : suis ta propre tendance plutôt que de te comparer."},
            {"q": "Comment mesurer sa fréquence cardiaque au repos ?",
             "a": "Au réveil, allongé et immobile, avant de te lever, car se mettre debout fait déjà monter le chiffre. Mesure tous les jours dans les mêmes conditions pour bâtir ta ligne de base ; une montre le fait très bien pendant le sommeil."},
            {"q": "Une fréquence cardiaque de repos basse est-elle bon signe ?",
             "a": "En général oui : elle reflète souvent une bonne condition cardiovasculaire. Mais une bradycardie sous 40 bpm accompagnée de malaises, de vertiges ou d'essoufflement doit être vérifiée par un médecin."},
        ],
        "sources": [
            {"t": "MedlinePlus (U.S. National Library of Medicine). Pulse. Medical Encyclopedia. 2025.",
             "u": "https://medlineplus.gov/ency/article/003399.htm"},
            {"t": "Quer G, Gouda P, Galarnyk M, et al. Inter- and intraindividual variability in daily resting heart rate and its associations with age, sex, sleep, BMI, and time of year: Retrospective, longitudinal cohort study of 92,457 adults. <em>PLoS One</em>. 2020.",
             "u": "https://doi.org/10.1371/journal.pone.0227709"},
            {"t": "Zhang D, Shen X, Qi X. Resting heart rate and all-cause and cardiovascular mortality in the general population: a meta-analysis. <em>CMAJ</em>. 2016.",
             "u": "https://doi.org/10.1503/cmaj.150535"},
            {"t": "Tanaka H, Monahan KD, Seals DR. Age-predicted maximal heart rate revisited. <em>J Am Coll Cardiol</em>. 2001.",
             "u": "https://doi.org/10.1016/s0735-1097(00)01054-8"},
            {"t": "Mishra T, Wang M, Metwally AA, et al. Pre-symptomatic detection of COVID-19 from smartwatch data. <em>Nat Biomed Eng</em>. 2020.",
             "u": "https://doi.org/10.1038/s41551-020-00640-6"},
            {"t": "Pietilä J, Helander E, Korhonen I, et al. Acute effect of alcohol intake on cardiovascular autonomic regulation during the first hours of sleep in a large real-world sample of Finnish employees: observational study. <em>JMIR Ment Health</em>. 2018.",
             "u": "https://doi.org/10.2196/mental.9519"},
        ],
    },
    {
        "slug": "recuperation-active-ou-passive",
        "cat": "Readiness",
        "title": "Récupération active ou passive : laquelle choisir ?",
        "description": "Récupération active ou passive : l'active relance la circulation après une séance, la passive repose vraiment. Comment choisir selon ton état du jour.",
        "date": "2026-09-21",
        "body": """
<p>La réponse courte : les deux sont utiles, mais elles ne servent pas au même moment. La <strong>récupération active</strong> — bouger léger le lendemain d'une grosse séance — est souvent la <em>meilleure</em> option quand tu es simplement raide et un peu fatigué. La <strong>récupération passive</strong> — repos complet — reste la bonne réponse quand tu es réellement vidé, malade ou blessé.</p>
<p>Autrement dit, la question n'est pas « laquelle est supérieure dans l'absolu ? », mais « dans quel état suis-je aujourd'hui ? ». C'est ton corps qui décide, pas le calendrier.</p>

<h2>La récupération active, c'est quoi</h2>
<p>Il s'agit d'un effort <strong>très facile</strong>, volontairement en dessous de la moindre notion de performance :</p>
<ul>
<li>Une <strong>marche</strong> tranquille, une sortie <strong>vélo</strong> souple, une nage lente.</li>
<li>De la <strong>mobilité</strong>, des étirements doux, un peu de gainage léger.</li>
<li>Une sortie <a href="/articles/zone-2-cardio-cest-quoi.html">en zone 2</a> menée vraiment cool — si tu peux tenir une conversation complète sans être essoufflé, tu es au bon endroit.</li>
</ul>
<p>L'idée : <strong>relancer la circulation</strong> sans ajouter de charge. Ça accélère bien l'élimination du lactate dans le sang, mais n'en attends pas de miracle : une revue de 2018 sur le retour au calme actif conclut qu'il change peu la performance du lendemain et la plupart des marqueurs de récupération — sans freiner, a priori, tes progrès à long terme. Son vrai atout, c'est le confort. Tu bouges pour récupérer, pas pour t'entraîner — la nuance est capitale.</p>
<p>Beaucoup de coureurs et de cyclistes intègrent d'ailleurs ces sorties très faciles à leur semaine sous le nom de « footing de récupération » ou de « décrassage » : ce ne sont pas des séances molles par paresse, mais un outil délibéré, calibré pour aider le corps sans le charger.</p>

<h2>La récupération passive, et quand la choisir</h2>
<p>Le repos complet n'est pas un aveu de faiblesse : c'est parfois exactement ce dont ton corps a besoin. Privilégie-le quand :</p>
<ul>
<li>Tu es <strong>réellement épuisé</strong>, pas juste un peu mou — une fatigue profonde, générale.</li>
<li>Tu es <strong>malade</strong>, tu couves quelque chose, ou tu relèves d'une infection.</li>
<li>Tu ressens une <strong>douleur inhabituelle</strong>, qui ressemble plus à une blessure qu'à une courbature.</li>
<li>Tu enchaînes une <strong>grosse période de charge</strong> et tu sens que tout le système sature — c'est le terrain du <a href="/articles/surentrainement-signes.html">surmenage</a>.</li>
</ul>
<p>Dans ces cas, forcer un mouvement « pour bien faire » ralentit la récupération au lieu de l'accélérer. Le repos complet est alors la stratégie gagnante.</p>

<h2>Le match sur les courbatures</h2>
<p>C'est là que l'active prend l'avantage. Quand tu as mal aux jambes deux jours après une grosse séance, l'instinct dit « ne bouge pas ». Or une activité légère soulage généralement <em>mieux</em> la raideur que l'immobilité totale : la circulation relancée assouplit et détend. Une méta-analyse de 2018 (99 études) range d'ailleurs la récupération active parmi les méthodes qui atténuent les courbatures, derrière le massage. Soyons honnêtes : bouger ne fait pas <strong>disparaître</strong> les courbatures plus vite sur le fond — aucune méthode ne les efface vraiment —, mais ça les rend nettement plus supportables sur le moment. Dans une étude de 2006, des mouvements très légers réduisaient la douleur d'environ 40 % juste après, sans accélérer la réparation du muscle. Pour le détail des vrais et faux remèdes, tout est là : <a href="/articles/courbatures-que-faire.html">que faire contre les courbatures</a>.</p>

<h2>Le bon dosage d'une séance de récup active</h2>
<p>Le piège classique, c'est d'en faire trop et de transformer la récup en séance déguisée. Quelques repères pour rester du bon côté :</p>
<ul>
<li><strong>La durée :</strong> 20 à 40 minutes suffisent amplement. On cherche à faire circuler le sang, pas à accumuler du volume.</li>
<li><strong>L'intensité :</strong> vraiment basse — le test de la conversation, ou un effort que tu situerais à 3 ou 4 sur 10. Si tu transpires comme à l'entraînement, tu es trop haut.</li>
<li><strong>Le moment :</strong> le lendemain d'une grosse séance, ou le jour même quelques heures après, quand la raideur commence à s'installer. Une revue de 2003 sur les courbatures conseille d'ailleurs de baisser intensité et durée pendant un à deux jours après une séance qui en provoque de fortes.</li>
<li><strong>La règle d'or :</strong> tu dois finir <em>plus frais</em> qu'au départ. C'est le seul critère qui dit si c'était vraiment de la récupération.</li>
</ul>

<h2>Comment choisir, concrètement</h2>
<p>Pas besoin de deviner : tes signaux du matin tranchent presque toujours. Pose-toi deux questions simples :</p>
<ul>
<li><strong>Suis-je raide, ou suis-je vidé ?</strong> Raide mais avec une énergie correcte → récup active. Vidé, sans jus, tête lourde → récup passive.</li>
<li><strong>Que disent mes vitaux ?</strong> Une fréquence cardiaque de repos et une variabilité proches de ta normale autorisent une sortie facile ; des vitaux franchement dégradés plaident pour le repos. C'est précisément ce qu'un <a href="/articles/readiness-score-comment-ca-marche.html">score de préparation</a> résume chaque matin.</li>
</ul>
<p>Et rien n'interdit de mélanger : commence par dix minutes de marche et arrête-toi si le corps ne suit pas. La récupération active bien menée ne coûte rien — elle ne doit jamais te fatiguer davantage. Si tu finis ta « récup » plus entamé qu'au départ, c'est que ce n'en était pas.</p>

<h2>Ce qu'il faut retenir</h2>
<ul>
<li>Active = mouvement très léger (marche, vélo doux, zone 2, mobilité) pour relancer la circulation sans ajouter de charge.</li>
<li>Passive = repos complet, à privilégier si tu es vraiment vidé, malade ou blessé.</li>
<li>L'active soulage souvent mieux les courbatures ; dans le doute, fie-toi à tes vitaux du matin plutôt qu'au calendrier.</li>
</ul>
""",
        "faq": [
            {"q": "Récupération active ou passive, laquelle est la meilleure ?",
             "a": "Les deux sont utiles à des moments différents. La récupération active (mouvement léger) est souvent préférable quand tu es simplement raide, tandis que le repos complet s'impose si tu es vraiment épuisé, malade ou blessé."},
            {"q": "C'est quoi la récupération active ?",
             "a": "Un effort très facile le lendemain d'une grosse séance — marche, vélo souple, nage lente ou mobilité — pour relancer la circulation et réduire la raideur sans ajouter de charge d'entraînement."},
            {"q": "La récupération active aide-t-elle contre les courbatures ?",
             "a": "Oui, elle soulage généralement mieux la raideur que l'immobilité totale, car la circulation relancée détend les muscles. Elle ne fait pas disparaître les courbatures plus vite, mais les rend plus supportables sur le moment."},
        ],
        "sources": [
            {"t": "Van Hooren B, Peake JM. Do we need a cool-down after exercise? A narrative review of the psychophysiological effects and the effects on performance, injuries and the long-term adaptive response. <em>Sports Med</em>. 2018.",
             "u": "https://doi.org/10.1007/s40279-018-0916-2"},
            {"t": "Dupuy O, Douzi W, Theurot D, et al. An evidence-based approach for choosing post-exercise recovery techniques to reduce markers of muscle damage, soreness, fatigue, and inflammation: a systematic review with meta-analysis. <em>Front Physiol</em>. 2018.",
             "u": "https://doi.org/10.3389/fphys.2018.00403"},
            {"t": "Zainuddin Z, Sacco P, Newton M, Nosaka K. Light concentric exercise has a temporarily analgesic effect on delayed-onset muscle soreness, but no effect on recovery from eccentric exercise. <em>Appl Physiol Nutr Metab</em>. 2006.",
             "u": "https://doi.org/10.1139/h05-010"},
            {"t": "Cheung K, Hume P, Maxwell L. Delayed onset muscle soreness: treatment strategies and performance factors. <em>Sports Med</em>. 2003.",
             "u": "https://doi.org/10.2165/00007256-200333020-00005"},
        ],
    },
    {
        "slug": "comment-savoir-si-on-est-bien-recupere",
        "cat": "Readiness",
        "title": "Comment savoir si tu es bien récupéré ?",
        "description": "Comment savoir si tu es bien récupéré : les signaux du matin (cœur de repos, HRV, sommeil) et le test de la performance pour t'entraîner au bon moment.",
        "date": "2026-09-21",
        "body": """
<p>La réponse courte : tu es bien récupéré quand tes <strong>signaux du matin sont revenus à ta normale</strong> et que ton corps a de nouveau envie de bouger. Concrètement : fréquence cardiaque de repos et variabilité cardiaque dans leurs valeurs habituelles, une nuit qui t'a réparé, des courbatures qui s'estompent, et cette sensation de fraîcheur qui donne envie d'y aller.</p>
<p>Le meilleur juge n'est pas ta seule motivation du matin — elle ment dans les deux sens — mais un petit faisceau d'indices, mesurés et ressentis. Pris ensemble, ils te disent bien plus honnêtement où tu en es qu'une impression au saut du lit.</p>

<h2>Les signaux du matin</h2>
<ul>
<li><strong>Ta fréquence cardiaque de repos est revenue à ta base.</strong> Encore élevée de plusieurs battements ? La récupération n'est pas finie. Pour savoir lire ce chiffre, vois <a href="/articles/frequence-cardiaque-repos-normale.html">la fréquence cardiaque au repos normale</a>.</li>
<li><strong>Ta variabilité cardiaque est dans ta zone habituelle.</strong> La <a href="/articles/hrv-variabilite-frequence-cardiaque.html">HRV</a> reflète l'état de ton système nerveux : revenue à ta normale, c'est bon signe. Basse plusieurs jours de suite, elle trahit le plus souvent une fatigue qui persiste.</li>
<li><strong>Ta nuit t'a réparé.</strong> Un <a href="/articles/combien-heures-sommeil-par-nuit.html">sommeil suffisant</a> et de qualité est le carburant nº1 de la récupération : sans lui, aucun des autres voyants ne passera au vert.</li>
<li><strong>Tes courbatures se sont résorbées</strong> et tu n'as plus cette raideur qui bride tes mouvements.</li>
<li><strong>Tu as envie de bouger.</strong> Ce n'est pas rien : une baisse durable d'envie et d'humeur est un vrai marqueur de sous-récupération. Une revue systématique de 2016 (56 études) a même montré que les questionnaires de ressenti — humeur, stress, fatigue perçue — suivent la charge d'entraînement plus finement que la plupart des mesures objectives.</li>
</ul>

<h2>Le test qui ne trompe pas : la performance</h2>
<p>Les capteurs, c'est bien ; la vérité du terrain, c'est mieux. Le signe le plus fiable que tu as encaissé ta charge, c'est que <strong>tes performances tiennent</strong> :</p>
<ul>
<li>Ta <strong>force</strong> est stable ou en hausse sur tes mouvements de référence.</li>
<li>Tes <strong>allures</strong> habituelles te paraissent aussi faciles qu'avant — pas d'effort anormalement pénible pour le même rythme.</li>
<li>Tes séances faciles te semblent... faciles.</li>
</ul>
<p>À l'inverse, quand une allure d'ordinaire confortable te paraît pénible, le corps te dit clairement qu'il n'a pas fini de récupérer. La performance stable ou en progression est le juge de paix — tout le reste n'est qu'indice. Un test tout bête et redoutable : refais un effort de référence que tu connais par cœur — la même côte, la même série au même poids — et compare la sensation. Là-dessus, ton corps ne triche pas.</p>

<h2>Les signaux qui disent l'inverse</h2>
<p>Sache aussi reconnaître les voyants rouges, pour ne pas les prendre pour un simple manque de motivation :</p>
<ul>
<li>Une <strong>FC de repos qui reste haute</strong> plusieurs matins d'affilée.</li>
<li>Un <strong>sommeil qui se dégrade</strong> alors que tu t'entraînes dur — paradoxal, mais typique de la surcharge.</li>
<li>Une <strong>irritabilité</strong>, une lassitude, des petites douleurs qui traînent.</li>
</ul>
<p>Quand ces signes s'accumulent, ce n'est plus de la fatigue passagère : tu entres dans le domaine du <strong>surmenage</strong>, et le seul remède est le repos. Ignorer ces voyants, c'est le meilleur moyen de creuser un trou dont on met des semaines à sortir.</p>

<h2>Un signal isolé ne suffit pas</h2>
<p>Attention à ne pas surinterpréter un seul chiffre un seul matin. Ta HRV peut plonger après un repas très arrosé sans que ta récupération de fond soit en cause ; ta FC de repos peut grimper simplement parce que la chambre était trop chaude. Ce qui compte, c'est la <strong>convergence</strong> : quand plusieurs signaux pointent dans la même direction pendant deux ou trois jours, le message est fiable. Un voyant isolé, lui, est du bruit — lis la tendance, pas le point. Les spécialistes de la HRV conseillent d'ailleurs de raisonner sur une moyenne de plusieurs jours. Et le sens peut surprendre : chez des triathlètes en surcharge, une étude de 2013 a observé une FC de repos plus basse et une HRV plus haute. Le consensus 2013 des sociétés européenne et américaine de médecine du sport (ECSS et ACSM) le résume : aucun marqueur ne suffit seul à trancher — d'où l'intérêt de toujours croiser avec la performance.</p>

<h2>Un seul chiffre pour tout résumer</h2>
<p>Suivre chaque marqueur à la main, c'est possible mais fastidieux. L'intérêt d'un <a href="/articles/readiness-score-comment-ca-marche.html">score de préparation</a>, c'est justement d'<strong>agréger</strong> tout ça — cœur de repos, HRV, sommeil, charge des jours précédents — en un seul indicateur lisible au réveil. La logique est celle d'un feu tricolore : <strong>vert</strong>, ton corps est prêt, tu peux pousser fort et attaquer une séance dure ; <strong>orange</strong>, tu t'entraînes mais sans chercher l'exploit ; <strong>rouge</strong>, la récupération n'est pas là, lève le pied ou repose-toi. Le score ne remplace pas ton ressenti — il le met en face de tes données, pour t'éviter de forcer un jour où il fallait souffler, ou de te ménager un jour où tu étais parfaitement frais.</p>

<h2>Ce qu'il faut retenir</h2>
<ul>
<li>Bien récupéré = FC de repos et HRV revenues à ta normale, sommeil réparateur, courbatures parties, envie de bouger.</li>
<li>Le test le plus fiable reste la performance : force et allures stables ou en hausse, séances faciles vécues comme faciles.</li>
<li>FC haute, sommeil dégradé et irritabilité qui durent = surmenage : repos. Un score de préparation résume tout ça d'un coup d'œil.</li>
</ul>
""",
        "faq": [
            {"q": "Comment savoir si on est bien récupéré ?",
             "a": "Quand tes signaux du matin sont revenus à ta normale : fréquence cardiaque de repos et variabilité cardiaque habituelles, sommeil réparateur, courbatures résorbées et envie de bouger. Le meilleur test reste une performance stable ou en hausse."},
            {"q": "Quels signes montrent qu'on n'a pas assez récupéré ?",
             "a": "Une fréquence cardiaque de repos élevée plusieurs matins de suite, un sommeil qui se dégrade malgré l'entraînement, de l'irritabilité et des allures habituelles qui paraissent pénibles. Accumulés, ces signes évoquent un surmenage : la réponse est le repos."},
            {"q": "Combien de temps faut-il pour bien récupérer ?",
             "a": "Ça dépend de la charge, du sommeil et de l'individu : quelques heures après une séance facile, un à trois jours après une grosse séance. Fie-toi à tes signaux du matin plutôt qu'à un délai fixe."},
        ],
        "sources": [
            {"t": "Meeusen R, Duclos M, Foster C, et al. Prevention, diagnosis, and treatment of the overtraining syndrome: joint consensus statement of the European College of Sport Science and the American College of Sports Medicine. <em>Med Sci Sports Exerc</em>. 2013.",
             "u": "https://doi.org/10.1249/MSS.0b013e318279a10a"},
            {"t": "Saw AE, Main LC, Gastin PB. Monitoring the athlete training response: subjective self-reported measures trump commonly used objective measures: a systematic review. <em>Br J Sports Med</em>. 2016.",
             "u": "https://doi.org/10.1136/bjsports-2015-094758"},
            {"t": "Plews DJ, Laursen PB, Stanley J, et al. Training adaptation and heart rate variability in elite endurance athletes: opening the door to effective monitoring. <em>Sports Med</em>. 2013.",
             "u": "https://doi.org/10.1007/s40279-013-0071-8"},
            {"t": "Le Meur Y, Pichon A, Schaal K, et al. Evidence of parasympathetic hyperactivity in functionally overreached athletes. <em>Med Sci Sports Exerc</em>. 2013.",
             "u": "https://doi.org/10.1249/MSS.0b013e3182980125"},
            {"t": "Kellmann M, Bertollo M, Bosquet L, et al. Recovery and performance in sport: consensus statement. <em>Int J Sports Physiol Perform</em>. 2018.",
             "u": "https://doi.org/10.1123/ijspp.2017-0759"},
        ],
    },
    {
        "slug": "cycle-menstruel-et-sport",
        "cat": "Contexte",
        "title": "Cycle menstruel et sport : faut-il adapter son entraînement ?",
        "description": "Cycle menstruel et sport : la science est limitée et très individuelle. Écoute ton corps plutôt qu'un calendrier, et l'aménorrhée n'est jamais anodine.",
        "date": "2026-09-21",
        "body": """
<p>La réponse courte : <strong>peut-être, mais pas selon une règle rigide et universelle</strong>. La science sur le sujet est encore <strong>limitée</strong> et, surtout, extrêmement <strong>individuelle</strong> : la variabilité d'une personne à l'autre domine tout ce qu'on pourrait vouloir généraliser. Beaucoup rapportent plus d'énergie en première moitié de cycle et plus de lourdeur avant les règles — mais ça reste une tendance moyenne, pas une loi qui s'appliquerait à toi précisément.</p>
<p>La bonne approche n'est donc pas de suivre un calendrier théorique trouvé en ligne, mais d'<strong>écouter ton corps et tes données</strong>, et de moduler l'intensité selon tes sensations réelles. Ton cycle est un facteur parmi d'autres — au même titre que ton sommeil ou ton stress —, pas un programme d'entraînement en soi.</p>

<h2>Ce que la science dit (et ne dit pas)</h2>
<p>Soyons honnêtes sur l'état des connaissances :</p>
<ul>
<li>Les <strong>études solides manquent</strong> : le sujet a longtemps été négligé par la recherche, et les protocoles restent hétérogènes.</li>
<li>Les <strong>effets moyens mesurés sont faibles</strong> comparés aux différences entre individus. Une méta-analyse de 2020 (78 études) ne trouve qu'une baisse de performance « triviale » en tout début de cycle, pendant les règles, sur des preuves de faible qualité — et recommande une approche personnalisée plutôt que des règles générales. Autrement dit, la phase du cycle explique bien moins ta forme du jour que ton sommeil, ta nutrition ou ta charge d'entraînement récente.</li>
<li>Aucune donnée solide ne justifie de <strong>brider systématiquement</strong> l'entraînement à tel moment du mois. Pour la musculation, une revue de synthèse de 2023 juge prématuré d'affirmer que les variations hormonales pèsent sur la force ou la prise de muscle. Tu peux t'entraîner et progresser sur l'ensemble du cycle.</li>
</ul>
<p>Bref : méfie-toi des méthodes qui promettent un « entraînement calé sur les 4 phases » avec une précision d'horloger. Ça se vend bien, mais ça surestime largement ce que la science permet d'affirmer aujourd'hui.</p>

<h2>Les tendances souvent rapportées</h2>
<p>Cela dit, beaucoup de femmes décrivent un ressenti assez cohérent : dans une enquête de 2021 auprès de 6 812 sportives, 86 % rapportaient de la fatigue liée au cycle et 91 % des changements d'humeur ou de l'anxiété. Un ressenti qui vaut la peine d'être observé sur <em>ton</em> cas :</p>
<ul>
<li><strong>Phase folliculaire</strong> (du premier jour des règles à l'ovulation, grosso modo la première moitié) : une fois les règles passées, souvent plus d'énergie, une bonne tolérance aux séances intenses et à la charge lourde.</li>
<li><strong>Phase lutéale et prémenstruelle</strong> (seconde moitié, avant les règles) : parfois plus de fatigue, une récupération qui traîne, une motivation en baisse, un sommeil moins bon.</li>
<li><strong>Pendant les règles</strong> : très variable — certaines sont gênées, d'autres se sentent parfaitement bien et performent normalement.</li>
</ul>
<p>La consigne : traite ça comme une <strong>hypothèse à vérifier sur toi</strong>, pas comme une vérité imposée. Note tes sensations sur deux ou trois cycles et regarde si un motif se dessine <em>vraiment</em> chez toi.</p>

<h2>La méthode qui marche : tes sensations et tes données</h2>
<p>Plutôt qu'un calendrier rigide, pilote au ressenti et aux signaux objectifs :</p>
<ul>
<li>Les jours où l'énergie est là, <strong>profites-en</strong> pour les séances exigeantes et la charge lourde.</li>
<li>Les jours de lourdeur, <strong>allège sans culpabiliser</strong> : baisse le volume ou l'intensité, garde le mouvement. Une séance modérée vaut toujours mieux qu'une séance forcée et ratée.</li>
<li>Appuie-toi sur tes vitaux du matin. Un <a href="/articles/readiness-score-comment-ca-marche.html">score de préparation</a> qui croise cœur de repos, variabilité et sommeil capte ta fatigue réelle du jour, quelle qu'en soit la cause — cycle compris — sans que tu aies à deviner.</li>
</ul>
<p>C'est plus fiable qu'un modèle théorique, parce que ça mesure ton état <em>réel</em> au lieu de le supposer.</p>

<h2>Un signal à ne jamais banaliser : l'absence de règles</h2>
<p>Un point important, qui sort du simple confort d'entraînement. Chez une sportive, la <strong>disparition des règles</strong> (aménorrhée) n'est <strong>pas</strong> un signe de bonne forme ni une conséquence « normale » d'un gros entraînement. C'est le plus souvent le signal d'un <strong>déficit énergétique</strong> — pas assez de carburant pour couvrir la dépense —, un mécanisme au cœur de ce qu'on appelle le déficit énergétique relatif dans le sport (REDs), objet d'un consensus du Comité international olympique mis à jour en 2023. Selon l'American College of Sports Medicine, c'est cette faible disponibilité énergétique, souvent involontaire, qui dérègle le cycle et fragilise les os. À la longue, ça touche les hormones, la densité osseuse et la santé globale. Et ce n'est pas réservé aux athlètes de haut niveau : ça guette aussi des amatrices assidues qui, sans le vouloir, mangent trop peu au regard de tout ce qu'elles dépensent.</p>
<p>Si tes règles disparaissent ou deviennent très irrégulières alors que tu t'entraînes, ce n'est pas un détail : commence par vérifier que tu <a href="/articles/deficit-calorique-comment-calculer.html">manges assez pour ta dépense</a>, et surtout <strong>parles-en à un médecin</strong>. C'est un motif de consultation, pas quelque chose à laisser filer — et une cause fréquente de <a href="/articles/toujours-fatigue-causes.html">fatigue persistante</a> chez la sportive.</p>

<h2>Ce qu'il faut retenir</h2>
<ul>
<li>La science est limitée et surtout très individuelle : pas de règle universelle pour caler l'entraînement sur le cycle.</li>
<li>Écoute ton corps et tes données, module l'intensité selon tes sensations plutôt que selon un calendrier théorique.</li>
<li>L'absence de règles chez une sportive n'est jamais « normale » : souvent un signe de déficit énergétique, et un motif de consultation médicale.</li>
</ul>
""",
        "faq": [
            {"q": "Faut-il adapter son entraînement à son cycle menstruel ?",
             "a": "Il n'existe pas de règle universelle : la science est limitée et très individuelle. Plutôt qu'un calendrier théorique, module l'intensité selon tes sensations et tes données du jour. Tu peux t'entraîner et progresser sur tout le cycle."},
            {"q": "Quand a-t-on le plus d'énergie dans le cycle menstruel ?",
             "a": "Beaucoup rapportent plus d'énergie une fois les règles passées, jusqu'à l'ovulation, et davantage de fatigue avant les règles. Mais la variabilité d'une personne à l'autre domine : observe ce qui se passe vraiment chez toi."},
            {"q": "Perdre ses règles à cause du sport, est-ce grave ?",
             "a": "Oui, c'est un signal à ne pas banaliser. L'absence de règles chez une sportive traduit souvent un déficit énergétique et peut affecter les hormones et les os. C'est un motif de consultation médicale, pas une conséquence normale de l'entraînement."},
        ],
        "sources": [
            {"t": "McNulty KL, Elliott-Sale KJ, Dolan E, et al. The effects of menstrual cycle phase on exercise performance in eumenorrheic women: a systematic review and meta-analysis. <em>Sports Med</em>. 2020.",
             "u": "https://doi.org/10.1007/s40279-020-01319-3"},
            {"t": "Colenso-Semple LM, D'Souza AC, Elliott-Sale KJ, Phillips SM. Current evidence shows no influence of women's menstrual cycle phase on acute strength performance or adaptations to resistance exercise training. <em>Front Sports Act Living</em>. 2023.",
             "u": "https://doi.org/10.3389/fspor.2023.1054542"},
            {"t": "Bruinvels G, Goldsmith E, Blagrove R, et al. Prevalence and frequency of menstrual cycle symptoms are associated with availability to train and compete: a study of 6812 exercising women recruited using the Strava exercise app. <em>Br J Sports Med</em>. 2021.",
             "u": "https://doi.org/10.1136/bjsports-2020-102792"},
            {"t": "Nattiv A, Loucks AB, Manore MM, et al. American College of Sports Medicine position stand. The female athlete triad. <em>Med Sci Sports Exerc</em>. 2007.",
             "u": "https://doi.org/10.1249/mss.0b013e318149f111"},
            {"t": "Mountjoy M, Ackerman KE, Bailey DM, et al. 2023 International Olympic Committee's (IOC) consensus statement on Relative Energy Deficiency in Sport (REDs). <em>Br J Sports Med</em>. 2023.",
             "u": "https://doi.org/10.1136/bjsports-2023-106994"},
        ],
    },
    {
        "slug": "tabac-nicotine-et-sport",
        "cat": "Contexte",
        "title": "Tabac, nicotine et sport : quels effets sur la performance ?",
        "description": "Tabac, nicotine et sport : le monoxyde de carbone plombe la VO2max, la nicotine freine la récup. Les effets réels sur la performance, et arrêter paie vite.",
        "date": "2026-09-21",
        "body": """
<p>La réponse courte : le tabac <strong>dégrade nettement</strong> la performance et la récupération, sur plusieurs fronts à la fois. Le monoxyde de carbone de la fumée prend la place de l'oxygène dans ton sang, la nicotine resserre les vaisseaux, et l'ensemble perturbe ton sommeil. Pour un sportif, c'est un handicap mesurable — et la bonne nouvelle, c'est qu'il est en grande partie réversible quand on arrête.</p>
<p>Restons factuels, sans moralisme : l'idée n'est pas de culpabiliser qui que ce soit, mais de comprendre <em>par quels mécanismes</em> le tabac et la nicotine pèsent sur ton corps de sportif, et ce que ça change concrètement.</p>

<h2>Pourquoi la fumée plombe l'endurance</h2>
<ul>
<li><strong>Le monoxyde de carbone vole la place de l'oxygène.</strong> Il se fixe sur l'hémoglobine bien plus facilement que l'oxygène, donc ton sang en transporte moins à chaque battement. Résultat direct : moins d'oxygène aux muscles, une <a href="/articles/vo2max-comment-l-ameliorer.html">VO2max plus basse</a> et un essoufflement plus rapide à l'effort. Une revue de 1999 confirme que ce CO réduit la capacité aérobie maximale et avance la fatigue.</li>
<li><strong>Les voies respiratoires s'irritent.</strong> La fumée agresse les bronches et réduit à terme la capacité pulmonaire — l'endurance en prend un coup, et pas seulement chez les gros fumeurs. Dans des cohortes américaines de 25 352 personnes, le déclin respiratoire des fumeurs de moins de cinq cigarettes par jour atteignait 68 % de celui des fumeurs d'au moins trente.</li>
<li><strong>Le cœur travaille plus pour moins.</strong> À effort égal, il doit compenser le déficit d'oxygène, ce qui rend chaque séance plus coûteuse.</li>
</ul>
<p>Concrètement : mêmes jambes, même entraînement, mais un plafond plus bas et des sensations plus dures. Et l'effet n'a rien de réservé à l'effort maximal : même une sortie facile réclame de l'oxygène, donc même ton endurance de base trinque. Le tabac ne te vole pas seulement de la performance — il te vole de la marge de progression.</p>

<h2>La nicotine, même sans fumée</h2>
<p>C'est le point que le vapotage ne règle pas. La nicotine, isolée de la fumée, garde ses propres effets sur ton corps de sportif :</p>
<ul>
<li><strong>Vasoconstriction :</strong> elle resserre les vaisseaux de la peau et du cœur, et accélère le rythme cardiaque. Mais elle dilate ceux des muscles, et selon une revue de 2016, sans combustion, ses risques cardiovasculaires restent faibles face à la cigarette. Son vrai coût pour ta récup passe par le sommeil.</li>
<li><strong>Stimulant :</strong> elle perturbe l'endormissement comme la qualité du sommeil, surtout consommée en soirée — une revue de 2009 (52 études) relève chez les consommateurs un endormissement plus long, un sommeil plus fragmenté et moins de sommeil profond. Et un mauvais sommeil, c'est une <a href="/articles/sommeil-profond-comment-augmenter.html">récupération sabotée</a> à la racine.</li>
<li><strong>Dépendance :</strong> elle crée une accoutumance forte, ce qui rend l'arrêt difficile et entretient la consommation.</li>
</ul>
<p>Le vapotage ou les sachets de nicotine suppriment le monoxyde de carbone et les goudrons de combustion — c'est un vrai avantage sur ce point précis — mais ils <strong>maintiennent la nicotine</strong>, donc la vasoconstriction, les effets sur le sommeil et la dépendance. « Sans fumée » n'est pas « sans effet ».</p>

<h2>Ce que ça change sur tes données</h2>
<p>Si tu suis tes vitaux, le tabac et la nicotine laissent des traces lisibles : une <a href="/articles/hrv-variabilite-frequence-cardiaque.html">variabilité cardiaque</a> souvent plus basse (signe d'un système nerveux moins bien régulé, retrouvé dans la grande majorité des études selon une revue de 2013), une fréquence cardiaque de repos plutôt tirée vers le haut, et un sommeil plus fragmenté les soirs de consommation. Ce ne sont pas des jugements, ce sont des mesures — et elles bougent quand la consommation bouge.</p>
<p>Un point pour les fumeurs occasionnels : même une consommation « sociale », le week-end, laisse une empreinte sur les nuits concernées. Pas besoin d'un paquet par jour pour que l'effet se voie sur ton sommeil et sur ta récupération du lendemain.</p>

<h2>La bonne nouvelle : arrêter, ça se voit vite</h2>
<p>C'est la partie qui motive, et de loin. Le corps répare une bonne partie des dégâts, souvent bien plus vite qu'on ne l'imagine. Le calendrier de l'OMS :</p>
<div class="tablewrap"><table>
<caption>Source : Organisation mondiale de la Santé (2020).</caption>
<thead><tr><th>Après la dernière cigarette</th><th>Ce qui change</th></tr></thead>
<tbody>
<tr><td>20 minutes</td><td>Fréquence cardiaque et tension artérielle baissent</td></tr>
<tr><td>12 heures</td><td>Le monoxyde de carbone du sang revient à la normale</td></tr>
<tr><td>2 à 12 semaines</td><td>La circulation s'améliore, la fonction pulmonaire augmente</td></tr>
<tr><td>1 à 9 mois</td><td>La toux et l'essoufflement diminuent</td></tr>
<tr><td>1 an</td><td>Le risque coronarien tombe à environ la moitié de celui d'un fumeur</td></tr>
</tbody>
</table></div>
<p>En douze heures, ton sang retransporte donc l'oxygène normalement ; en quelques semaines, beaucoup décrivent des séances « qui repassent » et un souffle retrouvé. La récupération et le sommeil se normalisent ensuite à mesure que la nicotine quitte l'équation, après quelques nuits parfois agitées le temps du sevrage.</p>
<p>Autrement dit, chaque semaine sans tabac est un gain de performance quasi gratuit — l'un des rares « progrès » qu'on obtient sans s'entraîner davantage. Si tu veux arrêter et que la dépendance rend ça difficile, un médecin ou un tabacologue peut t'accompagner : c'est un domaine où l'aide fait une vraie différence.</p>

<h2>Ce qu'il faut retenir</h2>
<ul>
<li>Le tabac dégrade l'endurance : le monoxyde de carbone réduit le transport d'oxygène et fait baisser la VO2max.</li>
<li>La nicotine seule (vape incluse) garde ses effets : vaisseaux resserrés, cœur accéléré, sommeil perturbé — donc récupération freinée — et dépendance.</li>
<li>Arrêter améliore la capacité respiratoire en quelques semaines ; pour la dépendance, un médecin ou un tabacologue peut aider.</li>
</ul>
""",
        "faq": [
            {"q": "Quels sont les effets du tabac sur le sport ?",
             "a": "Le tabac réduit la performance et la récupération : le monoxyde de carbone diminue le transport d'oxygène et fait baisser la VO2max, la fumée irrite les bronches, et la nicotine perturbe le sommeil, ce qui freine la récupération."},
            {"q": "Le vapotage est-il moins mauvais que la cigarette pour le sport ?",
             "a": "Le vapotage supprime le monoxyde de carbone et les goudrons de combustion, ce qui est un avantage. Mais il maintient la nicotine, donc la vasoconstriction, les effets sur le sommeil et la dépendance restent bien présents."},
            {"q": "Combien de temps pour récupérer son souffle après avoir arrêté de fumer ?",
             "a": "Selon l'OMS, le monoxyde de carbone du sang revient à la normale en 12 heures, et la circulation comme la fonction pulmonaire s'améliorent en 2 à 12 semaines. Toux et essoufflement diminuent ensuite entre 1 et 9 mois, et les bénéfices continuent de s'accumuler avec le temps."},
        ],
        "sources": [
            {"t": "World Health Organization. Tobacco: health benefits of smoking cessation. 2020.",
             "u": "https://www.who.int/news-room/questions-and-answers/item/tobacco-health-benefits-of-smoking-cessation"},
            {"t": "McDonough P, Moffatt RJ. Smoking-induced elevations in blood carboxyhaemoglobin levels. Effect on maximal oxygen uptake. <em>Sports Med</em>. 1999.",
             "u": "https://doi.org/10.2165/00007256-199927050-00001"},
            {"t": "Oelsner EC, Balte PP, Bhatt SP, et al. Lung function decline in former smokers and low-intensity current smokers: a secondary data analysis of the NHLBI Pooled Cohorts Study. <em>Lancet Respir Med</em>. 2020.",
             "u": "https://doi.org/10.1016/S2213-2600(19)30276-0"},
            {"t": "Benowitz NL, Burbank AD. Cardiovascular toxicity of nicotine: implications for electronic cigarette use. <em>Trends Cardiovasc Med</em>. 2016.",
             "u": "https://doi.org/10.1016/j.tcm.2016.03.001"},
            {"t": "Jaehne A, Loessl B, Bárkai Z, et al. Effects of nicotine on sleep during consumption, withdrawal and replacement therapy. <em>Sleep Med Rev</em>. 2009.",
             "u": "https://doi.org/10.1016/j.smrv.2008.12.003"},
            {"t": "Dinas PC, Koutedakis Y, Flouris AD. Effects of active and passive tobacco cigarette smoking on heart rate variability. <em>Int J Cardiol</em>. 2013.",
             "u": "https://doi.org/10.1016/j.ijcard.2011.10.140"},
        ],
    },
    {
        "slug": "recuperation-apres-40-ans",
        "cat": "Contexte",
        "title": "Récupérer après 40 ans : ce qui change vraiment",
        "description": "Récupérer après 40 ans : ça ralentit moins qu'on ne le croit si tu restes actif. Musculation, protéines, sommeil, échauffement : les vrais ajustements.",
        "date": "2026-09-21",
        "body": """
<p>La réponse courte : oui, la récupération ralentit un peu après 40 ans — mais <strong>bien moins qu'on ne le raconte</strong>, à condition de rester actif. L'essentiel de ce qu'on attribue à « l'âge » vient en réalité du <strong>déconditionnement</strong> : moins d'entraînement, moins de muscle, moins de sommeil. Quelqu'un qui bouge régulièrement à 45 ans peut très bien récupérer mieux qu'un sédentaire de 30 ans.</p>
<p>Autrement dit, passé 40 ans, le jeu n'est pas de « ralentir » mais d'<strong>ajuster</strong> : quelques réglages ciblés suffisent à garder une récupération solide et à continuer de progresser. Voici ce qui change vraiment, et ce qui n'est qu'une idée reçue.</p>

<h2>Ce qui change vraiment</h2>
<ul>
<li><strong>Le délai entre deux séances dures s'allonge un peu.</strong> La récupération après un gros effort peut demander un jour de plus. Une revue de 2016 sur les athlètes vétérans juge d'ailleurs l'effet de l'âge sur la récupération plus faible qu'on ne le pensait, la sédentarité pesant davantage. Ce n'est pas un mur, juste un rythme à respecter : espace davantage les séances très intenses plutôt que de les enchaîner. Rien ne t'oblige pour autant à réduire le nombre total de séances : c'est surtout la densité des efforts très durs qui réclame un peu d'air.</li>
<li><strong>La masse musculaire file plus vite si on ne fait rien.</strong> La fonte musculaire liée à l'âge (sarcopénie) s'installe discrètement : une étude IRM de 2000 (468 adultes) voit la masse musculaire reculer nettement à partir de la fin de la quarantaine, surtout aux jambes. C'est <em>le</em> paramètre à défendre, parce qu'il conditionne la force, le métabolisme et l'autonomie sur le long terme.</li>
<li><strong>La récupération tolère moins l'à-peu-près.</strong> Un sommeil bâclé ou un échauffement escamoté se paient plus cher qu'à 25 ans. La marge d'erreur se réduit — la rigueur, elle, rapporte davantage.</li>
</ul>

<h2>La musculation devient non négociable</h2>
<p>Si tu ne devais garder qu'une priorité après 40 ans, ce serait celle-là. Le renforcement musculaire est le <strong>meilleur antidote</strong> à la fonte musculaire : il entretient la force, protège les articulations, soutient le métabolisme et préserve la densité osseuse. L'OMS recommande d'en faire au moins deux jours par semaine, et deux à trois séances suffisent à inverser la tendance : une méta-analyse de 2011 (49 études, 1 328 participants de plus de 50 ans) chiffre le gain moyen à 1,1 kg de masse maigre, d'autant plus net qu'on commence tôt.</p>
<p>Et pour construire ou simplement conserver ce muscle, il faut le stimuler intelligemment dans la durée : c'est tout l'enjeu de la <a href="/articles/surcharge-progressive-comment-progresser.html">surcharge progressive</a>, appliquée sans précipitation. La régularité et la force priment largement sur la recherche de la séance « qui décoiffe ».</p>

<h2>Manger les protéines qu'il faut</h2>
<p>Un phénomène bien réel avec l'âge : la <strong>résistance anabolique</strong>. Le muscle vieillissant répond moins fort à une même quantité de protéines — il en faut donc un peu <strong>plus</strong> pour déclencher la construction musculaire. Le phénomène est surtout documenté chez les plus âgés : une analyse de 2015 situe le plafond de la synthèse musculaire à 0,40 g de protéines par kilo et par repas vers 71 ans, contre 0,24 g vers 22 ans. Concrètement, vise plutôt le <strong>haut de la fourchette</strong> recommandée, et répartis l'apport sur la journée au lieu de tout concentrer sur un seul repas. Le détail des quantités et de la répartition est ici : <a href="/articles/proteines-par-jour-prise-de-muscle.html">combien de protéines par jour</a>.</p>
<p>Ce n'est pas une lubie de magazine : c'est l'un des ajustements nutritionnels les mieux établis pour bien vieillir sportivement. Et ne néglige pas l'énergie globale : sous-manger en croyant « bien faire » accélère justement la fonte musculaire que tu cherches à éviter.</p>

<h2>Soigner le sommeil et l'échauffement</h2>
<p>Les deux gestes dont le rendement grimpe avec l'âge :</p>
<ul>
<li><strong>Le sommeil</strong> reste le premier outil de récupération, à tout âge — et il pardonne moins les nuits courtes après 40 ans. Vise d'abord la quantité et la régularité : tout part de <a href="/articles/combien-heures-sommeil-par-nuit.html">là</a>.</li>
<li><strong>L'échauffement</strong> mérite plus de temps qu'avant. Des tissus un peu moins souples ont besoin d'être préparés progressivement : quelques minutes de plus en montée en charge tendent à réduire le risque de bobo qui casse des semaines d'entraînement — c'est le sens de la majorité des essais randomisés, selon une revue de 2006.</li>
</ul>
<p>Rien de spectaculaire — juste des bases mieux tenues. C'est précisément ce qui fait la différence sur la durée.</p>

<h2>Reste progressif, écoute les signaux</h2>
<p>Le vrai risque après 40 ans n'est pas d'« en faire trop peu », c'est de vouloir reprendre comme à 20 ans du jour au lendemain. Monte en charge par paliers, laisse à ton corps le temps d'encaisser, et fie-toi à tes signaux de récupération plutôt qu'à ton ego. Les voyants d'un <a href="/articles/surentrainement-signes.html">surmenage</a> — sommeil qui se dégrade, fatigue qui traîne, motivation en berne, petites douleurs persistantes — comptent encore plus à cet âge, où la récupération demande un peu plus d'égards. Bien géré, l'entraînement après 40 ans ne se subit pas : il se pilote, et il continue de progresser longtemps.</p>

<h2>Ce qu'il faut retenir</h2>
<ul>
<li>La récupération ralentit un peu après 40 ans, mais bien moins que prévu si tu restes actif : l'essentiel se joue sur le déconditionnement.</li>
<li>Priorités : musculation pour contrer la fonte musculaire, protéines vers le haut de la fourchette, sommeil et échauffement soignés.</li>
<li>Espace un peu plus les grosses séances, reste progressif et écoute tes signaux — la régularité et la force priment sur l'intensité maximale.</li>
</ul>
""",
        "faq": [
            {"q": "La récupération est-elle plus longue après 40 ans ?",
             "a": "Un peu, mais bien moins qu'on ne le dit si tu restes actif. La plupart du ralentissement vient du déconditionnement, pas de l'âge lui-même. En pratique, espace un peu plus tes séances très intenses."},
            {"q": "Comment bien récupérer après 40 ans ?",
             "a": "Priorise la musculation pour contrer la fonte musculaire, vise le haut de la fourchette de protéines, soigne ton sommeil et ton échauffement, et reste progressif. La régularité et la force comptent plus que l'intensité maximale."},
            {"q": "Faut-il plus de protéines en prenant de l'âge ?",
             "a": "Oui, un peu : le muscle vieillissant répond moins bien aux protéines (résistance anabolique), il en faut donc plutôt vers le haut de la fourchette, réparti sur la journée, pour préserver la masse musculaire."},
        ],
        "sources": [
            {"t": "Borges N, Reaburn P, Driller M, Argus C. Age-related changes in performance and recovery kinetics in masters athletes: a narrative review. <em>J Aging Phys Act</em>. 2016.",
             "u": "https://doi.org/10.1123/japa.2015-0021"},
            {"t": "Janssen I, Heymsfield SB, Wang ZM, Ross R. Skeletal muscle mass and distribution in 468 men and women aged 18-88 yr. <em>J Appl Physiol</em>. 2000.",
             "u": "https://doi.org/10.1152/jappl.2000.89.1.81"},
            {"t": "Bull FC, Al-Ansari SS, Biddle S, et al. World Health Organization 2020 guidelines on physical activity and sedentary behaviour. <em>Br J Sports Med</em>. 2020.",
             "u": "https://doi.org/10.1136/bjsports-2020-102955"},
            {"t": "Peterson MD, Sen A, Gordon PM. Influence of resistance exercise on lean body mass in aging adults: a meta-analysis. <em>Med Sci Sports Exerc</em>. 2011.",
             "u": "https://doi.org/10.1249/MSS.0b013e3181eb6265"},
            {"t": "Moore DR, Churchward-Venne TA, Witard O, et al. Protein ingestion to stimulate myofibrillar protein synthesis requires greater relative protein intakes in healthy older versus younger men. <em>J Gerontol A Biol Sci Med Sci</em>. 2015.",
             "u": "https://doi.org/10.1093/gerona/glu103"},
            {"t": "Fradkin AJ, Gabbe BJ, Cameron PA. Does warming up prevent injury in sport? The evidence from randomised controlled trials? <em>J Sci Med Sport</em>. 2006.",
             "u": "https://doi.org/10.1016/j.jsams.2006.03.026"},
        ],
    },
]
