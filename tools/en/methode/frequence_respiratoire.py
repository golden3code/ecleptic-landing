# -*- coding: utf-8 -*-
"""English version of /methode/frequence-respiratoire.html → /en/methode/respiratory-rate.html.

Translation of tools/methode/frequence_respiratoire.py: same facts and links (internal
weight 12% of the 42-point vitals pillar, lower than your normal is better, 42-day
baseline, day excluded, min 7, full confidence 28, 0 points at 2 standard deviations
above normal, missing signal → weight redistributed). related / journal / kind / num /
order / date are taken from the French page.
"""

PAGE = {
    "fr": "frequence-respiratoire",
    "slug": "respiratory-rate",
    "label": "Respiratory rate",
    "title": "Respiratory rate, the quiet alarm of your nights",
    "seo_title": "Normal respiratory rate during sleep: ranges and red flags",
    "description": "Your nighttime respiratory rate is one of your most stable vitals. Normal values, what makes it rise, and how the app compares it with your own normal.",
    "lead": "While you sleep, you breathe with almost perfect regularity, from one night to the next. That's why <strong>even the slightest unusual rise matters</strong>: it often signals fatigue or an infection coming on.",
    "body": """
<h2>What is respiratory rate?</h2>
<p>Respiratory rate is <strong>the number of complete breaths — one inhale, one exhale — you take in one minute</strong>. Nobody pays attention to it, and yet it's one of your body's most constant signals: when it moves, it means something.</p>
<p>In the app, it's one of the five signals in the “vitals” pillar of the <a href="/methode/readiness-score.html">Readiness Score</a>, the ones your watch measures while you sleep.</p>

<h2>What it reflects in your body</h2>
<p>At night, you don't decide how you breathe: your brain regulates it continuously, to keep the oxygen and carbon dioxide in your blood within narrow limits. When your body has more work to do, it breathes a little faster, without you noticing.</p>
<p>Your breathing is also coupled to your heart: with each inhale, your heart speeds up slightly; with each exhale, it slows down. This back-and-forth, called respiratory sinus arrhythmia, is one of the sources of your <a href="/methode/variabilite-cardiaque.html">heart rate variability</a>.</p>
<p>Above all, during sleep, this regulation is remarkably stable: <strong>in the same person, nighttime respiratory rate varies very little from one night to the next</strong>. A rise that lasts several nights is rarely a coincidence.</p>

<h2>From the doctor's office to your watch</h2>
<p>At the doctor's office, a clinician measures it in the simplest way possible: by counting the movements of your chest for one minute, at rest. In a sleep lab, sensors placed on your chest and under your nose record it all night.</p>
<p>A watch, on the other hand, can't see your chest. It <strong>estimates</strong> your breathing from indirect signals: the tiny movements of your wrist with each breath, or the variations that breathing imprints on your pulse. These signals are weak and the slightest movement scrambles them: at night, lying still, you give your watch the best possible measuring conditions. The app then reads the value recorded in Apple Health.</p>

<h2>What is a normal respiratory rate, and why does it vary?</h2>
<p>In adults at rest, respiratory rate <strong>generally falls between 12 and 20 breaths per minute</strong>.</p>
<div class="figs">
  <div><span class="v">12–20</span><span class="u">Breaths per minute at rest</span></div>
  <div><span class="v">12%</span><span class="u">Of the vitals pillar</span></div>
  <div><span class="v">42</span><span class="u">Days of baseline</span></div>
  <div><span class="v">7</span><span class="u">Days to get started</span></div>
</div>
<p>This range is wide: two perfectly healthy adults can have different usual rates, without one being better than the other. <strong>What counts is the gap from your own normal.</strong> A night at 16 breaths per minute can be ordinary for someone else, and unusual for you if you normally hover around 13.</p>

<h2>What makes your respiratory rate go up</h2>
<ul>
<li><strong>An infection coming on:</strong> a rise in nighttime respiratory rate over several nights is one of the early signs, sometimes even before you feel sick. With a fever, your <a href="/methode/temperature-poignet.html">wrist temperature</a> also moves away from its normal.</li>
<li><strong>Fatigue and physiological stress:</strong> an unusual rise over several nights often signals a body that's struggling to recover.</li>
<li><strong>Alcohol:</strong> your body clears it during the night, and your vitals suffer, breathing included. The details in <a href="/articles/alcool-sommeil-effets.html">alcohol and sleep</a>.</li>
<li><strong>Heat:</strong> a hot night or an overheated bedroom can push it up.</li>
<li><strong>Altitude:</strong> each breath brings in less oxygen up there, your <a href="/methode/saturation-oxygene.html">blood oxygen saturation</a> drops, and your body compensates by breathing more, especially during the first few days.</li>
</ul>

<h2>How the app reads your respiratory rate</h2>
<p>The app pulls from Apple Health the respiratory rate your watch measures while you sleep, then compares it with <a href="/methode/ligne-de-base.html">your baseline</a>: your average and standard deviation over the last 42 days, not counting the day being assessed. It takes at least 7 days of data for the signal to count, and 28 days for full confidence.</p>
<ul>
<li><strong>The direction:</strong> the lower your breathing rate relative to your normal, the better. A rise costs you points.</li>
<li><strong>The threshold:</strong> at 2 standard deviations above your normal, this signal earns no points at all.</li>
<li><strong>The weight:</strong> 12% of the <a href="/methode/vitaux.html">vitals</a> pillar, which is worth 42 points out of 100. On a day when all the data is there, breathing therefore weighs about 5 points of the score.</li>
</ul>
<p>It's the third signal in the pillar, behind heart rate variability (45%) and resting heart rate (30%), the two most direct reflections of your recovery. Breathing complements them: it rarely moves, but when it does, it deserves your attention. On a night with no reading, its 12% is spread among the other vitals; without a watch, the whole pillar is redistributed.</p>

<h2>The limits of the measurement</h2>
<ul>
<li><strong>It's an estimate:</strong> your watch infers your breathing; it doesn't count it. Its value may differ from a clinical measurement; what makes it useful is its consistency from one night to the next.</li>
<li><strong>One night doesn't make a trend:</strong> a loose band, a restless night or a long stretch awake can distort a single value. The trend over several days matters more than any one morning.</li>
<li><strong>The score observes; it doesn't explain:</strong> the app sees that your breathing is outside your normal, not why. A virus, a glass of wine or a bedroom that's too warm: you're the one who knows the context.</li>
</ul>

<h2>When to talk to a doctor</h2>
<p>One odd night isn't an alarm. On the other hand, a respiratory rate that stays clearly above your normal several nights in a row, especially with a fever, a cough or unusual fatigue, is worth discussing with a doctor. And if you get sick, let your body heal before you train again: the rules are in <a href="/articles/reprendre-le-sport-apres-maladie.html">returning to exercise after an illness</a>.</p>
<p>Unusual shortness of breath, chest pain, palpitations or feeling faint aren't things to monitor on an app: see a doctor right away and, in an emergency, call your local emergency number (911 in the US, 999 or 112 in the UK and Europe). This app is a wellness tool, not a medical device.</p>
""",
    "refs": [
        "Miller D. J. et al. (2020), changes in nighttime respiratory rate and early detection of infection, <em>PLOS ONE</em>." ' <a href="https://doi.org/10.1371/journal.pone.0243693" rel="noopener" target="_blank">doi:10.1371/journal.pone.0243693</a>',
        "Shaffer F. and Ginsberg J. P. (2017), an overview of heart rate variability metrics and norms, <em>Frontiers in Public Health</em>." ' <a href="https://doi.org/10.3389/fpubh.2017.00258" rel="noopener" target="_blank">doi:10.3389/fpubh.2017.00258</a>',
        "Buchheit M. (2014), monitoring training status with heart rate measures, <em>Frontiers in Physiology</em>." ' <a href="https://doi.org/10.3389/fphys.2014.00073" rel="noopener" target="_blank">doi:10.3389/fphys.2014.00073</a>',
    ],
    "faq": [
        {"q": "What is a normal respiratory rate during sleep?",
         "a": "In adults at rest, it generally falls between 12 and 20 breaths per minute, and in the same person it varies very little from one night to the next. More than the number itself, it's the gap from your own normal that tells you about your recovery."},
        {"q": "Why is my respiratory rate higher than usual at night?",
         "a": "An unusual rise can come from fatigue that's building up, physiological stress or an infection coming on, but also from alcohol, heat or altitude. If it persists for several nights, especially with a fever or unusual fatigue, talk to a doctor."},
        {"q": "Is the respiratory rate measured by a smartwatch accurate?",
         "a": "The watch doesn't count your breaths: it estimates them while you sleep from indirect signals, such as tiny wrist movements or variations in your pulse. Its absolute value remains approximate, but its consistency from one night to the next makes it a good trend indicator."},
    ],
}
