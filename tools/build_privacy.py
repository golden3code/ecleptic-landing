# -*- coding: utf-8 -*-
"""Pages Confidentialité du site, générées depuis la MÊME source que l'app.

Google (fiche Play, revue Health Connect) exige que la politique publiée sur le
site soit identique à celle de l'application. Source unique :
  - français : ~/Desktop/Auros/legal/politique-de-confidentialite.md (hors dépôt,
    aussi copiée dans l'app par Auros-Code/scripts/sync-legal.mjs) ;
  - anglais : tools/legal/privacy-policy.en.md, traduction tenue à la main.
On retire, comme dans l'app, les encadrés internes « > ⚠️ … » et la section finale
« Hypothèses retenues ».

Usage (après chaque modification de la politique) :
    python3 tools/build_privacy.py
Écrit confidentialite.html et en/privacy.html. Échoue si la traduction anglaise
ne correspond plus à la date de la version française (ligne
« <!-- version-fr: AAAA-MM-JJ --> » en tête de la traduction).
"""
import html
import os
import re
import sys

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
FR_SOURCE = os.path.join(ROOT, "..", "legal", "politique-de-confidentialite.md")
EN_SOURCE = os.path.join(ROOT, "tools", "legal", "privacy-policy.en.md")

MONTHS_FR = {"janvier": 1, "février": 2, "mars": 3, "avril": 4, "mai": 5, "juin": 6, "juillet": 7,
             "août": 8, "septembre": 9, "octobre": 10, "novembre": 11, "décembre": 12}


def clean(md):
    """Même nettoyage que scripts/sync-legal.mjs (app)."""
    md = re.sub(r"\n---\s*\n+## Hypothèses retenues[\s\S]*$", "\n", md)
    md = re.sub(r"(?m)^> ⚠️.*\n(?:^>.*\n?)*", "", md)
    md = re.sub(r"(?m)^<!--.*-->\n", "", md)
    return md.strip() + "\n"


def fr_version(md):
    m = re.search(r"Dernière mise à jour\s*:\s*(\d{1,2})(?:er)? (\w+) (\d{4})", md)
    if not m:
        sys.exit("Date « Dernière mise à jour » introuvable dans la politique française.")
    return "%s-%02d-%02d" % (m.group(3), MONTHS_FR[m.group(2).lower()], int(m.group(1)))


def slug(text):
    s = text.lower()
    for a, b in (("àâä", "a"), ("éèêë", "e"), ("îï", "i"), ("ôö", "o"), ("ùûü", "u"), ("ç", "c")):
        s = re.sub("[%s]" % a, b, s)
    return re.sub(r"[^a-z0-9]+", "-", s).strip("-")


def inline(text):
    t = html.escape(text, quote=False)
    t = re.sub(r"\*\*(.+?)\*\*", r"<strong>\1</strong>", t)
    t = re.sub(r"(?<![\w/@.])([\w.+-]+@[\w-]+\.[\w.]+\w)", r'<a href="mailto:\1">\1</a>', t)
    t = re.sub(r"(?<![\"/\w])(https?://[^\s<)]+[^\s<).,;])", r'<a href="\1" rel="noopener">\1</a>', t)
    t = re.sub(r"(?<![/\w.])(www\.[a-z0-9.-]+\.[a-z]{2,})", r'<a href="https://\1" rel="noopener">\1</a>', t)
    return t


def to_html(md):
    """Markdown → HTML, pour le sous-ensemble des textes juridiques."""
    out, para, items = [], [], []
    lines = md.split("\n")
    title, date = "", ""

    def flush():
        if para:
            out.append("  <p>%s</p>" % inline(" ".join(para)))
            para.clear()
        if items:
            out.append("  <ul>\n%s\n  </ul>" % "\n".join("    <li>%s</li>" % inline(i) for i in items))
            items.clear()

    i = 0
    while i < len(lines):
        line = lines[i].rstrip()
        if line.startswith("# "):
            flush(); title = line[2:].strip()
        elif re.match(r"^\*\*(Dernière mise à jour|Last updated)", line):
            flush(); date = line.strip("*").strip()
        elif line.startswith("### "):
            flush(); out.append('  <h3 id="%s">%s</h3>' % (slug(line[4:]), inline(line[4:])))
        elif line.startswith("## "):
            flush(); out.append('  <h2 id="%s">%s</h2>' % (slug(line[3:]), inline(line[3:])))
        elif line.startswith("|"):
            flush()
            rows = []
            while i < len(lines) and lines[i].startswith("|"):
                rows.append([c.strip() for c in lines[i].strip().strip("|").split("|")])
                i += 1
            head, body = rows[0], [r for r in rows[2:]]
            t = ['  <div class="table"><table>', "    <thead><tr>%s</tr></thead>" % "".join("<th>%s</th>" % inline(c) for c in head), "    <tbody>"]
            t += ["      <tr>%s</tr>" % "".join("<td>%s</td>" % inline(c) for c in r) for r in body]
            t += ["    </tbody>", "  </table></div>"]
            out.append("\n".join(t))
            continue
        elif line.startswith("- "):
            if para:
                flush()
            items.append(line[2:])
        elif line.strip() in ("", "---"):
            flush()
        else:
            if items:
                flush()
            para.append(line.strip())
        i += 1
    flush()
    return title, date, "\n".join(out)


STYLE = """<style>
  :root{--gold:#D9A441;--ink:#F2EBDD;--muted:#9A8E77;--bg:#0B0A08;--line:#2A241B;color-scheme:dark}
  *{box-sizing:border-box;margin:0;padding:0}
  body{font-family:-apple-system,BlinkMacSystemFont,"Segoe UI",sans-serif;background:var(--bg);color:var(--ink);line-height:1.65}
  .wrap{max-width:760px;margin:0 auto;padding:48px 24px 64px}
  a{color:var(--gold);overflow-wrap:anywhere}
  h1{font-size:28px;margin-bottom:4px}
  .date{color:var(--muted);font-size:14px;margin-bottom:12px}
  .lead{color:var(--muted);font-size:14px;margin-bottom:28px}
  h2{font-size:19px;margin:32px 0 8px}
  h3{font-size:16px;margin:22px 0 6px;color:var(--ink)}
  p,li,td,th{font-size:15.5px;color:#CFC5B0}
  p{margin:8px 0}
  ul{padding-left:22px;margin:6px 0}
  li{margin:4px 0}
  .table{overflow-x:auto;margin:12px 0}
  table{border-collapse:collapse;width:100%;min-width:520px}
  th,td{border:1px solid var(--line);padding:8px 10px;text-align:left;vertical-align:top;font-size:14px}
  th{color:var(--ink);font-weight:600}
  footer{margin-top:40px;border-top:1px solid var(--line);padding-top:16px;color:var(--muted);font-size:13px}
</style>"""

PAGES = {
    "fr": {
        "file": "confidentialite.html",
        "lead": "Ce texte est le même que celui affiché dans l'application Ecleptic. Pour supprimer ton compte : "
                '<a href="/suppression-compte.html">suppression du compte et des données</a>.',
        "footer": '<a href="/">← Accueil</a> · <a href="/suppression-compte.html">Supprimer mon compte</a> · '
                  '<a href="/mentions-legales.html">Mentions légales</a> · <a href="mailto:contact@ecleptic.app">contact@ecleptic.app</a>',
    },
    "en": {
        "file": os.path.join("en", "privacy.html"),
        "lead": "This is an English translation of the French privacy policy shown in the Ecleptic app; "
                "the French version prevails. To delete your account: "
                '<a href="/en/delete-account.html">account and data deletion</a>.',
        "footer": '<a href="/en/">← Home</a> · <a href="/en/delete-account.html">Delete my account</a> · '
                  '<a href="/en/legal-notice.html">Legal notice</a> · <a href="mailto:contact@ecleptic.app">contact@ecleptic.app</a>',
    },
}


def build(lang, md):
    page = PAGES[lang]
    path = os.path.join(ROOT, page["file"])
    current = open(path, encoding="utf-8").read()
    # En-tête existant (CSP, balises meta, hreflang, routage de langue) conservé tel quel.
    head = current[: current.index("<style>")]
    title, date, body = to_html(md)
    doc = (head + STYLE + "\n</head>\n<body>\n<div class=\"wrap\">\n"
           "  <h1>%s</h1>\n  <p class=\"date\">%s</p>\n  <p class=\"lead\">%s</p>\n%s\n"
           "  <footer>\n    %s\n  </footer>\n</div>\n</body>\n</html>\n"
           % (inline(title), inline(date), page["lead"], body, page["footer"]))
    open(path, "w", encoding="utf-8").write(doc)
    print("%s écrit (%s)" % (page["file"], date))


def main():
    fr_raw = open(FR_SOURCE, encoding="utf-8").read()
    en_raw = open(EN_SOURCE, encoding="utf-8").read()
    version = fr_version(fr_raw)
    m = re.search(r"<!-- version-fr: (\d{4}-\d{2}-\d{2}) -->", en_raw)
    if not m or m.group(1) != version:
        sys.exit("Traduction anglaise à mettre à jour : elle suit la version française du %s, "
                 "la politique française est datée du %s." % (m.group(1) if m else "?", version))
    build("fr", clean(fr_raw))
    build("en", clean(en_raw))


if __name__ == "__main__":
    main()
