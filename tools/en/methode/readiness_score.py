# -*- coding: utf-8 -*-
"""English version of /methode/readiness-score.html → /en/methode/readiness-score.html.

Translation of tools/methode/readiness_score.py: same facts, weights and links
(pillars 42/21/21/16, sub-factors, 42-day baseline, min 7, full confidence 28,
weight redistribution, alcohol cap 80). related / journal / kind / num / order /
date are taken from the French page.
"""

PAGE = {
    "fr": "readiness-score",
    "slug": "readiness-score",
    "label": "The Readiness Score",
    "title": "The Readiness Score, pillar by pillar",
    "seo_title": "Readiness Score: how it's calculated, pillar by pillar",
    "description": "The Readiness Score combines your overnight vitals, sleep, nutrition and daily rhythm. Its 4 pillars, their weights and the full method, with no black box.",
    "lead": "Every morning, a number out of 100 tells you whether your body is ready to push or needs to recover. Here is exactly how it's built: four pillars, seventeen signals, and one rule that changes everything: your vitals are only ever compared with you.",
    "body": """
<h2>What the score actually measures</h2>
<p>The Readiness Score answers a single question: <strong>is your body ready to handle a training load today?</strong> It's not a fitness grade, and it's not a health grade. It's a reading of your recovery at a given moment, built from everything the app knows about your night, your meals and your workouts.</p>
<p>The score is calculated from your night as soon as you wake up, then updates throughout the day as you log your meals and workouts. It rests on four pillars, weighted by how much each one matters for recovery:</p>
<div class="figs">
  <div><span class="v">42</span><span class="u">Overnight vitals</span></div>
  <div><span class="v">21</span><span class="u">Sleep</span></div>
  <div><span class="v">21</span><span class="u">Nutrition</span></div>
  <div><span class="v">16</span><span class="u">Rhythm and load</span></div>
</div>

<h2>Pillar 1 · Overnight vitals (42 points)</h2>
<p>This is the heaviest pillar, because it's the most direct and most objective reflection of the state of your autonomic nervous system. Five signals, measured by your watch at rest, mostly while you sleep, and read through Apple Health:</p>
<ul>
<li><strong><a href="/methode/variabilite-cardiaque.html">Heart rate variability (HRV)</a> — 45% of the pillar.</strong> The higher it is compared with your normal, the better you've recovered.</li>
<li><strong><a href="/methode/frequence-cardiaque-repos.html">Resting heart rate</a> — 30%.</strong> The lower it is compared with your normal, the better.</li>
<li><strong><a href="/methode/frequence-respiratoire.html">Respiratory rate</a> — 12%.</strong> An unusual rise is often the first sign of fatigue or an infection coming on.</li>
<li><strong><a href="/methode/saturation-oxygene.html">Blood oxygen saturation</a> — 7%.</strong></li>
<li><strong><a href="/methode/temperature-poignet.html">Wrist temperature</a> — 6%.</strong> Here, what counts is the deviation, in either direction.</li>
</ul>
<p>Each signal is covered in detail on the <a href="/methode/vitaux.html">Vitals</a> page.</p>

<h2>Pillar 2 · Sleep (21 points)</h2>
<ul>
<li><strong>Duration against your need — 40%.</strong> Your need starts from the National Sleep Foundation's guidelines for your age, then adjusts to the length of your own sleep cycles once it's known. The details: <a href="/methode/besoin-de-sommeil.html">your sleep need</a>.</li>
<li><strong>Deep and REM sleep — 25%.</strong> Only when your watch actually measured them: the app never makes up sleep stages for a night you logged by hand.</li>
<li><strong>Efficiency — 20%.</strong> The share of your time in bed that you were actually asleep.</li>
<li><strong>Regularity — 15%.</strong> Consistent bedtimes and wake times, the most underrated factor in sleep.</li>
</ul>

<h2>Pillar 3 · Nutrition (21 points)</h2>
<ul>
<li><strong>How well you hit your targets — 40%.</strong> The day's calories and macronutrients, against the targets calculated by the <a href="/methode/cibles.html">Targets</a> engine.</li>
<li><strong>Refueling after exercise — 25%.</strong> The protein you eat after a workout. On rest days, this criterion drops out and its weight goes to the others.</li>
<li><strong>Micronutrients — 20%.</strong> How well your needs are covered, calculated from the lab-measured values in the <a href="/methode/nutrition.html">Ciqual table from ANSES</a>, France's food safety agency.</li>
<li><strong>Hydration — 15%.</strong> What you drank against what's recommended for you.</li>
</ul>
<p>One rule stands apart: <strong>if you drank alcohol the day before, the nutrition pillar is capped at 80</strong>, no matter how good everything else is. Alcohol weighs on recovery, and no perfect meal erases it.</p>

<h2>Pillar 4 · Rhythm and load (16 points)</h2>
<ul>
<li><strong>Training load — 40%.</strong> The balance between your recent load and your usual load. A sudden spike lowers the score: a hard session usually takes its toll for 24 to 72 hours.</li>
<li><strong>Consistency of your daily rhythms — 30%.</strong> Bedtime, wake time and meals at regular hours.</li>
<li><strong>Cadence — 20%.</strong> Your active days compared with your norm, and your weekend drift.</li>
<li><strong>Muscle soreness — 10%.</strong> How you feel when you wake up, when you log it.</li>
</ul>

<h2>You versus you: the baseline</h2>
<p>This is the heart of the method. <strong>Your vitals are never compared with a population norm.</strong> An HRV of 45 ms can be excellent for you and low for someone else: what matters is how far you are from your own normal.</p>
<p>For each of the five vitals, the app calculates your average and your usual variability over the <strong>last 42 days</strong> (about six weeks), excluding the day being assessed, then measures how far the morning's value departs from it. A baseline needs at least 7 days of data to exist, and 28 days to be fully reliable. The full explanation: <a href="/methode/ligne-de-base.html">your baseline</a>.</p>
<p>The other pillars follow the same personal logic, each with its own reference: your sleep is judged against your need, your nutrition against your targets, your load against your usual load.</p>

<h2>No watch? The score adapts</h2>
<p>When a pillar has no data, it isn't replaced with a made-up value: it's removed, and <strong>its weight is redistributed among the others</strong>. No watch means no vitals: sleep, nutrition and rhythm then share the 100 points. The same principle applies inside each pillar.</p>
<p>Alongside the score, a confidence index shows how much data today's score rests on. A score built on three days of history doesn't read the same as one built on two months.</p>

<h2>What you see in the app</h2>
<ul>
<li><strong>Today's score</strong> on the home screen; tap it to open the details, with a verdict for your day.</li>
<li><strong>The breakdown of the four pillars</strong>, with the one dragging you down shown in red, and the exact sub-factor to watch.</li>
<li><strong>Your trends</strong> over several weeks, for the score and for each pillar.</li>
<li><strong>The Lab's cross-analyses</strong>, which show, for example, how a drink or a late dinner affects your next-day score, for you specifically.</li>
</ul>

<h2>What the score is not</h2>
<p>The Readiness Score is a wellness tool for pacing your effort. It's not a medical device and it doesn't diagnose anything. One low day isn't an alarm: the trend over several days is what counts. If you notice unusual symptoms, see a doctor, not a score.</p>
""",
    "refs": [
        "Hirshkowitz M. et al. (2015), National Sleep Foundation's sleep duration recommendations, <em>Sleep Health</em>." ' <a href="https://doi.org/10.1016/j.sleh.2014.12.010" rel="noopener" target="_blank">doi:10.1016/j.sleh.2014.12.010</a>',
        "Plews D. J. et al. (2013), heart rate variability monitoring and training adaptation in endurance athletes, <em>Sports Medicine</em>." ' <a href="https://doi.org/10.1007/s40279-013-0071-8" rel="noopener" target="_blank">doi:10.1007/s40279-013-0071-8</a>',
        "Buchheit M. (2014), monitoring training status with heart rate measures, <em>Frontiers in Physiology</em>." ' <a href="https://doi.org/10.3389/fphys.2014.00073" rel="noopener" target="_blank">doi:10.3389/fphys.2014.00073</a>',
    ],
    "faq": [
        {"q": "How is Ecleptic's Readiness Score calculated?",
         "a": "It combines four pillars: overnight vitals (42 points), sleep (21), nutrition (21), and daily rhythm with training load (16). Your vitals are compared with your own average over the last 42 days, never with a population norm; your sleep is judged against your need, your nutrition against your targets."},
        {"q": "Do you need a smartwatch to get a Readiness Score?",
         "a": "No. Without a watch, your vitals aren't measured: their weight is redistributed among sleep, nutrition and rhythm, and a confidence index shows how much data the score rests on. With a watch, the score gains its most precise pillar."},
        {"q": "Why is my Readiness Score low when I feel fine?",
         "a": "The score compares your vitals with your own normal: heart rate variability or a resting heart rate that drifts from your usual levels can show up before you feel tired. Look at the pillar in red and the sub-factor to watch, then at the trend over the following days."},
    ],
}
