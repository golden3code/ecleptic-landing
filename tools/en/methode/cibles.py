# -*- coding: utf-8 -*-
"""English version of /methode/cibles.html → /en/methode/targets.html.

Translation of tools/methode/cibles.py: same facts, formulas and links
(Mifflin-St Jeor × 1.3/1.4/1.55/1.7, −78 constant if sex unspecified, 10-day
half-life, 14-day intake, ≥ 10 days of meals + ≥ 3 weigh-ins, valid days/21,
−10%/+25% damping, BMR and 1.2 × BMR checks, 7,700 / 5,500 kcal/kg, goal offsets,
protein 2.2 / 1.6 g/kg, fat 30% (≥ 0.8 g/kg), safeguards, day types, luteal phase,
Travel / illness switch). Imperial equivalents added once, in parentheses.
related / journal / kind / num / order / date are taken from the French page.
"""

PAGE = {
    "fr": "cibles",
    "slug": "targets",
    "label": "Targets",
    "title": "Targets, calibrated on what you actually burn",
    "seo_title": "Calorie and macro targets: how they're calculated",
    "description": "How Ecleptic calculates your calorie and macro targets: expenditure recalibrated from your weigh-ins and meals, your goal, and strict safeguards.",
    "lead": "How much you really burn, and so how much you should eat: the app doesn't guess it once and for all, <strong>it measures it from your actual weigh-ins and meals</strong>. Here is every step of the calculation, from the starting formula to your calorie and macro targets.",
    "body": """
<h2>What the engine calculates</h2>
<p>The targets engine answers two questions, in this order. First: <strong>how much do you really burn per day?</strong> That's your <a href="/methode/depense-energetique.html">energy expenditure</a>, or TDEE. Then: <strong>given your goal, how much should you eat, and in what split?</strong> Those are your calorie, protein, fat and carb targets.</p>
<p>A formula filled in on day one gives a ballpark figure, not your metabolism. The app only uses it as a starting point: after that, <strong>your expenditure is recalibrated continuously from your actual weigh-ins and meals</strong>. This is the observed energy balance method, the only one that converges on your own metabolism, not on that of a population average.</p>

<h2>The starting point: a formula</h2>
<p>On day one, the app knows neither your meals nor how your weight is trending. So it calculates your resting metabolic rate with the <strong>Mifflin-St Jeor</strong> equation, published in 1990 for healthy adults, from your weight, height, age and sex: 10 × weight (kg) + 6.25 × height (cm) − 5 × age, then + 5 for a man, − 161 for a woman, or − 78, the average of the two, if you haven't specified your sex.</p>
<p>This resting metabolic rate is then multiplied by an activity factor, based on your training level:</p>
<ul>
<li><strong>Beginner:</strong> × 1.3.</li>
<li><strong>Occasional:</strong> × 1.4.</li>
<li><strong>Regular:</strong> × 1.55.</li>
<li><strong>Intensive:</strong> × 1.7.</li>
</ul>
<p>Example: a 30-year-old man who weighs 80 kg (176 lb) and is 1.80 m (5 ft 11 in) tall has a resting metabolic rate of 1,780 kcal. If he trains regularly, his starting expenditure is about 2,760 kcal a day. That's a population estimate: for any given person, the error can exceed several hundred kilocalories a day. Hence the next step.</p>

<h2>Your real expenditure, read from your own energy balance</h2>
<p>The principle fits in one sentence: if your weight is stable, you eat what you burn; if it drops, you burn more; if it rises, less. So by crossing what you eat with how your weight changes, you can work back to what you really burn. The app crosses two data series:</p>
<ul>
<li><strong>Your weight trend:</strong> a smoothed average of your weigh-ins, with a 10-day half-life, where recent weigh-ins count more. Outlier weigh-ins are clipped: a temperamental scale doesn't make the trend.</li>
<li><strong>The intake you actually logged:</strong> the average of your meals over the last 14 days. How the app analyzes each meal: <a href="/methode/nutrition.html">Nutrition</a>.</li>
</ul>
<p>Observed expenditure is then calculated like this: <strong>average intake − (weight change per week × energy density) ÷ 7</strong>. Energy density is 7,700 kcal per kilo (about 3,500 kcal per pound), or 5,500 kcal per kilo when your goal is muscle gain, because weight gained while building muscle holds less energy. These values remain approximations, discussed in the <a href="/methode/depense-energetique.html">energy expenditure</a> explainer.</p>
<p>Example: you log an average of 2,200 kcal a day and your trend drops by 0.4 kg (about 0.9 lb) a week. That loss is worth 0.4 × 7,700 = 3,080 kcal a week, or 440 kcal a day: your observed expenditure is about 2,640 kcal.</p>
<p>This measurement only kicks in if it rests on enough data: <strong>at least 10 days of logged meals out of 14</strong> and <strong>at least 3 weigh-ins</strong> over the period. Otherwise, the formula prevails.</p>

<h2>A gradual, monitored handover</h2>
<p>The measurement doesn't replace the formula all at once. Its weight in the calculation equals the number of valid days, meaning your days with logged meals, <strong>divided by 21</strong>; the rest comes from the formula. As long as data is missing, it's the formula; after that, a blend that leans further toward your measurement the more consistently you log your meals.</p>
<p>Each new estimate is then <strong>dampened</strong> relative to the previous one: your expenditure can't drop by more than 10% or rise by more than 25% from one calculation to the next. The asymmetry is deliberate. A week of water retention shouldn't make your targets swing; on the other hand, after a stretch when you logged your meals less carefully, the rebound needs to be quick.</p>
<p>Finally, two plausibility checks set aside the observed estimate when the data tells an impossible story:</p>
<ul>
<li><strong>Below your resting metabolic rate:</strong> a total expenditure lower than what your body burns at rest makes no sense.</li>
<li><strong>Intake too low for a weight that isn't dropping:</strong> below 1.2 times your resting metabolic rate, with no drop in your weight, it's a sign that meals weren't logged, not of a real deficit.</li>
</ul>
<p>In both cases, the formula takes over again. An honest estimate beats a wrong measurement.</p>

<h2>From your expenditure to your targets</h2>
<p>Once your expenditure is estimated, your goal sets the adjustment to apply:</p>
<div class="figs">
  <div><span class="v">−18%</span><span class="u">Weight loss</span></div>
  <div><span class="v">+12%</span><span class="u">Muscle gain</span></div>
  <div><span class="v">+7%</span><span class="u">Strength</span></div>
  <div><span class="v">0%</span><span class="u">Maintenance, cardio, endurance</span></div>
</div>
<p>Protein is set first, in grams per kilo of body weight:</p>
<ul>
<li><strong>2.2 g/kg (about 1 g per pound):</strong> weight loss, muscle gain and strength building. In a deficit, it helps preserve your muscle; in a surplus, it supplies what you need to build it.</li>
<li><strong>1.6 g/kg (about 0.7 g per pound):</strong> maintenance, better cardio and endurance.</li>
</ul>
<p>Next comes <strong>fat, at 30% of calories</strong>, never dropping below 0.8 g per kilo: a minimum of fat remains essential, even in a deficit. <strong>Carbs make up</strong> the rest. The benchmarks behind these choices: <a href="/articles/proteines-par-jour-prise-de-muscle.html">how much protein per day</a> and <a href="/articles/glucides-et-sport-combien.html">how many carbs you need when you train</a>.</p>
<p>Back to our example. For weight loss, 2,760 kcal × 0.82 gives a target of about 2,260 kcal: 176 g of protein (2.2 × 80 kg), 75 g of fat (30% of calories) and about 220 g of carbs.</p>

<h2>Non-negotiable safeguards</h2>
<p>Some rules come before your goal, whatever it is:</p>
<ul>
<li><strong>BMI under 18.5:</strong> no deficit. Losing weight makes no sense when your build is already below the normal range.</li>
<li><strong>Under 18:</strong> no deficit. A growing body shouldn't be put on a diet by an app.</li>
<li><strong>Losing too fast:</strong> if your observed loss exceeds 1.5% of your body weight per week, the deficit is slowed to −10%. Losing weight too fast comes more at the expense of muscle.</li>
<li><strong>Sleep debt:</strong> if your nights over the past week add up to at least 5 hours of shortfall against 7 hours a night, across at least 4 logged nights, the deficit is limited to −15%. A long night doesn't make up for a short one. When you're short on sleep, a deficit is harder to stick to and costlier for your muscle.</li>
<li><strong>A capped rate of loss:</strong> your deficit never exceeds the equivalent of losing 1% of your body weight per week, about 11 kcal per kilo per day: 880 kcal at most at 80 kg.</li>
<li><strong>A calorie floor:</strong> your target never drops below your resting metabolic rate, nor below 1,200 kcal for a woman and 1,500 kcal for a man or if you haven't specified your sex. Your protein then stays the same; fat is recalculated and carbs take the rest.</li>
</ul>

<h2>When your targets change</h2>
<p>Your expenditure is re-estimated <strong>every night</strong>, and your targets are also recalculated when you weigh in or log your meals. So they follow your reality, week after week: if your weight moves faster or slower than expected, they adjust. Three situations also change them:</p>
<ul>
<li><strong>Your day:</strong> the app distinguishes five levels based on your active minutes, from rest to an intense day (1 hr 45 min or more), through very light, light (30 min) and moderate (1 hr). An active day gets a bonus of 4 kcal per active minute, calculated from your days at the same level over the past two weeks, 600 kcal at most; a rest day gets an offsetting cut, 300 kcal at most, so that on average your week stays close to your target. The whole difference goes through carbs: protein and fat don't move. The day's level is read from your workouts and your steps.</li>
<li><strong>Your cycle:</strong> if you track your menstrual cycle in the app, with your explicit consent and not on the combined pill, your target is raised by 150 kcal during your estimated luteal phase, once two complete cycles are logged. Around the start of your period, the measurement of your expenditure is set aside and the formula takes over again: water retention would skew your weight trend.</li>
<li><strong>Travel or illness:</strong> the “Travel / illness” switch freezes the estimate of your expenditure while it's on, then for seven more days. Random meals or a lost appetite shouldn't rewrite your metabolism. Only the measurement is frozen: your goal doesn't change.</li>
</ul>
<p>Your targets also count in your score: how well your day matches them makes up <strong>40% of the nutrition pillar</strong> of the <a href="/methode/readiness-score.html">Readiness Score</a>. Wrong targets would skew that pillar; one more reason for them to match your real expenditure.</p>

<h2>What this engine is not</h2>
<p>It's not a lab measurement. Your targets are only as good as your data: forgotten meals or infrequent weigh-ins delay the switch to your real expenditure, and the 7,700 kcal-per-kilo rule remains an approximation. The engine is designed to converge on your real expenditure smoothly, not to be accurate to the last kilocalorie.</p>
<p>Nor is it medical dietary care. The app is a wellness tool, not a medical device: it doesn't diagnose anything and replaces neither a doctor nor a dietitian. If you have a chronic disease, are pregnant, have a history of eating disorders or have lost weight without explanation, a health professional should set your intake.</p>
""",
    "refs": [
        "Mifflin M. D., St Jeor S. T. et al. (1990), a new equation for resting metabolic rate in healthy adults, <em>American Journal of Clinical Nutrition</em>." ' <a href="https://doi.org/10.1093/ajcn/51.2.241" rel="noopener" target="_blank">doi:10.1093/ajcn/51.2.241</a>',
        "Hall K. D. et al. (2011), quantifying the effect of energy imbalance on body weight, <em>The Lancet</em>." ' <a href="https://doi.org/10.1016/S0140-6736(11)60812-X" rel="noopener" target="_blank">doi:10.1016/S0140-6736(11)60812-X</a>',
    ],
    "faq": [
        {"q": "Why do my calorie targets change from week to week?",
         "a": "Because your expenditure is re-estimated from your weigh-ins and logged meals: if your weight moves faster or slower than expected, your targets follow. Changes are dampened, never more than 10% down or 25% up from one calculation to the next, so a week of water retention doesn't make them swing."},
        {"q": "How much protein do you need per day for your goal?",
         "a": "In Ecleptic, 2.2 g per kilo of body weight for weight loss, muscle gain and strength building, and 1.6 g per kilo for maintenance, cardio and endurance. Fat then covers 30% of calories, never less than 0.8 g per kilo, and carbs make up the rest."},
        {"q": "Do you need to weigh yourself every day to adjust your calories?",
         "a": "No, but you do need regular weigh-ins: the app measures your real expenditure once it has at least 3 weigh-ins and 10 days of logged meals out of the last 14. The more often you weigh yourself, the more reliable the trend, and a single weigh-in carries little weight, because outliers are clipped."},
    ],
}
