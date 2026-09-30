# -*- coding: utf-8 -*-
"""English version of /methode/frequence-cardiaque-repos.html → /en/methode/resting-heart-rate.html.

Translation of tools/methode/frequence_cardiaque_repos.py: same facts and links (resting
HR read from Apple Health (bpm), 30% of the 42-point vitals pillar, lower is better,
42-day baseline, day excluded, min 7, full confidence 28, 0 points beyond 2 standard
deviations above normal; biological age modifier, reference and cap not published,
when it isn't already part of the VO₂max equation). related / journal / kind / num /
order / date are taken from the French page.
"""

PAGE = {
    "fr": "frequence-cardiaque-repos",
    "slug": "resting-heart-rate",
    "label": "Resting heart rate",
    "title": "Resting heart rate, your engine's idle speed",
    "seo_title": "Resting heart rate: normal range, high, low, what it means",
    "description": "Resting heart rate: what it reflects, normal values, what makes it rise, when to see a doctor, and how the app compares it with your own normal.",
    "lead": "The number of beats your heart needs when you're doing nothing is <strong>your engine's idle speed</strong>. A few extra beats several mornings in a row, and your body is already telling you something, often before you feel it.",
    "body": """
<h2>What is resting heart rate?</h2>
<p>Resting heart rate is <strong>the number of times your heart beats per minute when you're completely at rest</strong>: awake but calm and still, or asleep. It's expressed in beats per minute, or bpm.</p>
<p>It's one of the simplest numbers in physiology, and one of the most telling, as long as you always measure it under the same conditions.</p>

<h2>What your resting heart rate reflects</h2>
<p>It tells two stories at once.</p>
<ul>
<li><strong>Your fitness, over months:</strong> a trained heart pumps out more blood with each contraction. So it needs to beat less often to deliver the same output. That's why endurance training lowers your resting heart rate, slowly, over the weeks.</li>
<li><strong>Your state, day to day:</strong> at rest, the parasympathetic nervous system puts the brakes on your heart. When fatigue or stress loosens that brake, or when your body is fighting an infection or is short on fluids, your heart rate climbs by a few beats.</li>
</ul>
<p>That double identity is what makes it so valuable. It's also why it should be read alongside <a href="/methode/variabilite-cardiaque.html">heart rate variability</a>: both reflect the same nervous balance, seen from two angles.</p>

<h2>How to measure resting heart rate</h2>
<p>At the doctor's office, it's taken in a calm setting, after a few minutes of rest, by checking your pulse or with an electrocardiogram. At home, the simplest way is to count your pulse <strong>when you wake up, before you get out of bed</strong>.</p>
<p>Your watch tracks it with its optical sensor on your wrist, using photoplethysmography. It's less precise than an electrocardiogram, but reliable for trends when the watch is worn properly. The right moment stays the same: <strong>when you wake up or while you sleep</strong>, when conditions repeat from one day to the next. A reading taken right after climbing the stairs or a heated conversation can't be compared with anything.</p>

<h2>What is a normal resting heart rate?</h2>
<p>In adults, resting heart rate generally falls <strong>between 60 and 100 bpm</strong>. In endurance athletes, it often drops to <strong>between 40 and 60</strong>. Fitness, genetics, sex, heat and some medications make it vary from one person to another.</p>
<p>Over the long term, large studies associate a low resting heart rate with better fitness, and a persistently high one with greater cardiovascular risk. But day to day, the absolute number matters less than <strong>how far it is from your own normal</strong>: 58 bpm may be perfect for your neighbor and, for you, if you usually sit at 50, the sign of a rough night. Everything that makes a <a href="/articles/frequence-cardiaque-repos-normale.html">normal resting heart rate</a> comes down to that gap.</p>

<h2>What makes your resting heart rate go up</h2>
<p>One extra beat one morning means nothing. <strong>Several extra beats, several days in a row</strong>, does. The most common causes:</p>
<ul>
<li><strong>Fatigue:</strong> a training load that builds up faster than you recover.</li>
<li><strong>Alcohol:</strong> it speeds up your heart during the night that follows.</li>
<li><strong>Stress:</strong> a tense stretch keeps your nervous system on alert, even at rest.</li>
<li><strong>Dehydration:</strong> less blood volume, so more beats for the same output.</li>
<li><strong>An infection coming on:</strong> your body mobilizes its defenses and your heart speeds up, sometimes before you feel sick.</li>
</ul>
<p>If your heart rate stays <a href="/articles/frequence-cardiaque-repos-elevee.html">high several days in a row</a>, start by going through these causes before you push your training.</p>

<h2>How the app reads your resting heart rate</h2>
<p>In the app, resting heart rate is the second signal in the vitals pillar of the <a href="/methode/readiness-score.html">Readiness Score</a>: <strong>30% of its 42 points</strong>, or nearly 13 points out of 100 when all the data is there. Together with HRV, it makes up three quarters of the pillar.</p>
<div class="figs">
  <div><span class="v">30%</span><span class="u">of the vitals pillar</span></div>
  <div><span class="v">≈ 13</span><span class="u">score points out of 100</span></div>
  <div><span class="v">42</span><span class="u">days of baseline</span></div>
  <div><span class="v">28</span><span class="u">days to full confidence</span></div>
</div>
<p>The app reads it from Apple Health, in bpm, then compares it with your <a href="/methode/ligne-de-base.html">baseline</a>: your average and standard deviation over the last 42 days, excluding the day being assessed, with a minimum of 7 days to get started and 28 for full confidence. <strong>The lower it is relative to your normal, the better</strong>; beyond two standard deviations above, it earns no points at all. The details of all five signals are on the <a href="/methode/vitaux.html">Vitals</a> page.</p>
<p>It also counts toward your <a href="/methode/age-biologique.html">biological age</a>, against a reference value, with an effect capped in either direction. The exception is when it's already part of the estimate of your <a href="/methode/vo2max.html">VO₂max</a>, since it's one of the inputs in some non-exercise models: it's never counted twice.</p>

<h2>The limits of the measurement</h2>
<ul>
<li><strong>The optical sensor:</strong> a watch that's too loose or badly positioned degrades the reading. Worn properly, it's reliable for trends.</li>
<li><strong>Medications:</strong> a medication that slows the heart, such as a beta-blocker, changes the reading. Your resting heart rate then no longer reflects only your fitness or your fatigue.</li>
<li><strong>Context:</strong> a very hot night, a big late dinner or a drink can push it up without any change in your fitness.</li>
</ul>

<h2>When to see a doctor</h2>
<p>This app isn't a medical device and doesn't diagnose anything. Some markers still deserve a medical opinion:</p>
<ul>
<li><strong>Above 100 bpm:</strong> a resting heart rate that stays there, day after day, with no explanation.</li>
<li><strong>Below 40 bpm with symptoms:</strong> feeling faint, dizziness or shortness of breath. With no symptoms at all, in an endurance athlete, a low heart rate is often simply a reflection of training.</li>
<li><strong>A rise that settles in:</strong> several days above your normal despite rest, with fatigue that won't go away.</li>
</ul>
<p>If you have palpitations, chest pain, feel faint or have unusual shortness of breath, see a doctor. In an emergency, call your local emergency number (911 in the US, 999 or 112 in the UK and Europe).</p>
""",
    "refs": [
        "Fox K. et al. (2007), resting heart rate in cardiovascular disease, <em>Journal of the American College of Cardiology</em>." ' <a href="https://doi.org/10.1016/j.jacc.2007.04.079" rel="noopener" target="_blank">doi:10.1016/j.jacc.2007.04.079</a>',
        "Jensen M. T. et al. (2013), resting heart rate, physical fitness and mortality (Copenhagen Male Study), <em>Heart</em>." ' <a href="https://doi.org/10.1136/heartjnl-2012-303375" rel="noopener" target="_blank">doi:10.1136/heartjnl-2012-303375</a>',
        "Buchheit M. (2014), monitoring training status with heart rate measures, <em>Frontiers in Physiology</em>." ' <a href="https://doi.org/10.3389/fphys.2014.00073" rel="noopener" target="_blank">doi:10.3389/fphys.2014.00073</a>',
        "Nes B. M. et al. (2011), estimating VO₂peak without an exercise test: the HUNT study, <em>Medicine &amp; Science in Sports &amp; Exercise</em>." ' <a href="https://doi.org/10.1249/MSS.0b013e31821d3f6f" rel="noopener" target="_blank">doi:10.1249/MSS.0b013e31821d3f6f</a>',
    ],
    "faq": [
        {"q": "What is a normal resting heart rate?",
         "a": "In adults, it generally falls between 60 and 100 beats per minute, and often between 40 and 60 in endurance athletes. Day to day, how far you are from your own normal says more than the absolute number."},
        {"q": "Why is my resting heart rate going up?",
         "a": "A rise of several beats, several days in a row, most often comes from fatigue, alcohol, stress, not drinking enough fluids or an infection coming on. If it stays above 100 bpm at rest, or comes with unusual symptoms, see a doctor."},
        {"q": "Is a resting heart rate of 45 dangerous?",
         "a": "In an endurance athlete with no symptoms at all, a rate that low is often simply a reflection of training. On the other hand, a rate below 40 that comes with feeling faint, dizziness or shortness of breath deserves a medical opinion. And if you take a medication that slows the heart, your low heart rate no longer reflects only your fitness."},
    ],
}
