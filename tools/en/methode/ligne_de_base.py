# -*- coding: utf-8 -*-
"""English version of /methode/ligne-de-base.html → /en/methode/baseline.html.

Translation of tools/methode/ligne_de_base.py: same facts and links (42-day rolling
window, day being assessed excluded, mean + sample standard deviation, z-score turned
into points according to each signal's direction, temperature penalized both ways,
0 points at 2 standard deviations on the wrong side, min 7 days, full confidence at 28,
baseline applied to the 5 vitals only). related / journal / kind / num / order / date
are taken from the French page.
"""

PAGE = {
    "fr": "ligne-de-base",
    "slug": "baseline",
    "label": "Your baseline",
    "title": "Your baseline: you versus you",
    "seo_title": "HRV baseline: your vitals compared with you over 42 days",
    "description": "Your baseline is your normal over 42 days. How Ecleptic uses it to judge your HRV, resting heart rate and other vitals: the calculation, z-score, limits.",
    "lead": "An HRV of 45 ms means nothing until you know your normal. Here's how the app builds that normal, day after day, and why comparing you with yourself is fairer than comparing you with an average.",
    "body": """
<h2>Your normal, not the population's</h2>
<p>Your baseline is <strong>the usual value of a signal for you</strong>, along with the normal range of its variations, calculated over your last few weeks. It's the reference the app uses every morning to judge your <a href="/methode/vitaux.html">overnight vitals</a>: heart rate variability, resting heart rate, respiratory rate, blood oxygen saturation and wrist temperature.</p>
<p>The principle fits in three words: <strong>you versus you</strong>. An HRV of 45 ms can be excellent for you and mediocre for someone else. A number on its own says almost nothing; how far it departs from your own normal says a lot. How long you sleep, for its part, has its own reference: <a href="/methode/besoin-de-sommeil.html">your sleep need</a>, calculated from your age and your cycles.</p>

<h2>Why compare you with yourself</h2>
<p>Because the gap between two people is much bigger than the variation in one person from one day to the next. Age, genetics and fitness set the level of your signals. <a href="/methode/variabilite-cardiaque.html">Heart rate variability</a> is the perfect example: its normal values spread across a very wide range from one adult to another.</p>
<p>Comparing your HRV with a population average mostly measures who you are. Comparing it with your baseline measures <strong>what changed last night</strong>, and that's exactly what tells you about <a href="/articles/comment-savoir-si-on-est-bien-recupere.html">your recovery</a>. It's also the approach backed by research on athlete monitoring: reason against your own values, and in trends.</p>

<h2>How the app calculates it</h2>
<p>For each signal, the app takes <strong>the last 42 days</strong>, about six weeks, and derives two numbers from them: your average, and your standard deviation, meaning the usual size of your variations around that average.</p>
<div class="figs">
  <div><span class="v">42</span><span class="u">Days in the rolling window</span></div>
  <div><span class="v">7</span><span class="u">Days for it to exist</span></div>
  <div><span class="v">28</span><span class="u">Days for full confidence</span></div>
  <div><span class="v">5</span><span class="u">Vitals judged against your normal</span></div>
</div>
<ul>
<li><strong>Why 42 days:</strong> long enough for your baseline to be stable, short enough to follow a real change in fitness without too much lag.</li>
<li><strong>Why the day being assessed is excluded:</strong> the morning's value is compared with your past, never with itself. Otherwise, an extreme night would pull its own reference toward it and look less unusual than it really is.</li>
<li><strong>Why a rolling window:</strong> every day, the oldest day drops out of the calculation and the most recent one comes in. Your baseline moves forward with you.</li>
</ul>

<h2>The z-score, or the deviation in plain terms</h2>
<p>The day's value is then expressed as a <strong>z-score</strong>: how many standard deviations it sits from your average. Zero is exactly your normal. Example: if your HRV hovers around 50 ms with a standard deviation of 5 ms, a night at 40 ms gives a z-score of −2, or two standard deviations below your normal.</p>
<p>That z-score is converted into points according to each signal's direction:</p>
<ul>
<li><strong>HRV and blood oxygen saturation:</strong> above your normal is better.</li>
<li><strong>Resting heart rate and respiratory rate:</strong> below is better. A <a href="/methode/frequence-cardiaque-repos.html">resting heart rate</a> that climbs above your usual level often comes with fatigue, stress or an infection coming on.</li>
<li><strong>Wrist temperature:</strong> there's no good side. Any deviation is penalized, in either direction.</li>
</ul>
<p>At two standard deviations on the wrong side, the signal earns no points at all. The five signals are then weighted within the vitals pillar, which counts for 42 points out of 100 in the <a href="/methode/readiness-score.html">Readiness Score</a>.</p>

<h2>7 days to exist, 28 to be reliable</h2>
<p>A baseline can't be guessed: it takes <strong>at least 7 days of data</strong> for it to exist. Before that, the signal isn't scored: it's removed from the calculation and its weight is redistributed, like any missing data. For your very first days with a watch, your score therefore rests on your sleep, your nutrition and your rhythm.</p>
<p>After that, confidence rises day by day until it's <strong>full at 28 days</strong>. A confidence index comes with the score: a number built on ten days of history doesn't read like a number built on six weeks.</p>

<h2>What shifts your baseline</h2>
<p>Your normal isn't frozen, and that's intentional. Several things can make it drift:</p>
<ul>
<li><strong>A training block:</strong> a few weeks of rising load, then the adaptation that follows.</li>
<li><strong>A stressful stretch:</strong> work, exams, a move, broken nights.</li>
<li><strong>An illness:</strong> an infection can shift several signals at once, sometimes for days.</li>
<li><strong>A new watch:</strong> a different sensor, a different algorithm, and sometimes a different starting level.</li>
</ul>
<p>Thanks to the rolling window, your baseline catches up with these changes within a few weeks. During the transition, read your deviations with a bit more distance.</p>

<h2>The limits of the method</h2>
<ul>
<li><strong>One night isn't a signal:</strong> HRV dropping for one night is often temporary: a drink, a late dinner, a less clean measurement. Several days in a row below your baseline is a signal. Read the trend, not the night.</li>
<li><strong>Normal doesn't mean healthy:</strong> your baseline tells you whether you're departing from your habits, not whether your habits are good.</li>
<li><strong>A slow drift goes unnoticed:</strong> if a value slides gradually over weeks, the rolling window absorbs it. The day's deviation looks ordinary, while your normal itself has moved.</li>
</ul>

<h2>When to see a doctor</h2>
<p>The app is a wellness tool, not a medical device: your baseline doesn't diagnose anything. If an abnormal value persists, even if your baseline ends up absorbing it, or if you feel faint or have chest pain, unusual shortness of breath or palpitations, see a doctor. In an emergency, call your local emergency number (911 in the US, 999 or 112 in the UK and Europe).</p>
""",
    "refs": [
        "Plews D. J. et al. (2013), heart rate variability monitoring and training adaptation in endurance athletes, <em>Sports Medicine</em>." ' <a href="https://doi.org/10.1007/s40279-013-0071-8" rel="noopener" target="_blank">doi:10.1007/s40279-013-0071-8</a>',
        "Buchheit M. (2014), monitoring training status with heart rate measures, <em>Frontiers in Physiology</em>." ' <a href="https://doi.org/10.3389/fphys.2014.00073" rel="noopener" target="_blank">doi:10.3389/fphys.2014.00073</a>',
        "Shaffer F. and Ginsberg J. P. (2017), an overview of heart rate variability metrics and norms, <em>Frontiers in Public Health</em>." ' <a href="https://doi.org/10.3389/fpubh.2017.00258" rel="noopener" target="_blank">doi:10.3389/fpubh.2017.00258</a>',
    ],
    "faq": [
        {"q": "What is an HRV baseline?",
         "a": "It's your usual heart rate variability value, along with the normal range of its variations, calculated over your last few weeks. In Ecleptic, it covers the last 42 days, not counting the day being assessed, and serves as the reference for judging each night."},
        {"q": "How long does it take to establish your HRV baseline?",
         "a": "In Ecleptic, it takes at least 7 days of data for a baseline to exist, and confidence becomes full at 28 days. In the meantime, the signal is set aside and its weight is redistributed among the others."},
        {"q": "Is it bad to have a lower-than-average HRV?",
         "a": "Not necessarily: heart rate variability varies enormously from one person to another depending on age, genetics and fitness. What tells you about your recovery is the deviation from your own normal, especially if it lasts several days. A value that stays unusual, or symptoms, are worth a doctor's opinion."},
    ],
}
