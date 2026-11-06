# -*- coding: utf-8 -*-
"""Descarga MinGit portable y lo extrae en _tools/mingit."""
import json
import os
import ssl
import urllib.request
import zipfile

ROOT = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
TOOLS = os.path.join(ROOT, "_tools")
os.makedirs(TOOLS, exist_ok=True)

ctx = ssl.create_default_context()
UA = {"User-Agent": "Mozilla/5.0"}

api = "https://api.github.com/repos/git-for-windows/git/releases/latest"
req = urllib.request.Request(api, headers=UA)
with urllib.request.urlopen(req, timeout=60, context=ctx) as r:
    data = json.load(r)

asset = None
for a in data.get("assets", []):
    n = a["name"]
    if n.startswith("MinGit") and "64-bit" in n and n.endswith(".zip") and "busybox" not in n:
        asset = a
        break

if not asset:
    raise SystemExit("No se encontro MinGit en el release")

print("Asset:", asset["name"], asset["size"] // 1024 // 1024, "MB")
zip_path = os.path.join(TOOLS, "mingit.zip")
req = urllib.request.Request(asset["browser_download_url"], headers=UA)
with urllib.request.urlopen(req, timeout=600, context=ctx) as r, open(zip_path, "wb") as f:
    while True:
        chunk = r.read(1024 * 256)
        if not chunk:
            break
        f.write(chunk)

dest = os.path.join(TOOLS, "mingit")
if os.path.exists(dest):
    import shutil
    shutil.rmtree(dest)
os.makedirs(dest, exist_ok=True)
with zipfile.ZipFile(zip_path) as z:
    z.extractall(dest)
os.remove(zip_path)

for candidate in ("cmd/git.exe", "mingw64/bin/git.exe", "bin/git.exe"):
    p = os.path.join(dest, candidate.replace("/", os.sep))
    if os.path.exists(p):
        print("GIT:", p)
        break
else:
    print("GIT no encontrado; contenido:", os.listdir(dest))
