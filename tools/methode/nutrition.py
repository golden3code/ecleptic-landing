# -*- coding: utf-8 -*-
"""La méthode · Moteur III — la nutrition.

Chargé par tools/build_articles.py (_load_methode) → /methode/nutrition.html.
Faits vérifiés (fiche de faits de l'app) le 24/09/2026 : catalogue de 438 267
références (433 631 produits USDA + 3 484 aliments Ciqual ANSES + 1 152 plats
composés) + produits à code-barres Open Food Facts ; scan jusqu'à 3 photos
fusionnées, l'IA reconnaît et estime les portions, les valeurs viennent des
bases ; 21 micronutriments, antioxydants, eau des aliments dans l'hydratation ;
pilier nutrition 21 pts (40/25/20/15, refuel retiré les jours de repos, plafond
alcool 80 sur 100, cf. lib/readiness/nutrition.ts) ; modificateur de l'âge
biologique (plafond non publié). Le fournisseur du modèle d'IA n'est pas nommé.
"""

PAGE = {
    "slug": "nutrition",
    "kind": "moteur",
    "num": "III",
    "order": 3,
    "label": "La nutrition",
    "title": "La nutrition, de la photo à la source officielle",
    "seo_title": "Nutrition : du scan de repas aux bases Ciqual et USDA — Ecleptic",
    "description": "Scan de repas : l'IA reconnaît les aliments et estime les portions, les bases Ciqual, USDA et Open Food Facts donnent les valeurs. La méthode et ses limites.",
    "date": "2026-09-24",
    "lead": "Tu prends ton assiette en photo, l'app affiche des calories, des macros, 21 micronutriments. Voici exactement ce qui se passe entre les deux, et pourquoi <strong>aucune valeur nutritionnelle n'est inventée par l'IA</strong> : toutes viennent de bases officielles.",
    "body": """
<h2>Ce que le moteur calcule</h2>
<p>Le moteur nutrition répond à une question simple : <strong>qu'as-tu réellement mangé, et qu'est-ce que ça t'a apporté ?</strong> Pour chaque repas, l'app calcule et t'affiche tes calories, tes protéines, tes glucides et tes lipides, mais aussi 21 micronutriments et tes apports en antioxydants.</p>
<p>Elle compte aussi ce qu'on oublie presque toujours : <strong>l'eau contenue dans les aliments</strong>. Une soupe, un fruit ou un yaourt t'hydratent eux aussi, et cette eau entre dans ton hydratation de la journée.</p>
<p>Tout repose sur une règle non négociable : <strong>l'IA identifie et estime, les bases officielles donnent les valeurs.</strong> L'IA reconnaît ce qu'il y a dans ton assiette et en estime les portions. Les valeurs, elles, viennent toujours d'une fiche publiée par une source de référence : calories, macros, micronutriments, antioxydants. Aucune valeur nutritionnelle affichée n'est une estimation inventée par l'IA.</p>

<h2>Un catalogue de 438&nbsp;267 références</h2>
<p>Quand tu scannes un repas, chaque aliment est rattaché aux bases de données nutritionnelles publiques qui font référence :</p>
<ul>
<li><strong>La table Ciqual de l'ANSES :</strong> l'agence sanitaire française y décrit 3&nbsp;484 aliments à travers 257&nbsp;000 valeurs nutritionnelles mesurées en laboratoire. C'est la table de référence en France.</li>
<li><strong>USDA FoodData Central :</strong> la base du département américain de l'Agriculture, dont l'app intègre 433&nbsp;631 produits. Elle apporte l'étendue : des centaines de milliers de références, là où Ciqual en décrit quelques milliers.</li>
<li><strong>Open Food Facts :</strong> la base collaborative des produits à code-barres, avec les valeurs d'un produit précis, marque comprise.</li>
</ul>
<p>Le catalogue compte aussi <strong>1&nbsp;152 plats composés</strong>, pour les assiettes qui ne se résument pas à un aliment isolé.</p>
<div class="figs">
  <div><span class="v">438&nbsp;267</span><span class="u">Références au catalogue</span></div>
  <div><span class="v">433&nbsp;631</span><span class="u">Produits USDA</span></div>
  <div><span class="v">3&nbsp;484</span><span class="u">Aliments Ciqual (ANSES)</span></div>
  <div><span class="v">1&nbsp;152</span><span class="u">Plats composés</span></div>
</div>
<p>À ces 438&nbsp;267 références s'ajoutent les produits à code-barres d'Open Food Facts. Macros, micronutriments, antioxydants : <strong>chaque valeur affichée dans l'app est traçable jusqu'à sa source officielle.</strong></p>

<h2>Du scan à la fiche, étape par étape</h2>
<ul>
<li><strong>La photo :</strong> tu prends ton repas en photo. Jusqu'à 3 photos par repas, fusionnées en une seule analyse, quand tout ne tient pas dans un seul cadre.</li>
<li><strong>La reconnaissance :</strong> l'IA identifie les aliments présents et estime la portion de chacun.</li>
<li><strong>Le rattachement :</strong> chaque aliment reconnu est rattaché à une fiche précise des bases officielles. C'est l'étape décisive : passé ce point, l'IA ne fournit plus aucun chiffre.</li>
<li><strong>Le calcul :</strong> les valeurs de chaque fiche sont ramenées à ta portion, puis additionnées pour donner le bilan du repas, et celui de ta journée.</li>
<li><strong>La correction :</strong> un aliment mal reconnu, une portion à revoir ? Tu corriges, et le calcul est refait avec la bonne fiche ou la bonne quantité.</li>
</ul>
<p>Deux autres portes d'entrée mènent aux mêmes bases. Le <strong>code-barres</strong> d'un produit emballé renvoie directement à sa fiche Open Food Facts. Et la <strong>recherche manuelle</strong> te permet de trouver un aliment dans le catalogue quand tu préfères le saisir toi-même.</p>

<h2>Pourquoi les valeurs ne viennent jamais de l'IA</h2>
<p>Il aurait été plus simple de demander à l'IA « combien de calories dans cette assiette ? ». Elle aurait répondu, avec aplomb. Mais un chiffre généré n'est pas un chiffre mesuré : il est plausible, invérifiable, et il peut changer d'une photo à l'autre du même plat.</p>
<p>D'où la séparation des rôles. L'IA fait ce qu'elle sait faire : reconnaître des aliments et estimer des quantités. Les bases font ce qu'elles savent faire : décrire la composition d'un aliment, fiche par fiche, avec une source identifiable. Le bénéfice est concret : quand un chiffre te surprend, il remonte à une fiche officielle, pas à l'intuition d'une machine.</p>
<p>Et pourquoi plusieurs bases plutôt qu'une ? Parce qu'aucune ne suffit seule. Ciqual apporte la rigueur de valeurs mesurées en laboratoire pour les aliments de base, mais elle ne décrit pas chaque produit du commerce. Open Food Facts connaît les produits emballés, marque par marque. USDA FoodData Central apporte le volume. Les croiser, c'est couvrir ton assiette sans sacrifier la rigueur.</p>

<h2>Ce que ta nutrition pèse dans ton score</h2>
<p>Tes repas ne servent pas qu'à tenir un journal. Ils nourrissent le pilier nutrition du <a href="/methode/readiness-score.html">Readiness Score</a>, qui vaut <strong>21 points sur 100</strong> et se note sur quatre critères :</p>
<ul>
<li><strong>L'adéquation à tes cibles — 40 %.</strong> Calories, protéines, glucides et lipides de la journée, face aux cibles calculées par le moteur <a href="/methode/cibles.html">Les cibles</a>.</li>
<li><strong>Le refuel après l'effort — 25 %.</strong> Les protéines que tu apportes après une séance, qui donnent au muscle les matériaux de sa réparation (<a href="/articles/que-manger-apres-le-sport.html">que manger après le sport</a>). Les jours de repos, ce critère est retiré et son poids est redistribué entre les autres.</li>
<li><strong>Les micronutriments — 20 %.</strong> La couverture de tes besoins, calculée à partir des valeurs des fiches officielles.</li>
<li><strong>L'hydratation — 15 %.</strong> Ton hydratation de la journée, face à ce qui est recommandé pour toi (<a href="/articles/combien-d-eau-boire-par-jour.html">combien d'eau boire par jour</a>).</li>
</ul>
<p>Une règle à part : <strong>si tu as bu de l'alcool la veille, le pilier est plafonné à 80 sur 100</strong>, même avec des repas irréprochables. L'alcool pèse sur la récupération, et aucune assiette ne l'efface.</p>
<p>Ta nutrition compte aussi à plus long terme : son score est l'un des modificateurs de ton <a href="/methode/age-biologique.html">âge biologique</a>, qu'il peut faire bouger dans un sens ou dans l'autre. Quant à ta cible calorique, elle n'a de sens que rapportée à ce que tu dépenses : la fiche <a href="/methode/depense-energetique.html">dépense énergétique</a> explique comment ta dépense est estimée.</p>

<h2>Les limites, sans maquillage</h2>
<p>Un moteur nutrition honnête doit dire ce qu'il ne sait pas faire.</p>
<ul>
<li><strong>Une photo ne pèse pas ton assiette :</strong> les portions sont estimées, avec une marge d'erreur. Un exemple : une fiche à 10&nbsp;g de protéines pour 100&nbsp;g, sur une portion estimée à 150&nbsp;g, donne 15&nbsp;g. Si la portion réelle pesait 200&nbsp;g, il en manque 5. C'est pour ça que tu peux corriger, et que la portion est la première chose à vérifier.</li>
<li><strong>Un aliment n'a pas une composition unique :</strong> les valeurs varient selon la variété, la cuisson, la marque. Une fiche décrit un aliment type, pas exactement celui de ton assiette.</li>
<li><strong>Toutes les sources n'ont pas le même statut :</strong> les valeurs Ciqual sont mesurées en laboratoire ; Open Food Facts est une base collaborative, où une erreur de saisie reste possible.</li>
<li><strong>Lis la tendance, pas le repas :</strong> une portion mal estimée un midi pèse peu sur une semaine ; une habitude qui se répète, elle, finit par se voir.</li>
</ul>

<h2>Ce que ce moteur n'est pas</h2>
<p>Ecleptic est un outil de bien-être, pas un dispositif médical. Le moteur nutrition te montre ce que tu manges et ce que ça t'apporte ; il ne pose aucun diagnostic, ne prescrit aucun régime et ne remplace pas un conseil diététique ou médical.</p>
<p>Si tu suis un régime lié à une maladie, si tu es enceinte, si tu prends un traitement, ou si ta relation à la nourriture devient une source d'angoisse, c'est un médecin ou un diététicien qu'il faut voir, pas une app. Et si un malaise ou un symptôme inhabituel apparaît, consulte ; en cas d'urgence, appelle le 15 ou le 112.</p>
""",
    "refs": [
        "ANSES, table de composition nutritionnelle des aliments Ciqual.",
        "USDA, base de données FoodData Central.",
        "Open Food Facts, base collaborative de produits alimentaires.",
    ],
    "faq": [
        {"q": "Comment une appli calcule-t-elle les calories d'un repas en photo ?",
         "a": "Dans Ecleptic, l'IA reconnaît les aliments sur la photo et estime leurs portions. Chaque aliment est ensuite rattaché à une fiche des bases officielles (table Ciqual de l'ANSES, USDA FoodData Central, Open Food Facts), et ce sont les valeurs de ces fiches, ramenées à ta portion, qui sont affichées."},
        {"q": "Les calories estimées sur une photo sont-elles fiables ?",
         "a": "Le point délicat est la portion : une photo ne pèse pas ton assiette, donc la quantité estimée a une marge d'erreur. Les valeurs nutritionnelles, elles, viennent de bases officielles et non d'une estimation de l'IA, et tu peux corriger un aliment ou une portion mal estimés. Pour juger ton alimentation, regarde la tendance sur plusieurs jours plutôt qu'un repas isolé."},
        {"q": "Quelle différence entre la table Ciqual et Open Food Facts ?",
         "a": "La table Ciqual est publiée par l'ANSES, l'agence sanitaire française : elle décrit des aliments génériques avec des valeurs mesurées en laboratoire. Open Food Facts est une base collaborative de produits à code-barres, qui donne les valeurs d'un produit précis d'une marque donnée. Ecleptic s'appuie sur les deux, avec USDA FoodData Central, et renvoie un code-barres scanné à sa fiche Open Food Facts."},
    ],
    "related": ["cibles", "readiness-score", "depense-energetique", "age-biologique"],
    "journal": ["proteines-par-jour-prise-de-muscle", "combien-de-calories-par-jour", "glucides-et-sport-combien", "magnesium-sport-fatigue"],
}
