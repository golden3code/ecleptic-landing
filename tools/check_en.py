#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Contrôle les traductions anglaises (articles ou pages méthode), sans rien écrire.

    python3 tools/check_en.py tools/en/articles/batch_a.py
    python3 tools/check_en.py tools/en/methode/vo2max.py
    python3 tools/check_en.py            # toutes les traductions

Vérifie : slug français existant, slug anglais attendu (tools/en/slugs.py ou
i18n.METHODE_EN_SLUG), longueurs, même nombre de FAQ, de tableaux et de liens
internes que le français (mêmes cibles), balises équilibrées, restes de français.
"""
import glob, importlib.util, os, re, sys

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
TOOLS = os.path.join(ROOT, "tools")
TAGS = ("p", "ul", "ol", "li", "h2", "h3", "strong", "em", "a", "table", "thead", "tbody", "tr", "th", "td", "caption", "div")
FRENCH = re.compile(r"\b(le|la|les|des|du|est|pour|avec|dans|une|sur|pas|que|qui|ton|ta|tes|tu|et|ou|au|aux|ce|cette|ces|mais|plus|très)\b", re.I)


def load(path, name):
    spec = importlib.util.spec_from_file_location(name, path)
    mod = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(mod)
    return mod


def fr_articles():
    out = {}
    for f in sorted(glob.glob(os.path.join(TOOLS, "satellites", "*.py"))):
        if not os.path.basename(f).startswith("_"):
            for a in load(f, "fr_" + os.path.basename(f)[:-3]).ENTRIES:
                out[a["slug"]] = a
    return out


def fr_methode():
    out = {}
    for f in sorted(glob.glob(os.path.join(TOOLS, "methode", "*.py"))):
        if not os.path.basename(f).startswith("_"):
            m = load(f, "frm_" + os.path.basename(f)[:-3])
            for p in getattr(m, "PAGES", []) or [m.PAGE]:
                out[p["slug"]] = p
    return out


def words(h):
    return len(re.sub(r"<[^>]+>", " ", h).split())


def links(h):
    return sorted(re.findall(r'href="(/[^"]*)"', h))


def french_ratio(h):
    txt = re.sub(r"<[^>]+>", " ", h)
    n = len(txt.split()) or 1
    return len(FRENCH.findall(txt)) / n


def common(label, en, fr, bad, body_key="body"):
    b = en.get(body_key, "")
    if not b:
        bad("corps vide")
        return
    for t in TAGS:
        o, c = len(re.findall(r"<%s[\s>]" % t, b)), len(re.findall(r"</%s>" % t, b))
        if o != c:
            bad("balises <%s> déséquilibrées (%d/%d)" % (t, o, c))
    if links(b) != links(fr.get(body_key, "")):
        bad("liens internes différents du français : %s ≠ %s" % (links(b), links(fr.get(body_key, ""))))
    if b.count("<table") != fr.get(body_key, "").count("<table"):
        bad("nombre de tableaux différent du français")
    if re.search(r'href="https?://', b):
        bad("lien externe dans le corps")
    if re.search(r"ecleptic", b, re.I):
        bad("« Ecleptic » dans le corps")
    wr = words(b) / max(1, words(fr.get(body_key, "")))
    if not 0.75 <= wr <= 1.3:
        bad("longueur %.0f %% du français (attendu 75-130 %%)" % (wr * 100))
    fr_r = french_ratio(b)
    if fr_r > 0.04:
        bad("restes de français probables (%.1f %% de mots-outils français)" % (fr_r * 100))
    d = en.get("description", "")
    if d and not 120 <= len(d) <= 165:
        bad("description de %d caractères (attendu 140-160)" % len(d))
    if len(en.get("faq", [])) != len(fr.get("faq", [])):
        bad("FAQ : %d questions contre %d en français" % (len(en.get("faq", [])), len(fr.get("faq", []))))
    t = en.get("seo_title") or en.get("title", "")
    if len(t) > 60 and not en.get("seo_title"):
        bad("titre de %d caractères : ajoute un seo_title ≤ 60" % len(t))
    if en.get("seo_title") and len(en["seo_title"]) > 60:
        bad("seo_title de %d caractères (max 60)" % len(en["seo_title"]))


def check_articles(path, FR, SL):
    probs = []
    for e in load(path, "en_" + os.path.basename(path)[:-3]).ENTRIES:
        fs = e.get("fr")
        def bad(m, fs=fs):
            probs.append("%s : %s" % (fs, m))
        if fs not in FR:
            bad("slug français inconnu")
            continue
        if e.get("slug") != SL.get(fs):
            bad("slug anglais %r ≠ attendu %r (tools/en/slugs.py)" % (e.get("slug"), SL.get(fs)))
        common(fs, e, FR[fs], bad)
    return probs


def check_methode(path, FRM, MS):
    probs = []
    mod = load(path, "enm_" + os.path.basename(path)[:-3])
    for e in (getattr(mod, "PAGES", []) or [mod.PAGE]):
        fs = e.get("fr")
        def bad(m, fs=fs):
            probs.append("%s : %s" % (fs, m))
        if fs not in FRM:
            bad("page méthode française inconnue")
            continue
        if e.get("slug") != MS.get(fs):
            bad("slug anglais %r ≠ attendu %r (i18n.METHODE_EN_SLUG)" % (e.get("slug"), MS.get(fs)))
        common(fs, e, FRM[fs], bad)
        for k in ("label", "title", "description", "lead"):
            if not e.get(k):
                bad("champ « %s » manquant" % k)
        if len(e.get("refs", [])) != len(FRM[fs].get("refs", [])):
            bad("références : %d contre %d en français" % (len(e.get("refs", [])), len(FRM[fs].get("refs", []))))
    return probs


if __name__ == "__main__":
    SL = load(os.path.join(TOOLS, "en", "slugs.py"), "slugs").EN_SLUGS
    MS = load(os.path.join(TOOLS, "i18n.py"), "i18n_chk").METHODE_EN_SLUG
    files = sys.argv[1:] or sorted(glob.glob(os.path.join(TOOLS, "en", "articles", "*.py")) +
                                   glob.glob(os.path.join(TOOLS, "en", "methode", "*.py")))
    files = [f for f in files if not os.path.basename(f).startswith("_")]
    FR, FRM, total = None, None, []
    for f in files:
        f = os.path.abspath(f)
        if os.sep + "methode" + os.sep in f:
            FRM = FRM or fr_methode()
            p = check_methode(f, FRM, MS)
        else:
            FR = FR or fr_articles()
            p = check_articles(f, FR, SL)
        total += p
        print("%-44s %s" % (os.path.relpath(f, ROOT), "OK" if not p else "%d problème(s)" % len(p)))
        for x in p:
            print("   - " + x)
    sys.exit(1 if total else 0)
