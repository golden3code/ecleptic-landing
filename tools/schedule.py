# -*- coding: utf-8 -*-
"""Planning de publication progressive des articles (« drip »).

Chaque article listé ci-dessous devient PUBLIC à la date calculée. Tant que
la date est dans le futur, l'article n'existe pas sur le site (ni page, ni
index, ni sitemap) et les liens internes vers lui sont neutralisés — donc
jamais de lien mort. Le cron GitHub Actions (.github/workflows/publish.yml)
rebuild chaque jour : l'article apparaît tout seul le jour venu.

Pour régler la cadence : change START (première publication) et INTERVAL_DAYS
(nombre de jours entre deux publications), puis :
    python3 tools/build_articles.py   # vérifier
    git add -A && git commit && git push
L'ordre de ORDER est volontairement entrelacé entre les thèmes pour que le
Journal grandisse de façon variée. Un article retiré de ORDER repasse à
publication immédiate (sa propre clé "date"). Ajouter un nouveau slug en fin
de ORDER lui donne automatiquement la prochaine date libre.
"""
from datetime import date, timedelta

# --- Réglages de cadence ---------------------------------------------------
START = date(2026, 9, 22)   # date de la 1re publication programmée
INTERVAL_DAYS = 2           # un article tous les 2 jours (~3-4 / semaine)

# --- Ordre de publication (entrelacé par thème) ----------------------------
ORDER = [
    "cafe-et-sommeil-combien-de-temps-avant",
    "zone-2-cardio-cest-quoi",
    "combien-de-calories-par-jour",
    "frequence-cardiaque-repos-normale",
    "bain-froid-recuperation-bienfaits",
    "decalage-horaire-que-faire",
    "semaine-de-decharge-deload",
    "sport-contre-anxiete-stress",
    "coup-de-barre-apres-manger",
    "reprendre-le-sport-apres-maladie",
    "lumiere-bleue-ecrans-avant-de-dormir",
    "vo2max-comment-l-ameliorer",
    "deficit-calorique-comment-calculer",
    "recuperation-active-ou-passive",
    "etirements-avant-ou-apres-le-sport",
    "travail-de-nuit-comment-mieux-dormir",
    "surcharge-progressive-comment-progresser",
    "coherence-cardiaque-respiration",
    "carence-en-fer-fatigue",
    "cycle-menstruel-et-sport",
    "se-reveiller-la-nuit-3h-du-matin",
    "combien-de-pas-par-jour",
    "creatine-bienfaits-comment-la-prendre",
    "comment-savoir-si-on-est-bien-recupere",
    "sauna-bienfaits-recuperation",
    "routine-du-soir-pour-bien-dormir",
    "temps-de-repos-entre-les-series",
    "cortisol-comment-le-faire-baisser",
    "tabac-nicotine-et-sport",
    "cardio-ou-muscu-pour-maigrir",
    "que-manger-avant-le-sport",
    "recuperation-apres-40-ans",
    "full-body-ou-split-musculation",
    "que-manger-apres-le-sport",
    "combien-de-repetitions-pour-prendre-du-muscle",
    "combien-d-eau-boire-par-jour",
]

SCHEDULE = {
    slug: (START + timedelta(days=INTERVAL_DAYS * i)).isoformat()
    for i, slug in enumerate(ORDER)
}
