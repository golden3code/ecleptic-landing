#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Génère les pages articles + l'index /articles/ + sitemap.xml.

Pour ajouter un article : ajouter une entrée dans ARTICLES puis lancer
    python3 tools/build_articles.py
depuis la racine du repo landing, et commiter les fichiers générés.
"""
import os, html

SITE = "https://ecleptic.health"
TF_LINK = "https://testflight.apple.com/join/H5CQgDa7"
POSTHOG_KEY = "phc_wzjqudiS3KH7MeMii8h6HmUR2onfQR5iasjhAs53AL2B"

# slug, title (H1 + <title>), description (meta), date ISO, body HTML
ARTICLES = [
    # Pour ajouter un article :
    # {
    #     "slug": "mon-slug-seo",
    #     "cat": "Sommeil",  # un des DOMAINS ci-dessous
    #     "title": "Titre de l'article",
    #     "description": "Meta description 140-160 caractères.",
    #     "date": "2026-09-19",
    #     "body": """<p>...</p><h2>...</h2>""",
    # },
    {
        "slug": "combien-heures-sommeil-par-nuit",
        "cat": "Sommeil",
        "title": "Combien d'heures de sommeil faut-il vraiment par nuit ?",
        "description": "7 à 9 heures pour la plupart des adultes — mais la vraie réponse dépend de toi. Ce que disent les données, et comment trouver ton besoin réel en deux semaines.",
        "date": "2026-09-19",
        "body": """
<p>La réponse courte : <strong>entre 7 et 9 heures</strong> pour la quasi-totalité des adultes. C'est la fourchette retenue par la National Sleep Foundation et par l'American Academy of Sleep Medicine, sur la base de centaines d'études. En dessous de 7 heures de façon répétée, les risques mesurables augmentent — métabolisme, immunité, humeur, accidents. Au-delà de 9 heures chez un adulte en bonne santé, c'est rarement un besoin : c'est souvent le signe d'une dette qui se rembourse, ou d'un sommeil de mauvaise qualité qui se compense en quantité.</p>
<p>La réponse honnête : <em>ça dépend de toi</em>, et la variation est plus grande qu'on ne le croit. Ton besoin réel est largement génétique. Certaines personnes fonctionnent parfaitement avec 7 heures. D'autres ont besoin de 9 heures pour être au même niveau. Les vrais « courts dormeurs » naturels — moins de 6 heures sans aucun déficit — existent, mais ils sont rarissimes : quelques personnes sur mille. Statistiquement, ce n'est pas toi.</p>

<h2>Pourquoi « 8 heures » est un malentendu</h2>
<p>Le chiffre de 8 heures n'est pas faux, il est mal compris. C'est une <strong>moyenne de population</strong>, pas une prescription individuelle. Dire « il faut dormir 8 heures » revient à dire « il faut chausser du 42 » : c'est vrai en moyenne et faux pour la moitié des gens.</p>
<p>Ce que la recherche montre de façon robuste, c'est la forme de la courbe : les risques pour la santé dessinent un U. Ils montent nettement sous 6 heures, restent bas entre 7 et 9, et remontent au-delà — probablement parce que dormir très longtemps est plus souvent un symptôme qu'une cause. Ta cible personnelle se trouve quelque part dans ce creux, et elle bouge selon les périodes de ta vie : charge d'entraînement, stress, maladie, sommeil en retard à rattraper.</p>

<h2>Si tu t'entraînes, vise le haut de la fourchette</h2>
<p>L'exercice augmente le besoin de sommeil, parce que c'est pendant la nuit que l'essentiel de la réparation se produit : sécrétion d'hormone de croissance en sommeil profond, synthèse protéique, consolidation des apprentissages moteurs.</p>
<p>Les études d'« extension de sommeil » chez les sportifs sont parlantes : quand des basketteurs universitaires sont passés à 10 heures au lit par nuit pendant plusieurs semaines, leurs sprints se sont améliorés, leur précision au tir a gagné environ 9 points de pourcentage, et leur temps de réaction a chuté. À l'inverse, une seule nuit courte dégrade la force maximale modestement — mais dégrade nettement l'endurance, la motivation et la tolérance à l'effort dès le lendemain.</p>
<ul>
<li><strong>Tu t'entraînes 3-4 fois par semaine :</strong> vise 7 h 30 – 8 h 30 de sommeil réel.</li>
<li><strong>Tu t'entraînes 5 fois ou plus, ou tu es en préparation :</strong> vise 8 – 9 heures, sieste comprise.</li>
<li><strong>Période de sèche ou de déficit calorique :</strong> le manque de sommeil fait fondre le muscle en priorité — dans une étude célèbre, à déficit égal, les participants qui dormaient 5 h 30 perdaient 60 % de masse maigre en plus que ceux qui dormaient 8 h 30.</li>
</ul>

<h2>Temps au lit ≠ temps de sommeil</h2>
<p>Détail qui change tout : ces chiffres parlent de <strong>sommeil réel</strong>, pas de temps passé au lit. Avec une efficacité de sommeil normale de 85-92 %, il faut environ 8 h 30 au lit pour dormir 7 h 45. Si tu te couches à minuit et te lèves à 7 h en croyant « dormir 7 heures », tu en dors probablement 6 h 15. C'est l'erreur de calcul la plus répandue — et elle suffit à créer une dette chronique invisible.</p>

<h2>Les signes que tu ne dors pas assez</h2>
<p>Ton corps répond à la question mieux qu'aucune règle générale. Les signaux fiables :</p>
<ul>
<li>Tu as <strong>besoin d'un réveil</strong> pour émerger, tous les jours, et il t'arrache au sommeil profond.</li>
<li>Tu dors <strong>1 h 30 de plus ou davantage le week-end</strong> : c'est une dette qui se rembourse, pas de la paresse.</li>
<li>Tu t'endors <strong>en moins de 5 minutes</strong> le soir — s'endormir instantanément n'est pas un talent, c'est un symptôme de privation.</li>
<li>Coup de barre marqué en début d'après-midi, café indispensable pour tenir la matinée, irritabilité sans raison claire.</li>
</ul>
<p>Aucun de ces signes isolé n'est une preuve. Les quatre ensemble, si.</p>

<h2>Trouver ton chiffre : le protocole des deux semaines</h2>
<p>La méthode la plus fiable ne demande aucun matériel, juste une période calme (vacances, ou deux semaines sans grosses échéances) :</p>
<ul>
<li>Couche-toi chaque soir à la même heure, choisie pour te laisser au moins 8 h 30 devant toi.</li>
<li><strong>Pas de réveil.</strong> Laisse ton corps se lever seul.</li>
<li>Ignore les premières nuits : tu rembourses d'abord ta dette, les durées seront gonflées.</li>
<li>Au bout de 10 à 14 jours, ta durée de réveil spontané se stabilise. <em>Ce chiffre-là est ton besoin réel.</em></li>
</ul>
<p>Ensuite, le travail consiste à protéger ce volume en semaine — et c'est là que la régularité des horaires compte presque autant que la durée elle-même : se coucher et se lever à heures fixes stabilise l'horloge circadienne, et améliore la qualité du sommeil à durée égale.</p>

<h2>Ce qu'il faut retenir</h2>
<ul>
<li>7 à 9 heures de <strong>sommeil réel</strong> pour presque tout le monde ; le haut de la fourchette si tu t'entraînes sérieusement.</li>
<li>« 8 heures » est une moyenne, pas ta prescription : ton besoin est personnel et se mesure.</li>
<li>Compte 30 à 60 minutes de plus au lit que ta cible de sommeil.</li>
<li>Réveil spontané, énergie stable en journée, pas de rattrapage massif le week-end : voilà à quoi ressemble un sommeil suffisant.</li>
</ul>
""",
    },
    {
        "slug": "readiness-score-comment-ca-marche",
        "cat": "Readiness",
        "title": "Readiness score : comment ça marche, et comment l'améliorer",
        "description": "HRV, fréquence cardiaque de repos, sommeil, charge récente : ce que mesure vraiment un score de préparation, ses limites, et comment le faire monter durablement.",
        "date": "2026-09-19",
        "body": """
<p>Un <strong>readiness score</strong> — score de préparation en français — est un chiffre, généralement sur 100, qui estime chaque matin l'état de ton corps : es-tu prêt à encaisser une grosse journée, ou en train de payer les précédentes ? Popularisé par Whoop et Oura, le concept repose sur une idée simple : la progression ne vient pas de l'entraînement lui-même, mais de la <em>récupération</em> qui le suit. Le score te dit où tu en es dans ce cycle.</p>

<h2>Ce qu'il y a dans le calcul</h2>
<p>Les formules varient d'une app à l'autre, mais les ingrédients sont presque toujours les mêmes :</p>
<ul>
<li><strong>La variabilité de fréquence cardiaque (HRV)</strong> — le signal le plus sensible de l'état de ton système nerveux. Elle chute quand le corps est sous pression (<a href="/articles/hrv-variabilite-frequence-cardiaque.html">on t'explique la HRV en détail ici</a>).</li>
<li><strong>La fréquence cardiaque de repos</strong> — mesurée la nuit. Quelques battements au-dessus de ta normale = récupération incomplète, maladie qui couve, ou alcool de la veille.</li>
<li><strong>Ton sommeil</strong> — durée et qualité de la nuit, comparées à ton besoin (<a href="/articles/combien-heures-sommeil-par-nuit.html">combien d'heures il te faut vraiment</a>).</li>
<li><strong>Ta charge récente</strong> — l'entraînement des derniers jours, parce qu'une grosse séance se paie pendant 24 à 72 heures.</li>
</ul>
<p>Le point décisif : tout est comparé à <strong>ta propre ligne de base</strong>, construite sur des semaines de données. Un bon score ne te compare jamais à une moyenne d'autres gens — une HRV de 45 ms peut être excellente pour toi et médiocre pour quelqu'un d'autre.</p>

<h2>Comment le lire sans se tromper</h2>
<p>Trois règles évitent l'essentiel des erreurs d'interprétation :</p>
<ul>
<li><strong>La tendance bat la valeur du jour.</strong> Un mauvais score isolé ne veut presque rien dire ; cinq matins en baisse racontent une vraie histoire.</li>
<li><strong>Le score est un conseil, pas un ordre.</strong> Un 55 ne t'interdit pas de t'entraîner — il suggère d'y aller moins fort, ou de troquer l'intensité contre de la technique.</li>
<li><strong>Ne le vérifie pas dix fois par jour.</strong> Il est calculé au réveil, sur ta nuit. La suite de la journée ne le change pas.</li>
</ul>

<h2>Ce qui fait monter un score de préparation</h2>
<p>Les leviers sont ennuyeux et c'est une bonne nouvelle : ils sont tous sous ton contrôle.</p>
<ul>
<li>Dormir assez, à <a href="/articles/se-coucher-meme-heure-regularite.html">horaires réguliers</a> — de loin le levier nº1.</li>
<li>Alterner vraiment les jours durs et les jours faciles, au lieu d'empiler du moyen tous les jours.</li>
<li>Limiter l'<a href="/articles/alcool-sommeil-effets.html">alcool le soir</a> : c'est l'un des rares facteurs capables d'écraser HRV, fréquence cardiaque et sommeil profond la même nuit.</li>
<li>Manger suffisamment les jours de grosse charge — un gros déficit calorique se lit dans les vitaux en 48 heures.</li>
</ul>

<h2>Ce qu'il faut retenir</h2>
<ul>
<li>Un readiness score croise HRV, cœur de repos, sommeil et charge récente, comparés à <strong>ta</strong> ligne de base.</li>
<li>Il se lit en tendance, et il oriente l'intensité du jour — il ne décide pas à ta place.</li>
<li>Sommeil régulier, alternance dur/facile, alcool rare : voilà ce qui le fait monter pour de bon.</li>
</ul>
""",
    },
    {
        "slug": "hrv-variabilite-frequence-cardiaque",
        "cat": "Récupération",
        "title": "HRV : c'est quoi la variabilité de fréquence cardiaque ?",
        "description": "La HRV mesure les micro-variations entre deux battements de cœur — le meilleur indicateur accessible de ta récupération. Comment la lire, et ce qui la fait bouger.",
        "date": "2026-09-19",
        "body": """
<p>La <strong>variabilité de fréquence cardiaque</strong> (HRV, pour heart rate variability) mesure une chose contre-intuitive : ton cœur ne bat pas comme un métronome, et c'est très bien. Entre deux battements, l'intervalle varie de quelques millisecondes — 850 ms, puis 910, puis 870. La HRV quantifie ces variations. <em>Plus elles sont grandes, mieux c'est.</em></p>
<p>Pourquoi ? Parce que ces micro-ajustements sont le reflet direct de ton système nerveux autonome. Le système <strong>parasympathique</strong> — celui du repos, de la digestion, de la réparation — freine et relâche le cœur en permanence, ce qui crée de la variabilité. Quand le corps est sous pression (entraînement non digéré, nuit courte, stress, alcool, infection), le système <strong>sympathique</strong> — celui de l'alerte — prend le dessus : le cœur bat plus « droit », et la HRV chute. C'est pour ça qu'elle est au cœur de tous les <a href="/articles/readiness-score-comment-ca-marche.html">scores de préparation</a>.</p>

<h2>Les trois règles pour la lire correctement</h2>
<ul>
<li><strong>Compare-toi à toi, jamais aux autres.</strong> La HRV normale va de 20 à plus de 100 ms selon l'âge, la génétique et le niveau d'entraînement. Ta valeur absolue ne dit presque rien ; son évolution par rapport à ta moyenne des dernières semaines dit presque tout.</li>
<li><strong>Seule compte la mesure dans les mêmes conditions.</strong> La référence, c'est la nuit ou le réveil, au calme. Une mesure prise debout après un café n'est pas comparable.</li>
<li><strong>Raisonne en moyenne sur 7 jours.</strong> La HRV varie naturellement d'un jour à l'autre ; une chute isolée est du bruit, une semaine en baisse est un signal.</li>
</ul>

<h2>Ce qui fait chuter ta HRV</h2>
<p>Les quatre suspects habituels, par ordre de fréquence :</p>
<ul>
<li><strong>L'alcool</strong> — même deux verres le soir peuvent l'écraser pendant une nuit entière, parfois deux (<a href="/articles/alcool-sommeil-effets.html">voici ce que l'alcool fait vraiment à ta nuit</a>).</li>
<li><strong>Une grosse séance non digérée</strong> — c'est normal 24 à 48 h après un effort intense ; c'est le corps qui répare. Si elle reste basse 4-5 jours, tu accumules plus que tu ne récupères — <a href="/articles/surentrainement-signes.html">les signes à surveiller ici</a>.</li>
<li><strong>Le manque de sommeil</strong> et les couchers irréguliers.</li>
<li><strong>Le stress psychologique et la maladie</strong> — la HRV chute souvent 24 à 48 h avant les premiers symptômes d'une infection.</li>
</ul>

<h2>Comment l'améliorer durablement</h2>
<p>Il n'existe aucun hack rapide, mais quatre leviers documentés : le volume et la régularité du sommeil, l'entraînement d'endurance à basse intensité (le levier le plus puissant sur le long terme), la respiration lente en fin de journée, et la sobriété les veilles de jours importants. En quelques mois d'entraînement régulier, la ligne de base monte — c'est l'un des marqueurs les plus fiables d'une condition physique qui progresse.</p>

<h2>Ce qu'il faut retenir</h2>
<ul>
<li>La HRV mesure les variations entre battements : haute = système nerveux détendu, basse = corps sous pression.</li>
<li>Elle se lit contre ta propre ligne de base, en tendance sur plusieurs jours, mesurée la nuit.</li>
<li>Alcool, nuits courtes, charge non digérée et stress sont ses quatre ennemis principaux.</li>
</ul>
""",
    },
    {
        "slug": "proteines-par-jour-prise-de-muscle",
        "cat": "Alimentation",
        "title": "Combien de protéines par jour pour prendre du muscle ?",
        "description": "1,6 à 2,2 g par kilo de poids de corps et par jour : ce que dit la recherche, pourquoi manger plus n'apporte rien, et comment répartir tes apports.",
        "date": "2026-09-19",
        "body": """
<p>La réponse courte : <strong>1,6 à 2,2 g de protéines par kilo de poids de corps et par jour</strong>. Pour quelqu'un de 75 kg, ça fait 120 à 165 g. C'est la fourchette qui ressort des méta-analyses les plus solides : en dessous de 1,6 g/kg, tu laisses de la croissance musculaire sur la table ; au-delà de 2,2 g/kg, les gains supplémentaires deviennent indétectables chez la quasi-totalité des gens.</p>
<p>Oublie les chiffres en grammes absolus (« il faut 150 g de protéines ») : tout se raisonne <em>par kilo de poids de corps</em>. Et oublie le réflexe « plus = mieux » : les protéines au-delà du besoin ne construisent pas plus de muscle, elles sont simplement utilisées comme énergie — une énergie chère et rassasiante, ce qui peut être utile en sèche, mais pas anabolique.</p>

<h2>Les cas où il faut viser plus haut</h2>
<ul>
<li><strong>En déficit calorique (sèche)</strong> : monte à 2,2 – 2,6 g/kg. Quand l'énergie manque, le corps est tenté de puiser dans le muscle ; un apport protéique élevé est ta meilleure assurance anti-fonte, avec l'entraînement lourd et un <a href="/articles/combien-heures-sommeil-par-nuit.html">sommeil suffisant</a> — le manque de sommeil en déficit fait fondre la masse maigre à une vitesse spectaculaire.</li>
<li><strong>Passé 50-60 ans</strong> : la « résistance anabolique » augmente le besoin — vise le haut de la fourchette, et des prises plus généreuses à chaque repas.</li>
<li><strong>Végétarien ou végétal</strong> : vise aussi le haut de la fourchette et varie les sources (légumineuses + céréales + soja) pour couvrir tous les acides aminés essentiels.</li>
</ul>

<h2>La répartition compte (un peu)</h2>
<p>Le total quotidien fait 80 % du travail. Les 20 % restants : répartir en <strong>3 à 5 prises d'environ 0,4 g/kg</strong> (25 à 40 g pour la plupart des gens), chacune apportant assez de leucine pour déclencher la synthèse protéique. La fameuse « fenêtre anabolique » de 30 minutes après la séance est un mythe dans sa version stricte : elle dure plutôt plusieurs heures. Un vrai repas dans les 2-3 heures qui suivent l'entraînement suffit largement.</p>
<p>Un point souvent négligé : <strong>la prise du soir</strong>. 30 à 40 g de protéines lentes (fromage blanc, caséine) avant le coucher améliorent la synthèse protéique nocturne — c'est pendant la nuit que l'essentiel de la réparation se joue.</p>

<h2>Et les reins, alors ?</h2>
<p>Chez une personne en bonne santé, aucune étude sérieuse n'a montré de dommage rénal aux apports dont on parle ici, y compris au-delà de 2,2 g/kg sur des années. La prudence ne s'impose qu'en cas de pathologie rénale existante — dans ce cas, c'est une discussion avec un médecin, pas avec un article.</p>

<h2>Ce qu'il faut retenir</h2>
<ul>
<li><strong>1,6 à 2,2 g/kg/jour</strong> pour construire du muscle ; 2,2 – 2,6 g/kg en sèche.</li>
<li>Le total quotidien d'abord, la répartition ensuite : 3 à 5 prises de ~0,4 g/kg, dont une le soir.</li>
<li>La fenêtre anabolique stricte est un mythe ; la régularité sur des mois est ce qui construit.</li>
</ul>
""",
    },
    {
        "slug": "surentrainement-signes",
        "cat": "Charge",
        "title": "Surentraînement : les signes que tu en fais trop",
        "description": "Performances qui stagnent, sommeil dégradé, cœur de repos qui monte, motivation en berne : les signaux du surentraînement, et comment réagir avant de casser.",
        "date": "2026-09-19",
        "body": """
<p>Le vrai surentraînement — le syndrome médical, celui qui met des mois à se réparer — est rare. Ce qui est fréquent, c'est l'étape d'avant : le <strong>surmenage non compensé</strong>, quand tu empiles les séances plus vite que ton corps ne les digère. La bonne nouvelle : il prévient. La mauvaise : ses signaux ressemblent à de la « baisse de motivation », et beaucoup répondent en s'entraînant <em>plus</em>. C'est exactement l'inverse qu'il faut faire.</p>

<h2>Les signaux qui doivent t'alerter</h2>
<p>Aucun n'est suffisant seul. Trois ou quatre en même temps, pendant plus d'une semaine, oui.</p>
<ul>
<li><strong>Tes performances stagnent ou baissent</strong> malgré un entraînement assidu — le signe cardinal. Mêmes charges plus lourdes à bouger, allures habituelles qui piquent.</li>
<li><strong>Ta fréquence cardiaque se comporte bizarrement</strong> : cœur de repos 5 battements au-dessus de ta normale plusieurs matins de suite, HRV en baisse sur une semaine (<a href="/articles/hrv-variabilite-frequence-cardiaque.html">comment lire ta HRV</a>), ou cardio anormalement haut sur des efforts faciles.</li>
<li><strong>Ton sommeil se dégrade alors que tu es épuisé</strong> — le paradoxe classique du système nerveux trop activé : endormissement difficile, réveils à 4 h du matin.</li>
<li><strong>L'envie disparaît.</strong> Pas la flemme d'un jour : la perte d'appétit pour des séances que tu aimais, l'irritabilité, le moral en pente douce.</li>
<li><strong>Tu tombes malade en boucle</strong> — rhumes à répétition, petite plaie qui traîne, courbatures qui durent 4-5 jours au lieu de 2.</li>
</ul>

<h2>Pourquoi ça arrive (même sans t'entraîner « énormément »)</h2>
<p>Le surmenage n'est pas une question de volume absolu : c'est un déséquilibre entre <strong>la charge que tu imposes et la récupération que tu fournis</strong>. Six séances par semaine avec 8 heures de sommeil, une assiette pleine et peu de stress passent très bien. Quatre séances avec 6 heures de sommeil, un déficit calorique agressif et un travail sous tension suffisent à te mettre dans le rouge. Le stress de la vie compte dans la même colonne que les séances — ton système nerveux ne fait pas la différence.</p>

<h2>Comment réagir — le protocole simple</h2>
<ul>
<li><strong>Semaine 1 : réduis de moitié.</strong> Garde la fréquence si tu y tiens, mais divise volume et intensité par deux. Marche, mobilité, technique légère.</li>
<li><strong>Dors.</strong> Vise le haut de ta fourchette (<a href="/articles/combien-heures-sommeil-par-nuit.html">ton besoin réel est ici</a>), couche-toi plus tôt, garde des horaires fixes.</li>
<li><strong>Mange à ta maintenance</strong>, au minimum. Ce n'est pas la semaine pour un déficit.</li>
<li><strong>Réévalue à J+7</strong> : cœur de repos revenu à la normale, envie de retourner t'entraîner, sommeil réparé → reprends progressivement. Sinon, encore une semaine calme — et si rien ne bouge après 3-4 semaines, consulte.</li>
</ul>

<h2>Ce qu'il faut retenir</h2>
<ul>
<li>Le surmenage prévient : perfs en baisse + vitaux dégradés + sommeil cassé + envie disparue.</li>
<li>La cause n'est jamais « trop de sport » seul : c'est la charge totale (sport + vie) contre ta récupération.</li>
<li>La réponse est toujours la même : moins d'intensité, plus de sommeil, assez de calories — pendant au moins une semaine.</li>
</ul>
""",
    },
    {
        "slug": "combien-seances-sport-par-semaine",
        "cat": "Sport",
        "title": "Combien de séances de sport par semaine pour progresser ?",
        "description": "3 à 5 séances bien récupérées battent 6 séances subies. Ce que dit la recherche sur la fréquence idéale en musculation et en cardio, selon ton niveau.",
        "date": "2026-09-19",
        "body": """
<p>La réponse courte : <strong>3 à 5 séances par semaine</strong> suffisent pour progresser sérieusement — et pour la plupart des gens, 3 séances bien construites et bien récupérées battent 6 séances empilées sur un corps qui ne suit pas. La fréquence n'est pas un objectif en soi : c'est un outil pour distribuer du volume d'entraînement que tu peux <em>digérer</em>.</p>

<h2>En musculation : le volume prime, la fréquence distribue</h2>
<p>La recherche est assez claire : à volume hebdomadaire égal, entraîner un muscle 2 fois par semaine fait mieux qu'une fois ; au-delà, la différence devient marginale. Concrètement :</p>
<ul>
<li><strong>Débutant :</strong> 3 séances full body par semaine, un jour de repos entre chaque. C'est la formule la plus efficace qui existe, et de loin.</li>
<li><strong>Intermédiaire :</strong> 3 à 5 séances, en half body (haut/bas) ou push/pull/legs. Chaque muscle travaillé 2 fois par semaine.</li>
<li><strong>Avancé :</strong> 4 à 6 séances, parce qu'il faut plus de volume pour progresser — pas parce que « plus de jours » serait magique.</li>
</ul>
<p>Un muscle a besoin de 48 à 72 heures pour se réparer après une séance dure. S'entraîner tous les jours est possible ; entraîner <em>la même chose</em> tous les jours ne l'est pas.</p>

<h2>En cardio : la règle du 80/20</h2>
<p>Pour l'endurance, la fréquence peut monter plus haut (le cardio à basse intensité se digère vite), mais la répartition des intensités est décisive : environ <strong>80 % du temps à intensité facile</strong> — tu peux parler en phrases complètes — et 20 % à intensité élevée. C'est la distribution qu'on retrouve chez les athlètes d'endurance à tous les niveaux. L'erreur classique du pratiquant motivé : tout courir « moyennement dur », la zone qui fatigue beaucoup et fait peu progresser.</p>

<h2>Le vrai plafond : ta récupération</h2>
<p>La bonne fréquence n'est pas un chiffre universel, c'est le point d'équilibre entre ta charge et ta vie. Quatre facteurs déplacent ce point : ton <a href="/articles/combien-heures-sommeil-par-nuit.html">sommeil</a>, tes calories, ton stress, et ton historique d'entraînement. Deux repères simples pour savoir si ta fréquence actuelle est la bonne :</p>
<ul>
<li>Tu progresses (charges, allures, répétitions) de semaine en semaine → elle est bonne.</li>
<li>Tu stagnes, tes vitaux se dégradent, l'envie baisse → tu es au-dessus de tes moyens de récupération (<a href="/articles/surentrainement-signes.html">les signes précis ici</a>). Réduis avant d'ajouter.</li>
</ul>

<h2>Ce qu'il faut retenir</h2>
<ul>
<li>3 à 5 séances par semaine couvrent 95 % des objectifs ; chaque muscle 2 fois par semaine en musculation.</li>
<li>En cardio : 80 % facile, 20 % dur — pas tout « moyennement dur ».</li>
<li>La fréquence idéale est celle que ta récupération encaisse en te laissant progresser.</li>
</ul>
""",
    },
    {
        "slug": "se-coucher-meme-heure-regularite",
        "cat": "Régularité",
        "title": "Se coucher à la même heure : ce que ça change vraiment",
        "description": "À durée de sommeil égale, des horaires réguliers améliorent la qualité des nuits, l'énergie et même la santé métabolique. Pourquoi, et comment y arriver.",
        "date": "2026-09-19",
        "body": """
<p>Voici le secret le moins spectaculaire et le plus rentable de tout le sommeil : <strong>te coucher et te lever à la même heure, tous les jours</strong>. À durée égale, un sommeil à horaires réguliers est plus profond, plus continu et plus réparateur qu'un sommeil en horaires anarchiques. Dans plusieurs grandes études récentes, la régularité du sommeil prédit même la santé à long terme <em>mieux que la durée elle-même</em>.</p>

<h2>Pourquoi ton corps y tient autant</h2>
<p>Ton organisme entier tourne sur une horloge circadienne d'environ 24 heures : température, cortisol, mélatonine, digestion, tout est programmé. Quand tu te couches à 22 h 30 en semaine et 2 h le week-end, tu imposes à cette horloge l'équivalent d'un vol Paris–New York tous les vendredis — c'est le <strong>jetlag social</strong>. Résultat : la mélatonine arrive au mauvais moment, l'endormissement traîne le dimanche soir, et le lundi commence en brouillard.</p>
<p>La régularité fait l'inverse : à force de recevoir le signal « on dort à cette heure-là », l'horloge anticipe. La température corporelle baisse avant le coucher, la mélatonine monte au bon moment, et l'endormissement devient presque automatique. C'est aussi l'un des leviers les plus directs pour faire monter un <a href="/articles/readiness-score-comment-ca-marche.html">score de préparation</a> : la HRV nocturne aime les horaires stables.</p>

<h2>L'heure du lever compte plus que celle du coucher</h2>
<p>Contre-intuitif mais central : c'est <strong>le lever qui règle l'horloge</strong>, parce que c'est lui qui fixe l'exposition à la lumière du matin — le signal circadien le plus puissant qui existe. Un lever stable à ±30 minutes, week-end compris, et le coucher finit par se caler tout seul : le soir, le sommeil « appuie » à la bonne heure.</p>

<h2>Comment y arriver sans en faire une prison</h2>
<ul>
<li><strong>Fixe d'abord ton heure de lever</strong>, 7 jours sur 7, à ±30-45 minutes. C'est la seule règle vraiment non négociable.</li>
<li><strong>Compte à rebours pour le coucher</strong> : ton besoin de sommeil (<a href="/articles/combien-heures-sommeil-par-nuit.html">le mesurer ici</a>) + 30 minutes d'endormissement.</li>
<li><strong>Lumière forte le matin, faible le soir</strong> : dehors dans la première heure après le lever, écrans et plafonniers tamisés la dernière heure avant le coucher.</li>
<li><strong>Le week-end, limite la dérive à une heure.</strong> Si tu sors tard, garde quand même un lever proche de l'habituel et fais une sieste courte — la grasse matinée de 3 heures coûte plus qu'elle ne rembourse.</li>
</ul>

<h2>Ce qu'il faut retenir</h2>
<ul>
<li>À durée égale, un sommeil régulier est objectivement plus réparateur — la régularité rivalise avec la durée.</li>
<li>Le lever fixe est la clé : il règle l'horloge via la lumière du matin.</li>
<li>Tolérance raisonnable : ±30-45 minutes en semaine, une heure le week-end.</li>
</ul>
""",
    },
    {
        "slug": "toujours-fatigue-causes",
        "cat": "Énergie",
        "title": "Toujours fatigué ? Les vraies causes d'une fatigue constante",
        "description": "Dette de sommeil invisible, horaires irréguliers, sous-alimentation, surmenage, carences : les causes les plus fréquentes d'une fatigue qui dure, dans l'ordre.",
        "date": "2026-09-19",
        "body": """
<p>« Je dors, mais je suis quand même fatigué. » C'est probablement la phrase qu'on entend le plus dès qu'on parle d'énergie. La fatigue constante a rarement une cause exotique : dans l'immense majorité des cas, c'est l'une des cinq suivantes — et souvent deux ou trois en même temps. Dans l'ordre où il faut les vérifier :</p>

<h2>1. Tu dors moins que tu ne crois</h2>
<p>La cause nº1, de très loin. Le piège classique : confondre temps au lit et temps de sommeil. Sept heures au lit, c'est environ six heures et quart de sommeil réel — répété cinq nuits, c'est une dette de plus de trois heures par semaine, invisible mais bien réelle. Commence par là : <a href="/articles/combien-heures-sommeil-par-nuit.html">mesure ton vrai besoin</a> et compare-le à ce que tu dors réellement, pas à ce que tu vises.</p>

<h2>2. Tu dors à des horaires anarchiques</h2>
<p>À durée égale, un sommeil décalé chaque soir est moins réparateur : l'horloge circadienne passe son temps à courir après tes horaires. Le symptôme typique, c'est la fatigue <em>malgré</em> des nuits « suffisantes » sur le papier — et le brouillard du lundi matin. <a href="/articles/se-coucher-meme-heure-regularite.html">La régularité change plus de choses que tu ne penses</a>.</p>

<h2>3. Tu ne manges pas assez (ou trop mal réparti)</h2>
<p>Fréquent chez les sportifs : un déficit calorique prolongé — volontaire ou pas — finit toujours par se payer en énergie. Le corps réduit la dépense là où il peut : thermogenèse, motivation, libido, tonus général. Signes typiques : frilosité inhabituelle, irritabilité, séances qui deviennent toutes laborieuses, sommeil qui se fragmente. Si tu cumules gros entraînement et petite assiette depuis des semaines, la fatigue n'est pas un mystère, c'est une facture.</p>

<h2>4. Tu en fais trop, tout simplement</h2>
<p>La fatigue qui persiste au réveil, des courbatures qui traînent, un cœur de repos au-dessus de ta normale, l'envie qui s'éteint : c'est le tableau du surmenage — l'entraînement et le stress de vie qui dépassent ta capacité de récupération. <a href="/articles/surentrainement-signes.html">Les signaux précis et le protocole pour en sortir sont ici</a>.</p>

<h2>5. Une cause médicale — à vérifier si le reste est en ordre</h2>
<p>Si tu dors assez, régulièrement, que tu manges à ta faim et que deux semaines calmes n'ont rien changé, c'est le moment d'une prise de sang. Les suspects fréquents et faciles à tester : <strong>carence en fer</strong> (surtout chez les femmes et les coureurs), <strong>vitamine D</strong> (quasi générale en hiver), <strong>thyroïde</strong>, et l'<strong>apnée du sommeil</strong> si tu ronfles et te réveilles la bouche sèche avec des maux de tête. Une fatigue qui dure des mois mérite un médecin, pas un article de blog — celui-ci sert à éliminer les causes évitables avant.</p>

<h2>Ce qu'il faut retenir</h2>
<ul>
<li>Vérifie dans l'ordre : durée réelle de sommeil → régularité → calories → charge totale → bilan médical.</li>
<li>La fatigue « inexpliquée » est presque toujours une dette de sommeil ou un surmenage qui ne dit pas son nom.</li>
<li>Deux semaines de sommeil suffisant et régulier sont le meilleur test diagnostique gratuit qui existe.</li>
</ul>
""",
    },
    {
        "slug": "stress-recuperation-sport",
        "cat": "Humeur",
        "title": "Stress et sport : pourquoi ton corps ne récupère plus",
        "description": "Ton système nerveux ne fait pas la différence entre une semaine de rush et une semaine de gros volume : le stress mental se paie en récupération physique.",
        "date": "2026-09-19",
        "body": """
<p>Tu as déjà vécu ça : une semaine chargée au travail, des nuits correctes, un entraînement pourtant raisonnable — et des jambes en béton, des perfs en berne, une motivation aux fraises. Ce n'est pas dans ta tête. Ou plutôt si, justement : <strong>ton système nerveux ne fait pas la différence entre le stress mental et le stress physique</strong>. Les deux tirent sur la même corde.</p>

<h2>Une seule jauge pour tout</h2>
<p>Le stress psychologique active exactement les mêmes systèmes que l'entraînement : l'axe du cortisol et le système nerveux sympathique — celui de l'alerte. Une deadline, un conflit, des soucis d'argent produisent la même signature physiologique qu'une grosse séance : cortisol élevé, cœur plus haut, <a href="/articles/hrv-variabilite-frequence-cardiaque.html">HRV en baisse</a>, sommeil plus léger. La conséquence pratique est énorme : <em>ta capacité de récupération est un budget unique</em>, dans lequel puisent à la fois tes séances et ta vie. Une semaine de rush professionnel est, pour ton corps, une semaine de gros volume d'entraînement — que tu l'aies choisie ou non.</p>
<p>C'est documenté jusque dans la blessure : les périodes de stress académique ou professionnel élevé multiplient le risque de blessure chez les athlètes, et la cicatrisation elle-même est mesurablement plus lente sous stress chronique.</p>

<h2>Adapter l'entraînement au stress — pas l'inverse</h2>
<p>La conclusion n'est pas « ne t'entraîne pas quand tu es stressé » : l'exercice reste l'un des meilleurs régulateurs du stress qui existent. La conclusion, c'est qu'il faut <strong>moduler l'intensité selon la charge totale</strong>, pas selon le seul programme :</p>
<ul>
<li><strong>Semaine tendue → volume réduit, intensité facile.</strong> Du cardio tranquille et de la technique entretiennent tout et coûtent presque rien au système nerveux. Garde les records pour les semaines calmes.</li>
<li><strong>Regarde tes matins, pas ton planning.</strong> Cœur de repos au-dessus de ta normale, HRV en baisse, réveil difficile plusieurs jours de suite : ton corps a déjà voté, même si « c'est jour de séance dure ».</li>
<li><strong>Protège le sommeil en priorité</strong> — c'est le seul moment où la jauge se recharge vraiment. En période de stress, <a href="/articles/se-coucher-meme-heure-regularite.html">les horaires réguliers</a> comptent double, et l'alcool « pour décompresser » <a href="/articles/alcool-sommeil-effets.html">aggrave précisément ce qu'il prétend soulager</a>.</li>
<li><strong>Ajoute une décharge active</strong> : 10 minutes de marche après les repas, respiration lente le soir (4-6 respirations par minute pendant 5 minutes) — des outils modestes, aux effets mesurables sur la HRV.</li>
</ul>

<h2>Ce qu'il faut retenir</h2>
<ul>
<li>Stress mental et charge d'entraînement puisent dans le même budget de récupération.</li>
<li>En semaine tendue, réduis l'intensité sportive au lieu de l'empiler « pour compenser ».</li>
<li>Tes vitaux du matin reflètent la charge totale — c'est eux qu'il faut écouter, pas le programme.</li>
</ul>
""",
    },
    {
        "slug": "alcool-sommeil-effets",
        "cat": "Contexte",
        "title": "Alcool et sommeil : ce qui se passe vraiment la nuit",
        "description": "L'alcool endort plus vite mais détruit la seconde moitié de la nuit : sommeil paradoxal amputé, réveils, HRV écrasée. Ce que montrent les données, verre par verre.",
        "date": "2026-09-19",
        "body": """
<p>L'alcool est le somnifère le plus utilisé du monde — et l'un des pires. Le paradoxe est bien connu : un ou deux verres <strong>aident réellement à s'endormir</strong> (l'alcool est sédatif), et pourtant la nuit qui suit est objectivement moins réparatrice. Ce n'est pas une impression de lendemain : c'est l'un des effets les plus visibles qui soient dans les données de sommeil.</p>

<h2>Le marché de dupes, heure par heure</h2>
<p>La soirée se passe en deux actes :</p>
<ul>
<li><strong>Première moitié de nuit :</strong> endormissement rapide, sommeil profond parfois même augmenté. Tout va bien en apparence.</li>
<li><strong>Seconde moitié :</strong> le corps a métabolisé l'alcool, et l'effet rebond arrive — système nerveux en alerte, sommeil léger et fragmenté, réveils multiples (souvent vers 3-4 h du matin), soif, chaleur. Le <strong>sommeil paradoxal</strong> (REM), concentré en fin de nuit, est le grand sacrifié : c'est lui qui gère la mémoire et la régulation émotionnelle. Résultat au réveil : le compte d'heures semble correct, la tête dit le contraire.</li>
</ul>

<h2>Ce que voient les capteurs</h2>
<p>Sur les données physiologiques, l'alcool du soir laisse une signature immanquable, proportionnelle à la dose : <strong>fréquence cardiaque nocturne en hausse</strong> de plusieurs battements, <a href="/articles/hrv-variabilite-frequence-cardiaque.html"><strong>HRV écrasée</strong></a> toute la nuit, température plus haute, et un <a href="/articles/readiness-score-comment-ca-marche.html">score de préparation</a> qui plonge au matin. Les études sur données de bracelets sont convergentes : même une consommation modérée dégrade mesurablement la qualité de la nuit, et une consommation forte peut se lire encore la nuit <em>suivante</em>.</p>

<h2>Limiter les dégâts sans devenir moine</h2>
<p>La dose fait tout, et le <em>moment</em> presque autant :</p>
<ul>
<li><strong>L'heure compte :</strong> le corps élimine environ un verre standard par heure. Deux verres finis à 19 h sont largement métabolisés au coucher ; les mêmes à 23 h occupent la moitié de ta nuit.</li>
<li><strong>La règle simple :</strong> plus tôt, moins, avec de l'eau et de la nourriture. Un verre au dîner est presque neutre ; trois verres tard, jamais.</li>
<li><strong>Choisis tes soirs :</strong> évite l'alcool tardif les veilles de grosse séance ou de journée importante — c'est précisément là que la nuit vaut cher.</li>
<li><strong>Ne « rembourse » pas en grasse matinée</strong> le lendemain : tu ajouterais du <a href="/articles/se-coucher-meme-heure-regularite.html">jetlag social</a> à la note. Lever habituel, sieste courte si besoin.</li>
</ul>

<h2>Ce qu'il faut retenir</h2>
<ul>
<li>L'alcool endort plus vite mais casse la seconde moitié de la nuit — surtout le sommeil paradoxal.</li>
<li>Cœur plus haut, HRV écrasée : la nuit alcoolisée se voit dans les données, dose par dose.</li>
<li>Les deux leviers : la quantité, et surtout l'heure. Tôt et léger change presque tout.</li>
</ul>
""",
    },
]

DOMAINS = ["Sommeil", "Readiness", "Sport", "Récupération", "Alimentation",
           "Charge", "Régularité", "Humeur", "Contexte", "Énergie"]

# ---------------------------------------------------------------------------

CSS = """:root{--gold:#D9A441;--gold-soft:#B07A2A;--ink:#F2EBDD;--muted:#9A8E77;--bg:#0B0A08;--card:#12100C;--line:rgba(242,235,221,.14);color-scheme:dark}
*{box-sizing:border-box;margin:0;padding:0}
body{font-family:-apple-system,BlinkMacSystemFont,"Segoe UI",sans-serif;background:var(--bg);color:var(--ink);line-height:1.75;font-weight:400;-webkit-font-smoothing:antialiased}
a{color:inherit}
.wrap{max-width:640px;margin:0 auto;padding:0 24px}
.wrap-wide{max-width:1080px;margin:0 auto;padding:0 24px}
.label{font-size:11px;letter-spacing:.35em;text-transform:uppercase;color:var(--muted);font-weight:400}
.label .gold{color:var(--gold)}
nav.site{display:flex;align-items:center;justify-content:space-between;max-width:1080px;margin:0 auto;padding:28px 24px}
nav.site .logo{font-size:16px;letter-spacing:.45em;text-transform:uppercase;color:var(--ink);font-weight:300;text-decoration:none}
nav.site .links{display:flex;gap:26px;font-size:11px;letter-spacing:.22em;text-transform:uppercase}
nav.site .links a{color:var(--muted);text-decoration:none;font-weight:400}
nav.site .links a.on{color:var(--ink)}
nav.site .links a:hover{color:var(--gold)}
@media(max-width:560px){nav.site{flex-direction:column;align-items:flex-start;gap:16px;padding:22px 24px}nav.site .links{gap:14px;font-size:10px;letter-spacing:.16em;flex-wrap:wrap}nav.site .logo{font-size:13px;letter-spacing:.35em}}
.display{font-weight:200;text-transform:uppercase;letter-spacing:-.01em;line-height:1.02}
.display .gold{color:var(--gold)}
.display .dim{color:var(--muted)}
.btn{display:inline-block;border:1px solid var(--line);color:var(--ink);text-decoration:none;
     padding:17px 36px;font-size:11.5px;font-weight:400;letter-spacing:.25em;text-transform:uppercase;
     transition:border-color .25s,color .25s;background:none;cursor:pointer}
.btn:hover{border-color:var(--gold);color:var(--gold)}
.btn.gold{border-color:var(--gold);color:var(--gold)}
.btn.gold:hover{background:var(--gold);color:#1C1710}
.hr{border:0;border-top:1px solid var(--line)}
/* ARTICLE */
article header{padding:64px 0 28px}
article header .label{display:block;margin-bottom:22px}
article h1{font-size:clamp(28px,5.4vw,44px);font-weight:200;text-transform:uppercase;letter-spacing:-.01em;line-height:1.08}
article .standfirst{color:var(--muted);font-size:16px;margin-top:20px;line-height:1.7}
article h2{font-size:13px;letter-spacing:.22em;text-transform:uppercase;font-weight:500;color:var(--gold);margin:52px 0 16px;padding-top:26px;position:relative}
article h2::before{content:"";position:absolute;top:0;left:6%;right:6%;border-top:1px solid var(--line)}
article p{margin:0 0 18px;font-size:16.5px;color:var(--ink);line-height:1.8}
article ul{margin:0 0 18px 22px}
article li{margin-bottom:11px;font-size:16.5px;line-height:1.75}
article li::marker{color:var(--gold)}
article strong{font-weight:600}
article em{color:var(--gold);font-style:normal}
article h1 .w{display:inline-block;white-space:nowrap}
article h1 .ch{display:inline-block;opacity:0;transform:translateY(.05em);transition:opacity .5s ease-out,transform .5s ease-out}
article h1 .ch.in{opacity:1;transform:none}
@media (prefers-reduced-motion:reduce){article h1 .ch{opacity:1;transform:none;transition:none}}
article .hero{margin:40px 0 10px}
article .hero img{width:100%;height:auto;display:block;border:1px solid var(--line);filter:saturate(.85) brightness(.92)}
/* fin d'article : la beta comme recompense */
.reward{margin:64px 0 8px;padding:52px 0;text-align:center;position:relative}
.reward::before{content:"";position:absolute;top:0;left:6%;right:6%;border-top:1px solid var(--line)}
.reward::after{content:"";position:absolute;bottom:0;left:6%;right:6%;border-top:1px solid var(--line)}
.reward.noafter::after{content:none}
.reward .label{display:block;margin-bottom:20px}
.reward h2{font-size:clamp(20px,3.6vw,28px);font-weight:200;text-transform:uppercase;letter-spacing:0;color:var(--ink);margin:0 0 14px;line-height:1.2}
.reward p{color:var(--muted);font-size:15px;max-width:420px;margin:0 auto 28px}
.next{padding:40px 0 8px}
.next .label{display:block;margin-bottom:18px}
.next a{display:block;text-decoration:none;padding:16px 0;font-weight:300;position:relative;
        font-size:16px;text-transform:uppercase;letter-spacing:.02em;color:var(--ink)}
.next a::after{content:"";position:absolute;bottom:0;left:6%;right:6%;border-top:1px solid var(--line)}
.next a:first-of-type::before{content:"";position:absolute;top:0;left:6%;right:6%;border-top:1px solid var(--line)}
.next a:hover{color:var(--gold)}
/* INDEX ARTICLES : liste editoriale */
.pagehead{padding:72px 0 24px}
.pagehead h1{font-size:clamp(34px,7vw,60px)}
.pagehead p{color:var(--muted);margin-top:22px;font-size:16px;max-width:480px}
.journal{margin:92px 0 0}
/* filets a 88 % de la largeur, centres (comme le cadre Derniers repas de l'app) */
.journal a.entry{display:flex;gap:32px;align-items:center;justify-content:space-between;text-decoration:none;padding:60px 0;position:relative}
.journal a.entry::before{content:"";position:absolute;top:0;left:6%;right:6%;border-top:1px solid var(--line)}
.journal a.entry:last-child::after{content:"";position:absolute;bottom:0;left:6%;right:6%;border-top:1px solid var(--line)}
.entry .etext{flex:1;min-width:0}
.entry .ethumb{flex:0 0 210px}
.entry .ethumb img{width:100%;aspect-ratio:1.9;object-fit:cover;display:block;border:1px solid var(--line);filter:saturate(.85) brightness(.9);transition:filter .25s}
.journal a.entry:hover .ethumb img{filter:saturate(1) brightness(1)}
@media(max-width:640px){.journal a.entry{flex-direction:column-reverse;align-items:stretch;gap:18px}.entry .ethumb{flex:none}}
.journal .label{display:block;margin-bottom:12px}
.journal h2{font-size:clamp(19px,3.4vw,25px);font-weight:250;text-transform:uppercase;letter-spacing:.01em;color:var(--ink);line-height:1.25;transition:color .2s}
.journal a.entry:hover h2{color:var(--gold)}
.journal p.desc{color:var(--muted);font-size:14.5px;margin-top:10px;max-width:540px}
footer.site{border-top:1px solid var(--line);margin-top:96px;padding:40px 0 64px;text-align:center}
footer.site .flinks{font-size:11px;letter-spacing:.22em;text-transform:uppercase}
footer.site a{color:var(--muted);text-decoration:none}
footer.site a:hover{color:var(--gold)}
.disclaimer{max-width:520px;margin:22px auto 0;color:var(--muted);font-size:12.5px;line-height:1.7}
/* JOURNAL : compteurs, themes, citation */
.stats{display:flex;gap:56px;margin:44px 0 10px}
.stats .n{font-size:clamp(30px,5vw,44px);font-weight:200;line-height:1}
.stats .l{display:block;margin-top:10px}
.themes{margin:40px 0 8px}
.themes .label{display:block;margin-bottom:16px}
.themescroll{border:1px solid var(--line);max-height:264px;overflow-y:auto;overscroll-behavior:contain;
             scrollbar-width:thin;scrollbar-color:rgba(154,142,119,.4) transparent}
.themescroll::-webkit-scrollbar{width:4px}
.themescroll::-webkit-scrollbar-thumb{background:rgba(154,142,119,.4)}
.theme{display:flex;justify-content:space-between;align-items:center;width:100%;text-align:left;
       background:none;border:0;border-left:2px solid rgba(154,142,119,.45);color:var(--muted);
       height:52px;padding:0 18px;font-size:11.5px;letter-spacing:.25em;text-transform:uppercase;
       cursor:pointer;transition:color .2s,border-color .2s;font-family:inherit}
.theme{position:relative}
.theme+.theme::after{content:"";position:absolute;top:0;left:6%;right:6%;border-top:1px solid var(--line)}
.theme .count{font-size:13px;letter-spacing:0;font-weight:300}
.theme:hover{color:var(--ink)}
.theme.on{color:var(--ink);border-left-color:var(--gold)}
.quote{margin:54px 0 10px;text-align:left}
.quote p{font-size:clamp(17px,2.8vw,21px);font-weight:300;font-style:italic;color:var(--ink)}
.quote .label{display:block;margin-top:14px}
.entry .meta{display:block;margin-bottom:12px}
.entry .readmore{display:inline-block;margin-top:14px;font-size:10.5px;letter-spacing:.28em;text-transform:uppercase;color:var(--gold)}
.empty{border-top:1px solid var(--line);border-bottom:1px solid var(--line);padding:56px 0;text-align:center;color:var(--muted);font-size:15px}
"""

POSTHOG = """<script>
  var POSTHOG_KEY="%s";
  if(POSTHOG_KEY){!function(t,e){var o,n,p,r;e.__SV||(window.posthog=e,e._i=[],e.init=function(i,s,a){function g(t,e){var o=e.split(".");2==o.length&&(t=t[o[0]],e=o[1]),t[e]=function(){t.push([e].concat(Array.prototype.slice.call(arguments,0)))}}(p=t.createElement("script")).type="text/javascript",p.async=!0,p.src=s.api_host+"/static/array.js",(r=t.getElementsByTagName("script")[0]).parentNode.insertBefore(p,r);var u=e;for(void 0!==a?u=e[a]=[]:a="posthog",u.people=u.people||[],u.toString=function(t){var e="posthog";return"posthog"!==a&&(e+="."+a),t||(e+=" (stub)"),e},u.people.toString=function(){return u.toString(1)+".people (stub)"},o="capture identify alias people.set people.set_once set_config register register_once unregister opt_out_capturing has_opted_out_capturing opt_in_capturing reset".split(" "),n=0;n<o.length;n++)g(u,o[n]);e._i.push([i,s,a])},e.__SV=1)}(document,window.posthog||[]);posthog.init(POSTHOG_KEY,{api_host:"https://eu.i.posthog.com"});}
  function track(ev,props){if(window.posthog&&POSTHOG_KEY)posthog.capture(ev,props||{});}
</script>""" % POSTHOG_KEY

NAV = """<nav class="site">
  <a class="logo" href="/">Ecleptic</a>
  <div class="links">
    <a href="/" %(on_home)s>Accueil</a>
    <a href="/articles/" %(on_articles)s>Journal</a>
    <a href="/guide.html">Guide</a>
    <a href="/science.html">Science-Based</a>
    <a href="/beta.html">La b&ecirc;ta</a>
  </div>
</nav>"""

FOOTER = """<footer class="site">
  <div class="wrap">
    <p class="flinks"><a href="/confidentialite.html">Confidentialit&eacute;</a> &nbsp;&middot;&nbsp; <a href="mailto:contact@ecleptic.app">Contact</a> &nbsp;&middot;&nbsp; <a href="/beta.html">La b&ecirc;ta</a></p>
    <p class="disclaimer">Ecleptic est une application de bien-&ecirc;tre. Ses contenus ne remplacent pas un avis m&eacute;dical et ne constituent pas un dispositif m&eacute;dical.</p>
  </div>
</footer>"""


def nav(section):
    return NAV % {
        "on_home": 'class="on"' if section == "home" else "",
        "on_articles": 'class="on"' if section == "articles" else "",
    }


def cat(a):
    return a.get("cat", "Journal")


MONTHS_FR = ["janvier", "février", "mars", "avril", "mai", "juin", "juillet",
             "août", "septembre", "octobre", "novembre", "décembre"]


def fr_date(iso):
    y, m, d = iso.split("-")
    return "%d %s %s" % (int(d), MONTHS_FR[int(m) - 1], y)


def img_path(a):
    """Chemin web de l'image de l'article, ou None si elle n'existe pas.
    Convention : assets/articles/<slug>.jpg (1600x840)."""
    root = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    rel = "assets/articles/%s.jpg" % a["slug"]
    return "/" + rel if os.path.exists(os.path.join(root, rel)) else None


def read_min(a):
    import re
    words = len(re.sub(r"<[^>]+>", " ", a["body"]).split())
    return max(2, round(words / 220))


def article_page(a, others):
    url = "%s/articles/%s.html" % (SITE, a["slug"])
    more = "\n".join(
        '<a href="/articles/%s.html">%s</a>' % (o["slug"], html.escape(o["title"]))
        for o in others[:3]
    )
    img = img_path(a)
    og_image = ('\n<meta property="og:image" content="%s%s">\n'
                '<meta name="twitter:card" content="summary_large_image">\n'
                '<meta name="twitter:image" content="%s%s">' % (SITE, img, SITE, img)) if img else ""
    hero = ('\n  <figure class="hero"><img src="%s" alt="%s" width="1600" height="840"></figure>'
            % (img, html.escape(a["title"], quote=True))) if img else ""
    # Titres-questions : apparition caractère par caractère, même animation que
    # « s'aligne. » sur l'accueil (délais en i², 100→1100 ms, translateY .05em).
    # Script inline juste après le header = anti-flash (split avant le 1er paint).
    reveal = """
<script>
(function(){
  var h = document.querySelector('article h1');
  if (!h) return;
  var reduce = window.matchMedia && window.matchMedia('(prefers-reduced-motion: reduce)').matches;
  var BASE = 100, SPREAD = 1000, P = 2;
  var text = h.textContent.replace(/ ([?!:;\\u00bb])/g, '\\u00a0$1');
  var letters = Array.from(text);
  var denom = Math.max(1, letters.length - 1);
  h.setAttribute('aria-label', text);
  h.textContent = '';
  var spans = [], w = null, idx = 0;
  letters.forEach(function(c){
    if (c === ' '){ h.appendChild(document.createTextNode(' ')); w = null; idx++; return; }
    if (!w){ w = document.createElement('span'); w.className = 'w'; w.setAttribute('aria-hidden','true'); h.appendChild(w); }
    var s = document.createElement('span');
    s.className = 'ch';
    s.textContent = c;
    if (!reduce) s.style.transitionDelay = (BASE + SPREAD*Math.pow(idx/denom, P)).toFixed(0)+'ms';
    idx++; w.appendChild(s); spans.push(s);
  });
  if (reduce){ spans.forEach(function(s){ s.classList.add('in'); }); return; }
  requestAnimationFrame(function(){ requestAnimationFrame(function(){
    spans.forEach(function(s){ s.classList.add('in'); });
  });});
})();
</script>""" if "?" in a["title"] else ""
    jsonld_img = '"image":"%s%s",' % (SITE, img) if img else ""
    jsonld = (
        '{"@context":"https://schema.org","@type":"Article","headline":%s,'
        '"description":%s,%s"datePublished":"%s","inLanguage":"fr",'
        '"author":{"@type":"Organization","name":"Ecleptic","url":"%s"},'
        '"publisher":{"@type":"Organization","name":"Ecleptic","url":"%s"},'
        '"mainEntityOfPage":"%s"}'
    ) % (
        __import__("json").dumps(a["title"], ensure_ascii=False),
        __import__("json").dumps(a["description"], ensure_ascii=False),
        jsonld_img, a["date"], SITE, SITE, url,
    )
    return """<!doctype html>
<html lang="fr">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>%(title)s — Ecleptic</title>
<meta name="description" content="%(desc)s">
<link rel="canonical" href="%(url)s">
<meta property="og:title" content="%(title)s">
<meta property="og:description" content="%(desc)s">
<meta property="og:type" content="article">
<meta property="og:url" content="%(url)s">%(og_image)s
<script type="application/ld+json">%(jsonld)s</script>
<link rel="stylesheet" href="/assets/site.css">
</head>
<body>
%(nav)s
<main class="wrap">
<article>
  <header>
    <span class="label"><span class="gold">%(cat)s</span> &nbsp;&middot;&nbsp; %(date)s &nbsp;&middot;&nbsp; %(mins)s min</span>
    <h1>%(title)s</h1>
    <p class="standfirst">%(desc)s</p>
  </header>%(reveal)s%(hero)s
  %(body)s
  <div class="reward">
    <span class="label">Pour aller plus loin</span>
    <h2>Ce que cet article explique,<br>l'app le mesure chez toi.</h2>
    <p>Ecleptic croise ton sommeil, ton alimentation et ton entraînement en un seul score, chaque matin. La bêta iOS est ouverte à un petit cercle.</p>
    <a class="btn gold" href="/beta.html" onclick="track('article_cta_click',{article:'%(slug)s'})">Demander l'accès</a>
  </div>
  <div class="next">
    <span class="label">À lire ensuite</span>
%(more)s
  </div>
</article>
</main>
%(footer)s
%(posthog)s
<script>track('article_view',{article:'%(slug)s'});</script>
</body>
</html>
""" % {
        "title": html.escape(a["title"]), "desc": html.escape(a["description"], quote=True),
        "url": url, "jsonld": jsonld, "og_image": og_image, "hero": hero, "reveal": reveal,
        "nav": nav("articles"), "date": fr_date(a["date"]),
        "cat": html.escape(cat(a)), "mins": read_min(a),
        "body": a["body"].strip(), "tf": TF_LINK, "slug": a["slug"], "more": more,
        "footer": FOOTER, "posthog": POSTHOG,
    }


def index_page():
    def card(a):
        img = img_path(a)
        thumb = ('\n  <span class="ethumb"><img src="%s" alt="" loading="lazy"></span>'
                 % img) if img else ""
        return """<a class="entry" href="/articles/%s.html" data-cat="%s">
  <span class="etext">
  <span class="label meta"><span class="gold">%s</span> &nbsp;&middot;&nbsp; %s &nbsp;&middot;&nbsp; %s min</span>
  <h2>%s</h2>
  <p class="desc">%s</p>
  <span class="readmore">Lire l'article →</span>
  </span>%s
</a>""" % (a["slug"], html.escape(cat(a)), html.escape(cat(a)), fr_date(a["date"]),
           read_min(a), html.escape(a["title"]), html.escape(a["description"]), thumb)

    cards = "\n".join(card(a) for a in sorted(ARTICLES, key=lambda x: x["date"], reverse=True))
    counts = {d: sum(1 for a in ARTICLES if cat(a) == d) for d in DOMAINS}
    themes = "\n".join(
        """<button class="theme" data-filter="%s"><span>%s</span><span class="count">%d</span></button>"""
        % (html.escape(d), html.escape(d), counts[d])
        for d in DOMAINS
    )
    empty = "" if ARTICLES else """<div class="empty">Les premiers textes sont en préparation.<br>La station ouvre bientôt son journal.</div>"""
    return """<!doctype html>
<html lang="fr">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>Le Journal de la station spatiale — Ecleptic</title>
<meta name="description" content="Sommeil, nutrition, entraînement, récupération : des articles courts, scientifiques et actionnables pour optimiser ta santé au quotidien.">
<link rel="canonical" href="%(site)s/articles/">
<meta property="og:title" content="Le Journal de la station spatiale — Ecleptic">
<meta property="og:description" content="Sommeil, nutrition, entraînement, récupération : des conseils scientifiques et actionnables.">
<meta property="og:type" content="website">
<link rel="stylesheet" href="/assets/site.css">
</head>
<body>
%(nav)s
<main class="wrap">
  <div class="pagehead">
    <span class="label">Journal de la station spatiale</span>
    <h1 class="display" style="margin-top:22px">Des jours<br>autrement<br><span class="gold">pensés</span>.</h1>
    <p>Des textes sur le sommeil, l'alimentation, l'entraînement et l'art de construire des journées qui méritent d'être vécues.</p>
    <div class="stats">
      <div><span class="n">%(narticles)d</span><span class="l label">Articles</span></div>
      <div><span class="n">%(nthemes)d</span><span class="l label">Thèmes</span></div>
    </div>
  </div>
  <div class="themes">
    <span class="label">Thèmes du journal</span>
    <div class="themescroll">
    <button class="theme on" data-filter="*"><span>Tout le journal</span><span class="count">%(narticles)d</span></button>
%(themes)s
    </div>
  </div>
  <div class="quote">
    <p>« Chaque décision que tu prends — de ce que tu manges à ce que tu fais de ta soirée — fait de toi qui tu seras demain. »</p>
    <span class="label">Chris Hadfield &nbsp;·&nbsp; Astronaute, commandant de l'ISS</span>
  </div>
  <div class="journal" id="entries">
%(cards)s
  </div>
%(empty)s
  <div class="reward noafter">
    <span class="label">Et ensuite</span>
    <h2>Lire, c'est bien.<br>Mesurer, c'est mieux.</h2>
    <p>Tout ce que le journal explique, l'app le suit automatiquement, sur tes propres données. La bêta iOS est ouverte à un petit cercle.</p>
    <a class="btn gold" href="/beta.html" onclick="track('article_cta_click',{article:'index'})">Demander l'accès</a>
  </div>
</main>
%(footer)s
%(posthog)s
<script>
track('articles_index_view');
(function(){
  var btns = document.querySelectorAll('.theme');
  var entries = document.querySelectorAll('#entries .entry');
  btns.forEach(function(b){
    b.addEventListener('click', function(){
      btns.forEach(function(x){ x.classList.remove('on'); });
      b.classList.add('on');
      var f = b.getAttribute('data-filter');
      entries.forEach(function(e){
        e.style.display = (f === '*' || e.getAttribute('data-cat') === f) ? '' : 'none';
      });
      track('journal_theme_click', {theme: f});
    });
  });
})();
</script>
</body>
</html>
""" % {"site": SITE, "nav": nav("articles"), "cards": cards, "themes": themes,
       "empty": empty, "narticles": len(ARTICLES), "nthemes": len(DOMAINS),
       "footer": FOOTER, "posthog": POSTHOG}


def sitemap():
    urls = ["%s/" % SITE, "%s/beta.html" % SITE, "%s/guide.html" % SITE,
            "%s/science.html" % SITE, "%s/articles/" % SITE]
    urls += ["%s/articles/%s.html" % (SITE, a["slug"]) for a in ARTICLES]
    items = "\n".join("  <url><loc>%s</loc></url>" % u for u in urls)
    return '<?xml version="1.0" encoding="UTF-8"?>\n<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">\n%s\n</urlset>\n' % items


def main():
    root = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    os.makedirs(os.path.join(root, "articles"), exist_ok=True)
    os.makedirs(os.path.join(root, "assets"), exist_ok=True)
    with open(os.path.join(root, "assets", "site.css"), "w") as f:
        f.write(CSS)
    for i, a in enumerate(ARTICLES):
        others = ARTICLES[i + 1:] + ARTICLES[:i]
        with open(os.path.join(root, "articles", a["slug"] + ".html"), "w") as f:
            f.write(article_page(a, others))
    with open(os.path.join(root, "articles", "index.html"), "w") as f:
        f.write(index_page())
    with open(os.path.join(root, "sitemap.xml"), "w") as f:
        f.write(sitemap())
    print("OK — %d articles + index + sitemap + css" % len(ARTICLES))


if __name__ == "__main__":
    main()
