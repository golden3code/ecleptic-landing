# -*- coding: utf-8 -*-
"""Guides pour les coachs, lot d : le métier (fiche client, bilan, questionnaire, tests, programme)."""

ENTRIES = [
    {
        "slug": "fiche-client-coach-sportif",
        "cat": "Métier",
        "title": "Fiche client de coach sportif : ce qu'elle doit contenir",
        "description": "Fiche client de coach sportif : les rubriques à prévoir, ce qui relève des données de santé, ce qu'il faut éviter d'écrire et combien de temps la garder.",
        "date": "2026-12-02",
        "body": """
<p>La réponse courte : une <strong>fiche client de coach sportif</strong> tient en sept rubriques : contact, cadre, objectif, pratique, santé, mesures et suivi. Je n'ai trouvé aucun texte qui impose un modèle. En revanche, dès qu'elle contient une blessure, un antécédent ou les réponses à un questionnaire, elle contient des données de santé et le RGPD s'applique. Note le strict nécessaire, recueille le consentement du client et garde la partie santé à part.</p>

<h2>Que doit contenir une fiche client ?</h2>
<p>Voici un exemple de structure. La dernière colonne suit la CNIL, qui apprécie la notion de donnée de santé au cas par cas.</p>
<div class="tablewrap"><table>
<caption>Source : CNIL pour la nature des données. Rubriques proposées à titre d'exemple.</caption>
<thead><tr><th>Rubrique</th><th>Ce que tu notes</th><th>Nature de la donnée</th></tr></thead>
<tbody>
<tr><td>Contact</td><td>Nom, e-mail, téléphone, personne à prévenir</td><td>Personnelle ordinaire</td></tr>
<tr><td>Cadre</td><td>Créneaux, lieu, matériel, formule, date de début</td><td>Personnelle ordinaire</td></tr>
<tr><td>Objectif</td><td>Phrase du client, échéance, motivation</td><td>Ordinaire, sauf si elle révèle un état de santé</td></tr>
<tr><td>Pratique</td><td>Activité actuelle, passé sportif, préférences, intensité visée</td><td>Ordinaire, à relire au cas par cas</td></tr>
<tr><td>Santé</td><td>Réponses au questionnaire, gêne signalée, avis médical demandé</td><td>Donnée de santé</td></tr>
<tr><td>Mesures</td><td>Poids, tour de taille, fréquence cardiaque, sommeil</td><td>À traiter comme une donnée de santé</td></tr>
<tr><td>Suivi</td><td>Tests, séances, charges, ressenti, décisions prises</td><td>Sensible dès qu'il est croisé avec les mesures</td></tr>
</tbody>
</table></div>
<p>Garde la phrase exacte du client pour l'objectif : « monter chez moi sans m'arrêter au deuxième étage » te servira mieux qu'un simple « cardio » pour choisir un test ou mesurer un progrès.</p>

<h2>Quelles informations sont des données de santé ?</h2>
<p>Selon la CNIL, une donnée de santé porte sur la santé physique ou mentale, passée, présente ou future. Antécédents, maladies, traitements et handicap en font partie par nature. Sa page ne cite pas les blessures, mais une blessure renseigne sur la santé physique : classe-la avec le reste. Les réponses à un <a href="/coachs/questionnaire-sante-avant-le-sport-client.html">questionnaire de santé</a> se traitent de la même façon.</p>
<p>Le poids dépend du contexte. La CNIL relève qu'un poids excessif peut révéler une obésité, et qu'un poids croisé avec le nombre de pas ou les apports caloriques devient une donnée de santé. Pour le sport amateur, elle cite la fréquence cardiaque, le poids et la taille parmi les mesures qui peuvent être sensibles, notamment via un objet connecté. Je n'ai trouvé aucune qualification écrite du sommeil : traite-le comme une donnée de santé par prudence. Ta fiche réunit ces mesures au même endroit : applique la règle la plus protectrice à l'ensemble.</p>
<p>Pour conserver ces données, demande le consentement explicite du client, séparé des CGV, après lui avoir dit ce que tu collectes et pourquoi. Le guide sur <a href="/coachs/rgpd-donnees-sante-coach-sportif.html">les données de santé et le RGPD</a> détaille la marche à suivre.</p>

<h2>Que faut-il éviter d'écrire ?</h2>
<ul>
<li><strong>Un diagnostic.</strong> Écris par exemple « genou droit douloureux dans les escaliers, signalé le 12/01, orienté vers un médecin ». N'ajoute aucun nom de pathologie de ton cru. Les données de santé d'un client ne s'interprètent pas : dès qu'un signe t'interroge, tu l'orientes vers un médecin.</li>
<li><strong>Le détail médical inutile.</strong> Tu as besoin de savoir qu'un avis médical existe et quelles limites il fixe. Une copie d'ordonnance ou un compte rendu n'a rien à faire dans ton dossier.</li>
<li><strong>Un jugement sur la personne.</strong> Le client peut demander l'accès à ses données et, selon la CNIL, tu as un mois au maximum pour répondre, sauf prolongation justifiée. Rédige chaque ligne comme s'il allait la lire.</li>
<li><strong>Ce qui ne change rien à ta séance.</strong> Pour chaque champ, demande-toi ce que tu ferais de différent avec cette information. Sans réponse, supprime le champ.</li>
</ul>

<h2>Combien de temps garder une fiche client, et où ?</h2>
<p>Je n'ai trouvé aucune durée propre aux données de santé d'un client de coach. Fixe la tienne, indique-la au client et supprime la partie santé quand tu n'en as plus besoin, en principe à la fin de l'accompagnement. Les factures suivent une autre règle : selon service-public, elles se conservent 10 ans. Sépare donc le dossier administratif du dossier sportif, pour effacer l'un sans toucher à l'autre.</p>
<p>Même seul, tu tiens un registre. Selon la CNIL, les structures de moins de 250 salariés doivent y inscrire les traitements non occasionnels et ceux qui portent sur des données sensibles. Ton suivi de clients en fait partie. La CNIL propose un modèle simplifié.</p>
<p>Côté stockage, je n'ai trouvé aucune règle de la CNIL propre aux coachs sur WhatsApp ou les tableurs. Elle demande une sécurité adaptée aux données de santé, et une conversation WhatsApp ou un fichier non protégé y répond mal. L'obligation d'un hébergement certifié HDS n'est pas établie pour un suivi sportif classique. Pour un travail en sport-santé ou sur prescription, je n'ai trouvé aucune source qui tranche.</p>

<h2>Comment faire vivre la fiche après le premier rendez-vous ?</h2>
<p>Ouvre-la au <a href="/coachs/bilan-forme-premier-rendez-vous.html">bilan forme</a>, puis ajoute après chaque séance trois éléments : ce qui a été fait, le ressenti du client, ce que tu changes la fois suivante. Note aussi les résultats des <a href="/coachs/tests-physiques-nouveau-client.html">tests physiques</a> avec leurs conditions de passation.</p>
<p>Montre ces chiffres au client. Une méta-analyse de 138 essais et 19 951 personnes (Harkin, 2016) indique que suivre ses progrès aide à atteindre ses objectifs, avec un effet plus fort quand le résultat est noté physiquement ou rendu public. Elle ne porte pas seulement sur le sport : c'est un repère.</p>
<p>Relis la rubrique santé dès que la situation change. Une douleur nouvelle te renvoie à la même règle : tu notes, tu n'interprètes pas, tu orientes.</p>
<p>Ce guide informe, il ne remplace pas l'avis d'un avocat ou d'un délégué à la protection des données.</p>

<h2>Ce qu'il faut retenir</h2>
<ul>
<li>Sept rubriques suffisent, et chaque champ doit changer quelque chose à ta séance.</li>
<li>Blessures, antécédents et questionnaire sont des données de santé. Poids et sommeil se traitent de la même façon par prudence.</li>
<li>Note les faits sans les interpréter, sépare santé et facturation, fixe une durée de conservation.</li>
</ul>
""",
        "faq": [
            {
                "q": "Comment faire une fiche client quand on est coach sportif ?",
                "a": "Prévois sept rubriques : contact, cadre, objectif, pratique, santé, mesures et suivi. Note le strict nécessaire et garde la partie santé à part, car elle relève du RGPD. Un tableur protégé ou un logiciel conviennent, à condition de sécuriser l'accès.",
            },
            {
                "q": "Une fiche client contient-elle des données de santé ?",
                "a": "Presque toujours. Blessures, antécédents et réponses à un questionnaire sont des données de santé. Le poids et le sommeil peuvent l'être aussi, surtout croisés avec d'autres mesures. Dans le doute, traite-les comme telles et demande un consentement explicite, séparé des CGV.",
            },
            {
                "q": "Combien de temps garder une fiche client ?",
                "a": "Je n'ai trouvé aucune durée propre aux clients de coach. Fixe la tienne, indique-la au client et supprime la partie santé quand tu n'en as plus besoin, en principe à la fin de l'accompagnement. Les factures, elles, se conservent 10 ans.",
            },
        ],
        "sources": [
            {"t": "CNIL. Qu'est-ce qu'une donnée de santé ? 2018.", "u": "https://www.cnil.fr/fr/quest-ce-ce-quune-donnee-de-sante"},
            {"t": "CNIL. Questions-réponses sur la protection des données dans le secteur du sport amateur (hors contrat). 2022.", "u": "https://www.cnil.fr/fr/sport-amateur-hors-contrat/questions-reponses"},
            {"t": "CNIL. Le registre des activités de traitement. 2018.", "u": "https://www.cnil.fr/fr/RGPD-le-registre-des-activites-de-traitement"},
            {"t": "CNIL. Professionnels : comment répondre à une demande de droit d'accès ? 2017.", "u": "https://www.cnil.fr/fr/professionnels-comment-repondre-une-demande-de-droit-dacces"},
            {"t": "Service-public.fr. Tout savoir sur la facturation. 2026.", "u": "https://entreprendre.service-public.gouv.fr/vosdroits/F23208"},
            {"t": "Harkin B, Webb TL, Chang BP, et al. Does monitoring goal progress promote goal attainment? A meta-analysis of the experimental evidence. <em>Psychol Bull</em>. 2016.", "u": "https://doi.org/10.1037/bul0000025"},
        ],
        "a_revoir": [
            "Conservation des factures : 10 ans (page service-public vérifiée le 07/08/2026).",
            "Pages CNIL de 2017, 2018 et 2022 : vérifier qu'elles restent en ligne et à jour.",
        ],
    },
    {
        "slug": "bilan-forme-premier-rendez-vous",
        "cat": "Métier",
        "title": "Bilan forme : comment mener le premier rendez-vous avec un client",
        "seo_title": "Bilan forme : mener le premier rendez-vous avec un client",
        "description": "Bilan forme de coach sportif : comment préparer le premier rendez-vous, quelles questions poser, que faire d'un signal de santé et comment conclure.",
        "date": "2026-12-02",
        "body": """
<p>La réponse courte : un <strong>bilan forme</strong> réussi suit quatre temps : écouter l'objectif, repérer ce qui demande un avis médical, mesurer un point de départ simple, puis proposer un plan clair. Je n'ai trouvé aucun texte qui fixe son contenu ou sa durée. Il sert à décider si tu peux commencer, à quelle intensité et dans quelle direction. Tu n'y poses aucun diagnostic.</p>

<h2>Que préparer avant le premier rendez-vous ?</h2>
<p>Trois envois t'évitent de perdre la moitié du temps sur place :</p>
<ul>
<li><strong>Le <a href="/coachs/questionnaire-sante-avant-le-sport-client.html">questionnaire de santé</a></strong>, à remplir avant de venir, avec l'explication de ce que tu fais de ces données et la demande de consentement.</li>
<li><strong>Les consignes pratiques :</strong> lieu, tenue, eau, durée annoncée.</li>
<li><strong>Le statut du rendez-vous :</strong> offert ou payant, tu le dis avant. La question est traitée dans le guide sur <a href="/coachs/seance-essai-coach-sportif.html">la séance d'essai</a>.</li>
</ul>
<p>Garde aussi ta carte professionnelle à portée de main. Tout client peut la vérifier sur recherche-educateur.sports.gouv.fr, autant le lui dire toi-même. Et parle de bilan forme, jamais de bilan de santé : le mot installe une attente que tu ne peux pas satisfaire.</p>

<h2>Comment dérouler une heure de bilan forme ?</h2>
<p>Je n'ai trouvé aucune recommandation qui fixe une durée. Voici un exemple de découpage sur 60 minutes, à adapter :</p>
<ol>
<li><strong>5 minutes, le cadre.</strong> Tu annonces ce qui va se passer et ce que le client aura en repartant.</li>
<li><strong>20 minutes, l'écoute.</strong> Objectif, passé sportif, contraintes, préférences.</li>
<li><strong>5 minutes, la sécurité.</strong> Tu relis le questionnaire avec lui.</li>
<li><strong>20 minutes, le mouvement.</strong> Deux ou trois tests simples, avec un échauffement si le protocole en prévoit un.</li>
<li><strong>10 minutes, la suite.</strong> Tu résumes et tu proposes.</li>
</ol>
<p>Les <a href="/coachs/tests-physiques-nouveau-client.html">tests physiques</a> fixent un point de départ. Ils attendent si le questionnaire ou l'échange soulève une question de santé. Au premier rendez-vous, garde une marge : rien de maximal chez une personne que tu découvres, et aucune épreuve qui relève du médecin. La HAS rappelle que l'épreuve d'effort avec analyse des gaz se fait dans des structures spécialisées, par des médecins formés.</p>

<h2>Quelles questions poser pendant le bilan ?</h2>
<p>Des questions ouvertes, et un client qui parle plus que toi :</p>
<ul>
<li><strong>« Qu'est-ce qui vous amène maintenant ? »</strong> La raison du moment dit souvent plus que l'objectif affiché.</li>
<li><strong>« À quoi verrez-vous que ça a marché ? »</strong> Tu obtiens un critère concret, dans ses mots.</li>
<li><strong>« Qu'avez-vous déjà essayé, et qu'est-ce qui vous a fait arrêter ? »</strong> Tu repères les freins avant qu'ils reviennent.</li>
<li><strong>« Combien de séances tiennent vraiment dans votre semaine ? »</strong> Le programme se construit sur cette réponse.</li>
<li><strong>« Qu'aimez-vous faire, et que refusez-vous de faire ? »</strong> Le client garde la main sur une partie des choix.</li>
</ul>
<p>Ce dernier point compte. Une revue de 66 études (Teixeira, 2012) montre un lien constant entre les formes autonomes de motivation et la pratique, et la motivation intrinsèque prédit mieux l'assiduité à long terme. La plupart de ces études sont descriptives : elles établissent un lien, pas une cause. Le guide de la HAS va dans le même sens pour l'entretien de motivation : repérer les freins et définir avec la personne des objectifs réalistes.</p>

<h2>Que faire si le client signale un problème de santé ?</h2>
<p>Depuis 2015, le tri de l'ACSM repose sur trois facteurs : l'activité actuelle, les signes ou maladies cardiovasculaires, métaboliques ou rénales, et l'intensité visée. Cette mise à jour répond à un excès : trop de renvois inutiles vers le médecin, qui peuvent décourager de bouger. L'OMS juge d'ailleurs un avis médical préalable généralement inutile, en l'absence de contre-indication, pour une activité légère à modérée qui ne dépasse pas la marche rapide.</p>
<p>La HAS donne la conduite à tenir quand le doute existe :</p>
<ul>
<li><strong>Une réponse positive au questionnaire :</strong> un avis médical est préconisé avant de commencer.</li>
<li><strong>Des signes évocateurs d'une maladie :</strong> la personne s'abstient d'activité, quelle que soit l'intensité, et consulte son médecin.</li>
<li><strong>45 ans ou plus, sans pratique intense régulière, avec un projet proche du maximum :</strong> un avis médical est conseillé.</li>
</ul>
<p>Dans ces trois cas, tu n'interprètes rien. Tu reformules ce que tu as entendu, tu expliques que la décision revient à un médecin, tu notes la date et tu reportes le mouvement. Si une douleur dans la poitrine ou un malaise survient devant toi, tu appelles le 15 ou le 112. L'article L. 4161-1 du code de la santé publique vise toute personne qui prend part habituellement au diagnostic ou au traitement de maladies sans être médecin. Une phrase comme « c'est sûrement votre tension » n'a donc pas sa place dans un bilan.</p>

<h2>Comment conclure le bilan ?</h2>
<p>Résume en trois phrases ce que tu as compris, ce que tu as mesuré et ce que tu proposes. Donne ensuite un objectif daté, le rythme des séances et la date du prochain point. Remets les conditions et le prix par écrit avant tout engagement.</p>
<p>Ne promets pas de résultat chiffré. Le code de la consommation vise les pratiques trompeuses, notamment sur les résultats attendus d'un service, et promettre ce que tu ne peux ni tenir ni prouver t'y expose. Annonce plutôt ce que tu mesureras, et quand. Le soir même, reporte l'essentiel dans la <a href="/coachs/fiche-client-coach-sportif.html">fiche client</a>, tant que les mots exacts du client sont frais.</p>

<h2>Ce qu'il faut retenir</h2>
<ul>
<li>Envoie le questionnaire avant le rendez-vous et garde le temps d'écoute le plus long.</li>
<li>Au moindre signal de santé, tu reportes le mouvement et tu orientes vers un médecin, sans interpréter.</li>
<li>Termine par un objectif daté et des conditions écrites, sans promesse de résultat.</li>
</ul>
""",
        "faq": [
            {
                "q": "Comment se passe un bilan forme avec un coach sportif ?",
                "a": "Le coach écoute l'objectif et le passé sportif, relit le questionnaire de santé, fait passer deux ou trois tests simples si rien ne s'y oppose, puis propose un plan. Ce rendez-vous évalue la condition physique. Il ne remplace pas une consultation médicale.",
            },
            {
                "q": "Combien de temps dure un bilan forme ?",
                "a": "Je n'ai trouvé aucune recommandation qui fixe une durée. Une heure est un format pratique : un tiers d'écoute, un tiers de mouvement, le reste pour le cadre, la sécurité et la suite. Adapte selon le client et les tests prévus.",
            },
            {
                "q": "Que demander à un client lors d'un premier rendez-vous ?",
                "a": "Ce qui l'amène maintenant, à quoi il verra que ça a marché, ce qu'il a déjà essayé, le temps réel dont il dispose, ce qu'il aime et ce qu'il refuse. Ajoute le questionnaire de santé, et oriente vers un médecin dès qu'une réponse le demande.",
            },
        ],
        "sources": [
            {"t": "HAS. Consultation et prescription médicale d'activité physique à des fins de santé chez l'adulte. Guide. 2022.", "u": "https://www.has-sante.fr/upload/docs/application/pdf/2018-10/guide_aps_vf.pdf"},
            {"t": "Riebe D, Franklin BA, Thompson PD, et al. Updating ACSM's Recommendations for Exercise Preparticipation Health Screening. <em>Med Sci Sports Exerc</em>. 2015.", "u": "https://doi.org/10.1249/MSS.0000000000000664"},
            {"t": "Bull FC, Al-Ansari SS, Biddle S, et al. World Health Organization 2020 guidelines on physical activity and sedentary behaviour. <em>Br J Sports Med</em>. 2020.", "u": "https://doi.org/10.1136/bjsports-2020-102955"},
            {"t": "Teixeira PJ, Carraça EV, Markland D, et al. Exercise, physical activity, and self-determination theory: a systematic review. <em>Int J Behav Nutr Phys Act</em>. 2012.", "u": "https://doi.org/10.1186/1479-5868-9-78"},
            {"t": "Code de la santé publique, articles L. 4161-1 à L. 4161-6.", "u": "https://www.legifrance.gouv.fr/codes/section_lc/LEGITEXT000006072665/LEGISCTA000006171288/"},
            {"t": "Code de la consommation, articles L. 121-2 à L. 121-5.", "u": "https://www.legifrance.gouv.fr/codes/section_lc/LEGITEXT000006069565/LEGISCTA000032220953/"},
        ],
        "a_revoir": [
            "Code de la santé publique, L. 4161-1 : version lue en vigueur depuis le 29/07/2026.",
        ],
    },
    {
        "slug": "questionnaire-sante-avant-le-sport-client",
        "cat": "Métier",
        "title": "Questionnaire de santé avant le sport : que demander à un client ?",
        "seo_title": "Questionnaire de santé avant le sport : que demander ?",
        "description": "Questionnaire de santé avant le sport : ce qu'un coach peut demander à un client, PAR-Q+, QS-SPORT, droits d'auteur et conduite à tenir après un oui.",
        "date": "2026-12-02",
        "body": """
<p>La réponse courte : je n'ai trouvé aucun texte qui impose à un coach indépendant un <strong>questionnaire de santé</strong> ou un certificat médical. L'outil reste utile : la HAS recommande un auto-questionnaire à toute personne qui veut commencer ou augmenter une activité d'intensité au moins modérée, et indique qu'un éducateur sportif peut le proposer. Demande l'activité actuelle, les maladies et les signes connus, l'intensité visée. Si le client répond oui, tu n'interprètes pas : tu l'orientes vers un médecin avant de commencer.</p>

<h2>Un questionnaire ou un certificat est-il obligatoire ?</h2>
<p>Pas pour travailler avec un coach indépendant, d'après les textes que j'ai trouvés. L'idée reçue vient du monde fédéral. Selon le ministère des Sports, le certificat n'est plus systématique depuis 2022 : pour un majeur licencié, chaque fédération décide. Beaucoup l'ont remplacé par un questionnaire, d'autres gardent un certificat tous les 1, 3 ou 5 ans.</p>
<p>Deux cas restent encadrés, toujours pour la licence ou la compétition. Le mineur remplit un questionnaire avec ses parents, et une seule réponse positive impose un certificat de moins de six mois. Certaines disciplines à contraintes particulières, comme la plongée subaquatique, exigent un certificat annuel.</p>
<p>Pour les salles privées, le ministère précise que le règlement intérieur décide, et qu'un mineur y présente le plus souvent une autorisation parentale et un certificat. Rien ne t'empêche donc de prévoir un questionnaire dans ton <a href="/coachs/contrat-coach-sportif-client.html">contrat</a>. Le certificat médical demandé pour ta propre carte professionnelle est un autre sujet.</p>

<h2>PAR-Q+, Q-AAP+, QS-SPORT : lequel utiliser ?</h2>
<div class="tablewrap"><table>
<caption>Source : code du sport, HAS 2022, conditions d'utilisation du PAR-Q+, lus le 31/10/2026.</caption>
<thead><tr><th>Outil</th><th>Usage</th><th>À savoir</th></tr></thead>
<tbody>
<tr><td>QS-SPORT</td><td>Renouvellement d'une licence fédérale</td><td>Annexe II-22 abrogée le 24/06/2022</td></tr>
<tr><td>Questionnaire des mineurs</td><td>Licence et compétition</td><td>Seul questionnaire encore dans le code du sport</td></tr>
<tr><td>PAR-Q+, appelé Q-AAP+ par la HAS</td><td>Repérage avant l'activité, de 15 à 69 ans</td><td>7 questions, texte protégé</td></tr>
<tr><td>Ton propre questionnaire</td><td>Ce qui change ta séance</td><td>À rédiger toi-même, sans copier le PAR-Q+</td></tr>
</tbody>
</table></div>
<p>Le QS-SPORT circule encore, et Légifrance affiche toujours l'arrêté de 2017 comme en vigueur, alors que ses articles ne faisaient que modifier le code. Ne le présente pas comme un questionnaire officiel en vigueur.</p>
<p>Le PAR-Q+ demande une précaution. Ses conditions exigent une autorisation écrite préalable pour le modifier ou l'intégrer à une application, un site, un logiciel ou un sondage en ligne. Citer la source ne vaut pas autorisation. Les versions officielles non modifiées sont aujourd'hui gratuites pour certains usages individuels, cliniques, éducatifs et de recherche non commerciale. Ces conditions ne nomment pas les coachs, même si le site propose des ressources aux professionnels de l'exercice, et des frais peuvent s'appliquer aux usages commerciaux : en cas de doute, écris à l'ayant droit.</p>
<p>Le plus simple : invite le client à le remplir lui-même sur le site officiel, eparmedx.com, qui liste une version française pour l'Amérique du Nord. Le guide de la HAS de 2022 reproduit un texte français au tableau 6 : cela ne t'autorise pas à le copier dans ton formulaire.</p>

<h2>Que demander à un client ?</h2>
<p>Pour ton propre questionnaire, pars de la logique de l'ACSM, qui tient en trois facteurs, et ajoute ce qui sert ta séance :</p>
<ul>
<li><strong>L'activité actuelle.</strong> Combien de séances par semaine, depuis quand, à quelle intensité.</li>
<li><strong>Ce qui est connu.</strong> Une maladie cardiovasculaire, métabolique ou rénale déjà diagnostiquée. Oui ou non suffit.</li>
<li><strong>Ce qui est nouveau.</strong> Un signe inhabituel, au repos ou à l'effort. Le tableau 7 du guide de la HAS liste les signes d'alerte : garde-le sous la main.</li>
<li><strong>L'intensité visée.</strong> Ce que le client veut faire, et à quel niveau.</li>
<li><strong>Ce qui limite le mouvement.</strong> Une gêne, une opération récente, une grossesse : tout ce qui t'oblige à adapter un exercice.</li>
</ul>
<p>Passe chaque question au même filtre : que changes-tu à ta séance si la réponse est oui ? Si rien ne change, retire-la.</p>
<p>La HAS ajoute deux repères d'âge. À 45 ans ou plus, sans activité intense régulière et avec un projet proche du maximum, un avis médical est conseillé. À partir de 70 ans, il est préconisé pour une activité d'intensité au moins élevée.</p>

<h2>Que faire si le client répond oui ?</h2>
<p>La HAS est claire. Une réponse positive : un avis médical est préconisé avant de commencer. Des signes ou symptômes évocateurs d'une maladie : la personne s'abstient et consulte son médecin. Tout négatif : elle peut devenir plus active, avec les précautions d'usage.</p>
<p>Ton rôle s'arrête là. Tu ne juges pas la gravité et tu ne rassures pas. Tu notes la date, tu attends que le client te confirme l'avis reçu et ses éventuelles limites, puis tu adaptes. Tu peux aussi demander un certificat par contrat : je n'ai trouvé aucun texte qui t'y oblige. Repasse le questionnaire dès que la situation change.</p>

<h2>Comment traiter les réponses ?</h2>
<p>Un questionnaire de santé se traite comme une donnée de santé : demande un consentement explicite, séparé des CGV, après avoir dit ce que tu collectes et pourquoi. Un point reste ouvert. À propos des objets connectés dans le sport amateur, la CNIL écrit que le consentement n'est pas valable si le refus prive le sportif de pratiquer. Elle admet aussi qu'une structure non affiliée exige un certificat dans son règlement, une condition parfois imposée par son assurance. Le cas du coach n'est pas traité : refuser un client qui ne remplit rien reste une question non tranchée. Pour le reste, suis le guide sur <a href="/coachs/rgpd-donnees-sante-coach-sportif.html">le RGPD</a> et range les réponses dans la partie santé de ta <a href="/coachs/fiche-client-coach-sportif.html">fiche client</a>.</p>
<p>Ce guide informe, il ne remplace pas l'avis d'un médecin ou d'un avocat.</p>

<h2>Ce qu'il faut retenir</h2>
<ul>
<li>Je n'ai trouvé aucun texte qui impose un questionnaire à un coach indépendant, mais la HAS en recommande un avant de commencer.</li>
<li>Le QS-SPORT a quitté le code du sport en 2022, et le PAR-Q+ ne se copie pas dans un formulaire sans autorisation écrite.</li>
<li>Face à un oui, tu n'interprètes pas : tu orientes vers un médecin avant de commencer.</li>
</ul>
""",
        "faq": [
            {
                "q": "Le PAR-Q+ est-il obligatoire ?",
                "a": "Non. Je n'ai trouvé aucun texte qui l'impose à un coach indépendant. La HAS recommande un auto-questionnaire de ce type avant de commencer ou d'augmenter une activité d'intensité au moins modérée. Ses conditions d'utilisation interdisent de le modifier ou de l'intégrer à un outil en ligne sans autorisation écrite.",
            },
            {
                "q": "Un coach sportif peut-il demander un certificat médical ?",
                "a": "Oui, il peut le prévoir dans son contrat, sans que la loi l'y oblige. Depuis 2022, le certificat n'est plus systématique, même en cadre fédéral. Le ministère précise que les salles privées fixent leurs conditions dans leur règlement intérieur.",
            },
            {
                "q": "Le QS-SPORT existe-t-il encore ?",
                "a": "Il circule encore, mais l'annexe II-22 du code du sport qui le contenait est abrogée depuis le 24 juin 2022. Il servait au renouvellement d'une licence fédérale. Seul le questionnaire des mineurs figure encore dans le code.",
            },
        ],
        "sources": [
            {"t": "Ministère des Sports. Tout savoir sur le certificat médical pour le sport. 2026.", "u": "https://www.sports.gouv.fr/tout-savoir-sur-le-certificat-medical-pour-le-sport-10299"},
            {"t": "Code du sport, annexe II-22 à l'article A. 231-2 (abrogée).", "u": "https://www.legifrance.gouv.fr/codes/article_lc/LEGIARTI000035554073"},
            {"t": "HAS. Consultation et prescription médicale d'activité physique à des fins de santé chez l'adulte. Guide. 2022.", "u": "https://www.has-sante.fr/upload/docs/application/pdf/2018-10/guide_aps_vf.pdf"},
            {"t": "Riebe D, Franklin BA, Thompson PD, et al. Updating ACSM's Recommendations for Exercise Preparticipation Health Screening. <em>Med Sci Sports Exerc</em>. 2015.", "u": "https://doi.org/10.1249/MSS.0000000000000664"},
            {"t": "CNIL. Questions-réponses sur la protection des données dans le secteur du sport amateur (hors contrat). 2022.", "u": "https://www.cnil.fr/fr/sport-amateur-hors-contrat/questions-reponses"},
            {"t": "PAR-Q+ Collaboration. Terms and Conditions. 2026.", "u": "https://eparmedx.com/terms-and-conditions/"},
        ],
        "a_revoir": [
            "Règles fédérales sur le certificat : page du ministère mise à jour le 04/09/2026.",
            "Conditions d'utilisation du PAR-Q+ : lues le 31/10/2026, des frais de licence peuvent apparaître.",
            "Version française du PAR-Q+ : listée sur le site de l'ayant droit (French, North America Official Version) au 31/10/2026, fichier non ouvert.",
        ],
    },
    {
        "slug": "tests-physiques-nouveau-client",
        "cat": "Métier",
        "title": "Tests physiques : lesquels faire passer à un nouveau client ?",
        "seo_title": "Tests physiques : lesquels pour un nouveau client ?",
        "description": "Tests physiques pour un nouveau client : lesquels choisir selon le profil, comment les faire passer, comment lire les résultats et que penser du Ruffier.",
        "date": "2026-12-02",
        "body": """
<p>La réponse courte : je n'ai trouvé aucune batterie officielle. Pour les <strong>tests physiques</strong> d'un nouveau client, choisis trois ou quatre tests liés à son objectif : un pour l'endurance, un pour le bas du corps, un pour le haut du corps, et un d'équilibre si son profil le justifie. Ils servent à suivre le client par rapport à lui-même. Ils ne posent aucun diagnostic.</p>

<h2>Quels tests choisir selon le profil du client ?</h2>
<p>La HAS détaille les tests de terrain les plus courants et rappelle qu'aucun test ne mesure à lui seul la force ou la souplesse de tout le corps. Le tableau croise ses repères avec quelques études.</p>
<div class="tablewrap"><table>
<caption>Source : HAS 2022 ; Holland 2014 ; Jones 1999 ; Penry 2011.</caption>
<thead><tr><th>Capacité</th><th>Test</th><th>Profil</th><th>À savoir</th></tr></thead>
<tbody>
<tr><td>Endurance</td><td>Marche de 6 minutes</td><td>Débutant, senior, reprise</td><td>Validation clinique, pas sportive</td></tr>
<tr><td>Endurance</td><td>Course de 12 minutes</td><td>Adulte jeune et déjà actif</td><td>Effort intense, estimation de la VO2max à prendre avec prudence</td></tr>
<tr><td>Jambes</td><td>Assis-debout en 30 secondes</td><td>Senior, débutant</td><td>Chaise sans accoudoirs, sans les bras. Validé après 60 ans</td></tr>
<tr><td>Haut du corps</td><td>Pompes sans s'arrêter</td><td>Adulte sans gêne à l'épaule</td><td>Mêle force et endurance</td></tr>
<tr><td>Force</td><td>Charge de 10 à 15 répétitions maximales</td><td>Débutant, senior, reprise</td><td>Propre à chaque exercice</td></tr>
<tr><td>Souplesse</td><td>Sit-and-reach</td><td>Client sans douleur au dos</td><td>Surtout les ischio-jambiers</td></tr>
<tr><td>Équilibre</td><td>Appui unipodal, yeux fermés</td><td>Senior</td><td>Trois essais, meilleur temps. Reste à côté, près d'un appui</td></tr>
</tbody>
</table></div>
<p>Deux exemples de sélection. Pour un sédentaire de 55 ans qui reprend : marche de 6 minutes, assis-debout, appui unipodal. Pour un adulte de 30 ans déjà actif qui vise la force : course de 12 minutes, pompes, charge de 8 répétitions maximales sur deux exercices qu'il maîtrise, en deux séances.</p>
<p>Avant tout test, relis le <a href="/coachs/questionnaire-sante-avant-le-sport-client.html">questionnaire de santé</a>. S'il demande un avis médical, le test attend.</p>

<h2>Comment faire passer les tests sans fausser les résultats ?</h2>
<p>Un test ne vaut que si tu peux le refaire à l'identique. Le standard ERS/ATS (Holland, 2014) juge les tests de marche valides, fiables et sensibles au changement dans les maladies respiratoires chroniques, tout en soulignant leur sensibilité à de petits écarts de méthode. Il recommande deux essais pour la marche de 6 minutes, espacés d'au moins 30 minutes, pour établir une base stable.</p>
<ul>
<li><strong>Même cadre.</strong> Même lieu, même parcours, même heure, mêmes chaussures, même chaise. La HAS décrit la marche de 6 minutes autour de deux plots séparés de 30 mètres. Le standard ERS/ATS demande un sol plat et 30 mètres au moins : sur un parcours plus court, oublie les normes.</li>
<li><strong>Mêmes mots.</strong> Écris tes consignes et lis-les. Pour la marche, le standard prévoit une phrase type chaque minute, et rien d'autre. Si le client s'arrête, le chrono continue.</li>
<li><strong>Même préparation.</strong> Pour la marche de 6 minutes, pas d'échauffement et pas d'effort intense dans les 2 heures, selon ce standard. Pour les autres tests, garde le même échauffement.</li>
<li><strong>Trace écrite.</strong> Note les conditions à côté du résultat, sinon tu compareras deux choses différentes.</li>
</ul>
<p>Si le client signale une douleur, un malaise, un essoufflement inhabituel ou des crampes, ou s'il titube ou pâlit, tu arrêtes le test et tu l'orientes vers un médecin. Devant une douleur dans la poitrine ou un malaise, tu le fais asseoir ou allonger et tu appelles le 15 ou le 112.</p>

<h2>Peut-on faire passer un test maximal à un nouveau client ?</h2>
<p>Pas au premier rendez-vous, sauf client entraîné qui le connaît déjà. La HAS décrit le 1-RM comme un indicateur fiable de la force, et les tests à 4 ou 8 répétitions maximales comme une estimation fiable. Elle juge les tests de 10 à 15 répétitions maximales plus prudents chez les personnes âgées, déconditionnées ou atteintes d'une maladie chronique. Même à 4 ou 8 répétitions, attends que le geste soit propre. La course de 12 minutes, elle, demande déjà un effort soutenu : réserve-la à un client habitué à l'intensité.</p>
<p>Ne confonds pas ces tests avec l'épreuve d'effort, qui se fait avec suivi de l'ECG et de la pression artérielle, dans un cadre clinique.</p>

<h2>Le test de Ruffier est-il fiable ?</h2>
<p>Il reste un repère simple, peu précis pour estimer la capacité cardiorespiratoire. Dans une étude sur 81 adultes sains (Sartor, 2016), l'indice de Ruffier-Dickson a une corrélation de -0,40 avec la capacité mesurée et explique 15 % de la variabilité. Il ne figure pas dans le tableau des tests de la HAS. Si ton client y tient, compare ses scores entre eux et n'en tire pas de VO2max.</p>

<h2>Comment lire les résultats et quand refaire les tests ?</h2>
<p>Compare le client à lui-même, c'est le sens d'une <a href="/methode/ligne-de-base.html">ligne de base</a>. Les normes portent sur d'autres populations. Pour la marche de 6 minutes, Enright (1998) trouve une médiane de 576 m chez les hommes et de 494 m chez les femmes, pour 290 adultes sains de 40 à 80 ans, et ses équations expliquent environ 40 % de la variance. Pour la course de 12 minutes, Penry (2011) note une bonne fiabilité chez des adultes jeunes, mais appelle à la prudence quand on en déduit une VO2max.</p>
<p>Un écart à une norme ne te permet donc aucune conclusion sur la santé du client. Si un résultat t'étonne, tu l'orientes vers un médecin sans le commenter. L'assis-debout, de son côté, a été validé chez 76 adultes de plus de 60 ans (Jones, 1999) : ses valeurs ne se transposent pas à un client de 30 ans.</p>
<p>Je n'ai trouvé aucune fréquence officielle pour refaire les tests. Le plus logique est de les repasser à la fin d'un cycle du <a href="/coachs/creer-programme-personnalise-client.html">programme</a>, dans les mêmes conditions, puis de montrer l'évolution dans le <a href="/coachs/bilan-mensuel-client-coaching.html">bilan mensuel</a>.</p>

<h2>Ce qu'il faut retenir</h2>
<ul>
<li>Trois ou quatre tests liés à l'objectif suffisent, choisis selon le profil.</li>
<li>Même protocole à chaque fois, conditions notées, et le client comparé à lui-même.</li>
<li>Un test ne pose pas de diagnostic : au moindre signal, tu arrêtes et tu orientes vers un médecin.</li>
</ul>
""",
        "faq": [
            {
                "q": "Quel test physique faire passer à un débutant ?",
                "a": "La marche de 6 minutes pour l'endurance, l'assis-debout de 30 secondes pour les jambes, et une charge de 10 à 15 répétitions maximales si besoin. Ces tests se dosent facilement. Relis toujours le questionnaire de santé avant de commencer.",
            },
            {
                "q": "Le test de Ruffier est-il fiable ?",
                "a": "C'est un repère simple, peu précis pour estimer la capacité cardiorespiratoire. Dans une étude sur 81 adultes sains, il expliquait 15 % de la variabilité. Il ne figure pas dans le tableau des tests de la HAS.",
            },
            {
                "q": "À quelle fréquence refaire les tests physiques ?",
                "a": "Je n'ai trouvé aucune fréquence officielle. Le plus logique est de les repasser à la fin d'un cycle d'entraînement, dans les mêmes conditions, pour comparer le client à lui-même.",
            },
        ],
        "sources": [
            {"t": "HAS. Guide des connaissances sur l'activité physique et la sédentarité. 2022.", "u": "https://www.has-sante.fr/upload/docs/application/pdf/2022-08/guide_connaissance_ap_sedentarite_vf.pdf"},
            {"t": "Holland AE, Spruit MA, Troosters T, et al. An official European Respiratory Society/American Thoracic Society technical standard: field walking tests in chronic respiratory disease. <em>Eur Respir J</em>. 2014.", "u": "https://doi.org/10.1183/09031936.00150314"},
            {"t": "Enright PL, Sherrill DL. Reference equations for the six-minute walk in healthy adults. <em>Am J Respir Crit Care Med</em>. 1998.", "u": "https://doi.org/10.1164/ajrccm.158.5.9710086"},
            {"t": "Jones CJ, Rikli RE, Beam WC. A 30-s chair-stand test as a measure of lower body strength in community-residing older adults. <em>Res Q Exerc Sport</em>. 1999.", "u": "https://doi.org/10.1080/02701367.1999.10608028"},
            {"t": "Penry JT, Wilcox AR, Yun J. Validity and reliability analysis of Cooper's 12-minute run and the multistage shuttle run in healthy adults. <em>J Strength Cond Res</em>. 2011.", "u": "https://doi.org/10.1519/JSC.0b013e3181cc2423"},
            {"t": "Sartor F, Bonato M, Papini G, et al. A 45-Second Self-Test for Cardiorespiratory Fitness: Heart Rate-Based Estimation in Healthy Individuals. <em>PLoS One</em>. 2016.", "u": "https://doi.org/10.1371/journal.pone.0168154"},
        ],
        "a_revoir": [],
    },
    {
        "slug": "creer-programme-personnalise-client",
        "cat": "Métier",
        "title": "Créer un programme personnalisé pour un client : la méthode",
        "description": "Programme personnalisé pour un client : la méthode du coach sportif, du bilan à la progression, avec les repères de l'OMS et de l'ACSM pour chaque objectif.",
        "date": "2026-12-02",
        "body": """
<p>La réponse courte : un <strong>programme personnalisé</strong> part du bilan du client, jamais d'un modèle. Pars de son objectif, de son temps réel et de son niveau. Fixe le volume et l'intensité, choisis une répartition qu'il tiendra, écris une règle de progression, puis ajuste à partir de ce qu'il rapporte. La position de l'ACSM publiée en 2026 montre que peu de variables changent vraiment les résultats : concentre-toi sur celles-là.</p>

<h2>Que faut-il savoir avant d'écrire le programme ?</h2>
<p>Cinq informations décident de presque tout. Elles sortent du <a href="/coachs/bilan-forme-premier-rendez-vous.html">bilan forme</a> et des <a href="/coachs/tests-physiques-nouveau-client.html">tests physiques</a> :</p>
<ul>
<li><strong>L'objectif</strong>, dans les mots du client, avec une échéance.</li>
<li><strong>Le temps réel :</strong> le nombre de séances qu'il tiendra une semaine chargée.</li>
<li><strong>Le niveau :</strong> ce qu'il fait aujourd'hui, et ce qu'il a déjà pratiqué.</li>
<li><strong>Le lieu et le matériel.</strong></li>
<li><strong>Les limites :</strong> gêne signalée, avis médical en attente ou limites fixées par un médecin.</li>
</ul>
<p>Si un avis médical est en attente, le programme attend aussi. Si le client a reçu des limites, tu les appliques telles quelles, sans les réinterpréter.</p>

<h2>Comment fixer le volume et l'intensité ?</h2>
<p>Deux références suffisent pour caler les repères : l'OMS pour la santé, et l'ACSM pour le renforcement, avec 137 revues systématiques et plus de 30 000 participants, chez des adultes en bonne santé.</p>
<div class="tablewrap"><table>
<caption>Source : OMS 2020 ; ACSM 2026 ; Schoenfeld 2017. Adultes en bonne santé.</caption>
<thead><tr><th>Objectif</th><th>Repère</th><th>Source</th></tr></thead>
<tbody>
<tr><td>Santé, reprise</td><td>150 à 300 min d'activité modérée par semaine, ou 75 à 150 min d'activité soutenue, et renforcement de tous les grands groupes musculaires 2 jours ou plus</td><td>OMS</td></tr>
<tr><td>Senior</td><td>Dans ce volume, activité variée axée sur l'équilibre et la force, 3 jours ou plus par semaine</td><td>OMS</td></tr>
<tr><td>Force</td><td>80 % du 1RM ou plus, 2 à 3 séries, 2 séances ou plus par semaine</td><td>ACSM</td></tr>
<tr><td>Volume musculaire</td><td>10 séries ou plus par semaine, par groupe musculaire. Plus de volume, plus de gain (15 études)</td><td>ACSM, Schoenfeld</td></tr>
<tr><td>Puissance</td><td>30 à 70 % du 1RM, phase de levée rapide</td><td>ACSM</td></tr>
</tbody>
</table></div>
<p>Ces chiffres sont des points d'arrivée, pas une première semaine. L'OMS conseille à qui en est loin de commencer petit, puis d'augmenter progressivement la fréquence, l'intensité et la durée. Face à l'absence d'entraînement, le renforcement améliore déjà la force, le volume musculaire et l'équilibre. Pour un débutant, un premier programme simple suffit.</p>
<p>D'autres réglages comptent moins qu'on le croit. Selon l'ACSM, aller jusqu'à l'échec musculaire ou changer de type de matériel n'a pas modifié les résultats de façon constante. Un client sans salle peut donc suivre un vrai programme, tant que la charge ou les répétitions peuvent monter.</p>

<h2>Comment répartir les séances dans la semaine ?</h2>
<p>Choisis d'après l'agenda du client. Une méta-analyse de 14 études et 392 personnes (Ramos-Campo, 2024) ne trouve pas de différence significative de force ou de masse musculaire entre full body et split quand le volume est égal. Les auteurs concluent que le choix peut suivre les préférences.</p>
<p>Voici un exemple de logique, à ajuster :</p>
<ul>
<li><strong>2 séances :</strong> tout le corps à chaque séance.</li>
<li><strong>3 séances :</strong> tout le corps, ou une alternance haut et bas du corps.</li>
<li><strong>4 séances ou plus :</strong> un split devient possible, si le client les tient vraiment.</li>
</ul>
<p>Pense à la semaine ratée : si une séance saute, un split laisse un groupe musculaire de côté, un full body non. Pour un objectif de force, place l'exercice prioritaire en début de séance, comme le relève l'ACSM.</p>

<h2>Comment faire progresser le programme ?</h2>
<p>Écris la règle dans le programme, pour que le client sache ce qui déclenche la suite. Exemple : quand toutes les séries atteignent 12 répétitions propres, la charge monte et les répétitions redescendent à 8.</p>
<p>Tu as plusieurs leviers. Un essai sur des pratiquants entraînés (Plotkin, 2022, 43 au départ, 38 à l'arrivée) montre que monter les répétitions ou monter la charge donne des adaptations comparables sur 8 semaines, avec un léger avantage à la charge pour la force maximale. C'est utile à domicile, quand la charge disponible plafonne. L'étude reste courte et ne porte que sur les quadriceps et les mollets.</p>
<p>Modifie une seule variable à la fois, pour savoir ce qui a produit quoi. La périodisation n'a pas changé les résultats de façon constante selon l'ACSM : garde les plans complexes pour un client avancé, et revois au besoin <a href="/articles/periodisation-entrainement-bases.html">les bases de la périodisation</a>.</p>

<h2>Quand ajuster le programme, et où s'arrête ton rôle ?</h2>
<p>Après chaque séance, recueille l'effort perçu, les gênes et ce qui a été sauté. Si le client manque deux fois de suite le même type de séance, change le programme avant de parler de motivation.</p>
<p>Trois limites ne bougent pas :</p>
<ul>
<li><strong>La santé.</strong> Selon l'OMS, une personne qui développe de nouveaux symptômes en augmentant son activité consulte un professionnel de santé. Tu suspends, tu orientes, tu n'interprètes pas.</li>
<li><strong>La nutrition.</strong> Tu peux rappeler des repères généraux. Plus le conseil est personnalisé, plus le risque est élevé, surtout en présence d'une maladie. Voir <a href="/coachs/coach-sportif-nutrition-droit.html">ce que tu as le droit de dire</a>.</li>
<li><strong>Le cadre légal.</strong> Dans une réponse publiée au Journal officiel le 29 avril 2025, le ministère des Sports soumet un coach en ligne aux mêmes obligations qu'en présentiel dès que son activité relève de l'enseignement, de l'animation ou de l'encadrement : qualification, déclaration, carte à jour, honorabilité, assurance. Le texte ne précise pas où commence cette activité pour un programme vendu sans suivi. Par prudence, considère que plus le suivi est individualisé, plus tu te rapproches de l'encadrement.</li>
</ul>

<h2>Ce qu'il faut retenir</h2>
<ul>
<li>Le programme vient du bilan : objectif, temps réel, niveau, matériel, limites.</li>
<li>Fixe peu de variables, avec une règle de progression écrite et une répartition que le client tiendra.</li>
<li>Symptôme nouveau, nutrition, cadre légal : ces limites passent avant le programme.</li>
</ul>
""",
        "faq": [
            {
                "q": "Comment créer un programme de musculation personnalisé pour un client ?",
                "a": "Pars du bilan : objectif, temps réel, niveau, matériel et limites. Fixe ensuite le volume et l'intensité selon l'objectif, choisis une répartition qu'il tiendra, écris une règle de progression et ajuste à partir de ses retours.",
            },
            {
                "q": "Combien de séances par semaine prévoir dans un programme ?",
                "a": "L'OMS retient un renforcement de tous les grands groupes musculaires 2 jours ou plus par semaine, et l'ACSM 2 séances ou plus pour la force. Pour un débutant, deux séances complètes sont un bon départ. Le bon chiffre reste celui que le client tient une semaine chargée.",
            },
            {
                "q": "Un coach sportif peut-il inclure un plan alimentaire dans son programme ?",
                "a": "Il peut rappeler des repères généraux, sans se présenter comme diététicien. La limite exacte avec un conseil individualisé n'est pas tranchée : plus le conseil est personnalisé, plus le risque est élevé, surtout en présence d'une maladie. Dans ce cas, oriente vers un médecin ou un diététicien.",
            },
        ],
        "sources": [
            {"t": "Currier BS, D'Souza AC, Singh MAF, et al. American College of Sports Medicine Position Stand. Resistance Training Prescription for Muscle Function, Hypertrophy, and Physical Performance in Healthy Adults: An Overview of Reviews. <em>Med Sci Sports Exerc</em>. 2026.", "u": "https://doi.org/10.1249/MSS.0000000000003897"},
            {"t": "Schoenfeld BJ, Ogborn D, Krieger JW. Dose-response relationship between weekly resistance training volume and increases in muscle mass: A systematic review and meta-analysis. <em>J Sports Sci</em>. 2017.", "u": "https://doi.org/10.1080/02640414.2016.1210197"},
            {"t": "Bull FC, Al-Ansari SS, Biddle S, et al. World Health Organization 2020 guidelines on physical activity and sedentary behaviour. <em>Br J Sports Med</em>. 2020.", "u": "https://doi.org/10.1136/bjsports-2020-102955"},
            {"t": "Ramos-Campo DJ, Benito-Peinado PJ, Andreu-Caravaca L, et al. Efficacy of Split Versus Full-Body Resistance Training on Strength and Muscle Growth: A Systematic Review With Meta-Analysis. <em>J Strength Cond Res</em>. 2024.", "u": "https://doi.org/10.1519/JSC.0000000000004774"},
            {"t": "Plotkin D, Coleman M, Van Every D, et al. Progressive overload without progressing load? The effects of load or repetition progression on muscular adaptations. <em>PeerJ</em>. 2022.", "u": "https://doi.org/10.7717/peerj.14142"},
            {"t": "Assemblée nationale. Question écrite n° 714, Statut des coachs exerçant leur activité en ligne. Réponse publiée au Journal officiel le 29 avril 2025.", "u": "https://www.assemblee-nationale.fr/dyn/17/questions/QANR5L17QE714"},
        ],
        "a_revoir": [
            "Position de l'ACSM de 2026 : remplacer les repères si une nouvelle édition paraît.",
            "Réponse ministérielle n° 714 du 29/04/2025 : interroger la base des questions avant publication.",
        ],
    },
]
