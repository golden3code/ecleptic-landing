# -*- coding: utf-8 -*-
"""English version of /methode/variabilite-cardiaque.html → /en/methode/heart-rate-variability.html.

Translation of tools/methode/variabilite_cardiaque.py: same facts and links (HRV read
from Apple Health in SDNN format (ms), 45% of the 42-point vitals pillar, higher is
better, 42-day baseline, day excluded, min 7, full confidence 28, 0 points beyond
2 standard deviations below normal; biological age modifier, reduced weight with a
heart-slowing medication, figures not published). related / journal / kind / num /
order / date are taken from the French page.
"""

PAGE = {
    "fr": "variabilite-cardiaque",
    "slug": "heart-rate-variability",
    "label": "Heart rate variability (HRV)",
    "title": "Heart rate variability (HRV), beat by beat",
    "seo_title": "Heart rate variability (HRV): what it is and how to read it",
    "description": "Heart rate variability (HRV): what it measures, why it varies so much from one person to the next, what lowers it, and how the app reads it every night.",
    "lead": "Your heart doesn't beat like a metronome, and that's excellent news. That gap from one beat to the next, <strong>heart rate variability</strong>, is one of the most sensitive markers of your recovery, as long as you compare it with yourself and never with other people.",
    "body": """
<h2>What is heart rate variability (HRV)?</h2>
<p>Heart rate variability, or HRV, is <strong>the variation in the time between two successive heartbeats</strong>. It's expressed in milliseconds.</p>
<p>Even at 60 beats per minute, your heart doesn't beat exactly once per second: one interval lasts 980 milliseconds, the next 1,030, the third 1,005. This irregularity isn't a flaw. It's the signature of a heart that's constantly adjusting to what your body asks of it.</p>

<h2>What HRV reflects: your autonomic nervous system</h2>
<p>Two systems steer your heart, without you ever having to think about it:</p>
<ul>
<li><strong>The sympathetic system, the accelerator:</strong> it takes over in response to stress, exertion or a threat. Your heartbeats become more regular, and HRV drops.</li>
<li><strong>The parasympathetic system, the brake:</strong> carried largely by the vagus nerve, it dominates at rest, during digestion and during recovery. Your heart adjusts beat by beat, and HRV rises.</li>
</ul>
<p>An HRV that's high relative to your normal signals a body in recovery mode; a low HRV, a body that's still mobilized. The same balance governs your <a href="/methode/frequence-cardiaque-repos.html">resting heart rate</a>, and your breathing plays a part too: your heart speeds up slightly when you inhale and slows down when you exhale, hence the close link with your <a href="/methode/frequence-respiratoire.html">respiratory rate</a>.</p>

<h2>How HRV is measured: ECG or smartwatch</h2>
<p>In the lab, the gold standard is the <strong>electrocardiogram (ECG)</strong>. It detects every heartbeat and measures the intervals, following international standards set back in 1996.</p>
<p>Your watch works differently. Its optical sensor on your wrist uses <strong>photoplethysmography (PPG)</strong> to detect the pulse wave through your skin. It's less precise than an ECG, but reliable for trends when the watch is worn properly and you're not moving. Nighttime meets both conditions.</p>
<p>Then there's the question of format. Apple Health records HRV as <strong>SDNN</strong>, the standard deviation of the intervals between heartbeats: that's what the Apple Watch measures. Many studies and other devices use <strong>RMSSD</strong>, calculated from the differences between successive heartbeats. The two can't be compared directly: a number you read on a forum, or on a friend's watch, tells you nothing about yours.</p>

<h2>Why your HRV looks like no one else's</h2>
<p>HRV is one of the <strong>most individual</strong> measurements there is. Depending on age, genetics and fitness, it ranges from around 20 to more than 100 milliseconds. It declines over the years, and endurance training tends to raise it.</p>
<p>The direct consequence: comparing your HRV with a chart you found online makes almost no sense. Two people of the same age, equally fit, can show very different values. <strong>The only comparison that counts is you versus you</strong>, over several weeks, with the same device.</p>

<h2>What lowers HRV, and what helps</h2>
<ul>
<li><strong>Lack of sleep:</strong> a short or broken night leaves your nervous system on alert.</li>
<li><strong>Alcohol:</strong> even in small amounts, a drink in the evening often lowers your HRV the following night.</li>
<li><strong>Stress:</strong> a tense stretch keeps the accelerator pressed down, even at rest.</li>
<li><strong>Training load:</strong> a hard session, or weeks strung together without enough recovery.</li>
<li><strong>An infection coming on:</strong> your body mobilizes its defenses, sometimes before you feel sick.</li>
</ul>
<p>Conversely, what helps is well known: <strong>regular sleep</strong>, progressive <strong>endurance</strong> training, <strong>slow breathing</strong>, of which <a href="/articles/coherence-cardiaque-respiration.html">resonance breathing</a> is the simplest form, and <strong>less alcohol</strong>.</p>

<h2>How the app reads your HRV</h2>
<p>In the app, HRV is the heaviest signal in the vitals pillar of the <a href="/methode/readiness-score.html">Readiness Score</a>: <strong>45% of its 42 points</strong>, or nearly 19 points out of 100 when all the data is there.</p>
<div class="figs">
  <div><span class="v">45%</span><span class="u">of the vitals pillar</span></div>
  <div><span class="v">≈ 19</span><span class="u">score points out of 100</span></div>
  <div><span class="v">42</span><span class="u">days of baseline</span></div>
  <div><span class="v">28</span><span class="u">days to full confidence</span></div>
</div>
<p>The app reads it from Apple Health, in SDNN format, then compares it with your <a href="/methode/ligne-de-base.html">baseline</a>: your average and standard deviation over the last 42 days, excluding the day being assessed. It takes 7 days of data to get started, and 28 for full confidence. The higher your HRV relative to your normal, the more points it earns; beyond two standard deviations below your average, it earns none at all. The details of all five signals: <a href="/methode/vitaux.html">Vitals</a>.</p>
<p>A low night lowers that day's score, and that's normal. But <strong>HRV dropping for one night is noise; a week below your baseline is a signal.</strong></p>
<p>HRV also counts toward your <a href="/methode/age-biologique.html">biological age</a>: compared with the values expected for your age, it can move it in either direction, and it counts for less there if you take a medication that slows the heart.</p>

<h2>The limits of the measurement</h2>
<ul>
<li><strong>The optical sensor:</strong> a watch that's too loose or an arm that moves, and the reading degrades. Wear it snug, all night.</li>
<li><strong>The heart rhythm itself:</strong> irregular heartbeats, such as premature beats (extrasystoles), throw off the HRV calculation.</li>
<li><strong>Medications:</strong> a medication that slows the heart changes how your HRV should be read.</li>
<li><strong>Switching devices:</strong> changing watches means changing instruments. For the six weeks that follow, your baseline still mixes nights from both devices.</li>
</ul>

<h2>When to see a doctor</h2>
<p>HRV isn't a diagnostic tool, and this app isn't a medical device. A low HRV, even several days in a row, isn't a disease: it's an invitation to <a href="/articles/hrv-basse-que-faire.html">work on what's pulling it down</a>, to sleep better, to lighten your training.</p>
<p>On the other hand, if a drop settles in for no apparent reason along with unusual fatigue, or if you have palpitations, feel faint, or have chest pain or unusual shortness of breath, see a doctor. In an emergency, call your local emergency number (911 in the US, 999 or 112 in the UK and Europe).</p>
""",
    "refs": [
        "Task Force of the European Society of Cardiology and NASPE (1996), standards of measurement for heart rate variability, <em>Circulation</em>." ' <a href="https://doi.org/10.1161/01.CIR.93.5.1043" rel="noopener" target="_blank">doi:10.1161/01.CIR.93.5.1043</a>',
        "Shaffer F. and Ginsberg J. P. (2017), an overview of heart rate variability metrics and norms, <em>Frontiers in Public Health</em>." ' <a href="https://doi.org/10.3389/fpubh.2017.00258" rel="noopener" target="_blank">doi:10.3389/fpubh.2017.00258</a>',
        "Nunan D. et al. (2010), normal values for short-term heart rate variability in healthy adults, <em>Pacing and Clinical Electrophysiology</em>." ' <a href="https://doi.org/10.1111/j.1540-8159.2010.02841.x" rel="noopener" target="_blank">doi:10.1111/j.1540-8159.2010.02841.x</a>',
        "Plews D. J. et al. (2013), heart rate variability monitoring and training adaptation in endurance athletes, <em>Sports Medicine</em>." ' <a href="https://doi.org/10.1007/s40279-013-0071-8" rel="noopener" target="_blank">doi:10.1007/s40279-013-0071-8</a>',
    ],
    "faq": [
        {"q": "What is a good HRV for my age?",
         "a": "There's no universal good value: depending on age, genetics and fitness, HRV ranges from around 20 to more than 100 milliseconds, and it declines over the years. The right benchmark is your own average over several weeks, measured with the same device."},
        {"q": "Why did my HRV drop last night?",
         "a": "The most common causes are a night that was too short, alcohol the evening before, a stressful period, a hard workout or an infection coming on. A single low night is often just noise; several days below your baseline are a real signal to ease off. If unusual symptoms come with it, see a doctor."},
        {"q": "Is Apple Watch HRV accurate?",
         "a": "The watch tracks your pulse with an optical sensor, less precise than an electrocardiogram but reliable for trends when it's worn properly and you're at rest, as you are at night. It expresses HRV in SDNN format, which can't be compared directly with the RMSSD used by other devices: compare yourself with yourself, on the same watch."},
    ],
}
