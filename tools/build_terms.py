# -*- coding: utf-8 -*-
"""Pages CGU et CGV du site, générées depuis la MÊME source que l'app.

Apple exige, pour un abonnement, un lien vers les conditions d'utilisation dans
la fiche App Store (règle 3.1.2). Source unique, comme pour la confidentialité :
  - français : ~/Desktop/Auros/legal/CGU.md et CGV.md (hors dépôt, aussi copiés
    dans l'app par Auros-Code/scripts/sync-legal.mjs) ;
  - anglais : tools/legal/terms.en.md et terms-of-sale.en.md, traductions tenues
    à la main.
On retire, comme dans l'app, les encadrés internes « > ⚠️ … » et la section finale
« Hypothèses retenues ».

Usage (après chaque modification des CGU ou des CGV) :
    python3 tools/build_terms.py
Écrit cgu.html, cgv.html, en/terms.html, en/terms-of-sale.html, cgv-coachs.html
(CGV des coachs, ~/Desktop/Auros/legal/cgv-coachs.md, en français seul), sous-traitance-coachs.html
et la documentation de l'API des coachs (api-coachs.html et en/coach-api.html, source
~/Desktop/Auros/legal/api-coachs.md, traduction tools/legal/api-coachs.en.md ; seule page avec
du code : `code` en ligne et blocs entre trois accents graves). Échoue si une
traduction anglaise ne correspond plus à la date de la version française (ligne
« <!-- version-fr: AAAA-MM-JJ --> » en tête de la traduction).
"""
import html
import os
import re
import sys

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
LEGAL_DIR = os.environ.get("ECLEPTIC_LEGAL_DIR") or os.path.join(ROOT, "..", "legal")
if not os.path.isdir(LEGAL_DIR):
    LEGAL_DIR = os.path.expanduser("~/Desktop/Auros/legal")

MONTHS_FR = {"janvier": 1, "février": 2, "mars": 3, "avril": 4, "mai": 5, "juin": 6, "juillet": 7,
             "août": 8, "septembre": 9, "octobre": 10, "novembre": 11, "décembre": 12}

FOOT_FR = ('<a href="/">← Accueil</a> · %s · <a href="/confidentialite.html">Confidentialité</a> · '
           '<a href="/mentions-legales.html">Mentions légales</a> · <a href="mailto:contact@ecleptic.app">contact@ecleptic.app</a>')
FOOT_EN = ('<a href="/en/">← Home</a> · %s · <a href="/en/privacy.html">Privacy</a> · '
           '<a href="/en/legal-notice.html">Legal notice</a> · <a href="mailto:contact@ecleptic.app">contact@ecleptic.app</a>')

DOCS = [
    {"fr_source": "CGU.md", "en_source": "terms.en.md",
     "fr": {"file": "cgu.html", "title": "Conditions générales d'utilisation — Ecleptic",
            "description": "Conditions générales d'utilisation de l'application Ecleptic : accès, compte, services, avertissement santé, responsabilité et litiges.",
            "lead": "Ce texte est le même que celui affiché dans l'application Ecleptic.",
            "footer": FOOT_FR % '<a href="/cgv.html">Conditions de vente</a>'},
     "en": {"file": "en/terms.html", "title": "Terms of Use — Ecleptic",
            "description": "Terms of Use of the Ecleptic app: access, account, services, health warning, liability and disputes.",
            "lead": "This is an English translation of the French Terms of Use shown in the Ecleptic app; the French version prevails.",
            "footer": FOOT_EN % '<a href="/en/terms-of-sale.html">Terms of Sale</a>'}},
    {"fr_source": "CGV.md", "en_source": "terms-of-sale.en.md",
     "fr": {"file": "cgv.html", "title": "Conditions générales de vente — Ecleptic",
            "description": "Conditions générales de vente d'Ecleptic : offres Copper et Golden, prix, renouvellement, résiliation, rétractation et garanties.",
            "lead": "Ce texte est le même que celui affiché dans l'application Ecleptic.",
            "footer": FOOT_FR % '<a href="/cgu.html">Conditions d\'utilisation</a>'},
     "en": {"file": "en/terms-of-sale.html", "title": "Terms of Sale — Ecleptic",
            "description": "Terms of Sale of Ecleptic: Copper and Golden offers, price, renewal, cancellation, withdrawal and guarantees.",
            "lead": "This is an English translation of the French Terms of Sale shown in the Ecleptic app; the French version prevails.",
            "footer": FOOT_EN % '<a href="/en/terms.html">Terms of Use</a>'}},
    # Documentation publique de l'API des coachs (plan « Parité », lot C10) : clés, lectures,
    # webhooks, signature, limites. Vérifiée dans le code de coach-api et coach-webhook-send.
    {"fr_source": "api-coachs.md", "en_source": "api-coachs.en.md", "code": True,
     "fr": {"file": "api-coachs.html", "title": "API des coachs : documentation — Ecleptic",
            "description": "Documentation de l'API des coachs d'Ecleptic : clés, lectures des élèves, séances, ventes et réservations, webhooks signés, limites. Aucune donnée de santé ne sort.",
            "lead": "Pour relier ton espace coach à un tableur, à ta comptabilité, au logiciel de ta salle ou à Zapier.",
            "footer": FOOT_FR % '<a href="/cgv-coachs.html">Conditions de vente des coachs</a>'},
     "en": {"file": "en/coach-api.html", "title": "Coach API: documentation — Ecleptic",
            "description": "Documentation of the Ecleptic coach API: keys, reading clients, sessions, sales and bookings, signed webhooks, limits. No health data ever leaves.",
            "lead": "To connect your coach space to a spreadsheet, your accounting, your gym software or Zapier. English translation of the French documentation; the French version prevails.",
            "footer": FOOT_EN % '<a href="/cgv-coachs.html">Coach terms of sale (French)</a>'}},
]

# Pages en français seul, sans traduction anglaise publiée. CGV des coachs (B2B) : les
# traductions de legal/international/cgv-coachs/ visent les coachs établis hors de France
# et ne sont pas publiées. Source : en-tête « **Dernière mise à jour : … ** » obligatoire ;
# les notes internes vont dans un encadré « > ⚠️ … », retiré par clean().
FR_ONLY = [
    {"fr_source": "cgv-coachs.md",
     "fr": {"file": "cgv-coachs.html", "title": "Conditions générales de vente des coachs — Ecleptic",
            "description": "Conditions générales de vente de l'espace coach d'Ecleptic : paliers et prix, essai, abonnement, vente des séances, frais de service, outils reliés et données.",
            "lead": "Conditions de l'abonnement des coachs professionnels à l'espace coach d'Ecleptic, dans l'app et sur coach.ecleptic.health.",
            "footer": FOOT_FR % '<a href="/sous-traitance-coachs.html">Accord de sous-traitance</a> · <a href="/cgu.html">Conditions d\'utilisation</a>'}},
    {"fr_source": "sous-traitance-coach.md",
     "fr": {"file": "sous-traitance-coachs.html", "title": "Accord de sous-traitance des coachs — Ecleptic",
            "description": "Accord de sous-traitance (article 28 du RGPD) annexé aux conditions de vente des coachs d'Ecleptic : données traitées pour le coach, sous-traitants ultérieurs, sécurité et durées.",
            "lead": "Annexe des conditions générales de vente des coachs : Ecleptic traite pour le coach les données de ses élèves, prospects et participants.",
            "footer": FOOT_FR % '<a href="/cgv-coachs.html">Conditions de vente des coachs</a>'}},
]


def clean(md):
    """Même nettoyage que scripts/sync-legal.mjs (app)."""
    md = re.sub(r"\n---\s*\n+## Hypothèses retenues[\s\S]*$", "\n", md)
    md = re.sub(r"(?m)^> ⚠️.*\n(?:^>.*\n?)*", "", md)
    md = re.sub(r"(?m)^<!--.*-->\n", "", md)
    return md.strip() + "\n"


def fr_version(md, name):
    m = re.search(r"Dernière mise à jour\s*:\s*(\d{1,2})(?:er)? (\w+) (\d{4})", md)
    if not m:
        sys.exit("Date « Dernière mise à jour » introuvable dans %s." % name)
    return "%s-%02d-%02d" % (m.group(3), MONTHS_FR[m.group(2).lower()], int(m.group(1)))


def slug(text):
    s = text.lower()
    for a, b in (("àâä", "a"), ("éèêë", "e"), ("îï", "i"), ("ôö", "o"), ("ùûü", "u"), ("ç", "c")):
        s = re.sub("[%s]" % a, b, s)
    return re.sub(r"[^a-z0-9]+", "-", s).strip("-")


def inline(text, code=False):
    """Gras, e-mails et adresses en liens ; avec code=True, `code` en ligne (rien n'est lié dedans)."""
    if code and "`" in text:
        parts = text.split("`")
        if len(parts) % 2 == 1:
            return "".join(("<code>%s</code>" % html.escape(p, quote=False)) if i % 2 else inline(p)
                           for i, p in enumerate(parts))
    t = html.escape(text, quote=False)
    t = re.sub(r"\*\*(.+?)\*\*", r"<strong>\1</strong>", t)
    t = re.sub(r"(?<![\w/@.])([\w.+-]+@[\w-]+\.[\w.]+\w)", r'<a href="mailto:\1">\1</a>', t)
    t = re.sub(r"(?<![\"/\w])(https?://[^\s<)]+[^\s<).,;])", r'<a href="\1" rel="noopener">\1</a>', t)
    return t


def to_html(md, code=False):
    """Markdown → HTML, pour le sous-ensemble des textes juridiques (dont le formulaire en citation).
    code=True (documentation de l'API) : `code` en ligne et blocs ``` recopiés tels quels."""
    out, para, items, quote, table = [], [], [], [], []
    title, date = "", ""
    fence = None
    _inline = globals()["inline"]

    def inline(text):  # noqa: F811 — même fonction, avec le code en ligne si la page en a
        return _inline(text, code)

    def flush():
        if para:
            out.append("  <p>%s</p>" % inline(" ".join(para)))
            para.clear()
        if items:
            out.append("  <ul>\n%s\n  </ul>" % "\n".join("    <li>%s</li>" % inline(i) for i in items))
            items.clear()
        if quote:
            out.append("  <blockquote>%s</blockquote>" % "<br>\n    ".join(inline(q) for q in quote))
            quote.clear()
        if table:
            head, body = table[0], [r for r in table[1:] if not all(re.match(r"^:?-+:?$", c) for c in r)]
            t = ['  <div class="table"><table>', "    <thead><tr>%s</tr></thead>" % "".join("<th>%s</th>" % inline(c) for c in head), "    <tbody>"]
            t += ["      <tr>%s</tr>" % "".join("<td>%s</td>" % inline(c) for c in r) for r in body]
            t += ["    </tbody>", "  </table></div>"]
            out.append("\n".join(t))
            table.clear()

    for raw in md.split("\n"):
        line = raw.rstrip()
        if code and fence is not None:
            if line.strip() == "```":
                out.append("  <pre><code>%s</code></pre>" % html.escape("\n".join(fence), quote=False))
                fence = None
            else:
                fence.append(raw)
            continue
        if code and line.strip().startswith("```"):
            flush(); fence = []
            continue
        if line.startswith("# "):
            flush(); title = line[2:].strip()
        elif re.match(r"^\*\*(Dernière mise à jour|Last updated)", line):
            flush(); date = line.strip("*").strip()
        elif line.startswith("### "):
            flush(); out.append('  <h3 id="%s">%s</h3>' % (slug(line[4:]), inline(line[4:])))
        elif line.startswith("## "):
            flush(); out.append('  <h2 id="%s">%s</h2>' % (slug(line[3:]), inline(line[3:])))
        elif line.startswith("|"):
            if para or items or quote:
                flush()
            table.append([c.strip() for c in line.strip().strip("|").split("|")])
        elif line.startswith(">"):
            if para or items or table:
                flush()
            text = line[1:].strip()
            if text:
                quote.append(text)
        elif line.startswith("- "):
            if para or quote or table:
                flush()
            items.append(line[2:])
        elif line.strip() in ("", "---"):
            flush()
        else:
            if items or quote or table or re.match(r"^\d+\. ", line):
                flush()
            para.append(line.strip())
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
  .table{overflow-x:auto;margin:12px 0}
  table{border-collapse:collapse;width:100%;min-width:520px}
  th,td{border:1px solid var(--line);padding:8px 10px;text-align:left;vertical-align:top}
  th{color:var(--ink);font-weight:600}
  p{margin:8px 0}
  ul{padding-left:22px;margin:6px 0}
  li{margin:4px 0}
  blockquote{border-left:2px solid var(--line);padding:6px 0 6px 14px;margin:12px 0;font-size:15px;color:#CFC5B0}
  footer{margin-top:40px;border-top:1px solid var(--line);padding-top:16px;color:var(--muted);font-size:13px}
</style>"""


def head(lang, doc):
    """En-tête de la page Confidentialité (CSP, icônes, routage de langue), adapté à la page."""
    src = open(os.path.join(ROOT, "confidentialite.html"), encoding="utf-8").read()
    h = src[: src.index("<style>")]
    page, fr_url = doc[lang], "https://ecleptic.health/" + doc["fr"]["file"]
    if "en" not in doc:  # français seul : pas de version anglaise, donc pas de renvoi de langue
        h = re.sub(r'<link rel="alternate" hreflang="[^"]*" href="[^"]*">\n', "", h)
    en_url = "https://ecleptic.health/" + doc["en"]["file"] if "en" in doc else fr_url
    h = h.replace('<html lang="fr">', '<html lang="%s">' % lang)
    h = re.sub(r"<title>.*?</title>", "<title>%s</title>" % html.escape(page["title"], quote=False), h)
    h = re.sub(r'<meta name="description" content="[^"]*">', '<meta name="description" content="%s">' % html.escape(page["description"]), h)
    h = re.sub(r'<link rel="canonical" href="[^"]*">', '<link rel="canonical" href="%s">' % (fr_url if lang == "fr" else en_url), h)
    h = re.sub(r'(<link rel="alternate" hreflang="fr" href=")[^"]*', r"\g<1>" + fr_url, h)
    h = re.sub(r'(<link rel="alternate" hreflang="(?:en|x-default)" href=")[^"]*', r"\g<1>" + en_url, h)
    return h


CODE_STYLE = """<style>
  code{font-family:ui-monospace,SFMono-Regular,Menlo,Consolas,monospace;font-size:.9em;color:var(--ink);background:#17140F;border:1px solid var(--line);border-radius:4px;padding:1px 5px;overflow-wrap:anywhere}
  pre{background:#17140F;border:1px solid var(--line);border-radius:6px;padding:12px 14px;margin:12px 0;overflow-x:auto}
  pre code{background:none;border:0;padding:0;font-size:13.5px;line-height:1.55;white-space:pre;overflow-wrap:normal}
</style>"""


def build(lang, doc, md):
    page = doc[lang]
    title, date, body = to_html(md, doc.get("code", False))
    style = STYLE + ("\n" + CODE_STYLE if doc.get("code") else "")
    out = (head(lang, doc) + style + "\n</head>\n<body>\n<div class=\"wrap\">\n"
           "  <h1>%s</h1>\n  <p class=\"date\">%s</p>\n  <p class=\"lead\">%s</p>\n%s\n"
           "  <footer>\n    %s\n  </footer>\n</div>\n</body>\n</html>\n"
           % (inline(title), inline(date), page["lead"], body, page["footer"]))
    open(os.path.join(ROOT, page["file"]), "w", encoding="utf-8").write(out)
    print("%s écrit (%s)" % (page["file"], date))


def main():
    for doc in DOCS:
        fr_raw = open(os.path.join(LEGAL_DIR, doc["fr_source"]), encoding="utf-8").read()
        en_raw = open(os.path.join(ROOT, "tools", "legal", doc["en_source"]), encoding="utf-8").read()
        version = fr_version(fr_raw, doc["fr_source"])
        m = re.search(r"<!-- version-fr: (\d{4}-\d{2}-\d{2}) -->", en_raw)
        if not m or m.group(1) != version:
            sys.exit("Traduction anglaise %s à mettre à jour : elle suit la version française du %s, "
                     "%s est daté du %s." % (doc["en_source"], m.group(1) if m else "?", doc["fr_source"], version))
        build("fr", doc, clean(fr_raw))
        build("en", doc, clean(en_raw))
    for doc in FR_ONLY:
        fr_raw = open(os.path.join(LEGAL_DIR, doc["fr_source"]), encoding="utf-8").read()
        fr_version(fr_raw, doc["fr_source"])
        build("fr", doc, clean(fr_raw))


if __name__ == "__main__":
    main()
