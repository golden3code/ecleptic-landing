# -*- coding: utf-8 -*-
"""English version of /methode/besoin-de-sommeil.html → /en/methode/sleep-need.html.

Translation of tools/methode/besoin_de_sommeil.py: same facts and links (NSF need at the
middle of the range: 9 h / 8 h / 7 h 30 min; 70/30 blend of whole cycles / raw need only
when cycle length is known; sleep pillar 21 points: duration 40, stages 25 if measured,
efficiency 20, regularity 15; weights redistributed; biological-age modifier described
without any figure). related / journal / kind / num / order / date are taken from the
French page.
"""

PAGE = {
    "fr": "besoin-de-sommeil",
    "slug": "sleep-need",
    "label": "Your sleep need",
    "title": "Your sleep need, from your age to your cycles",
    "seo_title": "Sleep need by age and sleep cycle: how it's calculated",
    "description": "Your sleep need starts from age-based guidelines and adjusts to your cycles. How Ecleptic calculates it and scores your night: duration, stages, efficiency.",
    "lead": "\"Eight hours for everyone\" is a starting point, not a truth. Here's how the app starts from the recommendations for your age, adjusts them to the length of your own cycles, then scores each night on four criteria.",
    "body": """
<h2>A need, not an average</h2>
<p>Your sleep need is <strong>the amount of sleep that lets you function at your best, day after day, without building up debt</strong>. It changes with age and varies from one person to another. In the app, it's the reference your nights' duration is judged against.</p>
<p>Sleeping below that need several nights in a row creates a debt: your attention drops, your mood frays, your recovery slows down. And sleeping in isn't always enough to <a href="/articles/dette-de-sommeil-rattraper.html">catch up on sleep debt</a>.</p>

<h2>What your nights repair</h2>
<p>Sleep isn't downtime. It's organized into cycles of about 90 minutes on average, each moving through three main types of sleep:</p>
<ul>
<li><strong>Light sleep:</strong> the transition between wakefulness and deeper sleep, which takes up a good part of the night.</li>
<li><strong>Deep sleep:</strong> the most restorative for the body, concentrated early in the night. There are concrete ways to <a href="/articles/sommeil-profond-comment-augmenter.html">get more deep sleep</a>.</li>
<li><strong>REM sleep:</strong> the dreaming stage, which plays a role in memory and emotional balance, and is more abundant toward the end of the night.</li>
</ul>
<p>Cutting your night short therefore mostly eats into the last cycles, the ones richest in REM sleep.</p>

<h2>The starting point: your age</h2>
<p>The app starts from the National Sleep Foundation's recommendations, which set a duration range for each age group, and uses <strong>the middle of each range</strong>:</p>
<div class="figs">
  <div><span class="v">9 h</span><span class="u">Ages 14 to 17 (8 to 10 h)</span></div>
  <div><span class="v">8 h</span><span class="u">Ages 18 to 64 (7 to 9 h)</span></div>
  <div><span class="v">7 h 30 min</span><span class="u">Ages 65 and up (7 to 8 h)</span></div>
  <div><span class="v">90</span><span class="u">Minutes per cycle, on average</span></div>
</div>
<p>These ranges are wide for a good reason: at the same age, some people really need 7 hours, others 9. The middle is just an honest starting point until the app knows more about you.</p>

<h2>Then the length of your cycles</h2>
<p>A cycle lasts about 90 minutes on average, but that length varies from person to person. And waking up in the middle of deep sleep leaves you groggier than waking up at the end of a cycle.</p>
<p>When the length of your own cycles is known, the app takes it into account: your sleep duration is judged <strong>70% against the number of whole cycles closest to your need</strong>, and 30% against the raw need. Example: with 100-minute cycles and a starting need of 8 hours, the closest target falls at 5 cycles, or 8 hours 20 minutes.</p>
<p>The remaining 30% keeps an anchor in the benchmarks for your age. As long as your cycles aren't known, the raw need serves as the reference.</p>

<h2>How the app scores your night</h2>
<p>Your need feeds the sleep pillar of the <a href="/methode/readiness-score.html">Readiness Score</a>, which weighs <strong>21 points out of 100</strong> and is made up of four criteria:</p>
<ul>
<li><strong>Duration against your need (40%):</strong> the heaviest criterion, calculated as described above.</li>
<li><strong>Deep and REM stages (25%):</strong> only when your watch measured them. For a night you log by hand, the app never makes up stages.</li>
<li><strong>Efficiency (20%):</strong> the share of your time in bed actually spent asleep.</li>
<li><strong>Regularity (15%):</strong> how consistent your bedtimes and wake-up times are.</li>
</ul>
<p>A criterion with no data is removed, and its weight is redistributed among the others. Your night also counts elsewhere in the score: while you sleep, your watch records your <a href="/methode/vitaux.html">vitals</a>, judged against <a href="/methode/ligne-de-base.html">your baseline</a>.</p>

<h2>Regularity, the underrated factor</h2>
<p>Everyone talks about duration. Yet <strong>regularity sometimes matters more</strong>: a study published in 2024 found that sleep regularity predicted mortality risk better than sleep duration. <a href="/articles/se-coucher-meme-heure-regularite.html">Going to bed and getting up at set times</a>, weekends included, remains one of the simplest levers.</p>
<p>Sleep also weighs on your <a href="/methode/age-biologique.html">biological age</a>. Nights of sufficient length, without excess, at regular times, work in your favor; sleep that's too short, too long or irregular can age you, by more than good sleep can make you younger.</p>

<h2>The limits of the measurement</h2>
<p>In a lab, sleep is measured by polysomnography: brain activity, eye movements, muscle tone. A watch, by contrast, estimates it from your movements and your heart rate. It's fairly reliable for duration and timing, much less so for the fine breakdown of stages.</p>
<p>Your need, for its part, remains an estimate, not a prescription. If you feel fully rested on a little less, or always tired on a little more, that information counts as much as the number.</p>

<h2>When to talk to a doctor</h2>
<p>The app is a wellness tool, not a medical device: it doesn't diagnose any sleep disorder. If you get enough sleep but stay exhausted, if the people around you notice loud snoring or pauses in your breathing, or if your trouble sleeping has lasted several weeks, talk to a doctor. And if you wake up with chest pain, palpitations or unusual shortness of breath, call your local emergency number (911 in the US, 999 or 112 in the UK and Europe).</p>
""",
    "refs": [
        "Hirshkowitz M. et al. (2015), the National Sleep Foundation's sleep duration recommendations, <em>Sleep Health</em>." ' <a href="https://doi.org/10.1016/j.sleh.2014.12.010" rel="noopener" target="_blank">doi:10.1016/j.sleh.2014.12.010</a>',
        "Windred D. P. et al. (2024), sleep regularity is a stronger predictor of mortality than sleep duration, <em>Sleep</em>." ' <a href="https://doi.org/10.1093/sleep/zsad253" rel="noopener" target="_blank">doi:10.1093/sleep/zsad253</a>',
    ],
    "faq": [
        {"q": "How many hours of sleep do you need by age?",
         "a": "The National Sleep Foundation recommends 8 to 10 hours between ages 14 and 17, 7 to 9 hours between 18 and 64, and 7 to 8 hours from age 65. Ecleptic starts from the middle of your range, meaning 9 hours, 8 hours or 7 hours 30 minutes, then adjusts it to your cycles once their length is known."},
        {"q": "How long is a sleep cycle?",
         "a": "About 90 minutes on average, but the length varies from person to person. Waking up at the end of a cycle rather than in the middle of deep sleep makes waking up easier. That's why Ecleptic judges your sleep duration 70% against the number of whole cycles closest to your need, as soon as your cycles are known."},
        {"q": "Is it better to sleep longer or at regular times?",
         "a": "Both matter, but regularity is often underrated: a study published in 2024 found that it predicted mortality risk better than duration. In Ecleptic's Readiness Score, duration against your need accounts for 40% of the sleep pillar, and the regularity of your bedtimes and wake-up times for 15%."},
    ],
}
