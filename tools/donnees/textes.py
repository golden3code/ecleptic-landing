# -*- coding: utf-8 -*-
"""Textes éditoriaux des pages « aliments riches en … » (FR + EN).

Les classements chiffrés viennent de tools/donnees/ciqual.json (table Ciqual 2025 de
l'ANSES) ; ce fichier ne contient que ce qui entoure les tableaux. Vérifié le 30/09/2026 :
- valeurs de besoins lues dans les résumés des avis EFSA (DRV), la page « références
  nutritionnelles en vitamines et minéraux » de l'ANSES (21/02/2025), les pages ANSES
  protéines / lipides / oméga-3, l'avis ANSES 2016 sur les repères du PNNS, et les
  rapports DRI des National Academies (tableaux de synthèse lus sur nap.edu) ;
- VNR : règlement (UE) 1169/2011, annexe XIII partie A (protéines : apport de référence
  de 50 g, partie B) ; allégations fibres : règlement (CE) 1924/2006, annexe ;
- chaque valeur d'aliment citée dans les conseils et les FAQ est une valeur Ciqual 2025
  (pour 100 g), relue dans le fichier officiel.
Contrôle : python3 tools/check_sources.py tools/donnees/textes.py
"""

NB = " "  # espace insécable (séparateur de milliers)

# --- Sources communes ---------------------------------------------------------------
CIQUAL = {"t": "Anses. Table de composition nutritionnelle des aliments Ciqual 2025.",
          "u": "https://doi.org/10.5281/zenodo.17550133"}
REG_1169 = {"t": "Règlement (UE) n° 1169/2011 du Parlement européen et du Conseil du 25 octobre 2011 "
                 "concernant l'information des consommateurs sur les denrées alimentaires, annexe XIII. "
                 "Journal officiel de l'Union européenne. 2011.",
            "u": "https://eur-lex.europa.eu/eli/reg/2011/1169/oj"}
REG_1924 = {"t": "Règlement (CE) n° 1924/2006 du Parlement européen et du Conseil du 20 décembre 2006 "
                 "concernant les allégations nutritionnelles et de santé portant sur les denrées "
                 "alimentaires, annexe. Journal officiel de l'Union européenne. 2006.",
            "u": "https://eur-lex.europa.eu/eli/reg/2006/1924/oj"}
ANSES_VM = {"t": "Anses. Les références nutritionnelles en vitamines et minéraux. 2025.",
            "u": "https://www.anses.fr/fr/content/les-references-nutritionnelles-en-vitamines-et-mineraux"}
ANSES_PNNS = {"t": "Anses. Actualisation des repères du PNNS : révision des repères de consommations "
                   "alimentaires. Avis et rapport d'expertise collective. 2016.",
              "u": "https://www.anses.fr/fr/system/files/NUT2012SA0103Ra-1.pdf"}


def efsa(title, year, doi):
    return {"t": "EFSA Panel on Dietetic Products, Nutrition and Allergies (NDA). %s. EFSA Journal. %s." % (title, year),
            "u": "https://doi.org/" + doi}


def nasem(org, title, year, doi):
    return {"t": "%s. %s. National Academies Press. %s." % (org, title, year), "u": "https://doi.org/" + doi}


TEXTES = {
    # ================================================================================
    "proteines": {
        "fr": {
            "nom": "protéines",
            "title": "Aliments riches en protéines : le classement de la table Ciqual",
            "seo_title": "Aliments riches en protéines : le classement Ciqual",
            "description": "Les aliments les plus riches en protéines selon la table Ciqual de l'ANSES, pour 100 g et pour 100 kcal, et tes vrais besoins selon l'EFSA et le sport.",
            "role": "<p>Les protéines sont le matériau de construction de ton corps : muscles, peau, cheveux, ongles, "
                    "matrice des os. Elles font aussi tourner la machine, sous forme d'enzymes, d'hormones, d'anticorps "
                    "ou d'hémoglobine. Elles sont assemblées à partir de 20 acides aminés, dont 9 que ton corps ne sait "
                    "pas fabriquer en quantité suffisante : histidine, isoleucine, leucine, lysine, méthionine, "
                    "phénylalanine, thréonine, tryptophane et valine. Ceux-là, seule ton assiette peut les apporter. "
                    "Les protéines animales en contiennent généralement davantage et se digèrent un peu mieux que les "
                    "protéines végétales, rappelle l'ANSES.</p>",
            "besoins": "<p>Il n'existe pas de VNR pour les protéines : l'étiquetage européen utilise seulement un apport "
                       "de référence de 50 g par jour pour un adulte type (annexe XIII du règlement 1169/2011). Ton "
                       "besoin réel dépend de ton poids. L'EFSA (2012) et l'ANSES fixent la référence de l'adulte à "
                       "0,83 g par kilo et par jour, soit environ 58 g pour 70 kg, avec un supplément pendant la "
                       "grossesse et l'allaitement. Si tu t'entraînes, la position 2017 de l'International Society of "
                       "Sports Nutrition situe les besoins entre 1,4 et 2 g par kilo et par jour pour construire et "
                       "garder ton muscle. L'EFSA juge sûrs des apports allant jusqu'au double de la référence.</p>",
            "conseils": "<ul>"
                        "<li><strong>Regarde aussi les protéines pour 100 kcal.</strong> Le classement pour 100 g "
                        "favorise les aliments secs, comme le blanc d'œuf en poudre ou la morue séchée. Le classement "
                        "par densité montre ce que tu obtiens par calorie : dans la table Ciqual, les poissons blancs "
                        "cuits (sole, lieu, cabillaud) dépassent 23 g de protéines pour 100 kcal.</li>"
                        "<li><strong>Répartis-les sur la journée.</strong> L'ISSN conseille environ 0,25 g de protéines "
                        "de qualité par kilo et par repas, soit 20 à 40 g, idéalement toutes les 3 à 4 heures.</li>"
                        "<li><strong>Végétarien ? Pas besoin de tout combiner.</strong> Les céréales manquent de lysine "
                        "et les légumineuses d'acides aminés soufrés, mais l'ANSES estime qu'avec des sources variées, "
                        "rien ne justifie d'associer systématiquement céréales et légumineuses. 100 g de lentilles "
                        "cuites apportent environ 10 g de protéines (Ciqual).</li>"
                        "<li><strong>Les aliments d'abord.</strong> L'ISSN rappelle qu'on peut couvrir ses besoins avec "
                        "des aliments ; la poudre n'est qu'une solution pratique quand le volume d'entraînement est "
                        "élevé.</li>"
                        "</ul>",
            "faq": [
                {"q": "Combien de protéines par jour ?",
                 "a": "Pour un adulte, la référence de l'EFSA et de l'ANSES est de 0,83 g par kilo de poids et par jour, "
                      "soit environ 58 g pour 70 kg. Si tu fais de la musculation ou beaucoup de sport, l'International "
                      "Society of Sports Nutrition situe les besoins entre 1,4 et 2 g par kilo, soit 98 à 140 g pour "
                      "70 kg."},
                {"q": "Quels aliments végétaux sont les plus riches en protéines ?",
                 "a": "Dans la table Ciqual, le soja en graine (36,5 g pour 100 g), le lupin sec (36,2 g), le chanvre "
                      "décortiqué (30,8 g) et la lentille corail sèche (27,7 g) arrivent en tête. Attention à l'état : "
                      "une fois cuites, les lentilles absorbent de l'eau et n'apportent plus qu'environ 10 g pour "
                      "100 g."},
            ],
        },
        "en": {
            "nom": "protein",
            "title": "Foods high in protein: ranked by France's official Ciqual table",
            "seo_title": "Foods high in protein: the official Ciqual ranking",
            "description": "The foods highest in protein in France's official Ciqual table, per 100 g and per 100 kcal, plus how much you really need according to EFSA and sports science.",
            "role": "<p>Protein is what your body is built from: muscle, skin, hair, nails and the matrix of your "
                    "bones. It also keeps the machinery running as enzymes, hormones, antibodies and hemoglobin. "
                    "Proteins are assembled from 20 amino acids, and 9 of them your body can't make in sufficient "
                    "amounts: histidine, isoleucine, leucine, lysine, methionine, phenylalanine, threonine, "
                    "tryptophan and valine. Those can only come from your plate. As France's food safety agency "
                    "ANSES points out, animal proteins generally contain more of them and are slightly more "
                    "digestible than plant proteins.</p>",
            "besoins": "<p>There is no nutrient reference value (NRV) for protein: EU labels only use a reference "
                       "intake of 50 g a day for an average adult (Regulation 1169/2011, Annex XIII). Your real need "
                       "scales with your weight. EFSA (2012) sets the adult reference at 0.83 g per kg of body weight "
                       "per day (about 0.38 g per lb), roughly 58 g for a 70 kg (154 lb) adult, with extra during "
                       "pregnancy and breastfeeding. If you train, the International Society of Sports Nutrition's "
                       "2017 position stand puts the range at 1.4 to 2.0 g per kg a day to build and maintain "
                       "muscle. EFSA considers intakes up to twice the reference safe.</p>",
            "conseils": "<ul>"
                        "<li><strong>Look at protein per 100 kcal too.</strong> Ranking per 100 g favors dried foods "
                        "like egg white powder or salt cod. The density ranking shows what you get per calorie: in the "
                        "Ciqual table, cooked white fish (sole, pollack, cod) deliver more than 23 g of protein per "
                        "100 kcal.</li>"
                        "<li><strong>Spread it over the day.</strong> The ISSN suggests about 0.25 g of high-quality "
                        "protein per kg per meal, or 20 to 40 g, ideally every 3 to 4 hours.</li>"
                        "<li><strong>Vegetarian? No need to combine at every meal.</strong> Grains are low in lysine "
                        "and legumes in sulfur amino acids, but ANSES sees no reason to systematically pair them when "
                        "your sources are varied. 100 g (3.5 oz) of cooked lentils provides about 10 g of protein "
                        "(Ciqual).</li>"
                        "<li><strong>Food first.</strong> The ISSN notes that you can meet your needs with whole foods; "
                        "powders are just a practical option when training volume is high.</li>"
                        "</ul>",
            "faq": [
                {"q": "How much protein do I need per day?",
                 "a": "For an adult, EFSA's reference is 0.83 g per kg of body weight per day, about 58 g for a 70 kg "
                      "(154 lb) person. If you lift weights or train a lot, the International Society of Sports "
                      "Nutrition puts the range at 1.4 to 2.0 g per kg, or 98 to 140 g for 70 kg."},
                {"q": "Which plant foods are highest in protein?",
                 "a": "In the Ciqual table, whole soybeans (36.5 g per 100 g), dried lupin (36.2 g), hulled hemp seeds "
                      "(30.8 g) and dried red lentils (27.7 g) come out on top. Mind the state they're in: once cooked, "
                      "lentils soak up water and drop to about 10 g per 100 g."},
            ],
        },
        "sources": [
            CIQUAL,
            efsa("Scientific Opinion on Dietary Reference Values for protein", 2012, "10.2903/j.efsa.2012.2557"),
            {"t": "Anses. Protéines : rôle, sources et apports recommandés. 2025.",
             "u": "https://www.anses.fr/fr/content/proteines-role-sources-et-apports-recommandes"},
            {"t": "Jäger R, Kerksick CM, Campbell BI, et al. International Society of Sports Nutrition Position "
                  "Stand: protein and exercise. J Int Soc Sports Nutr. 2017.",
             "u": "https://doi.org/10.1186/s12970-017-0177-8"},
            REG_1169,
        ],
        "articles": ["proteines-par-jour-prise-de-muscle", "que-manger-apres-le-sport"],
        "methode": ["nutrition", "cibles"],
    },
    # ================================================================================
    "fer": {
        "fr": {
            "nom": "fer",
            "title": "Aliments riches en fer : le classement de la table Ciqual",
            "seo_title": "Aliments riches en fer : le classement Ciqual",
            "description": "Les aliments les plus riches en fer selon la table Ciqual de l'ANSES, tes besoins selon l'EFSA, et comment mieux absorber le fer des végétaux au quotidien.",
            "role": "<p>Le fer sert d'abord à transporter l'oxygène et à l'utiliser dans tes cellules. Ton corps le "
                    "recycle très bien, mais il ne sait pas éliminer un excès : tout se règle à l'absorption. Dans "
                    "l'assiette, il existe sous deux formes. Le fer héminique, présent seulement dans la viande, les "
                    "abats, le poisson et les fruits de mer, est le mieux absorbé. Le fer non héminique, présent dans "
                    "presque tous les aliments, végétaux compris, l'est moins, et son absorption dépend du reste du "
                    "repas et de tes réserves. Un manque prolongé peut conduire à une anémie par carence en fer.</p>",
            "besoins": "<p>Sur les étiquettes, la VNR européenne du fer est de 14 mg par jour (règlement 1169/2011). "
                       "Tes besoins réels dépendent surtout des règles. Selon l'EFSA (2015), la référence est de 11 mg "
                       "par jour pour les hommes et les femmes ménopausées, de 16 mg pour les femmes non ménopausées, "
                       "grossesse et allaitement compris, et de 13 mg pour les adolescentes. L'ANSES reprend ces "
                       "valeurs mais distingue les femmes aux règles peu à modérément abondantes (11 mg) de celles "
                       "aux règles abondantes (16 mg). Ces chiffres tiennent compte du fait que tu n'absorbes qu'une "
                       "petite partie du fer de ton assiette : 16 à 18 % dans les calculs de l'EFSA.</p>",
            "conseils": "<ul>"
                        "<li><strong>Associe la vitamine C au fer végétal.</strong> Elle favorise l'absorption du fer "
                        "non héminique, rappelle l'ANSES : un poivron cru ou un kiwi au repas de lentilles, c'est utile. "
                        "C'est d'autant plus important que le fer d'une alimentation végétarienne est moins bien "
                        "absorbé : 5 à 12 %, contre 14 à 18 % pour une alimentation mixte, selon Hurrell et Egli "
                        "(2010).</li>"
                        "<li><strong>Décale le thé et le café.</strong> Les polyphénols, comme le calcium et les phytates, "
                        "freinent l'absorption du fer dans les études sur un repas ; sur une alimentation variée, l'effet "
                        "est plus modeste (Hurrell et Egli, 2010). Si tu manques de fer, garde ton thé ou ton café à "
                        "distance des repas.</li>"
                        "<li><strong>Lis le classement avec un œil critique.</strong> Céréales enrichies et chocolat "
                        "noir montent haut pour 100 g, mais leur fer est non héminique, donc moins bien absorbé. Le "
                        "boudin noir, le foie, les coques et les palourdes apportent du fer héminique.</li>"
                        "<li><strong>Fatigue qui dure ? Médecin avant complément.</strong> L'ANSES cite comme plus "
                        "exposés les enfants, les femmes enceintes, les femmes aux règles abondantes et les personnes "
                        "qui absorbent mal le fer. Ne prends pas de fer de ton propre chef : un excès n'est pas "
                        "anodin, et une prise de sang prescrite par ton médecin tranche.</li>"
                        "</ul>",
            "faq": [
                {"q": "Combien de fer par jour pour une femme ?",
                 "a": "Selon l'EFSA, 16 mg par jour avant la ménopause, grossesse et allaitement compris, puis 11 mg "
                      "après la ménopause, comme pour un homme. L'ANSES retient 11 mg pour les femmes dont les règles "
                      "sont peu ou modérément abondantes. La VNR de 14 mg imprimée sur les étiquettes est une valeur "
                      "d'étiquetage, pas un besoin individuel."},
                {"q": "Le thé empêche-t-il l'absorption du fer ?",
                 "a": "Il la freine. Les polyphénols, abondants dans le thé et le café, font partie des composés qui "
                      "réduisent l'absorption du fer non héminique dans les études sur un repas ; sur une alimentation "
                      "variée, l'effet est plus modeste (Hurrell et Egli, 2010). Si tu manques de fer, boire ton thé à "
                      "distance des repas est une précaution simple."},
            ],
        },
        "en": {
            "nom": "iron",
            "title": "Foods high in iron: ranked by France's official Ciqual table",
            "seo_title": "Foods high in iron: the official Ciqual ranking",
            "description": "The foods highest in iron in France's official Ciqual table, how much you need according to EFSA, and how to absorb more of the iron in plant foods.",
            "role": "<p>Iron's main job is carrying oxygen and helping your cells use it. Your body recycles it very "
                    "efficiently but has no way to get rid of an excess, so everything is regulated at absorption. "
                    "Food contains two forms. Heme iron, found only in meat, organ meats, fish and shellfish, is the "
                    "best absorbed. Non-heme iron, found in almost every food including plants, is absorbed less "
                    "well, and how much you take in depends on the rest of the meal and on your iron stores. A "
                    "long-lasting shortfall can lead to iron-deficiency anemia.</p>",
            "besoins": "<p>On EU labels, the nutrient reference value (NRV) for iron is 14 mg a day (Regulation "
                       "1169/2011). Your real needs depend mostly on menstruation. According to EFSA (2015), the "
                       "population reference intake is 11 mg a day for men and postmenopausal women, 16 mg for women "
                       "before menopause, including during pregnancy and breastfeeding, and 13 mg for teenage girls. "
                       "France's ANSES uses the same figures but separates women with light to moderate periods "
                       "(11 mg) from those with heavy periods (16 mg). These numbers already account for the fact "
                       "that you absorb only a small share of dietary iron: 16 to 18% in EFSA's calculations.</p>",
            "conseils": "<ul>"
                        "<li><strong>Pair plant iron with vitamin C.</strong> It boosts non-heme iron absorption, ANSES "
                        "notes: raw bell pepper or a kiwi with your lentils helps. It matters all the more because iron "
                        "from vegetarian diets is less available: 5 to 12%, versus 14 to 18% for mixed diets, according "
                        "to Hurrell and Egli (2010).</li>"
                        "<li><strong>Keep tea and coffee away from meals.</strong> Polyphenols, like calcium and phytates, "
                        "reduce iron absorption in single-meal studies; across a varied diet the effect is smaller "
                        "(Hurrell and Egli, 2010). If your iron is low, drink them between meals.</li>"
                        "<li><strong>Read the ranking critically.</strong> Fortified cereals and dark chocolate rank high "
                        "per 100 g, but their iron is non-heme and less well absorbed. Black pudding, liver, cockles and "
                        "clams provide heme iron.</li>"
                        "<li><strong>Tired all the time? Doctor before supplements.</strong> ANSES lists children, "
                        "pregnant women, women with heavy periods and people with poor absorption as most at risk. "
                        "Don't start iron on your own: too much is harmful, and a blood test ordered by your doctor "
                        "gives the answer.</li>"
                        "</ul>",
            "faq": [
                {"q": "How much iron does a woman need per day?",
                 "a": "According to EFSA, 16 mg a day before menopause, including during pregnancy and breastfeeding, "
                      "then 11 mg after menopause, the same as men. France's ANSES sets 11 mg for women with light to "
                      "moderate periods. The 14 mg NRV printed on EU labels is a labeling value, not an individual "
                      "requirement."},
                {"q": "Does tea block iron absorption?",
                 "a": "It reduces it. Polyphenols, plentiful in tea and coffee, are among the compounds that lower "
                      "non-heme iron absorption in single-meal studies; across a varied diet the effect is more modest "
                      "(Hurrell and Egli, 2010). If your iron is low, drinking tea between meals is an easy precaution."},
            ],
        },
        "sources": [
            CIQUAL,
            efsa("Scientific Opinion on Dietary Reference Values for iron", 2015, "10.2903/j.efsa.2015.4254"),
            ANSES_VM,
            REG_1169,
            {"t": "Hurrell R, Egli I. Iron bioavailability and dietary reference values. Am J Clin Nutr. 2010.",
             "u": "https://doi.org/10.3945/ajcn.2010.28674F"},
        ],
        "articles": ["carence-en-fer-fatigue", "toujours-fatigue-causes"],
        "methode": ["nutrition"],
    },
    # ================================================================================
    "magnesium": {
        "fr": {
            "nom": "magnésium",
            "title": "Aliments riches en magnésium : le classement de la table Ciqual",
            "seo_title": "Aliments riches en magnésium : le classement Ciqual",
            "description": "Les aliments les plus riches en magnésium selon la table Ciqual de l'ANSES, tes besoins selon l'EFSA et l'ANSES, et les gestes simples pour en manger plus.",
            "role": "<p>Le magnésium participe à plus de 300 systèmes enzymatiques. Il intervient dans la production "
                    "d'énergie et dans toutes les réactions qui utilisent l'ATP, le carburant de tes cellules, mais "
                    "aussi dans le maintien du potentiel électrique des membranes, le transport des ions et le "
                    "métabolisme du calcium. Un adulte en contient environ 25 g, dont 50 à 60 % dans les os et un "
                    "quart dans les muscles ; seul 1 % se trouve hors des cellules. Une vraie déficience peut faire "
                    "chuter le calcium et le potassium du sang, avec des symptômes cardiaques et neurologiques.</p>",
            "besoins": "<p>La VNR européenne est de 375 mg par jour (règlement 1169/2011). Faute de données pour "
                       "calculer un besoin moyen, l'EFSA (2015) a fixé un apport satisfaisant de 350 mg par jour pour "
                       "les hommes et 300 mg pour les femmes, sans supplément pendant la grossesse ou l'allaitement. "
                       "L'ANSES retient 380 mg pour les hommes et 300 mg pour les femmes. Les références américaines "
                       "sont plus hautes : 400 à 420 mg pour les hommes, 310 à 320 mg pour les femmes. L'ANSES fixe "
                       "aussi une limite de sécurité, mais elle ne vise que le magnésium des compléments et des "
                       "aliments enrichis, pas celui naturellement présent dans les aliments.</p>",
            "conseils": "<ul>"
                        "<li><strong>Passe au complet.</strong> Dans la table Ciqual, le riz complet cuit apporte 58 mg "
                        "de magnésium pour 100 g, contre 9 mg pour le riz blanc cuit ; les pâtes complètes cuites, "
                        "46 mg contre 22 mg pour les pâtes classiques.</li>"
                        "<li><strong>Graines et oléagineux en collation.</strong> Graines de courge (592 mg pour 100 g), "
                        "noix du Brésil (376 mg), noix de cajou et amandes (autour de 280 mg) : une petite poignée pèse "
                        "vite dans ta journée. Le chocolat noir à 70 % en apporte 200 mg pour 100 g.</li>"
                        "<li><strong>Regarde l'étiquette de ton eau.</strong> L'ANSES compte certaines eaux minérales "
                        "parmi les sources de magnésium, avec les oléagineux, le chocolat, le café, les céréales "
                        "complètes, les mollusques et les crustacés.</li>"
                        "<li><strong>Complément : demande avant.</strong> La limite de sécurité de l'ANSES porte "
                        "justement sur le magnésium des compléments : parles-en à ton médecin ou à ton pharmacien avant "
                        "d'en prendre.</li>"
                        "</ul>",
            "faq": [
                {"q": "Combien de magnésium par jour ?",
                 "a": "L'EFSA fixe 350 mg par jour pour un homme et 300 mg pour une femme ; l'ANSES retient 380 mg pour "
                      "un homme et 300 mg pour une femme. Sur les étiquettes, la VNR est de 375 mg. Oléagineux, céréales "
                      "complètes, chocolat, fruits de mer et certaines eaux minérales sont les principales sources selon "
                      "l'ANSES."},
                {"q": "Le chocolat noir est-il riche en magnésium ?",
                 "a": "Oui : la table Ciqual donne 200 mg pour 100 g de chocolat noir à 70 % de cacao, soit plus de la "
                      "moitié de la VNR. Mais 20 g de chocolat n'en apportent qu'environ 40 mg, avec du sucre et des "
                      "graisses en prime. C'est un plus, pas une stratégie : les graines, les noix et les céréales "
                      "complètes font mieux."},
            ],
        },
        "en": {
            "nom": "magnesium",
            "title": "Foods high in magnesium: ranked by France's official Ciqual table",
            "seo_title": "Foods high in magnesium: the official Ciqual ranking",
            "description": "The foods highest in magnesium in France's official Ciqual table, how much you need according to EFSA and US guidelines, and easy ways to eat more.",
            "role": "<p>Magnesium takes part in more than 300 enzyme systems. It is involved in energy production and "
                    "every reaction that uses ATP, your cells' fuel, as well as in keeping cell membranes electrically "
                    "charged, moving ions around and handling calcium. An adult body holds about 25 g, 50 to 60% of "
                    "it in bone and a quarter in muscle; only 1% sits outside the cells. A true deficiency can drag "
                    "down blood calcium and potassium, with heart and nerve symptoms.</p>",
            "besoins": "<p>The EU nutrient reference value (NRV) is 375 mg a day (Regulation 1169/2011). Without enough "
                       "data to calculate an average requirement, EFSA (2015) set an adequate intake of 350 mg a day "
                       "for men and 300 mg for women, with no increase during pregnancy or breastfeeding. France's "
                       "ANSES uses 380 mg for men and 300 mg for women. US recommended dietary allowances are higher: "
                       "400 to 420 mg for men and 310 to 320 mg for women, depending on age. ANSES also sets a safety "
                       "limit, but it applies only to magnesium from supplements and fortified foods, not to the "
                       "magnesium naturally present in food.</p>",
            "conseils": "<ul>"
                        "<li><strong>Go whole grain.</strong> In the Ciqual table, cooked brown rice provides 58 mg of "
                        "magnesium per 100 g (3.5 oz), versus 9 mg for cooked white rice; cooked whole-wheat pasta, "
                        "46 mg versus 22 mg for regular pasta.</li>"
                        "<li><strong>Snack on seeds and nuts.</strong> Pumpkin seeds (592 mg per 100 g), Brazil nuts "
                        "(376 mg), cashews and almonds (around 280 mg): a small handful adds up fast. Dark chocolate "
                        "with 70% cocoa provides 200 mg per 100 g.</li>"
                        "<li><strong>Check your water label.</strong> ANSES counts some mineral waters among magnesium "
                        "sources, alongside nuts and seeds, chocolate, coffee, whole grains and shellfish.</li>"
                        "<li><strong>Supplements: ask first.</strong> The ANSES safety limit targets supplemental "
                        "magnesium specifically, so talk to your doctor or pharmacist before taking any.</li>"
                        "</ul>",
            "faq": [
                {"q": "How much magnesium do I need per day?",
                 "a": "EFSA sets 350 mg a day for men and 300 mg for women; France's ANSES uses 380 mg for men. In the "
                      "US, the recommended dietary allowance is 400 to 420 mg for men and 310 to 320 mg for women. On EU "
                      "labels, the NRV is 375 mg."},
                {"q": "Is dark chocolate high in magnesium?",
                 "a": "Yes: the Ciqual table lists 200 mg per 100 g for 70% dark chocolate, more than half the EU NRV. "
                      "But 20 g (0.7 oz) only provides about 40 mg, along with sugar and fat. It's a bonus, not a "
                      "strategy: seeds, nuts and whole grains do better."},
            ],
        },
        "sources": [
            CIQUAL,
            efsa("Scientific Opinion on Dietary Reference Values for magnesium", 2015, "10.2903/j.efsa.2015.4186"),
            ANSES_VM,
            REG_1169,
            nasem("Institute of Medicine", "Dietary Reference Intakes for Calcium, Phosphorus, Magnesium, Vitamin D, "
                  "and Fluoride", 1997, "10.17226/5776"),
        ],
        "articles": ["magnesium-sport-fatigue"],
        "methode": ["nutrition"],
    },
    # ================================================================================
    "calcium": {
        "fr": {
            "nom": "calcium",
            "title": "Aliments riches en calcium : le classement de la table Ciqual",
            "seo_title": "Aliments riches en calcium : le classement Ciqual",
            "description": "Les aliments les plus riches en calcium selon la table Ciqual de l'ANSES, tes besoins selon l'EFSA, et pourquoi celui des épinards compte moins qu'on le croit.",
            "role": "<p>Le calcium est le minéral le plus abondant de ton corps : 1 à 2 % de ton poids, dont 99 % "
                    "dans le squelette. Il donne aux os et aux dents leur solidité, mais il sert aussi à "
                    "l'excitabilité des nerfs et des muscles, à la coagulation du sang, à la libération des hormones "
                    "et à l'activation de nombreuses enzymes. Son taux sanguin est réglé très finement, en lien avec "
                    "les réserves de l'os. À long terme, des apports insuffisants réduisent la masse osseuse et "
                    "augmentent le risque de fracture. La vitamine D, elle, favorise son absorption.</p>",
            "besoins": "<p>La VNR européenne est de 800 mg par jour (règlement 1169/2011). Les références de l'EFSA "
                       "(2015), reprises par l'ANSES, sont plus élevées : 950 mg par jour à partir de 25 ans, 1" + NB +
                       "000 mg entre 18 et 24 ans, quand l'os continue de se charger en calcium, et 1" + NB + "150 mg "
                       "de 11 à 17 ans. Grossesse et allaitement ne changent pas ces valeurs : le métabolisme du "
                       "calcium s'adapte. À l'inverse, l'ANSES fixe une limite de sécurité de 2" + NB + "500 mg par "
                       "jour chez l'adulte : plus n'est pas toujours mieux.</p>",
            "conseils": "<ul>"
                        "<li><strong>Les laitages restent les plus simples.</strong> D'après la table Ciqual, un verre "
                        "de lait demi-écrémé (250 ml) apporte environ 300 mg, un yaourt nature de 125 g environ 170 mg "
                        "et 30 g de comté environ 270 mg.</li>"
                        "<li><strong>Tous les légumes ne se valent pas.</strong> Le calcium du chou kale, pauvre en "
                        "oxalates, est très bien absorbé : un peu mieux que celui du lait dans une étude de 1990 (41 % "
                        "contre 32 %). Celui des épinards l'est mal, même si la table Ciqual affiche 240 mg pour 100 g "
                        "d'épinards bouillis.</li>"
                        "<li><strong>Pense aux graines, aux sardines et à l'eau.</strong> Le sésame (962 mg pour 100 g), "
                        "le tahin (284 mg) et les sardines à l'huile en boîte (432 mg) comptent ; l'ANSES cite aussi "
                        "certaines eaux dures, riches en calcium et en magnésium.</li>"
                        "<li><strong>Soigne ta vitamine D.</strong> Elle favorise l'absorption du calcium (ANSES) : les "
                        "deux vont ensemble, en particulier à l'adolescence, quand les besoins sont les plus hauts "
                        "selon l'EFSA.</li>"
                        "</ul>",
            "faq": [
                {"q": "Combien de calcium par jour ?",
                 "a": "Selon l'EFSA et l'ANSES, 950 mg par jour pour un adulte à partir de 25 ans, 1 000 mg entre 18 et "
                      "24 ans et 1 150 mg de 11 à 17 ans. La VNR des étiquettes, 800 mg, est plus basse : un aliment à "
                      "100 % de la VNR ne couvre donc pas tout ton besoin."},
                {"q": "Quels aliments riches en calcium sans produits laitiers ?",
                 "a": "Dans la table Ciqual, le sésame (962 mg pour 100 g) et le tahin (284 mg), les sardines à l'huile "
                      "en boîte (432 mg), le chou kale (254 mg), les amandes (260 mg) et le tofu nature "
                      "(100 mg) sont de bonnes options. Préfère les légumes pauvres en oxalates, comme le kale, aux "
                      "épinards, dont le calcium est mal absorbé."},
            ],
        },
        "en": {
            "nom": "calcium",
            "title": "Foods high in calcium: ranked by France's official Ciqual table",
            "seo_title": "Foods high in calcium: the official Ciqual ranking",
            "description": "The foods highest in calcium in France's official Ciqual table, how much you need according to EFSA, and why spinach calcium counts less than it seems.",
            "role": "<p>Calcium is the most abundant mineral in your body: 1 to 2% of your weight, 99% of it in your "
                    "skeleton. It gives bones and teeth their strength, but it also drives nerve and muscle "
                    "excitability, blood clotting, hormone release and the activation of many enzymes. Blood calcium "
                    "is kept within a tight range, in close connection with bone stores. Over the long run, low "
                    "intakes reduce bone mass and raise the risk of fractures. Vitamin D helps you absorb it.</p>",
            "besoins": "<p>The EU nutrient reference value (NRV) is 800 mg a day (Regulation 1169/2011). EFSA's 2015 "
                       "reference intakes, also used in France by ANSES, are higher: 950 mg a day from age 25, 1,000 mg "
                       "between 18 and 24, while bones are still building up calcium, and 1,150 mg from 11 to 17. "
                       "Pregnancy and breastfeeding don't change these values, because calcium metabolism adapts. On "
                       "the other side, ANSES sets a safety limit of 2,500 mg a day for adults: more isn't always "
                       "better.</p>",
            "conseils": "<ul>"
                        "<li><strong>Dairy is the easy route.</strong> Based on the Ciqual table, a 250 ml (8.5 fl oz) "
                        "glass of semi-skimmed milk provides about 300 mg, a 125 g plain yogurt about 170 mg and 30 g "
                        "(1 oz) of Comté cheese about 270 mg.</li>"
                        "<li><strong>Not all greens are equal.</strong> Calcium from kale, a low-oxalate vegetable, is "
                        "absorbed very well: slightly better than milk calcium in a 1990 study (41% versus 32%). Spinach "
                        "calcium is poorly absorbed, even though the Ciqual table lists 240 mg per 100 g of boiled "
                        "spinach.</li>"
                        "<li><strong>Think seeds, sardines and water.</strong> Sesame seeds (962 mg per 100 g), tahini "
                        "(284 mg) and canned sardines in oil (432 mg) all count; ANSES also mentions some hard mineral "
                        "waters rich in calcium and magnesium.</li>"
                        "<li><strong>Mind your vitamin D.</strong> It helps calcium absorption (ANSES): the two go "
                        "together, especially in the teenage years, when EFSA's reference intakes are highest.</li>"
                        "</ul>",
            "faq": [
                {"q": "How much calcium do I need per day?",
                 "a": "According to EFSA, 950 mg a day for adults from age 25, 1,000 mg between 18 and 24, and 1,150 mg "
                      "from 11 to 17. The EU label NRV, 800 mg, is lower, so a food providing 100% of the NRV doesn't "
                      "cover your whole need."},
                {"q": "What are good non-dairy sources of calcium?",
                 "a": "In the Ciqual table, sesame seeds (962 mg per 100 g) and tahini (284 mg), canned sardines in oil "
                      "(432 mg), kale (254 mg), almonds (260 mg) and plain tofu (100 mg) are good options. Choose "
                      "low-oxalate greens such as kale over spinach, whose calcium is poorly absorbed."},
            ],
        },
        "sources": [
            CIQUAL,
            efsa("Scientific Opinion on Dietary Reference Values for calcium", 2015, "10.2903/j.efsa.2015.4101"),
            ANSES_VM,
            REG_1169,
            {"t": "Heaney RP, Weaver CM. Calcium absorption from kale. Am J Clin Nutr. 1990.",
             "u": "https://doi.org/10.1093/ajcn/51.4.656"},
        ],
        "articles": ["vitamine-d-fatigue", "menopause-et-sport"],
        "methode": ["nutrition"],
    },
    # ================================================================================
    "fibres": {
        "fr": {
            "nom": "fibres",
            "title": "Aliments riches en fibres : le classement de la table Ciqual",
            "seo_title": "Aliments riches en fibres : le classement Ciqual",
            "description": "Les aliments les plus riches en fibres selon la table Ciqual de l'ANSES, combien en manger selon l'EFSA et l'ANSES, et comment atteindre 30 g par jour.",
            "role": "<p>Les fibres sont des glucides que ton intestin grêle ne digère pas, auxquels s'ajoute la "
                    "lignine : elles arrivent intactes dans le côlon. Leur effet le plus direct concerne le transit. "
                    "Mais leur intérêt va plus loin. Dans une série de méta-analyses publiée dans The Lancet en 2019 "
                    "(185 études prospectives, 58 essais cliniques), les plus gros mangeurs de fibres présentaient 15 "
                    "à 30 % de risque en moins de mortalité, de maladie coronarienne, d'AVC, de diabète de type 2 et "
                    "de cancer colorectal que les plus petits mangeurs. Les essais montraient aussi un poids, une "
                    "tension et un cholestérol plus bas.</p>",
            "besoins": "<p>Il n'existe pas de VNR pour les fibres. Le seul repère des étiquettes vient des allégations "
                       "(règlement 1924/2006) : « source de fibres » à partir de 3 g pour 100 g, « riche en fibres » à "
                       "partir de 6 g. Côté besoins, l'EFSA (2010) juge 25 g par jour suffisants pour un transit "
                       "normal chez l'adulte. L'ANSES (2016) vise 30 g par jour, car la baisse du risque de maladies "
                       "cardiovasculaires, de diabète de type 2 et de cancers du côlon et du sein apparaît parfois dès "
                       "25 g et de façon plus nette à 30 g. La méta-analyse du Lancet situe le bénéfice le plus marqué "
                       "entre 25 et 29 g par jour.</p>",
            "conseils": "<ul>"
                        "<li><strong>Remplace le raffiné par le complet.</strong> L'ANSES recommande des féculents "
                        "complets chaque jour. Dans la table Ciqual, les pâtes complètes cuites apportent 5,1 g de "
                        "fibres pour 100 g, contre 2,2 g pour les pâtes classiques ; le pain complet 7,3 g, contre 2,7 g "
                        "pour le pain blanc.</li>"
                        "<li><strong>Des légumineuses plusieurs fois par semaine.</strong> L'ANSES juge leur consommation "
                        "actuelle insuffisante. Même cuits, haricots rouges, lentilles et pois chiches apportent 8 à "
                        "12 g de fibres pour 100 g (Ciqual).</li>"
                        "<li><strong>Ajoute des graines.</strong> Chia (34,4 g pour 100 g) et lin (26,9 g) dominent le "
                        "classement Ciqual : une cuillère dans un yaourt ou un bol de flocons fait vite la "
                        "différence.</li>"
                        "<li><strong>Plus de fruits et de légumes.</strong> L'ANSES estime leur consommation moyenne "
                        "insuffisante et demande de l'augmenter nettement, en privilégiant les légumes.</li>"
                        "</ul>",
            "faq": [
                {"q": "Combien de fibres par jour ?",
                 "a": "L'ANSES recommande 30 g par jour pour un adulte, l'EFSA considère 25 g comme suffisants pour le "
                      "transit. Une grande méta-analyse publiée dans The Lancet en 2019 situe le bénéfice le plus marqué "
                      "entre 25 et 29 g par jour, et suggère que davantage pourrait protéger encore plus."},
                {"q": "Quels fruits sont les plus riches en fibres ?",
                 "a": "Parmi les fruits frais de la table Ciqual, le fruit de la passion (6,8 g pour 100 g), la goyave "
                      "(5,4 g), la mûre (5,2 g), la groseille (4,6 g) et la framboise (4,3 g) sont en tête. Les fruits "
                      "secs vont plus haut, comme la figue sèche (8,15 g), mais leurs sucres sont concentrés de la même "
                      "façon."},
            ],
        },
        "en": {
            "nom": "fiber",
            "title": "Foods high in fiber: ranked by France's official Ciqual table",
            "seo_title": "Foods high in fiber: the official Ciqual ranking",
            "description": "The foods highest in fiber in France's official Ciqual table, how much to eat according to EFSA and ANSES, and practical ways to reach 25 to 30 g a day.",
            "role": "<p>Fiber is the carbohydrate your small intestine can't digest, plus lignin: it reaches your colon "
                    "intact. Its most direct effect is on bowel regularity. But the benefits go further. In a "
                    "series of meta-analyses published in The Lancet in 2019 (185 prospective studies, 58 clinical "
                    "trials), people eating the most fiber had a 15 to 30% lower risk of death, coronary heart "
                    "disease, stroke, type 2 diabetes and colorectal cancer than those eating the least. The trials "
                    "also showed lower body weight, blood pressure and cholesterol with higher intakes.</p>",
            "besoins": "<p>There is no nutrient reference value (NRV) for fiber. The only label benchmark comes from EU "
                       "nutrition claims (Regulation 1924/2006): \"source of fibre\" from 3 g per 100 g, \"high "
                       "fibre\" from 6 g. As for needs, EFSA (2010) considers 25 g a day adequate for normal bowel "
                       "function in adults. France's ANSES (2016) aims for 30 g a day, because the lower risk of "
                       "cardiovascular disease, type 2 diabetes and colon and breast cancer sometimes appears from "
                       "25 g and more consistently at 30 g. The Lancet meta-analysis found the greatest benefit "
                       "between 25 and 29 g a day.</p>",
            "conseils": "<ul>"
                        "<li><strong>Swap refined for whole grain.</strong> ANSES recommends whole-grain starches every "
                        "day. In the Ciqual table, cooked whole-wheat pasta provides 5.1 g of fiber per 100 g (3.5 oz), "
                        "versus 2.2 g for regular pasta; whole-wheat bread 7.3 g, versus 2.7 g for white bread.</li>"
                        "<li><strong>Legumes several times a week.</strong> ANSES considers current intake too low. Even "
                        "cooked, kidney beans, lentils and chickpeas provide 8 to 12 g of fiber per 100 g (Ciqual).</li>"
                        "<li><strong>Add seeds.</strong> Chia (34.4 g per 100 g) and flaxseed (26.9 g) top the Ciqual "
                        "ranking: a spoonful in yogurt or oatmeal quickly makes a difference.</li>"
                        "<li><strong>More fruit and vegetables.</strong> ANSES finds average intake too low and calls for "
                        "a clear increase, favoring vegetables.</li>"
                        "</ul>",
            "faq": [
                {"q": "How much fiber should I eat per day?",
                 "a": "EFSA considers 25 g a day adequate for normal bowel function in adults, and France's ANSES "
                      "recommends 30 g. A large meta-analysis published in The Lancet in 2019 found the greatest "
                      "benefit between 25 and 29 g a day, and suggested that more could protect even further."},
                {"q": "Which fruits are highest in fiber?",
                 "a": "Among fresh fruits in the Ciqual table, passion fruit (6.8 g per 100 g), guava (5.4 g), "
                      "blackberries (5.2 g), red currants (4.6 g) and raspberries (4.3 g) lead the way. Dried fruit "
                      "ranks higher, like dried figs (8.15 g), but its sugars are concentrated just as much."},
            ],
        },
        "sources": [
            CIQUAL,
            efsa("Scientific Opinion on Dietary Reference Values for carbohydrates and dietary fibre", 2010,
                 "10.2903/j.efsa.2010.1462"),
            ANSES_PNNS,
            {"t": "Reynolds A, Mann J, Cummings J, et al. Carbohydrate quality and human health: a series of "
                  "systematic reviews and meta-analyses. Lancet. 2019.",
             "u": "https://doi.org/10.1016/S0140-6736(18)31809-9"},
            REG_1924,
        ],
        "articles": ["coup-de-barre-apres-manger", "pic-de-glycemie-fatigue"],
        "methode": ["nutrition"],
    },
    # ================================================================================
    "vitamine-c": {
        "fr": {
            "nom": "vitamine C",
            "title": "Aliments riches en vitamine C : le classement de la table Ciqual",
            "seo_title": "Aliments riches en vitamine C : le classement Ciqual",
            "description": "Les aliments les plus riches en vitamine C selon la table Ciqual de l'ANSES, tes besoins selon l'EFSA, et comment la cuisson change la donne dans ton assiette.",
            "role": "<p>La vitamine C, ou acide ascorbique, sert de cofacteur à quelques enzymes clés : celles qui "
                    "fabriquent le collagène de ta peau, de tes tendons et de tes vaisseaux, la carnitine et "
                    "certains neurotransmetteurs. C'est pour ça qu'une carence sévère, le scorbut, touche d'abord les "
                    "tissus conjonctifs. Elle joue aussi un rôle antioxydant et favorise l'absorption du fer des "
                    "végétaux. Ton corps en perd un peu chaque jour : l'EFSA calcule le besoin de façon à compenser "
                    "ces pertes et à garder une réserve suffisante. Les fruits et les légumes sont ses grandes "
                    "sources.</p>",
            "besoins": "<p>La VNR européenne est de 80 mg par jour (règlement 1169/2011). L'EFSA (2013) recommande "
                       "110 mg par jour pour les hommes et 95 mg pour les femmes, avec 10 mg de plus pendant la "
                       "grossesse et 60 mg de plus pendant l'allaitement. L'ANSES retient 110 mg pour tous les adultes, "
                       "120 mg pendant la grossesse et 170 mg pendant l'allaitement. Aux États-Unis, la référence est "
                       "plus basse (90 mg pour les hommes, 75 mg pour les femmes), mais elle augmente de 35 mg chez "
                       "les fumeurs, dont le stress oxydatif accélère l'usure de la vitamine C.</p>",
            "conseils": "<ul>"
                        "<li><strong>Le poivron bat l'orange.</strong> Dans la table Ciqual, le poivron rouge cru "
                        "apporte 121 mg pour 100 g, le cassis 181 mg et le kiwi 82 mg, contre 47,5 mg pour l'orange. "
                        "100 g de poivron rouge cru dépassent la référence de l'EFSA pour une femme.</li>"
                        "<li><strong>Garde une part de cru.</strong> La cuisson à l'eau lui fait mal : la table Ciqual "
                        "donne 91 mg pour 100 g de brocoli cru, mais 18 mg pour le brocoli bouilli, et 48 mg pour le "
                        "chou-fleur cru contre 10 mg bouilli.</li>"
                        "<li><strong>Les surgelés comptent.</strong> Toujours selon la table Ciqual, le brocoli surgelé "
                        "apporte 68 mg pour 100 g avant cuisson et le chou de Bruxelles surgelé 74 mg, pas si loin des "
                        "versions fraîches crues.</li>"
                        "<li><strong>Associe-la au fer végétal.</strong> Elle favorise l'absorption du fer non héminique "
                        "(ANSES) : des crudités ou un fruit au repas de lentilles, c'est un réflexe utile si tu manges "
                        "peu de viande.</li>"
                        "</ul>",
            "faq": [
                {"q": "Combien de vitamine C par jour ?",
                 "a": "L'EFSA recommande 110 mg par jour pour un homme et 95 mg pour une femme ; l'ANSES retient 110 mg "
                      "pour tous les adultes. C'est plus que la VNR des étiquettes (80 mg). Aux États-Unis, la "
                      "référence est augmentée de 35 mg pour les fumeurs."},
                {"q": "La cuisson détruit-elle la vitamine C ?",
                 "a": "En partie, surtout à l'eau. Dans la table Ciqual, le brocoli passe de 91 mg pour 100 g cru à "
                      "18 mg bouilli, le chou-fleur de 48 mg à 10 mg. Le poivron rouge, lui, reste très riche une fois "
                      "poêlé (144 mg). Garde une part de crudités chaque jour."},
            ],
        },
        "en": {
            "nom": "vitamin C",
            "title": "Foods high in vitamin C: ranked by France's official Ciqual table",
            "seo_title": "Foods high in vitamin C: the official Ciqual ranking",
            "description": "The foods highest in vitamin C in France's official Ciqual table, how much you need according to EFSA and US guidelines, and how cooking changes the numbers.",
            "role": "<p>Vitamin C, or ascorbic acid, is a cofactor for a handful of key enzymes: those that make the "
                    "collagen in your skin, tendons and blood vessels, carnitine and certain neurotransmitters. "
                    "That's why severe deficiency, scurvy, hits connective tissue first. It also acts as an "
                    "antioxidant and helps you absorb iron from plant foods. Your body loses a little every day, and "
                    "EFSA calculates requirements to replace those losses and keep an adequate body pool. Fruit and "
                    "vegetables are the main sources.</p>",
            "besoins": "<p>The EU nutrient reference value (NRV) is 80 mg a day (Regulation 1169/2011). EFSA (2013) "
                       "recommends 110 mg a day for men and 95 mg for women, plus 10 mg during pregnancy and 60 mg "
                       "during breastfeeding. France's ANSES uses 110 mg for all adults, 120 mg in pregnancy and 170 mg "
                       "while breastfeeding. The US recommended dietary allowance is lower, 90 mg for men and 75 mg for "
                       "women, but it goes up by 35 mg for smokers, whose higher oxidative stress uses up vitamin C "
                       "faster.</p>",
            "conseils": "<ul>"
                        "<li><strong>Bell pepper beats orange.</strong> In the Ciqual table, raw red bell pepper provides "
                        "121 mg per 100 g (3.5 oz), blackcurrants 181 mg and kiwi 82 mg, versus 47.5 mg for orange. "
                        "100 g of raw red pepper exceeds EFSA's reference intake for women.</li>"
                        "<li><strong>Keep some of it raw.</strong> Boiling takes a toll: the Ciqual table lists 91 mg "
                        "per 100 g for raw broccoli but 18 mg for boiled broccoli, and 48 mg for raw cauliflower versus "
                        "10 mg boiled.</li>"
                        "<li><strong>Frozen counts.</strong> Also per the Ciqual table, frozen broccoli provides 68 mg "
                        "per 100 g before cooking and frozen Brussels sprouts 74 mg, not far from the fresh raw "
                        "versions.</li>"
                        "<li><strong>Pair it with plant iron.</strong> It boosts non-heme iron absorption (ANSES): raw "
                        "vegetables or fruit with a lentil meal is a smart habit if you eat little meat.</li>"
                        "</ul>",
            "faq": [
                {"q": "How much vitamin C do I need per day?",
                 "a": "EFSA recommends 110 mg a day for men and 95 mg for women. In the US, the recommended dietary "
                      "allowance is 90 mg for men and 75 mg for women, plus 35 mg for smokers. The EU label NRV is "
                      "80 mg."},
                {"q": "Does cooking destroy vitamin C?",
                 "a": "Partly, especially boiling. In the Ciqual table, broccoli drops from 91 mg per 100 g raw to 18 mg "
                      "boiled, and cauliflower from 48 mg to 10 mg. Red bell pepper stays very rich once pan-fried "
                      "(144 mg). Keep some raw produce on your plate every day."},
            ],
        },
        "sources": [
            CIQUAL,
            efsa("Scientific Opinion on Dietary Reference Values for vitamin C", 2013, "10.2903/j.efsa.2013.3418"),
            ANSES_VM,
            REG_1169,
            nasem("Institute of Medicine", "Dietary Reference Intakes for Vitamin C, Vitamin E, Selenium, and "
                  "Carotenoids", 2000, "10.17226/9810"),
        ],
        "articles": ["carence-en-fer-fatigue"],
        "methode": ["nutrition"],
    },
    # ================================================================================
    "vitamine-d": {
        "fr": {
            "nom": "vitamine D",
            "title": "Aliments riches en vitamine D : le classement de la table Ciqual",
            "seo_title": "Aliments riches en vitamine D : le classement Ciqual",
            "description": "Les aliments les plus riches en vitamine D selon la table Ciqual de l'ANSES, tes besoins selon l'EFSA, et pourquoi l'assiette seule a du mal à suivre en hiver.",
            "role": "<p>La vitamine D règle ton équilibre en calcium et en phosphore et permet la minéralisation des "
                    "os, du cartilage et des dents. Sans elle, le calcium de l'assiette est mal absorbé : chez "
                    "l'enfant, cela donne le rachitisme, chez l'adulte une décalcification osseuse (ostéomalacie), et "
                    "avec l'âge une fragilité qui prédispose à l'ostéoporose et aux fractures. Sa particularité : ta "
                    "peau la fabrique sous l'effet des UVB du soleil. Cette production dépend de la latitude, de la "
                    "saison, de ton âge, de ta pigmentation, de tes vêtements et de la crème solaire.</p>",
            "besoins": "<p>La VNR européenne est de 5 µg par jour (règlement 1169/2011), trois fois moins que les "
                       "références actuelles : un aliment à 100 % de la VNR ne couvre qu'un tiers de ton besoin. L'EFSA "
                       "(2016) et l'ANSES fixent un apport satisfaisant de 15 µg par jour à partir d'un an, grossesse "
                       "et allaitement compris. L'EFSA précise que ce chiffre suppose une synthèse par la peau "
                       "minimale : quand ta peau en produit, le besoin alimentaire baisse, voire disparaît. Aux "
                       "États-Unis, la référence est de 15 µg (600 UI) jusqu'à 70 ans, puis de 20 µg (800 UI).</p>",
            "conseils": "<ul>"
                        "<li><strong>Poissons gras en priorité.</strong> Hareng, sardine, maquereau, truite, saumon : "
                        "dans la table Ciqual, beaucoup dépassent 7 µg pour 100 g, comme le hareng grillé (10,8 µg) ou la "
                        "truite arc-en-ciel au four (15 µg), et le foie de morue en boîte monte à 54 µg.</li>"
                        "<li><strong>Jaune d'œuf et produits enrichis.</strong> L'ANSES cite le jaune d'œuf parmi les "
                        "sources. Dans la table Ciqual, des céréales du petit-déjeuner enrichies affichent 8 à 12,5 µg "
                        "pour 100 g, et plusieurs matières grasses à tartiner 7,5 µg. Lis les étiquettes.</li>"
                        "<li><strong>Le soleil compte, mais pas toute l'année.</strong> La synthèse par la peau dépend "
                        "de la saison et de la latitude (ANSES) : quand le soleil est bas, l'alimentation pèse "
                        "davantage.</li>"
                        "<li><strong>Complément : avec ton médecin.</strong> La vitamine D est liposoluble et l'excès "
                        "existe : l'ANSES reprend une limite de sécurité de 100 µg par jour chez l'adulte. Si tu penses "
                        "en manquer, c'est un dosage sanguin prescrit par ton médecin qui tranche, et c'est lui qui "
                        "décide d'un éventuel complément.</li>"
                        "</ul>",
            "faq": [
                {"q": "Combien de vitamine D par jour ?",
                 "a": "L'EFSA et l'ANSES fixent 15 µg par jour pour les enfants dès un an et les adultes, grossesse et "
                      "allaitement compris, en supposant que ta peau en fabrique peu. La VNR des étiquettes, 5 µg, est "
                      "trois fois plus basse. Aux États-Unis, la référence passe à 20 µg après 70 ans."},
                {"q": "Peut-on avoir assez de vitamine D avec l'alimentation seule ?",
                 "a": "C'est difficile sans poisson gras. 100 g de sardines à l'huile d'olive en apportent environ 10 µg "
                      "dans la table Ciqual, mais la plupart des aliments courants en contiennent très peu. L'été, le "
                      "soleil fait une partie du travail. Si tu doutes de ton statut, parles-en à ton médecin plutôt "
                      "que de te supplémenter seul."},
            ],
        },
        "en": {
            "nom": "vitamin D",
            "title": "Foods high in vitamin D: ranked by France's official Ciqual table",
            "seo_title": "Foods high in vitamin D: the official Ciqual ranking",
            "description": "The foods highest in vitamin D in France's official Ciqual table, how much you need according to EFSA and US guidelines, and why food alone struggles in winter.",
            "role": "<p>Vitamin D keeps your calcium and phosphorus in balance and allows bones, cartilage and teeth "
                    "to mineralize. Without it, dietary calcium is poorly absorbed: in children this causes rickets, "
                    "in adults bone softening (osteomalacia), and with age a fragility that predisposes to "
                    "osteoporosis and fractures. What makes it unusual is that your skin produces it under the "
                    "sun's UVB rays. How much depends on latitude, season, age, skin pigmentation, clothing and "
                    "sunscreen.</p>",
            "besoins": "<p>The EU nutrient reference value (NRV) is 5 µg (200 IU) a day (Regulation 1169/2011), three "
                       "times lower than current reference intakes, so a food with 100% of the NRV covers only a third "
                       "of your need. EFSA (2016) and France's ANSES set an adequate intake of 15 µg (600 IU) a day "
                       "from age one, including during pregnancy and breastfeeding. EFSA stresses that this assumes "
                       "minimal skin synthesis: when your skin makes vitamin D, your dietary need drops and may even "
                       "disappear. In the US, the recommended dietary allowance is 15 µg (600 IU) up to age 70, then "
                       "20 µg (800 IU).</p>",
            "conseils": "<ul>"
                        "<li><strong>Oily fish first.</strong> Herring, sardines, mackerel, trout, salmon: in the "
                        "Ciqual table, many provide more than 7 µg per 100 g (3.5 oz), such as grilled herring (10.8 µg) "
                        "or baked rainbow trout (15 µg), and canned cod liver reaches 54 µg.</li>"
                        "<li><strong>Egg yolks and fortified foods.</strong> ANSES lists egg yolk among the sources. "
                        "In the Ciqual table, fortified breakfast cereals show 8 to 12.5 µg per 100 g, and several "
                        "spreads 7.5 µg. Read the labels.</li>"
                        "<li><strong>Sunlight counts, but not all year.</strong> Skin synthesis depends on season and "
                        "latitude (ANSES): when the sun is low, food carries more of the load.</li>"
                        "<li><strong>Supplements: with your doctor.</strong> Vitamin D is fat-soluble and too much is "
                        "possible: ANSES uses a safety limit of 100 µg (4,000 IU) a day for adults. If you think you're "
                        "low, a blood test ordered by your doctor settles it, and your doctor decides on any "
                        "supplement.</li>"
                        "</ul>",
            "faq": [
                {"q": "How much vitamin D do I need per day?",
                 "a": "EFSA sets 15 µg (600 IU) a day for children from age one and for adults, including during "
                      "pregnancy and breastfeeding, assuming your skin makes little. The US recommended dietary "
                      "allowance is also 15 µg up to age 70, then 20 µg (800 IU). The EU label NRV, 5 µg, is three "
                      "times lower."},
                {"q": "Can you get enough vitamin D from food alone?",
                 "a": "It's hard without oily fish. 100 g of sardines in olive oil provides about 10 µg in the Ciqual "
                      "table, but most everyday foods contain very little. In summer, sunlight does part of the job. "
                      "If you're unsure about your levels, talk to your doctor rather than supplementing on your own."},
            ],
        },
        "sources": [
            CIQUAL,
            efsa("Dietary reference values for vitamin D", 2016, "10.2903/j.efsa.2016.4547"),
            ANSES_VM,
            REG_1169,
            nasem("Institute of Medicine", "Dietary Reference Intakes for Calcium and Vitamin D", 2011,
                  "10.17226/13050"),
        ],
        "articles": ["vitamine-d-fatigue", "toujours-fatigue-causes"],
        "methode": ["nutrition"],
    },
    # ================================================================================
    "potassium": {
        "fr": {
            "nom": "potassium",
            "title": "Aliments riches en potassium : le classement de la table Ciqual",
            "seo_title": "Aliments riches en potassium : le classement Ciqual",
            "description": "Les aliments les plus riches en potassium selon la table Ciqual de l'ANSES, tes besoins selon l'EFSA, et pourquoi la banane n'est pas la championne qu'on croit.",
            "role": "<p>Le potassium joue un rôle central dans la transmission nerveuse, la contraction musculaire et "
                    "le fonctionnement du cœur. Il participe aussi à la sécrétion d'insuline, au métabolisme des "
                    "glucides et des protéines et à l'équilibre acido-basique. Un vrai manque (hypokaliémie) se "
                    "traduit surtout par des troubles du rythme cardiaque, des crampes et de la fatigue ; il vient "
                    "le plus souvent de pertes digestives, comme des diarrhées ou des vomissements, ou de régimes très "
                    "pauvres en calories. Sur le long terme, l'EFSA relie des apports suffisants à une tension "
                    "artérielle plus basse et à un moindre risque d'AVC.</p>",
            "besoins": "<p>La VNR européenne est de 2" + NB + "000 mg par jour (règlement 1169/2011). L'EFSA (2016) "
                       "et l'ANSES visent plus haut : 3" + NB + "500 mg par jour pour les adultes, 4" + NB + "000 mg "
                       "pendant l'allaitement. Ce chiffre s'appuie sur des essais montrant un effet favorable sur la "
                       "tension et sur des études d'observation où des apports plus faibles sont associés à davantage "
                       "d'AVC. Aux États-Unis, les références de 2019 sont de 3" + NB + "400 mg pour les hommes et "
                       "2" + NB + "600 mg pour les femmes. Si tu as une maladie rénale, demande l'avis de ton médecin "
                       "avant d'augmenter tes apports, et jamais de complément de potassium sans lui.</p>",
            "conseils": "<ul>"
                        "<li><strong>La banane n'est pas la championne.</strong> Dans la table Ciqual, elle apporte "
                        "320 mg pour 100 g, moins que l'avocat (430 mg) ou la pomme de terre cuite au four (535 mg). Les "
                        "fruits secs vont bien au-delà : 1" + NB + "400 mg pour l'abricot sec.</li>"
                        "<li><strong>Préfère la vapeur et le four à l'eau.</strong> D'après la table Ciqual, le brocoli "
                        "cuit à la vapeur garde 340 mg pour 100 g, contre 90 mg bouilli ; la pomme de terre au four "
                        "535 mg, contre 363 mg bouillie.</li>"
                        "<li><strong>Légumineuses et oléagineux.</strong> Cuits, les haricots blancs apportent 260 mg "
                        "pour 100 g et les lentilles 215 mg ; les pistaches grillées montent à 1" + NB + "010 mg "
                        "(Ciqual). L'ANSES cite aussi les légumes, les produits laitiers et le chocolat parmi les "
                        "principales sources.</li>"
                        "</ul>",
            "faq": [
                {"q": "Combien de potassium par jour ?",
                 "a": "L'EFSA et l'ANSES recommandent 3 500 mg par jour pour un adulte, 4 000 mg pendant l'allaitement. "
                      "Aux États-Unis, la référence est de 3 400 mg pour un homme et 2 600 mg pour une femme. La VNR des "
                      "étiquettes est de 2 000 mg. En cas de maladie rénale, c'est ton médecin qui fixe la cible."},
                {"q": "La banane est-elle l'aliment le plus riche en potassium ?",
                 "a": "Non. Avec 320 mg pour 100 g dans la table Ciqual, elle est devancée par l'avocat (430 mg), la "
                      "pomme de terre cuite au four (535 mg), les pistaches (1 010 mg) et surtout les fruits secs, "
                      "comme l'abricot sec (1 400 mg). Elle reste une source pratique, mais pas la meilleure."},
            ],
        },
        "en": {
            "nom": "potassium",
            "title": "Foods high in potassium: ranked by France's official Ciqual table",
            "seo_title": "Foods high in potassium: the official Ciqual ranking",
            "description": "The foods highest in potassium in France's official Ciqual table, how much you need according to EFSA and US guidelines, and why bananas aren't the top source.",
            "role": "<p>Potassium plays a central role in nerve transmission, muscle contraction and heart function. It "
                    "also takes part in insulin secretion, carbohydrate and protein metabolism and acid-base balance. "
                    "A true deficiency (hypokalemia) mainly shows up as heart rhythm problems, cramps and fatigue; it "
                    "usually comes from digestive losses, such as diarrhea or vomiting, or from very low-calorie "
                    "diets. Over the long term, EFSA links adequate intakes to lower blood pressure and a lower risk "
                    "of stroke.</p>",
            "besoins": "<p>The EU nutrient reference value (NRV) is 2,000 mg a day (Regulation 1169/2011). EFSA (2016) "
                       "and France's ANSES aim higher: 3,500 mg a day for adults and 4,000 mg while breastfeeding. That "
                       "figure rests on trials showing a benefit for blood pressure and on observational studies where "
                       "lower intakes are linked to more strokes. In the US, the 2019 adequate intakes are 3,400 mg "
                       "for men and 2,600 mg for women. If you have kidney disease, check with your doctor before "
                       "raising your intake, and never take potassium supplements without medical advice.</p>",
            "conseils": "<ul>"
                        "<li><strong>Bananas aren't the champions.</strong> In the Ciqual table, they provide 320 mg per "
                        "100 g (3.5 oz), less than avocado (430 mg) or oven-baked potato (535 mg). Dried fruit goes much "
                        "further: 1,400 mg for dried apricots.</li>"
                        "<li><strong>Steam or bake rather than boil.</strong> According to the Ciqual table, steamed "
                        "broccoli keeps 340 mg per 100 g versus 90 mg boiled; baked potato 535 mg versus 363 mg "
                        "boiled.</li>"
                        "<li><strong>Legumes, nuts and more.</strong> Cooked white beans provide 260 mg per 100 g and "
                        "cooked lentils 215 mg; roasted pistachios reach 1,010 mg (Ciqual). ANSES also lists vegetables, "
                        "dairy and chocolate among the main sources.</li>"
                        "</ul>",
            "faq": [
                {"q": "How much potassium do I need per day?",
                 "a": "EFSA recommends 3,500 mg a day for adults and 4,000 mg while breastfeeding. In the US, the "
                      "adequate intake is 3,400 mg for men and 2,600 mg for women. The EU label NRV is 2,000 mg. If you "
                      "have kidney disease, your doctor sets the target."},
                {"q": "Are bananas the best source of potassium?",
                 "a": "No. At 320 mg per 100 g in the Ciqual table, bananas trail avocado (430 mg), baked potato "
                      "(535 mg), pistachios (1,010 mg) and above all dried fruit, such as dried apricots (1,400 mg). "
                      "They're a handy source, just not the best one."},
            ],
        },
        "sources": [
            CIQUAL,
            efsa("Dietary reference values for potassium", 2016, "10.2903/j.efsa.2016.4592"),
            ANSES_VM,
            REG_1169,
            nasem("National Academies of Sciences, Engineering, and Medicine", "Dietary Reference Intakes for Sodium "
                  "and Potassium", 2019, "10.17226/25353"),
        ],
        "articles": [],
        "methode": ["nutrition"],
    },
    # ================================================================================
    "zinc": {
        "fr": {
            "nom": "zinc",
            "title": "Aliments riches en zinc : le classement de la table Ciqual",
            "seo_title": "Aliments riches en zinc : le classement Ciqual",
            "description": "Les aliments les plus riches en zinc selon la table Ciqual de l'ANSES, tes besoins selon l'EFSA, et pourquoi les phytates changent tout si tu manges végétal.",
            "role": "<p>Le zinc est un oligoélément indispensable : il intervient dans l'activité de près de 300 "
                    "enzymes et de plus de 2" + NB + "500 facteurs de transcription, ces protéines qui règlent "
                    "l'expression de tes gènes. Une carence ralentit la croissance et affaiblit les défenses "
                    "immunitaires. Particularité : son absorption dépend beaucoup du reste de l'assiette. Les "
                    "phytates, présents dans les céréales et les légumineuses, la réduisent. C'est pour ça que tes "
                    "besoins changent selon ta façon de manger, et qu'un même chiffre sur une étiquette ne dit pas "
                    "tout.</p>",
            "besoins": "<p>La VNR européenne est de 10 mg par jour (règlement 1169/2011). L'EFSA (2014) et l'ANSES "
                       "vont plus loin : la référence dépend de ta consommation de phytates. Pour un homme, elle va de "
                       "9,4 mg par jour avec 300 mg de phytates à 14 mg avec 900 mg (16,3 mg à 1" + NB + "200 mg selon "
                       "l'EFSA) ; pour une femme, de 7,5 à 11 mg (12,7 mg). Plus ton alimentation est riche en céréales "
                       "complètes et en légumineuses, plus ton besoin est haut. Grossesse et allaitement ajoutent "
                       "respectivement 1,6 et 2,9 mg par jour selon l'EFSA.</p>",
            "conseils": "<ul>"
                        "<li><strong>Viande et fruits de mer, les sources les plus directes.</strong> Dans la table "
                        "Ciqual, le bœuf braisé apporte 10,5 mg pour 100 g, le steak haché à 5 % cuit 6,4 mg et le crabe "
                        "en boîte 8,8 mg. L'ANSES cite aussi les abats, le fromage, les légumineuses et les "
                        "poissons.</li>"
                        "<li><strong>Trempe, fais germer, fermente.</strong> Faire tremper les légumineuses, germer les "
                        "graines ou fermenter (le pain au levain, par exemple) réduit les phytates et améliore la "
                        "biodisponibilité des minéraux, selon une revue de Hotz et Gibson (2007).</li>"
                        "<li><strong>Graines de sésame, de chanvre, de courge.</strong> Ce sont les végétaux les plus "
                        "riches de la table Ciqual (7,8 à 10,2 mg pour 100 g). Compte-les comme un appoint : on en mange "
                        "de petites quantités.</li>"
                        "<li><strong>Beaucoup de complet et de légumineuses ?</strong> Vise alors le haut de la "
                        "fourchette de l'EFSA plutôt que la VNR, et parles-en à ton médecin avant tout complément.</li>"
                        "</ul>",
            "faq": [
                {"q": "Combien de zinc par jour ?",
                 "a": "Selon l'EFSA et l'ANSES, cela dépend des phytates de ton alimentation : de 9,4 à 14 mg par jour "
                      "pour un homme et de 7,5 à 11 mg pour une femme, jusqu'à 16,3 et 12,7 mg quand les phytates sont "
                      "très élevés selon l'EFSA. La VNR des étiquettes est de 10 mg."},
                {"q": "Quels aliments végétaux sont riches en zinc ?",
                 "a": "Dans la table Ciqual, les graines de sésame grillées (10,2 mg pour 100 g), de chanvre (9,9 mg) et "
                      "de courge (7,8 mg), le lupin sec (4,75 mg) et les lentilles cuites (1,25 mg). Comme les phytates des "
                      "céréales et des légumineuses freinent son absorption, trempage, germination et fermentation "
                      "aident."},
            ],
        },
        "en": {
            "nom": "zinc",
            "title": "Foods high in zinc: ranked by France's official Ciqual table",
            "seo_title": "Foods high in zinc: the official Ciqual ranking",
            "description": "The foods highest in zinc in France's official Ciqual table, how much you need according to EFSA, and why phytates matter if you eat mostly plants.",
            "role": "<p>Zinc is an essential trace element: it is involved in the activity of about 300 enzymes and more "
                    "than 2,500 transcription factors, the proteins that switch your genes on and off. A deficiency "
                    "slows growth and weakens immune defenses. What makes zinc special is that absorption depends "
                    "heavily on the rest of your plate. Phytates, found in grains and legumes, reduce it. That's why "
                    "your needs shift with the way you eat, and why a single number on a label doesn't tell the whole "
                    "story.</p>",
            "besoins": "<p>The EU nutrient reference value (NRV) is 10 mg a day (Regulation 1169/2011). EFSA (2014) and "
                       "France's ANSES go further: the reference depends on how much phytate you eat. For men, it ranges "
                       "from 9.4 mg a day at 300 mg of phytate to 14 mg at 900 mg (16.3 mg at 1,200 mg according to "
                       "EFSA); for women, from 7.5 to 11 mg (12.7 mg). The more whole grains and legumes you eat, the "
                       "higher your need. Pregnancy and breastfeeding add 1.6 and 2.9 mg a day respectively, according "
                       "to EFSA.</p>",
            "conseils": "<ul>"
                        "<li><strong>Meat and shellfish are the most direct sources.</strong> In the Ciqual table, "
                        "braised beef provides 10.5 mg per 100 g (3.5 oz), cooked 5% fat ground beef 6.4 mg and canned "
                        "crab 8.8 mg. ANSES also lists organ meats, cheese, legumes and fish.</li>"
                        "<li><strong>Soak, sprout, ferment.</strong> Soaking legumes, sprouting seeds or fermenting "
                        "(sourdough bread, for instance) lowers phytates and improves mineral availability, according to "
                        "a review by Hotz and Gibson (2007).</li>"
                        "<li><strong>Sesame, hemp and pumpkin seeds.</strong> They're the richest plant foods in the "
                        "Ciqual table (7.8 to 10.2 mg per 100 g). Count them as a top-up, since portions are small.</li>"
                        "<li><strong>Lots of whole grains and legumes?</strong> Then aim for the upper end of EFSA's range "
                        "rather than the NRV, and talk to your doctor before taking any supplement.</li>"
                        "</ul>",
            "faq": [
                {"q": "How much zinc do I need per day?",
                 "a": "According to EFSA, it depends on the phytate in your diet: from 9.4 to 16.3 mg a day for men and "
                      "from 7.5 to 12.7 mg for women, the higher values applying to phytate-rich diets. The EU label NRV "
                      "is 10 mg."},
                {"q": "Which plant foods are high in zinc?",
                 "a": "In the Ciqual table: roasted sesame seeds (10.2 mg per 100 g), hemp seeds (9.9 mg), pumpkin seeds "
                      "(7.8 mg), dried lupin (4.75 mg) and cooked lentils (1.25 mg). Since phytates in grains and legumes "
                      "reduce absorption, soaking, sprouting and fermenting help."},
            ],
        },
        "sources": [
            CIQUAL,
            efsa("Scientific Opinion on Dietary Reference Values for zinc", 2014, "10.2903/j.efsa.2014.3844"),
            ANSES_VM,
            REG_1169,
            {"t": "Hotz C, Gibson RS. Traditional food-processing and preparation practices to enhance the "
                  "bioavailability of micronutrients in plant-based diets. J Nutr. 2007.",
             "u": "https://doi.org/10.1093/jn/137.4.1097"},
        ],
        "articles": [],
        "methode": ["nutrition"],
    },
    # ================================================================================
    "vitamine-b12": {
        "fr": {
            "nom": "vitamine B12",
            "title": "Aliments riches en vitamine B12 : le classement de la table Ciqual",
            "seo_title": "Aliments riches en vitamine B12 : le classement Ciqual",
            "description": "Les aliments les plus riches en vitamine B12 selon la table Ciqual de l'ANSES, tes besoins selon l'EFSA, et ce qu'il faut savoir si tu manges peu ou pas animal.",
            "role": "<p>La vitamine B12, ou cobalamine, intervient dans le métabolisme de tes cellules en lien étroit "
                    "avec la vitamine B9. Une carence se traduit le plus souvent par une anémie, avec fatigue et "
                    "essoufflement, et peut abîmer progressivement les nerfs, le cerveau et la moelle épinière ; ces "
                    "atteintes régressent avec la vitamine, mais laissent souvent des séquelles. Elle est fabriquée "
                    "par des micro-organismes, essentiellement des bactéries et des archées : on la trouve donc surtout dans les "
                    "produits animaux (abats, poissons, œufs, viande, laitages), et la carence est particulièrement "
                    "fréquente chez les végétaliens.</p>",
            "besoins": "<p>La VNR européenne est de 2,5 µg par jour (règlement 1169/2011). L'EFSA (2015) et l'ANSES "
                       "retiennent un apport satisfaisant de 4 µg par jour pour les adultes, 4,5 µg pendant la "
                       "grossesse et 5 µg pendant l'allaitement : à ce niveau, les marqueurs sanguins du statut en B12 "
                       "restent dans les normes. Aux États-Unis, la référence est de 2,4 µg, et l'Institute of Medicine "
                       "conseille après 50 ans de la tirer surtout d'aliments enrichis ou de compléments, car 10 à 30 % "
                       "des personnes âgées absorbent mal la B12 naturellement présente dans les aliments.</p>",
            "conseils": "<ul>"
                        "<li><strong>Quelques aliments couvrent la journée.</strong> Dans la table Ciqual, 100 g de "
                        "moules cuites apportent 17,6 µg, les sardines à l'huile d'olive 20 µg, le maquereau au four "
                        "19 µg et un steak de bœuf grillé 2,7 µg.</li>"
                        "<li><strong>Végétarien : œufs et fromages aident.</strong> 100 g d'œuf dur apportent 1,1 µg et "
                        "100 g de comté 2,6 µg (Ciqual) ; le lait et les yaourts nature en contiennent beaucoup moins, "
                        "autour de 0,15 à 0,2 µg pour 100 g.</li>"
                        "<li><strong>Végétalien : ce n'est pas négociable.</strong> Dans la table Ciqual, aucun végétal "
                        "n'en apporte une quantité utile : le miso affiche 0,08 µg pour 100 g, la spiruline 0. Parle "
                        "avec ton médecin d'une source fiable, aliments enrichis ou complément.</li>"
                        "<li><strong>Après 50 ans, reste attentif.</strong> L'absorption de la B12 des aliments baisse "
                        "chez une partie des personnes âgées. Fatigue inhabituelle, troubles de la sensibilité : "
                        "parles-en à ton médecin, un dosage sanguin tranche.</li>"
                        "</ul>",
            "faq": [
                {"q": "Combien de vitamine B12 par jour ?",
                 "a": "L'EFSA et l'ANSES retiennent 4 µg par jour pour un adulte, 4,5 µg pendant la grossesse et 5 µg "
                      "pendant l'allaitement. La VNR des étiquettes est de 2,5 µg, et la référence américaine de "
                      "2,4 µg."},
                {"q": "Où trouver de la vitamine B12 quand on est végétarien ?",
                 "a": "Dans les œufs (1,1 µg pour 100 g d'œuf dur dans la table Ciqual) et les fromages (2,6 µg pour "
                      "100 g de comté). Les végétaliens, eux, ne trouvent pas de B12 utile dans les végétaux : l'ANSES "
                      "souligne que la carence est fréquente dans ce cas. Parles-en à ton médecin pour choisir une "
                      "source fiable, aliments enrichis ou complément."},
            ],
        },
        "en": {
            "nom": "vitamin B12",
            "title": "Foods high in vitamin B12: ranked by France's official Ciqual table",
            "seo_title": "Foods high in vitamin B12: the official Ciqual ranking",
            "description": "The foods highest in vitamin B12 in France's official Ciqual table, how much you need according to EFSA and US guidelines, and what vegans should know.",
            "role": "<p>Vitamin B12, or cobalamin, is involved in your cells' metabolism, working closely with folate "
                    "(vitamin B9). A deficiency most often shows up as anemia, with fatigue and shortness of breath, "
                    "and can gradually damage nerves, the brain and the spinal cord; these problems improve with the "
                    "vitamin but often leave lasting effects. B12 is made by microorganisms, mainly bacteria and archaea, so it is "
                    "found mostly in animal foods (organ meats, fish, eggs, meat, dairy), and deficiency is especially "
                    "common among vegans, as France's ANSES points out.</p>",
            "besoins": "<p>The EU nutrient reference value (NRV) is 2.5 µg a day (Regulation 1169/2011). EFSA (2015) and "
                       "France's ANSES set an adequate intake of 4 µg a day for adults, 4.5 µg during pregnancy and "
                       "5 µg while breastfeeding: at that level, blood markers of B12 status stay within normal ranges. "
                       "In the US, the recommended dietary allowance is 2.4 µg, and the Institute of Medicine advises "
                       "people over 50 to get most of it from fortified foods or supplements, because 10 to 30% of older "
                       "people may not absorb the B12 naturally present in food.</p>",
            "conseils": "<ul>"
                        "<li><strong>A few foods cover the day.</strong> In the Ciqual table, 100 g (3.5 oz) of cooked "
                        "mussels provides 17.6 µg, sardines in olive oil 20 µg, baked mackerel 19 µg and a grilled beef "
                        "steak 2.7 µg.</li>"
                        "<li><strong>Vegetarian: eggs and cheese help.</strong> 100 g of hard-boiled egg provides 1.1 µg "
                        "and 100 g of Comté cheese 2.6 µg (Ciqual); milk and plain yogurt contain far less, around 0.15 "
                        "to 0.2 µg per 100 g.</li>"
                        "<li><strong>Vegan: this one isn't optional.</strong> In the Ciqual table, no plant food provides "
                        "a useful amount: miso shows 0.08 µg per 100 g, spirulina 0. Talk to your doctor about a reliable "
                        "source, fortified foods or a supplement.</li>"
                        "<li><strong>Over 50, stay alert.</strong> Absorption of food B12 drops in some older adults. "
                        "Unusual fatigue or changes in sensation: see your doctor, a blood test settles it.</li>"
                        "</ul>",
            "faq": [
                {"q": "How much vitamin B12 do I need per day?",
                 "a": "EFSA sets 4 µg a day for adults, 4.5 µg during pregnancy and 5 µg while breastfeeding. The US "
                      "recommended dietary allowance is 2.4 µg, and the EU label NRV is 2.5 µg."},
                {"q": "Where do vegetarians get vitamin B12?",
                 "a": "From eggs (1.1 µg per 100 g of hard-boiled egg in the Ciqual table) and cheese (2.6 µg per 100 g "
                      "of Comté). Vegans won't find useful B12 in plant foods, and France's ANSES notes that deficiency "
                      "is common in that case. Talk to your doctor about a reliable source, fortified foods or a "
                      "supplement."},
            ],
        },
        "sources": [
            CIQUAL,
            efsa("Scientific Opinion on Dietary Reference Values for cobalamin (vitamin B12)", 2015,
                 "10.2903/j.efsa.2015.4150"),
            ANSES_VM,
            REG_1169,
            nasem("Institute of Medicine", "Dietary Reference Intakes for Thiamin, Riboflavin, Niacin, Vitamin B6, "
                  "Folate, Vitamin B12, Pantothenic Acid, Biotin, and Choline", 1998, "10.17226/6015"),
        ],
        "articles": ["toujours-fatigue-causes"],
        "methode": ["nutrition"],
    },
    # ================================================================================
    "omega-3": {
        "fr": {
            "nom": "oméga-3",
            "title": "Aliments riches en oméga-3 : le classement de la table Ciqual",
            "seo_title": "Aliments riches en oméga-3 : le classement Ciqual",
            "description": "Les aliments les plus riches en oméga-3 selon la table Ciqual de l'ANSES : EPA et DHA des poissons, ALA des végétaux, et tes besoins selon l'EFSA et l'ANSES.",
            "role": "<p>Les oméga-3 forment une famille d'acides gras essentiels. Leur tête de file, l'acide "
                    "alpha-linolénique (ALA), est indispensable : ton corps ne sait pas le fabriquer. À partir de "
                    "lui, il produit l'EPA et le DHA, mais la conversion en DHA est trop faible pour couvrir les "
                    "besoins : le DHA doit donc lui aussi venir de l'assiette. Ces acides gras sont nécessaires au "
                    "développement et au fonctionnement de la rétine, du cerveau et du système nerveux. Côté cœur, "
                    "l'ANSES retient qu'ils font baisser la tension des personnes hypertendues et les triglycérides "
                    "du sang.</p>",
            "besoins": "<p>Il n'existe pas de VNR pour les oméga-3. L'EFSA (2010) fixe pour l'adulte un apport "
                       "satisfaisant de 0,5 % des calories en ALA et de 250 mg par jour d'EPA et de DHA réunis, avec "
                       "100 à 200 mg de DHA en plus pendant la grossesse et l'allaitement. L'ANSES vise plus haut : 1 % "
                       "des calories en ALA, soit environ 2,2 g par jour pour 2" + NB + "000 kcal, et 250 mg de DHA "
                       "plus 250 mg d'EPA, soit 500 mg d'EPA et DHA réunis. Les classements de cette page séparent donc "
                       "les deux familles : l'EPA et le DHA des produits de la mer, l'ALA des végétaux.</p>",
            "conseils": "<ul>"
                        "<li><strong>Deux portions de poisson par semaine, dont un poisson gras.</strong> C'est le repère "
                        "de l'ANSES, en variant les espèces et les lieux d'approvisionnement. Dans la table Ciqual, "
                        "100 g de hareng ou de saumon grillés apportent 2,3 g d'EPA et de DHA, plus de neuf fois la "
                        "référence de l'EFSA.</li>"
                        "<li><strong>Une huile riche en ALA chaque jour.</strong> L'ANSES recommande une consommation "
                        "quotidienne d'huiles de colza ou de noix. D'après la table Ciqual, 10 g d'huile de colza "
                        "apportent près de 0,8 g d'ALA, et autant d'huile de noix environ 1,2 g.</li>"
                        "<li><strong>Garde-les pour l'assaisonnement.</strong> L'ANSES rappelle que certaines huiles "
                        "riches en ALA ne supportent ni la friture ni le chauffage intense.</li>"
                        "<li><strong>Lin, chia, chanvre, noix.</strong> Hors huiles, les graines de lin (21 g d'ALA pour "
                        "100 g) et de chia (17,8 g), le chanvre décortiqué (8,7 g) et les cerneaux de noix (7,5 g) "
                        "figurent parmi les meilleures sources de la table Ciqual. Mais l'ALA ne remplace pas le DHA des "
                        "poissons, que ton corps en tire trop peu.</li>"
                        "</ul>",
            "faq": [
                {"q": "Combien d'oméga-3 par jour ?",
                 "a": "L'EFSA recommande 250 mg par jour d'EPA et de DHA réunis et 0,5 % des calories en ALA ; l'ANSES "
                      "vise 500 mg d'EPA et de DHA (250 mg de chaque) et 1 % des calories en ALA, soit environ 2,2 g pour "
                      "2 000 kcal. En pratique, l'ANSES le traduit par deux portions de poisson par semaine, dont un "
                      "gras, et une huile de colza ou de noix chaque jour."},
                {"q": "Quels poissons sont les plus riches en oméga-3 ?",
                 "a": "Dans la table Ciqual, les filets de maquereau en conserve (jusqu'à 4,5 g d'EPA et de DHA pour "
                      "100 g), le hareng fumé à l'huile (4,2 g), le pilchard et la sardine à la sauce tomate (2,8 à "
                      "3,1 g), puis le hareng et le saumon grillés (2,3 g). Le thon au naturel en apporte environ 1 g."},
            ],
        },
        "en": {
            "nom": "omega-3",
            "title": "Foods high in omega-3: ranked by France's official Ciqual table",
            "seo_title": "Foods high in omega-3: the official Ciqual ranking",
            "description": "The foods highest in omega-3 in France's official Ciqual table: EPA and DHA from fish, ALA from plants, and how much you need according to EFSA and ANSES.",
            "role": "<p>Omega-3s are a family of essential fatty acids. The parent compound, alpha-linolenic acid (ALA), "
                    "is essential because your body can't make it. From ALA your body produces EPA and DHA, but "
                    "conversion to DHA is too low to meet your needs, so DHA also has to come from food. These fatty "
                    "acids are needed for the development and function of the retina, brain and nervous system. For "
                    "the heart, France's food safety agency ANSES recognizes that they lower blood pressure in people "
                    "with hypertension and reduce blood triglycerides.</p>",
            "besoins": "<p>There is no nutrient reference value (NRV) for omega-3s. For adults, EFSA (2010) sets an "
                       "adequate intake of 0.5% of calories from ALA and 250 mg a day of EPA and DHA combined, plus "
                       "100 to 200 mg of extra DHA during pregnancy and breastfeeding. France's ANSES aims higher: 1% of "
                       "calories from ALA, about 2.2 g a day on a 2,000 kcal diet, plus 250 mg of DHA and 250 mg of EPA, "
                       "or 500 mg of EPA and DHA combined. That's why the rankings on this page keep the two families "
                       "apart: EPA and DHA from seafood, ALA from plants.</p>",
            "conseils": "<ul>"
                        "<li><strong>Two servings of fish a week, one of them oily.</strong> That's the ANSES guideline, "
                        "varying species and origins. In the Ciqual table, 100 g (3.5 oz) of grilled herring or salmon "
                        "provides 2.3 g of EPA and DHA, more than nine times EFSA's reference.</li>"
                        "<li><strong>An ALA-rich oil every day.</strong> ANSES recommends canola (rapeseed) or walnut oil "
                        "daily. Based on the Ciqual table, 10 g of canola oil provides almost 0.8 g of ALA, and the same "
                        "amount of walnut oil about 1.2 g.</li>"
                        "<li><strong>Keep them for dressings.</strong> ANSES notes that some ALA-rich oils can't handle "
                        "frying or high heat.</li>"
                        "<li><strong>Flax, chia, hemp, walnuts.</strong> Oils aside, flaxseed (21 g of ALA per 100 g), chia "
                        "(17.8 g), hulled hemp seeds (8.7 g) and walnut kernels (7.5 g) rank among the best sources in "
                        "the Ciqual table. But ALA doesn't replace the DHA in fish, since your body makes too little of "
                        "it.</li>"
                        "</ul>",
            "faq": [
                {"q": "How much omega-3 do I need per day?",
                 "a": "EFSA recommends 250 mg a day of EPA and DHA combined and 0.5% of calories from ALA; France's ANSES "
                      "aims for 500 mg of EPA and DHA (250 mg of each) and 1% of calories from ALA, about 2.2 g on a "
                      "2,000 kcal diet. In practice, ANSES translates this into two servings of fish a week, one of them "
                      "oily, and canola or walnut oil every day."},
                {"q": "Which fish are highest in omega-3?",
                 "a": "In the Ciqual table: canned mackerel fillets (up to 4.5 g of EPA and DHA per 100 g), smoked "
                      "herring in oil (4.2 g), pilchards and sardines in tomato sauce (2.8 to 3.1 g), then grilled "
                      "herring and salmon (2.3 g). Tuna canned in brine provides about 1 g."},
            ],
        },
        "sources": [
            CIQUAL,
            efsa("Scientific Opinion on Dietary Reference Values for fats, including saturated fatty acids, "
                 "polyunsaturated fatty acids, monounsaturated fatty acids, trans fatty acids, and cholesterol", 2010,
                 "10.2903/j.efsa.2010.1461"),
            {"t": "Anses. Les lipides. 2021.", "u": "https://www.anses.fr/fr/content/les-lipides"},
            {"t": "Anses. Les acides gras oméga 3. 2025.", "u": "https://www.anses.fr/fr/content/les-acides-gras-omega-3"},
            ANSES_PNNS,
        ],
        "articles": [],
        "methode": ["nutrition"],
    },
}
