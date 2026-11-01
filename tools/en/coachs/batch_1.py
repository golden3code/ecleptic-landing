# -*- coding: utf-8 -*-
# English adaptation of the coach guides for an international reader.
# Source: tools/coachs/batch_d.py and tools/coachs/batch_e.py.
# France-only rules removed (tools/en/_brief-coachs.md). The PAR-Q+ is never reproduced.

ENTRIES = [
    {
        "fr": "fiche-client-coach-sportif",
        "slug": "client-intake-form-personal-trainer",
        "title": "Client intake form for personal trainers: what to include",
        "description": "Client intake form for personal trainers: the sections to include, what counts as health data, what to avoid writing and how long to keep your records.",
        "body": """
<p>The short answer: a <strong>client intake form for personal trainers</strong> fits into seven sections: contact, setup, goal, training background, health, measurements and follow-up. As soon as it holds an injury, a medical history or the answers to a questionnaire, it holds health data, and if you work in the EU or the UK, health data is specially protected. Record only what you need, get the client's consent and keep the health section separate.</p>

<h2>What should a client intake form include?</h2>
<p>Here is an example structure. The last column shows how to treat each section, because whether something counts as health data is judged case by case.</p>
<div class="tablewrap"><table>
<caption>Sections suggested as an example, with a cautious reading of the GDPR.</caption>
<thead><tr><th>Section</th><th>What you record</th><th>Type of data</th></tr></thead>
<tbody>
<tr><td>Contact</td><td>Name, email, phone, emergency contact</td><td>Ordinary personal data</td></tr>
<tr><td>Setup</td><td>Time slots, location, equipment, package, start date</td><td>Ordinary personal data</td></tr>
<tr><td>Goal</td><td>The client's own words, deadline, motivation</td><td>Ordinary, unless it reveals a health condition</td></tr>
<tr><td>Training background</td><td>Current activity, sports history, preferences, target intensity</td><td>Ordinary, check case by case</td></tr>
<tr><td>Health</td><td>Questionnaire answers, reported discomfort, medical advice requested</td><td>Health data</td></tr>
<tr><td>Measurements</td><td>Weight, waist, heart rate, sleep</td><td>Treat as health data</td></tr>
<tr><td>Follow-up</td><td>Tests, sessions, loads, how the client felt, decisions made</td><td>Sensitive once combined with measurements</td></tr>
</tbody>
</table></div>
<p>Keep the client's exact words for the goal. "Get up to my apartment without stopping at the second floor" will serve you better than "cardio" when you choose a test or measure progress.</p>

<h2>What counts as health data on a client form?</h2>
<p>Health data covers physical or mental health, past, present or future. Medical history, illnesses, treatments and disabilities count by nature. An injury tells you about physical health too, so file it with the rest. Treat the answers to a <a href="/coachs/questionnaire-sante-avant-le-sport-client.html">health questionnaire</a> the same way.</p>
<p>Weight depends on context. A high weight can reveal obesity, and weight combined with step counts or calorie intake becomes health data. Heart rate, weight and height can also be sensitive, especially when they come from a connected device. I found no written classification of sleep data, so treat it as health data to be safe. Your form brings all these measurements together in one place: apply the most protective rule to the whole thing.</p>
<p>To keep this data, ask for the client's explicit consent, separate from your terms and conditions, after telling them what you collect and why. Check the rules where you work: data protection, qualification, insurance and consumer law vary by country.</p>

<h2>What should you avoid writing in client notes?</h2>
<ul>
<li><strong>A diagnosis.</strong> Write, for example, "right knee hurts on stairs, reported January 12, referred to a doctor." Don't add a condition name of your own. You don't interpret a client's health data: as soon as a sign raises a question, you refer them to a doctor.</li>
<li><strong>Medical detail you don't need.</strong> You need to know that medical advice exists and what limits it sets. A copy of a prescription or a medical report has no place in your file.</li>
<li><strong>A judgment about the person.</strong> A client can ask to see their data, and in the EU and the UK you generally have one month to reply, unless an extension is justified. Write every line as if they were going to read it.</li>
<li><strong>Anything that changes nothing in your session.</strong> For each field, ask what you would do differently with that information. If you have no answer, delete the field.</li>
</ul>

<h2>How long should you keep client records, and where?</h2>
<p>Set your own retention period, tell the client what it is and delete the health section once you no longer need it, normally at the end of coaching. Invoices follow separate accounting rules. So keep the admin file apart from the training file, and you can erase one without touching the other.</p>
<p>If you work in the EU or the UK, working alone doesn't exempt you from keeping a record of how you handle client data: regular tracking and health data both count.</p>
<p>For storage, health data needs security that matches its sensitivity, and a WhatsApp thread or an unprotected file is a poor fit.</p>

<h2>How do you keep a client form up to date?</h2>
<p>Open it at the <a href="/coachs/bilan-forme-premier-rendez-vous.html">first fitness assessment</a>, then add three things after each session: what was done, how the client felt, what you will change next time. Also record the results of <a href="/coachs/tests-physiques-nouveau-client.html">fitness tests</a> along with the conditions they were done in.</p>
<p>Show these numbers to the client. A meta-analysis of 138 trials and 19,951 people (Harkin, 2016) indicates that tracking progress helps people reach their goals, with a stronger effect when the outcome is physically recorded or made public. It doesn't cover only exercise, so treat it as a guide.</p>
<p>Reread the health section whenever the situation changes. New pain sends you back to the same rule: you note it, you don't interpret it, you refer.</p>
<p>This guide is for information only and doesn't replace advice from a lawyer or a data protection officer.</p>

<h2>Key takeaways</h2>
<ul>
<li>Seven sections are enough, and every field should change something in your session.</li>
<li>Injuries, medical history and questionnaire answers are health data. Treat weight and sleep the same way, to be safe.</li>
<li>Record facts without interpreting them, keep health and billing apart, and set a retention period.</li>
</ul>
""",
        "faq": [
            {"q": "How do you create a client intake form as a personal trainer?", "a": "Plan seven sections: contact, setup, goal, training background, health, measurements and follow-up. Record only what you need and keep the health section separate, because in the EU and the UK it falls under the GDPR. A protected spreadsheet or software both work, as long as access is secure."},
            {"q": "Does a client intake form contain health data?", "a": "Almost always. Injuries, medical history and questionnaire answers are health data. Weight and sleep can be too, especially combined with other measurements. If in doubt, treat them that way and ask for explicit consent, separate from your terms and conditions."},
            {"q": "How long should a personal trainer keep client records?", "a": "Set your own period, tell the client what it is and delete the health section once you no longer need it, normally at the end of coaching. Invoices follow separate accounting rules, which vary by country."},
        ],
        "sources": [
            {"t": "CNIL, France's data protection authority. Qu'est-ce qu'une donnée de santé ? 2018 (in French).", "u": "https://www.cnil.fr/fr/quest-ce-ce-quune-donnee-de-sante"},
            {"t": "CNIL. Questions-réponses sur la protection des données dans le secteur du sport amateur (hors contrat). 2022 (in French).", "u": "https://www.cnil.fr/fr/sport-amateur-hors-contrat/questions-reponses"},
            {"t": "CNIL. Le registre des activités de traitement. 2018 (in French).", "u": "https://www.cnil.fr/fr/RGPD-le-registre-des-activites-de-traitement"},
            {"t": "CNIL. Professionnels : comment répondre à une demande de droit d'accès ? 2017 (in French).", "u": "https://www.cnil.fr/fr/professionnels-comment-repondre-une-demande-de-droit-dacces"},
            {"t": "Harkin B, Webb TL, Chang BP, et al. Does monitoring goal progress promote goal attainment? A meta-analysis of the experimental evidence. <em>Psychol Bull</em>. 2016.", "u": "https://doi.org/10.1037/bul0000025"},
        ],
    },
    {
        "fr": "bilan-forme-premier-rendez-vous",
        "slug": "first-session-fitness-assessment",
        "title": "First session fitness assessment: how to run it with a new client",
        "seo_title": "First session fitness assessment: how to run it",
        "description": "First session fitness assessment for personal trainers: how to prepare, which questions to ask, what to do about a health flag and how to end the meeting.",
        "body": """
<p>The short answer: a good <strong>first session fitness assessment</strong> follows four steps: listen to the goal, spot anything that needs medical advice, measure a simple starting point, then propose a clear plan. I found no standard that sets its content or length. It helps you decide whether you can start, at what intensity and in what direction. You make no diagnosis.</p>

<h2>What should you prepare before a first session?</h2>
<p>Three things sent ahead keep you from losing half the meeting:</p>
<ul>
<li><strong>The <a href="/coachs/questionnaire-sante-avant-le-sport-client.html">health questionnaire</a></strong>, to fill in before coming, with an explanation of what you do with the data and a request for consent.</li>
<li><strong>Practical details:</strong> location, clothing, water, how long it will last.</li>
<li><strong>The status of the meeting:</strong> free or paid, you say so up front. The guide on <a href="/coachs/seance-essai-coach-sportif.html">trial sessions</a> covers that question.</li>
</ul>
<p>Call it a fitness assessment, never a health check: that phrase sets up an expectation you can't meet.</p>

<h2>How do you run a fitness assessment in one hour?</h2>
<p>I found no recommendation that sets a length. Here is an example 60-minute breakdown, to adapt:</p>
<ol>
<li><strong>5 minutes, the setup.</strong> You explain what will happen and what the client will leave with.</li>
<li><strong>20 minutes, listening.</strong> Goal, training history, constraints, preferences.</li>
<li><strong>5 minutes, safety.</strong> You go through the questionnaire together.</li>
<li><strong>20 minutes, movement.</strong> Two or three simple tests, with a warm-up if the protocol calls for one.</li>
<li><strong>10 minutes, next steps.</strong> You sum up and make your proposal.</li>
</ol>
<p><a href="/coachs/tests-physiques-nouveau-client.html">Fitness tests</a> set a starting point. They wait if the questionnaire or the conversation raises a health question. At a first session, leave a margin: nothing maximal with someone you're just meeting, and no test that belongs to a doctor. The French National Authority for Health (HAS) notes that exercise stress testing with gas analysis takes place in specialized facilities, with trained physicians.</p>

<h2>What questions should you ask a new client?</h2>
<p>Open questions, and a client who talks more than you do:</p>
<ul>
<li><strong>"What brings you here now?"</strong> The reason for the timing often says more than the stated goal.</li>
<li><strong>"How will you know it has worked?"</strong> You get a concrete criterion, in their words.</li>
<li><strong>"What have you tried before, and what made you stop?"</strong> You spot the obstacles before they come back.</li>
<li><strong>"How many sessions really fit into your week?"</strong> The program is built on that answer.</li>
<li><strong>"What do you enjoy doing, and what will you refuse to do?"</strong> The client keeps control over some of the choices.</li>
</ul>
<p>That last point matters. A review of 66 studies (Teixeira, 2012) shows a consistent link between autonomous forms of motivation and exercise, and intrinsic motivation better predicts long-term adherence. Most of those studies are descriptive: they establish a link, not a cause. The HAS guide points the same way for the motivational interview: identify obstacles and set realistic goals with the person.</p>

<h2>What should you do if a client reports a health problem?</h2>
<p>Since 2015, screening by the American College of Sports Medicine (ACSM) has rested on three factors: current activity, signs or known cardiovascular, metabolic or renal disease, and target intensity. That update answered an excess: too many needless referrals to doctors, which can discourage people from moving. The WHO also considers prior medical clearance generally unnecessary, absent a contraindication, for light to moderate activity that goes no further than brisk walking.</p>
<p>HAS gives the course of action when there is doubt:</p>
<ul>
<li><strong>A positive answer on the questionnaire:</strong> medical advice is recommended before starting.</li>
<li><strong>Signs suggesting a disease:</strong> the person holds off on activity, whatever the intensity, and sees their doctor.</li>
<li><strong>Age 45 or older, no regular intense exercise, and a plan close to maximum effort:</strong> medical advice is advised.</li>
</ul>
<p>In all three cases, you interpret nothing. You repeat back what you heard, explain that the decision belongs to a doctor, note the date and postpone the movement part. If a client has chest pain or a fainting spell in front of you, call your local emergency number (911 in the US, 999 or 112 in the UK and Europe). Diagnosis is a doctor's job, so a line like "it's probably your blood pressure" has no place in an assessment.</p>

<h2>How should you end a fitness assessment?</h2>
<p>Sum up in three sentences what you understood, what you measured and what you propose. Then give a dated goal, the session rhythm and the date of the next check-in. Put the terms and the price in writing before any commitment.</p>
<p>Don't promise a numeric result, because you can neither guarantee nor prove it. Say what you will measure, and when. Check the rules where you work: qualification, insurance and consumer law vary by country. That same evening, copy the essentials into the <a href="/coachs/fiche-client-coach-sportif.html">client intake form</a>, while the client's exact words are fresh.</p>

<h2>Key takeaways</h2>
<ul>
<li>Send the questionnaire before the session and make listening the longest part.</li>
<li>At the slightest health flag, postpone the movement and refer to a doctor, without interpreting.</li>
<li>End with a dated goal and written terms, with no promised result.</li>
</ul>
""",
        "faq": [
            {"q": "What happens in a fitness assessment with a personal trainer?", "a": "The coach listens to the goal and the training history, goes through the health questionnaire, runs two or three simple tests if nothing stands in the way, then proposes a plan. This meeting assesses fitness. It doesn't replace a medical consultation."},
            {"q": "How long does a fitness assessment take?", "a": "I found no recommendation that sets a length. One hour is a practical format: a third for listening, a third for movement, the rest for setup, safety and next steps. Adapt it to the client and the tests you plan."},
            {"q": "What should you ask a client at a first session?", "a": "What brings them here now, how they will know it worked, what they have already tried, how much time they really have, what they enjoy and what they refuse to do. Add the health questionnaire, and refer them to a doctor as soon as an answer calls for it."},
        ],
        "sources": [
            {"t": "HAS. Consultation et prescription médicale d'activité physique à des fins de santé chez l'adulte. Guide. 2022 (in French).", "u": "https://www.has-sante.fr/upload/docs/application/pdf/2018-10/guide_aps_vf.pdf"},
            {"t": "Riebe D, Franklin BA, Thompson PD, et al. Updating ACSM's Recommendations for Exercise Preparticipation Health Screening. <em>Med Sci Sports Exerc</em>. 2015.", "u": "https://doi.org/10.1249/MSS.0000000000000664"},
            {"t": "Bull FC, Al-Ansari SS, Biddle S, et al. World Health Organization 2020 guidelines on physical activity and sedentary behaviour. <em>Br J Sports Med</em>. 2020.", "u": "https://doi.org/10.1136/bjsports-2020-102955"},
            {"t": "Teixeira PJ, Carraça EV, Markland D, et al. Exercise, physical activity, and self-determination theory: a systematic review. <em>Int J Behav Nutr Phys Act</em>. 2012.", "u": "https://doi.org/10.1186/1479-5868-9-78"},
        ],
    },
    {
        "fr": "questionnaire-sante-avant-le-sport-client",
        "slug": "pre-exercise-health-questionnaire",
        "title": "Pre-exercise health questionnaire: what to ask a client",
        "description": "Pre-exercise health questionnaire: what a personal trainer can ask a client, how the PAR-Q+ copyright works and what to do when a client answers yes.",
        "body": """
<p>The short answer: a <strong>pre-exercise health questionnaire</strong> asks about current activity, known conditions, new symptoms and target intensity. Whether you must use one depends on where you work, but the tool is useful either way. The French National Authority for Health (HAS) recommends a self-administered questionnaire for anyone who wants to start or step up activity of at least moderate intensity, and says an exercise professional can offer it. If a client answers yes, you don't interpret: you refer them to a doctor before starting.</p>

<h2>Do personal trainers need a health questionnaire or a doctor's note?</h2>
<p>No single answer holds everywhere. Check the rules where you work: qualification, insurance and consumer law vary by country. Where nothing requires them, you can usually still build a questionnaire or a doctor's note into your client agreement.</p>

<h2>PAR-Q+ or your own form: which should you use?</h2>
<div class="tablewrap"><table>
<caption>Source: HAS 2022 and the PAR-Q+ terms and conditions, read on October 31, 2026.</caption>
<thead><tr><th>Option</th><th>Use</th><th>What to know</th></tr></thead>
<tbody>
<tr><td>PAR-Q+</td><td>Screening before activity, ages 15 to 69</td><td>7 questions, protected text</td></tr>
<tr><td>Your own questionnaire</td><td>What changes your session</td><td>Write it yourself, without copying the PAR-Q+</td></tr>
</tbody>
</table></div>
<p>The PAR-Q+ calls for care. Its terms require prior written permission to modify it or to build it into an app, website, software or online survey. Citing the source doesn't count as permission. Unmodified official versions are currently free for certain individual, clinical, educational and non-commercial research uses. The terms don't name coaches, even though the site offers resources for exercise professionals, and fees may apply to commercial use. If in doubt, write to the rights holder.</p>
<p>The simplest route: invite the client to fill it in themselves on the official site, eparmedx.com. Finding the text reprinted elsewhere doesn't give you permission to copy it into your form.</p>

<h2>What should a pre-exercise questionnaire ask?</h2>
<p>For your own questionnaire, start from the logic of the American College of Sports Medicine (ACSM), which comes down to three factors, and add what serves your session:</p>
<ul>
<li><strong>Current activity.</strong> How many sessions a week, for how long, at what intensity.</li>
<li><strong>What is known.</strong> A diagnosed cardiovascular, metabolic or renal disease. Yes or no is enough.</li>
<li><strong>What is new.</strong> An unusual sign, at rest or during exercise.</li>
<li><strong>Target intensity.</strong> What the client wants to do, and at what level.</li>
<li><strong>What limits movement.</strong> Discomfort, recent surgery, pregnancy: anything that forces you to adapt an exercise.</li>
</ul>
<p>Run each question through the same filter: what do you change in your session if the answer is yes? If nothing changes, cut it.</p>
<p>HAS adds two age markers. At 45 or older, with no regular intense activity and a plan close to maximum effort, medical advice is advised. From age 70, it is recommended for activity of at least high intensity.</p>

<h2>What should you do if a client answers yes?</h2>
<p>HAS is clear. A positive answer: medical advice is recommended before starting. Signs or symptoms suggesting a disease: the person holds off and sees their doctor. All negative: they can become more active, with the usual precautions.</p>
<p>Your role stops there. You don't judge how serious it is and you don't reassure. You note the date, wait for the client to confirm the advice they received and any limits, then adapt. Run the questionnaire again whenever the situation changes.</p>

<h2>How should you handle the answers?</h2>
<p>If you work in the EU or the UK, health data is specially protected, and a health questionnaire counts as health data. Ask for explicit consent, separate from your terms and conditions, after saying what you collect and why. One point stays open: consent only counts if the person can really refuse, so declining a client who leaves the form blank isn't a settled question. Store the answers in the health section of your <a href="/coachs/fiche-client-coach-sportif.html">client intake form</a>.</p>
<p>This guide is for information only and doesn't replace advice from a doctor or a lawyer.</p>

<h2>Key takeaways</h2>
<ul>
<li>Whether a questionnaire is required depends on where you work, but HAS recommends one before starting.</li>
<li>The PAR-Q+ can't be copied into a form without written permission.</li>
<li>When a client answers yes, you don't interpret: you refer them to a doctor before starting.</li>
</ul>
""",
        "faq": [
            {"q": "Is the PAR-Q+ mandatory?", "a": "That depends on the rules where you work. HAS, France's national health authority, recommends a self-administered questionnaire of this kind before starting or stepping up activity of at least moderate intensity. The PAR-Q+ terms forbid modifying it or building it into an online tool without written permission."},
            {"q": "Can a personal trainer ask for a doctor's note?", "a": "Yes, you can usually make it a condition in your client agreement. Whether a rule requires it depends on where you work. If a client's answers call for medical advice, wait for that advice before starting."},
            {"q": "What should you do when a client answers yes on a health questionnaire?", "a": "Don't interpret the answer and don't reassure. Medical advice is recommended before starting, and a client with signs or symptoms suggesting a disease holds off and sees their doctor. Note the date, then adapt once the client confirms the advice and any limits."},
        ],
        "sources": [
            {"t": "HAS. Consultation et prescription médicale d'activité physique à des fins de santé chez l'adulte. Guide. 2022 (in French).", "u": "https://www.has-sante.fr/upload/docs/application/pdf/2018-10/guide_aps_vf.pdf"},
            {"t": "Riebe D, Franklin BA, Thompson PD, et al. Updating ACSM's Recommendations for Exercise Preparticipation Health Screening. <em>Med Sci Sports Exerc</em>. 2015.", "u": "https://doi.org/10.1249/MSS.0000000000000664"},
            {"t": "CNIL, France's data protection authority. Questions-réponses sur la protection des données dans le secteur du sport amateur (hors contrat). 2022 (in French).", "u": "https://www.cnil.fr/fr/sport-amateur-hors-contrat/questions-reponses"},
            {"t": "PAR-Q+ Collaboration. Terms and Conditions. 2026.", "u": "https://eparmedx.com/terms-and-conditions/"},
        ],
    },
    {
        "fr": "tests-physiques-nouveau-client",
        "slug": "fitness-tests-for-new-clients",
        "title": "Fitness tests for new clients: which ones should you use?",
        "description": "Fitness tests for new clients: which ones to choose by profile, how to run them reliably, how to read the results and what to make of the Ruffier test.",
        "body": """
<p>The short answer: I found no official test battery. For <strong>fitness tests for new clients</strong>, choose three or four tests tied to the client's goal: one for endurance, one for the lower body, one for the upper body, and a balance test if their profile calls for it. They track the client against themselves. They make no diagnosis.</p>

<h2>Which fitness tests should you choose for each client?</h2>
<p>The French National Authority for Health (HAS) details the most common field tests and points out that no single test measures the strength or flexibility of the whole body. The table combines its benchmarks with a few studies.</p>
<div class="tablewrap"><table>
<caption>Source: HAS 2022; Holland 2014; Jones 1999; Penry 2011.</caption>
<thead><tr><th>Capacity</th><th>Test</th><th>Profile</th><th>What to know</th></tr></thead>
<tbody>
<tr><td>Endurance</td><td>6-minute walk</td><td>Beginner, older adult, returning to exercise</td><td>Clinical validation, not athletic</td></tr>
<tr><td>Endurance</td><td>12-minute run</td><td>Young adult who is already active</td><td>Intense effort, treat the VO2 max estimate with caution</td></tr>
<tr><td>Legs</td><td>30-second chair stand</td><td>Older adult, beginner</td><td>Chair without armrests, no hands. Validated after age 60</td></tr>
<tr><td>Upper body</td><td>Push-ups without stopping</td><td>Adult with no shoulder discomfort</td><td>Mixes strength and endurance</td></tr>
<tr><td>Strength</td><td>10- to 15-rep max</td><td>Beginner, older adult, returning to exercise</td><td>Specific to each exercise</td></tr>
<tr><td>Flexibility</td><td>Sit-and-reach</td><td>Client with no back pain</td><td>Mostly the hamstrings</td></tr>
<tr><td>Balance</td><td>Single-leg stance, eyes closed</td><td>Older adult</td><td>Three tries, best time. Stay beside them, near a support</td></tr>
</tbody>
</table></div>
<p>Two example selections. For a sedentary 55-year-old returning to exercise: 6-minute walk, chair stand, single-leg stance. For an active 30-year-old aiming for strength: 12-minute run, push-ups, and an 8-rep max on two exercises they have mastered, over two sessions.</p>
<p>Before any test, reread the <a href="/coachs/questionnaire-sante-avant-le-sport-client.html">health questionnaire</a>. If it calls for medical advice, the test waits.</p>

<h2>How do you run fitness tests without skewing the results?</h2>
<p>A test is only worth something if you can repeat it identically. The technical standard from the European Respiratory Society and the American Thoracic Society (ERS/ATS; Holland, 2014) considers walking tests valid, reliable and responsive to change in chronic respiratory disease, while stressing how sensitive they are to small differences in method. It recommends two attempts at the 6-minute walk, at least 30 minutes apart, to set a stable baseline.</p>
<ul>
<li><strong>Same setup.</strong> Same place, same course, same time of day, same shoes, same chair. HAS describes the 6-minute walk around two cones 30 m (about 100 ft) apart. The ERS/ATS standard calls for a flat surface and at least 30 m: on a shorter course, forget the norms.</li>
<li><strong>Same words.</strong> Write your instructions and read them out. For the walk, the standard provides a set phrase each minute, and nothing else. If the client stops, the clock keeps running.</li>
<li><strong>Same preparation.</strong> For the 6-minute walk, no warm-up and no intense effort in the previous 2 hours, according to that standard. For other tests, keep the same warm-up.</li>
<li><strong>A written record.</strong> Note the conditions next to the result, or you will end up comparing two different things.</li>
</ul>
<p>If the client reports pain, faintness, unusual breathlessness or cramps, or if they stagger or turn pale, stop the test and refer them to a doctor. For chest pain or a fainting spell, have them sit or lie down and call your local emergency number (911 in the US, 999 or 112 in the UK and Europe).</p>

<h2>Can a new client do a maximal test?</h2>
<p>Not at the first session, unless they are a trained client who already knows the test. HAS describes the 1RM as a reliable indicator of strength, and 4RM or 8RM tests as a reliable estimate. It considers 10- to 15-rep max tests safer for people who are older, deconditioned or living with a chronic disease. Even at 4 or 8 reps, wait until the technique is clean. The 12-minute run already takes sustained effort, so keep it for a client used to intensity.</p>
<p>Don't confuse these tests with a clinical exercise stress test, which is done with ECG and blood pressure monitoring in a clinical setting.</p>

<h2>Is the Ruffier test reliable?</h2>
<p>It remains a simple marker, not very precise for estimating cardiorespiratory fitness. In a study of 81 healthy adults (Sartor, 2016), the Ruffier-Dickson index had a correlation of -0.40 with measured fitness and explained 15% of the variability. It doesn't appear in the HAS table of tests. If your client insists on it, compare their scores with each other and don't derive a VO2 max from them.</p>

<h2>How do you read the results, and when should you retest?</h2>
<p>Compare the client with themselves: that is what a <a href="/methode/ligne-de-base.html">baseline</a> means. Norms describe other populations. For the 6-minute walk, Enright (1998) found a median of 576 m (about 1,890 ft) in men and 494 m (about 1,620 ft) in women, among 290 healthy adults aged 40 to 80, and the equations explain about 40% of the variance. For the 12-minute run, Penry (2011) reports good reliability in young adults but urges caution when deriving a VO2 max from it.</p>
<p>A gap from a norm lets you conclude nothing about the client's health. If a result surprises you, refer them to a doctor without commenting on it. The chair stand, for its part, was validated in 76 adults over 60 (Jones, 1999): its values don't transfer to a 30-year-old client.</p>
<p>I found no official frequency for retesting. The most logical approach is to retest at the end of a <a href="/coachs/creer-programme-personnalise-client.html">program</a> block, under the same conditions, then show the change in the <a href="/coachs/bilan-mensuel-client-coaching.html">monthly report</a>.</p>

<h2>Key takeaways</h2>
<ul>
<li>Three or four tests tied to the goal are enough, chosen by profile.</li>
<li>Use the same protocol every time, record the conditions and compare the client with themselves.</li>
<li>A test makes no diagnosis: at the slightest warning sign, stop and refer to a doctor.</li>
</ul>
""",
        "faq": [
            {"q": "What fitness test should a beginner do?", "a": "The 6-minute walk for endurance, the 30-second chair stand for the legs, and a 10- to 15-rep max if needed. These tests are easy to dose. Always reread the health questionnaire before starting."},
            {"q": "Is the Ruffier test reliable?", "a": "It is a simple marker, not very precise for estimating cardiorespiratory fitness. In a study of 81 healthy adults, it explained 15% of the variability. It doesn't appear in the table of tests from HAS, France's national health authority."},
            {"q": "How often should you retest a client?", "a": "I found no official frequency. The most logical approach is to retest at the end of a training block, under the same conditions, to compare the client with themselves."},
        ],
        "sources": [
            {"t": "HAS. Guide des connaissances sur l'activité physique et la sédentarité. 2022 (in French).", "u": "https://www.has-sante.fr/upload/docs/application/pdf/2022-08/guide_connaissance_ap_sedentarite_vf.pdf"},
            {"t": "Holland AE, Spruit MA, Troosters T, et al. An official European Respiratory Society/American Thoracic Society technical standard: field walking tests in chronic respiratory disease. <em>Eur Respir J</em>. 2014.", "u": "https://doi.org/10.1183/09031936.00150314"},
            {"t": "Enright PL, Sherrill DL. Reference equations for the six-minute walk in healthy adults. <em>Am J Respir Crit Care Med</em>. 1998.", "u": "https://doi.org/10.1164/ajrccm.158.5.9710086"},
            {"t": "Jones CJ, Rikli RE, Beam WC. A 30-s chair-stand test as a measure of lower body strength in community-residing older adults. <em>Res Q Exerc Sport</em>. 1999.", "u": "https://doi.org/10.1080/02701367.1999.10608028"},
            {"t": "Penry JT, Wilcox AR, Yun J. Validity and reliability analysis of Cooper's 12-minute run and the multistage shuttle run in healthy adults. <em>J Strength Cond Res</em>. 2011.", "u": "https://doi.org/10.1519/JSC.0b013e3181cc2423"},
            {"t": "Sartor F, Bonato M, Papini G, et al. A 45-Second Self-Test for Cardiorespiratory Fitness: Heart Rate-Based Estimation in Healthy Individuals. <em>PLoS One</em>. 2016.", "u": "https://doi.org/10.1371/journal.pone.0168154"},
        ],
    },
    {
        "fr": "creer-programme-personnalise-client",
        "slug": "how-to-write-a-client-training-program",
        "title": "How to write a training program for a client: the method",
        "description": "How to write a personalized training program for a client: from the first assessment to progression, with WHO and ACSM benchmarks for each training goal.",
        "body": """
<p>The short answer: a <strong>personalized training program</strong> starts from the client's assessment, never from a template. Begin with their goal, their real available time and their level. Set the volume and intensity, choose a split they will stick to, write a progression rule, then adjust from what they report. The American College of Sports Medicine (ACSM) position stand published in 2026 shows that few variables really change results, so focus on those.</p>

<h2>What do you need to know before writing a program?</h2>
<p>Five pieces of information decide almost everything. They come out of the <a href="/coachs/bilan-forme-premier-rendez-vous.html">first fitness assessment</a> and the <a href="/coachs/tests-physiques-nouveau-client.html">fitness tests</a>:</p>
<ul>
<li><strong>The goal</strong>, in the client's words, with a deadline.</li>
<li><strong>Real available time:</strong> the number of sessions they will keep up in a busy week.</li>
<li><strong>Level:</strong> what they do today, and what they have done before.</li>
<li><strong>Location and equipment.</strong></li>
<li><strong>Limits:</strong> reported discomfort, medical advice pending or limits set by a doctor.</li>
</ul>
<p>If medical advice is pending, the program waits too. If the client has been given limits, apply them as they are, without reinterpreting them.</p>

<h2>How do you set volume and intensity?</h2>
<p>Two references are enough to set the benchmarks: the WHO for health, and the ACSM for strength training, with 137 systematic reviews and more than 30,000 participants, all healthy adults.</p>
<div class="tablewrap"><table>
<caption>Source: WHO 2020; ACSM 2026; Schoenfeld 2017. Healthy adults.</caption>
<thead><tr><th>Goal</th><th>Benchmark</th><th>Source</th></tr></thead>
<tbody>
<tr><td>Health, returning to exercise</td><td>150 to 300 min of moderate activity per week, or 75 to 150 min of vigorous activity, plus strength work for all major muscle groups on 2 or more days</td><td>WHO</td></tr>
<tr><td>Older adults</td><td>Within that volume, varied activity focused on balance and strength, 3 or more days per week</td><td>WHO</td></tr>
<tr><td>Strength</td><td>80% of 1RM or more, 2 to 3 sets, 2 or more sessions per week</td><td>ACSM</td></tr>
<tr><td>Muscle size</td><td>10 or more sets per week, per muscle group. More volume, more gain (15 studies)</td><td>ACSM, Schoenfeld</td></tr>
<tr><td>Power</td><td>30 to 70% of 1RM, fast lifting phase</td><td>ACSM</td></tr>
</tbody>
</table></div>
<p>These figures describe the destination, well beyond a first week. The WHO advises anyone far from them to start small, then gradually increase frequency, intensity and duration. Compared with no training, strength work already improves strength, muscle size and balance. For a beginner, a simple first program is enough.</p>
<p>Other settings matter less than people think. According to the ACSM, training to muscle failure or changing the type of equipment did not consistently change results. A client without a gym can follow a real program, as long as the load or the reps can go up.</p>

<h2>How should you split sessions across the week?</h2>
<p>Choose from the client's calendar. A meta-analysis of 14 studies and 392 people (Ramos-Campo, 2024) found no significant difference in strength or muscle mass between full-body and split training when volume is equal. The authors conclude that the choice can follow preferences.</p>
<p>Here is an example logic, to adjust:</p>
<ul>
<li><strong>2 sessions:</strong> full body each time.</li>
<li><strong>3 sessions:</strong> full body, or an upper and lower body rotation.</li>
<li><strong>4 sessions or more:</strong> a split becomes possible, if the client really keeps them up.</li>
</ul>
<p>Think about the missed week: if a session drops out, a split leaves a muscle group behind and a full-body plan doesn't. For a strength goal, put the priority exercise early in the session, as the ACSM notes.</p>

<h2>How do you progress a training program?</h2>
<p>Write the rule into the program, so the client knows what triggers the next step. Example: when every set reaches 12 clean reps, the load goes up and the reps drop back to 8.</p>
<p>You have several levers. A trial in trained lifters (Plotkin, 2022, 43 at the start, 38 at the end) shows that adding reps or adding load gives comparable adaptations over 8 weeks, with a slight edge to load for maximal strength. That helps at home, when the available load tops out. The study is short and covers only the quadriceps and calves.</p>
<p>Change one variable at a time, so you know what produced what. Periodization did not consistently change results according to the ACSM: keep complex plans for an advanced client, and review <a href="/articles/periodisation-entrainement-bases.html">the basics of periodization</a> if you need to.</p>

<h2>When should you adjust a program, and where does your role end?</h2>
<p>After each session, collect perceived effort, any discomfort and what was skipped. If the client misses the same type of session twice in a row, change the program before you talk about motivation.</p>
<p>Three limits don't move:</p>
<ul>
<li><strong>Health.</strong> According to the WHO, someone who develops new symptoms as they increase their activity should see a health professional. You pause, you refer, you don't interpret.</li>
<li><strong>Nutrition.</strong> You can share general guidelines. The more personal the advice, the higher the risk, especially when a medical condition is involved.</li>
<li><strong>The legal framework.</strong> Check the rules where you work: qualification, insurance and consumer law vary by country. That applies to online coaching as well as in-person sessions.</li>
</ul>

<h2>Key takeaways</h2>
<ul>
<li>The program comes from the assessment: goal, real time, level, equipment, limits.</li>
<li>Set few variables, with a written progression rule and a split the client will stick to.</li>
<li>New symptoms, nutrition and local rules: these limits come before the program.</li>
</ul>
""",
        "faq": [
            {"q": "How do you write a personalized strength program for a client?", "a": "Start from the assessment: goal, real available time, level, equipment and limits. Then set volume and intensity for the goal, choose a split they will stick to, write a progression rule and adjust from their feedback."},
            {"q": "How many sessions per week should a program include?", "a": "The WHO recommends strength work for all major muscle groups on 2 or more days per week, and the ACSM 2 or more sessions for strength. For a beginner, two full sessions are a good start. The right number is the one the client keeps up in a busy week."},
            {"q": "Can a personal trainer include a meal plan in a program?", "a": "You can share general guidelines, without presenting yourself as a dietitian. The line with individual advice isn't clear-cut: the more personal the advice, the higher the risk, especially with a medical condition. In that case, refer the client to a doctor or dietitian."},
        ],
        "sources": [
            {"t": "Currier BS, D'Souza AC, Singh MAF, et al. American College of Sports Medicine Position Stand. Resistance Training Prescription for Muscle Function, Hypertrophy, and Physical Performance in Healthy Adults: An Overview of Reviews. <em>Med Sci Sports Exerc</em>. 2026.", "u": "https://doi.org/10.1249/MSS.0000000000003897"},
            {"t": "Schoenfeld BJ, Ogborn D, Krieger JW. Dose-response relationship between weekly resistance training volume and increases in muscle mass: A systematic review and meta-analysis. <em>J Sports Sci</em>. 2017.", "u": "https://doi.org/10.1080/02640414.2016.1210197"},
            {"t": "Bull FC, Al-Ansari SS, Biddle S, et al. World Health Organization 2020 guidelines on physical activity and sedentary behaviour. <em>Br J Sports Med</em>. 2020.", "u": "https://doi.org/10.1136/bjsports-2020-102955"},
            {"t": "Ramos-Campo DJ, Benito-Peinado PJ, Andreu-Caravaca L, et al. Efficacy of Split Versus Full-Body Resistance Training on Strength and Muscle Growth: A Systematic Review With Meta-Analysis. <em>J Strength Cond Res</em>. 2024.", "u": "https://doi.org/10.1519/JSC.0000000000004774"},
            {"t": "Plotkin D, Coleman M, Van Every D, et al. Progressive overload without progressing load? The effects of load or repetition progression on muscular adaptations. <em>PeerJ</em>. 2022.", "u": "https://doi.org/10.7717/peerj.14142"},
        ],
    },
    {
        "fr": "fideliser-clients-coaching-sportif",
        "slug": "client-retention-for-personal-trainers",
        "title": "Why your clients quit: client retention for personal trainers",
        "seo_title": "Client retention for personal trainers: why clients quit",
        "description": "Client retention for personal trainers: why clients quit, what dropout studies really show and how to calculate your retention rate from your own numbers.",
        "body": """
<p>The short answer: to improve <strong>client retention as a personal trainer</strong>, start by measuring who leaves and why, because no statistic will do that for you. I found no dropout rate specific to independent coaches. Research mostly supports three simple levers: a written goal, recorded progress and regular feedback. The rest is in your own client list.</p>

<h2>How many clients actually quit?</h2>
<p>The only solid figure I kept comes from one gym in Rio de Janeiro. Sperandei and colleagues followed 5,240 members: 63% had dropped out before the third month, and fewer than 4% passed twelve months of continuous activity. The study, published in 2016, covers a single gym, draws on its membership data and took place in an unsupervised setting, as its title says. So it applies neither to all gyms nor to a client working with a coach. Be wary of dropout percentages that circulate without a reference.</p>
<p>Your real number takes ten minutes to calculate. Take your active clients at the start of a quarter and count how many are still there at the end, without adding new ones. Example calculation: 12 clients on January 1, 9 still active on March 31, so 9 ÷ 12 = 75% retention over three months. With so few clients, one departure weighs more than 8 points. Read this rate over the year, and look above all at the reasons.</p>

<h2>Why do personal training clients quit?</h2>
<p>None of the studies cited here answers that for a client of an independent coach. Your best source remains your former clients. This working grid, which has no statistical value, helps you sort each departure:</p>
<ul>
<li><strong>Planned departure:</strong> the goal is reached, or the client now knows how to train alone. That is a success, and maybe a future referral.</li>
<li><strong>Forced departure:</strong> a move, budget, new work hours, a birth, health. You can sometimes offer a lighter or remote format.</li>
<li><strong>Avoidable departure:</strong> invisible progress, sessions that all feel the same, a goal never revisited, a time slot that stopped working, a relationship gone stale.</li>
</ul>
<p>Ask every client who leaves three questions: what triggered your decision, what would have made you stay, what would you say to someone thinking of starting? Write the answers down word for word. "I can't afford it anymore" can also mean "I no longer see what I'm getting out of it." If the same reason comes up several times in a year, you have found your top priority.</p>

<h2>What keeps a client long term?</h2>
<p>The work I selected doesn't cover independent one-to-one coaching, but it gives a direction.</p>
<ul>
<li><strong>Track progress.</strong> The meta-analysis by Harkin and colleagues (2016, 138 trials, 19,951 people) finds an average effect of 0.40 on goal attainment, stronger when the outcome is recorded or shared. It isn't limited to exercise.</li>
<li><strong>Go beyond self-monitoring.</strong> Across 122 evaluations and 44,747 people, Michie and colleagues (2009) show that interventions combining it with another technique from control theory reach an effect of 0.42, against 0.26 for the others.</li>
<li><strong>Get the setting right.</strong> The synthesis of 55 reviews by Collado-Mateo (2021) lists supervision, feedback, progress tracking, goals, social support and enjoyment, among others. It covers patients with chronic disease and older adults, not every client a coach sees.</li>
</ul>
<p>In practice: the client records, you respond, and you review the goal together. A <a href="/coachs/bilan-mensuel-client-coaching.html">one-page monthly report</a> is enough to set that rhythm.</p>

<h2>When should you step in?</h2>
<p>Don't wait for the client to announce they are leaving. Four moments call for action:</p>
<ul>
<li><strong>The first few weeks.</strong> At the Rio gym, dropout came early, and <a href="/articles/combien-de-temps-pour-prendre-une-habitude.html">a habit takes time to form</a>. Plan a quick check-in around week three: what works, what doesn't.</li>
<li><strong>The end of a package.</strong> Talk about what comes next two or three sessions before the last one, report in hand. <a href="/coachs/packs-abonnement-seance-coach-sportif.html">The plan you offer</a> also plays a part at that moment.</li>
<li><strong>Goal reached.</strong> Set the next one together, or prepare a clean exit with what they need to continue alone.</li>
<li><strong>Repeated absences.</strong> Apply <a href="/coachs/seance-annulee-regles-coach.html">your cancellation policy</a>, then ask what changed in their week.</li>
</ul>
<p>Don't count on the contract to hold anyone. Check the rules where you work: qualification, insurance and consumer law vary by country, and that includes automatic renewal and marketing emails. Before you email a former client, check that you're allowed to, and give them a simple way to refuse in every message.</p>

<h2>Key takeaways</h2>
<ul>
<li>No general dropout rate describes your business: calculate your retention from your own clients and note every reason for leaving.</li>
<li>Written goal, recorded progress, regular feedback: these levers have the best support, even if the studies don't cover independent coaches.</li>
<li>Act before the departure: first weeks, end of a package, goal reached, repeated absences.</li>
</ul>
""",
        "faq": [
            {"q": "How do personal trainers keep clients long term?", "a": "Set a written goal, record progress, run regular reviews and bring up what comes next before the package ends. Also ask every client who leaves what would have made them stay: your own reasons for departure will teach you more than a general statistic."},
            {"q": "What is the gym dropout rate?", "a": "I found no reliable overall figure. In one Rio de Janeiro gym studied across 5,240 members, 63% had dropped out before the third month. That result comes from a single gym in an unsupervised setting. It applies neither to all gyms nor to a client working with a coach."},
            {"q": "How do you calculate client retention?", "a": "Take your active clients at the start of a quarter and count how many are still there at the end, without adding new ones. For example, 12 clients on January 1 and 9 still active on March 31 give 9 ÷ 12 = 75% over three months. With few clients, read the rate over the year."},
        ],
        "sources": [
            {"t": "Sperandei S, Vieira MC, Reis AC. Adherence to physical activity in an unsupervised setting: Explanatory variables for high attrition rates among fitness center members. <em>J Sci Med Sport</em>. 2016.", "u": "https://doi.org/10.1016/j.jsams.2015.12.522"},
            {"t": "Harkin B, Webb TL, Chang BP, et al. Does monitoring goal progress promote goal attainment? A meta-analysis of the experimental evidence. <em>Psychol Bull</em>. 2016.", "u": "https://doi.org/10.1037/bul0000025"},
            {"t": "Michie S, Abraham C, Whittington C, McAteer J, Gupta S. Effective techniques in healthy eating and physical activity interventions: a meta-regression. <em>Health Psychol</em>. 2009.", "u": "https://doi.org/10.1037/a0016136"},
            {"t": "Collado-Mateo D, Lavín-Pérez AM, Peñacoba C, et al. Key Factors Associated with Adherence to Physical Exercise in Patients with Chronic Diseases and Older Adults: An Umbrella Review. <em>Int J Environ Res Public Health</em>. 2021.", "u": "https://doi.org/10.3390/ijerph18042023"},
        ],
    },
    {
        "fr": "bilan-mensuel-client-coaching",
        "slug": "monthly-client-progress-report",
        "title": "Monthly client progress report: what to show them",
        "description": "Monthly client progress report for personal trainers: which measures to show, how to compare them, how to run the review and how to handle health data.",
        "body": """
<p>The short answer: a <strong>monthly client progress report</strong> fits on one page and answers four questions: where does the goal stand, what did you do, what changed, and what do you change next month. Show three to five measures, always compared with the client themselves, then finish with a written decision. The monthly rhythm is a practical choice that the studies cited here don't set.</p>

<h2>Why run a progress review every month?</h2>
<p>From one session to the next, a client struggles to see their progress. The report makes it visible. The meta-analysis by Harkin and colleagues (2016, 138 trials, 19,951 people) shows that tracking progress helps people reach their goals, with a stronger effect when the outcome is recorded or shared. It isn't limited to exercise, but a report checks both boxes: it is written down, and it is shared with you.</p>
<p>It also helps you make a decision instead of rolling the same program over, and it gives you something to lean on to <a href="/coachs/fideliser-clients-coaching-sportif.html">keep a client long term</a>. One month already gives you material on attendance and loads. A field test can wait two or three months.</p>

<h2>What should a monthly progress report include?</h2>
<p>Choose according to the client's goal. This grid covers most cases:</p>
<div class="tablewrap"><table>
<caption>Source: working grid for this guide, to adapt to each client.</caption>
<thead><tr><th>Measure</th><th>What you show</th><th>Precaution</th></tr></thead>
<tbody>
<tr><td>Attendance</td><td>Sessions done out of sessions planned</td><td>Separate unavoidable absences from the others</td></tr>
<tr><td>Load</td><td>Perceived effort multiplied by duration, week by week</td><td>Compare with the client, never with someone else</td></tr>
<tr><td>Performance</td><td>Two or three benchmark exercises: load, reps, time</td><td>Keep the same exercise and the same instructions</td></tr>
<tr><td>Field test</td><td>One test only, if it serves the goal</td><td>Same conditions each time</td></tr>
<tr><td>How they feel</td><td>Energy, sleep, enjoyment, rated from 1 to 5</td><td>It guides the conversation and diagnoses nothing</td></tr>
<tr><td>Weight, measurements</td><td>Only if it is their goal and they agree</td><td>Never the only measure of success</td></tr>
</tbody>
</table></div>
<p>For load, the simplest method remains session RPE: an effort rating multiplied by duration. Foster and colleagues evaluated it in 2001 against a heart-rate-based method and found it valid across varied efforts. Choosing tests is covered in our guide on <a href="/coachs/tests-physiques-nouveau-client.html">fitness tests for new clients</a>.</p>

<h2>How do you compare results accurately?</h2>
<p>The only useful comparison puts the client against themselves, under equal conditions: same exercise, same instructions, same time of day, same warm-up. That rigor matters. For the 6-minute walk, the 2014 European and American standard notes that results are sensitive to small differences in method and recommends two attempts. This test was validated in chronic respiratory disease: with a healthy client, it only serves to compare them with themselves.</p>
<p>Also be wary of tests that promise too much. In the study by Sartor and colleagues (2016, 81 healthy adults), the Ruffier-Dickson index explains only 15% of the variability in cardiorespiratory fitness. Keep it as a simple marker, and don't derive a VO2 max from it. Read any gap over several months: a single drop can come from a busy week, a trip or a cold.</p>

<h2>How do you run the review with a client?</h2>
<p>Fifteen to twenty minutes is enough, during a session or by video call. One possible flow:</p>
<ol>
<li>Start by asking how the month felt, before showing a single number.</li>
<li>Show what improved, with the starting number next to it.</li>
<li>Present what stalled as facts: "6 sessions out of 8," with no comment on willpower.</li>
<li>Look for the cause together: schedule, sleep, an overly ambitious program, an outdated goal.</li>
<li>Decide on one to three changes and write down next month's goal.</li>
</ol>
<p>Treat a bad month the same way. If the client can't keep up three sessions a week, adapt the program to their real week. Don't promise any result for the next month. If they mention a new symptom, an illness or an eating disorder, you don't interpret: you refer them to a doctor or dietitian.</p>

<h2>What should you do with the report data?</h2>
<p>A report often contains sensitive data, and if you work in the EU or the UK, health data is specially protected. Medical history, illnesses and treatments are health data by nature, and weight can become health data too, especially combined with step counts or calories. Ask for explicit consent, separate from your terms and conditions, and keep these documents in a protected space. Check the rules where you work: qualification, insurance and consumer law vary by country.</p>
<p>The report stays between you and your client. Share it with a doctor, a physical therapist, another coach or a relative only with their agreement. The simplest approach: hand it to them, and they share it if they wish. Before you post a before-and-after photo in which they can be recognized, get written permission that states the medium, the purpose and the duration. Agreeing to be photographed isn't enough.</p>

<h2>Key takeaways</h2>
<ul>
<li>One page, three to five measures, one written decision: the report exists to change something next month.</li>
<li>Compare the client with themselves, under equal conditions, and read gaps over several months.</li>
<li>The report data belongs to the client: explicit consent, a protected space, no sharing without their agreement.</li>
</ul>
""",
        "faq": [
            {"q": "What should a monthly coaching progress report include?", "a": "The starting goal, attendance, two or three performance measures, how the client feels and the changes decided for the next month. One page is enough. Compare each number with the client themselves, never with an average or another client."},
            {"q": "Should you weigh a client at every review?", "a": "Only if weight matches their goal and they agree. That number should never be the only measure of success, and it can count as health data. If the client mentions an eating disorder or an illness, refer them to a doctor or dietitian."},
            {"q": "Can a personal trainer send a client's report to their doctor or physical therapist?", "a": "Only with the client's agreement. The simplest approach is to give them the report so they can pass it on themselves. Without that agreement, don't send it to anyone, even a health professional."},
        ],
        "sources": [
            {"t": "Harkin B, Webb TL, Chang BP, et al. Does monitoring goal progress promote goal attainment? A meta-analysis of the experimental evidence. <em>Psychol Bull</em>. 2016.", "u": "https://doi.org/10.1037/bul0000025"},
            {"t": "Foster C, Florhaug JA, Franklin J, et al. A new approach to monitoring exercise training. <em>J Strength Cond Res</em>. 2001.", "u": "https://pubmed.ncbi.nlm.nih.gov/11708692/"},
            {"t": "Holland AE, Spruit MA, Troosters T, et al. An official European Respiratory Society/American Thoracic Society technical standard: field walking tests in chronic respiratory disease. <em>Eur Respir J</em>. 2014.", "u": "https://doi.org/10.1183/09031936.00150314"},
            {"t": "Sartor F, Bonato M, Papini G, et al. A 45-Second Self-Test for Cardiorespiratory Fitness: Heart Rate-Based Estimation in Healthy Individuals. <em>PLoS One</em>. 2016.", "u": "https://doi.org/10.1371/journal.pone.0168154"},
            {"t": "CNIL, France's data protection authority. Qu'est-ce qu'une donnée de santé ? 2018 (in French).", "u": "https://www.cnil.fr/fr/quest-ce-ce-quune-donnee-de-sante"},
        ],
    },
    {
        "fr": "lire-etat-de-forme-client",
        "slug": "how-to-read-client-readiness",
        "title": "Sleep, fatigue, training load: how to read a client before a session",
        "seo_title": "How to read client readiness before a training session",
        "description": "How to read client readiness: what to ask before a session, what a short night changes, how to track load, and what smartwatches and HRV can really tell you.",
        "body": """
<p>The short answer: to read <strong>client readiness</strong>, ask three questions before the warm-up, compare the answers with what is normal for that client, then adjust the session when several signals point the same way. No single marker is enough: not sleep, not heart rate variability, not a smartwatch score. These measures help you dose an effort. They make no diagnosis.</p>

<h2>What should you ask a client before a session?</h2>
<p>Two minutes is enough. Keep the same questions and the same 1 to 5 scale:</p>
<ul>
<li>How did you sleep compared with usual?</li>
<li>How much energy do you have today, stress included?</li>
<li>Do you have any new pain or discomfort?</li>
</ul>
<p>The review by Saw and colleagues (2016, 56 studies) shows that subjective and objective measures agree poorly, and that subjective ones better reflect training load. It covers athletes, so apply it with caution. Record each answer, because only the gap from their normal tells you anything. A 2 from a client who always answers 4 counts for more than a 2 from one who often answers 2.</p>

<h2>Should a bad night's sleep change the session?</h2>
<p>Not necessarily. The meta-analysis by Craven and colleagues (2022, 69 publications, 959 participants, 89% of them men) finds performance down by 7.56% on average after 6 hours of sleep or less, with very high heterogeneity between studies. Two nuances help in practice:</p>
<ul>
<li><strong>The type of night.</strong> The effects were consistent only after a sleepless night or an early wake-up, not after a late bedtime. The drop then reached about 0.4% per hour awake before exercise.</li>
<li><strong>The time of the session.</strong> Afternoon and evening efforts were affected, morning ones very little.</li>
</ul>
<p>A client who got up at 5 a.m. and comes in at 7 p.m. is in a different situation from one who went to bed late and comes in at 8 a.m. These averages still don't predict their session: see how they respond to the warm-up before you change anything.</p>

<h2>How do you track training load without equipment?</h2>
<p>Have the client rate their effort from 0 to 10 after the session and multiply that rating by the duration: that is session RPE. Example calculation: 60 minutes rated 7 gives 420 units. Foster and colleagues evaluated it in 2001 against a heart-rate-based method and found it valid across varied efforts. Add up the sessions, including exercise done without you, then compare the weeks with each other.</p>
<p>This score describes what the client felt. Your loads, sets and distances describe what they did. For the same work, a perceived effort that climbs over several sessions deserves a question. Leave aside the acute:chronic workload ratio for injury prevention, though: Impellizzeri and colleagues concluded in 2020 that no evidence supports that use.</p>

<h2>How reliable are smartwatches and HRV?</h2>
<p>Read them as trends, with known limits.</p>
<ul>
<li><strong>Sleep.</strong> In Chinoy and colleagues (2021), seven consumer devices of the time, worn or placed near the bed and compared with polysomnography in 34 healthy young adults, detected sleep well (sensitivity of at least 0.93) and wakefulness less well (specificity of 0.18 to 0.54). Sleep stages were inconsistent, and disrupted nights were measured less well. Ignore one night's "deep sleep" number.</li>
<li><strong>Heart rate variability.</strong> According to the meta-analysis by Bellenger and colleagues (2016, 27 studies), it rises at rest when adaptation is positive and changes little with overreaching. A low value doesn't prove overtraining, and a normal value doesn't rule it out. These studies cover endurance athletes, far from the average client.</li>
<li><strong>Measurement.</strong> <a href="/methode/variabilite-cardiaque.html">Heart rate variability</a> depends on the sensor, how the watch is worn, irregular heartbeats or a medication that slows the heart. You can't compare it from one device to another.</li>
<li><strong>Reference point.</strong> Only the client's own <a href="/methode/ligne-de-base.html">baseline</a>, built over several weeks, means anything. It shows whether they are drifting from their habits, without saying whether those habits are good, and a slow drift can slip past it.</li>
<li><strong>Recovery scores.</strong> They summarize these signals, limits included. A low score forbids nothing, and a high score authorizes nothing.</li>
</ul>
<p>This data belongs to the client. They show it to you if they want to, with their explicit consent, and you pass it on to no one without them. Never make the session depend on that sharing. If you work in the EU or the UK, health data is specially protected.</p>

<h2>When should you adjust a session, and when should you refer to a doctor?</h2>
<p>Look for convergence: you watch a single signal and act on several.</p>
<div class="tablewrap"><table>
<caption>Source: cautious benchmarks from this guide, with no diagnostic value.</caption>
<thead><tr><th>What you observe</th><th>Possible decision</th></tr></thead>
<tbody>
<tr><td>Short night, decent energy, good warm-up</td><td>Planned session</td></tr>
<tr><td>Short night and low energy, afternoon or evening session</td><td>Less volume, no maximal load</td></tr>
<tr><td>Perceived effort rising over several sessions</td><td>Lighter week, look for the cause with the client</td></tr>
<tr><td>Pain that changes the movement</td><td>Remove the exercise, medical advice if it persists</td></tr>
<tr><td>Unusual fatigue that lasts despite a lighter load</td><td>Refer to a doctor</td></tr>
<tr><td>Faintness, chest pain, abnormal breathlessness, palpitations</td><td>Stop immediately, see a doctor, and in an emergency call your local emergency number (911 in the US, 999 or 112 in the UK and Europe)</td></tr>
</tbody>
</table></div>
<p>You don't have to name what is going on. "Overtraining" and "deficiency" are medical conclusions. Describe what you observe, suggest a consultation, and carry the trends into your <a href="/coachs/bilan-mensuel-client-coaching.html">monthly report</a>.</p>

<h2>Key takeaways</h2>
<ul>
<li>Three rated questions at each session already give you the essential: the gap from the client's normal.</li>
<li>Sleep, load, smartwatch and heart rate variability are read together and as trends. None is enough alone.</li>
<li>You adjust the session and you don't diagnose: a new symptom or lasting fatigue belongs with a doctor.</li>
</ul>
""",
        "faq": [
            {"q": "How do you know if a client is too tired to train?", "a": "Ask how they slept, how much energy they have and whether they have new pain, then watch how they respond to the warm-up. If several signals drop, lighten the session. If the fatigue lasts or comes with symptoms, refer them to a doctor."},
            {"q": "Should you cancel a session after a bad night's sleep?", "a": "Not necessarily. A short night lowers performance on average, especially in the afternoon or evening and after an early wake-up, but the response varies from person to person. Keep the session if the client responds well to the warm-up, and reduce volume or intensity if not."},
            {"q": "Does low HRV mean overtraining?", "a": "No. Results are contradictory and, according to a 2016 meta-analysis in endurance athletes, resting HRV changes little with overreaching. A single drop can come from a bad night or a less clean measurement. Read the trend, along with how the client feels."},
        ],
        "sources": [
            {"t": "Saw AE, Main LC, Gastin PB. Monitoring the athlete training response: subjective self-reported measures trump commonly used objective measures: a systematic review. <em>Br J Sports Med</em>. 2016.", "u": "https://doi.org/10.1136/bjsports-2015-094758"},
            {"t": "Craven J, McCartney D, Desbrow B, et al. Effects of Acute Sleep Loss on Physical Performance: A Systematic and Meta-Analytical Review. <em>Sports Med</em>. 2022.", "u": "https://doi.org/10.1007/s40279-022-01706-y"},
            {"t": "Foster C, Florhaug JA, Franklin J, et al. A new approach to monitoring exercise training. <em>J Strength Cond Res</em>. 2001.", "u": "https://pubmed.ncbi.nlm.nih.gov/11708692/"},
            {"t": "Impellizzeri FM, Tenan MS, Kempton T, Novak A, Coutts AJ. Acute:Chronic Workload Ratio: Conceptual Issues and Fundamental Pitfalls. <em>Int J Sports Physiol Perform</em>. 2020.", "u": "https://doi.org/10.1123/ijspp.2019-0864"},
            {"t": "Chinoy ED, Cuellar JA, Huwa KE, et al. Performance of seven consumer sleep-tracking devices compared with polysomnography. <em>Sleep</em>. 2021.", "u": "https://doi.org/10.1093/sleep/zsaa291"},
            {"t": "Bellenger CR, Fuller JT, Thomson RL, et al. Monitoring Athletic Training Status Through Autonomic Heart Rate Regulation: A Systematic Review and Meta-Analysis. <em>Sports Med</em>. 2016.", "u": "https://doi.org/10.1007/s40279-016-0484-2"},
        ],
    },
]
