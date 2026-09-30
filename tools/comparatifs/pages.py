# -*- coding: utf-8 -*-
"""Pages comparatives (FR + EN) : récupération, apps sommeil/alimentation/sport, âge biologique.

Rédigées le 30/09/2026. Règles suivies :
- Concurrents : uniquement leurs pages officielles (support, manuels, documentation,
  communiqués, fiches App Store), chaque fait rattaché à une URL de `sources`.
  Aucun prix ; seulement « abonnement requis : oui / non » quand la page le permet.
- Ecleptic : uniquement les faits publiés sur les pages méthode (tools/methode/
  readiness_score.py, vitaux.py, ligne_de_base.py, nutrition.py, age_biologique.py).
  Aucun chiffre du calcul de l'âge biologique (plafonds, marges, bornes) : la logique seule.
  Bêta iOS gratuite : aucun prix.
- Publicité comparative (art. L122-1 C. conso) : caractéristiques essentielles,
  vérifiables, pertinentes ; pas de dénigrement ni de superlatif ; transparence dès
  l'introduction.
- Corps : liens internes seulement (/methode/…, /articles/… publiés) ; aucun lien externe.
- Pages support WHOOP (Salesforce, rendu JavaScript) : texte lu via l'API publique du
  site (getArticleVersionId + getRecordWithLayouts), dates de publication relevées.
"""

VERIFIED = "2026-09-30"

TRANSPARENCE_FR = ("<p><em>Ecleptic est notre application ; ce comparatif s'en tient aux informations "
                   "publiques de chaque marque, liées en source, vérifiées le 30 septembre 2026.</em></p>")
TRANSPARENCE_EN = ("<p><em>Ecleptic is our app; this comparison sticks to each brand's public "
                   "information, linked in the sources below, checked on September 30, 2026.</em></p>")


# ---------------------------------------------------------------------------
# 1. Score de récupération
# ---------------------------------------------------------------------------
P_RECUPERATION = {
    "key": "recuperation",
    "slug_fr": "score-de-recuperation-whoop-oura-garmin-apple",
    "slug_en": "recovery-score-whoop-oura-garmin-apple",
    "date": "2026-09-30",
    "fr": {
        "title": "Score de récupération : comment Whoop, Oura, Garmin, Apple Watch et Ecleptic le calculent",
        "seo_title": "Score de récupération : Whoop, Oura, Garmin, Apple",
        "description": "Whoop, Oura, Garmin, Apple Watch et Ecleptic : nom du score de récupération, échelle, signaux, fenêtre de référence, matériel et abonnement, sources liées.",
        "lead": "Les cinq comparent tes signaux de la nuit à ta propre normale, mais pas sur la même échelle : 0 à 100 % chez Whoop, 1 à 100 chez Garmin, 0 à 10 sur l'Apple Watch, sur 100 chez Oura et Ecleptic. D'après les pages officielles consultées, l'alimentation n'entre directement que dans le calcul d'Ecleptic.",
        "body": TRANSPARENCE_FR + """
<h2>Le principe commun : toi contre toi</h2>
<p>Un score de récupération répond à une question : ce matin, ton corps est-il prêt à encaisser un effort ? Les cinq partent de la même idée : situer tes signaux de la nuit, à commencer par ta <a href="/articles/hrv-variabilite-frequence-cardiaque.html">variabilité cardiaque (HRV)</a> et ta <a href="/articles/frequence-cardiaque-repos-normale.html">fréquence cardiaque au repos</a>, face à ta propre normale, pas à une moyenne de population.</p>

<h2>Le tableau comparatif</h2>
<div class="tablewrap"><table>
<caption>Informations publiées par chaque marque, vérifiées le 30 septembre 2026. Sources en bas de page.</caption>
<thead><tr><th>Marque</th><th>Score</th><th>Échelle</th><th>Signaux publiés</th><th>Référence personnelle</th><th>Matériel</th><th>Abonnement requis</th></tr></thead>
<tbody>
<tr><td>Whoop</td><td>Recovery</td><td>0 à 100 %</td><td>HRV, FC au repos, respiration, sommeil face au besoin, sommeil léger et éveils, température cutanée, SpO₂, phase du cycle</td><td>HRV : 30 jours</td><td>Capteur WHOOP</td><td>Oui, capteur inclus</td></tr>
<tr><td>Oura</td><td>Score de préparation</td><td>0 à 100</td><td>9 contributeurs : FC au repos, HRV, température, indice de récupération, sommeil, activité</td><td>14 jours face à 2 ou 3 mois</td><td>Bague Oura</td><td>Non pour le score du jour ; oui pour le détail</td></tr>
<tr><td>Garmin</td><td>Préparation à l'entraînement</td><td>1 à 100</td><td>Sommeil, temps de récupération, état HRV, charge aiguë, stress des 3 derniers jours</td><td>HRV : moyenne sur 7 jours face à ta plage de référence</td><td>Montre Garmin compatible</td><td>Non, calculé par la montre</td></tr>
<tr><td>Apple Watch</td><td>Score de préparation</td><td>0 à 10</td><td>Activité et charge d'entraînement, signes vitaux de nuit et de jour, score de sommeil</td><td>Au moins 7 des 49 dernières nuits</td><td>Series 12 ou Ultra 4</td><td>Aucun dans les prérequis</td></tr>
<tr><td>Ecleptic</td><td>Readiness Score</td><td>Sur 100</td><td>Vitaux de la nuit, sommeil, nutrition, rythme et charge</td><td>Vitaux : 42 jours</td><td>iPhone ; montre facultative</td><td>Bêta iOS gratuite</td></tr>
</tbody>
</table></div>

<h2>Whoop : la Recovery, de 0 à 100 %</h2>
<p>Calculée chaque nuit et livrée au réveil, la Recovery est verte à partir de 67 %, rouge à 33 % et moins. Elle combine huit signaux : HRV, fréquence au repos, fréquence respiratoire, heures de sommeil face au besoin estimé, sommeil léger et éveils, température cutanée, SpO₂ et, le cas échéant, phase du cycle. Whoop précise que la HRV et la fréquence au repos pèsent le plus, et que ta HRV est comparée à ta ligne de base sur 30 jours. Le score ne change pas dans la journée, sauf si tu modifies ta nuit.</p>

<h2>Oura : le score de préparation</h2>
<p>Noté de 0 à 100 (optimal à partir de 85), il repose sur neuf contributeurs : fréquence au repos, équilibre HRV, température, indice de récupération, sommeil, équilibre et régularité du sommeil, activité de la veille, équilibre d'activité. Les contributeurs « équilibre » comparent tes 14 derniers jours à ta moyenne de long terme (deux mois, trois pour l'équilibre HRV), et Oura compte jusqu'à deux semaines pour apprendre tes valeurs. Sans abonnement actif, l'app affiche encore tes trois scores du jour ; l'abonnement débloque le détail.</p>

<h2>Garmin : la préparation à l'entraînement</h2>
<p>Sur les montres compatibles, comme la Venu X1 ou la Forerunner 965, ce score de 1 à 100 est recalculé en continu à partir de six facteurs : score de sommeil de la nuit, temps de récupération, état HRV, charge aiguë, sommeil des trois dernières nuits et stress des trois derniers jours. La comparaison à ta normale passe par l'état HRV : ta moyenne sur sept jours face à ta plage de référence, affichée après trois semaines de nuits régulières.</p>

<h2>Apple Watch : le score de préparation, de 0 à 10</h2>
<p>Avec watchOS 27, l'app Préparation de l'Apple Watch Series 12 et Ultra 4 note de 0 à 10, de « Récupérez » (0-1) à « Foncez » (8-10). Elle croise ton activité récente (calories actives, effort, charge d'entraînement), tes signes vitaux de nuit (fréquence cardiaque et respiratoire, température du poignet, HRV, oxygène sanguin) et de jour, et ton score de sommeil. Les vitaux sont comparés à ta ligne de base récente, qui exige au moins 7 nuits avec la montre sur les 49 dernières. Le score évolue dans la journée.</p>

<h2>Ecleptic : un score sur 100 qui intègre ta nutrition</h2>
<p>Notre Readiness Score part de ta nuit au réveil, puis se met à jour avec tes repas et tes séances. Ses quatre piliers et leurs poids sont publiés : <a href="/methode/vitaux.html">vitaux de la nuit</a> (42 points), sommeil (21), <a href="/methode/nutrition.html">nutrition</a> (21) et rythme avec charge d'entraînement (16). Chaque vital est comparé à ta normale des 42 derniers jours : 7 jours pour qu'une <a href="/methode/ligne-de-base.html">ligne de base</a> existe, 28 pour qu'elle soit pleinement fiable. Le détail : <a href="/methode/readiness-score.html">la méthode du Readiness Score</a>.</p>

<h2>Ce qui change vraiment d'un score à l'autre</h2>
<ul>
<li><strong>L'échelle :</strong> un 70 chez l'un ne vaut pas un 70 chez l'autre ; compare chaque score à son propre historique.</li>
<li><strong>La fenêtre :</strong> 30 jours pour la HRV chez Whoop, 14 jours face à deux ou trois mois chez Oura, 49 nuits chez Apple, 42 jours chez Ecleptic. Courte, elle réagit vite ; longue, elle lisse.</li>
<li><strong>Le rythme :</strong> Whoop fige sa Recovery pour la journée ; Garmin, Apple et Ecleptic font évoluer leur score.</li>
<li><strong>Les ingrédients :</strong> tous lisent le cœur et le sommeil ; Garmin, Oura et Apple ajoutent l'activité ou la charge. Parmi les signaux publiés, l'alimentation n'apparaît que chez Ecleptic ; Whoop la relie à la Recovery par les corrélations de son Journal.</li>
</ul>

<h2>Comment lire ton score</h2>
<p>Whoop, Apple et Ecleptic le précisent : ces scores sont des repères de bien-être, pas des diagnostics. Une journée basse n'est pas une alerte ; c'est la tendance qui compte. À lire aussi : <a href="/articles/readiness-score-comment-ca-marche.html">comment fonctionne un readiness score</a>.</p>
""",
        "faq": [
            {"q": "Comment Whoop calcule-t-il son score de récupération ?",
             "a": "Chaque nuit, Whoop combine ta HRV, comparée à ta ligne de base sur 30 jours, ta fréquence au repos, ta respiration, ton sommeil face à ton besoin, ta température cutanée, ta SpO₂ et la phase du cycle. Le score va de 0 à 100 % : vert à partir de 67 %."},
            {"q": "Quelle différence entre le score de préparation de l'Apple Watch et la Recovery de Whoop ?",
             "a": "Apple note de 0 à 10, Whoop de 0 à 100 %. Apple intègre ton activité et ta charge d'entraînement et fait évoluer son score dans la journée ; la Recovery de Whoop reste fixe jusqu'au lendemain."},
            {"q": "Peut-on avoir un score de récupération sans montre ni bague ?",
             "a": "Whoop, Oura, Garmin et Apple calculent leur score avec leur propre appareil. Ecleptic fonctionne aussi sans montre : le pilier des vitaux est retiré et son poids redistribué entre le sommeil, la nutrition et le rythme, avec un indice de confiance."},
        ],
    },
    "en": {
        "title": "Recovery score: how Whoop, Oura, Garmin, Apple Watch and Ecleptic calculate it",
        "seo_title": "Recovery score: Whoop, Oura, Garmin, Apple compared",
        "description": "Whoop, Oura, Garmin, Apple Watch and Ecleptic: each recovery score's name, scale, signals, personal baseline, hardware and subscription, with linked sources.",
        "lead": "All five compare your overnight signals with your own normal, but not on the same scale or with the same ingredients: Whoop rates Recovery from 0 to 100%, Oura and Ecleptic out of 100, Garmin from 1 to 100, Apple Watch from 0 to 10, and among the signals these five brands publish, only Ecleptic's includes what you eat.",
        "body": TRANSPARENCE_EN + """
<h2>The shared principle: you versus you</h2>
<p>A recovery score answers one question: is your body ready to take on effort this morning? The five tools compared here start from the same idea: place your overnight signals, starting with your <a href="/articles/hrv-variabilite-frequence-cardiaque.html">heart rate variability (HRV)</a> and your <a href="/articles/frequence-cardiaque-repos-normale.html">resting heart rate</a>, against your own normal rather than a population average.</p>

<h2>The comparison table</h2>
<div class="tablewrap"><table>
<caption>Information published by each brand, checked on September 30, 2026. Sources at the bottom of the page.</caption>
<thead><tr><th>Brand</th><th>Score</th><th>Scale</th><th>Published signals</th><th>Personal baseline</th><th>Hardware</th><th>Subscription required</th></tr></thead>
<tbody>
<tr><td>Whoop</td><td>Recovery</td><td>0 to 100%</td><td>HRV, resting heart rate, respiratory rate, sleep vs. need, light sleep and awake time, skin temperature, SpO₂, cycle phase</td><td>HRV: 30 days</td><td>WHOOP sensor</td><td>Yes, sensor included</td></tr>
<tr><td>Oura</td><td>Readiness Score</td><td>0 to 100</td><td>9 contributors: resting heart rate, HRV, temperature, recovery index, sleep, activity</td><td>14 days vs. 2 or 3 months</td><td>Oura Ring</td><td>No for the daily score; yes for the details</td></tr>
<tr><td>Garmin</td><td>Training Readiness</td><td>1 to 100</td><td>Sleep, recovery time, HRV status, acute load, stress over the last 3 days</td><td>HRV: 7-day average vs. your baseline range</td><td>Compatible Garmin watch</td><td>No, calculated on the watch</td></tr>
<tr><td>Apple Watch</td><td>Readiness score</td><td>0 to 10</td><td>Activity and training load, overnight and daytime vitals, sleep score</td><td>At least 7 of the past 49 nights</td><td>Series 12 or Ultra 4</td><td>None among the requirements</td></tr>
<tr><td>Ecleptic</td><td>Readiness Score</td><td>Out of 100</td><td>Overnight vitals, sleep, nutrition, rhythm and load</td><td>Vitals: 42 days</td><td>iPhone; watch optional</td><td>Free iOS beta</td></tr>
</tbody>
</table></div>

<h2>Whoop: Recovery, from 0 to 100%</h2>
<p>Calculated every night and delivered when you wake up, Recovery is green from 67% and red at 33% or below. It combines eight signals: HRV, resting heart rate, respiratory rate, hours of sleep versus estimated need, light sleep and awake time, skin temperature, SpO₂ and, where applicable, cycle phase. Whoop states that HRV and resting heart rate weigh the most, and that your HRV is compared with your 30-day baseline. The score does not change during the day unless you edit your sleep.</p>

<h2>Oura: the Readiness Score</h2>
<p>Rated from 0 to 100 (optimal from 85), it rests on nine contributors: resting heart rate, HRV balance, body temperature, recovery index, sleep, sleep balance, sleep regularity, previous day activity and activity balance. The "balance" contributors compare your last 14 days with your long-term average (two months, three for HRV balance), and Oura allows up to two weeks to learn your values. Without an active membership, the app still shows your three daily scores; the membership unlocks the details.</p>

<h2>Garmin: Training Readiness</h2>
<p>On compatible watches, such as the Venu X1 or the Forerunner 965, this 1-to-100 score is recalculated continuously from six factors: last night's sleep score, recovery time, HRV status, acute load, sleep over the last three nights and stress over the last three days. The comparison with your normal comes through HRV status: your seven-day average against your baseline range, shown after three weeks of consistent sleep data.</p>

<h2>Apple Watch: the readiness score, from 0 to 10</h2>
<p>With watchOS 27, the Readiness app on Apple Watch Series 12 and Ultra 4 scores you from 0 to 10, from "Recover" (0-1) to "Go For It" (8-10). It combines your recent activity (active calories, effort ratings, training load), your overnight vitals (heart rate, respiratory rate, wrist temperature, HRV, blood oxygen) and daytime heart rate, and your sleep score. Vitals are compared with your recent baseline, which requires at least 7 nights with the watch out of the past 49. The score changes during the day.</p>

<h2>Ecleptic: a score out of 100 that includes your nutrition</h2>
<p>Our Readiness Score starts from your night when you wake up, then updates with your meals and workouts. Its four pillars and their weights are published: <a href="/methode/vitaux.html">overnight vitals</a> (42 points), sleep (21), <a href="/methode/nutrition.html">nutrition</a> (21) and rhythm with training load (16). Each vital is compared with your normal over the last 42 days: 7 days for a <a href="/methode/ligne-de-base.html">baseline</a> to exist, 28 for it to be fully reliable. The details: <a href="/methode/readiness-score.html">the Readiness Score method</a>.</p>

<h2>What actually differs from one score to the next</h2>
<ul>
<li><strong>The scale:</strong> a 70 on one app is not a 70 on another. Compare each score with its own history, never across brands.</li>
<li><strong>The window:</strong> 30 days for HRV on Whoop, 14 days against two or three months on Oura, 49 nights on Apple Watch, 42 days on Ecleptic. A short window reacts fast; a long one smooths.</li>
<li><strong>The timing:</strong> Whoop locks Recovery for the day; Garmin, Apple and Ecleptic let their score move.</li>
<li><strong>The ingredients:</strong> all of them read your heart and your sleep; Garmin, Oura and Apple add activity or load. According to the official pages we checked, food feeds directly into Ecleptic's calculation only; Whoop links it to Recovery through the correlations in its Journal.</li>
</ul>

<h2>How to read your score</h2>
<p>Whoop, Apple and Ecleptic all say it: these scores are wellness guides, not diagnoses. One low day is not an alarm; the trend is what counts. To go further: <a href="/articles/readiness-score-comment-ca-marche.html">how a readiness score works</a>.</p>
""",
        "faq": [
            {"q": "How does Whoop calculate its recovery score?",
             "a": "Every night, Whoop combines your HRV, compared with your 30-day baseline, resting heart rate, respiratory rate, sleep versus need, skin temperature, SpO₂ and cycle phase. The score runs from 0 to 100%: green from 67%, red at 33% or below."},
            {"q": "What is the difference between the Apple Watch readiness score and Whoop Recovery?",
             "a": "Apple scores from 0 to 10, Whoop from 0 to 100%. Apple factors in your activity and training load and lets its score move during the day; Whoop Recovery stays fixed until the next morning."},
            {"q": "Can you get a recovery score without a watch or a ring?",
             "a": "Whoop, Oura, Garmin and Apple calculate their score with their own device. Ecleptic also works without a watch: the vitals pillar is removed and its weight shared among sleep, nutrition and rhythm, with a confidence index."},
        ],
    },
    "sources": [
        {"t": "WHOOP. WHOOP Recovery (support, publié le 11 septembre 2025). Consulté le 30 septembre 2026.",
         "u": "https://support.whoop.com/s/article/WHOOP-Recovery?language=en_US"},
        {"t": "WHOOP for Developers. WHOOP 101. Consulté le 30 septembre 2026.",
         "u": "https://developer.whoop.com/docs/whoop-101/"},
        {"t": "WHOOP. Membership Pricing (support, publié le 28 mai 2026). Consulté le 30 septembre 2026.",
         "u": "https://support.whoop.com/s/article/Membership-Pricing?language=en_US"},
        {"t": "WHOOP. WHOOP Journal Overview (support, publié le 18 septembre 2026). Consulté le 30 septembre 2026.",
         "u": "https://support.whoop.com/s/article/WHOOP-Journal-Overview?language=en_US"},
        {"t": "Oura. Readiness Score (Member Care, mis à jour le 14 juillet 2026). Consulté le 30 septembre 2026.",
         "u": "https://support.ouraring.com/hc/en-us/articles/360025589793-Readiness-Score"},
        {"t": "Oura. Readiness Contributors (Member Care, mis à jour le 14 juillet 2026). Consulté le 30 septembre 2026.",
         "u": "https://support.ouraring.com/hc/en-us/articles/360057791533-Readiness-Contributors"},
        {"t": "Oura. Score de préparation (Member Care, version française). Consulté le 30 septembre 2026.",
         "u": "https://support.ouraring.com/hc/fr/articles/360025589793-Score-de-pr%C3%A9paration"},
        {"t": "Oura. Oura Membership (Member Care, mis à jour le 8 septembre 2026). Consulté le 30 septembre 2026.",
         "u": "https://support.ouraring.com/hc/en-us/articles/4409086524819-Oura-Membership"},
        {"t": "Garmin. Manuel d'utilisation Venu X1 : Training Readiness (septembre 2026). Consulté le 30 septembre 2026.",
         "u": "https://www8.garmin.com/manuals/webhelp/GUID-C144B465-A0C8-4FE9-AFE6-41A3FE3F1D9A/EN-US/GUID-C21BE0C8-A08E-4DA1-B6C6-2E0E2DDDB372.html"},
        {"t": "Garmin. Manuel d'utilisation Venu X1 : Préparation à l'entraînement (version française). Consulté le 30 septembre 2026.",
         "u": "https://www8.garmin.com/manuals/webhelp/GUID-C144B465-A0C8-4FE9-AFE6-41A3FE3F1D9A/FR-FR/GUID-C21BE0C8-A08E-4DA1-B6C6-2E0E2DDDB372.html"},
        {"t": "Garmin. Manuel d'utilisation Venu X1 : Heart Rate Variability Status. Consulté le 30 septembre 2026.",
         "u": "https://www8.garmin.com/manuals/webhelp/GUID-C144B465-A0C8-4FE9-AFE6-41A3FE3F1D9A/EN-US/GUID-9282196F-D969-404D-B678-F48A13D8D0CB.html"},
        {"t": "Garmin. Manuel d'utilisation Forerunner 965 : Training Readiness. Consulté le 30 septembre 2026.",
         "u": "https://www8.garmin.com/manuals/webhelp/GUID-0221611A-992D-495E-8DED-1DD448F7A066/EN-US/GUID-C21BE0C8-A08E-4DA1-B6C6-2E0E2DDDB372.html"},
        {"t": "Apple. Guide d'utilisation de l'Apple Watch : Use the Readiness app on Apple Watch (watchOS 27). Consulté le 30 septembre 2026.",
         "u": "https://support.apple.com/guide/watch/readiness-flx4gnzby346/watchos"},
        {"t": "Apple. Understand your readiness score on Apple Watch (publié le 14 septembre 2026). Consulté le 30 septembre 2026.",
         "u": "https://support.apple.com/en-us/128112"},
        {"t": "Apple. Comprendre votre score de préparation sur l'Apple Watch (publié le 28 septembre 2026). Consulté le 30 septembre 2026.",
         "u": "https://support.apple.com/fr-fr/128112"},
        {"t": "Apple. Use the Vitals app on Apple Watch (publié le 14 septembre 2026). Consulté le 30 septembre 2026.",
         "u": "https://support.apple.com/en-us/120142"},
    ],
}


# ---------------------------------------------------------------------------
# 2. Relier sommeil, alimentation et sport sur iPhone
# ---------------------------------------------------------------------------
P_APPS = {
    "key": "apps-iphone",
    "slug_fr": "application-sommeil-alimentation-sport-iphone",
    "slug_en": "app-sleep-nutrition-training-iphone",
    "date": "2026-09-30",
    "fr": {
        "title": "Quelle app pour relier sommeil, alimentation et sport sur iPhone ?",
        "seo_title": "Sommeil, alimentation et sport sur iPhone : quelle app ?",
        "description": "Whoop, Oura, Athlytic, Apple Santé, MyFitnessPal, Yazio, Ecleptic : ce que chaque app relie entre sommeil, alimentation et sport, d'après ses pages officielles.",
        "lead": "Sur iPhone, les apps de récupération (Whoop, Oura, Athlytic, Apple) partent du sommeil et du cœur, les journaux alimentaires (MyFitnessPal, Yazio) partent de l'assiette. Pour relier les deux, certaines corrèlent un journal de comportements avec ta récupération ; Ecleptic fait entrer ta nutrition dans le calcul du score du jour lui-même.",
        "body": TRANSPARENCE_FR + """
<h2>Relier, ça peut vouloir dire trois choses</h2>
<ul>
<li><strong>Juxtaposer :</strong> voir ta nuit, tes repas et tes séances dans la même app.</li>
<li><strong>Corréler :</strong> noter un comportement (alcool, dîner tardif, calories) et voir, au fil des semaines, s'il coïncide avec une meilleure ou une moins bonne récupération.</li>
<li><strong>Intégrer :</strong> faire entrer l'alimentation dans le calcul du score du jour.</li>
</ul>
<p>Ce n'est pas un classement : le tableau indique, pour chaque app, ce que décrivent ses pages officielles.</p>

<h2>Le tableau des fonctionnalités</h2>
<div class="tablewrap"><table>
<caption>Fonctionnalités décrites par chaque éditeur (pages d'assistance ou fiche App Store), vérifiées le 30 septembre 2026. Sources en bas de page.</caption>
<thead><tr><th>App</th><th>Sommeil</th><th>Alimentation</th><th>Entraînement</th><th>Repère quotidien</th><th>Matériel</th><th>Abonnement requis</th></tr></thead>
<tbody>
<tr><td>Whoop</td><td>Oui</td><td>Comportements du Journal ; import d'autres apps via Apple Santé</td><td>Strain, activités détectées ou importées</td><td>Recovery (cœur, sommeil, température, SpO₂)</td><td>Capteur WHOOP</td><td>Oui</td></tr>
<tr><td>Oura</td><td>Oui</td><td>Meals : photo ou texte, analyse assistée par IA (en anglais)</td><td>Activité, détection automatique</td><td>Score de préparation (9 contributeurs)</td><td>Bague Oura</td><td>Oui pour Meals ; score du jour visible sans</td></tr>
<tr><td>Athlytic</td><td>Oui</td><td>Énergie consommée et macros, lues dans Apple Santé</td><td>Effort (Exertion), séances</td><td>Recovery (HRV et FC au repos de la nuit)</td><td>iPhone et Apple Watch pour l'essentiel</td><td>Oui pour l'app complète</td></tr>
<tr><td>Apple Santé et Fitness</td><td>Score de sommeil</td><td>Via d'autres apps, dont Santé centralise les données</td><td>Activité, charge d'entraînement</td><td>Score de préparation (activité, signes vitaux, sommeil)</td><td>Apple Watch Series 12 ou Ultra 4 pour la Préparation</td><td>Aucun dans les prérequis</td></tr>
<tr><td>MyFitnessPal</td><td>Non décrit sur sa fiche</td><td>Calories et macros ; scans code-barres et repas en Premium</td><td>Séances et pas ; plus de 40 appareils et apps connectables</td><td>Objectifs caloriques et macros</td><td>iPhone</td><td>Non pour le journal ; Premium pour les scans</td></tr>
<tr><td>Yazio</td><td>Non décrit sur sa fiche</td><td>Compteur de calories assisté par IA, code-barres, jeûne</td><td>Pas et activité ; synchro Fitbit ou Garmin en Pro</td><td>Objectif calorique</td><td>iPhone</td><td>Non pour le compteur ; Pro pour les fonctions avancées</td></tr>
<tr><td>Ecleptic</td><td>Oui</td><td>Scan photo, code-barres, recherche ; valeurs Ciqual, USDA, Open Food Facts</td><td>Séances, charge d'entraînement</td><td>Readiness Score (vitaux, sommeil, nutrition, rythme)</td><td>iPhone ; montre facultative</td><td>Bêta iOS gratuite</td></tr>
</tbody>
</table></div>

<h2>Whoop et Oura : le capteur d'abord</h2>
<p>Whoop et Oura mesurent ta nuit avec leur propre appareil. Leur score du jour repose sur le cœur, le sommeil, la température et, chez Oura, l'activité ; l'alimentation ne figure pas parmi leurs signaux publiés. Whoop la relie par corrélation : son Journal propose des comportements de nutrition (calories, protéines, glucides…), peut en recevoir d'autres apps via Apple Santé, et ses Behavior Insights mesurent leur effet sur ta récupération dès 5 réponses « oui » et 5 « non » sur 90 jours. Oura propose Meals : tu photographies ou décris ton repas, une analyse assistée par IA situe ses protéines, fibres, sucres ajoutés ou son degré de transformation (faible, modéré, élevé), et tes repas s'affichent sur une horloge de 24 heures à côté de tes heures de coucher et de lever. Meals demande un abonnement actif et n'existe pour l'instant qu'en anglais.</p>

<h2>Athlytic et Apple : tout part de l'Apple Watch</h2>
<p>Avec watchOS 27, l'Apple Watch Series 12 et Ultra 4 calcule déjà un score de préparation qui croise activité, signes vitaux et sommeil, et l'app Santé centralise les données d'autres apps. Athlytic lit ces données dans Apple Santé : sa Recovery compare ta HRV et ta fréquence au repos de la nuit à ta ligne de base, son Journal mesure l'effet de la caféine, de l'alcool ou d'un voyage sur ta récupération et ton sommeil, et ses tendances affichent l'énergie consommée et dépensée.</p>

<h2>MyFitnessPal et Yazio : l'assiette d'abord</h2>
<p>MyFitnessPal décrit un journal de calories et de macros avec coach IA, l'enregistrement des séances et des pas, et la connexion à plus de 40 appareils et apps ; les scans de code-barres et de repas font partie de Premium. Yazio décrit un compteur de calories assisté par IA avec scan de code-barres, un suivi du jeûne intermittent et un suivi intégré des pas et de l'activité ; la synchronisation avec Fitbit ou Garmin fait partie de Pro. Ni l'une ni l'autre fiche ne mentionne de score de récupération ou de suivi du sommeil.</p>

<h2>Ecleptic : l'alimentation dans le score du jour</h2>
<p>Ecleptic intègre : ta nutrition pèse 21 points sur 100 dans ton <a href="/methode/readiness-score.html">Readiness Score</a>, à côté des vitaux de la nuit (42), du sommeil (21) et du rythme avec la charge d'entraînement (16). Tu photographies ton repas (jusqu'à 3 photos), scannes un code-barres ou cherches un aliment : l'IA reconnaît les aliments et estime les portions, les valeurs viennent des bases officielles (table Ciqual de l'ANSES, USDA FoodData Central, Open Food Facts). Le pilier juge l'adéquation à tes <a href="/methode/cibles.html">cibles</a>, les protéines après l'effort, les micronutriments et l'hydratation, et il est plafonné à 80 si tu as bu de l'alcool la veille. Le détail : <a href="/methode/nutrition.html">la méthode nutrition</a>.</p>

<h2>Comment choisir selon ce que tu as déjà</h2>
<ul>
<li><strong>Une Apple Watch Series 12 ou Ultra 4 :</strong> le score de préparation est déjà dans ta montre ; une app qui lit Apple Santé peut y ajouter un journal ou tes repas.</li>
<li><strong>Un Whoop :</strong> vérifie que ton app alimentaire écrit dans Apple Santé, d'où Whoop importe la nutrition dans son Journal.</li>
<li><strong>Compter tes calories avant tout :</strong> c'est le cœur de MyFitnessPal et de Yazio.</li>
<li><strong>Que tes repas pèsent dans ton score du matin :</strong> c'est le principe d'Ecleptic.</li>
</ul>
<p>Dans tous les cas, c'est dans Apple Santé que tu choisis, catégorie par catégorie, ce que chaque app peut lire.</p>
""",
        "faq": [
            {"q": "Quelle app relie l'alimentation à la récupération sur iPhone ?",
             "a": "Parmi les apps comparées : Whoop corrèle les comportements de son Journal, dont la nutrition, avec ta récupération ; Athlytic mesure l'effet des entrées de son Journal sur sa Recovery ; Ecleptic intègre directement la nutrition à son Readiness Score, pour 21 points sur 100."},
            {"q": "MyFitnessPal ou Yazio calculent-ils un score de récupération ?",
             "a": "Leurs fiches App Store décrivent le suivi des calories, des macros, de l'activité et des pas, mais ne mentionnent ni score de récupération ni suivi du sommeil. Pour croiser ces données avec ta nuit, il faut les faire lire par une autre app."},
            {"q": "Faut-il une Apple Watch pour relier sommeil, alimentation et sport ?",
             "a": "Pas forcément. Whoop et Oura utilisent leur propre capteur, MyFitnessPal et Yazio fonctionnent sur iPhone seul, et Ecleptic calcule son score sans montre en retirant le pilier des vitaux. Athlytic et le score de préparation d'Apple reposent sur l'Apple Watch."},
        ],
    },
    "en": {
        "title": "Which app connects sleep, nutrition and training on iPhone?",
        "seo_title": "Which iPhone app connects sleep, nutrition and training?",
        "description": "Whoop, Oura, Athlytic, Apple Health, MyFitnessPal, Yazio and Ecleptic: what each app connects across sleep, food and training, based on official pages.",
        "lead": "On iPhone, recovery apps (Whoop, Oura, Athlytic, Apple) start from your sleep and your heart, while food logs (MyFitnessPal, Yazio) start from your plate. To connect the two, some correlate a behavior journal with your recovery; Ecleptic feeds your nutrition into the daily score itself.",
        "body": TRANSPARENCE_EN + """
<h2>"Connecting" can mean three things</h2>
<ul>
<li><strong>Side by side:</strong> seeing your night, your meals and your workouts in the same app.</li>
<li><strong>Correlating:</strong> logging a behavior (alcohol, a late dinner, calories) and seeing, over the weeks, whether it lines up with better or worse recovery.</li>
<li><strong>Integrating:</strong> making food part of the daily score calculation.</li>
</ul>
<p>This is not a ranking: the table shows what each app's official pages describe.</p>

<h2>The feature table</h2>
<div class="tablewrap"><table>
<caption>Features described by each developer (support pages or App Store listing), checked on September 30, 2026. Sources at the bottom of the page.</caption>
<thead><tr><th>App</th><th>Sleep</th><th>Food</th><th>Training</th><th>Daily metric</th><th>Hardware</th><th>Subscription required</th></tr></thead>
<tbody>
<tr><td>Whoop</td><td>Yes</td><td>Journal behaviors; import from other apps via Apple Health</td><td>Strain, detected or imported activities</td><td>Recovery (heart, sleep, temperature, SpO₂)</td><td>WHOOP sensor</td><td>Yes</td></tr>
<tr><td>Oura</td><td>Yes</td><td>Meals: photo or text, AI-assisted analysis (English only)</td><td>Activity, automatic detection</td><td>Readiness Score (9 contributors)</td><td>Oura Ring</td><td>Yes for Meals; daily score visible without</td></tr>
<tr><td>Athlytic</td><td>Yes</td><td>Energy consumed and macros, read from Apple Health</td><td>Exertion, workouts</td><td>Recovery (overnight HRV and resting heart rate)</td><td>iPhone and Apple Watch for most features</td><td>Yes for the full app</td></tr>
<tr><td>Apple Health and Fitness</td><td>Sleep score</td><td>Through other apps, whose data Health brings together</td><td>Activity, training load</td><td>Readiness score (activity, vitals, sleep)</td><td>Apple Watch Series 12 or Ultra 4 for Readiness</td><td>None among the requirements</td></tr>
<tr><td>MyFitnessPal</td><td>Not described in its listing</td><td>Calories and macros; barcode and meal scan with Premium</td><td>Workouts and steps; 40+ devices and apps can connect</td><td>Calorie and macro goals</td><td>iPhone</td><td>No for the log; Premium for scanning</td></tr>
<tr><td>Yazio</td><td>Not described in its listing</td><td>AI-assisted calorie counter, barcode scanner, fasting</td><td>Steps and activity; Fitbit or Garmin sync with Pro</td><td>Calorie goal</td><td>iPhone</td><td>No for the counter; Pro for advanced features</td></tr>
<tr><td>Ecleptic</td><td>Yes</td><td>Photo scan, barcode, search; values from Ciqual, USDA, Open Food Facts</td><td>Workouts, training load</td><td>Readiness Score (vitals, sleep, nutrition, rhythm)</td><td>iPhone; watch optional</td><td>Free iOS beta</td></tr>
</tbody>
</table></div>

<h2>Whoop and Oura: the sensor first</h2>
<p>Whoop and Oura measure your night with their own device. Their daily score rests on your heart, sleep, temperature and, for Oura, activity; food is not among their published signals. Whoop connects it through correlation: its Journal offers nutrition behaviors (calories, protein, carbohydrates, hydration and more), can receive them from other apps via Apple Health, and its Behavior Insights measure their effect on your recovery once you have 5 "yes" and 5 "no" answers within 90 days. Oura offers Meals: you photograph or describe your meal, an AI-assisted analysis rates its protein, fiber, added sugars or processing level (low, moderate, high), and your meals appear on a 24-hour clock next to your sleep and wake times. Meals requires an active membership and is currently available in English only.</p>

<h2>Athlytic and Apple: it all starts with Apple Watch</h2>
<p>With watchOS 27, Apple Watch Series 12 and Ultra 4 already calculate a readiness score combining activity, vitals and sleep, and the Health app brings together data from other apps. Athlytic reads that data from Apple Health: its Recovery compares your overnight HRV and resting heart rate with your baseline, its Journal shows how caffeine, alcohol or travel affect your recovery and sleep, and its trends display energy consumed and burned.</p>

<h2>MyFitnessPal and Yazio: the plate first</h2>
<p>MyFitnessPal describes a calorie and macro log with an AI coach, workout and step logging, and connections to more than 40 devices and apps; barcode and meal scanning are part of Premium. Yazio describes an AI-assisted calorie counter with a barcode scanner, intermittent fasting tracking and built-in step and activity tracking; syncing with Fitbit or Garmin is part of Pro. Neither listing mentions a recovery score or sleep tracking.</p>

<h2>Ecleptic: food inside the daily score</h2>
<p>Ecleptic integrates: your nutrition is worth 21 points out of 100 in your <a href="/methode/readiness-score.html">Readiness Score</a>, alongside overnight vitals (42), sleep (21) and rhythm with training load (16). You photograph your meal (up to 3 photos), scan a barcode or search for a food: the AI recognizes the foods and estimates portions, while the values come from official databases (the ANSES Ciqual table, USDA FoodData Central, Open Food Facts). The pillar looks at how well you hit your <a href="/methode/cibles.html">targets</a>, post-workout protein, micronutrients and hydration, and it is capped at 80 if you drank alcohol the day before. The details: <a href="/methode/nutrition.html">the nutrition method</a>.</p>

<h2>How to choose based on what you already have</h2>
<ul>
<li><strong>An Apple Watch Series 12 or Ultra 4:</strong> the readiness score is already on your watch; an app that reads Apple Health can add a journal or your meals.</li>
<li><strong>A Whoop:</strong> check that your food app writes to Apple Health, which is where Whoop imports nutrition into its Journal from.</li>
<li><strong>Counting calories above all:</strong> that is the core of MyFitnessPal and Yazio.</li>
<li><strong>Wanting your meals to count in your morning score:</strong> that is how Ecleptic works.</li>
</ul>
<p>Either way, Apple Health is where you choose, category by category, what each app can read.</p>
""",
        "faq": [
            {"q": "Which iPhone app connects nutrition with recovery?",
             "a": "Among the apps compared: Whoop correlates the behaviors in its Journal, nutrition included, with your recovery; Athlytic shows how its Journal entries affect its Recovery; Ecleptic builds nutrition directly into its Readiness Score, for 21 points out of 100."},
            {"q": "Do MyFitnessPal or Yazio calculate a recovery score?",
             "a": "Their App Store listings describe tracking calories, macros, activity and steps, but mention neither a recovery score nor sleep tracking. To cross that data with your night, another app has to read it."},
            {"q": "Do you need an Apple Watch to connect sleep, nutrition and training?",
             "a": "Not necessarily. Whoop and Oura use their own sensor, MyFitnessPal and Yazio work on iPhone alone, and Ecleptic calculates its score without a watch by removing the vitals pillar. Athlytic and Apple's readiness score rely on Apple Watch."},
        ],
    },
    "sources": [
        {"t": "WHOOP. WHOOP Recovery (support, publié le 11 septembre 2025). Consulté le 30 septembre 2026.",
         "u": "https://support.whoop.com/s/article/WHOOP-Recovery?language=en_US"},
        {"t": "WHOOP. WHOOP Journal Overview (support, publié le 18 septembre 2026). Consulté le 30 septembre 2026.",
         "u": "https://support.whoop.com/s/article/WHOOP-Journal-Overview?language=en_US"},
        {"t": "WHOOP. Apple Health Integration (support, publié le 16 avril 2026). Consulté le 30 septembre 2026.",
         "u": "https://support.whoop.com/s/article/Apple-Health-Integration?language=en_US"},
        {"t": "WHOOP. Membership Pricing (support, publié le 28 mai 2026). Consulté le 30 septembre 2026.",
         "u": "https://support.whoop.com/s/article/Membership-Pricing?language=en_US"},
        {"t": "WHOOP for Developers. WHOOP 101. Consulté le 30 septembre 2026.",
         "u": "https://developer.whoop.com/docs/whoop-101/"},
        {"t": "Oura. Readiness Contributors (Member Care, mis à jour le 14 juillet 2026). Consulté le 30 septembre 2026.",
         "u": "https://support.ouraring.com/hc/en-us/articles/360057791533-Readiness-Contributors"},
        {"t": "Oura. Meals (Member Care, mis à jour le 5 août 2026). Consulté le 30 septembre 2026.",
         "u": "https://support.ouraring.com/hc/en-us/articles/40264659421843-Meals"},
        {"t": "Oura. Oura Membership (Member Care, mis à jour le 8 septembre 2026). Consulté le 30 septembre 2026.",
         "u": "https://support.ouraring.com/hc/en-us/articles/4409086524819-Oura-Membership"},
        {"t": "MyndArc. Athlytic: Fitness & Recovery, fiche App Store (États-Unis). Consulté le 30 septembre 2026.",
         "u": "https://apps.apple.com/us/app/athlytic-fitness-recovery/id1543571755"},
        {"t": "Athlytic. Site officiel. Consulté le 30 septembre 2026.",
         "u": "https://athlyticapp.com/"},
        {"t": "Apple. Understand your readiness score on Apple Watch (publié le 14 septembre 2026). Consulté le 30 septembre 2026.",
         "u": "https://support.apple.com/en-us/128112"},
        {"t": "Apple. Guide d'utilisation de l'Apple Watch : Use the Readiness app on Apple Watch (watchOS 27). Consulté le 30 septembre 2026.",
         "u": "https://support.apple.com/guide/watch/readiness-flx4gnzby346/watchos"},
        {"t": "Apple. Guide d'utilisation de l'Apple Watch : View your sleep score on Apple Watch. Consulté le 30 septembre 2026.",
         "u": "https://support.apple.com/guide/watch/view-your-sleep-score-apded441a669/watchos"},
        {"t": "Apple. Guide d'utilisation de l'Apple Watch : Track your training load. Consulté le 30 septembre 2026.",
         "u": "https://support.apple.com/guide/watch/track-your-training-load-apde4c07a6cf/watchos"},
        {"t": "Apple. Guide d'utilisation de l'iPhone : Intro to Health data on iPhone. Consulté le 30 septembre 2026.",
         "u": "https://support.apple.com/guide/iphone/intro-to-health-data-iphbb8259c61/ios"},
        {"t": "MyFitnessPal, Inc. MyFitnessPal: Calorie Counter, fiche App Store (États-Unis). Consulté le 30 septembre 2026.",
         "u": "https://apps.apple.com/us/app/myfitnesspal-calorie-counter/id341232718"},
        {"t": "YAZIO GmbH. AI Calorie Tracker by Yazio, fiche App Store (États-Unis). Consulté le 30 septembre 2026.",
         "u": "https://apps.apple.com/us/app/ai-calorie-tracker-by-yazio/id946099227"},
    ],
}


# ---------------------------------------------------------------------------
# 3. Âge biologique, âge cardio, âge de forme
# ---------------------------------------------------------------------------
P_AGE = {
    "key": "age-biologique",
    "slug_fr": "age-biologique-application-whoop-garmin-oura",
    "slug_en": "biological-age-app-whoop-garmin-oura",
    "date": "2026-09-30",
    "fr": {
        "title": "Âge biologique, âge cardio, âge de forme : comment les apps le calculent",
        "seo_title": "Âge biologique : comment Whoop, Garmin et Oura le calculent",
        "description": "Âge physique Garmin, WHOOP Age, âge cardiovasculaire Oura, VO₂max Apple, âge biologique Ecleptic : ce que chaque app estime et avec quelles données.",
        "lead": "Derrière le mot « âge », ces apps n'estiment pas la même chose : Garmin tire un âge physique de ton IMC, de ta fréquence au repos et de ton activité soutenue ; Whoop combine neuf indicateurs sur six mois ; Oura estime l'âge de ton système cardiovasculaire d'après ton pouls ; Apple classe ta VO₂max selon ton âge et ton sexe ; Ecleptic part de ta VO₂max et l'ajuste avec sept facteurs du quotidien.",
        "body": TRANSPARENCE_FR + """
<h2>Trois familles d'« âges »</h2>
<p>L'<strong>âge de forme</strong> traduit ta condition physique en années : c'est l'idée de l'âge physique de Garmin, et le point de départ d'Ecleptic avec la VO₂max. L'<strong>âge cardiovasculaire</strong> estime l'état de ton système cardiovasculaire à partir de ton pouls : c'est l'approche d'Oura. L'<strong>âge physiologique global</strong> réunit plusieurs indicateurs de sommeil, d'activité et de forme, comme le WHOOP Age.</p>

<h2>Le tableau comparatif</h2>
<div class="tablewrap"><table>
<caption>Informations publiées par chaque marque, vérifiées le 30 septembre 2026. Sources en bas de page.</caption>
<thead><tr><th>Marque</th><th>Nom</th><th>Ce qui est estimé</th><th>Données utilisées</th><th>Délai</th><th>Matériel</th><th>Abonnement requis</th></tr></thead>
<tbody>
<tr><td>Garmin</td><td>Âge physique</td><td>Ta forme face à une personne du même sexe</td><td>Âge, IMC ou masse grasse, FC au repos, activités soutenues</td><td>Non précisé</td><td>Montre Garmin compatible</td><td>Non, affiché sur la montre</td></tr>
<tr><td>Whoop</td><td>WHOOP Age</td><td>Âge physiologique</td><td>9 indicateurs de sommeil, d'activité et de forme ; pas la HRV</td><td>21 Recovery sur 31 jours</td><td>Capteur WHOOP</td><td>Oui, formule Peak ou Life</td></tr>
<tr><td>Oura</td><td>Âge cardiovasculaire</td><td>Ton système cardiovasculaire</td><td>Onde de pouls estimée par capteur optique</td><td>14 nuits sur 30 jours</td><td>Bague Gen3 ou plus récente</td><td>Oui</td></tr>
<tr><td>Apple</td><td>Santé cardiovasculaire</td><td>Ta VO₂max, par âge et sexe</td><td>Effort cardiaque en extérieur, profil, traitements</td><td>Plusieurs séances en extérieur</td><td>Apple Watch</td><td>Aucun dans les prérequis</td></tr>
<tr><td>Athlytic</td><td>Athlytic Age</td><td>Un âge de forme</td><td>FC au repos, VO₂max, sommeil, composition corporelle, pas, entraînement</td><td>Non précisé</td><td>iPhone et Apple Watch</td><td>Oui pour l'app complète</td></tr>
<tr><td>Ecleptic</td><td>Âge biologique</td><td>L'âge de ton corps</td><td>VO₂max, puis 7 facteurs du quotidien</td><td>Dès l'inscription</td><td>iPhone ; montre facultative</td><td>Bêta iOS gratuite</td></tr>
</tbody>
</table></div>

<h2>Garmin : l'âge physique</h2>
<p>Garmin présente l'âge physique (Fitness Age) comme une façon de comparer ta condition physique à celle d'une personne du même sexe. La montre s'appuie sur ton âge, ton indice de masse corporelle, ta fréquence cardiaque au repos et ton historique d'activités soutenues ; avec une balance Index, le taux de graisse corporelle remplace l'IMC. Un profil utilisateur complet le rend plus précis.</p>

<h2>Whoop : WHOOP Age et Pace of Aging</h2>
<p>Dans sa fonction Healthspan, Whoop calcule le WHOOP Age, un âge physiologique moyenné sur six mois à partir de neuf indicateurs : heures et régularité du sommeil ; temps hebdomadaire en zones cardiaques 1 à 3 et 4 à 5, temps de musculation, pas quotidiens ; fréquence au repos, VO₂max et, si elle est connue, masse maigre. Le Pace of Aging, lui, lit tes 30 derniers jours pour dire si cet âge tend à monter ou à descendre. La HRV n'y entre pas, jugée trop individuelle pour une comparaison par âge. La fonction se débloque après 21 Recovery sur tes 31 premiers jours, se calibre en 90 jours et demande 18 ans et une formule Peak ou Life.</p>

<h2>Oura : l'âge cardiovasculaire</h2>
<p>L'âge cardiovasculaire d'Oura estime la santé de ton système cardiovasculaire par rapport à ton âge réel. La bague ne mesure pas directement la vitesse de l'onde de pouls : elle l'estime, avec les changements de forme du pouls liés à l'âge, grâce à son capteur optique. Après 14 nuits sur 30 jours, le résultat est classé en dessous, aligné (jusqu'à 5 ans d'écart) ou au-dessus de ton âge. Oura estime à part une capacité cardio, sa VO₂max ajustée à l'âge. Les deux demandent un abonnement actif.</p>

<h2>Apple : ta VO₂max par âge, et un Health Age annoncé</h2>
<p>L'Apple Watch estime ta VO₂max, appelée santé cardiovasculaire, pendant une marche, une course ou une randonnée en extérieur, en tenant compte de ton âge, de ton sexe, de ton poids, de ta taille et de certains traitements. L'app Santé l'affiche en VO₂max et la situe face aux niveaux de ton âge et de ton sexe. Le 9 septembre 2026, Apple a annoncé Health Age, qui situera ta VO₂max, ta fréquence au repos, ton sommeil et ta HRV face à ton âge réel, dans une app Santé attendue plus tard dans l'année, d'abord en anglais aux États-Unis.</p>

<h2>Ecleptic : un âge ancré sur ta VO₂max</h2>
<p>Notre âge biologique se calcule en deux temps. D'abord, ta <a href="/methode/vo2max.html">VO₂max</a> vient de la meilleure source disponible : ta montre via Apple Santé, tes courses (formule VDOT, qui ne peut que relever l'estimation), ou une estimation sans effort par l'équation de Nes et al., issue de la cohorte norvégienne HUNT. Comparée à la référence pour ton âge et ton sexe, elle devient un âge de forme. Ensuite, sept facteurs bornés et signés l'ajustent : variabilité cardiaque, fréquence au repos, tour de taille, activité, sommeil, alimentation et hygiène de vie, ce dernier ne pouvant jamais te rajeunir. Aucune donnée n'est comptée deux fois ; le résultat est lissé et accompagné d'une marge d'incertitude. La méthode : <a href="/methode/age-biologique.html">l'âge biologique</a>.</p>

<h2>Ce que ces chiffres ne sont pas</h2>
<p>Aucun n'est un diagnostic. Whoop précise qu'il n'existe pas de référence clinique pour valider son WHOOP Age ; Oura, que sa bague n'est pas un dispositif médical ; Ecleptic, que son âge biologique est une estimation, pas une prédiction de ta durée de vie. Tous trois les décrivent comme des indicateurs lents : c'est la tendance sur des semaines ou des mois qui compte.</p>

<h2>Ce qui fait bouger ces âges</h2>
<p>Les leviers se recoupent : la VO₂max entre dans le WHOOP Age, l'Athlytic Age, le Health Age d'Apple et l'âge biologique d'Ecleptic ; la fréquence au repos, dans ceux de Garmin, Whoop, Athlytic et Ecleptic. Pour agir : <a href="/articles/zone-2-cardio-cest-quoi.html">l'endurance en zone 2</a> et <a href="/articles/se-coucher-meme-heure-regularite.html">des horaires de coucher réguliers</a>.</p>
""",
        "faq": [
            {"q": "Comment Garmin calcule-t-il l'âge physique ?",
             "a": "À partir de ton âge, de ton indice de masse corporelle, de ta fréquence cardiaque au repos et de ton historique d'activités soutenues ; avec une balance Index, le taux de graisse corporelle remplace l'IMC. Le résultat compare ta condition physique à celle d'une personne du même sexe."},
            {"q": "Le WHOOP Age tient-il compte de la HRV ?",
             "a": "Non. Whoop juge la HRV trop individuelle pour une comparaison par âge et retient la fréquence cardiaque au repos, avec huit autres indicateurs de sommeil, d'activité et de forme, moyennés sur six mois."},
            {"q": "Quelle différence entre âge biologique et âge cardiovasculaire ?",
             "a": "L'âge cardiovasculaire d'Oura estime l'état de ton système cardiovasculaire à partir du signal de ton pouls. L'âge biologique d'Ecleptic part de ta forme cardiorespiratoire, la VO₂max, puis l'ajuste avec tes habitudes : sommeil, activité, alimentation, hygiène de vie."},
        ],
    },
    "en": {
        "title": "Biological age, heart age, fitness age: how apps calculate it",
        "seo_title": "Biological age: how Whoop, Garmin and Oura calculate it",
        "description": "Garmin Fitness Age, WHOOP Age, Oura Cardiovascular Age, Apple cardio fitness and Ecleptic's biological age: what each app estimates and from which data.",
        "lead": "Behind the word \"age\", these apps do not estimate the same thing: Garmin derives a fitness age from your BMI, resting heart rate and vigorous activity; Whoop combines nine metrics over six months; Oura estimates the age of your cardiovascular system from your pulse; Apple ranks your VO₂ max by age and sex; Ecleptic starts from your VO₂ max and adjusts it with seven everyday factors.",
        "body": TRANSPARENCE_EN + """
<h2>Three families of "ages"</h2>
<p><strong>Fitness age</strong> turns your physical fitness into years: that is the idea behind Garmin's Fitness Age, and Ecleptic's starting point with VO₂ max. <strong>Cardiovascular age</strong> estimates the state of your cardiovascular system from your pulse: that is Oura's approach. <strong>Overall physiological age</strong> combines several sleep, activity and fitness metrics, like WHOOP Age.</p>

<h2>The comparison table</h2>
<div class="tablewrap"><table>
<caption>Information published by each brand, checked on September 30, 2026. Sources at the bottom of the page.</caption>
<thead><tr><th>Brand</th><th>Name</th><th>What it estimates</th><th>Data used</th><th>Lead time</th><th>Hardware</th><th>Subscription required</th></tr></thead>
<tbody>
<tr><td>Garmin</td><td>Fitness Age</td><td>Your fitness vs. a person of the same sex</td><td>Age, BMI or body fat, resting heart rate, vigorous activity</td><td>Not specified</td><td>Compatible Garmin watch</td><td>No, shown on the watch</td></tr>
<tr><td>Whoop</td><td>WHOOP Age</td><td>Physiological age</td><td>9 sleep, activity and fitness metrics; not HRV</td><td>21 recoveries in 31 days</td><td>WHOOP sensor</td><td>Yes, Peak or Life plan</td></tr>
<tr><td>Oura</td><td>Cardiovascular Age</td><td>Your cardiovascular system</td><td>Pulse wave estimated by the optical sensor</td><td>14 nights in 30 days</td><td>Gen3 ring or later</td><td>Yes</td></tr>
<tr><td>Apple</td><td>Cardio Fitness</td><td>Your VO₂ max, by age and sex</td><td>Heart effort outdoors, profile, medications</td><td>Several outdoor workouts</td><td>Apple Watch</td><td>None among the requirements</td></tr>
<tr><td>Athlytic</td><td>Athlytic Age</td><td>A fitness age</td><td>Resting heart rate, VO₂ max, sleep, body composition, steps, training</td><td>Not specified</td><td>iPhone and Apple Watch</td><td>Yes for the full app</td></tr>
<tr><td>Ecleptic</td><td>Biological age</td><td>Your body's age</td><td>VO₂ max, then 7 everyday factors</td><td>From sign-up</td><td>iPhone; watch optional</td><td>Free iOS beta</td></tr>
</tbody>
</table></div>

<h2>Garmin: Fitness Age</h2>
<p>Garmin presents Fitness Age as a way to compare your fitness with that of a person of the same sex. The watch uses your age, body mass index, resting heart rate and vigorous activity history; with an Index scale, body fat percentage replaces BMI. A complete user profile makes it more accurate.</p>

<h2>Whoop: WHOOP Age and Pace of Aging</h2>
<p>Within its Healthspan feature, Whoop calculates WHOOP Age, a physiological age averaged over six months from nine metrics: hours of sleep and sleep consistency; weekly time in heart rate zones 1-3 and 4-5, strength training time, daily steps; resting heart rate, VO₂ max and, when available, lean body mass. Pace of Aging reads your last 30 days to show whether that age is likely to rise or fall. HRV is left out, considered too individual for age-based comparison. The feature unlocks after 21 recoveries in your first 31 days, calibrates over 90 days and requires being 18 or older and a Peak or Life plan.</p>

<h2>Oura: Cardiovascular Age</h2>
<p>Oura's Cardiovascular Age estimates the health of your cardiovascular system relative to your actual age. The ring does not measure pulse wave velocity directly: it estimates it, along with age-related changes in the shape of your pulse, from its optical sensor. After 14 nights within 30 days, the result is rated below, aligned with (within 5 years) or above your age. Separately, Oura estimates Cardio Capacity, its age-adjusted VO₂ max. Both require an active membership.</p>

<h2>Apple: VO₂ max by age, and an announced Health Age</h2>
<p>Apple Watch estimates your VO₂ max, called cardio fitness, during an outdoor walk, run or hike, taking into account your age, sex, weight, height and certain medications. The Health app shows it as a VO₂ max value and places it against the levels for your age and sex. On September 9, 2026, Apple announced Health Age, which will place your VO₂ max, resting heart rate, sleep and HRV against your chronological age, in a redesigned Health app due later this year, starting in U.S. English.</p>

<h2>Ecleptic: an age anchored on your VO₂ max</h2>
<p>Our biological age is calculated in two steps. First, your <a href="/methode/vo2max.html">VO₂ max</a> comes from the best available source: your watch via Apple Health, your runs (the VDOT formula, which can only raise the estimate), or a no-exercise estimate using the Nes et al. equation from Norway's HUNT cohort. Compared with the reference for your age and sex, it becomes a fitness age. Then seven bounded, signed factors adjust it: heart rate variability, resting heart rate, waist size, activity, sleep, diet and lifestyle, the last of which can never make you younger. No data point is counted twice; the result is smoothed and comes with an uncertainty margin. The method: <a href="/methode/age-biologique.html">biological age</a>.</p>

<h2>What these numbers are not</h2>
<p>None of them is a diagnosis. Whoop states that there is no clinical benchmark for validating WHOOP Age; Oura, that its ring is not a medical device; Ecleptic, that its biological age is an estimate, not a prediction of your lifespan. All three describe these as slow-moving metrics: the trend over weeks or months is what counts.</p>

<h2>What moves these ages</h2>
<p>The levers overlap: VO₂ max feeds WHOOP Age, Athlytic Age, Apple's Health Age and Ecleptic's biological age; resting heart rate feeds Garmin's, Whoop's, Athlytic's and Ecleptic's. To act on them: <a href="/articles/zone-2-cardio-cest-quoi.html">zone 2 endurance</a> and <a href="/articles/se-coucher-meme-heure-regularite.html">regular bedtimes</a>.</p>
""",
        "faq": [
            {"q": "How does Garmin calculate Fitness Age?",
             "a": "From your age, body mass index, resting heart rate and vigorous activity history; with an Index scale, body fat percentage replaces BMI. The result compares your fitness with that of a person of the same sex."},
            {"q": "Does WHOOP Age take HRV into account?",
             "a": "No. Whoop explains that HRV is too individual to compare against age-based benchmarks, and uses resting heart rate instead, alongside eight other sleep, activity and fitness metrics averaged over six months."},
            {"q": "What is the difference between biological age and cardiovascular age?",
             "a": "Oura's Cardiovascular Age estimates the state of your cardiovascular system from your pulse signal. Ecleptic's biological age starts from your cardiorespiratory fitness, VO₂ max, then adjusts it for your habits: sleep, activity, diet and lifestyle."},
        ],
    },
    "sources": [
        {"t": "Garmin. Manuel d'utilisation Venu X1 : Viewing Your Fitness Age (septembre 2026). Consulté le 30 septembre 2026.",
         "u": "https://www8.garmin.com/manuals/webhelp/GUID-C144B465-A0C8-4FE9-AFE6-41A3FE3F1D9A/EN-US/GUID-A52C695F-A924-4421-B2F9-49C8BDEF65AE.html"},
        {"t": "Garmin. Manuel d'utilisation Venu X1 : Affichage de l'âge physique (version française). Consulté le 30 septembre 2026.",
         "u": "https://www8.garmin.com/manuals/webhelp/GUID-C144B465-A0C8-4FE9-AFE6-41A3FE3F1D9A/FR-FR/GUID-A52C695F-A924-4421-B2F9-49C8BDEF65AE.html"},
        {"t": "WHOOP. Healthspan: WHOOP Age & Pace of Aging Guide (support, publié le 21 avril 2026). Consulté le 30 septembre 2026.",
         "u": "https://support.whoop.com/s/article/Healthspan-WHOOP-Age-Pace-of-Aging-Guide?language=en_US"},
        {"t": "WHOOP. Membership Pricing (support, publié le 28 mai 2026). Consulté le 30 septembre 2026.",
         "u": "https://support.whoop.com/s/article/Membership-Pricing?language=en_US"},
        {"t": "Oura. Cardiovascular Age (Member Care, mis à jour le 29 mai 2026). Consulté le 30 septembre 2026.",
         "u": "https://support.ouraring.com/hc/en-us/articles/28451491040019-Cardiovascular-Age"},
        {"t": "Oura. L'âge cardiovasculaire (Member Care, version française). Consulté le 30 septembre 2026.",
         "u": "https://support.ouraring.com/hc/fr/articles/28451491040019-L-%C3%A2ge-cardiovasculaire"},
        {"t": "Oura. Cardio Capacity (VO2 Max) (Member Care, mis à jour le 29 mai 2026). Consulté le 30 septembre 2026.",
         "u": "https://support.ouraring.com/hc/en-us/articles/28336620578835-Cardio-Capacity-VO2-Max"},
        {"t": "Apple. Track your cardio fitness levels (publié le 14 septembre 2026). Consulté le 30 septembre 2026.",
         "u": "https://support.apple.com/en-us/108790"},
        {"t": "Apple. Suivre vos niveaux de santé cardiovasculaire (version française). Consulté le 30 septembre 2026.",
         "u": "https://support.apple.com/fr-fr/108790"},
        {"t": "Apple Newsroom. Apple advances health and fitness capabilities using Apple Intelligence (9 septembre 2026). Consulté le 30 septembre 2026.",
         "u": "https://www.apple.com/newsroom/2026/09/apple-advances-health-and-fitness-capabilities-using-apple-intelligence/"},
        {"t": "MyndArc. Athlytic: Fitness & Recovery, fiche App Store (États-Unis). Consulté le 30 septembre 2026.",
         "u": "https://apps.apple.com/us/app/athlytic-fitness-recovery/id1543571755"},
    ],
}


PAGES = [P_RECUPERATION, P_APPS, P_AGE]
