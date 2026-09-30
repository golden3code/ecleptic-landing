# -*- coding: utf-8 -*-
# English version of batch A (Nutrition) — source: tools/satellites/batch_a.py.
# Sources are carried over automatically from the French entries.

ENTRIES = [
    {
        "fr": "combien-de-calories-par-jour",
        "slug": "how-many-calories-per-day",
        "title": "How many calories do you really need per day?",
        "description": "How many calories do you need per day? It depends on your metabolism and activity. Typical ranges, the limits of formulas, and how to find your real number.",
        "body": """
<p>The short answer: <strong>it depends on you</strong>. Your daily energy expenditure — the well-known <em>TDEE</em>, short for <strong>total daily energy expenditure</strong> — adds up your basal metabolic rate (what your body burns at rest, just to stay alive) and everything you move during the day. As a rough guide, that comes to about <strong>1,800 to 2,400 kcal</strong> for a woman and <strong>2,200 to 2,900 kcal</strong> for a man, from sedentary to active, according to reference values from the European Food Safety Authority (EFSA) — but these ranges are wide, and two people of the same weight can be 500 kcal apart.</p>
<p>The real message: there is no universal "right" number. Your needs depend on your height, your weight, your muscle mass, your age and, above all, how active you are — not just at the gym, but all day long. The good news is that you don't need to guess it perfectly: you start from a decent estimate, then let reality correct course.</p>

<h2>What your daily calorie burn is made of</h2>
<p>Four components, very unequal:</p>
<ul>
<li><strong>Basal metabolic rate (60-70%)</strong> — the energy your brain, heart, liver and muscles burn at rest. It's the biggest piece, and it depends mostly on your lean mass.</li>
<li><strong>Background activity, or NEAT (15-30%)</strong> — non-exercise activity: walking, standing, fidgeting, taking the stairs. It's the component that varies most from one person to the next, and the one that explains most of the differences.</li>
<li><strong>Exercise (5-15%)</strong> — often overestimated. A hard workout is 300 to 600 kcal, not 1,500.</li>
<li><strong>Digestion (~10%)</strong> — the energy spent processing what you eat: 5 to 15% of expenditure according to a 2004 review, a bit more when your plate is high in protein.</li>
</ul>

<h2>Calorie formulas: a starting point, not the truth</h2>
<p>The most reliable one is the <strong>Mifflin-St Jeor</strong> equation: a 2005 systematic review found it was the one that most often lands within 10% of measured metabolic rate. For a man: 10 × weight (kg) + 6.25 × height (cm) − 5 × age + 5; for a woman, the same calculation with −161 at the end (to convert, divide pounds by 2.2 and multiply inches by 2.54). That gives you your basal metabolic rate, which you then multiply by an activity factor: from 1.4 if you're sedentary to 2 if you're very active, according to EFSA.</p>
<div class="tablewrap"><table>
<caption>Source: EFSA (2013), average energy requirements for adults aged 30 to 39 (BMI of 22), converted to kcal.</caption>
<thead><tr><th>Activity level</th><th class="n">Women</th><th class="n">Men</th></tr></thead>
<tbody>
<tr><td>Sedentary (1.4)</td><td class="n">1,820 kcal</td><td class="n">2,270 kcal</td></tr>
<tr><td>Moderately active (1.6)</td><td class="n">2,080 kcal</td><td class="n">2,580 kcal</td></tr>
<tr><td>Active (1.8)</td><td class="n">2,340 kcal</td><td class="n">2,910 kcal</td></tr>
<tr><td>Very active (2.0)</td><td class="n">2,580 kcal</td><td class="n">3,220 kcal</td></tr>
</tbody>
</table></div>
<p>A concrete example: a 30-year-old man who weighs 75 kg (165 lb) and stands 178 cm (5'10") gets a basal metabolic rate of about <strong>1,720 kcal</strong>. Training three or four times a week (factor ~1.5), his total expenditure comes to around <strong>2,580 kcal</strong>. But keep this in mind: it's an <em>estimate</em>. Formulas can be off by 200 to 300 kcal either way, because they know neither your actual muscle mass nor how fidgety you are.</p>

<h2>How to find your maintenance calories: the scale over 2-3 weeks</h2>
<p>It's the only method that doesn't lie. Here's how to turn the estimate into a reliable number:</p>
<ul>
<li>Eat roughly at your estimated expenditure for <strong>2 to 3 weeks</strong>, without trying to lose or gain weight.</li>
<li>Weigh yourself in the morning on an empty stomach, and look only at the <strong>weekly average</strong> — a single day's weight means nothing (water, salt, digestion).</li>
<li>Stable weight → you've found your maintenance. Weight going up → your real expenditure is lower. Weight going down → it's higher. Adjust by 150-200 kcal and start again.</li>
</ul>
<p>That's exactly the logic you build on when you want to <a href="/articles/deficit-calorique-comment-calculer.html">calculate a calorie deficit</a> properly: you start from your real expenditure, not from a theoretical number.</p>

<h2>What affects how many calories you burn</h2>
<ul>
<li><strong>Your muscle mass.</strong> The more muscle you have, the higher your basal metabolic rate, even at rest — one of the long-term benefits of strength training, and a reason to <a href="/articles/proteines-par-jour-prise-de-muscle.html">eat enough protein</a>.</li>
<li><strong>Your background activity.</strong> In a study published in <em>Science</em> (2005), people with overweight sat 2 hours more per day than lean people: about 350 kcal less burned per day. <a href="/articles/combien-de-pas-par-jour.html">Your daily step count</a> often matters more than the workout itself.</li>
<li><strong>Age.</strong> Less than people think: according to a large study published in <em>Science</em> (2021), at equal lean mass, expenditure stays stable from age 20 to 60 and only declines after that. What drops before then is mostly muscle and movement — two things that are partly under your control.</li>
<li><strong>Sleep and stress.</strong> Poor sleep throws off appetite and spontaneous activity, which blurs the calculation around the edges.</li>
</ul>

<h2>Key takeaways</h2>
<ul>
<li>Your expenditure = basal metabolic rate + activity; as a rough guide, ~1,800-2,400 kcal (women) and ~2,200-2,900 kcal (men), highly variable.</li>
<li>Formulas like Mifflin-St Jeor give you a starting point within ±200-300 kcal, not the truth.</li>
<li>The only reliable method: eat at your estimate, track your average weight over 2-3 weeks, adjust.</li>
</ul>
""",
        "faq": [
            {"q": "How many calories should a woman eat per day?",
             "a": "As a rough guide, 1,800 to 2,400 kcal per day to maintain weight, depending on height, muscle mass, age and above all activity level. The range is wide: the only reliable way to find your own number is to track your weight over two to three weeks."},
            {"q": "How do you calculate your calorie needs?",
             "a": "Estimate your basal metabolic rate with the Mifflin-St Jeor equation, multiply it by an activity factor (from 1.4 if you're sedentary to 2 if you're very active, according to EFSA), then check it by tracking your average weight over 2-3 weeks. The estimate can be off by 200 to 300 kcal; the scale has the final say."},
            {"q": "How many calories should you eat to lose weight?",
             "a": "Subtract 300 to 500 kcal from your total expenditure, which leads to losing about 0.3 to 0.5 kg (0.7 to 1.1 lb) per week at first. Always start from your real expenditure, not from a standard number."},
        ],
    },
    {
        "fr": "deficit-calorique-comment-calculer",
        "slug": "how-to-calculate-a-calorie-deficit",
        "title": "Calorie deficit: how to calculate it the right way",
        "description": "Calorie deficit: 300 to 500 kcal below your expenditure, or about 0.3 to 0.5 kg a week at first. How to calculate it, stick to it and keep your muscle.",
        "body": """
<p>The short answer: start from your total daily energy expenditure and <strong>subtract 300 to 500 kcal per day</strong>. The pace to aim for: about <strong>0.5 to 1% of your body weight per week</strong>, the rate a 2014 review on bodybuilding contest prep recommends to best preserve muscle. In practice, a 300 to 500 kcal deficit leads to losing about 0.3 to 0.5 kg (0.7 to 1.1 lb) per week at first: the low end of that range for most people.</p>
<p>The classic mistake is calculating the deficit from a made-up number. A deficit only means something relative to <em>your</em> real expenditure: so start by estimating it, then track your weight to confirm it — <a href="/articles/combien-de-calories-par-jour.html">we break down the method here</a>. Without that starting point, you're calculating in a vacuum.</p>

<h2>How big should your calorie deficit be?</h2>
<p>A useful benchmark: about <strong>7,000 to 7,700 kcal</strong> roughly equals one kilo lost (the familiar "3,500 calories per pound"). A 2008 analysis from the National Institutes of Health considers this rule approximate: it mostly holds when you have a lot of fat to lose. A 500 kcal daily deficit is ~3,500 kcal over the week, or roughly half a kilo — a ballpark, not a Swiss watch. Three ways to create that deficit, best combined:</p>
<ul>
<li><strong>Eat a little less</strong> — mainly by cutting the "easy" calories: sugary drinks, alcohol, snacking, oils.</li>
<li><strong>Move a little more day to day</strong> — background activity (walking, steps) often matters more than the workout.</li>
<li><strong>Keep training</strong> — not to "burn," but to protect your muscle (more on that below).</li>
</ul>

<h2>Why an aggressive calorie deficit backfires</h2>
<p>Cutting your calories in half makes you lose weight fast — then breaks the machine. Too low for too long, and you get <strong>muscle loss</strong> (your body taps into muscle when energy runs short), hunger that's hard to manage, a drop in energy and spontaneous activity, and motivation that collapses. Lack of sleep makes everything worse: at the same deficit, poor sleep <a href="/articles/combien-heures-sommeil-par-nuit.html">melts lean mass much faster</a>. In a 2010 trial on an identical diet, two weeks at 5.5 hours in bed instead of 8.5 increased lean mass loss by 60%. A moderate deficit held for three months always beats a brutal deficit held for three weeks.</p>

<h2>How to keep muscle in a calorie deficit: the non-negotiable trio</h2>
<ul>
<li><strong>High protein</strong> — <a href="/articles/proteines-par-jour-prise-de-muscle.html">2.2 to 2.6 g per kilo per day when cutting</a> (about 1 to 1.2 g per pound), or 2.3 to 3.1 g per kilo of lean mass according to the 2014 review. It's your best insurance against muscle loss, and it keeps you full.</li>
<li><strong>Strength training</strong> — the signal that tells your body to hold on to its muscle. In a deficit, you keep your loads up; intensity is not the first thing you cut.</li>
<li><strong>A reasonable deficit</strong> — the more aggressive it is, the bigger the share of muscle you lose. In elite athletes (a 2011 trial), losing 0.7% of body weight per week led to a 2.1% gain in lean mass, versus none at a faster pace.</li>
</ul>
<p>A common question: <a href="/articles/cardio-ou-muscu-pour-maigrir.html">cardio or weights for fat loss</a>? Both help, in different roles — the calorie deficit creates the loss, strength training decides <em>what</em> you lose.</p>

<h2>Should you count calories?</h2>
<p>Both approaches work, on one condition: being honest. Counting (an app, a kitchen scale) teaches you a lot in the first few weeks — many people <strong>significantly underestimate what they eat</strong>, especially oils, sauces, alcohol and eyeballed portions. In a <em>New England Journal of Medicine</em> study (1992), people convinced they ate less than 1,200 kcal a day were actually underestimating their intake by 47% on average. If you'd rather steer without counting, rely on simple markers: a protein source at every meal, lots of vegetables, and an eye on the scale. But if your weight stalls while you're "sure" you're in a deficit, the cause is almost always the same — your actual intake is higher than your estimated intake. Weighing your food for a week or two is often enough to get things moving again.</p>

<h2>Adjust based on real results, not theory</h2>
<p>No calculation is perfect, because your body adapts along the way: it burns a little less when you eat less. The only reliable compass is the trend:</p>
<ul>
<li>Weigh yourself in the morning and track the <strong>average over 1 to 2 weeks</strong>, never a single day's number.</li>
<li>Loss within the 0.5-1%/week range → change nothing.</li>
<li>Loss stalled for two weeks → cut 150-200 kcal or add some walking.</li>
<li>Loss too fast, energy on the floor, workouts falling apart → you're too low, eat more.</li>
</ul>

<h2>Key takeaways</h2>
<ul>
<li>A 300-500 kcal/day deficit below your real expenditure (~0.3 to 0.5 kg per week); target pace: 0.5 to 1% of body weight per week.</li>
<li>Too aggressive = muscle loss, hunger, giving up; lack of sleep speeds up muscle loss.</li>
<li>High protein + strength training preserve muscle; adjust based on your average weight, not the formula.</li>
</ul>
""",
        "faq": [
            {"q": "What calorie deficit do you need to lose 1 kg (2.2 lb) a week?",
             "a": "It would take a deficit of about 1,100 kcal per day, which is aggressive and risky for muscle and energy in most people. Aim instead for a 300 to 500 kcal deficit (0.3 to 0.5 kg per week at first) and a pace of 0.5 to 1% of your body weight per week at most."},
            {"q": "How do you calculate your calorie deficit?",
             "a": "Estimate your total daily energy expenditure, then subtract 300 to 500 kcal. Confirm the result by tracking your average weight over two weeks and adjust: the scale has the final say, not the formula."},
            {"q": "Can you lose fat without losing muscle?",
             "a": "Largely, yes: a moderate deficit, high protein (2.2 to 2.6 g/kg) and strength training let you lose mostly fat. The more aggressive the deficit, the bigger the share of muscle you lose."},
        ],
    },
    {
        "fr": "creatine-bienfaits-comment-la-prendre",
        "slug": "creatine-benefits-how-to-take-it",
        "title": "Creatine: benefits and how to take it",
        "description": "Creatine monohydrate, 3 to 5 g a day, every day: the real benefits, how to take it, why loading is unnecessary, and the myths. The most studied supplement.",
        "body": """
<p>The short answer: <strong>creatine monohydrate, 3 to 5 g a day, every day</strong>, with a big glass of water, at any time of day. No need for an "exotic" form or a loading phase. It's by far <strong>the most studied and the safest</strong> sports supplement for healthy people — more than 500 scientific publications and decades of track record.</p>
<p>There's nothing magical or shady about creatine: it's a molecule your body already makes, and one you get from meat and fish. As a supplement, it fills your muscle stores to the brim, which helps your muscles produce energy during short, intense efforts. The practical result: a little more strength, a few more reps, workout after workout.</p>

<h2>How to take creatine (it's simple)</h2>
<ul>
<li><strong>The form:</strong> monohydrate, period. It's the only one that has truly proven itself; the pricier "new generation" versions add nothing.</li>
<li><strong>The dose:</strong> 3 to 5 g a day. One teaspoon, in water or in whatever you're drinking.</li>
<li><strong>The timing:</strong> it doesn't matter. Before, after, morning, evening — only consistency counts.</li>
<li><strong>Rest days too.</strong> You don't "top up" before a workout; you keep your stores full at all times: it's an everyday baseline, not a pre-workout.</li>
</ul>
<p>The <strong>loading phase</strong> (20 g/day for 5-7 days) is optional: it only saturates your stores a little faster. At 3-5 g a day, you reach the same level in about four weeks, without risking the digestive discomfort of large doses. A landmark study (1996) measured it: 20 g a day for 6 days or 3 g a day for 28 days produced the same rise, of about 20%, in muscle creatine.</p>

<h2>Creatine benefits: what it really does</h2>
<ul>
<li><strong>Strength and power:</strong> the main and best-demonstrated benefit, for explosive efforts and heavy sets. It doesn't lift the bar for you — it helps you do a little more, and that small extra, repeated over time, is what builds results (<a href="/articles/surcharge-progressive-comment-progresser.html">progressive overload does the rest</a>). Across 22 studies pooled in 2003, strength increased by 20% with creatine plus training, versus 12% with placebo.</li>
<li><strong>A slight size gain:</strong> creatine draws a little water <em>into</em> the muscle. Muscles look slightly fuller, and you can gain 1 to 3 kg (about 2 to 7 lb), mostly water, during a loading phase (less, and more gradually, at 3-5 g a day) — not fat.</li>
<li><strong>Cognition and recovery:</strong> interesting leads, but less solid than the strength side. A 2018 review (6 trials, 281 participants) suggests an effect on short-term memory and reasoning, especially in older or stressed people, with conflicting results elsewhere. Worth watching, without overselling.</li>
</ul>

<h2>Creatine myths to drop</h2>
<ul>
<li><strong>"It's a steroid."</strong> No, nothing of the sort: it's neither a hormone nor a doping product. It's an amino acid derivative already present in your diet.</li>
<li><strong>"It makes you fat."</strong> The initial weight gain is water inside the muscle, not fat.</li>
<li><strong>"You need to cycle it."</strong> There's no need to cycle it or take regular breaks: according to the International Society of Sports Nutrition, intakes of up to 30 g a day for 5 years have been shown to be safe in healthy people.</li>
</ul>

<h2>Creatine vs protein: two different things</h2>
<p>Creatine isn't a protein, and it doesn't replace your diet. It helps you train better; <a href="/articles/proteines-par-jour-prise-de-muscle.html">protein</a>, for its part, provides the building materials. Muscle is built with training that progresses, enough protein and enough sleep — creatine is a solid boost on top, not a shortcut that lets you skip the rest.</p>

<h2>Is creatine safe? One caveat</h2>
<p>In healthy people, creatine is very well tolerated. However, if you have known <strong>kidney disease</strong> (or any doubt about it), this is a decision to make with a doctor, not alone in the supplement aisle. Same during pregnancy: ask for medical advice.</p>

<h2>Key takeaways</h2>
<ul>
<li>Monohydrate, 3 to 5 g a day, every day, whenever suits you — loading is optional.</li>
<li>The main proven benefit: strength and power; the initial weight gain is water, not fat.</li>
<li>The safest supplement for healthy people; get medical advice if you have kidney problems.</li>
</ul>
""",
        "faq": [
            {"q": "Do you need a creatine loading phase?",
             "a": "No, it's optional. A loading phase (20 g/day for 5-7 days) saturates your stores a little faster, but 3 to 5 g a day reaches the same level in about four weeks, without digestive discomfort."},
            {"q": "Does creatine make you gain weight?",
             "a": "It can add 1 to 3 kg at first, especially with a loading phase, but that's essentially water stored in the muscle, not fat. Your muscles look a little fuller; there is no fat gain linked to creatine."},
            {"q": "When should you take creatine?",
             "a": "At any time: before or after training, morning or evening, and on rest days too. It's an everyday baseline where only daily consistency counts, not timing."},
        ],
    },
    {
        "fr": "que-manger-avant-le-sport",
        "slug": "what-to-eat-before-a-workout",
        "title": "What to eat before a workout to perform your best",
        "description": "What to eat before a workout? Carbs, mainly. A real meal 2-3 hours before or a light snack 30-60 minutes before, with concrete examples and hydration tips.",
        "body": """
<p>The short answer: <strong>carbs, mainly</strong>. They're what fuels exercise. Two formats work, depending on how much time you have — a <strong>real meal 2 to 3 hours before</strong>, or a <strong>light, carb-rich snack 30 to 60 minutes before</strong>. Either way, keep fat and fiber low right before: they slow digestion and sit heavy in your stomach while you exercise.</p>
<p>No need to overcomplicate it. The goal is to show up <em>full of energy with a settled stomach</em> — neither starving nor still digesting a heavy meal.</p>

<h2>Why carbs before a workout?</h2>
<p>Carbs are stored in your muscles and liver as glycogen: it's the preferred fuel as soon as intensity rises, and the brain's main energy source. Before a session, they fill the tank and steady your blood sugar, which translates into more drive and better focus. Protein and fat are useful in your overall diet, but right before exercise they digest slowly and don't provide immediate energy.</p>

<h2>How long before a workout should you eat?</h2>
<ul>
<li><strong>2 to 3 hours before:</strong> a real balanced meal, mostly carbs, with a little protein and little fat. Maximum comfort — everything is digested by the time you get going.</li>
<li><strong>30 to 60 minutes before:</strong> a light snack, almost entirely easy-to-digest carbs. The closer you are to the session, the smaller, simpler, and lower in fat and fiber it should be.</li>
</ul>

<h2>Pre-workout meal and snack ideas</h2>
<ul>
<li><strong>Meal 2-3 hours before:</strong> rice or pasta + chicken + cooked vegetables; or whole-grain bread + eggs + fruit; or a bowl of oatmeal with milk and a banana.</li>
<li><strong>Snack 30-60 minutes before:</strong> a banana, a fruit compote or applesauce, a few dates, a slice of bread with honey, or a piece of fruit.</li>
<li><strong>Avoid right before:</strong> fried food, very fatty dishes, a big bowl of raw vegetables or legumes — too slow to digest, bloating guaranteed.</li>
</ul>

<h2>Is it OK to work out on an empty stomach?</h2>
<p>It depends on what you're doing. For easy <a href="/articles/zone-2-cardio-cest-quoi.html">zone 2 cardio</a> in the morning, training fasted is perfectly viable — plenty of people do very well with it. A 2018 meta-analysis (46 studies) backs this up: eating beforehand improves prolonged endurance efforts, but not shorter ones. For <strong>strength or high-intensity work</strong>, the data are thinner; if you feel flat on an empty stomach, a small carb snack 30 minutes before often makes a real difference. And if you're <strong>chasing performance</strong> in a long effort, don't go in fasted.</p>

<h2>Match your pre-workout meal to your session</h2>
<p>Not every effort has the same needs. For a <strong>short, easy session</strong>, you need almost nothing in particular. For a <strong>strength or high-intensity session</strong>, having carbs available can help on the last sets. And for a <strong>long effort</strong> — more than an hour — that's where filling up on carbs matters most: for intense exercise lasting more than 90 minutes, the International Society of Sports Nutrition recommends 1 to 4 g of carbs per kilo (about 0.5 to 1.8 g per pound) in the hours beforehand, then 30 to 60 g per hour during exercise. Simple rule: the longer or harder the session, the more the carbs beforehand count.</p>

<h2>Should you drink coffee before a workout?</h2>
<p>Caffeine is one of the few "boosters" whose effect on performance is solidly established: a bit more strength and endurance, sharper alertness. According to the International Society of Sports Nutrition (2021), the effect is consistent between 3 and 6 mg per kilo, most often taken 60 minutes before, and may start as low as 2 mg per kilo: for 70 kg (154 lb), that's about 140 to 210 mg, or roughly two cups of coffee. Two safeguards: keep the dose reasonable — the European Food Safety Authority (EFSA) considers up to 200 mg in a single dose safe, even before intense exercise, and 400 mg over the day — and above all <a href="/articles/cafe-et-sommeil-combien-de-temps-avant.html">avoid caffeine late in the day</a>: an evening workout fueled by coffee can cost you your night, and recovery happens precisely during sleep.</p>

<h2>Don't forget to hydrate</h2>
<p>Showing up dehydrated hurts performance as much as an empty tank: the American College of Sports Medicine advises starting exercise well hydrated, drinking from a few hours beforehand. Drink normally in the hours leading up, have a glass or two before you start, and <a href="/articles/combien-d-eau-boire-par-jour.html">adjust for heat and sweat</a>. And think about afterward right away: <a href="/articles/que-manger-apres-le-sport.html">what you eat after your workout</a> matters just as much for your recovery.</p>

<h2>Key takeaways</h2>
<ul>
<li>Before exercise, carbs come first: a real meal 2-3 hours before, or a light snack 30-60 minutes before.</li>
<li>Less fat and fiber as the session gets closer; the closer it is, the smaller and simpler.</li>
<li>Fasted: fine for easy cardio; for a long effort or when chasing performance, eat beforehand. And drink before you start.</li>
</ul>
""",
        "faq": [
            {"q": "What should you eat before lifting weights?",
             "a": "A carb-rich meal with a little protein 2 to 3 hours before (rice + chicken + vegetables, for example), or a light carb snack 30 to 60 minutes before (a banana, bread with honey). Avoid fat and fiber right before the session."},
            {"q": "Can you work out on an empty stomach?",
             "a": "Yes for easy or short cardio, where it's no problem. For a long effort or when chasing performance, eating beforehand improves results. For strength training or high-intensity work, the data are less clear: if you feel flat, a small carb snack 30 minutes before is often enough."},
            {"q": "How long before a workout should you eat?",
             "a": "Have a full meal 2 to 3 hours before so it has time to digest; a light, carb-rich snack 30 to 60 minutes before. The closer you eat to the session, the smaller and lower in fat the portion should be."},
        ],
    },
    {
        "fr": "que-manger-apres-le-sport",
        "slug": "what-to-eat-after-a-workout",
        "title": "What to eat after a workout for better recovery",
        "description": "What to eat after a workout: 20 to 40 g of protein plus carbs. Why the 30-minute anabolic window is a myth, with concrete post-workout meal examples.",
        "body": """
<p>The short answer: <strong>protein (20 to 40 g) and carbs</strong>. Protein provides the building blocks to repair muscle; carbs refill the glycogen your workout drew down. A normal meal containing both, within <strong>two to three hours</strong> of your session, covers the essentials — no need to lunge for a shaker the second you rack the bar.</p>
<p>This is the part that surprises people most: the famous 30-minute <strong>"anabolic window" is a myth</strong>, at least in its strict, stressful version.</p>

<h2>Protein + carbs: the post-workout duo</h2>
<p>After exercise, two things are happening. On one side, <strong>muscle protein synthesis</strong> is stimulated: 20 to 40 g of high-quality protein (0.25 to 0.4 g per kilo of body weight), the dose the International Society of Sports Nutrition (ISSN) settles on, provides enough amino acids to get the most out of it. On the other, your <strong>glycogen</strong> stores are rebuilding: carbs speed up the refill, especially after a big session or long cardio. Together, they make a complete recovery meal.</p>

<h2>The 30-minute anabolic window is a myth</h2>
<p>For a long time, people believed you had to eat within half an hour or "lose" your workout. The data have corrected that: the window actually lasts <strong>several hours</strong>. A 2013 meta-analysis (about twenty trials, more than 500 participants) goes further: once total protein intake is accounted for, timing around the session makes no difference to muscle or strength gains. In short, <a href="/articles/proteines-par-jour-prise-de-muscle.html">your total intake across the day is what builds muscle</a>, far more than the exact minute of your post-workout meal. In other words: relax. A real meal within two to three hours is more than enough for most goals.</p>

<h2>When post-workout timing really matters</h2>
<ul>
<li><strong>You're doing two sessions</strong> a few hours apart: then refilling carbs quickly really pays off — the ISSN recommends rapid refueling when fewer than 4 hours separate the two efforts.</li>
<li><strong>You trained fasted</strong> or several hours after your last meal: eating fairly soon afterward becomes more useful. If you went more than 3 to 4 hours without food before the session, a 2013 review advises at least 25 g of protein as soon as possible.</li>
<li><strong>High-volume endurance sports:</strong> rebuilding glycogen quickly helps you handle the training load of the following days.</li>
</ul>
<p>Outside these situations, the rush is a non-issue.</p>

<h2>What if you're in a calorie deficit to lose fat?</h2>
<p>Even when cutting, the principle doesn't change: protein to protect muscle, some carbs to refuel. The only difference is that these calories have to <strong>fit within your daily total</strong> — you don't add them on top. The post-workout meal is actually the best place to put a good share of your carbs when you don't have many: it's when your body uses them best.</p>

<h2>Post-workout meal ideas</h2>
<ul>
<li>Greek yogurt or skyr + fruit + oats.</li>
<li>Chicken or fish + rice + vegetables.</li>
<li>Eggs + whole-grain bread + a piece of fruit.</li>
<li>In a rush or not hungry right after: a protein shake + a banana, as a fallback — not a requirement.</li>
</ul>

<h2>Food isn't everything</h2>
<p>The post-workout meal is only one piece of recovery. The rest comes down to your <a href="/articles/proteines-par-jour-prise-de-muscle.html">protein intake spread across the day</a> (about 0.4 g per kilo at a minimum of four meals, according to a 2018 review), your sleep, and how you manage your training load. And no, no meal "cures" <a href="/articles/courbatures-que-faire.html">sore muscles</a>: they run their course whatever you eat. Set up your next session, too, by paying attention to <a href="/articles/que-manger-avant-le-sport.html">what you eat beforehand</a>.</p>

<h2>Don't forget to rehydrate</h2>
<p>Rehydration is part of recovery, especially after a heavy sweat. Drink to thirst in the hours that follow, a bit more if it was hot — <a href="/articles/combien-d-eau-boire-par-jour.html">how much you actually need is covered here</a>. No need to gulp down liters at once: refill gradually.</p>

<h2>Key takeaways</h2>
<ul>
<li>After exercise: 20 to 40 g of protein + carbs, in a normal meal within 2-3 hours.</li>
<li>The strict 30-minute anabolic window is a myth; your daily total is what counts.</li>
<li>Tight timing only really matters if you do back-to-back sessions or train fasted.</li>
</ul>
""",
        "faq": [
            {"q": "Do you need to eat right after a workout?",
             "a": "Not urgently: the 30-minute anabolic window is a myth. A meal with protein and carbs within two to three hours is enough. Tight timing only matters if you do two sessions back to back or trained fasted."},
            {"q": "What should you eat after strength training to recover?",
             "a": "20 to 40 g of protein (0.25 to 0.4 g per kilo) and carbs: Greek yogurt + fruit + oats, chicken + rice + vegetables, or eggs + bread. Protein repairs muscle; carbs refill glycogen."},
            {"q": "Should you drink a protein shake after training?",
             "a": "It's not mandatory. A shake is handy if you're in a rush or not hungry, but a real meal works just as well. Your total protein for the day is what counts, not the drink right after the session."},
        ],
    },
    {
        "fr": "combien-d-eau-boire-par-jour",
        "slug": "how-much-water-should-you-drink-a-day",
        "title": "How much water should you drink a day?",
        "description": "How much water should you drink a day? EFSA says 2 L in total for women and 2.5 L for men, food included. The 8-glasses myth, thirst, and exercise.",
        "body": """
<p>The short answer: about <strong>30 to 35 ml per kilo of body weight</strong> (roughly half an ounce per pound), or about <strong>1.5 to 2.5 L per day</strong> (about 50 to 85 oz) for most adults — <em>plus</em> whatever you lose through exercise and heat. For 70 kg (154 lb), that's roughly 2 to 2.5 L, drinks included.</p>
<p>But the exact number matters less than you might think, because your body has a very fine-tuned regulation system: thirst. The "8 glasses a day" ritual is a handy benchmark, not a law of physiology — and it doesn't account for your weight, your climate or your activity.</p>

<h2>Where the daily water number comes from</h2>
<p>The 30-35 ml/kg rule is a reasonable estimate of an adult's total water needs. It lines up with the reference values of the European Food Safety Authority (EFSA):</p>
<div class="tablewrap"><table>
<caption>Source: EFSA (2010), adequate intakes of total water (drinks and food), temperate climate, moderate activity.</caption>
<thead><tr><th>Profile</th><th class="n">Total water per day</th></tr></thead>
<tbody>
<tr><td>Adult woman</td><td class="n">2.0 L</td></tr>
<tr><td>Adult man</td><td class="n">2.5 L</td></tr>
<tr><td>Pregnant woman</td><td class="n">2.3 L</td></tr>
<tr><td>Breastfeeding woman</td><td class="n">2.7 L</td></tr>
<tr><td>Teens from age 14, older adults</td><td class="n">same as adults</td></tr>
</tbody>
</table></div>
<p>Two clarifications that change everything:</p>
<ul>
<li>This total includes <strong>all drinks</strong>, not just plain water: tea, coffee, herbal tea and soup all count. Caffeine at usual doses doesn't have the "dehydrating" effect it's often credited with: in a 2014 trial of 50 regular coffee drinkers, four cups a day hydrated just as well as water.</li>
<li>It also includes <strong>the water in your food</strong> — fruit, vegetables, yogurt and saucy dishes provide a good share of it. That's why you don't need to drink your entire requirement from the tap.</li>
</ul>

<h2>Do you really need 8 glasses of water a day?</h2>
<p>"Eight glasses of water a day" is an easy formula to remember, but when physiologist Heinz Valtin went looking for its origin in 2002, he found no scientific study to make it a universal target for healthy adults. Your needs go up with heat, altitude, exercise, breastfeeding or a very active day — and go down when you're sedentary somewhere cool. Trying to force down a fixed number of liters no matter what makes no sense: it pushes you either to force yourself or to feel guilty for nothing.</p>

<h2>How to tell if you're drinking enough</h2>
<p>Forget the count and listen to your two best indicators:</p>
<ul>
<li><strong>Thirst.</strong> In healthy adults, it's a reliable guide: drink when you're thirsty, and that's usually enough. Two caveats — older people sense thirst less well, and during intense exercise it's better to drink ahead of time rather than wait for a dry throat.</li>
<li><strong>Urine color.</strong> The simplest indicator there is, reliable in the field according to a 1994 study: <strong>pale yellow</strong>, all good; dark and scant, drink more; almost clear all the time, you're probably drinking more than you need.</li>
</ul>

<h2>Exercise and heat: how much extra water you need</h2>
<p>This is where your needs really go up. An hour of sweating can easily mean <strong>0.5 to 1 L of losses</strong> (about 17 to 34 oz), sometimes more in intense heat: among 1,303 athletes, average sweat rates ranged from 0.8 to 1.5 L per hour depending on the sport. Drink before you start, regularly during long efforts, and refill afterward — <a href="/articles/que-manger-avant-le-sport.html">hydration is part of preparing for a session</a>. For very long efforts or in full heat, water alone is no longer enough: salt losses count too.</p>

<h2>Do you need electrolytes?</h2>
<p>On a normal day, no: water and a balanced diet are enough, and the salt in your meals does the rest. <strong>Electrolytes</strong> (mostly sodium) become useful in one specific case — <strong>long, intense or hot-weather</strong> efforts, where you lose a lot of salt through sweat. Then a sports drink or a simple pinch of salt makes sense. Outside of that, everyday electrolyte powders are mostly marketing. Keep in mind, too, that even moderate dehydration measurably degrades performance and focus — the American College of Sports Medicine advises not losing more than 2% of your body weight during exercise. Don't start a hard session already short on water.</p>

<h2>Can you drink too much water?</h2>
<p>Yes, but it's rare. Forcing down very large volumes of plain water in a short time — typically during endurance events — can dilute the sodium in your blood too much (<em>hyponatremia</em>), which is dangerous: your kidneys can't eliminate more than 0.7 to 1 L per hour, according to EFSA. The practical lesson: don't force yourself to gulp down liters "on principle." On the flip side, even mild dehydration costs you energy and focus: if you're <a href="/articles/toujours-fatigue-causes.html">often tired for no clear reason</a>, not drinking enough is one of the simple causes to rule out first.</p>

<h2>Key takeaways</h2>
<ul>
<li>About 30-35 ml/kg, or ~1.5-2.5 L per day, counting drinks and the water in food.</li>
<li>The "8 glasses" is a benchmark, not a rule: trust your thirst and aim for pale yellow urine.</li>
<li>Add 0.5-1 L per hour of sweating; don't force yourself to drink beyond that — too much water is a real thing.</li>
</ul>
""",
        "faq": [
            {"q": "Do you really need to drink 8 glasses of water a day?",
             "a": "No, it's a handy benchmark, not a rule. Your needs are around 30-35 ml per kilo (~1.5-2.5 L), vary with heat and activity, and include all drinks plus the water in food."},
            {"q": "How do I know if I'm drinking enough water?",
             "a": "Two indicators: thirst, which is reliable in healthy adults, and urine color. Pale yellow means you're well hydrated; dark and scant means you need to drink more."},
            {"q": "How much water should you drink when you exercise?",
             "a": "Add about 0.5 to 1 L per hour of sweating to your baseline needs, more in intense heat. Drink before, during long efforts and after. For very long efforts, also think about salt losses."},
        ],
    },
]
