#!/usr/bin/env python3
# Écrit tools/intl/_calendrier.md : calendrier proposé des guides coachs en es, de, it, nl, pt.
#     python3 tools/intl/calendrier.py
import glob, importlib.util, os, sys
from datetime import date, timedelta

ROOT = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))  # racine du dépôt
LANGS = ("es", "de", "it", "nl", "pt")
FR_DAYS = ["lundi", "mardi", "mercredi", "jeudi", "vendredi", "samedi", "dimanche"]


def load(path, name):
    spec = importlib.util.spec_from_file_location(name, path)
    mod = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(mod)
    return mod


def entries(sub):
    out = {}
    for f in sorted(glob.glob(os.path.join(ROOT, "tools", sub, "*.py"))):
        if not os.path.basename(f).startswith("_"):
            for e in load(f, "x_" + sub.replace("/", "_") + os.path.basename(f)[:-3]).ENTRIES:
                out[e.get("fr") or e["slug"]] = e
    return out


def d(iso):
    x = date.fromisoformat(iso)
    return "%s %02d/%02d" % (FR_DAYS[x.weekday()][:3], x.day, x.month)


s = load(os.path.join(ROOT, "tools", "schedule.py"), "sched")
FR = entries("coachs")
EN = entries("en/coachs")
INTL = {l: entries("%s/coachs" % l) for l in LANGS}
order = [x for x in s.COACH_ORDER if x in EN]
B = date(2026, 12, 15)
rows = []
for i, x in enumerate(order):
    a = s.COACH_SCHEDULE[x]
    b = max(a, (B + timedelta(days=i // 2)).isoformat())
    rows.append((i + 1, x, a, b))

out = []
out.append("# Calendrier proposé : guides pour coachs en espagnol, allemand, italien, néerlandais, portugais\n")
out.append("Option A retenue par le user le 10/11/2026 (lot L10). Rien n'est en ligne : la branche "
           "`feat/guides-coachs-5-langues` attend le « Oui, publie » du user. Disponibles : " +
           ", ".join("%s %d/28" % (l, len(INTL[l])) for l in LANGS) + ".\n")
out.append("## Deux options\n")
out.append("| | A · même jour que le français et l'anglais (RETENUE par le user le 10/11/2026) | B · à l'ouverture de la vague 1 |")
out.append("|---|---|---|")
out.append("| Réglage dans `tools/schedule.py` | `INTL_COACH_START = None` (valeur actuelle) | `INTL_COACH_START = date(2026, 12, 15)` |")
out.append("| Première sortie | 02/12/2026 | 15/12/2026 |")
out.append("| Dernière sortie | 26/12/2026 | 28/12/2026 |")
out.append("| Guides en ligne par langue le 15/12 | 15 | 2 |")
out.append("| Rythme | 1 à 2 par jour et par langue, comme le français | 2 par jour et par langue |")
out.append("| Bouton de fin | « Me prévenir » (e-mail) jusqu'à l'ouverture de la vague 1, puis « Essayer l'espace coach » quand `COACH_INTL_LIVE` passe à vrai pour la langue | idem |")
out.append("")
out.append("Pourquoi A : Google met une à quatre semaines à découvrir une nouvelle section dans une nouvelle langue. "
           "Avec A, la moitié des guides est en ligne avant l'ouverture du 15/12 et tout est sorti avant janvier, "
           "période clé. Les guides publiés avant le 15/12 proposent seulement d'être prévenu : rien n'invite à "
           "s'inscrire avant l'ouverture. Chaque guide sort le même jour dans les 7 langues, donc les liens hreflang "
           "sont complets dès le premier jour.\n")
out.append("## Guide par guide\n")
head = "| N° | A | B | Français | " + " | ".join(l.upper() for l in LANGS) + " |"
out.append(head)
out.append("|" + "---|" * (4 + len(LANGS)))
for n, x, a, b in rows:
    cells = []
    for l in LANGS:
        e = INTL[l].get(x)
        cells.append(e["title"].replace("|", "/") if e else "—")
    out.append("| %d | %s | %s | %s | %s |" % (n, d(a), d(b), FR[x]["title"].replace("|", "/"), " | ".join(cells)))
out.append("")
out.append("## À l'ouverture de la vague 1 (15/12/2026)\n")
out.append("Dans `tools/build_articles.py`, passer à `True` les langues ouvertes dans `COACH_INTL_LIVE` "
           "(es, de, it, nl ; pt seulement si l'on accepte que les coachs brésiliens, vague 3, arrivent sur la "
           "console avant l'ouverture du Brésil). Le bouton devient alors « Essayer l'espace coach » en bas des "
           "guides et « Se connecter » sur la page coachs de la langue, si `COACH_LIVE` est déjà vrai.\n")
open(os.path.join(ROOT, "tools", "intl", "_calendrier.md"), "w").write("\n".join(out) + "\n")
print("ok", {l: len(INTL[l]) for l in LANGS})
