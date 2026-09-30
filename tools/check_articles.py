#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Contrôle un lot d'articles après édition (gabarit, liens, sources), sans rien écrire.

    python3 tools/check_articles.py tools/satellites/batch_a.py
    python3 tools/check_articles.py            # tous les lots

Compare aussi avec la version commitée (git HEAD) : slug, cat, title, description,
date et questions de FAQ ne doivent pas changer.
"""
import importlib.util, os, re, subprocess, sys

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
SAT = os.path.join(ROOT, "tools", "satellites")
FROZEN = ("slug", "cat", "title", "description", "date")
TAGS = ("p", "ul", "ol", "li", "h2", "h3", "strong", "em", "a", "table", "thead", "tbody", "tr", "th", "td", "caption", "div")


def load_src(code, name):
    spec = importlib.util.spec_from_loader(name, loader=None)
    mod = importlib.util.module_from_spec(spec)
    exec(compile(code, name, "exec"), mod.__dict__)
    return mod


def entries(path):
    return load_src(open(path, encoding="utf-8").read(), os.path.basename(path)).ENTRIES


def head_entries(path):
    rel = os.path.relpath(path, ROOT)
    r = subprocess.run(["git", "-C", ROOT, "show", "HEAD:" + rel], capture_output=True, text=True)
    return {a["slug"]: a for a in load_src(r.stdout, "head_" + rel).ENTRIES} if r.returncode == 0 else {}


def all_slugs():
    s = set()
    for f in os.listdir(SAT):
        if f.endswith(".py") and not f.startswith("_"):
            s |= {a["slug"] for a in entries(os.path.join(SAT, f))}
    return s


def methode_slugs():
    d = os.path.join(ROOT, "tools", "methode")
    return {f[:-3].replace("_", "-") for f in os.listdir(d) if f.endswith(".py") and not f.startswith("_")}


def words(h):
    return len(re.sub(r"<[^>]+>", " ", h).split())


def check_file(path, slugs, mslugs):
    problems = []
    head = head_entries(path)
    for a in entries(path):
        sl = a.get("slug", "?")
        def bad(msg):
            problems.append("%s : %s" % (sl, msg))
        old = head.get(sl)
        if old:
            for k in FROZEN:
                if a.get(k) != old.get(k):
                    bad("champ « %s » modifié (interdit)" % k)
            if [q["q"] for q in a.get("faq", [])] != [q["q"] for q in old.get("faq", [])]:
                bad("questions de FAQ modifiées (interdit)")
            grow = words(a["body"]) - words(old["body"])
            if grow > 160:
                bad("corps allongé de %d mots (max +160)" % grow)
        body = a.get("body", "")
        w = words(body)
        if not 600 <= w <= 1150:
            bad("%d mots (attendu 600-1150)" % w)
        if re.search(r"ecleptic", body, re.I):
            bad("« Ecleptic » dans le corps")
        for href in re.findall(r'href="([^"]+)"', body):
            m = re.match(r"/articles/([a-z0-9-]+)\.html$", href)
            if m:
                if m.group(1) not in slugs:
                    bad("lien vers un article inconnu : %s" % href)
                continue
            m = re.match(r"/methode/([a-z0-9-]+)\.html$", href)
            if m:
                if m.group(1) not in mslugs:
                    bad("lien vers une page méthode inconnue : %s" % href)
                continue
            bad("lien non autorisé dans le corps (sources → section Sources) : %s" % href)
        for t in TAGS:
            o = len(re.findall(r"<%s[\s>]" % t, body))
            c = len(re.findall(r"</%s>" % t, body))
            if o != c:
                bad("balises <%s> déséquilibrées (%d ouvertes, %d fermées)" % (t, o, c))
        if "<table" in body and body.count("<table") != body.count('<div class="tablewrap"><table'):
            bad('chaque <table> doit être dans <div class="tablewrap">')
        if body.count("<table") > 1:
            bad("plus d'un tableau")
        srcs = a.get("sources")
        if not srcs or not 3 <= len(srcs) <= 6:
            bad("%s sources (attendu 3 à 6)" % (len(srcs) if srcs else 0))
        for s in srcs or []:
            if not s.get("t") or not s.get("u", "").startswith("https://"):
                bad("source incomplète : %r" % s)
        if len({s.get("u") for s in srcs or []}) != len(srcs or []):
            bad("source en double")
        if len(a.get("faq", [])) != 3:
            bad("FAQ : %d questions (attendu 3)" % len(a.get("faq", [])))
    return problems


if __name__ == "__main__":
    files = sys.argv[1:] or sorted(os.path.join(SAT, f) for f in os.listdir(SAT)
                                   if f.endswith(".py") and not f.startswith("_"))
    slugs, mslugs = all_slugs(), methode_slugs()
    total = []
    for f in files:
        p = check_file(os.path.abspath(f), slugs, mslugs)
        total += p
        print("%-44s %s" % (os.path.relpath(f, ROOT), "OK" if not p else "%d problème(s)" % len(p)))
        for x in p:
            print("   - " + x)
    sys.exit(1 if total else 0)
