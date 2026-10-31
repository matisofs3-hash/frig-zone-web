# -*- coding: utf-8 -*-
"""Descarga las imágenes del sitio actual y las convierte a WebP optimizado."""
import os
import urllib.request
import ssl
from PIL import Image

BASE = "https://frigzone.com.ar/data/img/"
OUT = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), "assets", "img")
os.makedirs(OUT, exist_ok=True)

ctx = ssl.create_default_context()
UA = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64)"}

MAP = {
    "camaradefrio2.png": "camara-frio",
    "camaradefrioistalaciontodopais.png": "camara-instalacion",
    "camarasdefrio.png": "camara-productos",
    "equipamientoyrefrigeracion.png": "equipamiento",
    "imagengenerica.png": "infraestructura",
    "refrigeracionindustrial.png": "refrigeracion-industrial",
    "senalescamarafrigorificanosirve.png": "guia-senales",
    "trespilaresdefriocamaras.png": "guia-pilares",
}


def fetch(name):
    req = urllib.request.Request(BASE + name, headers=UA)
    with urllib.request.urlopen(req, timeout=60, context=ctx) as r:
        return r.read()


total_before = 0
total_after = 0
for src, base in MAP.items():
    try:
        raw = fetch(src)
        total_before += len(raw)
        tmp = os.path.join(OUT, "_tmp_" + base + ".png")
        with open(tmp, "wb") as f:
            f.write(raw)
        im = Image.open(tmp).convert("RGB")
        # version grande (1600 px de ancho maximo)
        w, h = im.size
        if w > 1600:
            im = im.resize((1600, int(h * 1600 / w)), Image.LANCZOS)
        big = os.path.join(OUT, base + ".webp")
        im.save(big, "WEBP", quality=78, method=6)
        total_after += os.path.getsize(big)
        # version chica (800 px)
        w2, h2 = im.size
        small = im.resize((800, int(h2 * 800 / w2)), Image.LANCZOS)
        small.save(os.path.join(OUT, base + "-800.webp"), "WEBP", quality=76, method=6)
        print(f"OK {base}.webp  {len(raw)/1024:8.1f} KB -> {os.path.getsize(big)/1024:7.1f} KB")
        os.remove(tmp)
    except Exception as e:
        print("FAIL", src, type(e).__name__, e)

print(f"\nTOTAL: {total_before/1024/1024:.2f} MB -> {total_after/1024/1024:.2f} MB")
