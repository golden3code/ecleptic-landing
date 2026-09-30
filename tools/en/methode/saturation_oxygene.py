# -*- coding: utf-8 -*-
"""English version of /methode/saturation-oxygene.html → /en/methode/blood-oxygen.html.

Translation of tools/methode/saturation_oxygene.py: same facts and links (internal
weight 7% of the 42-point vitals pillar, higher than your normal is better, 42-day
baseline, day excluded, min 7, full confidence 28, 0 points at 2 standard deviations
below normal, missing signal → weight redistributed; low weight is a deliberate choice,
noisy signal). related / journal / kind / num / order / date are taken from the French
page.
"""

PAGE = {
    "fr": "saturation-oxygene",
    "slug": "blood-oxygen",
    "label": "Blood oxygen saturation (SpO₂)",
    "title": "Blood oxygen saturation, measured at the wrist",
    "seo_title": "Normal blood oxygen level (SpO₂): ranges and limits",
    "description": "Blood oxygen saturation (SpO₂) is generally 95 to 100% in healthy adults. What it measures, the limits of your watch, and how the app reads it at night.",
    "lead": "Every night, your watch estimates how loaded with oxygen your blood is. <strong>A valuable signal when it drops off, but a noisy one at the wrist</strong>: here's how to read it, and why the app gives it only a small weight.",
    "body": """
<h2>What does SpO₂ measure?</h2>
<p>Blood oxygen saturation is <strong>the share of your hemoglobin that's carrying oxygen</strong>. Hemoglobin is the protein in your red blood cells that carries oxygen from your lungs to your tissues; saturation tells you, as a percentage, how full it is.</p>
<p>The “p” in SpO₂ indicates a measurement by pulse oximetry, through the skin; when it's measured directly in blood from an artery, it's called SaO₂. In the app, SpO₂ is one of the five signals in the “vitals” pillar of the <a href="/methode/readiness-score.html">Readiness Score</a>.</p>

<h2>What it reflects in your body</h2>
<p>Each time it passes through your lungs, your blood reloads with oxygen. SpO₂ tells you whether that loading is complete: it depends on your breathing, the state of your lungs and the air you breathe. In a healthy person, hemoglobin is almost full at all times, and SpO₂ moves very little. That's why a clear drop is meaningful.</p>
<p>Don't confuse it with <a href="/methode/vo2max.html">VO₂max</a>, which measures how much oxygen your body can use during exercise. You can have perfect saturation and a modest VO₂max.</p>

<h2>From blood test to wrist</h2>
<p>The gold standard is arterial blood gas analysis: blood drawn from an artery and analyzed in a lab. Day to day, clinicians use a pulse oximeter, the little clip placed on your fingertip. It shines a red light and an infrared light through your finger; hemoglobin loaded with oxygen and hemoglobin without it don't absorb them the same way, and the device works out your saturation from that, beat by beat.</p>
<p>Your watch applies the same principle, but at the wrist, and without shining through: its sensor reads the light reflected back by your tissues. The signal is weaker, and more sensitive to movement, to your skin and to how tight the band is. The result: <strong>a less precise measurement than a medical fingertip oximeter</strong>, which works best when you're still, in other words while you sleep. The app then reads these values from Apple Health.</p>

<h2>What is a normal blood oxygen level in adults?</h2>
<p>In healthy adults, SpO₂ <strong>generally falls between 95 and 100%</strong>. During sleep, it dips slightly, because you breathe a little less deeply: that's normal.</p>
<div class="figs">
  <div><span class="v">95–100</span><span class="u">% in healthy adults</span></div>
  <div><span class="v">7%</span><span class="u">Of the vitals pillar</span></div>
  <div><span class="v">42</span><span class="u">Days of baseline</span></div>
  <div><span class="v">28</span><span class="u">Days to full confidence</span></div>
</div>
<p>Two healthy people don't necessarily have the same usual value: the state of their lungs and the altitude where they live matter, and, for wrist measurements, their skin and the way the watch sits on it. That's why the app doesn't judge you against a common threshold, but on <strong>the gap from your own normal</strong>.</p>

<h2>What makes your blood oxygen drop</h2>
<ul>
<li><strong>Altitude:</strong> each breath brings in less oxygen up there, and your saturation goes down. Your body compensates by breathing more, which raises your <a href="/methode/frequence-respiratoire.html">respiratory rate</a>. The details: <a href="/articles/sport-en-altitude-effets.html">training at altitude</a>.</li>
<li><strong>Breathing pauses during sleep:</strong> each pause makes your saturation drop, and it comes back up when breathing resumes. Repeated night after night, they can point to sleep apnea.</li>
<li><strong>An infection or a respiratory illness:</strong> when your lungs exchange gases less efficiently, saturation drops.</li>
<li><strong>The measurement itself:</strong> a moving arm, a loose band, a cold wrist or a tattoo can produce outlier values.</li>
</ul>

<h2>How the app uses your SpO₂</h2>
<p>The app pulls from Apple Health the saturation your watch measures while you sleep, and compares it with <a href="/methode/ligne-de-base.html">your baseline</a>: your average and standard deviation over the last 42 days, not counting the day being assessed. It takes at least 7 days of data for the signal to count, and 28 days for full confidence.</p>
<ul>
<li><strong>The direction:</strong> the higher your SpO₂ relative to your normal, the better. A drop costs you points.</li>
<li><strong>The threshold:</strong> at 2 standard deviations below your normal, this signal earns no points at all.</li>
<li><strong>The weight:</strong> 7% of the <a href="/methode/vitaux.html">vitals</a> pillar, which is worth 42 points out of 100. On a day when all the data is there, SpO₂ therefore weighs about 3 points of the score.</li>
</ul>
<p>That small weight is deliberate. SpO₂ is a useful warning signal, but it's noisier and less directly tied to your recovery than heart rate variability and resting heart rate, which together make up 75% of the pillar. Same logic for <a href="/methode/temperature-poignet.html">wrist temperature</a>, at 6%. If your watch didn't record your saturation, its weight is spread among the other vitals; without a watch, the whole pillar is redistributed.</p>

<h2>The limits of wrist measurement</h2>
<ul>
<li><strong>It's not a medical tool:</strong> your watch's saturation measurement is for wellness tracking, not diagnosis, and this app isn't a medical device.</li>
<li><strong>A single value doesn't mean much:</strong> what counts is repetition over several nights.</li>
<li><strong>The score observes; it doesn't explain:</strong> the app sees that your saturation is moving away from your normal, not why. A night at altitude, a cold or a loose band: you're the one with the context.</li>
</ul>

<h2>When to see a doctor</h2>
<p>Talk to a doctor if your SpO₂ is regularly low, if the people around you notice pauses in your breathing, or if you snore loudly and wake up tired despite full nights: these signs can raise suspicion of sleep apnea, which can be treated. Only a sleep study, ordered by a doctor, can settle the question.</p>
<p>Unusual shortness of breath, bluish lips or nails, chest pain or feeling faint: that's an emergency, so call your local emergency number (911 in the US, 999 or 112 in the UK and Europe). And never count on a watch to reassure you when you feel unwell.</p>
""",
    "refs": [
        "WHO (2011), pulse oximetry training manual." ' <a href="https://cdn.who.int/media/docs/default-source/patient-safety/pulse-oximetry/who-ps-pulse-oxymetry-training-manual-en.pdf" rel="noopener" target="_blank">who.int</a>',
        "Buchheit M. (2014), monitoring training status with heart rate measures, <em>Frontiers in Physiology</em>." ' <a href="https://doi.org/10.3389/fphys.2014.00073" rel="noopener" target="_blank">doi:10.3389/fphys.2014.00073</a>',
    ],
    "faq": [
        {"q": "What is a normal blood oxygen saturation level?",
         "a": "In healthy adults, blood oxygen saturation (SpO₂) generally falls between 95 and 100%, with a slight dip during sleep. A value that's regularly lower, especially with symptoms, is worth discussing with a doctor."},
        {"q": "Is smartwatch blood oxygen accurate?",
         "a": "The watch uses the same principle as an oximeter, but at the wrist, with a weaker signal: it's less precise than a medical fingertip oximeter and sensitive to movement, how tight the band is and your skin. It's for following a trend, never for making a diagnosis."},
        {"q": "Why does my blood oxygen drop at night?",
         "a": "During sleep, you breathe a little less deeply, so a slight dip is normal. Altitude, a respiratory infection or breathing pauses can make it drop further; repeated drops along with snoring and waking up tired are reason enough to talk to a doctor."},
    ],
}
