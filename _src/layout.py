# -*- coding: utf-8 -*-
"""Layout, iconos y componentes HTML del sitio."""
import html
from data import MARCAS, SERVICIOS, ZONAS, OBRAS, RESENAS, FAQ, GUIAS, WA, WA_TEXT, TEL, EMAIL, SITE

ICONS = {
    "check": '<path d="M20 6 9 17l-5-5"/>',
    "arrow": '<path d="M5 12h14"/><path d="m12 5 7 7-7 7"/>',
    "left": '<path d="m15 18-6-6 6-6"/>',
    "right": '<path d="m9 18 6-6-6-6"/>',
    "phone": '<path d="M22 16.92v3a2 2 0 0 1-2.18 2 19.79 19.79 0 0 1-8.63-3.07 19.5 19.5 0 0 1-6-6 19.79 19.79 0 0 1-3.07-8.67A2 2 0 0 1 4.11 2h3a2 2 0 0 1 2 1.72 12.84 12.84 0 0 0 .7 2.81 2 2 0 0 1-.45 2.11L8.09 9.91a16 16 0 0 0 6 6l1.27-1.27a2 2 0 0 1 2.11-.45 12.84 12.84 0 0 0 2.81.7A2 2 0 0 1 22 16.92z"/>',
    "pin": '<path d="M20 10c0 6-8 12-8 12s-8-6-8-12a8 8 0 0 1 16 0Z"/><circle cx="12" cy="10" r="3"/>',
    "clock": '<circle cx="12" cy="12" r="10"/><polyline points="12 6 12 12 16 14"/>',
    "shield": '<path d="M20 13c0 5-3.5 7.5-7.66 8.95a1 1 0 0 1-.67-.01C7.5 20.5 4 18 4 13V6a1 1 0 0 1 1-1c2 0 4.5-1.2 6.24-2.72a1.17 1.17 0 0 1 1.52 0C14.51 3.81 17 5 19 5a1 1 0 0 1 1 1z"/>',
    "wrench": '<path d="M14.7 6.3a1 1 0 0 0 0 1.4l1.6 1.6a1 1 0 0 0 1.4 0l3.77-3.77a6 6 0 0 1-7.94 7.94l-6.91 6.91a2.12 2.12 0 0 1-3-3l6.91-6.91a6 6 0 0 1 7.94-7.94l-3.76 3.76z"/>',
    "snow": '<line x1="2" x2="22" y1="12" y2="12"/><line x1="12" x2="12" y1="2" y2="22"/><path d="m20 16-4-4 4-4"/><path d="m4 8 4 4-4 4"/><path d="m16 4-4 4-4-4"/><path d="m8 20 4-4 4 4"/>',
    "wind": '<path d="M17.7 7.7a2.5 2.5 0 1 1 1.8 4.3H2"/><path d="M9.6 4.6A2 2 0 1 1 11 8H2"/><path d="M12.6 19.4A2 2 0 1 0 14 16H2"/>',
    "therm": '<path d="M14 4v10.54a4 4 0 1 1-4 0V4a2 2 0 0 1 4 0Z"/>',
    "building": '<rect width="16" height="20" x="4" y="2" rx="2"/><path d="M9 22v-4h6v4"/><path d="M8 6h.01M16 6h.01M12 6h.01M12 10h.01M12 14h.01M16 10h.01M16 14h.01M8 10h.01M8 14h.01"/>',
    "droplet": '<path d="M12 22a7 7 0 0 0 7-7c0-2-1-3.9-3-5.5s-3.5-4-4-6.5c-.5 2.5-2 4.9-4 6.5C6 11.1 5 13 5 15a7 7 0 0 0 7 7z"/>',
    "box": '<path d="m7.5 4.27 9 5.15"/><path d="M21 8a2 2 0 0 0-1-1.73l-7-4a2 2 0 0 0-2 0l-7 4A2 2 0 0 0 3 8v8a2 2 0 0 0 1 1.73l7 4a2 2 0 0 0 2 0l7-4A2 2 0 0 0 21 16Z"/><path d="m3.3 7 8.7 5 8.7-5"/><path d="M12 22V12"/>',
    "star": '<polygon points="12 2 15.09 8.26 22 9.27 17 14.14 18.18 21.02 12 17.77 5.82 21.02 7 14.14 2 9.27 8.91 8.26 12 2"/>',
    "wa": '<path fill="currentColor" stroke="none" d="M17.5 14.4c-.3-.2-1.7-.8-2-.9-.3-.1-.5-.2-.7.1-.2.3-.7.9-.9 1.1-.2.2-.3.2-.6.1-1.7-.8-2.8-1.5-3.9-3.3-.3-.5.3-.5.8-1.5.1-.2 0-.4 0-.5-.1-.2-.7-1.6-.9-2.2-.2-.6-.5-.5-.7-.5h-.6c-.2 0-.5.1-.8.4-.3.3-1 1-1 2.4s1 2.8 1.2 3c.1.2 2 3.1 4.9 4.3 1.8.8 2.5.8 3.4.7.5-.1 1.7-.7 1.9-1.3.2-.7.2-1.2.2-1.3 0-.1-.2-.2-.4-.3zM12 2a10 10 0 0 0-8.6 15L2 22l5.2-1.4A10 10 0 1 0 12 2z"/>',
    "ig": '<rect width="20" height="20" x="2" y="2" rx="5"/><path d="M16 11.37A4 4 0 1 1 12.63 8 4 4 0 0 1 16 11.37z"/><line x1="17.5" x2="17.51" y1="6.5" y2="6.5"/>',
    "fb": '<path d="M18 2h-3a5 5 0 0 0-5 5v3H7v4h3v8h4v-8h3l1-4h-4V7a1 1 0 0 1 1-1h3z"/>',
    "tiktok": '<path d="M16 8.2a6.5 6.5 0 0 0 4 1.4V6.5a3.5 3.5 0 0 1-3.5-3.5H13v11.5a2.5 2.5 0 1 1-2.5-2.5c.2 0 .3 0 .5.1V8.5A6.5 6.5 0 1 0 16 8.2z"/>',
    "mail": '<rect width="20" height="16" x="2" y="4" rx="2"/><path d="m22 7-8.97 5.7a1.94 1.94 0 0 1-2.06 0L2 7"/>',
    "menu": '<line x1="4" x2="20" y1="6" y2="6"/><line x1="4" x2="20" y1="12" y2="12"/><line x1="4" x2="20" y1="18" y2="18"/>',
    "info": '<circle cx="12" cy="12" r="10"/><path d="M12 16v-4"/><path d="M12 8h.01"/>',
    "spark": '<path d="m12 3-1.9 5.8a2 2 0 0 1-1.3 1.3L3 12l5.8 1.9a2 2 0 0 1 1.3 1.3L12 21l1.9-5.8a2 2 0 0 1 1.3-1.3L21 12l-5.8-1.9a2 2 0 0 1-1.3-1.3z"/>',
}


def icon(name, cls=""):
    body = ICONS.get(name, ICONS["info"])
    c = f' class="{cls}"' if cls else ""
    return (f'<svg{c} viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8" '
            f'stroke-linecap="round" stroke-linejoin="round" aria-hidden="true">{body}</svg>')


def u(path, depth):
    return ("../" * depth) + path


def wa(text="Hola Frig Zone, necesito una consulta técnica"):
    from urllib.parse import quote
    return f"https://wa.me/{WA}?text={quote(text)}"


def nav_items(depth):
    return [
        ("Inicio", u("index.html", depth)),
        ("Servicios", u("servicios/index.html", depth)),
        ("Zonas", u("zonas/index.html", depth)),
        ("Obras", u("obras.html", depth)),
        ("Precios", u("precios.html", depth)),
        ("Guías", u("guias/index.html", depth)),
        ("Nosotros", u("sobre-nosotros.html", depth)),
        ("Contacto", u("contacto.html", depth)),
    ]


def _nav_link(label, href, active):
    cur = ' aria-current="page"' if label == active else ""
    return f'<a href="{href}"{cur}>{label}</a>'


def header(depth, active=""):
    links = "".join(_nav_link(label, href, active) for label, href in nav_items(depth))
    mobile = "".join(
        f'<a href="{href}">{label}</a>' for label, href in nav_items(depth)
    )
    return f'''
<div class="topbar">
  <div class="wrap">
    <ul class="topbar-list">
      <li>{icon("pin")}<span>CABA y alrededores</span></li>
      <li>{icon("shield")}<span>Garantía escrita</span></li>
      <li>{icon("clock")}<span>Respuesta en el día</span></li>
    </ul>
    <a href="{wa()}" target="_blank" rel="noopener">{TEL}</a>
  </div>
</div>
<header class="site-header">
  <div class="wrap">
    <a class="logo" href="{u("index.html", depth)}" aria-label="Frig Zone, inicio">
      <img src="{u("assets/img/snowflake.svg", depth)}" alt="" width="34" height="34">
      <span class="logo-text">FRIG<span>ZONE</span><span class="logo-sub">REFRIGERACIÓN · CABA</span></span>
    </a>
    <nav class="nav" aria-label="Principal">{links}</nav>
    <div class="header-cta">
      <a class="btn btn-primary btn-sm" href="{wa()}" target="_blank" rel="noopener">{icon("wa")}Pedir visita</a>
      <button class="burger" type="button" aria-expanded="false" aria-controls="mobileNav" aria-label="Abrir menú">{icon("menu")}</button>
    </div>
  </div>
  <nav class="mobile-nav" id="mobileNav" aria-label="Menú móvil">
    {mobile}
    <a class="btn btn-primary" href="{wa()}" target="_blank" rel="noopener">{icon("wa")}Pedir visita por WhatsApp</a>
  </nav>
</header>'''


def footer(depth):
    return f'''
<footer class="site-footer">
  <div class="wrap">
    <div class="footer-grid">
      <div class="footer-brand">
        <a class="logo" href="{u("index.html", depth)}">
          <img src="{u("assets/img/snowflake.svg", depth)}" alt="" width="30" height="30">
          <span class="logo-text" style="font-size:17px">FRIG<span>ZONE</span></span>
        </a>
        <p>Servicio técnico de refrigeración y climatización en CABA. Instalación, reparación y mantenimiento con garantía escrita.</p>
        <div class="socials">
          <a href="https://www.instagram.com/frig.zone" target="_blank" rel="noopener" aria-label="Instagram">{icon("ig")}</a>
          <a href="https://www.facebook.com/frigzone.caba" target="_blank" rel="noopener" aria-label="Facebook">{icon("fb")}</a>
          <a href="https://www.tiktok.com/@refrigeracionfrigzone" target="_blank" rel="noopener" aria-label="TikTok">{icon("tiktok")}</a>
          <a href="{wa()}" target="_blank" rel="noopener" aria-label="WhatsApp">{icon("wa")}</a>
        </div>
      </div>
      <div>
        <h3>Servicios</h3>
        <ul>
          {''.join(f'<li><a href="{u("servicios/" + s["slug"] + ".html", depth)}">{s["nombre"]}</a></li>' for s in SERVICIOS)}
        </ul>
      </div>
      <div>
        <h3>Zonas</h3>
        <ul>
          {''.join(f'<li><a href="{u("zonas/" + z[0] + ".html", depth)}">{z[1]}</a></li>' for z in ZONAS)}
          <li><a href="{u("zonas/index.html", depth)}">Ver todas</a></li>
        </ul>
      </div>
      <div>
        <h3>Contacto</h3>
        <ul>
          <li><a href="{wa()}" target="_blank" rel="noopener">{TEL}</a></li>
          <li><a href="mailto:{EMAIL}">{EMAIL}</a></li>
          <li>Lun a Vie · 9 a 18 h</li>
          <li>Sáb · 9 a 13 h</li>
          <li>CUIT [completar]</li>
        </ul>
      </div>
    </div>
    <div class="footer-bottom">
      <span>© <span data-year>2026</span> Frig Zone. Todos los derechos reservados.</span>
      <span><a href="{u("privacidad.html", depth)}">Política de privacidad</a> · <a href="{u("links.html", depth)}">Links</a></span>
    </div>
  </div>
</footer>
<a class="float-wa" href="{wa()}" target="_blank" rel="noopener" aria-label="Escribinos por WhatsApp">{icon("wa")}</a>
<script src="{u("assets/js/main.js", depth)}" defer></script>'''


def local_business_ld():
    return '''{
  "@context": "https://schema.org",
  "@type": "LocalBusiness",
  "@id": "https://frigzone.com.ar/#business",
  "name": "Frig Zone — Refrigeración y Climatización",
  "url": "https://frigzone.com.ar",
  "telephone": "+5491173719821",
  "email": "contacto@frigzone.com.ar",
  "priceRange": "$$",
  "image": "https://frigzone.com.ar/assets/img/camara-frio.webp",
  "description": "Instalación, reparación y mantenimiento de aires acondicionados, heladeras comerciales y cámaras frigoríficas en CABA.",
  "address": {"@type": "PostalAddress", "addressLocality": "Ciudad Autónoma de Buenos Aires", "addressRegion": "CABA", "addressCountry": "AR"},
  "areaServed": ["Ciudad Autónoma de Buenos Aires", "Palermo", "Belgrano", "Caballito", "Almagro", "Villa Urquiza", "Recoleta"],
  "openingHoursSpecification": [{"@type": "OpeningHoursSpecification", "dayOfWeek": ["Monday","Tuesday","Wednesday","Thursday","Friday"], "opens": "09:00", "closes": "18:00"}],
  "sameAs": ["https://www.instagram.com/frig.zone", "https://www.tiktok.com/@refrigeracionfrigzone", "https://www.facebook.com/frigzone.caba"]
}'''


def page(path, depth, title, desc, body, active="", extra_ld="", og_image="assets/img/camara-frio.webp", noindex=False):
    clean = path[:-len("index.html")] if path.endswith("index.html") else path
    canonical = SITE + "/" + clean
    robots = '<meta name="robots" content="noindex, follow">' if noindex else '<meta name="robots" content="index, follow">'
    ld = local_business_ld()
    extra = f'<script type="application/ld+json">{extra_ld}</script>' if extra_ld else ""
    return f'''<!DOCTYPE html>
<html lang="es-AR">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>{html.escape(title)}</title>
<meta name="description" content="{html.escape(desc)}">
<link rel="canonical" href="{canonical}">
{robots}
<meta property="og:type" content="website">
<meta property="og:site_name" content="Frig Zone">
<meta property="og:locale" content="es_AR">
<meta property="og:title" content="{html.escape(title)}">
<meta property="og:description" content="{html.escape(desc)}">
<meta property="og:url" content="{canonical}">
<meta property="og:image" content="{SITE}/{og_image}">
<meta property="og:image:width" content="1200">
<meta property="og:image:height" content="630">
<meta name="twitter:card" content="summary_large_image">
<meta name="theme-color" content="#060c16">
<link rel="icon" type="image/svg+xml" href="{u("assets/img/snowflake.svg", depth)}">
<link rel="preload" as="image" href="{u("assets/img/camara-frio.webp", depth)}" fetchpriority="high">
<link rel="stylesheet" href="{u("assets/css/styles.css", depth)}">
<script type="application/ld+json">{ld}</script>
{extra}
</head>
<body>
<a class="skip" href="#contenido">Saltar al contenido</a>
{header(depth, active)}
<main id="contenido">
{body}
</main>
{footer(depth)}
</body>
</html>
'''


def brands_carousel():
    cards = "".join(
        f'<div class="brand {cls}" title="{html.escape(rubro)}"><span>{html.escape(nombre)}</span></div>'
        for nombre, cls, rubro in MARCAS
    )
    return f'''
<section class="section brands-section" id="marcas" aria-labelledby="marcas-title">
  <div class="wrap">
    <div class="brands-head">
      <div>
        <div class="eyebrow">Marcas que trabajamos</div>
        <h2 id="marcas-title">Equipos de las principales marcas del mercado</h2>
        <p>Trabajamos con equipos residenciales, comerciales e industriales. Si tu marca no aparece, escribinos: la mayoría de las veces también la atendemos.</p>
      </div>
      <div class="brands-controls">
        <button class="brand-btn" type="button" data-brands-prev aria-label="Ver marcas anteriores">{icon("left")}</button>
        <button class="brand-btn" type="button" data-brands-next aria-label="Ver más marcas">{icon("right")}</button>
      </div>
    </div>
    <div class="brands-viewport">
      <div class="brands-track" id="brandsTrack" tabindex="0" aria-label="Carrusel de marcas">
        {cards}
      </div>
    </div>
    <p class="brand-note">Logotipos tipográficos de referencia. Las marcas pertenecen a sus respectivos titulares; no implica servicio oficial.</p>
  </div>
</section>'''


def services_section(depth):
    cards = ""
    for s in SERVICIOS:
        lis = "".join(f"<li>{html.escape(b)}</li>" for b in s["bullets"][:3])
        cards += f'''
<article class="card reveal">
  <div class="icon">{icon(s["icon"])}</div>
  <h3>{html.escape(s["nombre"])}</h3>
  <p>{html.escape(s["corto"])}</p>
  <ul>{lis}</ul>
  <a class="card-link" href="{u("servicios/" + s["slug"] + ".html", depth)}">Ver servicio {icon("arrow")}</a>
</article>'''
    return f'''
<section class="section section-alt" id="servicios">
  <div class="wrap">
    <div class="section-head">
      <div class="eyebrow">Servicios</div>
      <h2>Todo el frío de tu casa o comercio, en un solo lugar</h2>
      <p>Desde la instalación de un split hasta una cámara frigorífica completa. Trabajamos con instrumental y garantía escrita.</p>
    </div>
    <div class="grid-3">{cards}</div>
  </div>
</section>'''


def works_section(depth, limit=3):
    items = ""
    for img, tag, titulo, desc in OBRAS[:limit]:
        items += f'''
<a class="work reveal" href="{u("obras.html", depth)}">
  <img src="{u("assets/img/" + img + ".webp", depth)}" srcset="{u("assets/img/" + img + "-800.webp", depth)} 800w, {u("assets/img/" + img + ".webp", depth)} 1600w" sizes="(max-width: 640px) 100vw, (max-width: 1024px) 50vw, 33vw" alt="{html.escape(titulo)}" loading="lazy" width="800" height="600">
  <div class="overlay">
    <span class="tag">{html.escape(tag)}</span>
    <h3>{html.escape(titulo)}</h3>
    <p>{html.escape(desc)}</p>
  </div>
</a>'''
    return f'''
<section class="section" id="obras">
  <div class="wrap">
    <div class="section-head">
      <div class="eyebrow">Obras reales</div>
      <h2>Lo que hacemos, sin fotos de stock</h2>
      <p>Casos de instalación, montaje y mantenimiento en CABA. Cada obra con su barrio, su problema y su solución.</p>
    </div>
    <div class="works">{items}</div>
  </div>
</section>'''


def zones_section(depth):
    chips = "".join(
        f'<a class="zone" href="{u("zonas/" + slug + ".html", depth)}">{icon("pin")}{nombre}</a>'
        for slug, nombre, _ in ZONAS
    )
    return f'''
<section class="section section-alt" id="zonas">
  <div class="wrap">
    <div class="section-head">
      <div class="eyebrow">Zona de cobertura</div>
      <h2>Atendemos en CABA y alrededores</h2>
      <p>Estas son las zonas con cobertura habitual. Si estás cerca, escribinos igual: coordinamos según disponibilidad.</p>
    </div>
    <div class="zones">
      {chips}
      <a class="zone" href="{u("zonas/index.html", depth)}">{icon("arrow")}Ver todas las zonas</a>
    </div>
  </div>
</section>'''


def reviews_section():
    cards = ""
    for nombre, servicio, texto in RESENAS:
        cards += f'''
<article class="review reveal">
  <div class="stars" aria-label="5 de 5 estrellas">★★★★★</div>
  <p>“{html.escape(texto)}”</p>
  <footer><strong>{html.escape(nombre)}</strong>{html.escape(servicio)}</footer>
</article>'''
    return f'''
<section class="section" id="resenas">
  <div class="wrap">
    <div class="section-head">
      <div class="eyebrow">Reseñas</div>
      <h2>Lo que dicen los clientes</h2>
      <p>Reseñas de ejemplo. En producción se conectan las reseñas reales de Google Business Profile.</p>
    </div>
    <div class="grid-3">{cards}</div>
  </div>
</section>'''


def faq_section():
    items = "".join(
        f'<details><summary>{html.escape(q)}</summary><div class="answer">{html.escape(a)}</div></details>'
        for q, a in FAQ
    )
    return f'''
<section class="section section-alt" id="faq">
  <div class="wrap">
    <div class="section-head" style="text-align:center;margin-inline:auto">
      <div class="eyebrow">Preguntas frecuentes</div>
      <h2>Dudas comunes antes de contratar</h2>
    </div>
    <div class="faq">{items}</div>
  </div>
</section>'''


def cta_band(depth):
    return f'''
<section class="cta-band">
  <div class="wrap">
    <div>
      <h2>¿Te quedaste sin frío?</h2>
      <p>Contanos qué equipo es y en qué barrio estás. Te respondemos con un diagnóstico y un turno.</p>
    </div>
    <div class="hero-actions" style="margin:0">
      <a class="btn btn-primary" href="{wa()}" target="_blank" rel="noopener">{icon("wa")}Escribir por WhatsApp</a>
      <a class="btn btn-ghost" href="tel:+5491173719821">{icon("phone")}Llamar</a>
    </div>
  </div>
</section>'''


def breadcrumbs(depth, items):
    parts = []
    for i, (label, href) in enumerate(items):
        if i:
            parts.append('<span aria-hidden="true">/</span>')
        if href:
            parts.append(f'<a href="{u(href, depth)}">{html.escape(label)}</a>')
        else:
            parts.append(f'<span>{html.escape(label)}</span>')
    return '<nav class="breadcrumbs" aria-label="Miga de pan">' + "".join(parts) + "</nav>"


def brand_list_jsonld():
    return ""
