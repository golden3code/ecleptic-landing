# -*- coding: utf-8 -*-
"""English version of /methode/vo2max.html → /en/methode/vo2max.html.

Translation of tools/methode/vo2max.py: same facts and links (anchor of biological age,
sources in order of priority: Apple Health Cardio Fitness, Daniels' VDOT as a cautious
upward adjustment only, Nes HUNT equation, Jackson/BMI equation; starting margin of
uncertainty by source, figures not published; VO₂max is not part of the Readiness
Score). related / journal / kind / num / order / date are taken from the French page.
"""

PAGE = {
    "fr": "vo2max",
    "slug": "vo2max",
    "label": "VO₂max",
    "title": "VO₂max, your cardiorespiratory fitness",
    "seo_title": "VO2 max: what it is, how it's measured, link to longevity",
    "description": "VO₂max is the maximum oxygen your body can use during exercise. What it means, lab vs. watch measurement, benchmarks, and its role in your biological age.",
    "lead": "It's the number that best sums up your aerobic engine, and one of the numbers research links most strongly to longevity. Here's what it measures, how to estimate it without a lab, and how the app uses it to calculate your <strong>biological age</strong>.",
    "body": """
<h2>What does VO₂max measure?</h2>
<p>VO₂max (often written VO2 max) is the <strong>maximum volume of oxygen your body can use per minute during an all-out effort</strong>. It's expressed in milliliters per kilogram of body weight per minute (mL/kg/min), which makes it possible to compare people of different builds.</p>
<p>This number sums up the whole oxygen chain: your <strong>lungs</strong> pass it into your blood, your <strong>heart</strong> pumps it, your <strong>blood vessels</strong> deliver it, and your <strong>muscles</strong> use it to produce energy. In a healthy person, it's mainly the heart's pumping capacity that sets the ceiling.</p>

<h2>Why VO₂max matters so much</h2>
<p>Cardiorespiratory fitness is one of the most powerful predictors of all-cause mortality. The large studies that have measured it in tens of thousands of people all point the same way: the higher it is, the lower the risk. And <strong>the least fit have the most to gain</strong>: moving out of the lowest group is the step that pays off the most.</p>

<h2>How is VO₂max measured?</h2>
<ul>
<li><strong>In the lab:</strong> an exercise test with analysis of the gases you breathe remains the gold standard. On a treadmill or a bike, the intensity climbs until exhaustion while a mask measures the oxygen you consume.</li>
<li><strong>With a watch:</strong> it estimates your VO₂max during an outdoor workout, from your heart rate and your pace measured by GPS.</li>
<li><strong>Without exercise:</strong> equations estimate it from simple data. The one by Nes et al. (2011), developed on Norway's HUNT cohort, uses waist circumference, resting heart rate and activity level; the one by Jackson et al. (1990) relies notably on BMI.</li>
<li><strong>From your runs:</strong> Jack Daniels' VDOT formula derives a VO₂max from a time you ran over a given distance, provided the effort was truly maximal.</li>
</ul>

<h2>What's a good VO₂max? Very personal values</h2>
<p>There's no such thing as a good VO₂max in absolute terms. It peaks in young adulthood, then declines with age. At the same age, it's lower on average in women, notably because their blood contains less hemoglobin and their share of body fat is higher. Genetics count too: with the same training, not everyone improves at the same rate. In the best endurance athletes, it can exceed 80 mL/kg/min.</p>
<p>So a VO₂max is never read on its own, but <strong>against the reference values for your age and sex</strong>. That's exactly what the app does.</p>

<h2>What moves your VO₂max</h2>
<ul>
<li><strong>Zone 2 endurance:</strong> volume at an easy pace, where you can still talk, builds the base, with a heart that pumps more blood with each beat and more capillaries and mitochondria in your muscles. The details: <a href="/articles/zone-2-cardio-cest-quoi.html">what zone 2 cardio is</a>.</li>
<li><strong>Intervals:</strong> short repeats close to your max push the ceiling itself. One or two sessions a week, built on that base, are enough. How much to do: <a href="/articles/hiit-combien-de-fois-par-semaine.html">how many HIIT sessions a week</a>.</li>
<li><strong>Weight:</strong> since it's calculated per kilogram, losing body fat raises your relative VO₂max.</li>
<li><strong>Inactivity:</strong> a few weeks without training are enough to make it slip. It needs maintaining.</li>
<li><strong>Altitude:</strong> the air there delivers less oxygen, and your VO₂max drops for as long as you stay.</li>
</ul>
<p>Above all, it's trainable at any age. After 40, progress is still real, as long as you pay more attention to <a href="/articles/recuperation-apres-40-ans.html">recovery</a>. The full plan: <a href="/articles/vo2max-comment-l-ameliorer.html">how to improve your VO₂max</a>.</p>

<h2>How the app reads and uses your VO₂max</h2>
<p>In the app, VO₂max is <strong>the anchor of your <a href="/methode/age-biologique.html">biological age</a></strong>: it gives a fitness age, which your habits then adjust. The app takes it from the best available source, in this order; the more direct the source, the more precise your biological age:</p>
<ul>
<li><strong>Measured by your watch:</strong> the “Cardio Fitness” value read from Apple Health.</li>
<li><strong>Calculated from your runs:</strong> with the VDOT formula.</li>
<li><strong>Estimated without exercise:</strong> with the HUNT equation, from your waist circumference, your <a href="/methode/frequence-cardiaque-repos.html">resting heart rate</a> and your activity level.</li>
<li><strong>Failing that:</strong> with the Jackson equation, from your BMI.</li>
</ul>
<p>A rule of caution governs runs: since a run isn't necessarily a maximal effort, <strong>VDOT can only raise the no-exercise estimate, never lower it</strong>. Without a baseline estimate, a VDOT below the value expected for your age is ignored: a simple jog shouldn't make you older.</p>
<p>Unlike your <a href="/methode/variabilite-cardiaque.html">heart rate variability</a>, VO₂max isn't part of the <a href="/methode/readiness-score.html">Readiness Score</a>: it describes your capacity, which changes over weeks, not how you're doing today.</p>

<h2>The limits of the measurement</h2>
<p>Outside the lab, every VO₂max is an <strong>estimate</strong>. Your watch's is calculated only during certain outdoor workouts and depends on their conditions, such as elevation changes or heat. No-exercise equations are accurate on average, but can be clearly off for any given person. VDOT assumes a maximal effort. And a medication that slows the heart can skew estimates based on heart rate.</p>
<p>So the right way to read it is the <strong>trend over several weeks</strong>, not a single value. That's also why the app calculates your biological age with a margin of uncertainty and smooths its value over time.</p>

<h2>When to see a doctor</h2>
<p>This is a wellness app, not a medical device: your VO₂max isn't used to diagnose anything. See a doctor if it drops sharply and persistently for no apparent reason, or if exercise comes with unusual shortness of breath, chest pain, palpitations or feeling faint. In an emergency, call your local emergency number (911 in the US, 999 or 112 in the UK and Europe).</p>
<p>Before returning to intense training after a long break, especially if you have cardiovascular risk factors, get medical advice. An exercise stress test, ideally with gas analysis, checks that your heart can keep up and measures your VO₂max for real.</p>
""",
    "refs": [
        "Kodama S. et al. (2009), cardiorespiratory fitness as a predictor of all-cause mortality, <em>JAMA</em>." ' <a href="https://doi.org/10.1001/jama.2009.681" rel="noopener" target="_blank">doi:10.1001/jama.2009.681</a>',
        "Mandsager K. et al. (2018), cardiorespiratory fitness and long-term mortality, <em>JAMA Network Open</em>." ' <a href="https://doi.org/10.1001/jamanetworkopen.2018.3605" rel="noopener" target="_blank">doi:10.1001/jamanetworkopen.2018.3605</a>',
        "Nes B. M. et al. (2011), estimating VO₂peak without an exercise test: the HUNT study, <em>Medicine &amp; Science in Sports &amp; Exercise</em>." ' <a href="https://doi.org/10.1249/MSS.0b013e31821d3f6f" rel="noopener" target="_blank">doi:10.1249/MSS.0b013e31821d3f6f</a>',
        "Jackson A. S. et al. (1990), prediction of aerobic capacity without exercise testing, <em>Medicine &amp; Science in Sports &amp; Exercise</em>." ' <a href="https://doi.org/10.1249/00005768-199012000-00021" rel="noopener" target="_blank">doi:10.1249/00005768-199012000-00021</a>',
        "Daniels J. and Gilbert J. (1979), VDOT performance tables, <em>Oxygen Power</em>." ' <a href="https://books.google.com/books?id=h7f_tgAACAAJ" rel="noopener" target="_blank">Google Books</a>',
    ],
    "faq": [
        {"q": "What is a good VO₂max for your age?",
         "a": "There's no universal threshold: VO₂max is read according to age and sex, because it declines over the years and remains lower on average in women. What counts is where you stand against the reference values for your age, and how you progress over time; the best endurance athletes can exceed 80 mL/kg/min."},
        {"q": "Is Apple Watch VO₂max accurate?",
         "a": "It's an estimate, not a lab measurement: the watch derives it notably from your heart rate and your pace during an outdoor workout. It's mostly useful for tracking your trend over several weeks; only an exercise test with gas analysis gives a direct measurement."},
        {"q": "How can you increase your VO₂max after 40?",
         "a": "It's trainable at any age: combine plenty of easy zone 2 endurance, where you can still talk, with one or two interval sessions a week, leaving recovery days between them. Progress is measured in months. If you're returning after a long break or have cardiovascular risk factors, get medical advice first."},
    ],
}
