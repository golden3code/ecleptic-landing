#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""IndexNow : prévient Bing (et Yandex, Seznam, Naver…) qu'une page est nouvelle ou modifiée.

Bing alimente la recherche web de ChatGPT, Copilot et DuckDuckGo : sans lui, ces
moteurs ne voient pas le site. Pas de compte : la clé est vérifiée par le fichier
<KEY>.txt à la racine du site (NE PAS SUPPRIMER).

    python3 tools/indexnow.py --all                     # tout le sitemap
    python3 tools/indexnow.py --diff ancien.xml sitemap.xml   # nouvelles URL + lastmod changés
    python3 tools/indexnow.py URL [URL…]
"""
import json, os, re, sys, urllib.request

HOST = "ecleptic.health"
ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


def key():
    for fn in os.listdir(ROOT):
        if re.fullmatch(r"[0-9a-f]{32}\.txt", fn):
            return fn[:-4]
    raise SystemExit("clé IndexNow introuvable (<32 hex>.txt à la racine)")


def entries(path):
    s = open(path, encoding="utf-8").read() if os.path.exists(path) else ""
    out = {}
    for block in re.findall(r"<url>(.*?)</url>", s, re.S):
        loc = re.search(r"<loc>(.*?)</loc>", block).group(1)
        lm = re.search(r"<lastmod>(.*?)</lastmod>", block)
        out[loc] = lm.group(1) if lm else ""
    return out


def submit(urls):
    urls = sorted(set(urls))
    if not urls:
        print("IndexNow : rien à signaler")
        return
    k = key()
    for i in range(0, len(urls), 10000):
        body = json.dumps({"host": HOST, "key": k, "keyLocation": "https://%s/%s.txt" % (HOST, k),
                           "urlList": urls[i:i + 10000]}).encode()
        req = urllib.request.Request("https://api.indexnow.org/indexnow", data=body,
                                     headers={"Content-Type": "application/json; charset=utf-8"})
        try:
            with urllib.request.urlopen(req, timeout=30) as r:
                print("IndexNow : %d URL envoyées → HTTP %d" % (len(urls[i:i + 10000]), r.status))
        except urllib.error.HTTPError as e:
            # 200/202 = reçu ; 403 = clé non trouvée ; 422 = URL hors domaine ; 429 = trop de requêtes
            print("IndexNow : HTTP %d %s" % (e.code, e.read()[:200]))


if __name__ == "__main__":
    a = sys.argv[1:]
    if a[:1] == ["--all"]:
        submit(entries(os.path.join(ROOT, "sitemap.xml")).keys())
    elif a[:1] == ["--diff"] and len(a) == 3:
        old, new = entries(a[1]), entries(a[2])
        submit([u for u, lm in new.items() if old.get(u) != lm])
    elif a:
        submit(a)
    else:
        print(__doc__)
