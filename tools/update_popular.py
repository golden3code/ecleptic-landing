#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Met à jour le classement « Les plus lus » depuis PostHog.

Interroge l'API PostHog (région EU) : décompte des événements `article_view`
par article sur les 90 derniers jours, puis écrit `tools/popular.json` —
que `build_articles.py` lit pour ordonner /articles/?sort=populaires.

Usage :
    python3 tools/update_popular.py && python3 tools/build_articles.py
    # puis commit + push

Authentification (clé API PERSONNELLE, pas la clé projet phc_) :
  - fichier `.posthog_key` à la racine du repo landing (git-ignoré), OU
  - variable d'environnement POSTHOG_PERSONAL_API_KEY.
Créer la clé : PostHog (eu.posthog.com) → Settings → Personal API keys →
Create key, scope « Query : Read » suffit.
"""
import json
import os
import sys
import urllib.request

HOST = "https://eu.posthog.com"
DAYS = 90
ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
OUT = os.path.join(ROOT, "tools", "popular.json")


def api_key():
    path = os.path.join(ROOT, ".posthog_key")
    if os.path.exists(path):
        return open(path).read().strip()
    key = os.environ.get("POSTHOG_PERSONAL_API_KEY", "").strip()
    if key:
        return key
    sys.exit(
        "Aucune clé API personnelle PostHog.\n"
        "→ Crée-la sur eu.posthog.com (Settings → Personal API keys, scope Query:Read)\n"
        "→ puis colle-la dans le fichier .posthog_key à la racine du repo landing."
    )


def call(key, path, payload=None):
    req = urllib.request.Request(
        HOST + path,
        data=json.dumps(payload).encode() if payload else None,
        headers={"Authorization": "Bearer " + key, "Content-Type": "application/json"},
    )
    with urllib.request.urlopen(req, timeout=30) as r:
        return json.load(r)


def main():
    key = api_key()
    projects = call(key, "/api/projects/")["results"]
    if not projects:
        sys.exit("La clé ne donne accès à aucun projet PostHog.")
    project_id = projects[0]["id"]

    hogql = (
        "SELECT properties.article AS article, count() AS n "
        "FROM events WHERE event = 'article_view' "
        "AND timestamp > now() - INTERVAL %d DAY "
        "AND properties.article IS NOT NULL AND properties.article != 'index' "
        "GROUP BY article ORDER BY n DESC" % DAYS
    )
    res = call(key, "/api/projects/%s/query/" % project_id,
               {"query": {"kind": "HogQLQuery", "query": hogql}})
    rows = res.get("results", [])
    if not rows:
        sys.exit("Aucun événement article_view sur %d jours — popular.json inchangé." % DAYS)

    order = [r[0] for r in rows]
    with open(OUT, "w") as f:
        json.dump(order, f, indent=2, ensure_ascii=False)
        f.write("\n")
    print("popular.json mis à jour (%d articles, fenêtre %d j) :" % (len(order), DAYS))
    for slug, n in rows[:10]:
        print("  %5d  %s" % (n, slug))
    print("→ lance maintenant : python3 tools/build_articles.py, puis commit + push.")


if __name__ == "__main__":
    main()
