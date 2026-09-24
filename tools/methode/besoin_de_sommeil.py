# -*- coding: utf-8 -*-
"""La méthode · Fiche 8 — Ton besoin de sommeil (repères par âge, cycles, pilier sommeil).

Chargé par tools/build_articles.py (_load_methode) → /methode/besoin-de-sommeil.html.
Faits vérifiés dans le code de l'app (lib/readiness/sleep.ts, sync.ts,
lib/bioAge/model.ts) le 24/09/2026 : besoin NSF au milieu de la fourchette
(9 h / 8 h / 7 h 30), mélange 70/30 cycles entiers / besoin brut seulement si
la longueur de cycle est connue (pas le 90 min par défaut), pilier sommeil 21
pts (durée 40, phases 25 si mesurées, efficacité 20, régularité 15),
redistribution des poids, modificateur âge biologique durée + régularité
(asymétrique : la pénalité dépasse le bonus ; chiffres non publiés).
"""

PAGE = {
    "slug": "besoin-de-sommeil",
    "kind": "fiche",
    "num": None,
    "order": 8,
    "label": "Ton besoin de sommeil",
    "title": "Ton besoin de sommeil, de ton âge à tes cycles",
    "seo_title": "Besoin de sommeil : le calcul selon ton âge et tes cycles — Ecleptic",
    "description": "Ton besoin de sommeil part des repères de ton âge et s'ajuste à tes cycles. Comment Ecleptic le calcule et note ta nuit : durée, phases, efficacité, régularité.",
    "date": "2026-09-24",
    "lead": "« Huit heures pour tout le monde » est un point de départ, pas une vérité. Voici comment l'app part des recommandations pour ton âge, les ajuste à la longueur de tes propres cycles, puis note chaque nuit sur quatre critères.",
    "body": """
<h2>Un besoin, pas une moyenne</h2>
<p>Ton besoin de sommeil, c'est <strong>la durée qui te permet de fonctionner au mieux, jour après jour, sans accumuler de dette</strong>. Il change avec l'âge et varie d'une personne à l'autre. Dans l'app, c'est la référence contre laquelle la durée de tes nuits est jugée.</p>
<p>Dormir sous ce besoin plusieurs nuits de suite crée une dette : l'attention baisse, l'humeur se tend, la récupération ralentit. Et une grasse matinée ne suffit pas toujours à <a href="/articles/dette-de-sommeil-rattraper.html">rattraper une dette de sommeil</a>.</p>

<h2>Ce que tes nuits réparent</h2>
<p>Le sommeil n'est pas un temps mort. Il s'organise en cycles d'environ 90 minutes en moyenne, qui enchaînent trois grands types de sommeil :</p>
<ul>
<li><strong>Le sommeil léger :</strong> la transition entre l'éveil et le sommeil plus profond, qui occupe une bonne partie de la nuit.</li>
<li><strong>Le sommeil profond :</strong> le plus réparateur pour le corps, concentré en début de nuit. Il existe des leviers concrets pour <a href="/articles/sommeil-profond-comment-augmenter.html">augmenter ton sommeil profond</a>.</li>
<li><strong>Le sommeil paradoxal :</strong> celui des rêves, qui joue un rôle dans la mémoire et l'équilibre émotionnel, plus abondant en fin de nuit.</li>
</ul>
<p>Écourter ta nuit, c'est donc surtout rogner sur les derniers cycles, les plus riches en sommeil paradoxal.</p>

<h2>Le point de départ : ton âge</h2>
<p>L'app part des recommandations de la National Sleep Foundation, qui fixent une fourchette de durée pour chaque âge, et retient <strong>le milieu de chaque fourchette</strong> :</p>
<div class="figs">
  <div><span class="v">9 h</span><span class="u">De 14 à 17 ans (8 à 10 h)</span></div>
  <div><span class="v">8 h</span><span class="u">De 18 à 64 ans (7 à 9 h)</span></div>
  <div><span class="v">7 h 30</span><span class="u">Dès 65 ans (7 à 8 h)</span></div>
  <div><span class="v">90</span><span class="u">Minutes par cycle, en moyenne</span></div>
</div>
<p>Ces fourchettes sont larges pour une bonne raison : à âge égal, certains ont vraiment besoin de 7 heures, d'autres de 9. Le milieu n'est qu'un point de départ honnête, en attendant d'en savoir plus sur toi.</p>

<h2>Puis la longueur de tes cycles</h2>
<p>Un cycle dure environ 90 minutes en moyenne, mais cette durée varie d'une personne à l'autre. Or un réveil en plein sommeil profond laisse plus groggy qu'un réveil en fin de cycle.</p>
<p>Quand la longueur de tes propres cycles est connue, l'app en tient compte : ta durée de sommeil est jugée <strong>pour 70 % face au nombre de cycles entiers le plus proche de ton besoin</strong>, et pour 30 % face au besoin brut. Exemple : avec des cycles de 100 minutes et un besoin de départ de 8 heures, la cible la plus proche tombe à 5 cycles, soit 8 h 20.</p>
<p>Les 30 % restants gardent un ancrage dans les repères de ton âge. Tant que tes cycles ne sont pas connus, c'est le besoin brut qui sert de référence.</p>

<h2>Comment l'app note ta nuit</h2>
<p>Ton besoin alimente le pilier sommeil du <a href="/methode/readiness-score.html">Readiness Score</a>, qui pèse <strong>21 points sur 100</strong> et se compose de quatre critères :</p>
<ul>
<li><strong>La durée face à ton besoin — 40 % :</strong> le critère le plus lourd, calculé comme on vient de le voir.</li>
<li><strong>Les phases profond et paradoxal — 25 % :</strong> seulement quand ta montre les a mesurées. Pour une nuit saisie à la main, l'app n'invente jamais de phases.</li>
<li><strong>L'efficacité — 20 % :</strong> la part de ton temps au lit passée à dormir vraiment.</li>
<li><strong>La régularité — 15 % :</strong> la stabilité de tes heures de coucher et de lever.</li>
</ul>
<p>Un critère sans donnée est retiré, et son poids redistribué entre les autres. Ta nuit compte aussi ailleurs dans le score : pendant que tu dors, ta montre relève tes <a href="/methode/vitaux.html">vitaux</a>, jugés contre <a href="/methode/ligne-de-base.html">ta ligne de base</a>.</p>

<h2>La régularité, le facteur sous-estimé</h2>
<p>On parle toujours de durée. Pourtant, <strong>la régularité compte parfois plus</strong> : une étude publiée en 2024 a trouvé que la régularité du sommeil prédisait mieux le risque de mortalité que sa durée. <a href="/articles/se-coucher-meme-heure-regularite.html">Se coucher et se lever à heures fixes</a>, week-end compris, reste l'un des leviers les plus simples.</p>
<p>Le sommeil pèse aussi sur ton <a href="/methode/age-biologique.html">âge biologique</a>. Des nuits de durée suffisante, sans excès, à heures régulières, jouent en ta faveur ; un sommeil trop court, trop long ou irrégulier peut te vieillir, davantage qu'un bon sommeil ne peut te rajeunir.</p>

<h2>Les limites de la mesure</h2>
<p>En laboratoire, le sommeil se mesure par polysomnographie : activité cérébrale, mouvements des yeux, tonus musculaire. Une montre, elle, l'estime à partir de tes mouvements et de ton rythme cardiaque. Elle est plutôt fiable pour la durée et les horaires, nettement moins pour le découpage fin des phases.</p>
<p>Ton besoin, lui, reste une estimation, pas une prescription. Si tu te sens pleinement reposé avec un peu moins, ou toujours fatigué avec un peu plus, c'est une information qui compte autant que le chiffre.</p>

<h2>Quand en parler à un médecin</h2>
<p>Ecleptic est un outil de bien-être, pas un dispositif médical : il ne diagnostique aucun trouble du sommeil. Si tu dors suffisamment mais restes épuisé, si ton entourage remarque de forts ronflements ou des pauses dans ta respiration, ou si tes difficultés à dormir durent depuis plusieurs semaines, parles-en à un médecin. Et si tu te réveilles avec une douleur thoracique, des palpitations ou un essoufflement anormal, appelle le 15 ou le 112.</p>
""",
    "refs": [
        "Hirshkowitz M. et al. (2015), recommandations de durée de sommeil de la National Sleep Foundation, <em>Sleep Health</em>.",
        "Windred D. P. et al. (2024), la régularité du sommeil prédit mieux la mortalité que sa durée, <em>Sleep</em>.",
    ],
    "faq": [
        {"q": "Combien d'heures de sommeil faut-il selon l'âge ?",
         "a": "La National Sleep Foundation recommande 8 à 10 heures entre 14 et 17 ans, 7 à 9 heures entre 18 et 64 ans, et 7 à 8 heures à partir de 65 ans. Ecleptic part du milieu de ta fourchette, soit 9 h, 8 h ou 7 h 30, puis l'ajuste à tes cycles quand leur longueur est connue."},
        {"q": "Combien de temps dure un cycle de sommeil ?",
         "a": "Environ 90 minutes en moyenne, mais la durée varie d'une personne à l'autre. Se réveiller en fin de cycle plutôt qu'en plein sommeil profond rend le réveil plus facile. C'est pourquoi Ecleptic juge ta durée de sommeil pour 70 % face au nombre de cycles entiers le plus proche de ton besoin, dès que tes cycles sont connus."},
        {"q": "Vaut-il mieux dormir plus longtemps ou à heures régulières ?",
         "a": "Les deux comptent, mais la régularité est souvent sous-estimée : une étude publiée en 2024 a trouvé qu'elle prédisait mieux le risque de mortalité que la durée. Dans le Readiness Score d'Ecleptic, la durée face à ton besoin pèse 40 % du pilier sommeil, et la régularité de tes heures de coucher et de lever 15 %."},
    ],
    "related": ["readiness-score", "vitaux", "ligne-de-base", "age-biologique"],
    "journal": ["combien-heures-sommeil-par-nuit", "se-coucher-meme-heure-regularite", "sommeil-paradoxal-role", "chronotype-matin-ou-soir"],
}
