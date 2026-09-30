#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Vérifie que chaque source citée existe et correspond à ce qui est écrit.

    python3 tools/check_sources.py                         # tous les articles + pages méthode
    python3 tools/check_sources.py tools/satellites/batch_a.py   # un lot
    python3 tools/check_sources.py tools/methode           # pages méthode seulement

- https://doi.org/<doi>        → Crossref : le DOI existe, le titre et l'année concordent
- https://pubmed.ncbi.nlm.nih.gov/<pmid>/ → PubMed : idem
- autre URL (société savante, agence) → la page répond (200) ; 403/429 = à vérifier à la main
Sortie non nulle s'il reste une source en ÉCHEC. Aucune écriture.
"""
import importlib.util, json, os, re, sys, time, unicodedata, urllib.request, urllib.error

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
UA = "EclepticSourceCheck/1.0 (+https://ecleptic.health/a-propos.html)"
BROWSER_UA = "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/17.0 Safari/605.1.15"
STOP = set("the and for with from that this into over under between among during after before their your what when how "
           "which while than then them they were been being have has had not but are was its our out off per via".split())


def load(path):
    spec = importlib.util.spec_from_file_location("m_" + os.path.basename(path)[:-3], path)
    mod = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(mod)
    return mod


def norm_tokens(s):
    s = unicodedata.normalize("NFKD", re.sub(r"<[^>]+>", " ", s)).encode("ascii", "ignore").decode().lower()
    return {w for w in re.findall(r"[a-z0-9]+", s) if len(w) >= 4 and w not in STOP}


def get(url, ua=UA, tries=3):
    for i in range(tries):
        try:
            req = urllib.request.Request(url, headers={"User-Agent": ua, "Accept": "*/*"})
            with urllib.request.urlopen(req, timeout=25) as r:
                return r.status, r.read()
        except urllib.error.HTTPError as e:
            if e.code in (429, 500, 502, 503, 504) and i < tries - 1:
                time.sleep(2 + 3 * i)
                continue
            return e.code, b""
        except Exception as e:  # réseau, TLS, délai
            if i < tries - 1:
                time.sleep(2)
                continue
            return 0, str(e).encode()
    return 0, b""


def first_surname(cited):
    """« Kodama S. et al. (2009)… » / « Morton RW, et al. … » → « kodama » / « morton »."""
    m = re.match(r"\s*([A-Za-zÀ-ÿ'\- ]+?)[\s,]+(?:[A-Z]{1,3}\b|[A-Z]\.)", cited)
    return unicodedata.normalize("NFKD", m.group(1)).encode("ascii", "ignore").decode().lower().strip() if m else ""


def title_match(real_title, cited, real_year=None):
    rt, ct = norm_tokens(real_title), norm_tokens(cited)
    ratio = len(rt & ct) / max(1, len(rt))
    years = re.findall(r"\b(19[5-9]\d|20[0-3]\d)\b", cited)
    year_ok = (real_year is None or not years or any(abs(int(y) - int(real_year)) <= 1 for y in years))
    return ratio, year_ok


def check(src):
    """→ (statut, détail) ; statut ∈ OK, ÉCHEC, À VÉRIFIER."""
    u, t = src.get("u", ""), src.get("t", "")
    if not u.startswith("https://"):
        return "ÉCHEC", "URL non https"
    m = re.match(r"https://(?:dx\.)?doi\.org/(10\.\S+)$", u)
    if m:
        doi = m.group(1)
        st, body = get("https://api.crossref.org/works/" + urllib.request.quote(doi, safe="/:;()"))
        if st == 404:
            # DOI hors Crossref (Zenodo, jeux de données…) : on interroge DataCite, même contrôle
            st, body = get("https://api.datacite.org/dois/" + urllib.request.quote(doi, safe="/:;()"))
            if st == 404:
                return "ÉCHEC", "DOI inconnu de Crossref et de DataCite"
            if st != 200:
                return "À VÉRIFIER", "DataCite HTTP %s" % st
            att = json.loads(body)["data"]["attributes"]
            real = " ".join(x.get("title", "") for x in att.get("titles") or [])
            year = att.get("publicationYear")
            ratio, year_ok = title_match(real, t, year)
            if year_ok and ratio >= 0.6:
                return "OK", "%s (%s) [DataCite]" % (real[:80], year)
            return "ÉCHEC", "ne concorde pas avec DataCite : « %s » (%s), recouvrement %.0f %%" % (
                real[:110], year, ratio * 100)
        if st != 200:
            return "À VÉRIFIER", "Crossref HTTP %s" % st
        msg = json.loads(body)["message"]
        real = " ".join(msg.get("title") or [""])
        year = None
        for k in ("published-print", "published-online", "issued"):
            dp = (msg.get(k) or {}).get("date-parts") or [[None]]
            if dp[0] and dp[0][0]:
                year = dp[0][0]
                break
        ratio, year_ok = title_match(real, t, year)
        fams = {unicodedata.normalize("NFKD", a.get("family", "")).encode("ascii", "ignore").decode().lower()
                for a in msg.get("author", [])}
        author_ok = first_surname(t) in fams
        if year_ok and (ratio >= 0.6 or author_ok):
            return "OK", "%s (%s)%s" % (real[:80], year, "" if ratio >= 0.6 else " [auteur + année]")
        return "ÉCHEC", "ne concorde pas avec Crossref : « %s » (%s), recouvrement %.0f %%, 1er auteur %s" % (
            real[:110], year, ratio * 100, "trouvé" if author_ok else "absent")
    m = re.match(r"https://pubmed\.ncbi\.nlm\.nih\.gov/(\d+)/?$", u)
    if m:
        pmid = m.group(1)
        time.sleep(0.4)  # E-utilities : 3 requêtes/s sans clé
        st, body = get("https://eutils.ncbi.nlm.nih.gov/entrez/eutils/esummary.fcgi?db=pubmed&retmode=json&id=" + pmid)
        if st != 200:
            return "À VÉRIFIER", "PubMed HTTP %s" % st
        res = json.loads(body).get("result", {}).get(pmid)
        if not res or res.get("error"):
            return "ÉCHEC", "PMID inconnu"
        real = res.get("title", "")
        year = (re.findall(r"\d{4}", res.get("pubdate", "")) or [None])[0]
        ratio, year_ok = title_match(real, t, year)
        fams = {unicodedata.normalize("NFKD", a.get("name", "").rsplit(" ", 1)[0]).encode("ascii", "ignore").decode().lower()
                for a in res.get("authors", [])}
        author_ok = first_surname(t) in fams
        if year_ok and (ratio >= 0.6 or author_ok):
            return "OK", "%s (%s)%s" % (real[:80], year, "" if ratio >= 0.6 else " [auteur + année]")
        return "ÉCHEC", "ne concorde pas avec PubMed : « %s » (%s), recouvrement %.0f %%, 1er auteur %s" % (
            real[:110], year, ratio * 100, "trouvé" if author_ok else "absent")
    st, _ = get(u, ua=BROWSER_UA)
    if 200 <= st < 400:
        return "OK", "page accessible (HTTP %d)" % st
    if st in (401, 403, 429, 0):
        return "À VÉRIFIER", "HTTP %s (protection anti-robots ?)" % st
    return "ÉCHEC", "HTTP %s" % st


def targets(arg):
    """Liste de (origine, source) à vérifier."""
    out = []
    if arg and arg.endswith("textes.py"):
        for slug, t in load(arg).TEXTES.items():
            out += [("donnees/" + slug, s) for s in t.get("sources", [])]
        return out
    if arg and arg.endswith(".py") and "satellites" in arg:
        for a in load(arg).ENTRIES:
            out += [(a["slug"], s) for s in a.get("sources", [])]
        return out
    if not arg or "satellites" in arg:
        d = os.path.join(ROOT, "tools", "satellites")
        for f in sorted(os.listdir(d)):
            if f.endswith(".py") and not f.startswith("_"):
                for a in load(os.path.join(d, f)).ENTRIES:
                    out += [(a["slug"], s) for s in a.get("sources", [])]
    if not arg or "methode" in arg:
        d = os.path.join(ROOT, "tools", "methode")
        for f in sorted(os.listdir(d)):
            if f.endswith(".py") and not f.startswith("_"):
                mod = load(os.path.join(d, f))
                for p in getattr(mod, "PAGES", []) or [mod.PAGE]:
                    for r in p.get("refs", []):
                        for href in re.findall(r'href="([^"]+)"', r):
                            out.append(("methode/" + p["slug"], {"t": re.sub(r"<[^>]+>", " ", r), "u": href}))
    return out


if __name__ == "__main__":
    arg = sys.argv[1] if len(sys.argv) > 1 else None
    todo = targets(arg)
    fails = warns = 0
    for origin, src in todo:
        st, detail = check(src)
        if st != "OK":
            fails += st == "ÉCHEC"
            warns += st == "À VÉRIFIER"
            print("%-10s %-44s %s\n           %s\n           → %s" % (st, origin, src["u"], re.sub(r"\s+", " ", src["t"])[:150], detail))
    print("\n%d sources vérifiées : %d OK, %d à vérifier, %d en échec" % (len(todo), len(todo) - fails - warns, warns, fails))
    sys.exit(1 if fails else 0)
