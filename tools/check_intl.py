#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Contrôle les guides pour coachs en espagnol, allemand, italien, néerlandais et portugais
(tools/<langue>/coachs/*.py), sans rien écrire.

    python3 tools/check_intl.py tools/es/coachs/batch_1.py
    python3 tools/check_intl.py es              # une langue
    python3 tools/check_intl.py                 # tout

Base : la version anglaise du même guide (tools/en/coachs). Vérifie : guide anglais existant,
slug propre et unique dans la langue, titre et description, structure (réponse courte, « à
retenir »), balises équilibrées, liens internes inclus dans ceux de l'anglais, aucun lien
externe, ni « Ecleptic », ni tiret cadratin, ni numéro d'urgence américain ou britannique,
longueur 75-155 % de l'anglais, 3 questions de FAQ, au moins 2 sources, chacune reprise de
l'anglais ou d'une fiche de faits vérifiée (tools/intl/_faits-*.md), restes d'anglais ou de
français, registre (tutoiement). Les avertissements (⚠) ne bloquent pas : à relire.
"""
import glob, importlib.util, os, re, sys

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
TOOLS = os.path.join(ROOT, "tools")
LANGS = ("es", "de", "it", "nl", "pt")
TAGS = ("p", "ul", "ol", "li", "h2", "h3", "strong", "em", "a", "table", "thead", "tbody", "tr", "th", "td", "caption", "div")

SHORT = {"es": "La respuesta corta:", "de": "Die kurze Antwort:", "it": "La risposta breve:",
         "nl": "Het korte antwoord:", "pt": "A resposta curta:"}
TAKEAWAYS = {"es": "Puntos clave", "de": "Das Wichtigste in Kürze", "it": "In sintesi",
             "nl": "In het kort", "pt": "Em resumo"}
ENGLISH = re.compile(r"\b(the|and|with|your|you|is|are|that|this|for|from|which|what|when|should)\b", re.I)
FRENCH = re.compile(r"\b(avec|pour|dans|vous|très|aussi|chez|leurs|cette|est-ce)\b", re.I)
FRENCH_LAW = re.compile(r"(?i)\b(cnil|urssaf|dgccrf|bpjeps|qs-sport|code du sport|micro-entrepr\w*|siret|insee)\b")
FRANCE = re.compile(r"\b(France|Francia|Frankreich|Frankrijk|França|franc[eé]s\w*|französisch\w*|frances[ei]\w*|Frans\w*|francês\w*)\b", re.I)
NON_EU_NUMBERS = re.compile(r"\b(911|999|988|Samaritans)\b")
REGISTER = {
    "de": (re.compile(r"(?<![.!?:]\s)(?<!^)\b(Ihnen|Ihr|Ihre|Ihren|Ihrem|Ihrer)\b"), "vouvoiement allemand (Ihnen, Ihr…) : tutoyer (du, dein)"),
    "es": (re.compile(r"\b(usted|ustedes)\b", re.I), "vouvoiement espagnol (usted) : tutoyer (tú)"),
    "pt": (re.compile(r"\b(tu|teu|tua|teus|tuas|contigo)\b", re.I), "« tu / teu / tua » : portugais du Brésil au « você »"),
    "nl": (re.compile(r"(?:^|[\s(])(u|uw)(?=[\s,.;:!?)])"), "vouvoiement néerlandais (u, uw) : tutoyer (je, jij)"),
    "it": (re.compile(r"\b(Lei|Suo|Sua|Suoi|Sue)\b(?! [A-Z])"), "vouvoiement italien (Lei, Suo) : tutoyer (tu)"),
}


def load(path, name):
    spec = importlib.util.spec_from_file_location(name, path)
    mod = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(mod)
    return mod


def en_guides():
    out = {}
    for f in sorted(glob.glob(os.path.join(TOOLS, "en", "coachs", "*.py"))):
        if not os.path.basename(f).startswith("_"):
            for e in load(f, "en_" + os.path.basename(f)[:-3]).ENTRIES:
                out[e["fr"]] = e
    return out


def fact_urls(lang):
    """URL citables : celles des fiches de faits vérifiées (UE + pays de la langue)."""
    urls = set()
    for f in ("_faits-ue.md", "_faits-%s.md" % lang):
        p = os.path.join(TOOLS, "intl", f)
        if os.path.exists(p):
            for u in re.findall(r"https?://[^\s>\]`\"'<]+", open(p, encoding="utf-8").read()):
                while u.endswith(")") and u.count("(") < u.count(")"):
                    u = u[:-1]  # parenthèse fermante du texte, pas de l'adresse
                urls.add(norm(u))
    return urls


def norm(u):
    """Même document, autre langue : EUR-Lex (/legal-content/XX/), aide Google (?hl=xx)."""
    u = re.sub(r"[?&]hl=[\w-]+", "", u.strip().rstrip(".,;:"))
    u = re.sub(r"(eur-lex\.europa\.eu/legal-content/)[A-Z]{2}/", r"\1FR/", u)
    return u.rstrip("/")


def text(h):
    return re.sub(r"<[^>]+>", " ", h)


def words(h):
    return len(text(h).split())


def links(h):
    return sorted(re.findall(r'href="(/[^"]*)"', h))


def check_entry(e, lang, EN, FACTS, bad, warn):
    fs = e.get("fr")
    en = EN.get(fs)
    if not en:
        bad("pas de version anglaise pour %r (la base des 5 langues)" % fs)
        return
    for k in ("slug", "title", "description", "body"):
        if not e.get(k):
            bad("champ « %s » manquant" % k)
            return
    if not re.match(r"^[a-z0-9]+(?:-[a-z0-9]+)*$", e["slug"]):
        bad("slug %r : minuscules, chiffres et tirets seulement, sans accent" % e["slug"])
    b = e["body"]
    for t in TAGS:
        o, c = len(re.findall(r"<%s[\s>]" % t, b)), len(re.findall(r"</%s>" % t, b))
        if o != c:
            bad("balises <%s> déséquilibrées (%d/%d)" % (t, o, c))
    if not re.match(r"\s*<p>%s" % re.escape(SHORT[lang]), b):
        bad("le corps doit commencer par <p>%s" % SHORT[lang])
    if "<h2>%s</h2>" % TAKEAWAYS[lang] not in b:
        bad("section <h2>%s</h2> absente" % TAKEAWAYS[lang])
    extra = set(links(b)) - set(links(en["body"]))
    if extra:
        bad("lien absent de la version anglaise : %s" % sorted(extra))
    if re.search(r'href="https?://', b):
        bad("lien externe dans le corps")
    if re.search(r"ecleptic", b + e["title"] + e["description"], re.I):
        bad("« Ecleptic » dans le corps, le titre ou la description")
    if "—" in b + e["title"] + e["description"]:
        bad("tiret cadratin")
    if NON_EU_NUMBERS.search(text(b) + " ".join(q["a"] for q in e.get("faq", []))):
        bad("numéro d'urgence américain ou britannique resté (911, 999, 988, Samaritans)")
    if FRENCH_LAW.search(text(b)):
        bad("référence au droit ou aux organismes français : %s" % FRENCH_LAW.search(text(b)).group(0))
    m = FRANCE.search(text(b))
    if m:
        warn("la France est citée dans le corps (« %s ») : vérifier que ce n'est pas une règle française" % m.group(0))
    wr = words(b) / max(1, words(en["body"]))
    if not 0.75 <= wr <= 1.55:
        bad("longueur %.0f %% de l'anglais (attendu 75-155 %%)" % (wr * 100))
    t = text(b)
    n = len(t.split()) or 1
    if len(ENGLISH.findall(t)) / n > 0.02:
        bad("restes d'anglais probables (%.1f %% de mots-outils anglais)" % (100 * len(ENGLISH.findall(t)) / n))
    if len(FRENCH.findall(t)) / n > 0.005:
        bad("restes de français probables (%s)" % ", ".join(sorted(set(FRENCH.findall(t)))[:5]))
    reg = REGISTER.get(lang)
    if reg:
        hits = reg[0].findall(t + " " + " ".join(q["q"] + " " + q["a"] for q in e.get("faq", [])))
        if hits:
            (bad if lang == "pt" else warn)("%s : %s" % (reg[1], ", ".join(sorted(set(hits))[:5])))
    d = e["description"]
    if not 130 <= len(d) <= 165:
        bad("description de %d caractères (attendu 140-160)" % len(d))
    if len(e["title"]) > 60 and not e.get("seo_title"):
        bad("titre de %d caractères : ajoute un seo_title de 60 au plus" % len(e["title"]))
    if e.get("seo_title") and len(e["seo_title"]) > 60:
        bad("seo_title de %d caractères (max 60)" % len(e["seo_title"]))
    if (":" in en["title"]) and ":" not in e["title"]:
        warn("le titre anglais a la forme « Préfixe: suite », pas celui-ci (animation du titre)")
    faq = e.get("faq", [])
    if len(faq) != 3 or not all(q.get("q") and q.get("a") for q in faq):
        bad("FAQ : 3 questions avec réponse attendues (%d)" % len(faq))
    srcs = e.get("sources", [])
    if len(srcs) < 2:
        bad("au moins 2 sources attendues")
    if len(srcs) > 8:
        bad("%d sources : 8 au plus (cite une ou deux lois régionales en exemple)" % len(srcs))
    allowed = {norm(x["u"]) for x in en.get("sources", [])} | FACTS
    for x in srcs:
        if not (x.get("t") and x.get("u", "").startswith("https://")):
            bad("source incomplète ou non https : %r" % x)
        elif norm(x["u"]) not in allowed:
            bad("source ni anglaise ni dans une fiche de faits vérifiée : %s" % x["u"])


def check_file(path, EN, FACTS_BY_LANG, seen):
    lang = os.path.basename(os.path.dirname(os.path.dirname(os.path.abspath(path))))
    probs, warns = [], []
    if lang not in LANGS:
        return ["%s : dossier de langue inconnu (attendu tools/<es|de|it|nl|pt>/coachs/)" % path], []
    for e in load(path, "%s_%s" % (lang, os.path.basename(path)[:-3])).ENTRIES:
        fs = e.get("fr", "?")
        bad = lambda m, fs=fs: probs.append("%s : %s" % (fs, m))
        warn = lambda m, fs=fs: warns.append("%s : %s" % (fs, m))
        check_entry(e, lang, EN, FACTS_BY_LANG[lang], bad, warn)
        key = (lang, e.get("slug"))
        if key in seen and seen[key] != fs:
            bad("slug %r déjà pris par %s" % (e.get("slug"), seen[key]))
        seen[key] = fs
        kf = (lang, "fr", fs)
        if kf in seen:
            bad("guide déjà adapté dans un autre fichier de la langue")
        seen[kf] = path
    return probs, warns


if __name__ == "__main__":
    args = sys.argv[1:]
    files = []
    for a in args or LANGS:
        if a in LANGS:
            files += sorted(glob.glob(os.path.join(TOOLS, a, "coachs", "*.py")))
        else:
            files.append(a)
    files = [os.path.abspath(f) for f in files if not os.path.basename(f).startswith("_")]
    EN = en_guides()
    FACTS = {l: fact_urls(l) for l in LANGS}
    seen, total = {}, 0
    # Les slugs se comparent à toute la langue, même si un seul fichier est contrôlé.
    for l in LANGS:
        for f in sorted(glob.glob(os.path.join(TOOLS, l, "coachs", "*.py"))):
            if os.path.abspath(f) not in files and not os.path.basename(f).startswith("_"):
                for e in load(f, "pre_%s_%s" % (l, os.path.basename(f)[:-3])).ENTRIES:
                    seen[(l, e.get("slug"))] = e.get("fr")
                    seen[(l, "fr", e.get("fr"))] = f
    for f in files:
        p, w = check_file(f, EN, FACTS, seen)
        total += len(p)
        print("%-40s %s%s" % (os.path.relpath(f, ROOT), "OK" if not p else "%d problème(s)" % len(p),
                              "" if not w else ", %d avertissement(s)" % len(w)))
        for x in p:
            print("   - " + x)
        for x in w:
            print("   ⚠ " + x)
    sys.exit(1 if total else 0)
