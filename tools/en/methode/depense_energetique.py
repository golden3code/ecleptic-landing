# -*- coding: utf-8 -*-
"""English version of /methode/depense-energetique.html → /en/methode/energy-expenditure.html.

Translation of tools/methode/depense_energetique.py: same facts and links (Mifflin-St Jeor
start × 1.3/1.4/1.55/1.7, smoothed weight trend with a 10-day half-life and outlier
weigh-ins removed, 14 days of intake, ≥ 10 days of meals + ≥ 3 weigh-ins, 7,700 kcal/kg
(5,500 for a muscle-gain goal), plausibility safeguards, nightly re-estimation; resting
metabolism 60-70%, thermic effect ≈ 10%, 7,700 kcal/kg as an approximation, Hall 2011).
Imperial equivalents added: 61 kg (134 lb), 1.68 m (5 ft 6 in), 7,700 kcal/kg ≈ 3,500
kcal/lb. related / journal / kind / num / order / date are taken from the French page.
"""

PAGE = {
    "fr": "depense-energetique",
    "slug": "energy-expenditure",
    "label": "Energy expenditure (TDEE)",
    "title": "Energy expenditure, measured rather than guessed",
    "seo_title": "TDEE: how to actually measure your energy expenditure",
    "description": "Energy expenditure (TDEE): its three components, why formulas can be off by several hundred kcal, and how Ecleptic measures yours from your own data.",
    "lead": "Your energy expenditure is everything your body burns in 24 hours. <strong>No formula truly knows it</strong>: day to day, the most reliable way to get close to it is to read it in how your weight changes against what you eat.",
    "body": """
<h2>What your energy expenditure covers</h2>
<p>Total energy expenditure, or <strong>TDEE</strong> (<em>total daily energy expenditure</em>), is all the energy your body burns in 24 hours. It breaks down into three parts:</p>
<ul>
<li><strong>Resting metabolism:</strong> what your heart, your brain, your organs and keeping your temperature steady cost, even when you're not moving. It's the biggest share, often 60 to 70% of the total.</li>
<li><strong>The thermic effect of food:</strong> the energy spent digesting and absorbing what you eat, about 10%.</li>
<li><strong>Activity:</strong> exercise and all the spontaneous movement of daily life. It's the most variable part, from one day to the next as well as from one person to another.</li>
</ul>

<h2>How it's measured</h2>
<p>In a lab, it's measured by <strong>indirect calorimetry</strong>: the oxygen you consume and the carbon dioxide you breathe out reveal how much energy your body produces. Over several days, the gold standard is doubly labeled water, which is accurate but reserved for research. In everyday life, that leaves three approaches:</p>
<ul>
<li><strong>Formulas:</strong> your resting metabolism calculated from your weight, height, age and sex, multiplied by an activity factor.</li>
<li><strong>Watches:</strong> your active calories, estimated from your heart rate and your movements. Useful for comparing your days, much less so for knowing your total.</li>
<li><strong>Observed energy balance:</strong> what you eat, compared with how your weight changes.</li>
</ul>

<h2>Why two people don't burn the same amount</h2>
<p>The best-known formulas (Harris-Benedict, the oldest, then Mifflin-St Jeor in 1990) were built on groups of people. They give a <strong>population average</strong>, not your value: for an individual, the error can exceed several hundred kilocalories a day.</p>
<p>A benchmark: for a 30-year-old woman who weighs 61 kg (134 lb), stands 1.68 m (5 ft 6 in) and exercises occasionally, the formula gives about 1,350 kcal at rest and 1,890 kcal a day. Yet another woman with the same build can burn more, or less, for two reasons the formula ignores:</p>
<ul>
<li><strong>Body composition:</strong> at the same weight, more muscle means a higher resting metabolism.</li>
<li><strong>Spontaneous activity:</strong> getting up often, pacing while on the phone, moving around while you work. It varies enormously from one person to another.</li>
</ul>
<p>For a first ballpark figure based on your profile: <a href="/articles/combien-de-calories-par-jour.html">how many calories a day</a>.</p>

<h2>What makes it shift</h2>
<ul>
<li><strong>Your activity:</strong> a workout, but also the sum of your steps and everything you do on your feet. Benchmarks: <a href="/articles/combien-de-pas-par-jour.html">how many steps a day</a> and <a href="/articles/cardio-ou-muscu-pour-maigrir.html">cardio or strength training for weight loss</a>.</li>
<li><strong>Your weight:</strong> a lighter body burns less. As you lose weight, your expenditure drops with you, and in a deficit people often move a little less without realizing it. A target set once and for all therefore ends up being wrong.</li>
<li><strong>Your diet:</strong> the more you eat, the more digestion costs, and protein costs a little more to digest than carbs or fat.</li>
</ul>

<h2>Observed energy balance: measuring rather than guessing</h2>
<p>If your weight is stable over several weeks, you're eating roughly what you burn. If it goes down or up, the gap between your intake and your expenditure shows up in the slope. Instead of guessing your expenditure, you <strong>deduce it from what your body actually does</strong>: it's the only everyday approach that converges on your metabolism, rather than on an average person's.</p>
<p>To convert kilos into energy, the usual figure is <strong>7,700 kcal per kilo</strong> (about 3,500 kcal per pound). It's a useful approximation over a few weeks, not an exact law: over the long term, it overestimates weight loss, because expenditure drops as weight goes down, as models published in <em>The Lancet</em> in 2011 showed.</p>
<p>Another trap: from one day to the next, the scale moves mostly with <strong>water and glycogen</strong>, the sugar stores in your muscles and liver, which are stored along with water. A salty or carb-heavy dinner is enough to push it up the next morning, without a single extra gram of fat. Hence the value of a smoothed trend over the day's weigh-in.</p>

<h2>How the app reads it</h2>
<p>The app applies exactly this principle, in two stages. At the start, with no data yet, it estimates your expenditure with the Mifflin-St Jeor equation, multiplied by an activity factor based on your exercise level: 1.3 beginner, 1.4 occasional, 1.55 regular, 1.7 intensive.</p>
<p>Then it cross-references your weight trend, smoothed and cleared of outlier weigh-ins, with the intake you've actually logged (see <a href="/methode/nutrition.html">Nutrition</a>):</p>
<div class="figs">
  <div><span class="v">14 days</span><span class="u">Of intake matched against your weight</span></div>
  <div><span class="v">10 days</span><span class="u">Half-life of the weight trend</span></div>
  <div><span class="v">10 / 14</span><span class="u">Days of logged meals, at minimum</span></div>
  <div><span class="v">3</span><span class="u">Weigh-ins minimum over the period</span></div>
</div>
<p>The conversion uses 7,700 kcal per kilo, or 5,500 when your goal is muscle gain. The switch from the formula to your own measurement is gradual and damped, and implausible estimates, given away by forgotten meals, are thrown out. Your expenditure is re-estimated every night, and your calorie and macro targets follow from it: all the details in <a href="/methode/cibles.html">Targets</a>. Those targets in turn count toward the nutrition pillar of the <a href="/methode/readiness-score.html">Readiness Score</a>.</p>

<h2>Limits, and when to see a doctor</h2>
<p>Observed energy balance is only as good as your data: forgotten meals make your expenditure look lower than it is, and infrequent weigh-ins delay the measurement.</p>
<p>The app is a wellness tool, not a medical device: it doesn't diagnose anything. Unexplained weight loss or gain, with no change in your habits, deserves a doctor's opinion. The same goes if you're pregnant, have a chronic illness or a history of eating disorders: it's up to a professional to set your intake. And if you feel faint, have palpitations or unusual shortness of breath while cutting back on food, stop and see a doctor; in an emergency, call your local emergency number (911 in the US, 999 or 112 in the UK and Europe).</p>
""",
    "refs": [
        "Mifflin M. D., St Jeor S. T. et al. (1990), a new predictive equation for resting energy expenditure in healthy individuals, <em>American Journal of Clinical Nutrition</em>." ' <a href="https://doi.org/10.1093/ajcn/51.2.241" rel="noopener" target="_blank">doi:10.1093/ajcn/51.2.241</a>',
        "Hall K. D. et al. (2011), quantification of the effect of energy imbalance on bodyweight, <em>The Lancet</em>." ' <a href="https://doi.org/10.1016/S0140-6736(11)60812-X" rel="noopener" target="_blank">doi:10.1016/S0140-6736(11)60812-X</a>',
    ],
    "faq": [
        {"q": "How do you calculate your daily energy expenditure?",
         "a": "A formula like Mifflin-St Jeor estimates your resting metabolism from your weight, height, age and sex; multiplied by an activity factor, it gives you a starting point. To know your real expenditure, the most reliable way is still to compare your intake with how your weight changes over at least two weeks."},
        {"q": "Is the 7,700 kcal per kilo rule (3,500 kcal per pound) true?",
         "a": "It's a useful approximation over a few weeks, not an exact law. Over the long term, it overestimates weight loss, because your expenditure drops as your weight goes down, and from one day to the next, water and glycogen move the scale far more than fat does."},
        {"q": "Why am I not losing weight in a calorie deficit?",
         "a": "Often, the deficit exists only on paper: a formula can overestimate your expenditure by several hundred kilocalories a day, and forgotten meals throw off the count. Water retention can also mask real weight loss for a few days: judge the trend over two weeks or more, and talk to a doctor if your weight changes for no clear reason."},
    ],
}
