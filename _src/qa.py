# -*- coding: utf-8 -*-
import os
import re
import json
from html.parser import HTMLParser

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
errors = []
warnings = []
pages = []
total_size = 0
imgs = set()

for dirpath, dirnames, files in os.walk(ROOT):
    dirnames[:] = [d for d in dirnames if d not in (".git", "_src", "__pycache__")]
    for f in files:
        p = os.path.join(dirpath, f)
        total_size += os.path.getsize(p)
        if f.endswith(".html"):
            pages.append(p)

href_re = re.compile(r'(?:href|src)="([^"]+)"')
ld_re = re.compile(r'<script type="application/ld\+json">(.*?)</script>', re.S)
title_re = re.compile(r"<title>(.*?)</title>", re.S)
desc_re = re.compile(r'<meta name="description" content="([^"]*)"')

internal_links = 0
for p in pages:
    html = open(p, encoding="utf-8").read()
    base = os.path.dirname(p)
    rel = os.path.relpath(p, ROOT).replace("\\", "/")

    t = title_re.search(html)
    d = desc_re.search(html)
    if not t:
        errors.append(f"{rel}: sin <title>")
    elif len(t.group(1)) > 70:
        warnings.append(f"{rel}: title {len(t.group(1))} chars")
    if not d:
        errors.append(f"{rel}: sin meta description")
    elif len(d.group(1)) > 175:
        warnings.append(f"{rel}: description {len(d.group(1))} chars")

    for block in ld_re.findall(html):
        try:
            json.loads(block)
        except Exception as e:
            errors.append(f"{rel}: JSON-LD invalido: {e}")

    for link in href_re.findall(html):
        if link.startswith(("http", "mailto:", "tel:", "#", "data:")):
            continue
        internal_links += 1
        clean = link.split("#")[0].split("?")[0]
        if not clean:
            continue
        target = os.path.normpath(os.path.join(base, clean))
        if not os.path.exists(target):
            errors.append(f"{rel}: enlace roto -> {link}")
        if clean.endswith((".webp", ".svg", ".png", ".jpg")):
            imgs.add(target)

    stripped = ld_re.sub("", html)
    if "{{" in stripped or "}}" in stripped:
        errors.append(f"{rel}: llaves sin renderizar")

print(f"Paginas: {len(pages)}")
print(f"Enlaces internos verificados: {internal_links}")
print(f"Imagenes referenciadas: {len(imgs)}")
print(f"Peso total del sitio: {total_size/1024/1024:.2f} MB")
print(f"Errores: {len(errors)}")
for e in errors[:30]:
    print("  ERROR", e)
print(f"Advertencias: {len(warnings)}")
for w in warnings[:20]:
    print("  WARN", w)

# marcas en el carrusel
home = open(os.path.join(ROOT, "index.html"), encoding="utf-8").read()
print("Tarjetas de marca en home:", home.count('class="brand '))
