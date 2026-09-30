# -*- coding: utf-8 -*-
"""English version of /methode/vitaux.html → /en/methode/vitals.html.

Translation of tools/methode/vitaux.py: same facts and links (five signals read from
Apple Health, weights 45/30/12/7/6 within the 42-point vitals pillar, 42-day baseline,
day excluded, min 7, full confidence 28, 0 points beyond 2 standard deviations,
missing signal removed and weight spread). related / journal / kind / num / order /
date are taken from the French page.
"""

PAGE = {
    "fr": "vitaux",
    "slug": "vitals",
    "label": "Vitals",
    "title": "Overnight vitals, signal by signal",
    "seo_title": "Overnight vitals (HRV, resting HR): how the app reads them",
    "description": "Overnight vitals carry 42 points of the Readiness Score: HRV, resting heart rate, breathing, SpO₂, temperature. How the app compares them with your normal.",
    "lead": "At night, your body speaks without a filter: no coffee, no meetings, no effort to muddy the message. Here is how the app reads your <strong>five vital signs</strong>, each one against your own normal, and why a single bad night is never enough to draw a conclusion.",
    "body": """
<h2>What the engine calculates</h2>
<p>The vitals engine turns five raw measurements from your watch into a single sub-score: the vitals pillar of the <a href="/methode/readiness-score.html">Readiness Score</a>, the heaviest of the four at <strong>42 points out of 100</strong>. It doesn't judge your health. It measures one thing only: <strong>how far your night departs from your normal</strong>, and in which direction.</p>
<p>Why give it so much weight? Because these signals depend neither on what you report nor on how you feel. They're the most direct and most objective reflection of your recovery, starting with the state of your autonomic nervous system, the one that decides, without asking your opinion, whether your body is in recovery mode or on alert.</p>

<h2>Five signals, read from Apple Health</h2>
<p>The app reads five signals from Apple Health, recorded by your watch at rest and mostly while you sleep. Each one has its own weight within the pillar:</p>
<div class="figs">
  <div><span class="v">45%</span><span class="u">Heart rate variability</span></div>
  <div><span class="v">30%</span><span class="u">Resting HR</span></div>
  <div><span class="v">12%</span><span class="u">Breathing</span></div>
  <div><span class="v">7%</span><span class="u">SpO₂</span></div>
  <div><span class="v">6%</span><span class="u">Temperature</span></div>
</div>
<ul>
<li><strong><a href="/methode/variabilite-cardiaque.html">Heart rate variability (HRV)</a>:</strong> the variation in time between two heartbeats, in milliseconds, in SDNN format. Higher than your normal is better.</li>
<li><strong><a href="/methode/frequence-cardiaque-repos.html">Resting heart rate</a>:</strong> in beats per minute. Lower than your normal is better.</li>
<li><strong><a href="/methode/frequence-respiratoire.html">Respiratory rate</a>:</strong> your breaths per minute. Lower is better; an unusual rise often comes with fatigue or an infection coming on.</li>
<li><strong><a href="/methode/saturation-oxygene.html">Blood oxygen saturation (SpO₂)</a>:</strong> the share of your hemoglobin carrying oxygen. Higher is better.</li>
<li><strong><a href="/methode/temperature-poignet.html">Wrist temperature</a>:</strong> measured while you sleep. Here, any deviation is penalized, in either direction.</li>
</ul>
<p>Together, HRV and resting heart rate make up <strong>three quarters of the pillar</strong>. When all the data is there, HRV alone weighs nearly 19 of the score's 100 points: no other signal weighs as much.</p>

<h2>Why at night</h2>
<p>Night is <strong>the only time when conditions are comparable from one day to the next</strong>. You're lying down, at rest, away from coffee, stress and exertion. An HRV reading taken at 3 p.m., after two coffees and a tense meeting, tells the story of your afternoon, not your recovery.</p>
<p>At night, the setting repeats: same position, same calm, same watch on the same wrist. That repetition is what makes the comparison fair. Without it, you're comparing different days, not the state of your body.</p>

<h2>The method, step by step</h2>
<ul>
<li><strong>1. Your baseline:</strong> for each signal, the app calculates your average and your standard deviation over the <strong>last 42 days</strong>, excluding the day being assessed. It needs at least 7 days of data to exist, and 28 for full confidence. All the details: <a href="/methode/ligne-de-base.html">your baseline</a>.</li>
<li><strong>2. The deviation from your normal:</strong> the night's value is translated into a number of standard deviations above or below your average. If your HRV hovers around 50 ms and usually varies by 5 ms, a night at 45 ms sits one standard deviation below your normal; a night at 40 ms, two.</li>
<li><strong>3. Points, in the right direction:</strong> that deviation becomes points according to the signal's direction. HRV and SpO₂: higher is better. Resting HR and breathing: lower is better. Temperature: any deviation is penalized. Beyond two standard deviations on the wrong side, the signal earns no points at all.</li>
<li><strong>4. Weighting:</strong> the five sub-scores are combined according to their weights. If your watch didn't record a signal that night, or if the signal doesn't yet have 7 days of history, it's removed and its weight is spread among the others. Nothing is made up to fill the gap.</li>
</ul>

<h2>One night is noise; a week is a signal</h2>
<p>Your vitals naturally move from one night to the next. A short night, one drink too many, a stressful day: your HRV can plunge without it meaning much. <strong>HRV dropping for one night is noise. A week below your baseline is a signal.</strong></p>
<p>The method already does part of the sorting. Because each deviation is measured against your own usual variability, someone whose HRV swings a lot has to deviate further to lose points than someone who's very steady. But a low night really does lower that day's score: it's up to you not to jump to conclusions.</p>
<p>The real signal is <strong>repetition</strong>: several days below your normal, especially when your resting heart rate rises at the same time. That's the pattern of fatigue building up, a training load ramped up too abruptly or an infection coming on. That's why the app also shows you the trend of your score and of each pillar over several weeks.</p>

<h2>Why these choices</h2>
<ul>
<li><strong>You versus you:</strong> HRV ranges from 20 to more than 100 ms depending on age, genetics and fitness. Judging it against a population norm would condemn some people to look tired their whole lives. Only the deviation from your own normal makes sense.</li>
<li><strong>The same device:</strong> Apple Health records HRV in SDNN format, the Apple Watch's format, whereas many studies and other devices use RMSSD. The two can't be compared directly. Comparing you with yourself, on the same watch, solves the problem.</li>
<li><strong>42 days:</strong> long enough for your normal to be stable, short enough to track a real change in fitness. The day being assessed is excluded from the calculation, so an extreme value doesn't dilute its own reference.</li>
<li><strong>Unequal weights:</strong> HRV and resting HR are the most direct windows onto your autonomic nervous system, hence their three quarters of the pillar. Breathing, SpO₂ and temperature weigh less, but they capture something else: an infection coming on often pushes up breathing rate and temperature.</li>
</ul>

<h2>Beyond the score: your biological age</h2>
<p>Two of these signals are also used elsewhere. In the calculation of your <a href="/methode/age-biologique.html">biological age</a>, HRV acts as a modifier: compared with the values expected for your age, it can move it in either direction. It counts for less there if you take a medication that slows the heart.</p>
<p>Resting HR does the same, against a reference value, except when it's already part of your VO₂max equation. It's never counted twice.</p>

<h2>No watch, and the limits of measurement</h2>
<p><strong>No watch, no vitals.</strong> The pillar is then removed and its weight redistributed among sleep, nutrition and rhythm. A confidence index tells you so: a score without its vitals doesn't read like a complete score.</p>
<p>With a watch, keep in mind how it measures. Its optical sensor uses photoplethysmography (PPG) to track your pulse through the skin of your wrist: it's less precise than an electrocardiogram, but <strong>reliable for trends when the watch is worn properly</strong>, snug and kept on all night.</p>
<p>Finally, this engine is a wellness tool, not a medical device: it doesn't diagnose anything. A signal below your normal is a nudge to ease off, not a reason to panic. If an unusual value persists, or if you feel faint or have chest pain, unusual shortness of breath or palpitations, see a doctor. In an emergency, call your local emergency number (911 in the US, 999 or 112 in the UK and Europe).</p>
""",
    "refs": [
        "Task Force of the European Society of Cardiology and NASPE (1996), standards of measurement for heart rate variability, <em>Circulation</em>." ' <a href="https://doi.org/10.1161/01.CIR.93.5.1043" rel="noopener" target="_blank">doi:10.1161/01.CIR.93.5.1043</a>',
        "Plews D. J. et al. (2013), heart rate variability monitoring and training adaptation in endurance athletes, <em>Sports Medicine</em>." ' <a href="https://doi.org/10.1007/s40279-013-0071-8" rel="noopener" target="_blank">doi:10.1007/s40279-013-0071-8</a>',
        "Buchheit M. (2014), monitoring training status with heart rate measures, <em>Frontiers in Physiology</em>." ' <a href="https://doi.org/10.3389/fphys.2014.00073" rel="noopener" target="_blank">doi:10.3389/fphys.2014.00073</a>',
        "Miller D. J. et al. (2020), changes in nighttime respiratory rate and early detection of infection, <em>PLOS ONE</em>." ' <a href="https://doi.org/10.1371/journal.pone.0243693" rel="noopener" target="_blank">doi:10.1371/journal.pone.0243693</a>',
        "WHO (2011), pulse oximetry training manual." ' <a href="https://cdn.who.int/media/docs/default-source/patient-safety/pulse-oximetry/who-ps-pulse-oxymetry-training-manual-en.pdf" rel="noopener" target="_blank">who.int</a>',
    ],
    "faq": [
        {"q": "How do I know if my overnight vitals are normal?",
         "a": "The most reliable way is to compare them with your own average over the past few weeks rather than with a general norm: that's what the app does, over 42 days, for each of the five signals. A one-night deviation is often just noise; a deviation that persists, or comes with unusual symptoms, is worth a doctor's opinion."},
        {"q": "What's the difference between SDNN and RMSSD?",
         "a": "They're two ways of calculating heart rate variability. SDNN, used by Apple Health and the Apple Watch, is the standard deviation of the intervals between heartbeats; RMSSD, common in studies and on other devices, is calculated from the differences between successive heartbeats. The two can't be compared directly, which is why it pays to compare you with yourself, on the same device."},
        {"q": "What happens if my watch didn't measure a signal last night?",
         "a": "The missing signal is removed for that night and its weight is spread among the other vitals: nothing is made up to replace it. With no vitals at all, for example without a watch, the whole pillar is removed and its weight goes to sleep, nutrition and rhythm, with a confidence index that flags it."},
    ],
}
