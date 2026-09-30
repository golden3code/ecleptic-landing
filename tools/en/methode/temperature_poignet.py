# -*- coding: utf-8 -*-
"""English version of /methode/temperature-poignet.html → /en/methode/wrist-temperature.html.

Translation of tools/methode/temperature_poignet.py: same facts and links (6% of the
42-point vitals pillar, deviation score penalized in both directions, 0 points beyond
2 standard deviations, 42-day baseline with the day excluded, min 7, full confidence 28,
missing signal → weight redistributed). related / journal / kind / num / order / date
are taken from the French page.
"""

PAGE = {
    "fr": "temperature-poignet",
    "slug": "wrist-temperature",
    "label": "Wrist temperature",
    "title": "Wrist temperature, a deviation rather than a number",
    "seo_title": "Wrist temperature at night: what the deviation means",
    "description": "Overnight wrist temperature is a deviation from your own normal, not a fever reading. What makes it shift, and how Ecleptic factors it into your score.",
    "lead": "Your watch doesn't take your temperature: night after night, it tracks <strong>how far your wrist departs from your own normal</strong>. It's a quiet signal that reacts to your cycle, to a virus, to a glass of wine, and to a comforter that's too warm.",
    "body": """
<h2>What the watch actually measures</h2>
<p>Wrist temperature, as your watch tracks it, is <strong>the deviation between the skin temperature at your wrist while you sleep and your own normal</strong>. It isn't your body temperature, and your watch isn't a thermometer: it's a relative marker that tells you whether your night ran warmer or cooler than usual.</p>
<p>In the app, it's the lightest of the five signals in the vitals pillar of the <a href="/methode/readiness-score.html">Readiness Score</a>, and the only one that reads in both directions.</p>

<h2>What it reflects in your body</h2>
<p>Your core temperature isn't fixed: it follows a 24-hour rhythm. In the evening, it drops to prepare you for sleep, and it hits its low point toward the end of the night. To cool down, your body releases heat through the skin, mostly through your hands and feet, whose blood vessels widen.</p>
<p>Your wrist sits at the crossroads: its temperature depends both on what's happening inside (your rhythm, your hormones, a fever coming on) and on what surrounds it (the bedroom, the comforter). That's what makes this signal rich, and hard to interpret on its own.</p>

<h2>Thermometer vs. watch: two different measurements</h2>
<p>A medical thermometer measures your core temperature, in the mouth, the ear or the rectum; in adults, it hovers around 37 °C (98.6 °F). The watch, on the other hand, measures the surface of your skin, which is cooler and far more sensitive to its surroundings. Its raw value therefore has no universal norm: that's why the reasoning is in deviations, against a reference that's specific to you.</p>
<p>Your watch needs <strong>a few nights to establish that reference</strong> before it can give you a deviation. And not every model measures this signal: it's a feature of recent Apple Watch models. The app then reads this data from Apple Health.</p>
<div class="figs">
  <div><span class="v">6%</span><span class="u">Of the vitals pillar</span></div>
  <div><span class="v">±2</span><span class="u">Standard deviations: 0 points</span></div>
  <div><span class="v">42</span><span class="u">Days of baseline</span></div>
  <div><span class="v">7</span><span class="u">Days to get started</span></div>
</div>

<h2>What makes it shift</h2>
<ul>
<li><strong>The menstrual cycle:</strong> after ovulation, basal temperature rises by a few tenths of a degree Celsius and stays higher until your next period. If you have periods, your deviation rises and falls over the month, and that's normal. To adapt your training: <a href="/articles/cycle-menstruel-et-sport.html">menstrual cycle and exercise</a>.</li>
<li><strong>Fever or infection:</strong> your temperature goes up, and your <a href="/methode/frequence-respiratoire.html">respiratory rate</a> often climbs along with it.</li>
<li><strong>Alcohol:</strong> it widens the blood vessels in your skin, your wrist warms up, and your night pays the price. The details in <a href="/articles/alcool-sommeil-effets.html">alcohol and sleep</a>.</li>
<li><strong>A late meal:</strong> digestion produces heat just as your body is trying to cool down.</li>
<li><strong>Your bedroom and bedding:</strong> a warm room or a thick comforter, and the deviation climbs; a cold bedroom, and it drops. The right benchmarks: <a href="/articles/temperature-ideale-chambre-dormir.html">the ideal temperature for sleep</a>.</li>
</ul>

<h2>How the app uses it</h2>
<p>The app pulls the wrist temperature measured during your sleep from Apple Health and compares it with <a href="/methode/ligne-de-base.html">your baseline</a>: your average and your standard deviation over the last 42 days, not counting the day being assessed. It takes at least 7 days of data for the signal to count, and 28 days for full confidence. Add the few nights your watch needs at the start, and this signal calls for a little patience.</p>
<ul>
<li><strong>Direction:</strong> here, there is no "better." Any deviation from your normal, warmer or cooler, costs points.</li>
<li><strong>Threshold:</strong> beyond 2 standard deviations, in either direction, this signal earns no points at all.</li>
<li><strong>Weight:</strong> 6% of the <a href="/methode/vitaux.html">vitals</a> pillar, which is worth 42 points out of 100. On a day when all the data is there, temperature therefore weighs about 2.5 points of the score.</li>
</ul>
<p>Why so little? It's a deliberate choice. Temperature is useful for spotting a night that's out of the ordinary, but it's noisier and less directly tied to your recovery than heart rate variability or resting heart rate: an overheated bedroom or a comforter that's too thick moves it with no connection to how fit you are. If your watch doesn't measure it, its weight is split among the other vitals; with no watch, the whole pillar is redistributed.</p>

<h2>The limits of the measurement</h2>
<ul>
<li><strong>It isn't a thermometer:</strong> the watch isn't meant to diagnose a fever. If you feel feverish, take your temperature with a real thermometer.</li>
<li><strong>Your environment blurs the signal:</strong> a night away from home, an open window, an arm under the comforter or on top of it: all nuances the watch can't tell apart from an internal change.</li>
<li><strong>The score observes, it doesn't explain:</strong> the app sees that your temperature is departing from your normal, not why. A virus, a glass of wine, your cycle or the radiator: it's up to you to connect the dots.</li>
</ul>

<h2>When to see a doctor</h2>
<p>A one-off deviation, especially after a night of drinking or in an overheated bedroom, is usually nothing to worry about. On the other hand, if you feel feverish, check with a thermometer, and see a doctor if the fever lasts several days or comes with symptoms that worry you. Also let your body heal before you train again: the rules are in <a href="/articles/reprendre-le-sport-apres-maladie.html">returning to exercise after being sick</a>.</p>
<p>Feeling faint, chest pain, unusual shortness of breath or palpitations are not things to monitor with a watch: get medical help right away and, in an emergency, call your local emergency number (911 in the US, 999 or 112 in the UK and Europe). The app is a wellness tool, not a medical device.</p>
""",
    "refs": [
        "Buchheit M. (2014), monitoring training status with heart rate measures, <em>Frontiers in Physiology</em>." ' <a href="https://doi.org/10.3389/fphys.2014.00073" rel="noopener" target="_blank">doi:10.3389/fphys.2014.00073</a>',
        "Miller D. J. et al. (2020), changes in nighttime respiratory rate and early detection of infection, <em>PLOS ONE</em>." ' <a href="https://doi.org/10.1371/journal.pone.0243693" rel="noopener" target="_blank">doi:10.1371/journal.pone.0243693</a>',
    ],
    "faq": [
        {"q": "What is wrist temperature on the Apple Watch for?",
         "a": "While you sleep, it tracks how far your wrist temperature departs from your own normal, established over a few nights. It isn't a body temperature: it's for spotting a night that breaks from your usual pattern, not for measuring a fever."},
        {"q": "Why is my wrist temperature higher than usual?",
         "a": "It can rise for ordinary reasons: a bedroom or comforter that's too warm, alcohol, a late meal, or the second half of the menstrual cycle, after ovulation. A fever or an infection can also push it up: if you feel unwell, check with a real thermometer."},
        {"q": "Can a smartwatch detect a fever?",
         "a": "No: it measures the skin of your wrist, which is influenced by your bedroom and bedding, not your core temperature. A deviation can prompt you to check, but only a thermometer confirms a fever; if it persists or comes with worrying symptoms, see a doctor."},
    ],
}
