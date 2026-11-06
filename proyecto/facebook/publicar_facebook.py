#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Publica o programa posts (con o sin foto) en una página de Facebook.

Uso:
    python publicar_facebook.py --file posts_campana.json --dry-run
    python publicar_facebook.py --file posts_campana.json

Lee FB_TOKEN y FB_PAGE_ID del entorno o del registro de usuario
(las guarda configurar_credenciales.ps1).

Formato del JSON:
[
  {"message": "...", "link": "...", "image": "ruta/a/foto.jpg",
   "scheduled_iso": "2026-10-25T10:00:00-03:00"}
]
"""
import os
import sys
import json
import time
import argparse
import datetime
import urllib.parse
import urllib.request

GRAPH = "https://graph.facebook.com/v21.0"


def env(name):
    v = os.environ.get(name)
    if v:
        return v
    try:
        import winreg
        with winreg.OpenKey(winreg.HKEY_CURRENT_USER, "Environment") as k:
            return winreg.QueryValueEx(k, name)[0]
    except Exception:
        return None


def _ts(cuando):
    dt = datetime.datetime.fromisoformat(cuando)
    return str(int(dt.timestamp()))


def publicar_texto(page_id, token, params):
    params = dict(params)
    params["access_token"] = token
    data = urllib.parse.urlencode(params).encode("utf-8")
    req = urllib.request.Request(f"{GRAPH}/{page_id}/feed", data=data, method="POST")
    with urllib.request.urlopen(req, timeout=60) as r:
        return json.loads(r.read().decode("utf-8"))


def publicar_foto(page_id, token, image_path, caption, cuando=None):
    boundary = "----FrigZone" + str(int(time.time() * 1000))
    fields = {"caption": caption, "access_token": token}
    if cuando:
        fields["published"] = "false"
        fields["scheduled_publish_time"] = _ts(cuando)

    body = b""
    for k, v in fields.items():
        body += (f"--{boundary}\r\nContent-Disposition: form-data; name=\"{k}\"\r\n\r\n{v}\r\n").encode("utf-8")

    with open(image_path, "rb") as f:
        img = f.read()

    body += (f"--{boundary}\r\nContent-Disposition: form-data; name=\"source\"; "
             f"filename=\"{os.path.basename(image_path)}\"\r\nContent-Type: image/jpeg\r\n\r\n").encode("utf-8")
    body += img + b"\r\n"
    body += (f"--{boundary}--\r\n").encode("utf-8")

    req = urllib.request.Request(f"{GRAPH}/{page_id}/photos", data=body, method="POST")
    req.add_header("Content-Type", f"multipart/form-data; boundary={boundary}")
    with urllib.request.urlopen(req, timeout=180) as r:
        return json.loads(r.read().decode("utf-8"))


def main():
    ap = argparse.ArgumentParser(description="Publica posts en una página de Facebook")
    ap.add_argument("--file", required=True, help="JSON con la lista de publicaciones")
    ap.add_argument("--dry-run", action="store_true", help="Muestra sin publicar")
    args = ap.parse_args()

    if not os.path.exists(args.file):
        sys.exit(f"No existe el archivo: {args.file}")

    with open(args.file, encoding="utf-8") as f:
        posts = json.load(f)

    if not isinstance(posts, list) or not posts:
        sys.exit("El JSON debe ser una lista con al menos una publicación")

    base = os.path.dirname(os.path.abspath(args.file))
    token = env("FB_TOKEN")
    page_id = env("FB_PAGE_ID")

    if not args.dry_run and (not token or not page_id):
        sys.exit("Faltan FB_PAGE_ID y/o FB_TOKEN. Ejecutá configurar_credenciales.ps1.")

    for i, p in enumerate(posts, 1):
        msg = (p.get("message") or "").strip()
        if not msg:
            print(f"[{i}] SALTADO: mensaje vacío")
            continue

        cuando = p.get("scheduled_iso") or None
        img = p.get("image")
        img_path = None
        if img:
            img_path = os.path.normpath(os.path.join(base, img))
            if not os.path.exists(img_path):
                print(f"[{i}] SALTADO: no encuentro la imagen {img_path}")
                continue

        if args.dry_run:
            modo = f"programado {cuando}" if cuando else "inmediato"
            tipo = "FOTO" if img_path else "TEXTO"
            print(f"[{i}] DRY-RUN · {tipo} · {modo} · {len(msg)} caracteres")
            print("     " + msg.split("\n")[0][:90])
            continue

        try:
            if img_path:
                r = publicar_foto(page_id, token, img_path, msg, cuando)
            else:
                params = {"message": msg}
                if p.get("link"):
                    params["link"] = p["link"]
                if cuando:
                    params["published"] = "false"
                    params["scheduled_publish_time"] = _ts(cuando)
                r = publicar_texto(page_id, token, params)
            print(f"[{i}] OK · id={r.get('id') or r.get('post_id')}")
        except Exception as e:
            print(f"[{i}] ERROR · {e}")


if __name__ == "__main__":
    main()
