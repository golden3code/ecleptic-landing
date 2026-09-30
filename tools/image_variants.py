#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Versions allégées des photos d'articles (srcset du héros et vignettes du Journal).

    python3 tools/image_variants.py

Pour chaque assets/articles/<slug>.jpg (1600x840), écrit s'ils manquent :
    assets/articles/640/<slug>.jpg   (vignettes, petits écrans)
    assets/articles/1200/<slug>.jpg  (héros sur iPhone et écrans retina)
Le générateur (build_articles.py) ne référence une version que si le fichier
existe : une nouvelle photo sans variantes sort quand même, en 1600 seul.
À relancer après chaque dépôt de nouvelles photos, puis commiter.
Nécessite Pillow (installé en local, pas sur le cron GitHub).
"""
import os, sys
from PIL import Image

WIDTHS = (640, 1200)
QUALITY = 78

root = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
adir = os.path.join(root, "assets", "articles")
force = "--force" in sys.argv
made = 0
for fn in sorted(os.listdir(adir)):
    if not fn.endswith(".jpg"):
        continue
    src = os.path.join(adir, fn)
    im = None
    for w in WIDTHS:
        out_dir = os.path.join(adir, str(w))
        out = os.path.join(out_dir, fn)
        if os.path.exists(out) and not force:
            continue
        if im is None:
            im = Image.open(src).convert("RGB")
        os.makedirs(out_dir, exist_ok=True)
        h = round(im.height * w / im.width)
        im.resize((w, h), Image.LANCZOS).save(out, "JPEG", quality=QUALITY, optimize=True, progressive=True)
        made += 1
print("OK — %d variantes écrites" % made)
