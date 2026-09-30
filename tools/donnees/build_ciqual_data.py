#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Table Ciqual 2025 (ANSES) → tools/donnees/ciqual.json, lu par build_articles.py.

    python3 tools/donnees/build_ciqual_data.py

Entrée : tools/donnees/ciqual-2025/ (fichiers officiels du dépôt Zenodo 17550133 de
l'ANSES, licence CC BY 4.0 ; non versionnés, voir fetch en bas de ce fichier).
Sortie : classements par nutriment, déterministes (tri valeur décroissante, puis code).
Règles de valeurs Ciqual : « 12,3 » → 12.3 ; « traces » → 0 ; « < 0,5 » et « - » → non
classés (valeur inconnue ou sous le seuil de quantification).
"""
import html, json, os, re, sys, urllib.parse, urllib.request, hashlib

HERE = os.path.dirname(os.path.abspath(__file__))
RAW = os.path.join(HERE, "ciqual-2025")
XLSX = "Table Ciqual 2025_ENG_2025_11_03.xlsx"
ZENODO = "17550133"
FILES = [XLSX, "alim_2025_11_03.xml", "alim_grp_2025_11_03.xml", "const_2025_11_03.xml"]

# Sous-groupes exclus des classements « au quotidien » : consommés en très petites
# quantités, compléments, produits infantiles, alcool, viandes et poissons crus
# (la version cuite est gardée), moyennes Ciqual (groupe 00).
EXCLUDE_DAILY = {"1002", "1003", "1004", "1005", "1006", "1007", "1008", "1009", "0904",
                 "0601", "0602", "0603", "0701", "0703", "0402", "0406", "0408", "0304"}
EXCLUDE_GROUPS = {"00", "11"}
CONDIMENTS = {"1005", "1006", "1007", "1002"}  # records bruts cités à part (épices, herbes, algues…)

# Valeurs manifestement atypiques, écartées des classements (revue manuelle du 30/09/2026,
# détection : valeur > 3× la médiane des aliments de même nom ; seules celles qu'aucune
# explication ne justifie — séché/frais, enrichi, graine/chair — sont écartées).
ATYPICAL = {
    ("zinc", "15045"): "Tournesol, graine, grillé, salé : 36 mg/100 g, environ 7 fois les autres graines de tournesol de la table",
}

FAMILIES = [
    ("viandes", "Viandes", "Meat", {"0401"}),
    ("poissons", "Poissons et fruits de mer", "Fish and seafood", {"0405", "0407", "0409"}),
    ("oeufs-laitiers", "Œufs et produits laitiers", "Eggs and dairy", {"0410", "0501", "0502", "0503"}),
    ("feculents", "Légumineuses, céréales, tubercules", "Legumes, grains, tubers", {"0203", "0301", "0302", "0202"}),
    ("fruits-legumes", "Fruits et légumes", "Fruits and vegetables", {"0201", "0204"}),
    ("oleagineux", "Fruits à coque et graines", "Nuts and seeds", {"0205"}),
]

# slug : (colonne xlsx (préfixe), unité, VNR UE 1169/2011 ou None)
NUTRIENTS = {
    "proteines": ("Protein\n(g", "g", None),
    "fer": ("Iron (mg", "mg", 14),
    "magnesium": ("Magnesium\n(mg", "mg", 375),
    "calcium": ("Calcium\n(mg", "mg", 800),
    "fibres": ("Fibres\n(g", "g", None),
    "vitamine-c": ("Vitamin\nC (mg", "mg", 80),
    "vitamine-d": ("Vitamin\nD (µg", "µg", 5),
    "potassium": ("Potassium\n(mg", "mg", 2000),
    "zinc": ("Zinc\n(mg", "mg", 10),
    "vitamine-b12": ("Vitamin\nB12\n(µg", "µg", 2.5),
}
KCAL = "Energy,\nRegulation\nEU No\n1169\n2011 (kcal"
ALA = "FA 18:3\nc9,c12,c15"
EPA = "FA 20:5"
DHA = "FA 22:6"


def fetch():
    """Télécharge les fichiers officiels (Zenodo, ANSES) avec contrôle MD5."""
    os.makedirs(RAW, exist_ok=True)
    rec = json.load(urllib.request.urlopen(urllib.request.Request(
        "https://zenodo.org/api/records/" + ZENODO, headers={"Accept": "application/json"})))
    sums = {f["key"]: f["checksum"] for f in rec["files"]}
    for k in FILES:
        url = "https://zenodo.org/records/%s/files/%s?download=1" % (ZENODO, urllib.parse.quote(k))
        data = urllib.request.urlopen(urllib.request.Request(url, headers={"User-Agent": "Mozilla/5.0"})).read()
        if "md5:" + hashlib.md5(data).hexdigest() != sums[k]:
            raise SystemExit("MD5 différent pour " + k)
        open(os.path.join(RAW, k), "wb").write(data)
        print("téléchargé", k)


def num(v):
    if v is None:
        return None
    s = str(v).strip().replace(" ", " ")
    if s in ("", "-"):
        return None
    if s.lower() == "traces":
        return 0.0
    if s.startswith("<"):
        return None
    try:
        return float(s.replace(",", "."))
    except ValueError:
        return None


def clean(name):
    """Nom affiché : entités décodées, espaces normalisés, lieu d'échantillonnage abrégé
    (« …, prélevée à la Martinique » → « … (Martinique) »)."""
    n = re.sub(r"\s+", " ", html.unescape(name)).strip()
    n = re.sub(r"\s*,\s*prélevée?s? (?:à|en) (?:la |La )?(Martinique|Réunion|Guadeloupe|Guyane|Mayotte)", r" (\1)", n)
    n = re.sub(r"\s*,\s*sampled in the island(?: of)? (?:La )?(Martinique|Réunion|Guadeloupe|Guyane|Mayotte)", r" (\1)", n)
    return n.replace(" ,", ",")


def xml_records(fn, tag):
    s = open(os.path.join(RAW, fn), encoding="utf-8-sig").read()
    out = []
    for b in re.findall(r"<%s>(.*?)</%s>" % (tag, tag), s, re.S):
        out.append({k: v.strip() for k, v in re.findall(r"<(\w+)>(.*?)</\1>", b, re.S)})
    return out


def load():
    import openpyxl
    names = {r["alim_code"]: r for r in xml_records("alim_2025_11_03.xml", "ALIM")}
    grps = {}
    for r in xml_records("alim_grp_2025_11_03.xml", "ALIM_GRP"):
        grps[r["alim_ssgrp_code"]] = (clean(r["alim_ssgrp_nom_fr"]), clean(r["alim_ssgrp_nom_eng"]))
    ws = openpyxl.load_workbook(os.path.join(RAW, XLSX), read_only=True)["food composition"]
    rows = ws.iter_rows(values_only=True)
    hdr = [str(h or "") for h in next(rows)]

    def col(prefix):
        hits = [i for i, h in enumerate(hdr) if h.startswith(prefix)]
        if len(hits) != 1:
            raise SystemExit("colonne ambiguë ou absente : %r → %s" % (prefix, hits))
        return hits[0]
    cols = {k: col(v[0]) for k, v in NUTRIENTS.items()}
    cols.update({"kcal": col(KCAL), "ala": col(ALA), "epa": col(EPA), "dha": col(DHA)})
    foods = []
    for r in rows:
        code = str(r[6]).strip()
        if code not in names:
            continue
        n = names[code]
        ss = n.get("alim_ssgrp_code", "")
        foods.append({
            "code": code, "fr": clean(n["alim_nom_fr"]), "en": clean(n["alim_nom_eng"]),
            "grp": n.get("alim_grp_code", ""), "ss": ss,
            "ss_fr": grps.get(ss, ("", ""))[0], "ss_en": grps.get(ss, ("", ""))[1],
            "v": {k: num(r[i]) for k, i in cols.items()},
        })
    return foods


def head_key(f):
    """Regroupe les quasi-doublons (« Thon, au naturel… », « Thon, à l'huile… ») sur le
    premier segment du nom, pour des classements variés."""
    return re.split(r"[,(]", f["fr"])[0].strip().lower()


def ranked(foods, key, pool, n, dedupe=True, value=None):
    value = value or (lambda f: f["v"][key])
    cand = sorted((f for f in pool(foods) if value(f) is not None and value(f) > 0 and (key, f["code"]) not in ATYPICAL),
                  key=lambda f: (-value(f), f["code"]))
    out, seen = [], set()
    for f in cand:
        h = head_key(f)
        if dedupe and h in seen:
            continue
        seen.add(h)
        out.append({"code": f["code"], "fr": f["fr"], "en": f["en"], "grp_fr": f["ss_fr"], "grp_en": f["ss_en"],
                    "v": round(value(f), 3)})
        if len(out) == n:
            break
    return out


def daily(foods):
    return [f for f in foods if f["grp"] not in EXCLUDE_GROUPS and f["ss"] not in EXCLUDE_DAILY]


def build():
    foods = load()
    out = {"source": "Anses. 2025. Table de composition nutritionnelle des aliments Ciqual.",
           "source_en": "Anses. 2025. Ciqual French food composition table.",
           "version": "2025-11-03", "doi": "https://doi.org/10.5281/zenodo.17550133",
           "licence": "CC BY 4.0", "n_foods": len(foods), "nutrients": {},
           "atypical": {k + ":" + c: why for (k, c), why in ATYPICAL.items()}}
    for k, (_, unit, nrv) in NUTRIENTS.items():
        known = sum(1 for f in foods if f["v"][k] is not None)
        entry = {"unit": unit, "nrv": nrv, "n_known": known,
                 "top": ranked(foods, k, daily, 25),
                 "families": [{"slug": s, "fr": fr, "en": en,
                               "items": ranked(foods, k, lambda fs, g=g: [f for f in daily(fs) if f["ss"] in g], 3)}
                              for s, fr, en, g in FAMILIES],
                 "condiments": ranked(foods, k, lambda fs: [f for f in fs if f["ss"] in CONDIMENTS], 5)}
        if k == "proteines":
            dens = lambda f: (f["v"]["proteines"] / f["v"]["kcal"] * 100) if (
                f["v"]["proteines"] is not None and f["v"]["kcal"] and f["v"]["kcal"] >= 40) else None
            entry["density"] = ranked(foods, k, daily, 20, value=dens)
        out["nutrients"][k] = entry
    # Oméga-3 : EPA + DHA (poissons) et ALA (végétal), en g/100 g
    epadha = lambda f: (f["v"]["epa"] + f["v"]["dha"]) if (f["v"]["epa"] is not None and f["v"]["dha"] is not None) else None
    out["nutrients"]["omega-3"] = {
        "unit": "g", "nrv": None,
        "n_known": sum(1 for f in foods if epadha(f) is not None),
        "top": ranked(foods, "epa", daily, 20, value=epadha),
        "ala": ranked(foods, "ala", daily, 15),
        "families": [], "condiments": []}
    path = os.path.join(HERE, "ciqual.json")
    json.dump(out, open(path, "w", encoding="utf-8"), ensure_ascii=False, indent=1, sort_keys=True)
    print("OK — %d aliments, %d nutriments → %s" % (len(foods), len(out["nutrients"]), os.path.relpath(path)))


if __name__ == "__main__":
    if "--fetch" in sys.argv or not os.path.exists(os.path.join(RAW, XLSX)):
        fetch()
    build()
