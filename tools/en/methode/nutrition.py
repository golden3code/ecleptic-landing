# -*- coding: utf-8 -*-
"""English version of /methode/nutrition.html → /en/methode/nutrition.html.

Translation of tools/methode/nutrition.py: same facts and links (catalog of 438,267
entries = 433,631 USDA + 3,484 Ciqual + 1,152 mixed dishes, plus Open Food Facts;
up to 3 photos; 21 micronutrients; pillar 21 points, 40/25/20/15, alcohol cap 80).
The AI model provider is not named. related / journal / kind / num / order / date
are taken from the French page.
"""

PAGE = {
    "fr": "nutrition",
    "slug": "nutrition",
    "label": "Nutrition",
    "title": "Nutrition, from photo to official source",
    "seo_title": "Photo calorie counting: from AI scan to USDA and Ciqual",
    "description": "Meal scanning: AI recognizes the foods and estimates portions, while Ciqual, USDA and Open Food Facts supply the values. The method, and its limits.",
    "lead": "You snap a photo of your plate, and the app shows calories, macros and 21 micronutrients. Here is exactly what happens in between, and why <strong>no nutrition value is ever made up by the AI</strong>: they all come from official databases.",
    "body": """
<h2>What the engine calculates</h2>
<p>The nutrition engine answers a simple question: <strong>what did you actually eat, and what did it give you?</strong> For each meal, the app calculates and shows your calories, protein, carbs and fat, but also 21 micronutrients and your antioxidant intake.</p>
<p>It also counts what almost everyone forgets: <strong>the water in food</strong>. A soup, a piece of fruit or a yogurt hydrates you too, and that water counts toward your hydration for the day.</p>
<p>Everything rests on one non-negotiable rule: <strong>the AI identifies and estimates; official databases supply the values.</strong> The AI recognizes what's on your plate and estimates the portions. The values, on the other hand, always come from an entry published by a reference source: calories, macros, micronutrients, antioxidants. No nutrition value shown is an estimate made up by the AI.</p>

<h2>A catalog of 438,267 entries</h2>
<p>When you scan a meal, each food is matched to the public nutrition databases that serve as the reference:</p>
<ul>
<li><strong>The ANSES Ciqual table:</strong> France's food safety agency describes 3,484 foods in it, through 257,000 nutrient values measured in the lab. It's the reference table in France.</li>
<li><strong>USDA FoodData Central:</strong> the US Department of Agriculture's database, from which the app includes 433,631 products. It brings breadth: hundreds of thousands of entries, where Ciqual describes a few thousand.</li>
<li><strong>Open Food Facts:</strong> the collaborative database of barcoded products, with the values for one specific product, brand included.</li>
</ul>
<p>The catalog also includes <strong>1,152 mixed dishes</strong>, for plates that don't come down to a single food.</p>
<div class="figs">
  <div><span class="v">438,267</span><span class="u">Catalog entries</span></div>
  <div><span class="v">433,631</span><span class="u">USDA products</span></div>
  <div><span class="v">3,484</span><span class="u">Ciqual foods (ANSES)</span></div>
  <div><span class="v">1,152</span><span class="u">Mixed dishes</span></div>
</div>
<p>On top of these 438,267 entries come the barcoded products from Open Food Facts. Macros, micronutrients, antioxidants: <strong>every value shown in the app can be traced back to its official source.</strong></p>

<h2>From scan to entry, step by step</h2>
<ul>
<li><strong>The photo:</strong> you take a photo of your meal. Up to 3 photos per meal, merged into a single analysis, when everything doesn't fit in one frame.</li>
<li><strong>Recognition:</strong> the AI identifies the foods present and estimates the portion of each one.</li>
<li><strong>Matching:</strong> each recognized food is matched to a specific entry in the official databases. This is the decisive step: past this point, the AI doesn't supply a single number.</li>
<li><strong>Calculation:</strong> each entry's values are scaled to your portion, then added up to give the totals for the meal, and for your day.</li>
<li><strong>Correction:</strong> a food misidentified, a portion that needs adjusting? You correct it, and the calculation is redone with the right entry or the right amount.</li>
</ul>
<p>Two other entry points lead to the same databases. A packaged product's <strong>barcode</strong> takes you straight to its Open Food Facts entry. And <strong>manual search</strong> lets you find a food in the catalog when you'd rather enter it yourself.</p>

<h2>Why the values never come from the AI</h2>
<p>It would have been simpler to ask the AI, “How many calories are on this plate?” It would have answered, confidently. But a generated number isn't a measured number: it's plausible, unverifiable, and it can change from one photo of the same dish to the next.</p>
<p>Hence the separation of roles. The AI does what it's good at: recognizing foods and estimating quantities. The databases do what they're good at: describing a food's composition, entry by entry, with an identifiable source. The benefit is concrete: when a number surprises you, it traces back to an official entry, not to a machine's hunch.</p>
<p>And why several databases rather than one? Because none is enough on its own. Ciqual brings the rigor of lab-measured values for basic foods, but it doesn't describe every product on the shelves. Open Food Facts knows packaged products, brand by brand. USDA FoodData Central brings volume. Combining them covers your plate without sacrificing rigor.</p>

<h2>How much your nutrition weighs in your score</h2>
<p>Your meals aren't just for keeping a food log. They feed the nutrition pillar of the <a href="/methode/readiness-score.html">Readiness Score</a>, which is worth <strong>21 points out of 100</strong> and is scored on four criteria:</p>
<ul>
<li><strong>How well you hit your targets — 40%.</strong> The day's calories, protein, carbs and fat, against the targets calculated by the <a href="/methode/cibles.html">Targets</a> engine.</li>
<li><strong>Refueling after exercise — 25%.</strong> The protein you get after a workout, which gives your muscles the raw materials for repair (<a href="/articles/que-manger-apres-le-sport.html">what to eat after a workout</a>). On rest days, this criterion is removed and its weight is redistributed among the others.</li>
<li><strong>Micronutrients — 20%.</strong> How well your needs are covered, calculated from the values in the official entries.</li>
<li><strong>Hydration — 15%.</strong> Your hydration for the day, against what's recommended for you (<a href="/articles/combien-d-eau-boire-par-jour.html">how much water to drink a day</a>).</li>
</ul>
<p>One rule stands apart: <strong>if you drank alcohol the day before, the pillar is capped at 80 out of 100</strong>, even with flawless meals. Alcohol weighs on recovery, and no plate erases it.</p>
<p>Your nutrition also matters in the longer run: its score is one of the modifiers of your <a href="/methode/age-biologique.html">biological age</a>, which it can move in either direction. As for your calorie target, it only makes sense relative to what you burn: the <a href="/methode/depense-energetique.html">energy expenditure</a> explainer shows how your expenditure is estimated.</p>

<h2>The limits, no sugarcoating</h2>
<p>An honest nutrition engine has to say what it can't do.</p>
<ul>
<li><strong>A photo doesn't weigh your plate:</strong> portions are estimated, with a margin of error. An example: an entry with 10 g of protein per 100 g, on a portion estimated at 150 g, gives 15 g. If the real portion weighed 200 g, you're 5 g short. That's why you can correct it, and why the portion is the first thing to check.</li>
<li><strong>A food doesn't have a single composition:</strong> values vary with the variety, the cooking method and the brand. An entry describes a typical food, not exactly the one on your plate.</li>
<li><strong>Not all sources have the same status:</strong> Ciqual values are measured in the lab; Open Food Facts is a collaborative database, where a data-entry error is still possible.</li>
<li><strong>Read the trend, not the meal:</strong> a portion misjudged at one lunch weighs little over a week; a habit that repeats, on the other hand, eventually shows.</li>
</ul>

<h2>What this engine is not</h2>
<p>The app is a wellness tool, not a medical device. The nutrition engine shows you what you eat and what it gives you; it doesn't diagnose anything, doesn't prescribe any diet and doesn't replace dietary or medical advice.</p>
<p>If you follow a diet because of a medical condition, if you're pregnant, if you take medication, or if your relationship with food is becoming a source of anxiety, see a doctor or a dietitian, not an app. And if you feel unwell or notice an unusual symptom, get medical advice; in an emergency, call your local emergency number (911 in the US, 999 or 112 in the UK and Europe).</p>
""",
    "refs": [
        "ANSES, Ciqual food composition table." ' <a href="https://ciqual.anses.fr/" rel="noopener" target="_blank">ciqual.anses.fr</a>',
        "USDA, FoodData Central database." ' <a href="https://fdc.nal.usda.gov/" rel="noopener" target="_blank">fdc.nal.usda.gov</a>',
        "Open Food Facts, collaborative database of food products." ' <a href="https://fr.openfoodfacts.org/" rel="noopener" target="_blank">fr.openfoodfacts.org</a>',
    ],
    "faq": [
        {"q": "How does an app calculate the calories in a meal from a photo?",
         "a": "In Ecleptic, the AI recognizes the foods in the photo and estimates their portions. Each food is then matched to an entry in official databases (the Ciqual table from ANSES, France's food safety agency; USDA FoodData Central; Open Food Facts), and it's the values from those entries, scaled to your portion, that are shown."},
        {"q": "Are calories estimated from a photo accurate?",
         "a": "The tricky part is the portion: a photo doesn't weigh your plate, so the estimated amount has a margin of error. The nutrition values, however, come from official databases, not from an AI estimate, and you can correct a food or a portion that was misjudged. To judge your diet, look at the trend over several days rather than a single meal."},
        {"q": "What's the difference between the Ciqual table and Open Food Facts?",
         "a": "The Ciqual table is published by ANSES, France's food safety agency: it describes generic foods with values measured in the lab. Open Food Facts is a collaborative database of barcoded products, giving the values for one specific product from a given brand. Ecleptic relies on both, along with USDA FoodData Central, and links a scanned barcode to its Open Food Facts entry."},
    ],
}
