# -*- coding: utf-8 -*-
# English adaptations of the software guides in tools/coachs/batch_i.py and batch_j.py
# (see tools/en/_brief-coachs.md).
# Not adapted on purpose: meilleures-applications-coach-sportif and hexfit-everfit-my-pt-hub-avis.
# Both rest on French-language availability, French store ratings and tools sold mainly in France.

ENTRIES = [
    {
        "fr": "logiciel-coach-sportif-comment-choisir",
        "slug": "how-to-choose-personal-trainer-software",
        "title": "Personal trainer software: how to choose",
        "description": "How to choose personal trainer software: what to test on support, cancellation, the client app, data export, nutrition and intake forms before you pay.",
        "body": """
<p>The short answer: to choose <strong>personal trainer software</strong>, judge six things first: support, how the vendor bills you and lets you leave, the app your client will have to open, your data export, nutrition tracking and intake documents. Price comes next, because a cheaper subscription does not make up for a painful cancellation or an app your clients ignore. No software wins everywhere: look for the one that holds up on the points your business leans on most.</p>

<h2>How do you test software support during a free trial?</h2>
<p>A promise on a homepage proves nothing. Use the trial to send two real questions: a simple one and an awkward one, such as “How do I export a client with their full history?” Note three things: the response time, the language, and whether the answer actually deals with your question. Try again on an evening or a weekend, since that is often when you build your programs.</p>
<p>Ask how the vendor warns you about outages and whether it publishes a response time. Then read recent reviews, especially the bad ones, and look for the complaint that keeps coming back. The full method is in our guide on <a href="/coachs/verifier-logiciel-coaching-avant-de-choisir.html">what to check before you choose</a>.</p>

<h2>What should you ask about billing and cancellation?</h2>
<p>Before you enter your card, get these answers in writing:</p>
<ul>
<li><strong>Commitment:</strong> monthly or annual, renewal date, refund or not if you stop partway through.</li>
<li><strong>Cancellation:</strong> from your account, or by email with notice? What do your clients see the next day?</li>
<li><strong>Tiers:</strong> what do you pay for the next client, and can you move back down if you lose some?</li>
<li><strong>Add-ons:</strong> nutrition, payments, automations, an app under your own name: included or extra?</li>
<li><strong>Commission:</strong> does the vendor take a percentage on top of your payment provider?</li>
</ul>
<p>Watch out for one misleading reflex. Where consumer law makes canceling easy, it usually protects consumers, and when you subscribe for your business, you are buying as a professional. Do not count on it: read the vendor's terms, including the governing law if the vendor is based abroad.</p>
<p>Then work out the real cost at the number of clients you expect in six months, add-ons included, plus any sales tax you cannot recover. If the software issues your invoices, ask for a sample: do not assume it shows what your local rules require.</p>

<h2>What should you look for in the client app and nutrition tracking?</h2>
<p>Your client will judge the tool on their phone. Create a test account and live a week on their side: install or simple link, your clients' language, iPhone and Android, time needed to log a session. See also what they keep if they stop working with you. This point deserves its own test, described in our guide on <a href="/coachs/application-suivi-client-coach.html">what your clients actually use</a>.</p>
<p>For nutrition, check whether the module is included, whether the food database covers the products sold in your country, and whether your client can log a meal without spending ten minutes on it. A meal-plan module does not change what you are allowed to advise: the more personalized the advice, the higher the risk, especially when a medical condition is involved.</p>

<h2>What happens to your data and intake documents?</h2>
<p>The most useful test takes ten minutes: during the trial, export one full client. If you work in the EU or the UK, clients can ask you for their data in a reusable format, and formats such as CSV or JSON fit that request better than a PDF or an image. Without an export, you face that request alone, and you are stuck the day you want to change tools.</p>
<p>The vendor that hosts your client records generally processes that data on your behalf. If the GDPR applies to you, a contract with mandatory terms must then bind you both, and it is expected to cover deleting or returning the data at the end of the service. So ask for the vendor's data processing terms, where the data is hosted, the list of its subprocessors, and whether it uses the data for its own purposes.</p>
<p>On intake, check that you can create your own forms, collect separate consent for health data and find the signed version again. One trap: the PAR-Q+ cannot be built into software freely. Its terms of use, read on October 31, 2026, require prior written permission to integrate it into software, so ask the vendor whether it has that permission (see our guide on the <a href="/coachs/questionnaire-sante-avant-le-sport-client.html">health questionnaire</a>).</p>
<p>A waiver copied from a template found online does not guarantee protection either. Check the rules where you work: qualification, insurance and consumer law vary by country.</p>
<p>This guide is for information and does not replace a lawyer's advice.</p>

<h2>Key takeaways</h2>
<ul>
<li>Test support, export and the client app during the trial, with real questions and a real phone.</li>
<li>Get written confirmation of the commitment, cancellation, add-ons and what happens to your data when the contract ends.</li>
<li>Compare prices last, at your target client count, with add-ons and any tax you cannot recover.</li>
</ul>
""",
        "faq": [
            {
                "q": "What software should a personal trainer use?",
                "a": "No software suits every coach. Start from your business: in-person or remote, target client count, need for nutrition and payments. Then test support, export and the client app during the trial, and compare prices last.",
            },
            {
                "q": "Does coaching software work in my clients' language?",
                "a": "It depends on the tool, so check both sides, because your coach dashboard and your client's app are not always translated the same way. Check the support language too by writing to the vendor during the trial.",
            },
            {
                "q": "What happens to my data if I leave a coaching platform?",
                "a": "That depends on your contract with the vendor. Under the GDPR, the data is meant to be deleted or returned at the end of the service. Read this point before you subscribe, and export one full client during the trial to see what you get back.",
            },
        ],
        "sources": [
            {"t": "CNIL (French data protection authority). Controllers and processors: 6 good practices to respect personal data. 2020. In French.", "u": "https://www.cnil.fr/fr/responsable-de-traitement-et-sous-traitant-6-bonnes-pratiques-pour-respecter-les-donnees"},
            {"t": "CNIL. Processing on behalf of a controller: sample clauses. 2017. In French.", "u": "https://www.cnil.fr/fr/sous-traitance-exemple-de-clauses"},
            {"t": "CNIL. Businesses: how to respond to a data portability request. In French.", "u": "https://www.cnil.fr/fr/respecter-les-droits-des-personnes/professionnels-comment-repondre-une-demande-de-droit-la-portabilite"},
            {"t": "PAR-Q+ Collaboration. Terms and conditions. Read October 31, 2026.", "u": "https://eparmedx.com/terms-and-conditions/"},
        ],
    },
    {
        "fr": "application-coach-sportif-gratuite-ou-payante",
        "slug": "free-or-paid-coaching-app",
        "title": "Coaching app for personal trainers: free or paid?",
        "description": "Free or paid coaching app? The real limits of free plans for personal trainers, what they leave out, and the point where paying starts to make sense.",
        "body": """
<p>The short answer: a <strong>free coaching app for personal trainers</strong> works for testing a tool or following your very first clients. On the official pages checked on October 31, 2026, the two free plans cited here stop at 1 and 5 clients, and paid plans keep items such as consultation forms, integrated payments or a meal plan add-on. The decision turns on what you lose and on your ability to leave with your data. The small monthly saving comes after that.</p>

<h2>How far does a free plan go?</h2>
<p>The cap is counted in clients, sometimes in usage too. Here are two examples, in alphabetical order, with the same criteria for each. They are neither a ranking nor a full list, and they say nothing about the quality of these tools.</p>
<div class="tablewrap"><table>
<caption>Source: vendors' official pages, checked on October 31, 2026. Temporary trials excluded.</caption>
<thead><tr><th>Software</th><th class="n">Clients on the free plan</th><th>Examples reserved for paid plans</th></tr></thead>
<tbody>
<tr><td>Everfit</td><td class="n">5</td><td>Meal plans and recipes add-on</td></tr>
<tr><td>Trainerize</td><td class="n">1</td><td>Consultation forms, integrated payments</td></tr>
</tbody>
</table></div>
<p>The cap and the contents vary from one tool to another: choose based on what you want to test.</p>
<p>Two reading traps. A permanent free plan is a different thing from a 14-day or 30-day trial, which stops on a fixed date. And a pricing page can change without notice, or contradict itself from one block to the next: if a point matters to you, have the vendor confirm it the day you sign up.</p>

<h2>What do you lose on a free plan?</h2>
<ul>
<li><strong>Intake documents:</strong> without forms, you handle the questionnaire and consent elsewhere, in a second tool you will also have to secure.</li>
<li><strong>Payments:</strong> you invoice and chase by hand. With two or three clients, that stays manageable.</li>
<li><strong>Nutrition:</strong> it varies a lot from one tool to another. Read the details, because a “nutrition tracking” line can mean a simple log or a full module.</li>
<li><strong>Support:</strong> ask what is included on the free plan, through which channel and how fast. Your first setup is often when you need it most.</li>
</ul>
<p>None of this rules out a free plan. You just need to know what it covers before you put a paying client on it.</p>

<h2>Does free mean no risk for client data?</h2>
<p>Price does not change your responsibility: you remain responsible for your client records, even on a free plan. If you work in the EU or the UK, a provider that handles data on your behalf is your processor under the GDPR, with a contract to match. If it uses the data for its own purposes, it becomes responsible for that specific use. A free plan exists first to move you to a paid one, which is legitimate, but your data deserves the same questions as anywhere else:</p>
<ul>
<li>Does the vendor use your clients' data for its own purposes?</li>
<li>Where is the data hosted, and who else can access it?</li>
<li>Can you export it from the free plan, in a reusable format such as CSV?</li>
<li>What happens to your account and your clients' history if you leave, or if the plan disappears?</li>
</ul>
<p>If you work in the EU or the UK, health data is specially protected, on free and paid plans alike.</p>

<h2>When does it make sense to pay for a coaching app?</h2>
<p>No official threshold exists. Three signals beat a client count:</p>
<ol>
<li><strong>The cap blocks a signup.</strong> One more client should not have to wait because your tool is full.</li>
<li><strong>You copy by hand what a paid plan would do:</strong> forms, payments, reminders. Our guide on <a href="/coachs/excel-whatsapp-logiciel-coaching.html">Excel, WhatsApp and PDFs</a> shows how to measure that time.</li>
<li><strong>A specific feature gives you back time or prevents a mistake</strong>, and you can say which one.</li>
</ol>
<p>Example calculation: a subscription at €30 a month for 6 clients comes to €5 per client per month. Add the add-ons you really need, then compare that figure with the time you get back. If you cannot name the gain, stay on the free plan.</p>
<p>Before you pay, run the tool with a real client and try an export. Switching later costs time, yours and your client's, and that cost can far exceed a month's subscription. To compare paid plans with each other, use our framework for <a href="/coachs/logiciel-coach-sportif-comment-choisir.html">choosing personal trainer software</a>.</p>

<h2>Key takeaways</h2>
<ul>
<li>A free plan is enough to test a tool and follow your first clients: the examples checked on October 31, 2026 stop at 1 and 5 clients.</li>
<li>Look at what it leaves out and what you can take with you: forms, payments, nutrition, export.</li>
<li>Move to a paid plan for a need you can name, after testing the tool with a real client.</li>
</ul>
""",
        "faq": [
            {
                "q": "Is there free software for personal trainers?",
                "a": "Yes. The two free plans checked in this guide on October 31, 2026 stop at 1 and 5 clients. Beyond that, or for some features such as forms, you need a paid plan. Reread the pricing page the day you sign up, because it can change.",
            },
            {
                "q": "Can you manage coaching clients for free?",
                "a": "Yes, at a very small scale, with a free plan or a spreadsheet. The limit comes quickly: client cap, forms and payments handled elsewhere, health data to protect. Measure the time it takes you before you decide to pay.",
            },
            {
                "q": "Is a free coaching app GDPR compliant?",
                "a": "Price says nothing about compliance. You remain responsible for your client records, free or not. Ask the vendor for its data processing terms, the hosting location, the export available and whether it uses the data for its own purposes.",
            },
        ],
        "sources": [
            {"t": "Everfit. Everfit's Meal Plan Generator. Official blog, 2026. Checked October 31, 2026.", "u": "https://blog.everfit.io/everfits-meal-plan-generator"},
            {"t": "ABC Trainerize. Pricing Plans. Checked October 31, 2026.", "u": "https://www.trainerize.com/pricing/"},
            {"t": "CNIL (French data protection authority). Controllers and processors: 6 good practices to respect personal data. 2020. In French.", "u": "https://www.cnil.fr/fr/responsable-de-traitement-et-sous-traitant-6-bonnes-pratiques-pour-respecter-les-donnees"},
        ],
    },
    {
        "fr": "excel-whatsapp-logiciel-coaching",
        "slug": "spreadsheets-vs-coaching-software",
        "title": "Excel, WhatsApp, PDF: when to switch to coaching software",
        "description": "Personal training management software: when to leave Excel, WhatsApp and PDFs. The signals to watch, the time to measure, and the limits for health data.",
        "body": """
<p>The short answer: move to <strong>personal training management software</strong> when your homemade system takes more time than it saves, or when a simple question sends you digging: who paid, who skipped their session, where is that health questionnaire. There is no official threshold in number of clients. Two measurements are enough to decide: your admin time over two weeks, and where your clients' health data is sitting.</p>

<h2>What do Excel, WhatsApp and PDFs do well?</h2>
<p>Do not throw out what works. A spreadsheet is flexible and stays under your control. A PDF opens anywhere, with no account to create. WhatsApp is something your client already opens, with no new tool to learn. With a few in-person clients whose sessions you log yourself, this trio can be enough. Taking out a subscription by reflex, to look more professional, solves nothing.</p>
<p>The limits show up with individual remote coaching. A PDF you have sent is frozen: to change one exercise, you send a new file, and nobody knows which version counts. The spreadsheet only holds what you copy into it. WhatsApp mixes Tuesday's time slot, a sore knee and a meal photo in the same thread. To structure this work, read our guide on <a href="/coachs/suivre-client-a-distance.html">coaching clients remotely without losing your evenings</a>.</p>

<h2>When does your homemade system cost too much?</h2>
<p>I found no serious data that sets this threshold for an independent coach. Measure yours: for two weeks, note the time you spend copying sessions, resending programs, chasing payments and hunting for information in your messages.</p>
<p>Example calculation: 20 minutes per client per week, across 10 clients, comes to 3 hours 20 minutes a week, or about 14 hours a month. If a tool gives you back half of that, you recover 7 hours, to compare with its real cost. If your figure is closer to 5 minutes per client, keep your spreadsheet.</p>
<p>Watch these signals too, which weigh as much as the math:</p>
<ul>
<li>You copy the same information in two places, and the two end up disagreeing.</li>
<li>You find out about a missed session at the next appointment.</li>
<li>Your <a href="/coachs/bilan-mensuel-client-coaching.html">monthly report</a> gets skipped because everything has to be rebuilt by hand.</li>
<li>You chase payments from memory.</li>
<li>A client told you about an injury, and you can no longer find the message.</li>
</ul>

<h2>Is WhatsApp safe for client health data?</h2>
<p>I found no rule aimed specifically at coaches in the data protection guidance I read, so nothing I can point to bans these tools. If you work in the EU or the UK, though, health data is specially protected and needs security to match, and a WhatsApp thread or an unprotected file is a poor fit for it.</p>
<p>Medical history, illnesses and treatments are health data by nature, and weight can become health data, especially combined with other measurements. Treat injuries and the health questionnaire the same way. As soon as this data enters your files:</p>
<ul>
<li><strong>Consent:</strong> ask for it explicitly, separately from your terms of sale, after saying what you collect and why.</li>
<li><strong>Records:</strong> even working alone, keep a record of what you process. Client management and sensitive data belong in it.</li>
<li><strong>Retention:</strong> set a period, and delete this data when you no longer need it, in principle at the end of the coaching relationship. Check everywhere: phone, computer, backups, chat threads.</li>
<li><strong>Protection:</strong> password on the file, locked phone, access limited to you.</li>
</ul>
<p>Software does not do any of this for you, and you remain responsible for your records. It does bring this data into one place, which makes these four habits simpler.</p>

<h2>How do you switch without breaking everything?</h2>
<ol>
<li><strong>Start small.</strong> Take your next two clients, and leave the others where they are while you break in the tool.</li>
<li><strong>Bring over what you need.</strong> For an active client: goals, latest loads, key measurements. The full history can wait.</li>
<li><strong>Set a channel rule.</strong> WhatsApp for a time change or a late arrival, the tool for health, sessions and reports. Tell your clients.</li>
<li><strong>Clean up.</strong> Delete the health data of former clients once the period you set has passed. Keep your invoices, and check the rules where you work: retention periods, insurance and consumer law vary by country.</li>
</ol>
<p>To find the tool, follow our framework for <a href="/coachs/logiciel-coach-sportif-comment-choisir.html">choosing personal trainer software</a>.</p>
<p>This guide is for information and does not replace a lawyer's advice.</p>

<h2>Key takeaways</h2>
<ul>
<li>No official threshold exists: measure your time over two weeks and watch the signals.</li>
<li>I found no coach-specific rule on WhatsApp or Excel, but these tools are a poor fit for health data.</li>
<li>Move in stages, starting with your new clients, and clean up your old files.</li>
</ul>
""",
        "faq": [
            {
                "q": "Can a personal trainer use WhatsApp with clients?",
                "a": "I found no rule aimed at coaches on this point in the guidance I read. WhatsApp stays practical for a time change or a late arrival. A thread like this is a poor fit for health data, though, such as an injury, a medical history or a treatment.",
            },
            {
                "q": "Is Excel enough to manage coaching clients?",
                "a": "With a few in-person clients, a password-protected spreadsheet can be enough. It hits its limits when you have to follow sessions remotely, copy the same information again and again, or find a client's history. Measure your time over two weeks to decide.",
            },
            {
                "q": "How many clients before you need coaching software?",
                "a": "There is no official threshold. The right marker is the time you spend on admin and where health data sits in your files. Example calculation: 20 minutes per client per week, across 10 clients, comes to about 14 hours a month.",
            },
        ],
        "sources": [
            {"t": "CNIL (French data protection authority). What is health data? In French.", "u": "https://www.cnil.fr/fr/quest-ce-ce-quune-donnee-de-sante"},
            {"t": "CNIL. The record of processing activities. In French.", "u": "https://www.cnil.fr/fr/RGPD-le-registre-des-activites-de-traitement"},
            {"t": "CNIL. Mobile health apps and personal data protection: the questions to ask. 2018. In French.", "u": "https://www.cnil.fr/fr/applications-mobiles-en-sante-et-protection-des-donnees-personnelles-les-questions-se-poser"},
            {"t": "CNIL. GDPR compliance: how to inform people and ensure transparency. In French.", "u": "https://www.cnil.fr/fr/conformite-rgpd-information-des-personnes-et-transparence"},
        ],
    },
    {
        "fr": "application-suivi-client-coach",
        "slug": "client-tracking-app",
        "title": "Client tracking app: what your clients actually use",
        "description": "Client tracking app for personal trainers: what clients actually use, what research says about self-monitoring, and how to test an app on your own clients.",
        "body": """
<p>The short answer: I found no independent statistics on which features of a <strong>client tracking app for personal trainers</strong> clients really use. Research still gives a solid lead: logging what you do and seeing your progress helps you reach your goals. The rest can be measured on your own clients, with a two-week test. So judge an app on today's session, quick logging and the link with you, before you read its feature list.</p>

<h2>What features do clients actually use?</h2>
<p>I found no independent study on coaching clients. The work I saw covers consumer fitness apps, a different use from yours. Be wary of percentages published by vendors: they describe their own users, with a method you do not know.</p>
<p>Start instead from what your client has to do each week. That gives you four actions to test:</p>
<ul>
<li><strong>See today's session</strong> as soon as they open the app, without searching.</li>
<li><strong>Log what they did</strong> in a few seconds, between two sets, with one hand.</li>
<li><strong>See their progress</strong> on what interests them: loads, reps, consistency, measurements.</li>
<li><strong>Message you</strong> in the same place, and get a reply.</li>
</ul>
<p>This list remains a hypothesis to check on your clients. Challenges, badges, recipes and habit reminders will please some people: it is up to you to see whether they help yours. Also spot what blocks a client before the first session: an account to create, a password, an app that is not in their language, an old phone, or a plain refusal to install one more app.</p>

<h2>Does logging workouts actually help clients?</h2>
<p>Harkin and colleagues pooled 138 trials and 19,951 people: interventions that have people monitor their progress improve goal attainment, with a moderate effect (0.40). The effect is stronger when the result is reported to someone or physically recorded. This meta-analysis does not cover exercise alone. Michie and colleagues, across 122 evaluations of healthy eating and physical activity interventions, found that self-monitoring explained the largest share of the differences between studies. Combined with at least one other self-regulation technique, it produced an effect of 0.42, against 0.26 for other interventions.</p>
<p>Three practical consequences. Logging has to be quick enough to survive a busy week. Your attention counts: a result reported to someone carries more weight, hence the value of a brief note on logged sessions and a <a href="/coachs/bilan-mensuel-client-coaching.html">monthly report</a> your client actually reads. And the app is not the only option: a client who dislikes screens can keep a paper logbook, since physical recording is part of what Harkin's meta-analysis measures.</p>

<h2>Should you sync a client's watch, sleep and weight data?</h2>
<p>Ask one question first: what will you do with this number next week? If the answer is nothing, leave sync off. On reliability, Chinoy and colleagues compared seven consumer devices with polysomnography in 34 adults: sleep detection was good, but sleep stages were inconsistent, and the devices did worse on disturbed nights. So read this data as a trend, as our article on <a href="/articles/montre-connectee-fiabilite-sommeil.html">smartwatch sleep accuracy</a> explains, and keep listening to how your client feels.</p>
<p>On the data side, if you work in the EU or the UK, health data is specially protected. A step count alone is not health data, but weight combined with steps or calorie intake gives an indication of someone's health. Apps for better sleep count among the wellness apps where explicit consent is required if health data is collected, so treat sleep as health data, out of caution.</p>
<p>Guidance I read for amateur sports clubs expects explicit consent when a connected device collects this data, and does not accept it as valid if refusing means giving up training. It does not address independent coaches, so the cautious choice is to offer sync as an option. Check the rules where you work: qualification, insurance and data protection law vary by country.</p>

<h2>How do you test an app on your clients?</h2>
<ol>
<li><strong>Pick two opposite volunteers:</strong> one comfortable with their phone, the other not, ideally one iPhone and one Android.</li>
<li><strong>Watch the first session.</strong> Note where it jams and how long it takes to log a set, without helping.</li>
<li><strong>Count over two weeks.</strong> Example calculation: 6 sessions logged out of 8 planned gives 75%. That figure holds only for your two testers and serves only to spot a blocker.</li>
<li><strong>Spot what never got opened.</strong> A feature nobody uses does not justify a more expensive tier.</li>
<li><strong>Ask three questions:</strong> what annoyed you, what did you do outside the app, and what would you miss if it disappeared?</li>
</ol>
<p>To organize daily follow-up, read our guide on <a href="/coachs/suivre-client-a-distance.html">coaching clients remotely</a>. For the rest of the choice, go back to our framework for <a href="/coachs/logiciel-coach-sportif-comment-choisir.html">choosing software</a>.</p>
<p>This guide is for information and does not replace a lawyer's advice.</p>

<h2>Key takeaways</h2>
<ul>
<li>I found no independent numbers on what clients use: your test on two clients will teach you more than a sales pitch.</li>
<li>Bet on fast logging and on your feedback: meta-analyses support progress monitoring, especially when it is reported or recorded.</li>
<li>Read wearable data as a trend and keep it optional, with explicit consent.</li>
</ul>
""",
        "faq": [
            {
                "q": "Which tracking app should I choose for my coaching clients?",
                "a": "The one your clients still open after two weeks. Test four actions on two volunteers: see today's session, log it fast, see their progress, message you. Then compare plans on the other criteria, such as support and export.",
            },
            {
                "q": "Do clients have to use their coach's app?",
                "a": "I found no text that requires it. If you work with an app, say so before the contract and keep a simple option for clients who refuse, such as a paper logbook. Guidance for amateur sports clubs rejects a consent where refusing blocks training. It does not cover independent coaches.",
            },
            {
                "q": "Are weight and sleep health data?",
                "a": "They can be, especially combined with other measurements. It is judged case by case. If in doubt, treat them as health data and ask for explicit consent, separate from your terms of sale.",
            },
        ],
        "sources": [
            {"t": "Harkin B, Webb TL, Chang BP, et al. Does monitoring goal progress promote goal attainment? A meta-analysis of the experimental evidence. Psychol Bull. 2016.", "u": "https://doi.org/10.1037/bul0000025"},
            {"t": "Michie S, Abraham C, Whittington C, et al. Effective techniques in healthy eating and physical activity interventions: a meta-regression. Health Psychol. 2009.", "u": "https://doi.org/10.1037/a0016136"},
            {"t": "Chinoy ED, Cuellar JA, Huwa KE, et al. Performance of seven consumer sleep-tracking devices compared with polysomnography. Sleep. 2021.", "u": "https://doi.org/10.1093/sleep/zsaa291"},
            {"t": "CNIL (French data protection authority). What is health data? In French.", "u": "https://www.cnil.fr/fr/quest-ce-ce-quune-donnee-de-sante"},
            {"t": "CNIL. Questions and answers on data protection in amateur sport. In French.", "u": "https://www.cnil.fr/fr/sport-amateur-hors-contrat/questions-reponses"},
            {"t": "CNIL. Mobile health apps and personal data protection: the questions to ask. 2018. In French.", "u": "https://www.cnil.fr/fr/applications-mobiles-en-sante-et-protection-des-donnees-personnelles-les-questions-se-poser"},
        ],
    },
    {
        "fr": "changer-logiciel-coaching",
        "slug": "how-to-switch-coaching-software",
        "title": "How to switch coaching software without losing clients",
        "description": "How to switch coaching software without losing clients: notice periods, data export, active payments and moving clients over in small groups, step by step.",
        "body": """
<p>The short answer: to <strong>switch coaching software</strong> without losing clients, export before you cancel, test the new tool with two or three willing clients, move the others in small groups, then shut down the old tool at its renewal date. The danger lies in the order of operations: at cancellation, accounts can be deactivated and payments can stop, or keep running.</p>

<h2>What should you check before you cancel?</h2>
<p>Three dates and one question. Note your renewal date, your notice period and the day your data disappears. Then find out what happens to your clients on the last day.</p>
<p>The answers vary a lot from vendor to vendor. According to its pricing page, checked on October 31, 2026, Trainerize moves the account to the free plan, deactivates clients beyond 1 and cancels recurring products. The My PT Hub contract (version dated November 19, 2025, read on October 31, 2026) says your clients lose access at the end, and that their recurring payments continue until you cancel them. Two opposite logics: read yours before you act.</p>
<p>Look at your plan too. If you pay annually, or if a commitment is still running, canceling too early will not necessarily save you money. The best move is often to time the switch to your renewal date.</p>

<h2>What data should you export, and in what format?</h2>
<p>First list what you really use: client records, current programs, load history, measurements, reports, invoices. Then look for what your contract says about leaving. Here are three examples from published contracts, one from My PT Hub and two from French vendors:</p>

<div class="tablewrap"><table>
<caption>Source: published terms, checked on October 31, 2026. Versions dated July 8, 2026 (AZEOO), March 23, 2026 (Gymkee) and November 19, 2025 (My PT Hub).</caption>
<thead><tr><th>Tool</th><th>Export provided</th><th>After the contract ends</th></tr></thead>
<tbody>
<tr><td>AZEOO</td><td>Athlete data, content and history, in a structured machine-readable format</td><td>Export possible for 30 days</td></tr>
<tr><td>Gymkee</td><td>Programs, exercises and client data, from the settings, provided the feature is available</td><td>Content kept for 30 days, then deleted</td></tr>
<tr><td>My PT Hub</td><td>Export or download on request</td><td>Request within 30 days, after that no obligation to keep the data</td></tr>
</tbody>
</table></div>

<p>If you work in the EU or the UK, the format expected for data portability is a reusable one such as CSV, JSON or XML, and PDFs and images are discouraged. That right belongs to your client, for the data they provided. With the vendor, you rely on your contract and on Article 28 of the GDPR: at the end of the service, the processor returns or deletes the data, at the choice of the controller. And the controller is you.</p>
<p>Open every exported file before you cancel. An export you never opened proves nothing.</p>

<h2>How do you move clients over without losing them?</h2>
<ol>
<li><strong>Ask the new tool what it brings over.</strong> Some vendors advertise a migration by their team. Get it in writing whether the history comes across, or only the programs.</li>
<li><strong>Prepare current programs.</strong> Start with your active clients. The archives can wait.</li>
<li><strong>Test with two or three willing clients.</strong> Choose clients who will tell you what jams: login, session, messages.</li>
<li><strong>Tell everyone in writing.</strong> Say what changes, what does not, the date and how to install the app.</li>
<li><strong>Move clients in small groups</strong>, ideally between two training blocks, so nobody changes tools in the middle of a preparation.</li>
<li><strong>Keep the old tool open</strong> until the renewal date, so you can go back or find a piece of data.</li>
</ol>
<p>Sample message to adapt: <em>“Starting March 1, your program moves to a new app. Your sessions and your rate stay the same. I'll send you the link the day before, and we'll go through it together at your next session.”</em></p>
<p>Timing matters as much as the tool. Avoid changing apps for a client who is coming back after a break or nearing a target date. Our guide on <a href="/coachs/fideliser-clients-coaching-sportif.html">client retention</a> looks at why clients stop.</p>

<h2>What should you do with active payments?</h2>
<p>This is the most sensitive step: a client charged twice, or not at all, costs you trust or money.</p>
<ul>
<li><strong>List your active subscriptions</strong>, with each client's next charge date.</li>
<li><strong>Ask both vendors</strong> whether subscriptions carry over, or whether each client will have to re-enter their card.</li>
<li><strong>Stop the old charge before you start the new one</strong>, client by client. With My PT Hub, the contract read on October 31, 2026 leaves this task to you: cancel the subscriptions or disconnect your payment account.</li>
<li><strong>Collect your invoices</strong> before the end. Check the rules where you work: record keeping, insurance and consumer law vary by country.</li>
</ul>
<p>Once the switch is done, update your records and what you tell clients, since the recipient of their data changes. Then ask the old vendor in writing to delete the data. Before signing with the new one, go through <a href="/coachs/verifier-logiciel-coaching-avant-de-choisir.html">the points to check before you choose</a>, so you do not relive the same exit.</p>
<p>This guide is for information and does not replace a lawyer's advice.</p>

<h2>Key takeaways</h2>
<ul>
<li>Export and check your files before you cancel: in the three contracts cited, read on October 31, 2026, everything happens within 30 days after the end.</li>
<li>Move clients in small groups and keep the old tool open until the renewal date.</li>
<li>Handle payments client by client: depending on the vendor, they stop or continue at cancellation.</li>
</ul>
""",
        "faq": [
            {
                "q": "How do you switch coaching software?",
                "a": "Note your renewal date and notice period, export your data, test the new tool with two or three willing clients, tell everyone in writing, move clients in small groups, handle payments client by client, then cancel the old tool at its renewal date.",
            },
            {
                "q": "Do you lose client history when you change software?",
                "a": "It depends on both vendors: what the old one lets you export, and what the new one can import. Some advertise a migration of the history, others only mention programs. Get this in writing before you cancel, and keep your export files.",
            },
            {
                "q": "How do I get my data back before canceling?",
                "a": "Look for the export feature in the settings and the exit clause in the contract. Several vendors provide 30 days after the end, sometimes on request, in the terms read on October 31, 2026. Export before you cancel, ask for a reusable format such as CSV, and open the files to check them.",
            },
        ],
        "sources": [
            {"t": "CNIL (French data protection authority). Businesses: how to respond to a data portability request. In French.", "u": "https://www.cnil.fr/fr/respecter-les-droits-des-personnes/professionnels-comment-repondre-une-demande-de-droit-la-portabilite"},
            {"t": "CNIL. Controllers and processors: 6 good practices to respect personal data. In French.", "u": "https://www.cnil.fr/fr/responsable-de-traitement-et-sous-traitant-6-bonnes-pratiques-pour-respecter-les-donnees"},
            {"t": "ABC Trainerize. Pricing. Checked October 31, 2026.", "u": "https://www.trainerize.com/pricing/"},
            {"t": "My PT Hub. Subscription Services Agreement. Version dated November 19, 2025, read October 31, 2026.", "u": "https://www.mypthub.net/legal/subscription-services-agreement/"},
            {"t": "Gymkee. Terms of use. Version dated March 23, 2026, read October 31, 2026. In French.", "u": "https://gymkee.com/fr/terms/"},
            {"t": "AZEOO. General terms, version 2.0 dated July 8, 2026, read October 31, 2026. In French.", "u": "https://azeoo.com/conditions-generales-utilisation-professionnel"},
        ],
    },
    {
        "fr": "verifier-logiciel-coaching-avant-de-choisir",
        "slug": "what-to-check-before-choosing-coaching-software",
        "title": "Support, cancellation, bugs: what to check before choosing software",
        "seo_title": "Coaching software: what to check before you choose",
        "description": "Coaching software reviews only go so far: how to test support, read cancellation terms, catch bugs and interpret ratings during your free trial.",
        "body": """
<p>The short answer: before you choose, <strong>check coaching software</strong> on four points during the trial: how support answers a real question, the written exit terms, how the app holds up on a client's phone, and what happens to your data. Reviews help, but a rating out of 5 answers none of these questions. All of this can be tested before you pay.</p>

<h2>How do you test support before you pay?</h2>
<p>Do not ask a demo question. Send two real questions during the trial, at two different times:</p>
<ul>
<li><strong>An exit question:</strong> “How do I export client records and history if I leave?” A precise answer tells you a lot.</li>
<li><strong>A field question:</strong> a real problem with a program, a payment or a client's login.</li>
</ul>
<p>Note the response time, the language and above all the quality: did they understand your situation, or did you get a generic link? Also check that this channel stays open once you subscribe. A response time shown on a website is a vendor's number: only your own test counts.</p>

<h2>What should you read in the contract before you commit?</h2>
<p>Read the FAQ, then the contract. Four examples show how much the terms vary, and none of them is the rule. One comes from My PT Hub, the other three from French vendors:</p>

<div class="tablewrap"><table>
<caption>Source: published terms and FAQs, checked on October 31, 2026. Versions dated July 8, 2026 (AZEOO), December 7, 2025 (Ekklo), March 23, 2026 (Gymkee) and November 19, 2025 (My PT Hub).</caption>
<thead><tr><th>Tool</th><th>How to leave</th><th>Notice or effect</th><th>Refund</th></tr></thead>
<tbody>
<tr><td>AZEOO (Essential, Professional)</td><td>By email</td><td>One month's notice</td><td>No proration for the current period</td></tr>
<tr><td>Ekklo</td><td>In 1 click according to its FAQ</td><td>Amounts due through the end of the commitment remain payable under its terms</td><td>None after activation, except a clear error by Ekklo</td></tr>
<tr><td>Gymkee</td><td>From the account settings</td><td>End of the current period</td><td>No proration</td></tr>
<tr><td>My PT Hub</td><td>Written notice of non-renewal</td><td>3 days before renewal on monthly plans, 30 days on annual plans</td><td>None. Early exit: the rest of the period is due</td></tr>
</tbody>
</table></div>

<p>Three reflexes. If the FAQ and the contract disagree, write to the vendor and keep the reply. If an annual price is billed monthly, ask whether you are committing for a year. If you want an app under your own name, look at the term: as of October 31, 2026, AZEOO asks for 24 months on Customized, and Gymkee for 12 or 24 months on Custom.</p>
<p>Do not count on consumer law to bail you out. A coach who subscribes for their business generally buys as a professional, so your contract comes first. Check the rules where you work: qualification, insurance and consumer law vary by country. If a clause worries you, ask a lawyer.</p>
<h3>What about your data?</h3>
<p>You remain responsible for your client records, even inside software. The vendor is generally your processor, and a contract should frame that role. Ask these questions in writing:</p>
<ul>
<li>If I work in the EU or the UK, is there a data processing agreement that meets Article 28 of the GDPR?</li>
<li>Where is the data hosted, and does it leave my country or region?</li>
<li>Can I export everything, client data included, in a reusable format?</li>
<li>What happens to the data when the contract ends?</li>
<li>How will I be told about a data breach?</li>
</ul>

<h2>How do you spot bugs before your clients do?</h2>
<p>Walk through your client's journey on real phones:</p>
<ol>
<li>Create a fake client and install the app on an iPhone and an Android, including an old phone if you can.</li>
<li>Run a full session: loads, video, timer, end of session, feedback to you.</li>
<li>Turn off the network mid-session, as in a basement gym, then see what was saved.</li>
<li>Send a message and a photo, and connect a watch if your clients wear one.</li>
<li>Look at the last update date in the app store and the release notes.</li>
</ol>
<p>Also ask the vendor how it announces outages and where it publishes its fixes.</p>

<h2>How do you read coaching software reviews?</h2>
<p>A useful review has three markers: the platform, the date, the number of reviews. Without them, a figure means nothing. A few reflexes:</p>
<ul>
<li><strong>Sort by date.</strong> A review from 2022 describes a different product. Read the last 12 months.</li>
<li><strong>Read low and middling ratings first.</strong> Look for what keeps coming back: billing, cancellation, an app that crashes.</li>
<li><strong>Ask who is talking.</strong> An app rating often comes from clients, not coaches.</li>
<li><strong>Check the country.</strong> On Google Play, the rating shown can change with the country you view it from, as seen on October 31, 2026.</li>
<li><strong>Keep your distance from testimonials.</strong> The ones on a vendor's site are chosen by the vendor.</li>
</ul>
<p>A percentage drawn from a few dozen reviews gives you a lead, never a truth about a whole market.</p>

<p>If you are already leaving a tool, follow the method for <a href="/coachs/changer-logiciel-coaching.html">switching software</a>.</p>
<p>This guide is for information and does not replace a lawyer's advice.</p>

<h2>Key takeaways</h2>
<ul>
<li>Test support with a real question during the trial, ideally about exporting your data.</li>
<li>Read the contract as well as the FAQ: notice, commitment, refunds and how your data leaves.</li>
<li>Walk through a full client journey on a real phone, and read recent reviews with their platform, date and number.</li>
</ul>
""",
        "faq": [
            {
                "q": "How do you know if coaching software is reliable?",
                "a": "Test it during the trial: a full session on a real phone, with the network cut partway through, and a real question to support. Look at the last update date in the app store, read recent reviews and ask how the vendor announces outages.",
            },
            {
                "q": "Can I cancel my coaching software at any time?",
                "a": "It depends on the contract. Some vendors let you cancel at any time with effect at the end of the paid period, others ask for notice, and an annual plan can commit you until the end of its term. Read the cancellation clause before you subscribe, because you are buying as a professional.",
            },
            {
                "q": "Where can I find reliable reviews of coaching software?",
                "a": "Cross-check several platforms, for example the App Store, Google Play and review sites for professionals. Always look at the date and number of reviews, and separate client ratings from coach ratings. Treat testimonials published by the vendor as marketing.",
            },
        ],
        "sources": [
            {"t": "AZEOO. General terms, version 2.0 dated July 8, 2026, read October 31, 2026. In French.", "u": "https://azeoo.com/conditions-generales-utilisation-professionnel"},
            {"t": "Ekklo. Terms of use. Version dated December 7, 2025, read October 31, 2026. In French.", "u": "https://www.ekklo.com/fr/legal/cgu"},
            {"t": "Gymkee. Terms of use. Version dated March 23, 2026, read October 31, 2026. In French.", "u": "https://gymkee.com/fr/terms/"},
            {"t": "My PT Hub. Subscription Services Agreement. Version dated November 19, 2025, read October 31, 2026.", "u": "https://www.mypthub.net/legal/subscription-services-agreement/"},
        ],
    },
]
