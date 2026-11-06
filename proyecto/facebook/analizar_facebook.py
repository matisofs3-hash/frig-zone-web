# -*- coding: utf-8 -*-
"""
Analiza una página de Facebook con la Graph API y genera un informe.

Requiere FB_TOKEN (token de página) y FB_PAGE_ID.
Lee las variables del entorno o del registro de usuario de Windows
(las que guarda configurar_credenciales.ps1).

Uso:
    python analizar_facebook.py
    python analizar_facebook.py --dias 30
"""
import os
import sys
import json
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


def get(path, params, token):
    params = dict(params)
    params["access_token"] = token
    url = f"{GRAPH}/{path}?" + urllib.parse.urlencode(params)
    with urllib.request.urlopen(url, timeout=60) as r:
        return json.loads(r.read().decode("utf-8"))


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--dias", type=int, default=30)
    args = ap.parse_args()

    token = env("FB_TOKEN")
    page = env("FB_PAGE_ID")
    if not token or not page:
        sys.exit("Faltan FB_TOKEN y/o FB_PAGE_ID. Ejecutá configurar_credenciales.ps1 primero.")

    print("Consultando página...")
    datos = get(page, {
        "fields": "name,about,fan_count,followers_count,category,link,website,phone,emails,verification_status"
    }, token)

    print("Consultando publicaciones...")
    posts = get(f"{page}/posts", {
        "fields": "message,created_time,permalink_url,shares,reactions.summary(total_count),comments.summary(total_count)",
        "limit": 25,
    }, token).get("data", [])

    hasta = datetime.date.today()
    desde = hasta - datetime.timedelta(days=args.dias)
    print("Consultando métricas...")
    try:
        insights = get(f"{page}/insights", {
            "metric": "page_impressions,page_engaged_users,page_fans",
            "period": "day",
            "since": desde.isoformat(),
            "until": hasta.isoformat(),
        }, token).get("data", [])
    except Exception as e:
        insights = []
        print("  (sin permisos de insights:", e, ")")

    # Análisis simple
    total_reac = sum(int(p.get("reactions", {}).get("summary", {}).get("total_count", 0)) for p in posts)
    total_com = sum(int(p.get("comments", {}).get("summary", {}).get("total_count", 0)) for p in posts)
    total_sh = sum(int(p.get("shares", {}).get("count", 0)) for p in posts)
    mejor = None
    if posts:
        mejor = max(posts, key=lambda p: int(p.get("reactions", {}).get("summary", {}).get("total_count", 0)))

    lineas = []
    lineas.append("# Informe de Facebook — Frig Zone\n")
    lineas.append(f"Generado: {datetime.datetime.now().strftime('%d/%m/%Y %H:%M')}\n")
    lineas.append(f"Período de métricas: últimos {args.dias} días\n")
    lineas.append("\n## Página\n")
    for k in ["name", "category", "fan_count", "followers_count", "phone", "website", "verification_status"]:
        if k in datos:
            lineas.append(f"- **{k}:** {datos[k]}")
    lineas.append("\n## Últimas publicaciones\n")
    lineas.append("| Fecha | Reacciones | Comentarios | Compartidos | Texto |")
    lineas.append("|---|---|---|---|---|")
    for p in posts[:15]:
        txt = (p.get("message") or "").replace("\n", " ")[:70]
        lineas.append(
            f"| {p.get('created_time','')[:10]} | "
            f"{p.get('reactions',{}).get('summary',{}).get('total_count',0)} | "
            f"{p.get('comments',{}).get('summary',{}).get('total_count',0)} | "
            f"{p.get('shares',{}).get('count',0)} | {txt} |"
        )

    lineas.append("\n## Totales\n")
    lineas.append(f"- Reacciones: **{total_reac}**")
    lineas.append(f"- Comentarios: **{total_com}**")
    lineas.append(f"- Compartidos: **{total_sh}**")
    lineas.append(f"- Publicaciones analizadas: **{len(posts)}**")
    if mejor:
        lineas.append(f"\n**Mejor publicación:** {mejor.get('permalink_url','')}")
        lineas.append(f"> {(mejor.get('message') or '')[:200]}")

    lineas.append("\n## Métricas de página\n")
    for m in insights:
        vals = m.get("values", [])
        if vals:
            lineas.append(f"- **{m.get('name')}:** último valor {vals[-1].get('value')}")

    salida = os.path.join(os.path.dirname(os.path.abspath(__file__)), "Informe_Facebook.md")
    with open(salida, "w", encoding="utf-8") as f:
        f.write("\n".join(lineas))

    with open(os.path.join(os.path.dirname(salida), "facebook_datos.json"), "w", encoding="utf-8") as f:
        json.dump({"pagina": datos, "posts": posts, "insights": insights}, f, ensure_ascii=False, indent=2)

    print("OK ·", salida)


if __name__ == "__main__":
    main()
