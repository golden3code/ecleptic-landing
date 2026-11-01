# -*- coding: utf-8 -*-
"""Lot C — guides pour les coachs : CGV, contrat, RGPD, nutrition, vente de programmes.

Chargé par tools/build_articles.py (_load_coachs) → /coachs/<slug>.html.
Guides n° 25, 28, 32, 36 et 26 de tools/coachs/_cahier-coachs.md.
Faits : tools/coachs/_faits-fiscal.md et _faits-sport.md, textes relus le 31/10/2026.
"""

ENTRIES = [
    {
        "slug": "cgv-coach-sportif",
        "cat": "Statut et droit",
        "title": "CGV de coach sportif : ce qu'elles doivent prévoir",
        "description": "CGV coach sportif : ce qu'elles doivent contenir, les clauses abusives à retirer, la rétractation de 14 jours et le médiateur à désigner, textes à l'appui.",
        "date": "2026-12-02",
        "body": """
<p>La réponse courte : les <strong>CGV d'un coach sportif</strong> se remettent à tout client particulier avant le contrat, et figurent sur ton site si tu vends en ligne. Elles disent ce que tu vends, à quel prix, comment annuler et quel médiateur saisir. Un modèle copié sans relecture reste risqué : une clause abusive est réputée non écrite (L. 241-1 du code de la consommation), et en cas de litige c'est à toi de prouver que tu as informé le client.</p>

<h2>Un coach sportif est-il obligé d'avoir des CGV ?</h2>
<p>Avec des particuliers, oui. Selon service-public, elles sont obligatoires et se fournissent avant la conclusion du contrat. Avec une salle ou une entreprise, elles sont facultatives, mais à transmettre sur demande : un refus coûte jusqu'à 15 000 € à un entrepreneur individuel (code de commerce, L. 441-1).</p>
<p>L'article L. 111-1 du code de la consommation donne le socle : avant de s'engager, le client connaît le service, le prix, le délai, ton identité et le médiateur. L'article L. 111-5 met la preuve à ta charge. Garde une trace datée : CGV signées, case cochée, e-mail d'envoi. Le <a href="/coachs/contrat-coach-sportif-client.html">contrat avec chaque client</a> précise ensuite ce qui lui est propre.</p>
<p>Un manquement expose à une injonction de la DGCCRF et à une amende administrative. En 2026, pour un entrepreneur individuel, le plafond est de 3 000 € sur ces informations (L. 131-1), et de 15 000 € sur les garanties et les autres conditions contractuelles (L. 131-1-1) ou pour un contrat à distance ou hors établissement (L. 242-10). En société, ces plafonds passent à 15 000 € et 75 000 €.</p>

<h2>Que doivent contenir les CGV d'un coach ?</h2>
<p>Je n'ai pas trouvé de modèle officiel. Les textes conduisent à prévoir :</p>
<ul>
<li><strong>Ton identité :</strong> nom et prénom suivis de « EI », adresse, e-mail, téléphone, immatriculation, numéro de TVA s'il existe.</li>
<li><strong>La prestation :</strong> type et durée des séances, lieu, ce qui est inclus ou non.</li>
<li><strong>Le prix :</strong> montant TTC, échéances, moyens de paiement, validité d'un pack.</li>
<li><strong>L'exécution :</strong> début, report, retard, et <a href="/coachs/seance-annulee-regles-coach.html">règles d'annulation</a> des deux côtés. Je n'ai trouvé aucun délai légal de 24 ou 48 heures.</li>
<li><strong>La fin du contrat :</strong> durée, suspension, résiliation, sort des séances payées et non faites.</li>
<li><strong>Tes garanties :</strong> assurance professionnelle, assureur et zone couverte, selon la liste de service-public.</li>
<li><strong>Les litiges :</strong> droit applicable, juridiction selon les règles légales, coordonnées du médiateur.</li>
<li><strong>Les données :</strong> un renvoi à ta politique de confidentialité. L'accord sur les <a href="/coachs/rgpd-donnees-sante-coach-sportif.html">données de santé</a> se recueille à part.</li>
</ul>

<h2>Quelles clauses sont abusives dans des CGV de coach ?</h2>
<p>Les articles R. 212-1 et R. 212-2 du code de la consommation listent les clauses interdites et celles présumées abusives. La recommandation de 2024 de la Commission des clauses abusives sur les clubs de sport lucratifs cite les packs de séances et le coaching. Elle ne s'impose pas au juge et ne vise pas directement un coach indépendant, mais sert de repère.</p>
<div class="tablewrap"><table>
<caption>Source : code de la consommation ; Commission des clauses abusives, recommandation n° 24-01.</caption>
<thead><tr><th>Clause à revoir</th><th>Risque</th><th>À prévoir plutôt</th></tr></thead>
<tbody>
<tr><td>« Aucune séance n'est remboursée, quel que soit le motif »</td><td>Clause abusive possible, surtout si tu annules ou en cas de force majeure (R. 212-2, 2°)</td><td>Les mêmes règles dans les deux sens, une indemnité proportionnée</td></tr>
<tr><td>« Le coach décline toute responsabilité en cas de blessure »</td><td>Suppression du droit à réparation, interdite (R. 212-1, 6°)</td><td>Une information sur les risques, sans décharge générale</td></tr>
<tr><td>« Les tarifs peuvent changer à tout moment »</td><td>Modification unilatérale du prix (R. 212-1, 3°)</td><td>Un prix fixe sur une durée déterminée, sinon un préavis et un droit de résilier</td></tr>
<tr><td>« 40 € de frais pour tout impayé »</td><td>Indemnité réservée aux clients professionnels (point 56)</td><td>Rien de tel dans les CGV pour particuliers</td></tr>
<tr><td>« Seul le tribunal de ma ville est compétent »</td><td>Choix du juge restreint (point 53)</td><td>Un renvoi aux règles légales</td></tr>
</tbody>
</table></div>

<h2>Que changer si tu vends à distance ou en ligne ?</h2>
<p>Un contrat conclu à distance, par e-mail ou sur un site, ouvre 14 jours de rétractation à partir de sa conclusion (article L. 221-18). Signé en face à face sur ton lieu habituel d'activité, il n'est pas concerné. Signé ailleurs, il peut être considéré comme hors établissement.</p>
<ul>
<li><strong>Information :</strong> tes CGV donnent le délai, les modalités et le formulaire type. Sans cette information, le délai est prolongé de 12 mois.</li>
<li><strong>Démarrage anticipé :</strong> fais-le demander par écrit. Si le client se rétracte ensuite, il paie la part déjà réalisée. Sans cette demande, il ne doit rien. Utiliser le service ne vaut pas renonciation.</li>
<li><strong>Vente en ligne :</strong> depuis le 19 juin 2026, l'article L. 221-21 impose une fonction gratuite de rétractation, du type « renoncer au contrat ici », et tes CGV disent où la trouver (L. 221-5, 7°).</li>
</ul>
<p>Je n'ai trouvé aucune source qui range une séance datée dans les « activités de loisirs » exclues par l'article L. 221-28, 12° : ne compte pas sur cette exclusion.</p>

<h2>Faut-il un médiateur quand on travaille seul ?</h2>
<p>Oui. Selon service-public, tout professionnel qui vend à des consommateurs désigne un médiateur, quelle que soit sa taille, sur la liste de la CECMC. La médiation est gratuite pour le client, le coût est pour toi. Nom, adresse postale et site du médiateur figurent sur ton site et dans tes CGV, et tu les redonnes après une réclamation restée sans réponse. En 2026, le défaut d'information expose à une amende de 3 000 € au plus pour un entrepreneur individuel, 15 000 € pour une société. Une clause qui impose la médiation avant le juge est interdite.</p>
<p>Ce guide informe, il ne remplace pas l'avis d'un avocat.</p>

<h2>Ce qu'il faut retenir</h2>
<ul>
<li>Avec des particuliers, remets tes CGV avant le contrat et garde la preuve. En ligne, publie-les sur ton site.</li>
<li>Retire les clauses qui suppriment ta responsabilité ou refusent tout remboursement.</li>
<li>À distance, prévois les 14 jours de rétractation. Dans tous les cas, désigne un médiateur.</li>
</ul>
""",
        "faq": [
            {"q": "Les CGV sont-elles obligatoires pour un coach sportif ?",
             "a": "Oui avec des particuliers : service-public indique qu'elles doivent être fournies avant le contrat, et figurer sur le site en cas de vente en ligne. Entre professionnels, elles sont facultatives, mais à communiquer sur demande si elles existent."},
            {"q": "Quelle différence entre CGV et contrat pour un coach sportif ?",
             "a": "Les CGV fixent les règles communes à tous tes clients : prix, annulation, résiliation, médiateur. Le contrat précise ce qui est propre à un client : formule, nombre de séances, dates, lieu. Il renvoie aux CGV, que le client doit avoir reçues avant de s'engager."},
            {"q": "Un coach sportif peut-il refuser de rembourser un pack de séances ?",
             "a": "Une clause qui exclut tout remboursement, quel que soit le motif, expose à un risque de clause abusive, surtout si c'est toi qui annules ou en cas de force majeure. Prévois des règles écrites dans les deux sens et une indemnité proportionnée. Je n'ai trouvé aucun barème dans les textes."},
        ],
        "sources": [
            {"t": "Code de la consommation, articles L. 111-1 à L. 111-8, L. 131-1, L. 131-1-1, L. 241-1 et L. 242-10.", "u": "https://www.legifrance.gouv.fr/codes/texte_lc/LEGITEXT000006069565/"},
            {"t": "Code de la consommation, articles L. 221-1 à L. 221-29.", "u": "https://www.legifrance.gouv.fr/codes/section_lc/LEGITEXT000006069565/LEGISCTA000032221319/"},
            {"t": "Code de la consommation, articles R. 212-1 à R. 212-5.", "u": "https://www.legifrance.gouv.fr/codes/section_lc/LEGITEXT000006069565/LEGISCTA000032807194"},
            {"t": "Commission des clauses abusives. Recommandation n° 24-01 sur les contrats de clubs de sport à caractère lucratif. 2024.", "u": "https://clauses-abusives.fr/wp-content/uploads/2024/09/Recommandation-Version-definitive-V1septembre-2024.pdf"},
            {"t": "Service-public. Conditions générales de vente (CGV). 2026.", "u": "https://entreprendre.service-public.gouv.fr/vosdroits/F33527"},
            {"t": "Service-public. Médiation des litiges de la consommation. 2026.", "u": "https://entreprendre.service-public.gouv.fr/vosdroits/F33338"},
        ],
        "a_revoir": [
            "Amendes d'information précontractuelle : L. 131-1 (3 000 € et 15 000 €), L. 131-1-1 et L. 242-10 (15 000 € et 75 000 €), lues sur Légifrance le 31/10/2026.",
            "Amende pour refus de communiquer les CGV à un professionnel : 15 000 € et 75 000 € (code de commerce, L. 441-1, IV, lu le 31/10/2026).",
            "Amende pour défaut d'information sur le médiateur : 3 000 € et 15 000 € (L. 641-1, lu le 31/10/2026 ; service-public F33338, vérifié le 16/10/2026).",
            "Fonction de rétractation en ligne, L. 221-21 et D. 221-5, en vigueur depuis le 19/06/2026 (lus le 31/10/2026).",
        ],
    },
    {
        "slug": "contrat-coach-sportif-client",
        "cat": "Statut et droit",
        "title": "Contrat entre un coach sportif et son client : les clauses utiles",
        "seo_title": "Contrat coach sportif et client : les clauses utiles",
        "description": "Contrat coach sportif : faut-il un écrit, quelles clauses prévoir, où signer et quand encaisser. Ce que dit le droit de la consommation, sans modèle à recopier.",
        "date": "2026-12-02",
        "body": """
<p>La réponse courte : un <strong>contrat de coach sportif</strong> fixe ce qui est propre à chaque client : formule, nombre de séances, durée, prix, lieu, suspension et fin du contrat. Je n'ai trouvé aucun texte qui impose un écrit pour une vente en face à face, mais c'est à toi de prouver ce que tu as annoncé. Un document court qui renvoie à tes CGV suffit souvent. Regarde surtout où tu signes : le lieu décide de la rétractation et de ton droit d'encaisser tout de suite.</p>

<h2>Faut-il un contrat écrit avec chaque client ?</h2>
<p>En face à face, je n'ai trouvé aucune obligation d'écrit : l'article L. 111-2 du code de la consommation envisage même une prestation sans contrat écrit. L'article L. 111-5 met pourtant la preuve de ton information à ta charge. À distance, tu confirmes le contrat sur un support durable (L. 221-13). Hors établissement, tu remets un exemplaire daté et signé, avec le formulaire de rétractation (L. 221-9).</p>
<p>Je n'ai pas trouvé de modèle officiel. Un modèle du web se relit clause par clause, car certaines formules courantes tombent sous le coup du droit de la consommation. Les règles communes vont dans tes <a href="/coachs/cgv-coach-sportif.html">CGV</a>.</p>

<h2>Le lieu de signature change-t-il tes obligations ?</h2>
<div class="tablewrap"><table>
<caption>Source : code de la consommation, articles L. 221-1, L. 221-8 à L. 221-10, L. 221-13 et L. 221-18.</caption>
<thead><tr><th>Où le contrat est conclu</th><th>Rétractation</th><th>Encaissement</th><th>À remettre</th></tr></thead>
<tbody>
<tr><td>Face à face, sur ton lieu habituel d'activité</td><td>Pas de délai légal de 14 jours</td><td>Possible à la signature</td><td>CGV et contrat</td></tr>
<tr><td>À distance : e-mail, site, visio</td><td>14 jours à partir de la conclusion</td><td>Possible, remboursement si le client se rétracte</td><td>Confirmation sur support durable, formulaire type</td></tr>
<tr><td>Ailleurs, en présence du client : domicile, parc, café</td><td>14 jours si le contrat est hors établissement</td><td>Aucun paiement pendant 7 jours dans ce cas</td><td>Informations sur papier, exemplaire daté et signé, formulaire type</td></tr>
</tbody>
</table></div>
<p>Le dernier cas est le plus risqué. L'article L. 221-1 vise un lieu autre que celui où tu exerces en permanence ou de façon habituelle, même si c'est le client qui t'a sollicité. L'article L. 221-10 interdit alors tout paiement ou contrepartie pendant sept jours, sauf exceptions précises. Cette interdiction et la remise du contrat sont prévues à peine de nullité (L. 242-1). En 2026, ne pas remettre le contrat, ou exiger ou obtenir un paiement pendant ce délai, est puni de deux ans d'emprisonnement et de 150 000 € d'amende (L. 242-5 et L. 242-7). Sans le formulaire type, l'amende est de 150 000 € (L. 242-6).</p>
<p>Si tu travailles toujours chez tes clients, leur domicile est-il ton lieu habituel ? Je n'ai trouvé aucune source qui le tranche. Le contrat peut donc être considéré comme hors établissement : par prudence, applique ce régime.</p>

<h2>Quelles clauses prévoir dans un contrat de coaching ?</h2>
<ul>
<li><strong>Objet :</strong> formule, nombre et durée des séances, lieu, début, validité du pack. La Commission des clauses abusives vise les contrats qui laissent la durée d'engagement incertaine.</li>
<li><strong>Engagements :</strong> décris ta méthode et le suivi prévu. Ne garantis pas un résultat que tu ne peux pas tenir.</li>
<li><strong>Santé :</strong> je n'ai trouvé aucun texte qui t'impose un <a href="/coachs/questionnaire-sante-avant-le-sport-client.html">questionnaire de santé</a> ou un certificat, mais ton contrat peut les demander. Le client s'engage à signaler tout changement.</li>
<li><strong>Paiement :</strong> échéances, moyens de paiement, nature de toute avance. Si le contrat ne dit rien, une somme versée d'avance vaut arrhes : le client renonce en la perdant, toi en rendant le double. Pour un acompte, écris-le expressément.</li>
<li><strong>Annulation et retard :</strong> des <a href="/coachs/seance-annulee-regles-coach.html">règles d'annulation</a> valables dans les deux sens. Je n'ai trouvé aucun texte qui fixe un délai.</li>
<li><strong>Suspension :</strong> cas prévus, justificatifs, report des séances. N'écris pas que tout dépend de ton accord, même en cas de force majeure : la Commission écarte ces clauses.</li>
<li><strong>Résiliation :</strong> manquements précis, préavis raisonnable, sort des séances payées. L'article R. 212-1 interdit de te réserver un droit de résilier à ta guise que le client n'a pas. Une indemnité manifestement disproportionnée est présumée abusive (R. 212-2, 3°).</li>
<li><strong>Image :</strong> un accord écrit séparé, qui précise support, objectif et durée. La Commission écarte la cession illimitée signée à l'inscription.</li>
</ul>

<h2>Un abonnement peut-il se renouveler tout seul ?</h2>
<p>Oui, à des conditions strictes. Pour un contrat à durée déterminée reconduit tacitement, l'article L. 215-1 t'oblige à prévenir le client par écrit, entre trois mois et un mois avant la date limite pour refuser. Sans cet avis, il peut résilier gratuitement à tout moment après la reconduction, et tu rembourses les avances versées depuis, déduction faite de ce qui a été exécuté. L'article L. 215-4 impose aussi de reproduire les articles L. 215-1 à L. 215-3 et L. 241-3 dans le contrat. Si tes clients s'abonnent en ligne, ils doivent pouvoir résilier en ligne, gratuitement (L. 215-1-1).</p>
<p>Une durée déterminée sans reconduction, renouvelée par un nouvel accord, échappe à ces formalités.</p>

<h2>Une décharge de responsabilité protège-t-elle le coach ?</h2>
<p>Face à un particulier, une clause générale ne te protège pas. L'article R. 212-1, 6°, interdit de supprimer ou de réduire son droit à réparation quand tu manques à une obligation, et la Commission écarte la clause qui lui laisse toutes les conséquences de sa pratique sur sa santé. Ton contrat peut l'informer des risques et lui demander de signaler une douleur. Pour le reste, couvre-toi par une <a href="/coachs/assurance-coach-sportif.html">assurance de responsabilité civile</a>.</p>
<p>Ce guide informe, il ne remplace pas l'avis d'un avocat.</p>

<h2>Ce qu'il faut retenir</h2>
<ul>
<li>Un écrit court, relié à tes CGV, te donne la preuve que le code de la consommation met à ta charge.</li>
<li>Hors de ton lieu habituel d'activité, pense aux 14 jours de rétractation et aux sept jours sans paiement.</li>
<li>Pas de décharge générale ni de clause à sens unique : des règles précises et proportionnées.</li>
</ul>
""",
        "faq": [
            {"q": "Un coach sportif doit-il faire signer un contrat ?",
             "a": "Je n'ai trouvé aucune obligation d'écrit pour une vente en face à face. L'écrit est en revanche prévu à distance et hors établissement, et c'est toujours à toi de prouver que tu as informé le client. Un document court, signé et relié à tes CGV reste le plus sûr."},
            {"q": "Où trouver un modèle de contrat de coach sportif ?",
             "a": "Je n'ai pas trouvé de modèle officiel. Un modèle du web se relit clause par clause : décharge générale, absence totale de remboursement et résiliation à ta seule main exposent à un risque de clause abusive. Pour un contrat sur mesure, demande à un avocat."},
            {"q": "Un client peut-il annuler un contrat de coaching après l'avoir signé ?",
             "a": "Conclu à distance, le contrat ouvre 14 jours de rétractation à partir de sa conclusion. Signé hors de ton lieu habituel d'activité, il peut être hors établissement, avec le même délai. Signé en face à face sur ton lieu habituel, il ne donne pas ce droit, et les règles de résiliation de ton contrat s'appliquent."},
        ],
        "sources": [
            {"t": "Code de la consommation, articles L. 111-1 à L. 111-8.", "u": "https://www.legifrance.gouv.fr/codes/section_lc/LEGITEXT000006069565/LEGISCTA000032220901/"},
            {"t": "Code de la consommation, articles L. 221-1 à L. 221-29.", "u": "https://www.legifrance.gouv.fr/codes/section_lc/LEGITEXT000006069565/LEGISCTA000032221319/"},
            {"t": "Code de la consommation, articles L. 215-1 à L. 215-5.", "u": "https://www.legifrance.gouv.fr/codes/id/LEGISCTA000046194160"},
            {"t": "Code de la consommation, articles R. 212-1 à R. 212-5.", "u": "https://www.legifrance.gouv.fr/codes/section_lc/LEGITEXT000006069565/LEGISCTA000032807194"},
            {"t": "Commission des clauses abusives. Recommandation n° 24-01 sur les contrats de clubs de sport à caractère lucratif. 2024.", "u": "https://clauses-abusives.fr/wp-content/uploads/2024/09/Recommandation-Version-definitive-V1septembre-2024.pdf"},
            {"t": "Code de la consommation, articles L. 242-1 à L. 242-14-1.", "u": "https://www.legifrance.gouv.fr/codes/section_lc/LEGITEXT000006069565/LEGISCTA000032221801/"},
        ],
        "a_revoir": [
            "Nullité (L. 242-1) ; 2 ans d'emprisonnement et 150 000 € d'amende (L. 242-5, L. 242-7) ; 150 000 € d'amende (L. 242-6, modifié le 28/05/2026) : lus sur Légifrance le 31/10/2026.",
        ],
    },
    {
        "slug": "rgpd-donnees-sante-coach-sportif",
        "cat": "Statut et droit",
        "title": "Données de santé de tes clients : ce que le RGPD t'impose",
        "description": "Coach sportif et RGPD : quelles données sont des données de santé, quel consentement demander, combien de temps les garder et quels outils choisir.",
        "date": "2026-12-02",
        "body": """
<p>La réponse courte : le <strong>RGPD s'applique au coach sportif</strong> dès qu'il garde des fiches clients, même seul et en micro-entreprise. Blessures, antécédents et questionnaire de santé sont des données de santé, dont le traitement est interdit par principe. Pour les conserver, demande le consentement explicite du client, séparé des CGV. Collecte le strict nécessaire, fixe une durée, sécurise, et tiens un registre simple.</p>

<h2>Quelles données de tes clients sont des données de santé ?</h2>
<p>Le RGPD vise les données qui révèlent l'état de santé d'une personne. La CNIL précise que la notion est large et s'apprécie au cas par cas : une donnée peut l'être par nature, par croisement ou par destination. Je n'ai pas trouvé de page dédiée au coach. Ce tableau applique ses repères à une <a href="/coachs/fiche-client-coach-sportif.html">fiche client</a>.</p>
<div class="tablewrap"><table>
<caption>Source : CNIL, lecture appliquée à une fiche client.</caption>
<thead><tr><th>Élément de la fiche</th><th>Qualification</th></tr></thead>
<tbody>
<tr><td>Blessures, antécédents, maladies, traitements, handicap</td><td>Donnée de santé par nature</td></tr>
<tr><td>Réponses à un questionnaire de santé</td><td>À traiter comme donnée de santé</td></tr>
<tr><td>Poids seul</td><td>Cas par cas : un poids excessif peut révéler une obésité</td></tr>
<tr><td>Poids croisé avec les pas, les calories ou l'effort</td><td>Donnée de santé par croisement</td></tr>
<tr><td>Fréquence cardiaque issue d'un objet connecté</td><td>Sensible, consentement exprès attendu</td></tr>
<tr><td>Sommeil</td><td>Pas de qualification écrite, à traiter comme donnée de santé par prudence</td></tr>
<tr><td>Nom, e-mail, planning, nombre de pas seul</td><td>Donnée personnelle ordinaire</td></tr>
</tbody>
</table></div>
<p>Dans le doute, traite l'information comme une donnée de santé, et ne note que ce qui change ta séance.</p>

<h2>Quel consentement demander au client ?</h2>
<p>L'article 9 du RGPD interdit par principe le traitement des données de santé. Pour un coach, l'exception pratique est le consentement explicite (article 9.2.a). L'exception de l'article 9.2.h suppose une personne soumise à une obligation de secret, et je n'ai trouvé aucune source qui l'applique à un coach.</p>
<ul>
<li><strong>Séparé :</strong> la CNIL écrit, pour les applications de bien-être, qu'une case unique ne peut pas valoir à la fois acceptation des conditions et accord sur les données de santé. Signer ton contrat ne suffit donc pas.</li>
<li><strong>Informé :</strong> avant l'accord, dis quelles données tu collectes et pourquoi.</li>
<li><strong>Prouvable :</strong> garde la date et le support. L'article 7 te demande de pouvoir démontrer ce consentement.</li>
<li><strong>Retirable :</strong> le client retire son accord aussi simplement qu'il l'a donné.</li>
</ul>
<p>Un point reste ouvert : peux-tu refuser un client qui ne remplit pas ton <a href="/coachs/questionnaire-sante-avant-le-sport-client.html">questionnaire de santé</a> ? Pour le sport amateur, la CNIL admet qu'une structure non affiliée exige un certificat, parfois à la demande de l'assureur. Elle ajoute qu'un consentement n'est pas valable si le refus interdit de pratiquer. Le cas du coach n'est pas traité. Explique à quoi servent tes questions, limite-les à la sécurité de la séance et demande à ton assureur ce qu'il exige.</p>

<h2>Que dire au client et combien de temps garder ses données ?</h2>
<p>À la collecte, remets une note courte : qui tu es, pourquoi tu collectes, sur quelle base, qui reçoit les données, combien de temps, quels droits, et le droit de saisir la CNIL. Le client peut demander l'accès, la rectification, l'effacement, la limitation, l'opposition ou la portabilité. Tu réponds sous un mois au maximum, sauf exceptions.</p>
<p>Je n'ai trouvé aucune durée propre aux données de santé d'un client de coach. La règle générale vaut : rien au-delà du nécessaire. Fixe une durée, écris-la, et supprime ces données quand tu n'en as plus besoin, en principe à la fin de l'accompagnement. Tes factures se gardent 10 ans par prudence : n'y fais figurer aucune information de santé.</p>

<h2>WhatsApp, Excel, logiciel : quels outils utiliser ?</h2>
<p>Je n'ai trouvé aucune règle de la CNIL propre aux coachs sur WhatsApp ou les tableurs, et ses repères sur les messageries visent les soignants. Le RGPD demande en revanche une sécurité adaptée au risque (article 32). Une conversation WhatsApp ou un fichier non protégé convient mal à ces données, comme le montre notre guide sur <a href="/coachs/excel-whatsapp-logiciel-coaching.html">Excel, WhatsApp et les logiciels</a>. Le minimum : accès limité, mots de passe, chiffrement.</p>
<p>Si tu gères tes fiches avec un logiciel, tu restes responsable de ces données. L'éditeur qui les traite pour toi est en principe ton sous-traitant, et l'article 28 impose un contrat. Demande où elles sont hébergées, si elles sortent de l'Union européenne, comment les exporter et ce qu'elles deviennent à la fin. Si tu interviens sur les fiches d'une salle, ton rôle s'analyse au cas par cas.</p>
<p>La certification HDS vise les données recueillies lors d'activités de prévention, de diagnostic, de soins ou de suivi social et médico-social. Pour un suivi sportif classique, cette obligation n'est pas établie. En sport-santé, sur prescription ou avec des soignants, la notion de prévention peut jouer : je n'ai trouvé aucune source qui traite ce cas.</p>

<h2>Registre et fuite de données : que faire ?</h2>
<p>Même seul, tiens un registre. Selon la CNIL, la dérogation des structures de moins de 250 salariés ne couvre ni les traitements non occasionnels, comme la gestion des clients, ni les données sensibles. Elle propose un modèle simplifié.</p>
<p>Téléphone perdu, message au mauvais destinataire, compte piraté : note chaque incident. S'il crée un risque pour les personnes, notifie la CNIL, si possible sous 72 heures (article 33). Si le risque est élevé, préviens aussi les clients concernés (article 34).</p>
<p>Ce guide informe, il ne remplace pas l'avis d'un avocat ou d'un délégué à la protection des données.</p>

<h2>Ce qu'il faut retenir</h2>
<ul>
<li>Blessures, antécédents et questionnaire sont des données de santé. Poids et sommeil peuvent l'être aussi : dans le doute, protège-les.</li>
<li>Demande un consentement explicite, séparé de tes CGV, que tu peux prouver et que le client peut retirer.</li>
<li>Collecte peu, écris une durée, choisis un outil sécurisé et tiens un registre, même seul.</li>
</ul>
""",
        "faq": [
            {"q": "Le RGPD s'applique-t-il à un coach sportif auto-entrepreneur ?",
             "a": "Oui. La CNIL ne prévoit pas de régime propre à l'entrepreneur individuel. Le coach qui décide seul de ses fiches clients est responsable de ces données, même s'il utilise un logiciel, et il doit tenir un registre simple."},
            {"q": "Le poids d'un client est-il une donnée de santé ?",
             "a": "Cela s'apprécie au cas par cas. La CNIL relève qu'un poids excessif peut révéler une obésité, et qu'un poids croisé avec le nombre de pas ou les apports caloriques peut devenir une donnée de santé. Dans un suivi de coaching, traite-le comme tel par prudence."},
            {"q": "Un coach sportif doit-il utiliser un hébergeur HDS ?",
             "a": "Pour un suivi sportif classique, cette obligation n'est pas établie. La certification vise les activités de prévention, de diagnostic, de soins ou de suivi social et médico-social. Un hébergement sécurisé reste indispensable. Pour le sport-santé ou un travail sur prescription, le point n'est pas tranché."},
        ],
        "sources": [
            {"t": "CNIL. Qu'est-ce qu'une donnée de santé ? 2018.", "u": "https://www.cnil.fr/fr/quest-ce-ce-quune-donnee-de-sante"},
            {"t": "Règlement (UE) 2016/679 (RGPD), chapitre II, articles 5 à 11, texte publié par la CNIL.", "u": "https://www.cnil.fr/fr/reglement-europeen-protection-donnees/chapitre2"},
            {"t": "Règlement (UE) 2016/679 (RGPD), chapitre IV, articles 24 à 43, texte publié par la CNIL.", "u": "https://www.cnil.fr/fr/reglement-europeen-protection-donnees/chapitre4"},
            {"t": "CNIL. Sport amateur hors contrat : questions-réponses. 2022.", "u": "https://www.cnil.fr/fr/sport-amateur-hors-contrat/questions-reponses"},
            {"t": "CNIL. Applications mobiles en santé et protection des données personnelles : les questions à se poser. 2018.", "u": "https://www.cnil.fr/fr/applications-mobiles-en-sante-et-protection-des-donnees-personnelles-les-questions-se-poser"},
            {"t": "CNIL. RGPD : le registre des activités de traitement.", "u": "https://www.cnil.fr/fr/RGPD-le-registre-des-activites-de-traitement"},
        ],
        "a_revoir": [
            "Délai de notification de 72 heures et seuil de 250 salariés : vérifier qu'aucune révision du RGPD n'est entrée en vigueur.",
            "Pages CNIL de 2018 et 2022 (donnée de santé, sport amateur, applications mobiles, HDS) : vérifier qu'elles restent en ligne et inchangées.",
            "Conservation des factures : 10 ans (code de commerce, L. 123-22, écrit pour les commerçants), 6 ans au titre fiscal (LPF, L. 102 B, fiche 5.3).",
        ],
    },
    {
        "slug": "coach-sportif-nutrition-droit",
        "cat": "Statut et droit",
        "title": "Coach sportif et nutrition : ce que tu as le droit de dire",
        "description": "Coach sportif et nutrition : les repères que tu peux donner, la limite avec le diététicien, le mot nutritionniste, et quand orienter un client vers un soignant.",
        "date": "2026-12-02",
        "body": """
<p>La réponse courte : un <strong>coach sportif</strong> peut parler de <strong>nutrition</strong> en rappelant les repères généraux du PNNS, sans se présenter comme diététicien, sans poser de diagnostic et sans traiter de maladie. Dès qu'un client signale une maladie ou un trouble du métabolisme ou de l'alimentation, il l'oriente vers un médecin ou un diététicien. Entre les deux, la limite n'est pas tranchée : plus le conseil est personnalisé, plus le risque est élevé, surtout en présence d'une maladie.</p>

<h2>Diététicien, nutritionniste, coach en nutrition : quelle différence ?</h2>
<p><strong>Diététicien</strong> est une profession de santé réglementée. L'article L. 4371-1 du code de la santé publique vise toute personne qui, habituellement, dispense des conseils nutritionnels et, sur prescription médicale, participe à l'éducation et à la rééducation nutritionnelle de patients atteints de troubles du métabolisme ou de l'alimentation. Seuls les titulaires des diplômes reconnus peuvent exercer (L. 4371-2). En 2026, l'exercice illégal est puni d'un an d'emprisonnement et de 15 000 € d'amende (L. 4372-1), et l'usage sans droit du titre est une usurpation (L. 4372-2).</p>
<p>Je n'ai trouvé aucune définition légale de <strong>nutritionniste</strong>. Dans une réponse publiée le 19 décembre 2023, le gouvernement précise que nutritionnistes, coachs en nutrition et nutrithérapeutes ne sont pas assimilés aux diététiciens, ne peuvent pas s'en revendiquer, et n'ont pas le droit de prendre part au diagnostic ou au traitement de maladies.</p>
<p>Tu veux devenir coach sportif et nutrition ? Une formation enrichit tes connaissances sans changer ton statut : selon cette même réponse, une inscription au RNCP n'ouvre pas une profession médicale ou paramédicale. « Coach nutritionniste » peut aussi laisser croire à une qualification de santé, et l'article L. 121-2 du code de la consommation vise les allégations trompeuses sur les qualités du professionnel. Écris ce que tu es, et cite la formation suivie.</p>

<h2>Que peux-tu dire à un client sur son alimentation ?</h2>
<div class="tablewrap"><table>
<caption>Source : code de la santé publique, réponse ministérielle du 19/12/2023. Grille de prudence, aucun texte ne la pose telle quelle.</caption>
<thead><tr><th>Situation</th><th>Position</th></tr></thead>
<tbody>
<tr><td>Rappeler les repères du PNNS</td><td>Possible, sans te présenter comme diététicien</td></tr>
<tr><td>Parler hydratation ou repas autour de l'entraînement, en termes généraux</td><td>Repère général, tant qu'il n'est pas individualisé</td></tr>
<tr><td>Plan alimentaire ou calcul individuel, sans maladie signalée</td><td>Non tranché, risque croissant avec la personnalisation</td></tr>
<tr><td>Suivi alimentaire régulier et facturé</td><td>Non tranché, le caractère habituel pèse</td></tr>
<tr><td>Client avec une maladie, un trouble du métabolisme ou de l'alimentation</td><td>Orienter vers un médecin ou un diététicien</td></tr>
<tr><td>Diagnostiquer une carence, une intolérance, un trouble</td><td>Interdit</td></tr>
<tr><td>Présenter un régime comme un traitement</td><td>Interdit</td></tr>
</tbody>
</table></div>
<p>L'article L. 4371-1 unit deux éléments par le mot « et » : les conseils habituels, et la participation, sur prescription, à la rééducation de patients par un bilan diététique personnalisé. Les conseils seuls suffisent-ils à constituer l'exercice de la profession ? Je n'ai trouvé aucune décision de justice sur un coach. Personne ne peut donc te dire qu'un plan alimentaire personnalisé est permis, ni qu'il est toujours interdit.</p>
<p>Trois questions situent ton conseil. Vaut-il pour tout le monde, ou pour ce seul client ? Revient-il chaque semaine ? Touche-t-il une maladie ou un traitement ? Un conseil individuel, répété et lié à une maladie est le plus exposé.</p>

<h2>Quels repères généraux peux-tu citer ?</h2>
<p>Santé publique France a actualisé en décembre 2018 les recommandations du PNNS pour les adultes. Cite-les telles quelles :</p>
<ul>
<li>Au moins 5 fruits et légumes par jour, et une petite poignée de fruits à coque.</li>
<li>Des légumes secs au moins 2 fois par semaine, et au moins un féculent complet par jour.</li>
<li>Du poisson 2 fois par semaine, dont un poisson gras, et 2 produits laitiers par jour.</li>
<li>Au maximum 150 g de charcuterie et 500 g de viande hors volaille par semaine.</li>
<li>Moins de sel, et 10 verres standard d'alcool par semaine au maximum, 2 par jour, pas tous les jours.</li>
</ul>
<p>Ces repères ne remplacent pas un avis médical. Pour l'entraînement, renvoie vers un article général comme <a href="/articles/que-manger-apres-le-sport.html">que manger après le sport</a>.</p>

<h2>Quand orienter vers un médecin ou un diététicien ?</h2>
<p>Dès qu'un client signale une maladie, un traitement, ou un trouble du métabolisme ou de l'alimentation. Diabète, perte de poids inexpliquée, restriction qui t'inquiète : tu ne nommes rien, tu ne conclus rien. Tu dis que le sujet dépasse ton cadre et tu l'orientes. L'article L. 4161-1 vise celui qui prend part habituellement au diagnostic ou au traitement de maladies, réelles ou supposées, sans être médecin. En 2026, la peine est de deux ans d'emprisonnement et de 30 000 € d'amende, portée à cinq ans et 75 000 € en ligne (L. 4161-5).</p>

<h2>Peux-tu vendre un suivi nutrition ou des compléments ?</h2>
<p>Un suivi nutrition reste en zone grise. Une ligne facturée à part rend visible une activité de conseil habituelle : par prudence, confie cette partie à un diététicien. L'exonération de TVA des cours n'est pas établie pour un tel suivi. Il n'existe pas de barème officiel pour une offre « coach sportif et nutrition » : calcule ton prix avec la méthode de notre guide sur le <a href="/coachs/tarif-coach-sportif-independant.html">tarif d'un coach</a>.</p>
<p>La vente de compléments relève de la vente de marchandises, avec son propre régime (voir notre guide <a href="/coachs/coach-sportif-bic-ou-bnc.html">BIC ou BNC</a>). Ne présente jamais un produit comme un substitut à un traitement : affirmer faussement qu'il guérit une maladie est réputé trompeur (L. 121-4, 16°).</p>
<p>Ce guide informe, il ne remplace pas l'avis d'un avocat.</p>

<h2>Ce qu'il faut retenir</h2>
<ul>
<li>Tu peux rappeler les repères du PNNS, sans te dire diététicien, sans diagnostic ni traitement.</li>
<li>La limite avec le conseil individualisé n'est pas tranchée : plus il est personnalisé, plus le risque monte.</li>
<li>Maladie, traitement ou trouble de l'alimentation : oriente vers un médecin ou un diététicien.</li>
</ul>
""",
        "faq": [
            {"q": "Un coach sportif peut-il faire un plan alimentaire ?",
             "a": "La question n'est pas tranchée. Je n'ai trouvé ni texte qui l'autorise clairement ou l'interdise dans tous les cas, ni décision sur un coach. Plus le conseil est personnalisé, plus le risque est élevé, surtout en présence d'une maladie. Dans ce dernier cas, oriente vers un médecin ou un diététicien."},
            {"q": "Un coach sportif peut-il se dire nutritionniste ?",
             "a": "Je n'ai trouvé aucune définition légale du mot, mais il peut laisser croire à une qualification de santé. Le titre de diététicien, lui, est protégé. Le gouvernement rappelle qu'un coach en nutrition ne peut pas s'en revendiquer, et que le RNCP n'ouvre pas une profession de santé."},
            {"q": "Quel est le tarif d'un coach sportif et nutrition ?",
             "a": "Il n'existe pas de barème officiel, et je n'ai trouvé aucune donnée fiable. Calcule ton prix à partir de ton temps et de tes charges. Facturer un suivi nutrition à part soulève une question de droit : pour la partie alimentaire individualisée, travailler avec un diététicien reste plus prudent."},
        ],
        "sources": [
            {"t": "Code de la santé publique, articles L. 4371-1 à L. 4371-9.", "u": "https://www.legifrance.gouv.fr/codes/section_lc/LEGITEXT000006072665/LEGISCTA000006171333/"},
            {"t": "Code de la santé publique, articles L. 4372-1 et L. 4372-2.", "u": "https://www.legifrance.gouv.fr/codes/section_lc/LEGITEXT000006072665/LEGISCTA000006171334/"},
            {"t": "Code de la santé publique, articles L. 4161-1 à L. 4161-6.", "u": "https://www.legifrance.gouv.fr/codes/section_lc/LEGITEXT000006072665/LEGISCTA000006171288/"},
            {"t": "Code de la consommation, articles L. 121-2 à L. 121-5.", "u": "https://www.legifrance.gouv.fr/codes/section_lc/LEGITEXT000006069565/LEGISCTA000032220953/"},
            {"t": "Assemblée nationale. Question écrite n° 9716, réponse publiée le 19 décembre 2023.", "u": "https://www.assemblee-nationale.fr/dyn/16/questions/QANR5L16QE9716"},
            {"t": "Santé publique France. Recommandations relatives à l'alimentation, à l'activité physique et à la sédentarité pour les adultes. 2018.", "u": "https://www.santepubliquefrance.fr/sites/default/files/rdd/document/42466_spf00000619.pdf"},
        ],
        "a_revoir": [
            "Peines de L. 4161-5 (2 ans et 30 000 €, 5 ans et 75 000 € en ligne) et de L. 4372-1 (1 an et 15 000 €), lues le 31/10/2026.",
            "Recommandations de Santé publique France de décembre 2018 : vérifier qu'une mise à jour n'a pas été publiée.",
            "Exonération de TVA pour un suivi nutrition : point INCERTAIN de la fiche 3.4, à revoir avec CIBS L. 213-91 en 2027.",
        ],
    },
    {
        "slug": "reglementation-vente-programme-sportif",
        "cat": "En ligne",
        "title": "Vente de programmes sportifs : ce que dit la réglementation",
        "description": "Réglementation de la vente de programmes sportifs : carte professionnelle, rétractation, garantie, promesses, fiscalité. Ce qui est clair, ce qui reste ouvert.",
        "date": "2026-12-02",
        "body": """
<p>La réponse courte : je n'ai trouvé aucun texte propre à la <strong>vente de programmes sportifs</strong>. Le code du sport, le code de la consommation et les règles fiscales s'appliquent selon ce que tu vends. Selon le ministère des sports, un coach en ligne a les mêmes obligations qu'en présentiel dès que son activité relève de l'enseignement, de l'animation ou de l'encadrement. Pour un programme standard vendu sans suivi, la question n'est pas tranchée.</p>

<h2>Faut-il une carte professionnelle pour vendre un programme ?</h2>
<p>L'article L. 212-1 du code du sport réserve aux titulaires d'une certification le fait d'enseigner, d'animer ou d'encadrer une activité physique contre rémunération, ou d'en entraîner les pratiquants. En 2026, l'article L. 212-8 punit l'exercice sans la qualification requise d'un an d'emprisonnement et de 15 000 € d'amende.</p>
<p>Dans une réponse publiée au Journal officiel le 29 avril 2025, le ministère des sports écrit que ce texte ne distingue pas le présentiel du distanciel. Le coach en ligne reste soumis à la qualification, à la déclaration avec carte à jour, à l'honorabilité et à l'assurance de responsabilité civile. Il ajoute qu'il travaille avec la DGCCRF pour développer les contrôles sur les plateformes numériques.</p>
<p>Cette réponse ne dit pas où commence l'encadrement pour un PDF, une vidéo ou une application vendus sans suivi. Elle n'a pas la valeur d'une loi, et je n'ai trouvé aucun texte plus récent. Personne ne peut donc t'affirmer que c'est autorisé, ni que c'est interdit. Une lecture de prudence : plus le suivi est individualisé, plus l'activité se rapproche de l'encadrement.</p>
<p>Sans qualification ni carte, tu ne peux pas vendre de coaching, en ligne comme ailleurs : notre guide <a href="/coachs/coach-sportif-sans-diplome.html">coach sportif sans diplôme</a> détaille les risques. Pour un programme sans suivi, interroge par écrit ton service départemental à la jeunesse, à l'engagement et aux sports, ou un avocat.</p>

<h2>Quelles règles s'appliquent à une vente en ligne ?</h2>
<p>Dès qu'un particulier achète sur ton site, le code de la consommation encadre le parcours. La pratique est dans notre guide pour <a href="/coachs/vendre-programme-sportif-en-ligne.html">vendre en ligne</a>.</p>
<ul>
<li><strong>Avant l'achat :</strong> caractéristiques, prix, durée, rétractation et médiateur, repris dans des <a href="/coachs/cgv-coach-sportif.html">CGV</a> publiées sur le site (L. 221-5).</li>
<li><strong>Au paiement :</strong> la validation indique clairement l'obligation de payer, par exemple « commande avec obligation de paiement » (L. 221-14).</li>
<li><strong>Après l'achat :</strong> tu confirmes le contrat sur un support durable, avec le formulaire de rétractation (L. 221-13).</li>
<li><strong>Pendant 14 jours :</strong> une fonction gratuite, du type « renoncer au contrat ici », reste accessible sur le site (L. 221-21, depuis le 19 juin 2026).</li>
<li><strong>En abonnement :</strong> si le client peut s'abonner en ligne, il doit pouvoir résilier en ligne, gratuitement.</li>
</ul>

<h2>Un client peut-il se faire rembourser un programme ?</h2>
<p>Oui, dans les 14 jours suivant l'achat en ligne, sauf cas précis :</p>
<ul>
<li><strong>Fichier téléchargeable :</strong> le client perd sa rétractation seulement s'il a demandé l'accès immédiat, reconnu perdre ce droit, et si tu lui as confirmé cet accord (L. 221-28, 13°). Sans ces trois éléments, il peut se rétracter et ne rien devoir.</li>
<li><strong>Suivi à distance :</strong> s'il demande à commencer tout de suite puis se rétracte, il paie la part déjà fournie (L. 221-25). Sans demande expresse, il ne doit rien.</li>
</ul>
<p>Le programme bénéficie aussi d'une garantie légale de conformité (L. 224-25-12 et suivants). Pour une fourniture unique, tu réponds des défauts qui apparaissent dans les 2 ans, et ceux des 12 premiers mois sont présumés exister dès la fourniture. Pour un accès continu, tu en réponds pendant toute sa durée. Exemples : fichier illisible, vidéos inaccessibles, contenu différent de la description. Le client a droit à la mise en conformité gratuite, sinon à une réduction du prix ou à la résolution, sauf défaut mineur.</p>

<h2>Que peux-tu promettre sur ta page de vente ?</h2>
<p>L'article L. 121-2 du code de la consommation vise les allégations trompeuses, notamment sur les résultats attendus d'un service et sur tes qualités. Promettre un résultat que tu ne peux ni tenir ni prouver peut constituer une pratique commerciale trompeuse, qui est un délit.</p>
<ul>
<li><strong>Résultats :</strong> pas de chiffre garanti dans un délai. Tout ce que tu décris sert aussi à juger la conformité du programme.</li>
<li><strong>Santé :</strong> affirmer faussement qu'un service guérit une maladie est réputé trompeur (L. 121-4, 16°). Évite tout discours de soin et tout programme présenté pour une pathologie.</li>
<li><strong>Témoignages :</strong> de vrais clients, sans retouche du texte (L. 121-4, 27° et 28°), avec un accord écrit pour chaque photo.</li>
<li><strong>Prudence :</strong> indique le niveau visé, et demande de consulter un médecin en cas de symptômes.</li>
</ul>

<h2>Comment déclarer ces ventes ?</h2>
<p>Je n'ai trouvé aucune source officielle qui qualifie le programme numérique standard. Un programme personnalisé avec suivi et un fichier identique vendu à tous peuvent être traités différemment. N'en déduis ni BNC ni BIC : demande la qualification à l'URSSAF ou aux impôts et garde la réponse. Notre guide <a href="/coachs/coach-sportif-bic-ou-bnc.html">BIC ou BNC</a> pose le cadre.</p>
<p>Même prudence pour la TVA. L'exonération des cours suppose des leçons données à titre personnel : ne présente pas un téléchargement comme exonéré. Un fichier vendu à des particuliers d'autres pays de l'UE peut aussi relever des services électroniques. En 2026, selon impots.gouv.fr, au-delà de 10 000 € HT de chiffre d'affaires annuel sur ces ventes, apprécié sur l'année en cours et la précédente, la TVA est due dans le pays du client.</p>
<p>Ce guide informe, il ne remplace pas l'avis d'un avocat ou d'un expert-comptable.</p>

<h2>Ce qu'il faut retenir</h2>
<ul>
<li>Un suivi en ligne relève des mêmes obligations qu'en présentiel. Pour un programme sans suivi, le droit n'est pas tranché.</li>
<li>En ligne, prévois l'information, la confirmation, la rétractation et la garantie de conformité.</li>
<li>Ne garantis aucun résultat, et fais qualifier tes ventes par l'URSSAF ou les impôts.</li>
</ul>
""",
        "faq": [
            {"q": "Faut-il un diplôme pour vendre un programme sportif en ligne ?",
             "a": "Pour une activité d'enseignement, d'animation ou d'encadrement, oui : le ministère applique les mêmes obligations qu'en présentiel, carte comprise. Pour un programme vendu sans suivi, la question n'est pas tranchée. Ne conclus ni que c'est libre, ni que c'est interdit, et interroge ton service départemental ou un avocat."},
            {"q": "Peut-on se faire rembourser un programme sportif en PDF ?",
             "a": "Acheté en ligne, il ouvre 14 jours de rétractation. Le client perd ce droit seulement s'il a demandé l'accès immédiat, reconnu perdre ce droit, et si le vendeur a confirmé cet accord. Sans ces trois éléments, il peut se rétracter et ne rien devoir. La garantie légale de conformité s'ajoute à ce droit."},
            {"q": "Vendre un programme sportif en ligne, est-ce du BIC ou du BNC ?",
             "a": "Je n'ai trouvé aucune source officielle qui le dise pour un programme numérique standard. Un programme personnalisé avec suivi et un fichier identique vendu à tous peuvent être qualifiés différemment. Demande la réponse à l'URSSAF ou aux impôts, et garde-la."},
        ],
        "sources": [
            {"t": "Assemblée nationale. Question écrite n° 714, réponse publiée le 29 avril 2025.", "u": "https://www.assemblee-nationale.fr/dyn/17/questions/QANR5L17QE714"},
            {"t": "Code du sport, articles L. 212-1 à L. 212-8.", "u": "https://www.legifrance.gouv.fr/codes/section_lc/LEGITEXT000006071318/LEGISCTA000006167038/"},
            {"t": "Code de la consommation, articles L. 221-1 à L. 221-29.", "u": "https://www.legifrance.gouv.fr/codes/section_lc/LEGITEXT000006069565/LEGISCTA000032221319/"},
            {"t": "Code de la consommation, articles L. 224-25-12 à L. 224-25-26.", "u": "https://www.legifrance.gouv.fr/codes/section_lc/LEGITEXT000006069565/LEGISCTA000044132865/"},
            {"t": "Code de la consommation, articles L. 121-2 à L. 121-5.", "u": "https://www.legifrance.gouv.fr/codes/section_lc/LEGITEXT000006069565/LEGISCTA000032220953/"},
            {"t": "impots.gouv.fr. Guichet unique TVA : suis-je concerné ? 2024.", "u": "https://www.impots.gouv.fr/professionnel/suis-je-concerne-0"},
        ],
        "a_revoir": [
            "Réponse ministérielle n° 714 du 29/04/2025 : interroger les bases de l'Assemblée et du Sénat pour une réponse plus récente sur les coachs en ligne.",
            "Fonction de rétractation en ligne, L. 221-21 et D. 221-5, en vigueur depuis le 19/06/2026.",
            "Seuil de 10 000 € HT pour la TVA des services électroniques (page impots.gouv.fr modifiée le 22/03/2024) et articulation avec la franchise en base.",
            "Qualification fiscale et TVA du programme numérique standard : points INCERTAIN des fiches 2.5 et 3.4, à revoir avec le CIBS en 2027.",
        ],
    },
]
