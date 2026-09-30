# -*- coding: utf-8 -*-
"""English version of /methode/age-biologique.html → /en/methode/biological-age.html.

Translation of tools/methode/age_biologique.py: same facts and links. As in French,
no number from the calculation (caps, margins, bounds, numeric references) is
published here; they stay in lib/bioAge. related / journal / kind / num / order /
date are taken from the French page.
"""

PAGE = {
    "fr": "age-biologique",
    "slug": "biological-age",
    "label": "Biological age",
    "title": "Biological age, anchored on your VO₂max",
    "seo_title": "Biological age: how it's calculated, step by step",
    "description": "Your biological age starts from your VO₂max, converted into a fitness age, then seven everyday factors adjust it. Sources, bounds, margin of error: the method.",
    "lead": "Ecleptic estimates your body's age in two steps: your VO₂max gives a <strong>fitness age</strong>, then seven factors drawn from your habits adjust it, each within strict limits. Here is the method, step by step, with its sources and its safeguards.",
    "body": """
<h2>What the engine calculates</h2>
<p>Your chronological age counts the years that have gone by. Your biological age estimates something else: <strong>how old your body is, judging by your fitness and your habits</strong>. Two people born the same year can be years apart on that front, and that gap is what the engine puts a number on.</p>
<p>The calculation happens in two steps. First, your <a href="/methode/vo2max.html">VO₂max</a>, the marker research most strongly links to longevity, is converted into a fitness age. Then seven modifiers drawn from your habits adjust that age. Each one is bounded and signed: with a “+”, it ages you; with a “−”, it makes you younger.</p>
<div class="figs">
  <div><span class="v">4</span><span class="u">VO₂max sources, from your watch to your BMI</span></div>
  <div><span class="v">7</span><span class="u">everyday factors, bounded and signed</span></div>
  <div><span class="v">Day 0</span><span class="u">a first estimate as soon as you sign up</span></div>
</div>

<h2>Step 1 · Finding your best VO₂max</h2>
<p>VO₂max is the maximum volume of oxygen your body can use per minute during an all-out effort. The app takes it from the <strong>best available source</strong>, in this order:</p>
<ul>
<li><strong>Measured by your watch:</strong> the “Cardio Fitness” value recorded in Apple Health, calculated during your outdoor workouts.</li>
<li><strong>Calculated from your runs:</strong> with Jack Daniels' VDOT formula, a standard in endurance training for more than forty years, which derives a VO₂max from a distance and a time.</li>
<li><strong>Estimated without exercise:</strong> with the equation from Nes et al., built on Norway's HUNT cohort, using your waist circumference, your <a href="/methode/frequence-cardiaque-repos.html">resting heart rate</a> and your activity level.</li>
<li><strong>As a fallback:</strong> with the equation from Jackson et al. (1990), using your BMI.</li>
</ul>
<p>Runs follow a rule of caution. <strong>A run isn't necessarily a maximal effort</strong>, and an easy jog underestimates your VO₂max. So VDOT can only raise the no-exercise estimate, never lower it. Without a baseline estimate, a VDOT below the value expected for your age is ignored: a simple jog shouldn't make you older.</p>
<p>The more direct the source, the more precise the result: the margin of uncertainty on your biological age is narrowest when your watch measures your VO₂max, and it widens as the source becomes more indirect.</p>

<h2>Step 2 · Converting your VO₂max into a fitness age</h2>
<p>A VO₂max on its own doesn't mean much: the same value can be excellent at 60 and ordinary at 25. So the app compares it with the <strong>reference value for your age and sex</strong>, then translates the gap into years. Above the reference, your fitness age drops below your chronological age; below it, your fitness age rises above.</p>
<p>This conversion relies on research from the HUNT cohort, a large Norwegian population study in which the VO₂max of thousands of adults was measured in the lab. It's the anchor of the calculation: everything else adjusts it, never replaces it.</p>

<h2>Step 3 · Seven modifiers, bounded and signed</h2>
<p>Your fitness age is then adjusted by your habits. The factors don't all carry the same weight, and each has its own cap, so that no single one can swing the result on its own:</p>
<ul>
<li><strong>Heart rate variability.</strong> Your <a href="/methode/variabilite-cardiaque.html">HRV</a> is compared with the values expected for your age: above them, it makes you younger; below them, it ages you. If you take a medication that slows the heart, it counts for less.</li>
<li><strong>Resting heart rate.</strong> It's placed against a reference value: lower, it makes you younger; higher, it ages you.</li>
<li><strong>Waist circumference.</strong> It's compared with the risk thresholds set by the World Health Organization (WHO), which differ for men and women.</li>
<li><strong>Activity.</strong> Your weekly minutes of activity, against the WHO recommendations.</li>
<li><strong>Sleep.</strong> This factor isn't symmetrical: disrupted sleep can age you more than good sleep can make you younger. Nights of sufficient length, without overdoing it, and regular bedtimes work in your favor; nights that are too short or too long and irregular bedtimes weigh the other way. The details: <a href="/methode/besoin-de-sommeil.html">your sleep need</a>.</li>
<li><strong>Diet.</strong> The quality of what you eat, as measured by your <a href="/methode/nutrition.html">nutrition score</a>.</li>
<li><strong>Lifestyle.</strong> What you report: nicotine, and alcohol based on the number of days a week you drink. This factor can never make you younger.</li>
</ul>
<p>One rule prevents counting the same thing twice. <strong>Resting heart rate, waist circumference and activity only act as modifiers if your VO₂max is measured by your watch or calculated from your runs.</strong> When it's estimated without exercise, they're switched off: the HUNT equation already contains all three, and counting them again would double their weight. Heart rate variability, sleep, diet and lifestyle, which no equation contains, apply as soon as the data exists.</p>

<h2>Step 4 · Bound it, smooth it, frame it</h2>
<ul>
<li><strong>Bounds:</strong> your biological age can't move away from your chronological age beyond a fixed limit, and it always stays within a realistic range of adult ages. It's a safeguard against outliers.</li>
<li><strong>Smoothing:</strong> the displayed value is an exponential moving average of your successive estimates. The most recent ones weigh more, but a single isolated measurement doesn't make the number jump.</li>
<li><strong>A margin of uncertainty:</strong> every result is calculated with its own, and its starting width depends on the source of your VO₂max.</li>
</ul>

<h2>Why these choices</h2>
<ul>
<li><strong>VO₂max as the anchor:</strong> it's the fitness marker research most strongly links to longevity. Even estimated without any exercise, from a few simple data points, cardiorespiratory fitness predicts long-term mortality: the Norwegian team behind the HUNT equation showed it.</li>
<li><strong>One anchor plus modifiers, not an average of everything:</strong> adding up overlapping factors would artificially inflate their effect. Each piece of data counts once, and only once.</li>
<li><strong>Caution with runs:</strong> a slow run doesn't prove low capacity. Better to ignore a run than to draw a false verdict from it.</li>
<li><strong>An honest number rather than a flattering one:</strong> the reference isn't chosen to please you. A flattering biological age would teach you nothing; an accurate number shows you what you still have to gain.</li>
<li><strong>A result from day one:</strong> the no-exercise equations allow a first estimate as soon as you sign up, without waiting for weeks of history. Its margin of uncertainty, wider at the start, reflects what that first number is worth.</li>
</ul>

<h2>What you see in the app</h2>
<ul>
<li><strong>Your biological age</strong>, smoothed over time, and how far it is from your chronological age.</li>
<li><strong>The factor breakdown</strong>, each with its effect in years: “+” if it ages you, “−” if it makes you younger.</li>
<li><strong>A first estimate as soon as you sign up</strong>, which sharpens as your watch, workouts, nights and meals feed the calculation.</li>
</ul>
<p>The most powerful lever is still the anchor: your VO₂max can be trained at any age, and every gain shows up in your fitness age. The method to raise it: <a href="/articles/vo2max-comment-l-ameliorer.html">how to improve your VO₂max</a>.</p>

<h2>What biological age is not</h2>
<p>It's a wellness indicator, not a medical diagnosis, and the app is not a medical device. It predicts neither your lifespan nor your future health: it's an estimate, with its margin of error, of how old your body is judging by your fitness and your habits. Given that margin, a one-year gap means nothing in itself; the trend over several months is what counts.</p>
<p>It's not a day-to-day indicator either. To know whether you can push today, check your <a href="/methode/readiness-score.html">Readiness Score</a>; biological age moves at the pace of your habits. And if you notice unusual shortness of breath, chest pain or palpitations, or you feel faint, see a doctor; in an emergency, call your local emergency number (911 in the US, 999 or 112 in the UK and Europe).</p>
""",
    "refs": [
        "Nes B. M. et al. (2011), estimating VO₂peak without an exercise test: the HUNT study, <em>Medicine &amp; Science in Sports &amp; Exercise</em>." ' <a href="https://doi.org/10.1249/MSS.0b013e31821d3f6f" rel="noopener" target="_blank">doi:10.1249/MSS.0b013e31821d3f6f</a>',
        "Nes B. M. et al. (2014), a simple nonexercise model of cardiorespiratory fitness predicts long-term mortality, <em>Medicine &amp; Science in Sports &amp; Exercise</em>." ' <a href="https://doi.org/10.1249/MSS.0000000000000219" rel="noopener" target="_blank">doi:10.1249/MSS.0000000000000219</a>',
        "Jackson A. S. et al. (1990), prediction of aerobic capacity without exercise testing, <em>Medicine &amp; Science in Sports &amp; Exercise</em>." ' <a href="https://doi.org/10.1249/00005768-199012000-00021" rel="noopener" target="_blank">doi:10.1249/00005768-199012000-00021</a>',
        "Daniels J. and Gilbert J. (1979), VDOT performance tables, <em>Oxygen Power</em>." ' <a href="https://books.google.com/books?id=h7f_tgAACAAJ" rel="noopener" target="_blank">Google Books</a>',
        "WHO (2011), waist circumference and waist-hip ratio: report of an expert consultation." ' <a href="https://www.who.int/publications/i/item/9789241501491" rel="noopener" target="_blank">who.int</a>',
    ],
    "faq": [
        {"q": "How does Ecleptic calculate biological age?",
         "a": "In two steps. Your VO₂max, measured by your watch, calculated from your runs or estimated without exercise, is converted into a fitness age; then seven factors adjust it, each within a fixed limit: heart rate variability, resting heart rate, waist circumference, activity, sleep, diet and lifestyle."},
        {"q": "Can you find out your biological age without a smartwatch?",
         "a": "Yes. Without a VO₂max measured by a watch, Ecleptic estimates it without exercise using the HUNT equation (waist circumference, resting heart rate, activity level) or the Jackson equation (BMI), and a hard-paced run can raise that estimate through the VDOT formula. The result is simply less precise: its starting margin of uncertainty is wider than with a VO₂max measured by your watch."},
        {"q": "Why is my biological age higher than my real age?",
         "a": "Either your VO₂max, the anchor of the calculation, is below the reference value for your age and sex, or some factors are aging you, such as nights that are too short, too long or irregular, heart rate variability that's low for your age, nicotine or alcohol. Also keep the margin of uncertainty in mind, wider when your VO₂max is estimated without exercise: a small gap may mean nothing; the trend over several months is what counts."},
    ],
}
