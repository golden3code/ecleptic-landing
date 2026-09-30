# -*- coding: utf-8 -*-
# English version of batch K (Training load long tail) — source: tools/satellites/batch_k.py.
# Sources are carried over automatically from the French entries.

ENTRIES = [
    {
        "fr": "charge-d-entrainement-c-est-quoi",
        "slug": "what-is-training-load",
        "title": "Training load: what is it and how do you measure it?",
        "description": "Training load is volume × intensity. External vs internal load, the minutes × perceived effort method and weekly tracking: how to measure it simply.",
        "body": """
<p>The short answer: <strong>training load</strong> is the dose of work you put your body through, roughly <strong>volume multiplied by intensity</strong>. The simplest way to measure it, with no equipment: <strong>session length in minutes × perceived effort rated out of 10</strong>. Add up your sessions for the week, and you finally know whether you're doing more, less or the same as before.</p>
<p>Why bother putting a number on it? Because your body doesn't count your miles or your sets: it absorbs a <em>dose</em>. Two one-hour sessions have nothing in common if one is an easy jog and the other is all-out intervals. And it's the balance between that dose and your recovery that decides whether you progress, stall or get injured.</p>

<h2>External vs internal training load: what's the difference?</h2>
<ul>
<li><strong>External load:</strong> what you did, measurable from the outside. Distance, duration, pace, watts, elevation gain — or, in the weight room, sets × reps × weight.</li>
<li><strong>Internal load:</strong> what it cost you. Your heart rate, how out of breath you got, your perceived effort: your body's response.</li>
</ul>
<p>The distinction is crucial, because the same external load doesn't always produce the same internal load. Your usual 10 km (6.2 miles), at the same pace, costs you far more after a 5-hour night, at 30 °C (86 °F) or in the middle of a crunch week. Life stress <a href="/articles/stress-recuperation-sport.html">draws on the same recovery budget</a> as your workouts. Internal load is what tells you what your body actually absorbed, and it's what triggers adaptations, as the researchers who formalized this distinction back in 2003 pointed out in 2019: it's the one to track first.</p>

<h2>How do you calculate training load simply?</h2>
<p>The most widely used method, from pro sports to recreational athletes, was proposed in 2001 by the team of American physiologist Carl Foster. It fits in one multiplication: <strong>duration in minutes × perceived effort for the session</strong>, from 1 to 10. It's called "session RPE," and the result is expressed in arbitrary units (AU). A 2017 review identified 36 studies confirming its validity and reliability, in children as well as adults, from recreational to elite level.</p>
<ul>
<li><strong>Tip:</strong> rate your effort about 30 minutes after the session, judging the whole session, not just the final sprint. That's the delay the method originally called for; a 2021 review also shows the rating stays stable anywhere from one minute to 14 days afterward.</li>
<li><strong>Tip:</strong> if you're unsure which number to give, the equivalents are laid out in <a href="/articles/rpe-echelle-effort-percu.html">the perceived exertion scale</a>.</li>
<li><strong>Tip:</strong> the method works for every sport, so you can add running, cycling and strength training into a single total.</li>
</ul>
<p>Example over one week: a 45-minute easy run at 3 (135 AU), a 60-minute strength session at 7 (420 AU), a 50-minute interval session at 8 (400 AU), a 90-minute long run at 5 (450 AU). Total: <strong>1,405 AU</strong>. That number means nothing in absolute terms; its only use is to compare you with yourself.</p>
<p>Your watch may already calculate a load score from your heart rate. Same logic: time spent × cardiac intensity. It's relevant for endurance, much less so for strength training, where your heart poorly reflects the effort you're putting in. The minutes × perceived effort method works everywhere.</p>

<h2>How to track your training load over the week</h2>
<p>The right time frame is the week. A single session doesn't say much: it's the accumulation that tires you out, and it's the accumulation that makes you progress. Three things to look at:</p>
<ul>
<li><strong>The total:</strong> stable, rising gently or rising sharply compared with previous weeks?</li>
<li><strong>The spikes:</strong> a week well above your recent average is the classic injury scenario. According to the International Olympic Committee consensus statement (2016), poorly managed load, rapid increases included, is a major risk factor for injury. The <a href="/articles/ratio-charge-aigue-chronique.html">acute:chronic workload ratio</a> is designed precisely to spot these spikes.</li>
<li><strong>The distribution:</strong> a week where every day looks the same, always moderately hard, is more tiring than it seems. As early as 1998, Carl Foster observed in 25 athletes that a good share of minor illnesses occurred when their load, multiplied by its monotony, exceeded an individual threshold. Alternating truly hard days with truly easy days helps your body absorb the work.</li>
</ul>
<p>To progress, load has to rise over time — that's the principle of <a href="/articles/surcharge-progressive-comment-progresser.html">progressive overload</a> — but in small steps, broken up by lighter weeks.</p>

<h2>How do you know if your training load is too high?</h2>
<p>The number alone won't tell you: 2,000 AU can be an easy week for a marathoner and a wall for someone getting back into training. What matters is how you respond. The signs that your load is outpacing your recovery:</p>
<ul>
<li><strong>Usual sessions that feel harder</strong>, at the same pace or the same weight.</li>
<li>A <strong>resting heart rate that creeps up</strong> several mornings in a row, and sleep that gets worse.</li>
<li><strong>Localized pain that keeps coming back</strong> every session, in a tendon or a bone.</li>
</ul>
<p>When these signals light up, cut your load for a few days, sleep more and build back up more gradually. Pinpoint bone pain that gets worse with exercise, swelling or a limp, on the other hand, are not something to manage on your own: see a doctor.</p>

<h2>Key takeaways</h2>
<ul>
<li>Training load is volume × intensity: the real dose your body has to absorb.</li>
<li>External load tells you what you did, internal load what it cost you: track the second one above all.</li>
<li>Simple method: minutes × perceived effort out of 10, added up over the week and compared with your previous weeks.</li>
</ul>
""",
        "faq": [
            {"q": "What is training load in sports?",
             "a": "It's the dose of work imposed on the body, combining volume (duration, distance, sets) and intensity (pace, weight, effort). There's external load, what you did, and internal load, what it cost you physiologically."},
            {"q": "What's the difference between training volume and intensity?",
             "a": "Volume measures the amount of work: minutes, kilometers or miles, sets. Intensity measures how hard it is: pace, percentage of your maximum weight, perceived effort. Training load combines the two, because an easy hour and an all-out hour don't weigh the same at all."},
            {"q": "Is the training load calculated by a watch reliable?",
             "a": "For endurance, it's a good benchmark, because it's based on your heart rate during exercise. In strength training or very short efforts, your heart poorly reflects the effort you're putting in, and the duration × perceived effort method is more accurate. Either way, compare yourself with yourself, never with someone else's numbers."},
        ],
    },
    {
        "fr": "ratio-charge-aigue-chronique",
        "slug": "acute-chronic-workload-ratio",
        "title": "Acute:chronic workload ratio: the injury-prevention metric",
        "description": "The acute:chronic workload ratio compares your week with your last 4. Safe zone of 0.8 to 1.3, spikes above 1.5 to avoid, and the metric's limitations.",
        "body": """
<p>The short answer: the <strong>acute:chronic workload ratio</strong> compares your training load for the <strong>current week</strong> with your <strong>weekly average over the last 4 weeks</strong>. Around 1, you're doing roughly what your body is used to. The zone generally considered safe runs from <strong>0.8 to 1.3</strong>; above about <strong>1.5</strong>, you're spiking in a way your tissues haven't had time to prepare for, and several studies in team sports link that to more injuries.</p>
<p>The idea is powerful because it shifts the question. What gets you hurt isn't so much training a lot as training <strong>a lot more than usual, all at once</strong>. An important caveat: it's a useful metric, not a law of physics, and it's seriously debated in the scientific literature. More on that below.</p>

<h2>How do you calculate the acute:chronic workload ratio (ACWR)?</h2>
<p>You need a load measure, always the same one: kilometers, hours, sets, or better yet, the duration × perceived effort load explained in <a href="/articles/charge-d-entrainement-c-est-quoi.html">how to measure your training load</a>. Then:</p>
<ul>
<li><strong>Acute load:</strong> the total for the last 7 days. It's the fatigue you're carrying right now.</li>
<li><strong>Chronic load:</strong> the weekly average over the last 4 weeks. It's the load your body is prepared for.</li>
<li><strong>Ratio:</strong> acute divided by chronic.</li>
</ul>
<p>Example for a runner: 28, 30, 32 and 30 km over the previous four weeks, an average of 30 km (about 19 miles). A 36 km week gives a ratio of 1.2: you're progressing without forcing it. A 45 km week gives 1.5: that's a spike. Depending on the version of the calculation, the current week is included in the average or not; leaving it out makes spikes more visible.</p>

<h2>What ACWR should you aim for to avoid injury?</h2>
<p>These benchmarks come from a 2016 review by Australian researcher Tim Gabbett: 0.8 to 1.3 is the "sweet spot"; 1.5 or more is the "danger zone."</p>
<ul>
<li><strong>Below 0.8:</strong> you're doing clearly less than usual. Not the riskiest scenario, but already outside the sweet spot: your fitness erodes, and getting back into it will create an even sharper spike.</li>
<li><strong>0.8 to 1.3:</strong> the safe zone. Your load is changing at a pace your body can keep up with.</li>
<li><strong>1.3 to 1.5:</strong> caution. Acceptable once in a while, for a training camp or a heavy week, not week after week.</li>
<li><strong>Above 1.5:</strong> the spike to avoid. In the first study on the subject, in 28 elite cricket fast bowlers, a ratio of 1.5 or more came with a 2 to 4 times higher risk of injury in the following 7 days.</li>
</ul>
<p>The other lesson from this research, often forgotten: a <strong>high chronic load, built up gradually</strong>, seems to protect rather than expose you. In 53 professional rugby league players followed over two seasons (2016), those with a high chronic load were more resistant to injury as long as the ratio stayed between 0.85 and 1.35, but became more vulnerable to spikes around 1.5. The runner who has patiently built up to 50 km (31 miles) a week can handle a long run that someone running 15 couldn't. Volume isn't the enemy; a step that's too high is.</p>

<h2>Why do people so often get injured when they return to training?</h2>
<p>It's the most common scenario among recreational athletes. Two or three weeks off make your chronic load melt away. If you jump straight back to your previous volume, your ratio shoots up, even if the week feels "normal" to you. Same logic after an injury or an illness: start lower, then build back up in stages, as explained in <a href="/articles/reprendre-le-sport-apres-maladie.html">returning to exercise after an illness</a>. In running, the <a href="/articles/regle-des-10-pourcent-course.html">10% rule</a> pursues the same goal with a more rough-and-ready calculation.</p>

<h2>What are the limitations of the acute:chronic workload ratio?</h2>
<p>Let's be honest: the metric has been heavily criticized, and rightly so on several points.</p>
<ul>
<li><strong>Association isn't causation:</strong> the studies are observational, often conducted in professional athletes. In 2020 and again in 2021, researcher Franco Impellizzeri's team concluded that no data justify steering training with this ratio to reduce injuries, and that it offers almost no predictive power. In 5,205 recreational runners followed for 18 months (2025), its spikes weren't linked to more injuries; a single run much longer than usual, on the other hand, was.</li>
<li><strong>The calculation changes the result:</strong> simple or weighted average, current week included or not. The same history can produce different ratios.</li>
<li><strong>It becomes unstable at low volume:</strong> if you run 10 km a week, one extra run makes the ratio jump without the real risk changing much.</li>
<li><strong>It ignores the type of load:</strong> 10 km of downhill trail running or sprints don't stress your tissues like 10 km of easy jogging. It also ignores your sleep, your stress and your injury history.</li>
</ul>
<p>So use it as a <strong>guardrail</strong>, not an oracle: excellent for spotting an abnormal week, unable to predict an injury on its own. Cross-check it with how you feel and your morning vitals, which is what a <a href="/articles/readiness-score-comment-ca-marche.html">readiness score</a> does. And if a specific pain settles into a bone or a tendon, the ratio doesn't matter: the pain is what counts.</p>

<h2>Key takeaways</h2>
<ul>
<li>The ratio compares your current week with your average over the last 4: between 0.8 and 1.3, you're in the safe zone.</li>
<li>Avoid spikes above 1.5, especially when coming back from a break, when your chronic load has melted away.</li>
<li>It's a useful but debated metric: a guardrail to cross-check with how you feel, not a prediction.</li>
</ul>
""",
        "faq": [
            {"q": "What is the ACWR in sports?",
             "a": "The ACWR, or acute:chronic workload ratio, compares your training load for the week with your average load over the last 4 weeks. It's used to spot sudden increases, which are linked to more injuries. The zone often considered safe runs from 0.8 to 1.3."},
            {"q": "What should I do if my workload ratio goes above 1.5?",
             "a": "Go lighter over the following days to bring your load back toward your recent average, cutting the most intense sessions first. Keep an eye on how you feel and on any localized pain. A single spike doesn't guarantee an injury, but it justifies a calmer week afterward."},
            {"q": "Does the acute:chronic workload ratio really predict injuries?",
             "a": "Not on its own. It spots load spikes, linked to more injuries in several team-sport studies, but it remains debated: the calculation varies, the data come mostly from professional sports, it's unstable at low volume, and the link was absent in a large cohort of recreational runners. It's a guardrail, not a prediction."},
        ],
    },
    {
        "fr": "rpe-echelle-effort-percu",
        "slug": "rpe-rate-of-perceived-exertion",
        "title": "RPE scale: how to use perceived exertion in your workouts",
        "description": "The RPE scale rates effort from 1 to 10: how it maps to breathing and talking, reps in reserve (RIR) for lifting, and how to use it to dose your workouts.",
        "body": """
<p>The short answer: <strong>RPE</strong> (<em>rating of perceived exertion</em>) is a score from <strong>1 to 10</strong> that you give your effort: 1 is close to resting; 10 is your absolute max. A simple benchmark: if you can <strong>hold a conversation</strong>, you're around 3-4; if you can only get out <strong>a few words</strong>, you're around 7-8. In strength training, it translates into <strong>reps in reserve</strong>: an RPE 8 is a set stopped 2 reps short of failure.</p>
<p>It seems too simple to be serious. Yet it's one of coaches' favorite tools, because it measures what no sensor fully captures: what the effort costs you <em>today</em>, with your sleep, your stress and your fatigue of the moment.</p>

<h2>How do you read the 1-to-10 perceived exertion scale?</h2>
<p>There are several versions — the oldest, the Borg scale, runs from 6 to 20 — but the 1-to-10 version has become the most practical. The equivalents:</p>
<ul>
<li><strong>1-2:</strong> very easy. A relaxed walk, active recovery. You could sing.</li>
<li><strong>3-4:</strong> easy. You're breathing a bit harder but can hold a full conversation: the territory of easy endurance work and <a href="/articles/zone-2-cardio-cest-quoi.html">zone 2</a>.</li>
<li><strong>5-6:</strong> moderate. You speak in short sentences, your breathing becomes audible. Sustainable for a long time, but it takes focus.</li>
<li><strong>7-8:</strong> hard. A few words at a time, heavy breathing. Threshold pace, long intervals, heavy sets.</li>
<li><strong>9:</strong> very hard. Talking becomes impossible, and you can only sustain the effort briefly.</li>
<li><strong>10:</strong> maximal. You have nothing more to give.</li>
</ul>
<p>The World Health Organization's 2020 guidelines use the same benchmarks: moderate activity generally corresponds to 5 or 6 out of 10, vigorous activity to 7 or 8.</p>

<h2>What is RIR in strength training?</h2>
<p><strong>RIR</strong> (<em>reps in reserve</em>) is the number of reps you could still have done at the end of a set, with clean technique. It gives RPE a concrete reference under the bar. This correspondence was proposed and tested in 2016 in 29 squatters, both beginners and experienced lifters:</p>
<div class="tablewrap"><table>
<caption>Source: Zourdos et al. (2016).</caption>
<thead><tr><th>RPE</th><th class="n">Reps in reserve (RIR)</th></tr></thead>
<tbody>
<tr><td>RPE 10: couldn't do one more rep</td><td class="n">0</td></tr>
<tr><td>RPE 9</td><td class="n">1</td></tr>
<tr><td>RPE 8</td><td class="n">2</td></tr>
<tr><td>RPE 7</td><td class="n">3</td></tr>
</tbody>
</table></div>
<p>That's exactly the useful zone for building muscle: sets finished 0 to 3 reps short of failure, whatever your rep range (the details are in <a href="/articles/combien-de-repetitions-pour-prendre-du-muscle.html">how many reps to build muscle</a>). Meta-regressions published in 2024 show that muscle growth increases the closer to failure you end your sets, while strength gains vary little.</p>
<p>One trap to know about: almost everyone gets it wrong in the same direction, beginner or experienced. According to a 2022 meta-analysis (12 studies, 414 participants), people underestimate on average by about one rep how many they have left before failure, and the error grows on long sets, beyond 12 reps. To calibrate yourself, occasionally take a last set all the way on a low-risk exercise — leg press, machine, curls — and compare with your estimate. Avoid this test on the squat or bench press without a spotter.</p>

<h2>RPE or heart rate: which should you trust?</h2>
<p>Both, for different reasons. Heart rate is objective, but slow to respond, affected by heat, caffeine or dehydration, and nearly silent during a set of squats. RPE takes everything into account: muscle fatigue, breathing, mental state. That's both its strength and its weakness, because it also shifts with your mood or the music in your earbuds.</p>
<p>The most valuable signal comes from their <strong>disagreement</strong>: a usual pace that feels like a 7 instead of a 5, with a heart rate higher than usual, signals incomplete recovery. You'll find these clues in <a href="/articles/comment-savoir-si-on-est-bien-recupere.html">how to know if you're fully recovered</a>.</p>

<h2>How to use RPE day to day</h2>
<ul>
<li><strong>Program by RPE, not just by weight:</strong> "3 sets of 5 at RPE 8" rather than "3 × 5 at 100 kg (220 lb)." On a day when you're in great shape, the weight goes up on its own; on a tired day, you go lighter without missing your session. That's autoregulation.</li>
<li><strong>Keep easy sessions truly easy:</strong> according to a 2010 review by physiologist Stephen Seiler, elite endurance athletes do about 80% of their sessions at low intensity (3-4), with the remaining 20% dominated by hard work (7 and up). The classic trap is doing everything at 5-6: too hard to recover, not hard enough to progress.</li>
<li><strong>Record the RPE of every session</strong> about 30 minutes afterward, for the whole session. Multiplied by the duration, it gives you your <a href="/articles/charge-d-entrainement-c-est-quoi.html">training load</a>, to track from week to week.</li>
</ul>

<h2>Key takeaways</h2>
<ul>
<li>RPE rates your effort from 1 to 10: conversation possible around 3-4, a few words around 7-8, not a single word at 9-10.</li>
<li>In strength training, RPE 8 = 2 reps in reserve; the useful zone for muscle is 0 to 3 reps in reserve.</li>
<li>Program by RPE to adjust to how you feel on the day, and keep your easy sessions truly easy.</li>
</ul>
""",
        "faq": [
            {"q": "What does RPE mean in weight training?",
             "a": "RPE stands for rating of perceived exertion, your perceived effort rated from 1 to 10. In weight training, it's read as reps in reserve: RPE 10 means failure, RPE 8 means two more reps were possible. It lets you adjust the weight to how you feel on the day."},
            {"q": "What does RPE 7 correspond to?",
             "a": "A hard but controlled effort. In endurance training, you can only say a few words at a time; in strength training, you finish the set with about 3 reps in reserve. It's a common level for working sets and for paces close to threshold."},
            {"q": "What's the difference between RPE and RIR?",
             "a": "RPE rates effort out of 10, RIR counts the reps you had left at the end of the set. In strength training, the two match up: RPE 9 = 1 RIR, RPE 8 = 2 RIR, RPE 7 = 3 RIR. RIR is often easier to estimate under the bar."},
        ],
    },
    {
        "fr": "regle-des-10-pourcent-course",
        "slug": "10-percent-rule-running",
        "title": "The 10% rule: how to increase your mileage without injury",
        "description": "The 10% rule: no more than 10% extra volume per week. What it's really worth, its limitations, and safer alternatives for increasing your running mileage.",
        "body": """
<p>The short answer: the <strong>10% rule</strong> says not to increase your training volume — distance or time — by more than <strong>10% from one week to the next</strong>. It's a good <strong>rule of thumb</strong> against sudden jumps, which are linked to more injuries in runners. But it isn't a law: the number is arbitrary, it ignores intensity and it forgets about recovery weeks. You're better off building in stages and listening to your body's signals.</p>
<p>It has one huge merit: it forces patience. Your heart and lungs improve fast, within a few weeks. Your tendons and bones, on the other hand, adapt over months. That gap is what traps so many motivated runners: their cardio keeps up, their tissues don't.</p>

<h2>What exactly does the 10% rule say?</h2>
<p>The principle fits in one line: if you ran 30 km (18.6 miles) this week, next week doesn't go above 33 km (20.5 miles). Simple, easy to remember, usable without any math. It comes from running, but the logic applies to cycling, swimming or the number of sets in the weight room.</p>
<p>What it tries to prevent is the classic scenario: you sign up for a half marathon, motivation peaks, and your mileage jumps 50% all at once. Your tissues hold up for a few weeks, then give out.</p>

<h2>Is the 10% rule backed by science?</h2>
<p>Not really. A 2008 Dutch randomized trial tested it on 532 novice runners training for a 6.7 km race: 20.8% got injured on a 13-week program built on the 10% rule, versus 20.3% on the standard 8-week program. No difference. What the data suggest is that small increases aren't the problem: it's <strong>big, sudden jumps</strong> that seem to cause injuries. In 874 novice runners followed for a year (2014), those who increased their volume by more than 30% over two weeks appeared more exposed to distance-related injuries, but a 2018 systematic review judged this evidence very limited. There's nothing physiological about the 10% figure; it's a cautious benchmark that became popular because it's a round number.</p>
<p>The largest study to date shifts the question. In 5,205 runners tracked for 18 months with their watches (2025), the week-to-week increase wasn't linked to injuries. However, a single run exceeding the longest run of the previous 30 days by 10 to 30% came with a 64% higher rate of overuse injuries. The 10% threshold may apply more to your single run than to your week.</p>

<h2>What are the limitations of the 10% rule?</h2>
<ul>
<li><strong>At low volume, it's negligible:</strong> 10% of 10 km is 1 km. A beginner can often progress a little faster in absolute terms, as long as they stay pain-free.</li>
<li><strong>Applied week after week without a break, it doubles your volume:</strong> +10% a week for just over 7 weeks, and your mileage has doubled. No tendon likes a continuous ramp without a plateau.</li>
<li><strong>It ignores intensity and context:</strong> 3 km of intervals or downhill trail running don't weigh the same as 3 km of easy jogging. New shoes, a new surface or short nights also change the equation.</li>
<li><strong>It only looks at the previous week:</strong> after a lighter week, it would hold you back for no reason; after an exceptional week, it would let you climb even higher.</li>
</ul>

<h2>What are safer ways to increase your running mileage?</h2>
<ul>
<li><strong>Plateaus:</strong> increase, then hold that volume for two to three weeks before going up again. Your tissues consolidate at each step.</li>
<li><strong>Lighter weeks:</strong> every 3 or 4 weeks, cut your volume significantly, by a quarter to a half depending on your fatigue. It's the running version of the <a href="/articles/semaine-de-decharge-deload.html">deload week</a>.</li>
<li><strong>One variable at a time:</strong> the week you lengthen your long run, don't also add intervals or elevation gain.</li>
<li><strong>Your recent average as the reference:</strong> compare your week with your last four, as the <a href="/articles/ratio-charge-aigue-chronique.html">acute:chronic workload ratio</a> does, rather than with the previous week alone. And only lengthen your longest run in small increments.</li>
</ul>
<p>Example: 20 km two weeks in a row, 22 km for two weeks, a lighter week at 16 km, then 24 km. Coming back from the light week, you restart from your plateau, not from 16 km. You progress like a staircase rather than a ramp: that's <a href="/articles/surcharge-progressive-comment-progresser.html">progressive overload</a> applied to running.</p>

<h2>What signs should make you back off?</h2>
<p>No calculation rule replaces your body. Cut your volume right away if:</p>
<ul>
<li><strong>Localized pain</strong> shows up earlier and earlier in your run, or is still there the next morning.</li>
<li><strong>A tendon is stiff when you wake up</strong>, for example your Achilles tendon on your first steps.</li>
<li>Your easy runs become a struggle and your resting heart rate climbs several mornings in a row.</li>
</ul>
<p><strong>Pinpoint bone pain that gets worse with exercise</strong>, swelling or a limp aren't something you fix by adjusting your plan: see a doctor, it's the typical picture of a stress fracture. The other signs are covered in <a href="/articles/blessure-de-surmenage-signes.html">the signs of an overuse injury</a>.</p>

<h2>Key takeaways</h2>
<ul>
<li>The 10% rule is a useful benchmark against sudden jumps, not a scientific law.</li>
<li>Build in stages, schedule a lighter week every 3 to 4 weeks, and change only one variable at a time.</li>
<li>Pain that settles in overrides any plan; pinpoint bone pain, swelling or a limp: see a doctor.</li>
</ul>
""",
        "faq": [
            {"q": "How much should you increase your running mileage per week?",
             "a": "The classic benchmark is 10% at most from one week to the next, but it's a cautious limit rather than a law. The safest approach: build in stages, hold each level for two to three weeks, schedule a lighter week every 3 to 4 weeks, and avoid any run that's more than 10% longer than your longest run of the past month."},
            {"q": "Should you take a recovery week in running?",
             "a": "Yes, it's one of the best protections against overuse. Every 3 or 4 weeks, cut your volume significantly, by a quarter to a half depending on your fatigue, while keeping some easy runs. You then start the next stage fresher."},
            {"q": "Why do you get injured when you increase your mileage too quickly?",
             "a": "Because your heart and lungs adapt within a few weeks, while your tendons and bones need months. A sudden increase overloads these tissues before they've gotten stronger, which leads to tendinopathies, shin splints and stress fractures."},
        ],
    },
    {
        "fr": "periodisation-entrainement-bases",
        "slug": "training-periodization-basics",
        "title": "Training periodization: the basics to keep making progress",
        "description": "Training periodization explained: macro-, meso- and microcycles, linear vs undulating models, where deload weeks fit, and a concrete 4-week example.",
        "body": """
<p>The short answer: <strong>periodization</strong> means organizing your training into <strong>planned cycles</strong> instead of repeating the same week forever. You vary volume and intensity to progress toward a goal while managing fatigue: a few weeks where the load goes up, a lighter week to absorb it, then a new cycle one notch higher.</p>
<p>The word sounds intimidating, but the principle is simple. Your body adapts to what you ask of it, then stops progressing if the demand no longer changes. And it can't handle a load that keeps rising forever. Periodization solves both problems at once: it's often what separates progress that lasts from long months stuck on a plateau.</p>

<h2>Macrocycle, mesocycle, microcycle: how do they fit together?</h2>
<ul>
<li><strong>The macrocycle:</strong> the big picture, from several months to a year. It leads to a goal: a marathon, a strength competition, a fit summer.</li>
<li><strong>The mesocycle:</strong> a block of 3 to 6 weeks with a clear priority — building a base, developing strength, sharpening speed. It usually ends with a lighter week.</li>
<li><strong>The microcycle:</strong> most often, the week. It's how your sessions are arranged: which day is hard, which day is easy, which day is rest.</li>
</ul>
<p>Like Russian nesting dolls: weeks make up blocks, blocks make up the season. You don't need to plan a whole year to benefit; a single well-built block already changes your results.</p>

<h2>Linear vs undulating periodization: which should you choose?</h2>
<ul>
<li><strong>Linear:</strong> volume goes down and intensity goes up over the weeks. In strength training, for example, you move from sets of 12 to sets of 8, then 5, with heavier and heavier weights. Easy to follow, ideal for preparing for a specific date.</li>
<li><strong>Undulating:</strong> intensity varies within the week. Monday heavy with sets of 5, Wednesday moderate with sets of 10, Friday lighter with sets of 15. More variety, several qualities trained in parallel.</li>
</ul>
<p>Which one is best? First, periodizing pays off mainly for strength: a 2017 meta-analysis (18 studies) found a moderate effect on maximal strength compared with an identical program repeated week after week. For muscle mass, with volume equated, the difference disappears (2022 meta-analysis, 35 studies). Between linear and undulating, the gaps are small: no difference in strength in a 2015 meta-analysis (17 studies, 510 participants), and an advantage for undulating, limited to already trained lifters, in the 2022 one. The right model is the one you follow consistently and that actually increases the demand: the foundation remains <a href="/articles/surcharge-progressive-comment-progresser.html">progressive overload</a>.</p>
<p>In endurance, same logic: a base phase rich in easy volume, then a specific phase where hard sessions take up more room, then a taper before the goal. According to a 2007 meta-analysis (27 studies), the most effective taper lasts about 2 weeks, with volume reduced by 41 to 60%, without touching intensity or session frequency.</p>

<h2>When should you schedule deload weeks?</h2>
<p>At the end of each mesocycle. A common format is "3 + 1": 3 weeks building up, then a lighter week, sometimes after 2 if the load is very heavy or your life very busy. Seasoned lifters often space them out more: among 246 strength and physique competitors surveyed in 2024, deloads came around every 5 to 6 weeks on average and lasted about a week. The how-to is covered in <a href="/articles/semaine-de-decharge-deload.html">the deload week</a>: you cut volume significantly, keep some intensity, and let fatigue subside so your gains can show.</p>
<p>The calendar is only a starting point. If your warning signs light up before the planned date — worse sleep, performance slipping, a higher resting heart rate — bring the deload forward. Same reflex if your <a href="/articles/ratio-charge-aigue-chronique.html">acute:chronic workload ratio</a> flags a spike.</p>

<h2>A 4-week periodization example</h2>
<p>A simple strength-training mesocycle, guided by <a href="/articles/rpe-echelle-effort-percu.html">perceived exertion</a> and reps in reserve:</p>
<ul>
<li><strong>Week 1:</strong> 3 sets per exercise, stopped 3 reps short of failure (RPE 7). You set your reference weights.</li>
<li><strong>Week 2:</strong> 4 sets, stopped 2 reps short of failure (RPE 8), at the same or slightly higher weight.</li>
<li><strong>Week 3:</strong> 4 sets at 1 rep short of failure (RPE 9). The hardest week of the block.</li>
<li><strong>Week 4:</strong> deload. 2 sets per exercise, far from failure, with slightly reduced weights.</li>
</ul>
<p>For a runner, same architecture: for example 30, 33, then 36 km (roughly 19, 20.5 and 22 miles) with one hard session per week, then a 24 km (15-mile) week. The next block starts one notch above the previous one. And write everything down: without a training log, there's no way to know whether the cycle worked.</p>

<h2>Key takeaways</h2>
<ul>
<li>Periodizing means organizing your training into nested cycles: the season (macro), blocks of 3 to 6 weeks (meso), the week (micro).</li>
<li>Linear or undulating, the differences are small: what matters is a structure you stick to and a load that goes up.</li>
<li>End each block with a deload week, and bring it forward if your fatigue signals light up.</li>
</ul>
""",
        "faq": [
            {"q": "What is a mesocycle in strength training?",
             "a": "A training block of 3 to 6 weeks focused on one priority, such as strength or volume. It usually strings together a few weeks of increasing load, then a lighter week, before starting again one notch higher."},
            {"q": "Should beginners periodize their training?",
             "a": "No need for a complex plan: at the start, almost anything makes you progress. But a simple structure helps from day one: increase the load over 3 weeks, go lighter in the fourth, and log your sessions to know what works."},
            {"q": "How long should a training cycle last?",
             "a": "A block most often lasts 3 to 6 weeks, deload included, and a full season several months. The 3 weeks of building plus 1 lighter week format is a good starting point for a recreational athlete; experienced strength athletes tend to deload every 5 to 6 weeks on average."},
        ],
    },
    {
        "fr": "blessure-de-surmenage-signes",
        "slug": "overuse-injury-signs",
        "title": "Overuse injury: the warning signs you shouldn't ignore",
        "description": "Overuse injuries: tendinopathy, shin splints, stress fractures. The warning signs you shouldn't ignore, why they happen and when to see a doctor.",
        "body": """
<p>The short answer: an <strong>overuse injury</strong> sets in when you repeat the same stress faster than your tissues can recover. The sign not to ignore: <strong>localized pain that shows up during exercise and then lingers</strong>, comes back every session and appears earlier and earlier. Unlike muscle soreness, it doesn't fade in two or three days. And <strong>pinpoint bone pain that gets worse with exercise</strong>, especially with swelling or a limp, means you need to see a doctor.</p>
<p>These injuries never happen all at once, even if you often discover them one morning. They give warnings for days, sometimes weeks. The problem is that we learn to silence those signals.</p>

<h2>Tendinitis, shin splints, stress fractures: the most common overuse injuries</h2>
<ul>
<li><strong>Tendinopathy</strong> (often called tendinitis): Achilles tendon, patellar tendon, shoulder, elbow. Pain when you start that fades once you're warmed up and then returns when you cool down, stiffness on your first steps in the morning, a tendon that's tender to the touch.</li>
<li><strong>Shin splints</strong> (medial tibial stress syndrome): diffuse pain along the inner edge of the shinbone, over several centimeters (a few inches), typical of runners who increase their volume quickly or change surfaces.</li>
<li><strong>Stress fracture:</strong> a crack in the bone caused by repeated impact, in the shinbone, the metatarsals of the foot, sometimes the hip or pelvis. <strong>Very localized</strong> pain, on a precise spot, that gets worse with exercise and eventually makes itself felt at rest or at night. A 2014 review focused on distance runners describes it as one stage of a continuum: a stress reaction in the bone, then a crack, and at worst a complete fracture.</li>
<li><strong>Plantar fasciitis:</strong> pain under the heel, sharp on your first steps in the morning or after sitting for a while.</li>
</ul>
<p>The trap with tendinopathy is that it "warms up": it hurts for ten minutes, then nothing, so you keep going. That evening or the next day, it hands you the bill.</p>

<h2>Muscle soreness or injury: how can you tell the difference?</h2>
<ul>
<li><strong>Location:</strong> soreness is diffuse, in the belly of the muscle, often on both sides. An overuse injury is precise, on a tendon or a bone, often on one side only.</li>
<li><strong>How it evolves:</strong> soreness generally peaks 48 to 72 hours after the session, according to a 2018 review, then fades. Overuse pain comes back every session, earlier and earlier.</li>
<li><strong>Response to movement:</strong> moving eases soreness. Pain that increases as the effort goes on, or that changes your stride, is a red flag.</li>
</ul>
<p>For what's simply muscle soreness, the real remedies are here: <a href="/articles/courbatures-que-faire.html">what to do about sore muscles</a>.</p>

<h2>Why do overuse injuries happen?</h2>
<p>Tendons and bones get stronger with training, but far more slowly than your cardio. The classic causes:</p>
<ul>
<li><strong>A load increase that's too fast:</strong> more miles, more intensity, new hills or jumps. That's what the <a href="/articles/ratio-charge-aigue-chronique.html">acute:chronic workload ratio</a> monitors and what the <a href="/articles/regle-des-10-pourcent-course.html">10% rule</a> tries to rein in.</li>
<li><strong>Not enough recovery:</strong> hard sessions back to back, short nights, high stress. The tissue doesn't have time to rebuild between two loads.</li>
<li><strong>Energy intake that's too low:</strong> eating too little for what you burn weakens your bones. In elite distance athletes (2018), bone injuries were about 4.5 times more common in those with absent periods, or with low testosterone in men. For female athletes, losing your period is therefore a warning sign, explained in <a href="/articles/cycle-menstruel-et-sport.html">menstrual cycle and training</a>.</li>
<li><strong>Sudden changes:</strong> new shoes, a new surface, returning after a break. And a past injury in the same spot increases the risk.</li>
</ul>

<h2>What should you do at the first signs?</h2>
<ul>
<li><strong>Cut your load right away:</strong> less volume, less intensity, and drop whatever triggers the pain (intervals, downhills, jumps).</li>
<li><strong>Keep what doesn't hurt:</strong> cycling, swimming or pain-free strength work maintain your fitness without aggravating the area.</li>
<li><strong>Don't grit your teeth:</strong> pushing through the pain can turn a simple bone stress reaction into a real fracture, and a few weeks of discomfort into several months off.</li>
<li><strong>For a tendon:</strong> complete rest isn't always the answer. A physical therapist can offer you progressive strengthening, the foundation of tendinopathy treatment: a review of 25 systematic reviews (2020) identifies eccentric exercises as the most consistently effective treatment.</li>
</ul>

<h2>When should you see a doctor?</h2>
<p>See a doctor without delay if you have <strong>localized bone pain that gets worse with exercise</strong>, <strong>swelling</strong>, a <strong>limp</strong>, pain that persists at rest or at night, or groin pain when running. That's the picture of a possible stress fracture, and some locations, like the femoral neck at the hip, tolerate no delay: a late diagnosis increases the risk of the fracture becoming displaced. Same advice if pain doesn't improve after one to two weeks of reduced load. Early on, an X-ray can look normal: according to a 2016 systematic review, it picks up only 12 to 56% of stress fractures, with MRI being the most reliable test. Only a professional can make the diagnosis.</p>

<h2>Key takeaways</h2>
<ul>
<li>Localized pain that appears during exercise, lingers and comes back earlier and earlier is the No. 1 warning sign of overuse.</li>
<li>The causes: load rising too fast, not enough recovery, energy intake that's too low, sudden changes.</li>
<li>Pinpoint bone pain that gets worse with exercise, swelling or a limp: see a doctor, it may be a stress fracture.</li>
</ul>
""",
        "faq": [
            {"q": "How do you know if you have a stress fracture?",
             "a": "It shows up as very localized bone pain, on a precise spot, that gets worse with exercise and eventually makes itself felt at rest, sometimes with swelling. Only a doctor can confirm it, often with imaging, because an X-ray can look normal early on: see a doctor without delay."},
            {"q": "Tendinitis: should you stop exercising completely?",
             "a": "Not necessarily. You need to reduce or cut out whatever triggers the pain, but complete rest isn't always the best option for a tendon. A physical therapist can offer suitable progressive strengthening, which is the foundation of treatment."},
            {"q": "How long do shin splints last?",
             "a": "It mainly depends on how early you react: caught early, with a reduced load, they often improve within a few weeks; neglected, they can drag on for months. If the pain is concentrated on one precise spot on the bone, get it checked to rule out a stress fracture."},
        ],
    },
]
