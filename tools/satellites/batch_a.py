# -*- coding: utf-8 -*-
# Lot A de satellites longue traîne — catégorie Alimentation.
# Chargé automatiquement par build_articles.py (_load_satellites).

ENTRIES = [
    {
        "slug": "combien-de-calories-par-jour",
        "cat": "Alimentation",
        "title": "Combien de calories par jour faut-il vraiment ?",
        "description": "Combien de calories par jour ? Ça dépend de ton métabolisme et de ton activité. Ordres de grandeur, limites des formules, et comment trouver ton vrai chiffre.",
        "date": "2026-09-06",
        "updated": "2026-09-30",
        "body": """
<p>La réponse courte : <strong>ça dépend de toi</strong>. Ta dépense énergétique quotidienne — le fameux <em>TDEE</em>, pour <strong>total daily energy expenditure</strong> — additionne ton métabolisme de base (ce que ton corps brûle au repos, juste pour rester en vie) et tout ce que tu bouges dans la journée. En ordre de grandeur, ça donne à peu près <strong>1 800 à 2 400 kcal</strong> pour une femme et <strong>2 200 à 2 900 kcal</strong> pour un homme, de sédentaire à actif, selon les repères de l'Autorité européenne de sécurité des aliments (EFSA) — mais ces fourchettes sont larges, et deux personnes du même poids peuvent avoir 500 kcal d'écart.</p>
<p>Le vrai message : il n'existe pas de « bon » chiffre universel. Ton besoin dépend de ta taille, de ton poids, de ta masse musculaire, de ton âge et surtout de à quel point tu es actif — pas seulement à la salle, mais toute la journée. La bonne nouvelle, c'est que tu n'as pas besoin de le deviner parfaitement : tu pars d'une estimation correcte, puis tu laisses la réalité corriger le tir.</p>

<h2>De quoi ta dépense est faite</h2>
<p>Quatre postes, très inégaux :</p>
<ul>
<li><strong>Le métabolisme de base (60-70 %)</strong> — l'énergie que brûlent ton cerveau, ton cœur, ton foie et tes muscles au repos. C'est le gros morceau, et il dépend surtout de ta masse maigre.</li>
<li><strong>L'activité de fond, ou NEAT (15-30 %)</strong> — marcher, tenir debout, gesticuler, monter les escaliers. C'est le poste le plus variable d'une personne à l'autre, et celui qui explique le plus les différences.</li>
<li><strong>Le sport (5-15 %)</strong> — souvent surestimé. Une grosse séance, c'est 300 à 600 kcal, pas 1 500.</li>
<li><strong>La digestion (~10 %)</strong> — l'énergie dépensée pour assimiler ce que tu manges : 5 à 15 % de la dépense selon une revue de 2004, un peu plus quand l'assiette est riche en protéines.</li>
</ul>

<h2>Les formules : un point de départ, pas une vérité</h2>
<p>La plus fiable est celle de <strong>Mifflin-St Jeor</strong> : une revue systématique de 2005 a montré que c'est elle qui tombe le plus souvent à moins de 10 % du métabolisme mesuré. Pour un homme : 10 × poids(kg) + 6,25 × taille(cm) − 5 × âge + 5 ; pour une femme, le même calcul avec −161 à la fin. Tu obtiens ton métabolisme de base, que tu multiplies ensuite par un facteur d'activité : de 1,4 si tu es sédentaire à 2 si tu es très actif, selon l'EFSA.</p>
<div class="tablewrap"><table>
<caption>Source : EFSA (2013), besoins énergétiques moyens des adultes de 30 à 39 ans (IMC de 22), convertis en kcal.</caption>
<thead><tr><th>Niveau d'activité</th><th class="n">Femme</th><th class="n">Homme</th></tr></thead>
<tbody>
<tr><td>Sédentaire (1,4)</td><td class="n">1 820 kcal</td><td class="n">2 270 kcal</td></tr>
<tr><td>Modérément actif (1,6)</td><td class="n">2 080 kcal</td><td class="n">2 580 kcal</td></tr>
<tr><td>Actif (1,8)</td><td class="n">2 340 kcal</td><td class="n">2 910 kcal</td></tr>
<tr><td>Très actif (2,0)</td><td class="n">2 580 kcal</td><td class="n">3 220 kcal</td></tr>
</tbody>
</table></div>
<p>Un exemple concret : un homme de 75 kg, 178 cm, 30 ans obtient un métabolisme de base d'environ <strong>1 720 kcal</strong>. En s'entraînant trois ou quatre fois par semaine (facteur ~1,5), sa dépense totale tourne autour de <strong>2 580 kcal</strong>. Mais retiens bien : c'est une <em>estimation</em>. Les formules peuvent se tromper de 200 à 300 kcal dans un sens ou dans l'autre, parce qu'elles ne connaissent ni ta masse musculaire réelle ni ton niveau d'agitation.</p>

<h2>La seule méthode qui ne ment pas : la balance sur 2-3 semaines</h2>
<p>Voilà comment transformer l'estimation en chiffre fiable :</p>
<ul>
<li>Mange à peu près à ta dépense estimée pendant <strong>2 à 3 semaines</strong>, sans chercher à maigrir ni à grossir.</li>
<li>Pèse-toi le matin à jeun, et ne regarde que la <strong>moyenne hebdomadaire</strong> — le poids d'un seul jour ne veut rien dire (eau, sel, digestion).</li>
<li>Poids stable → tu as trouvé ta maintenance. Poids qui monte → ta vraie dépense est plus basse. Poids qui descend → elle est plus haute. Ajuste de 150-200 kcal et recommence.</li>
</ul>
<p>C'est exactement cette logique qui sert de base quand on veut <a href="/articles/deficit-calorique-comment-calculer.html">calculer un déficit calorique</a> proprement : on part de la dépense réelle, pas d'un chiffre théorique.</p>

<h2>Ce qui déplace ton chiffre</h2>
<ul>
<li><strong>Ta masse musculaire.</strong> Plus tu as de muscle, plus ton métabolisme de base est haut, même au repos — un des intérêts long terme de la musculation, et une raison de <a href="/articles/proteines-par-jour-prise-de-muscle.html">manger assez de protéines</a>.</li>
<li><strong>Ton activité de fond.</strong> Dans une étude publiée dans <em>Science</em> (2005), des personnes en surpoids restaient assises 2 heures de plus par jour que des personnes minces : environ 350 kcal de dépense en moins par jour. <a href="/articles/combien-de-pas-par-jour.html">Le nombre de pas quotidiens</a> pèse souvent plus lourd que la séance elle-même.</li>
<li><strong>L'âge.</strong> Moins qu'on ne le croit : selon une vaste étude publiée dans <em>Science</em> (2021), à masse maigre égale, la dépense reste stable de 20 à 60 ans et ne recule qu'ensuite. Ce qui baisse avant, c'est surtout le muscle et le mouvement — deux choses en partie sous ton contrôle.</li>
<li><strong>Le sommeil et le stress.</strong> Mal dormir dérègle l'appétit et l'activité spontanée, ce qui brouille le calcul sur les bords.</li>
</ul>

<h2>Ce qu'il faut retenir</h2>
<ul>
<li>Ta dépense = métabolisme de base + activité ; en ordre de grandeur, ~1 800-2 400 kcal (femme) et ~2 200-2 900 kcal (homme), très variables.</li>
<li>Les formules type Mifflin-St Jeor donnent un point de départ à ±200-300 kcal, pas une vérité.</li>
<li>La seule méthode fiable : manger à l'estimation, suivre la moyenne de poids sur 2-3 semaines, ajuster.</li>
</ul>
""",
        "faq": [
            {"q": "Combien de calories par jour pour une femme ?",
             "a": "En ordre de grandeur, 1 800 à 2 400 kcal par jour pour maintenir son poids, selon la taille, la masse musculaire, l'âge et surtout le niveau d'activité. La fourchette est large : le seul moyen fiable de trouver son chiffre est de suivre son poids sur deux à trois semaines."},
            {"q": "Comment calculer ses besoins caloriques ?",
             "a": "Estime ton métabolisme de base avec la formule de Mifflin-St Jeor, multiplie par un facteur d'activité (de 1,4 si tu es sédentaire à 2 si tu es très actif, selon l'EFSA), puis vérifie en suivant la moyenne de ton poids sur 2-3 semaines. L'estimation peut se tromper de 200 à 300 kcal ; la balance tranche."},
            {"q": "Combien de calories pour perdre du poids ?",
             "a": "Retire 300 à 500 kcal à ta dépense totale, ce qui fait perdre environ 0,3 à 0,5 kg par semaine au début. Pars toujours de ta dépense réelle, pas d'un chiffre standard."},
        ],
        "sources": [
            {"t": "EFSA Panel on Dietetic Products, Nutrition and Allergies (NDA). Scientific Opinion on Dietary Reference Values for energy. <em>EFSA J</em>. 2013.",
             "u": "https://doi.org/10.2903/j.efsa.2013.3005"},
            {"t": "Mifflin MD, St Jeor ST, Hill LA, et al. A new predictive equation for resting energy expenditure in healthy individuals. <em>Am J Clin Nutr</em>. 1990.",
             "u": "https://doi.org/10.1093/ajcn/51.2.241"},
            {"t": "Frankenfield D, Roth-Yousey L, Compher C. Comparison of predictive equations for resting metabolic rate in healthy nonobese and obese adults: a systematic review. <em>J Am Diet Assoc</em>. 2005.",
             "u": "https://doi.org/10.1016/j.jada.2005.02.005"},
            {"t": "Westerterp KR. Diet induced thermogenesis. <em>Nutr Metab (Lond)</em>. 2004.",
             "u": "https://doi.org/10.1186/1743-7075-1-5"},
            {"t": "Levine JA, Lanningham-Foster LM, McCrady SK, et al. Interindividual variation in posture allocation: possible role in human obesity. <em>Science</em>. 2005.",
             "u": "https://doi.org/10.1126/science.1106561"},
            {"t": "Pontzer H, Yamada Y, Sagayama H, et al. Daily energy expenditure through the human life course. <em>Science</em>. 2021.",
             "u": "https://doi.org/10.1126/science.abe5017"},
        ],
    },
    {
        "slug": "deficit-calorique-comment-calculer",
        "cat": "Alimentation",
        "title": "Déficit calorique : comment le calculer sans se tromper ?",
        "description": "Déficit calorique : 300 à 500 kcal sous ta dépense, soit environ 0,3 à 0,5 kg par semaine au début. Comment le calculer, le tenir et préserver ton muscle.",
        "date": "2026-09-08",
        "body": """
<p>La réponse courte : pars de ta dépense énergétique totale et <strong>retire-lui 300 à 500 kcal par jour</strong>. Le rythme à viser : environ <strong>0,5 à 1 % de ton poids de corps par semaine</strong>, celui qu'une revue de 2014 sur la sèche en musculation recommande pour préserver au mieux le muscle. Concrètement, 300 à 500 kcal de déficit font perdre environ 0,3 à 0,5 kg par semaine au début : le bas de cette fourchette pour la plupart des gens.</p>
<p>La faute classique, c'est de calculer le déficit à partir d'un chiffre inventé. Un déficit n'a de sens que par rapport à <em>ta</em> dépense réelle : commence donc par l'estimer, puis suis ton poids pour la confirmer — <a href="/articles/combien-de-calories-par-jour.html">on détaille la méthode ici</a>. Sans ce point de départ, tu calcules dans le vide.</p>

<h2>La bonne taille de déficit</h2>
<p>Un repère utile : environ <strong>7 000 à 7 700 kcal</strong> correspondent à peu près à un kilo perdu. Une analyse des National Institutes of Health (2008) juge cette règle approximative : elle vaut surtout quand on a beaucoup de graisse à perdre. Un déficit de 500 kcal par jour, c'est ~3 500 kcal sur la semaine, soit à peu près un demi-kilo — un ordre de grandeur, pas une horloge suisse. Trois façons de creuser ce déficit, à combiner :</p>
<ul>
<li><strong>Manger un peu moins</strong> — surtout en réduisant les calories « faciles » : boissons sucrées, alcool, grignotage, huiles.</li>
<li><strong>Bouger un peu plus au quotidien</strong> — l'activité de fond (marche, pas) pèse souvent plus lourd que la séance.</li>
<li><strong>Garder l'entraînement</strong> — non pour « brûler », mais pour protéger le muscle (on y vient).</li>
</ul>

<h2>Pourquoi un déficit trop agressif se retourne contre toi</h2>
<p>Diviser tes calories par deux fait perdre du poids vite — puis casse la machine. Trop bas, trop longtemps, et tu récoltes une <strong>fonte musculaire</strong> (le corps puise dans le muscle quand l'énergie manque), une faim difficile à tenir, une baisse d'énergie et d'activité spontanée, et une motivation qui s'effondre. Le manque de sommeil aggrave tout : à déficit égal, mal dormir <a href="/articles/combien-heures-sommeil-par-nuit.html">fait fondre la masse maigre bien plus vite</a>. Dans un essai de 2010, à régime identique, deux semaines à 5 h 30 au lit au lieu de 8 h 30 ont augmenté de 60 % la perte de masse maigre. Un déficit modéré tenu trois mois bat toujours un déficit brutal tenu trois semaines.</p>

<h2>Préserver le muscle : le trio non négociable</h2>
<ul>
<li><strong>Des protéines hautes</strong> — <a href="/articles/proteines-par-jour-prise-de-muscle.html">2,2 à 2,6 g par kilo et par jour en sèche</a> (2,3 à 3,1 g par kilo de masse maigre selon la revue de 2014). C'est ta meilleure assurance anti-fonte, et ça rassasie.</li>
<li><strong>De la musculation</strong> — le signal qui dit à ton corps de garder ses muscles. En déficit, on maintient les charges, on ne rogne pas d'abord sur l'intensité.</li>
<li><strong>Un déficit raisonnable</strong> — plus il est agressif, plus la part de muscle perdue grimpe. Chez des athlètes d'élite (essai de 2011), perdre 0,7 % du poids par semaine a fait gagner 2,1 % de masse maigre, contre rien à un rythme plus rapide.</li>
</ul>
<p>Question fréquente : <a href="/articles/cardio-ou-muscu-pour-maigrir.html">cardio ou muscu pour maigrir</a> ? Les deux servent, dans des rôles différents — le déficit alimentaire crée la perte, la muscu décide de <em>ce que</em> tu perds.</p>

<h2>Compter ses calories, ou pas ?</h2>
<p>Les deux marchent, à une condition : être honnête. Compter (application, balance de cuisine) apprend énormément les premières semaines — beaucoup de gens <strong>sous-estiment nettement ce qu'ils mangent</strong>, surtout les huiles, les sauces, l'alcool et les portions « à l'œil ». Dans une étude du <em>New England Journal of Medicine</em> (1992), des personnes persuadées de manger moins de 1 200 kcal par jour sous-estimaient en réalité leurs apports de 47 % en moyenne. Si tu préfères piloter sans compter, appuie-toi sur des repères : une source de protéines à chaque repas, beaucoup de légumes, la balance sous surveillance. Mais si ton poids stagne alors que tu es « sûr » d'être en déficit, la cause est presque toujours la même — l'apport réel dépasse l'apport estimé. Peser sa nourriture une semaine ou deux suffit souvent à débloquer la situation.</p>

<h2>Ajuste sur les résultats réels, pas sur la théorie</h2>
<p>Aucun calcul n'est parfait, parce que ton corps s'adapte en chemin : il dépense un peu moins quand tu manges moins. La seule boussole fiable, c'est la tendance :</p>
<ul>
<li>Pèse-toi le matin, suis la <strong>moyenne sur 1 à 2 semaines</strong>, jamais le chiffre d'un jour.</li>
<li>Perte dans la fourchette 0,5-1 %/semaine → ne touche à rien.</li>
<li>Perte à l'arrêt depuis deux semaines → retire 150-200 kcal ou ajoute de la marche.</li>
<li>Perte trop rapide, énergie au sol, entraînements qui s'écroulent → tu es trop bas, remonte.</li>
</ul>

<h2>Ce qu'il faut retenir</h2>
<ul>
<li>Déficit de 300-500 kcal/jour sous ta dépense réelle (~0,3 à 0,5 kg par semaine) ; rythme cible : 0,5 à 1 % du poids par semaine.</li>
<li>Trop agressif = fonte musculaire, faim, abandon ; le manque de sommeil accélère la perte de muscle.</li>
<li>Protéines hautes + musculation préservent le muscle ; ajuste sur la moyenne de poids, pas sur la formule.</li>
</ul>
""",
        "faq": [
            {"q": "Quel déficit calorique pour perdre 1 kg par semaine ?",
             "a": "Il faudrait environ 1 100 kcal de déficit par jour, ce qui est agressif et risqué pour le muscle et l'énergie chez la plupart des gens. Vise plutôt un déficit de 300 à 500 kcal (0,3 à 0,5 kg par semaine au début) et un rythme de 0,5 à 1 % de ton poids par semaine au maximum."},
            {"q": "Comment calculer son déficit calorique ?",
             "a": "Estime ta dépense énergétique totale, puis retire-lui 300 à 500 kcal. Confirme le résultat en suivant la moyenne de ton poids sur deux semaines et ajuste : c'est la réalité de la balance qui tranche, pas la formule."},
            {"q": "Peut-on perdre de la graisse sans perdre de muscle ?",
             "a": "En grande partie, oui : un déficit modéré, des protéines hautes (2,2 à 2,6 g/kg) et de la musculation permettent de perdre surtout du gras. Plus le déficit est agressif, plus la part de muscle perdue augmente."},
        ],
        "sources": [
            {"t": "Helms ER, Aragon AA, Fitschen PJ. Evidence-based recommendations for natural bodybuilding contest preparation: nutrition and supplementation. <em>J Int Soc Sports Nutr</em>. 2014.",
             "u": "https://doi.org/10.1186/1550-2783-11-20"},
            {"t": "Hall KD. What is the required energy deficit per unit weight loss? <em>Int J Obes (Lond)</em>. 2008.",
             "u": "https://doi.org/10.1038/sj.ijo.0803720"},
            {"t": "Nedeltcheva AV, Kilkus JM, Imperial J, et al. Insufficient sleep undermines dietary efforts to reduce adiposity. <em>Ann Intern Med</em>. 2010.",
             "u": "https://doi.org/10.7326/0003-4819-153-7-201010050-00006"},
            {"t": "Garthe I, Raastad T, Refsnes PE, et al. Effect of two different weight-loss rates on body composition and strength and power-related performance in elite athletes. <em>Int J Sport Nutr Exerc Metab</em>. 2011.",
             "u": "https://doi.org/10.1123/ijsnem.21.2.97"},
            {"t": "Lichtman SW, Pisarska K, Berman ER, et al. Discrepancy between self-reported and actual caloric intake and exercise in obese subjects. <em>N Engl J Med</em>. 1992.",
             "u": "https://doi.org/10.1056/NEJM199212313272701"},
        ],
    },
    {
        "slug": "creatine-bienfaits-comment-la-prendre",
        "cat": "Alimentation",
        "title": "Créatine : bienfaits et comment la prendre",
        "description": "Créatine monohydrate, 3 à 5 g par jour, tous les jours : bienfaits réels, comment la prendre, phase de charge inutile et mythes. Le complément le plus étudié.",
        "date": "2026-09-10",
        "body": """
<p>La réponse courte : <strong>créatine monohydrate, 3 à 5 g par jour, tous les jours</strong>, avec un grand verre d'eau, à n'importe quel moment de la journée. Pas besoin de forme « exotique » ni de phase de charge. C'est, de très loin, le complément sportif <strong>le plus étudié et le plus sûr</strong> chez la personne en bonne santé — plus de 500 publications scientifiques, des décennies de recul.</p>
<p>La créatine n'a rien de magique ni de sulfureux : c'est une molécule que ton corps fabrique déjà et que tu trouves dans la viande et le poisson. En complément, elle remplit tes réserves musculaires à ras bord, ce qui aide tes muscles à produire de l'énergie sur les efforts courts et intenses. Résultat concret : un peu plus de force, un peu plus de répétitions, séance après séance.</p>

<h2>Comment la prendre (c'est simple)</h2>
<ul>
<li><strong>La forme :</strong> monohydrate, point. C'est la seule qui a vraiment fait ses preuves ; les versions « nouvelle génération » plus chères n'apportent rien de plus.</li>
<li><strong>La dose :</strong> 3 à 5 g par jour. Une petite cuillère, avec de l'eau ou dans ta boisson.</li>
<li><strong>Le moment :</strong> indifférent. Avant, après, le matin, le soir — seule compte la régularité.</li>
<li><strong>Les jours de repos aussi.</strong> Tu ne « recharges » pas avant la séance, tu maintiens un taux plein en permanence : c'est un traitement de fond, pas un pré-workout.</li>
</ul>
<p>La <strong>phase de charge</strong> (20 g/jour pendant 5-7 jours) est facultative : elle ne fait que saturer les réserves un peu plus vite. À 3-5 g par jour, tu atteins le même niveau en environ quatre semaines, sans risquer les inconforts digestifs des grosses doses. Une étude de référence (1996) l'a mesuré : 20 g par jour pendant 6 jours ou 3 g par jour pendant 28 jours donnent la même hausse, d'environ 20 %, de la créatine musculaire.</p>

<h2>Ce qu'elle fait vraiment</h2>
<ul>
<li><strong>Force et puissance :</strong> le bénéfice principal et le mieux démontré, sur les efforts explosifs et les séries lourdes. Elle ne soulève pas la barre à ta place — elle t'aide à en faire un peu plus, et c'est ce petit surplus, répété, qui construit (<a href="/articles/surcharge-progressive-comment-progresser.html">la surcharge progressive fait le reste</a>). Sur 22 études compilées en 2003, la force progressait de 20 % avec créatine et entraînement, contre 12 % avec placebo.</li>
<li><strong>Un léger gain de volume :</strong> la créatine attire un peu d'eau <em>dans</em> le muscle. Muscles un rien plus pleins, et une prise de poids de 1 à 3 kg, surtout d'eau, pendant une phase de charge (moins, et plus progressive, à 3-5 g par jour) — pas de la graisse.</li>
<li><strong>Cognition et récupération :</strong> des pistes intéressantes, mais moins solides que le volet force. Une revue de 2018 (6 essais, 281 participants) suggère un effet sur la mémoire à court terme et le raisonnement, surtout chez les personnes âgées ou stressées, avec des résultats contradictoires ailleurs. À suivre, sans survendre.</li>
</ul>

<h2>Les mythes à jeter</h2>
<ul>
<li><strong>« C'est un stéroïde. »</strong> Non, aucun rapport : ni hormone, ni produit dopant. Un dérivé d'acides aminés déjà présent dans ton alimentation.</li>
<li><strong>« Ça fait grossir. »</strong> La prise de poids initiale, c'est de l'eau intramusculaire, pas du gras.</li>
<li><strong>« Il faut faire des cures. »</strong> Inutile de cycler ou d'arrêter régulièrement : selon l'International Society of Sports Nutrition, des prises allant jusqu'à 30 g par jour pendant 5 ans se sont montrées sûres chez le sujet sain.</li>
</ul>

<h2>Créatine et protéines : deux choses différentes</h2>
<p>La créatine n'est pas une protéine et ne remplace pas ton alimentation. Elle t'aide à mieux t'entraîner ; <a href="/articles/proteines-par-jour-prise-de-muscle.html">les protéines</a>, elles, fournissent les matériaux de construction. Le muscle se bâtit avec un entraînement qui progresse, assez de protéines et assez de sommeil — la créatine est un coup de pouce solide par-dessus, pas un raccourci qui dispense du reste.</p>

<h2>Une réserve de sécurité</h2>
<p>Chez le sujet sain, la créatine est très bien tolérée. En revanche, en cas de <strong>maladie rénale</strong> connue (ou de doute), c'est une décision à prendre avec un médecin, pas seul dans un rayon de compléments. Idem pendant la grossesse : demande un avis.</p>

<h2>Ce qu'il faut retenir</h2>
<ul>
<li>Monohydrate, 3 à 5 g par jour, tous les jours, à l'heure qui t'arrange — la charge est facultative.</li>
<li>Bénéfice principal et prouvé : force et puissance ; le gain de poids initial est de l'eau, pas du gras.</li>
<li>Complément le plus sûr chez le sujet sain ; avis médical en cas de problème rénal.</li>
</ul>
""",
        "faq": [
            {"q": "Faut-il faire une phase de charge de créatine ?",
             "a": "Non, c'est facultatif. Une phase de charge (20 g/jour pendant 5-7 jours) sature les réserves un peu plus vite, mais 3 à 5 g par jour atteignent le même niveau en environ quatre semaines, sans inconfort digestif."},
            {"q": "La créatine fait-elle grossir ?",
             "a": "Elle peut faire prendre 1 à 3 kg au début, surtout avec une phase de charge, mais c'est essentiellement de l'eau stockée dans le muscle, pas de la graisse. Les muscles paraissent un peu plus pleins ; il n'y a aucune prise de gras liée à la créatine."},
            {"q": "Quand prendre la créatine ?",
             "a": "À n'importe quel moment : avant ou après l'entraînement, le matin ou le soir, et aussi les jours de repos. C'est un traitement de fond où seule la régularité quotidienne compte, pas le timing."},
        ],
        "sources": [
            {"t": "Kreider RB, Kalman DS, Antonio J, et al. International Society of Sports Nutrition position stand: safety and efficacy of creatine supplementation in exercise, sport, and medicine. <em>J Int Soc Sports Nutr</em>. 2017.",
             "u": "https://doi.org/10.1186/s12970-017-0173-z"},
            {"t": "Antonio J, Candow DG, Forbes SC, et al. Common questions and misconceptions about creatine supplementation: what does the scientific evidence really show? <em>J Int Soc Sports Nutr</em>. 2021.",
             "u": "https://doi.org/10.1186/s12970-021-00412-w"},
            {"t": "Hultman E, Söderlund K, Timmons JA, et al. Muscle creatine loading in men. <em>J Appl Physiol</em>. 1996.",
             "u": "https://doi.org/10.1152/jappl.1996.81.1.232"},
            {"t": "Rawson ES, Volek JS. Effects of creatine supplementation and resistance training on muscle strength and weightlifting performance. <em>J Strength Cond Res</em>. 2003.",
             "u": "https://doi.org/10.1519/1533-4287(2003)017<0822:EOCSAR>2.0.CO;2"},
            {"t": "Avgerinos KI, Spyrou N, Bougioukas KI, Kapogiannis D. Effects of creatine supplementation on cognitive function of healthy individuals: a systematic review of randomized controlled trials. <em>Exp Gerontol</em>. 2018.",
             "u": "https://doi.org/10.1016/j.exger.2018.04.013"},
        ],
    },
    {
        "slug": "que-manger-avant-le-sport",
        "cat": "Alimentation",
        "title": "Que manger avant le sport pour performer ?",
        "description": "Que manger avant le sport ? Des glucides, surtout. Un vrai repas 2-3 h avant ou une collation légère 30-60 min avant, exemples concrets et hydratation.",
        "date": "2026-09-12",
        "body": """
<p>La réponse courte : <strong>des glucides, surtout</strong>. Ce sont eux qui alimentent l'effort. Deux formats marchent selon le temps dont tu disposes — un <strong>vrai repas 2 à 3 heures avant</strong>, ou une <strong>collation légère et riche en glucides 30 à 60 minutes avant</strong>. Dans les deux cas, on limite le gras et les fibres juste avant : ils ralentissent la digestion et pèsent sur l'estomac à l'effort.</p>
<p>Inutile de compliquer. L'objectif est d'arriver <em>plein d'énergie et l'estomac tranquille</em> — ni affamé, ni en train de digérer un plat lourd.</p>

<h2>Pourquoi des glucides</h2>
<p>Les glucides se stockent dans les muscles et le foie sous forme de glycogène : c'est le carburant de prédilection dès que l'intensité monte, et la principale source d'énergie du cerveau. Avant une séance, ils remplissent le réservoir et stabilisent ta glycémie, ce qui se traduit par plus de jus et une meilleure concentration. Les protéines et les lipides sont utiles dans ton alimentation globale, mais juste avant l'effort, ils digèrent lentement et n'apportent pas d'énergie immédiate.</p>

<h2>Le bon timing</h2>
<ul>
<li><strong>2 à 3 heures avant :</strong> un vrai repas équilibré, dominé par les glucides, avec un peu de protéines et peu de gras. Confort maximal — tout est digéré au moment d'attaquer.</li>
<li><strong>30 à 60 minutes avant :</strong> une collation légère, presque uniquement des glucides faciles à digérer. Plus c'est proche de la séance, plus ça doit être petit, simple et pauvre en gras et en fibres.</li>
</ul>

<h2>Des exemples concrets</h2>
<ul>
<li><strong>Repas 2-3 h avant :</strong> riz ou pâtes + poulet + légumes cuits ; ou pain complet + œufs + fruit ; ou un bol de flocons d'avoine avec du lait et une banane.</li>
<li><strong>Collation 30-60 min avant :</strong> une banane, une compote, quelques dattes, une tranche de pain avec du miel, ou un fruit.</li>
<li><strong>À éviter juste avant :</strong> friture, plat très gras, gros bol de crudités ou de légumineuses — trop long à digérer, ballonnements assurés.</li>
</ul>

<h2>S'entraîner à jeun, bonne ou mauvaise idée ?</h2>
<p>Ça dépend de ce que tu fais. Pour du <a href="/articles/zone-2-cardio-cest-quoi.html">cardio facile en zone 2</a> le matin, t'entraîner à jeun est tout à fait viable — beaucoup le vivent très bien. Une méta-analyse de 2018 (46 études) le confirme : manger avant améliore les efforts d'endurance prolongés, mais pas les efforts plus courts. Pour la <strong>force ou la haute intensité</strong>, les données sont plus minces ; si tu te sens à plat l'estomac vide, une petite collation glucidique 30 minutes avant fait souvent une vraie différence. Et pour une <strong>recherche de performance</strong> sur un effort long, ne pars pas à jeun.</p>

<h2>Adapte à ta séance</h2>
<p>Tous les efforts n'ont pas les mêmes besoins. Pour une <strong>séance courte et légère</strong>, tu n'as quasiment besoin de rien de particulier. Pour une <strong>séance de musculation ou de haute intensité</strong>, des glucides disponibles peuvent aider sur les dernières séries. Et pour un <strong>effort long</strong> — plus d'une heure — c'est là que le plein de glucides compte le plus : pour un effort intense de plus de 90 minutes, l'International Society of Sports Nutrition recommande 1 à 4 g de glucides par kilo dans les heures qui précèdent, puis 30 à 60 g par heure pendant l'effort. Règle simple : plus la séance est longue ou intense, plus les glucides d'avant pèsent lourd.</p>

<h2>Et le café avant l'entraînement ?</h2>
<p>La caféine est l'un des rares « boosters » dont l'effet sur la performance est solidement établi : un peu plus de force et d'endurance, une vigilance accrue. Selon l'International Society of Sports Nutrition (2021), l'effet est constant entre 3 et 6 mg par kilo, pris le plus souvent 60 minutes avant, et commence peut-être dès 2 mg par kilo : pour 70 kg, environ 140 à 210 mg, soit à peu près deux cafés. Deux garde-fous : reste raisonnable sur la dose — l'EFSA juge sans risque jusqu'à 200 mg en une prise, même avant un effort intense, et 400 mg sur la journée — et surtout <a href="/articles/cafe-et-sommeil-combien-de-temps-avant.html">évite la caféine en fin de journée</a> — un entraînement du soir dopé au café peut te coûter ta nuit, et la récupération se joue justement pendant le sommeil.</p>

<h2>N'oublie pas de boire</h2>
<p>Arriver déshydraté plombe la performance autant qu'un réservoir vide : l'American College of Sports Medicine conseille de commencer l'effort bien hydraté, en buvant dès quelques heures avant. Bois normalement dans les heures qui précèdent, un verre ou deux avant de commencer, et <a href="/articles/combien-d-eau-boire-par-jour.html">ajuste selon la chaleur et la transpiration</a>. Et pense à l'après tout de suite : <a href="/articles/que-manger-apres-le-sport.html">ce que tu manges après la séance</a> compte autant pour ta récupération.</p>

<h2>Ce qu'il faut retenir</h2>
<ul>
<li>Avant l'effort, priorité aux glucides : vrai repas 2-3 h avant, ou collation légère 30-60 min avant.</li>
<li>Moins de gras et de fibres à l'approche de la séance ; plus c'est proche, plus c'est petit et simple.</li>
<li>À jeun : ok pour du cardio léger ; pour un effort long ou une recherche de perf, mange avant. Et bois avant de commencer.</li>
</ul>
""",
        "faq": [
            {"q": "Que manger avant une séance de musculation ?",
             "a": "Un repas riche en glucides avec un peu de protéines 2 à 3 heures avant (riz + poulet + légumes, par exemple), ou une collation glucidique légère 30 à 60 minutes avant (banane, pain-miel). On évite le gras et les fibres juste avant la séance."},
            {"q": "Peut-on faire du sport à jeun ?",
             "a": "Oui pour du cardio facile ou court, où c'est sans problème. Pour un effort long ou une recherche de performance, manger avant améliore les résultats. Pour la musculation ou la haute intensité, les données sont moins nettes : si tu te sens à plat, une petite collation glucidique 30 minutes avant suffit souvent."},
            {"q": "Combien de temps avant le sport faut-il manger ?",
             "a": "Un vrai repas se prend 2 à 3 heures avant pour être digéré ; une collation légère et riche en glucides, 30 à 60 minutes avant. Plus tu manges près de la séance, plus la portion doit être petite et pauvre en gras."},
        ],
        "sources": [
            {"t": "Kerksick CM, Arent S, Schoenfeld BJ, et al. International society of sports nutrition position stand: nutrient timing. <em>J Int Soc Sports Nutr</em>. 2017.",
             "u": "https://doi.org/10.1186/s12970-017-0189-4"},
            {"t": "Aird TP, Davies RW, Carson BP. Effects of fasted vs fed-state exercise on performance and post-exercise metabolism: a systematic review and meta-analysis. <em>Scand J Med Sci Sports</em>. 2018.",
             "u": "https://doi.org/10.1111/sms.13054"},
            {"t": "Guest NS, VanDusseldorp TA, Nelson MT, et al. International society of sports nutrition position stand: caffeine and exercise performance. <em>J Int Soc Sports Nutr</em>. 2021.",
             "u": "https://doi.org/10.1186/s12970-020-00383-4"},
            {"t": "EFSA Panel on Dietetic Products, Nutrition and Allergies (NDA). Scientific Opinion on the safety of caffeine. <em>EFSA J</em>. 2015.",
             "u": "https://doi.org/10.2903/j.efsa.2015.4102"},
            {"t": "American College of Sports Medicine, Sawka MN, Burke LM, et al. American College of Sports Medicine position stand. Exercise and fluid replacement. <em>Med Sci Sports Exerc</em>. 2007.",
             "u": "https://doi.org/10.1249/mss.0b013e31802ca597"},
        ],
    },
    {
        "slug": "que-manger-apres-le-sport",
        "cat": "Alimentation",
        "title": "Que manger après le sport pour bien récupérer ?",
        "description": "Que manger après le sport : 20 à 40 g de protéines et des glucides. Pourquoi la fenêtre anabolique de 30 minutes est un mythe, et des exemples concrets.",
        "date": "2026-09-13",
        "body": """
<p>La réponse courte : <strong>des protéines (20 à 40 g) et des glucides</strong>. Les protéines fournissent les briques pour réparer le muscle, les glucides rechargent le glycogène que l'effort a entamé. Un repas normal contenant les deux, dans les <strong>deux à trois heures</strong> qui suivent la séance, couvre l'essentiel — pas besoin de te jeter sur un shaker à la seconde où tu reposes la barre.</p>
<p>C'est le point qui surprend le plus : la fameuse <strong>« fenêtre anabolique » de 30 minutes est un mythe</strong>, du moins dans sa version stricte et stressante.</p>

<h2>Le duo protéines + glucides</h2>
<p>Après l'effort, deux choses se rejouent. D'un côté, la <strong>synthèse des protéines musculaires</strong> est stimulée : un apport de 20 à 40 g de protéines de qualité (0,25 à 0,4 g par kilo de poids de corps), la dose que retient l'International Society of Sports Nutrition, fournit assez d'acides aminés pour en tirer le maximum. De l'autre, tes réserves de <strong>glycogène</strong> se reconstituent : des glucides accélèrent le plein, surtout après une grosse séance ou du cardio long. Les deux ensemble font un repas de récupération complet.</p>

<h2>La fenêtre de 30 minutes est un mythe</h2>
<p>Longtemps, on a cru qu'il fallait manger dans la demi-heure sous peine de « perdre » sa séance. Les données ont corrigé ça : la fenêtre dure en réalité <strong>plusieurs heures</strong>. Une méta-analyse de 2013 (une vingtaine d'essais, plus de 500 participants) va plus loin : une fois l'apport total en protéines pris en compte, le timing autour de la séance ne change rien à la prise de muscle ni de force. Bref, <a href="/articles/proteines-par-jour-prise-de-muscle.html">c'est ton apport total sur la journée qui construit</a>, bien plus que la minute exacte du repas post-séance. Autrement dit : respire. Un vrai repas dans les deux-trois heures suffit très largement pour la plupart des objectifs.</p>

<h2>Les seuls cas où le timing compte vraiment</h2>
<ul>
<li><strong>Tu enchaînes deux séances</strong> à quelques heures d'écart : là, recharger vite les glucides a un vrai intérêt — l'ISSN parle de recharge rapide quand moins de 4 heures séparent les efforts.</li>
<li><strong>Tu t'es entraîné à jeun</strong> ou plusieurs heures après ton dernier repas : manger assez vite après devient plus utile. Au-delà de 3 à 4 heures sans manger avant la séance, une revue de 2013 conseille au moins 25 g de protéines dès que possible.</li>
<li><strong>Sport d'endurance à gros volume :</strong> reconstituer le glycogène rapidement aide à tenir la charge des jours suivants.</li>
</ul>
<p>En dehors de ces situations, l'urgence est un faux problème.</p>

<h2>Et si tu es en déficit pour perdre du gras ?</h2>
<p>Même en sèche, le principe ne bouge pas : des protéines pour protéger le muscle, un peu de glucides pour recharger. La seule différence, c'est que ces calories doivent <strong>tenir dans ton total de la journée</strong> — tu ne les ajoutes pas en plus. Le repas d'après-séance reste d'ailleurs le meilleur endroit où placer une bonne part de tes glucides quand tu en as peu : c'est le moment où ton corps les utilise le mieux.</p>

<h2>Des exemples concrets</h2>
<ul>
<li>Fromage blanc ou skyr + fruits + flocons d'avoine.</li>
<li>Poulet ou poisson + riz + légumes.</li>
<li>Œufs + pain complet + un fruit.</li>
<li>Pressé ou sans faim juste après : un shaker de protéines + une banane, en dépannage — pas une obligation.</li>
</ul>

<h2>Manger ne fait pas tout</h2>
<p>Le repas d'après-séance n'est qu'une pièce de la récupération. Le reste se joue sur ton <a href="/articles/proteines-par-jour-prise-de-muscle.html">apport en protéines réparti sur la journée</a> (environ 0,4 g par kilo à au moins quatre repas, selon une revue de 2018), sur ton sommeil, et sur ta gestion de la charge. Et non, aucun repas ne « soigne » les <a href="/articles/courbatures-que-faire.html">courbatures</a> : elles suivent leur cours quoi que tu avales. Prépare aussi ta prochaine séance en soignant <a href="/articles/que-manger-avant-le-sport.html">ce que tu manges avant</a>.</p>

<h2>Pense à te réhydrater</h2>
<p>La réhydratation fait partie de la récupération, surtout après avoir beaucoup transpiré. Bois à ta soif dans les heures qui suivent, un peu plus s'il faisait chaud — <a href="/articles/combien-d-eau-boire-par-jour.html">de quelle quantité tu as besoin, c'est ici</a>. Inutile d'engloutir des litres d'un coup : refais le plein progressivement.</p>

<h2>Ce qu'il faut retenir</h2>
<ul>
<li>Après l'effort : 20 à 40 g de protéines + des glucides, dans un repas normal sous 2-3 heures.</li>
<li>La fenêtre anabolique stricte de 30 minutes est un mythe ; c'est le total du jour qui compte.</li>
<li>Le timing serré ne compte vraiment que si tu enchaînes les séances ou t'entraînes à jeun.</li>
</ul>
""",
        "faq": [
            {"q": "Faut-il manger juste après le sport ?",
             "a": "Pas dans l'urgence : la fenêtre anabolique de 30 minutes est un mythe. Un repas avec protéines et glucides dans les deux à trois heures suffit. Le timing serré ne compte que si tu enchaînes deux séances ou t'es entraîné à jeun."},
            {"q": "Que manger après la musculation pour récupérer ?",
             "a": "20 à 40 g de protéines (0,25 à 0,4 g par kilo) et des glucides : fromage blanc + fruits + flocons, poulet + riz + légumes, ou œufs + pain. Les protéines réparent le muscle, les glucides rechargent le glycogène."},
            {"q": "Faut-il boire un shaker de protéines après l'entraînement ?",
             "a": "Ce n'est pas obligatoire. Un shaker est pratique si tu es pressé ou sans appétit, mais un vrai repas fait aussi bien. C'est ton total de protéines sur la journée qui compte, pas la boisson juste après la séance."},
        ],
        "sources": [
            {"t": "Schoenfeld BJ, Aragon AA, Krieger JW. The effect of protein timing on muscle strength and hypertrophy: a meta-analysis. <em>J Int Soc Sports Nutr</em>. 2013.",
             "u": "https://doi.org/10.1186/1550-2783-10-53"},
            {"t": "Aragon AA, Schoenfeld BJ. Nutrient timing revisited: is there a post-exercise anabolic window? <em>J Int Soc Sports Nutr</em>. 2013.",
             "u": "https://doi.org/10.1186/1550-2783-10-5"},
            {"t": "Kerksick CM, Arent S, Schoenfeld BJ, et al. International society of sports nutrition position stand: nutrient timing. <em>J Int Soc Sports Nutr</em>. 2017.",
             "u": "https://doi.org/10.1186/s12970-017-0189-4"},
            {"t": "Jäger R, Kerksick CM, Campbell BI, et al. International Society of Sports Nutrition Position Stand: protein and exercise. <em>J Int Soc Sports Nutr</em>. 2017.",
             "u": "https://doi.org/10.1186/s12970-017-0177-8"},
            {"t": "Schoenfeld BJ, Aragon AA. How much protein can the body use in a single meal for muscle-building? Implications for daily protein distribution. <em>J Int Soc Sports Nutr</em>. 2018.",
             "u": "https://doi.org/10.1186/s12970-018-0215-1"},
        ],
    },
    {
        "slug": "combien-d-eau-boire-par-jour",
        "cat": "Alimentation",
        "title": "Combien d'eau faut-il boire par jour ?",
        "description": "Combien d'eau boire par jour ? Selon l'EFSA, 2 L au total pour une femme et 2,5 L pour un homme, aliments compris. Le mythe des 8 verres, la soif, le sport.",
        "date": "2026-09-15",
        "body": """
<p>La réponse courte : environ <strong>30 à 35 ml par kilo de poids de corps</strong>, soit à peu près <strong>1,5 à 2,5 L par jour</strong> pour la plupart des adultes — <em>plus</em> ce que tu perds à l'effort et à la chaleur. Pour 70 kg, ça fait grosso modo 2 à 2,5 L, boissons comprises.</p>
<p>Mais le chiffre exact importe moins qu'on ne le croit, parce que ton corps possède un système de régulation très fin : la soif. Le rituel des « 8 verres par jour » est un repère commode, pas une loi physiologique — et il ne colle ni à ton poids, ni à ton climat, ni à ton activité.</p>

<h2>D'où vient le chiffre</h2>
<p>La règle des 30-35 ml/kg est une estimation raisonnable des besoins totaux en eau d'un adulte. Elle recoupe les repères de l'Autorité européenne de sécurité des aliments (EFSA) :</p>
<div class="tablewrap"><table>
<caption>Source : EFSA (2010), apports adéquats en eau totale (boissons et aliments), climat tempéré, activité modérée.</caption>
<thead><tr><th>Profil</th><th class="n">Eau totale par jour</th></tr></thead>
<tbody>
<tr><td>Femme adulte</td><td class="n">2,0 L</td></tr>
<tr><td>Homme adulte</td><td class="n">2,5 L</td></tr>
<tr><td>Femme enceinte</td><td class="n">2,3 L</td></tr>
<tr><td>Femme qui allaite</td><td class="n">2,7 L</td></tr>
<tr><td>Adolescent dès 14 ans, senior</td><td class="n">comme l'adulte</td></tr>
</tbody>
</table></div>
<p>Deux précisions qui changent tout :</p>
<ul>
<li>Ce total inclut <strong>toutes les boissons</strong>, pas seulement l'eau plate : thé, café, tisanes, soupes comptent. La caféine à doses habituelles n'a pas l'effet « déshydratant » qu'on lui prête : dans un essai de 2014 sur 50 buveurs réguliers, quatre tasses par jour hydrataient aussi bien que de l'eau.</li>
<li>Il inclut aussi <strong>l'eau contenue dans les aliments</strong> — fruits, légumes, yaourts, plats en sauce en apportent une bonne part. C'est pour ça qu'on n'a pas besoin de boire l'intégralité de ses besoins au robinet.</li>
</ul>

<h2>Le mythe des 8 verres</h2>
<p>« Huit verres d'eau par jour » est une formule facile à retenir, mais quand le physiologiste Heinz Valtin a cherché son origine en 2002, il n'a trouvé aucune étude scientifique pour en faire une cible universelle chez l'adulte en bonne santé. Tes besoins montent avec la chaleur, l'altitude, l'exercice, l'allaitement ou une journée très active — et descendent quand tu es sédentaire au frais. Vouloir avaler un nombre fixe de litres coûte que coûte n'a pas de sens : ça pousse soit à te forcer, soit à culpabiliser pour rien.</p>

<h2>Tes deux meilleurs indicateurs</h2>
<p>Oublie le décompte, écoute deux signaux :</p>
<ul>
<li><strong>La soif.</strong> Chez l'adulte en bonne santé, c'est un guide fiable : bois quand tu as soif, c'est le plus souvent suffisant. Deux nuances — les personnes âgées ressentent moins bien la soif, et à l'effort intense il vaut mieux anticiper sans attendre d'avoir la gorge sèche.</li>
<li><strong>La couleur des urines.</strong> L'indicateur le plus simple qui soit, fiable sur le terrain selon une étude de 1994 : <strong>jaune pâle</strong>, tout va bien ; foncé et peu abondant, bois davantage ; presque transparent en permanence, tu bois probablement plus que nécessaire.</li>
</ul>

<h2>Sport et chaleur : le vrai supplément</h2>
<p>C'est là que les besoins grimpent pour de bon. Une heure de transpiration, c'est facilement <strong>0,5 à 1 L de pertes</strong>, parfois plus par forte chaleur : chez 1 303 athlètes, la transpiration moyenne allait de 0,8 à 1,5 L par heure selon le sport. Bois avant de commencer, régulièrement pendant l'effort long, et refais le plein après — <a href="/articles/que-manger-avant-le-sport.html">l'hydratation fait partie de la préparation d'une séance</a>. Sur les efforts très longs ou en pleine chaleur, l'eau seule ne suffit plus : les pertes en sel comptent aussi.</p>

<h2>Faut-il des électrolytes ?</h2>
<p>Pour une journée normale, non : de l'eau et une alimentation équilibrée suffisent, le sel de tes repas fait le reste. Les <strong>électrolytes</strong> (le sodium surtout) deviennent utiles dans un cas précis — les efforts <strong>longs, intenses ou en pleine chaleur</strong>, où tu perds beaucoup de sel dans la sueur. Là, une boisson d'effort ou une simple pincée de sel a du sens. En dehors de ça, les poudres d'électrolytes du quotidien relèvent surtout du marketing. Retiens aussi qu'une déshydratation même modérée dégrade mesurablement la performance et la concentration — l'American College of Sports Medicine conseille de ne pas perdre plus de 2 % de ton poids pendant l'effort. Ne commence pas une grosse séance déjà en manque d'eau.</p>

<h2>Peut-on boire trop ?</h2>
<p>Oui, mais c'est rare. Forcer sur de très grands volumes d'eau plate en peu de temps — typiquement lors d'épreuves d'endurance — peut trop diluer le sodium du sang (<em>hyponatrémie</em>), ce qui est dangereux : tes reins n'éliminent pas plus de 0,7 à 1 L par heure, selon l'EFSA. La leçon pratique : ne te force pas à engloutir des litres « par principe ». À l'inverse, une déshydratation même légère se paie en énergie et en concentration : si tu es <a href="/articles/toujours-fatigue-causes.html">souvent fatigué sans raison claire</a>, un apport d'eau insuffisant fait partie des causes bêtes à écarter en premier.</p>

<h2>Ce qu'il faut retenir</h2>
<ul>
<li>Environ 30-35 ml/kg, soit ~1,5-2,5 L par jour, boissons et eau des aliments comprises.</li>
<li>Les « 8 verres » sont un repère, pas une règle : fie-toi à la soif et à des urines jaune pâle.</li>
<li>Ajoute 0,5-1 L par heure de transpiration ; ne te force pas à boire au-delà — l'excès existe.</li>
</ul>
""",
        "faq": [
            {"q": "Faut-il vraiment boire 8 verres d'eau par jour ?",
             "a": "Non, c'est un repère commode, pas une règle. Tes besoins tournent autour de 30-35 ml par kilo (soit ~1,5-2,5 L), varient selon la chaleur et l'activité, et incluent toutes les boissons plus l'eau des aliments."},
            {"q": "Comment savoir si je bois assez ?",
             "a": "Deux indicateurs : la soif, fiable chez l'adulte en bonne santé, et la couleur des urines. Jaune pâle signifie que tu es bien hydraté ; foncé et peu abondant, il faut boire davantage."},
            {"q": "Combien d'eau boire quand on fait du sport ?",
             "a": "Ajoute environ 0,5 à 1 L par heure de transpiration à tes besoins de base, davantage par forte chaleur. Bois avant, pendant les efforts longs et après. Sur les efforts très longs, pense aussi aux pertes en sel."},
        ],
        "sources": [
            {"t": "EFSA Panel on Dietetic Products, Nutrition and Allergies (NDA). Scientific Opinion on Dietary Reference Values for water. <em>EFSA J</em>. 2010.",
             "u": "https://doi.org/10.2903/j.efsa.2010.1459"},
            {"t": "Valtin H. \"Drink at least eight glasses of water a day.\" Really? Is there scientific evidence for \"8 x 8\"? <em>Am J Physiol Regul Integr Comp Physiol</em>. 2002.",
             "u": "https://doi.org/10.1152/ajpregu.00365.2002"},
            {"t": "Killer SC, Blannin AK, Jeukendrup AE. No evidence of dehydration with moderate daily coffee intake: a counterbalanced cross-over study in a free-living population. <em>PLoS One</em>. 2014.",
             "u": "https://doi.org/10.1371/journal.pone.0084154"},
            {"t": "Armstrong LE, Maresh CM, Castellani JW, et al. Urinary indices of hydration status. <em>Int J Sport Nutr</em>. 1994.",
             "u": "https://doi.org/10.1123/ijsn.4.3.265"},
            {"t": "Barnes KA, Anderson ML, Stofan JR, et al. Normative data for sweating rate, sweat sodium concentration, and sweat sodium loss in athletes: an update and analysis by sport. <em>J Sports Sci</em>. 2019.",
             "u": "https://doi.org/10.1080/02640414.2019.1633159"},
            {"t": "American College of Sports Medicine, Sawka MN, Burke LM, et al. American College of Sports Medicine position stand. Exercise and fluid replacement. <em>Med Sci Sports Exerc</em>. 2007.",
             "u": "https://doi.org/10.1249/mss.0b013e31802ca597"},
        ],
    },
]
