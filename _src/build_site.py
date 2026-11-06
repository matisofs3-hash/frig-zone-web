# -*- coding: utf-8 -*-
"""Genera el sitio estático de Frig Zone en /frigzone-web."""
import os
import sys
import json
import html

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

from data import (SERVICIOS, ZONAS, OBRAS, GUIAS, FAQ, MARCAS, WA, TEL, EMAIL, SITE)
from layout import (page, icon, u, wa, brands_carousel, services_section,
                    works_section, zones_section, reviews_section, faq_section,
                    cta_band, breadcrumbs, local_business_ld)

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
WRITTEN = []


def write(path, content):
    full = os.path.join(ROOT, path.replace("/", os.sep))
    os.makedirs(os.path.dirname(full), exist_ok=True)
    with open(full, "w", encoding="utf-8", newline="\n") as f:
        f.write(content)
    WRITTEN.append(path)


# ---------------------------------------------------------------- HOME
def hero_home():
    return f'''
<section class="hero">
  <div class="wrap">
    <div>
      <span class="badge"><span class="dot"></span>Servicio técnico especializado · CABA</span>
      <h1>Refrigeración y climatización en CABA, <em>sin atajos</em>.</h1>
      <p class="lead">Instalación, service y mantenimiento de aires acondicionados, heladeras comerciales y cámaras frigoríficas. Vacío medido con vacuómetro, presurización con nitrógeno y garantía escrita.</p>
      <div class="hero-actions">
        <a class="btn btn-primary" href="{wa()}" target="_blank" rel="noopener">{icon("wa")}Pedir visita por WhatsApp</a>
        <a class="btn btn-ghost" href="#diagnostico">{icon("spark")}Diagnóstico en 3 pasos</a>
      </div>
      <div class="hero-proof">
        <div><strong>-25 °C</strong><span>Cámaras de congelado</span></div>
        <div><strong>&lt; 500</strong><span>Micrones de vacío</span></div>
        <div><strong>A/B</strong><span>Factura para comercios</span></div>
        <div><strong>CABA</strong><span>Cobertura y alrededores</span></div>
      </div>
    </div>
    <div class="hero-media">
      <div class="frame">
        <img src="assets/img/camara-frio.webp" srcset="assets/img/camara-frio-800.webp 800w, assets/img/camara-frio.webp 1600w" sizes="(max-width: 1024px) 100vw, 46vw" alt="Cámara frigorífica instalada por Frig Zone" width="1200" height="900" fetchpriority="high">
        <span class="hero-chip">{icon("therm")}-25 °C a +10 °C</span>
        <div class="caption">
          <div>
            <strong>Cámara de frío a medida</strong>
            <small>Paneles de alta densidad · Caballito</small>
          </div>
        </div>
      </div>
    </div>
  </div>
</section>'''


def trust_bar():
    items = [
        ("shield", "Garantía escrita", "En mano de obra"),
        ("check", "Factura A y B", "Particulares y comercios"),
        ("check", "Efectivo, transferencia o MP", "Formas de pago flexibles"),
        ("clock", "Respuesta en el día", "Según disponibilidad"),
    ]
    out = ""
    for ic, t, s in items:
        out += f'<div class="trust-item">{icon(ic)}<div><strong>{t}</strong><span>{s}</span></div></div>'
    return f'<section class="trust"><div class="wrap">{out}</div></section>'


def diag_section():
    return f'''
<section class="section" id="diagnostico">
  <div class="wrap">
    <div class="diag">
      <div>
        <div class="eyebrow">Pre-diagnóstico</div>
        <h2 style="font-size:clamp(27px,3vw,38px);letter-spacing:-.02em">Contanos qué pasa y te orientamos</h2>
        <p style="color:var(--muted);margin-top:12px">No hace falta que sepas el nombre de la falla. Con tres datos podemos decirte si es algo simple o si conviene una visita.</p>
        <div class="diag-steps">
          <div class="diag-step"><div class="n">1</div><div><strong>Elegí el equipo</strong><span>Split, inverter, heladera, cámara o multisplit.</span></div></div>
          <div class="diag-step"><div class="n">2</div><div><strong>Contá el síntoma</strong><span>No enfría, gotea, hace ruido, no arranca.</span></div></div>
          <div class="diag-step"><div class="n">3</div><div><strong>Decinos tu zona</strong><span>Barrio de CABA o alrededores.</span></div></div>
        </div>
      </div>
      <form class="form-panel" data-wa-form>
        <h3>Pre-diagnóstico técnico</h3>
        <p class="hint">Te respondemos por WhatsApp. Sin compromiso.</p>
        <div class="field-row">
          <div class="field">
            <label for="equipo">Tipo de equipo</label>
            <select id="equipo" name="equipo" data-label="Equipo" required>
              <option value="">Elegir</option>
              <option>Aire split</option>
              <option>Sistema inverter</option>
              <option>Multisplit / piso techo / cassette</option>
              <option>Heladera comercial</option>
              <option>Cámara frigorífica</option>
            </select>
          </div>
          <div class="field">
            <label for="servicio">Servicio</label>
            <select id="servicio" name="servicio" data-label="Servicio" required>
              <option value="">Elegir</option>
              <option>Reparación / falla</option>
              <option>Instalación nueva</option>
              <option>Mantenimiento / limpieza</option>
              <option>Carga de gas</option>
              <option>Desinstalación / mudanza</option>
            </select>
          </div>
        </div>
        <div class="field">
          <label for="zona">Barrio o zona</label>
          <input id="zona" name="zona" data-label="Zona" placeholder="Ej: Palermo" required>
        </div>
        <div class="field">
          <label for="sintoma">Síntoma o detalle</label>
          <textarea id="sintoma" name="sintoma" data-label="Síntoma" rows="3" placeholder="Ej: prende pero no enfría, gotea agua"></textarea>
        </div>
        <button class="btn btn-primary btn-block" type="submit">{icon("wa")}Enviar diagnóstico por WhatsApp</button>
        <p class="form-msg" role="status"></p>
      </form>
    </div>
  </div>
</section>'''


def guides_home():
    cards = ""
    for g in GUIAS:
        cards += f'''
<a class="guide reveal" href="guias/{g["slug"]}.html">
  <img src="assets/img/{g["img"]}.webp" alt="{html.escape(g["titulo"])}" loading="lazy" width="192" height="152">
  <div><h3>{html.escape(g["titulo"])}</h3><span>Leer guía</span></div>
</a>'''
    return f'''
<section class="section" id="guias">
  <div class="wrap">
    <div class="section-head">
      <div class="eyebrow">Guías técnicas</div>
      <h2>Información útil antes de llamar a un técnico</h2>
      <p>Explicaciones cortas, sin vueltas, para que sepas qué está pasando y qué esperar.</p>
    </div>
    <div class="grid-3">{cards}</div>
  </div>
</section>'''


def about_home():
    return f'''
<section class="section section-alt" id="nosotros">
  <div class="wrap">
    <div class="about">
      <div class="about-media">
        <img src="assets/img/camara-instalacion.webp" alt="Instalación de cámara frigorífica en obra" loading="lazy" width="800" height="880">
        <div class="badge-card">
          <div class="avatar">M</div>
          <div><strong>Mati · Técnico en refrigeración</strong><span>Instalaciones y service en CABA</span></div>
        </div>
      </div>
      <div>
        <div class="eyebrow">Quién está detrás</div>
        <h2 style="font-size:clamp(27px,3vw,38px);letter-spacing:-.02em">Un técnico, no un call center</h2>
        <p style="color:var(--muted);margin-top:12px">Atiendo personalmente cada trabajo. Eso significa que quien te responde por WhatsApp es la misma persona que después va a tu casa o comercio.</p>
        <ul class="about-list">
          <li>{icon("check")}<span>Trabajo con instrumental: vacuómetro digital, bomba de dos etapas y balanza de gas.</span></li>
          <li>{icon("check")}<span>Garantía escrita y factura. Sin sorpresas después del trabajo.</span></li>
          <li>{icon("check")}<span>Explico qué se hace y por qué, antes de tocar el equipo.</span></li>
        </ul>
        <div class="hero-actions" style="margin-top:26px">
          <a class="btn btn-primary" href="sobre-nosotros.html">Conocer más</a>
        </div>
      </div>
    </div>
  </div>
</section>'''


def home():
    body = (hero_home() + trust_bar() + services_section(0) + diag_section() +
            works_section(0) + brands_carousel() + zones_section(0) +
            reviews_section() + about_home() + guides_home() + faq_section() + cta_band(0))
    faq_ld = {
        "@context": "https://schema.org",
        "@type": "FAQPage",
        "mainEntity": [{"@type": "Question", "name": q,
                        "acceptedAnswer": {"@type": "Answer", "text": a}} for q, a in FAQ],
    }
    write("index.html", page(
        "index.html", 0,
        "Refrigeración y Climatización en CABA | Frig Zone",
        "Instalación, service y cámaras de frío en CABA. Garantía escrita, factura y presupuesto sin cargo. Escribinos por WhatsApp.",
        body, active="Inicio", extra_ld=json.dumps(faq_ld, ensure_ascii=False)))


# ---------------------------------------------------------------- SERVICIOS
def servicios_index():
    body = f'''
<section class="page-hero">
  <div class="wrap">
    {breadcrumbs(1, [("Inicio", "index.html"), ("Servicios", None)])}
    <h1>Servicios de refrigeración y climatización</h1>
    <p>Seis especialidades, un mismo procedimiento: diagnóstico, presupuesto escrito y garantía. Elegí la que necesitás.</p>
  </div>
</section>
{services_section(1)}
{brands_carousel()}
{cta_band(1)}'''
    write("servicios/index.html", page(
        "servicios/index.html", 1,
        "Servicios de Refrigeración en CABA | Frig Zone",
        "Instalación de aires, service inverter, cámaras frigoríficas, heladeras comerciales, limpieza profunda y pre-instalación en obras.",
        body, active="Servicios"))


def servicio_page(s):
    idx = SERVICIOS.index(s)
    rel = [x for x in SERVICIOS if x is not s][:3]
    rel_cards = "".join(
        f'<a class="guide" href="{x["slug"]}.html"><img src="../assets/img/{x["img"]}.webp" alt="" loading="lazy" width="192" height="152">'
        f'<div><h3>{html.escape(x["nombre"])}</h3><span>Ver servicio</span></div></a>' for x in rel)

    incluye = "".join(f"<li>{html.escape(i)}</li>" for i in s["incluye"])
    proceso = "".join(
        f'<div class="diag-step"><div class="n">{i}</div><div><strong>Paso {i}</strong><span>{html.escape(p)}</span></div></div>'
        for i, p in enumerate(s["proceso"], 1))
    faqs = "".join(
        f'<details><summary>{html.escape(q)}</summary><div class="answer">{html.escape(a)}</div></details>'
        for q, a in s["faq"])

    body = f'''
<section class="page-hero">
  <div class="wrap">
    {breadcrumbs(1, [("Inicio", "index.html"), ("Servicios", "servicios/index.html"), (s["nombre"], None)])}
    <h1>{html.escape(s["h1"])}</h1>
    <p>{html.escape(s["intro"])}</p>
    <div class="hero-actions">
      <a class="btn btn-primary" href="{wa("Hola Frig Zone, quiero consultar por " + s["nombre"])}" target="_blank" rel="noopener">{icon("wa")}Pedir presupuesto</a>
      <a class="btn btn-ghost" href="tel:+5491173719821">{icon("phone")}Llamar</a>
    </div>
  </div>
</section>

<section class="section">
  <div class="wrap">
    <div class="grid-2" style="align-items:start">
      <div class="prose">
        <h2>Qué incluye</h2>
        <ul>{incluye}</ul>
        <div class="note"><strong>Cómo se cotiza:</strong> {html.escape(s["precio"])}</div>
        <h2>Cómo trabajamos</h2>
        <div class="diag-steps">{proceso}</div>
      </div>
      <div>
        <img src="../assets/img/{s["img"]}.webp" alt="{html.escape(s["nombre"])}" loading="lazy" width="1200" height="900"
             style="border-radius:16px;border:1px solid var(--line);width:100%;aspect-ratio:4/3;object-fit:cover">
        <div class="form-panel" style="margin-top:16px">
          <h3>¿Lo resolvemos?</h3>
          <p class="hint">Contanos el equipo y la zona. Te respondemos con un turno.</p>
          <a class="btn btn-primary btn-block" href="{wa("Hola Frig Zone, necesito " + s["nombre"])}" target="_blank" rel="noopener">{icon("wa")}Escribir por WhatsApp</a>
        </div>
      </div>
    </div>
  </div>
</section>

<section class="section section-alt">
  <div class="wrap">
    <div class="section-head"><div class="eyebrow">Preguntas</div><h2>Dudas sobre {html.escape(s["nombre"].lower())}</h2></div>
    <div class="faq">{faqs}</div>
  </div>
</section>

<section class="section">
  <div class="wrap">
    <div class="section-head"><div class="eyebrow">Seguí explorando</div><h2>Otros servicios</h2></div>
    <div class="grid-3">{rel_cards}</div>
  </div>
</section>
{cta_band(1)}'''

    ld = {
        "@context": "https://schema.org",
        "@type": "Service",
        "name": s["nombre"],
        "serviceType": s["nombre"],
        "description": s["meta_desc"],
        "areaServed": "Ciudad Autónoma de Buenos Aires",
        "provider": {"@type": "LocalBusiness", "name": "Frig Zone", "telephone": "+5491173719821",
                     "url": "https://frigzone.com.ar"},
    }
    bc = {
        "@context": "https://schema.org",
        "@type": "BreadcrumbList",
        "itemListElement": [
            {"@type": "ListItem", "position": 1, "name": "Inicio", "item": "https://frigzone.com.ar/"},
            {"@type": "ListItem", "position": 2, "name": "Servicios", "item": "https://frigzone.com.ar/servicios/"},
            {"@type": "ListItem", "position": 3, "name": s["nombre"]},
        ],
    }
    faq_ld = {
        "@context": "https://schema.org", "@type": "FAQPage",
        "mainEntity": [{"@type": "Question", "name": q,
                        "acceptedAnswer": {"@type": "Answer", "text": a}} for q, a in s["faq"]],
    }
    extra = json.dumps([ld, bc, faq_ld], ensure_ascii=False)
    write(f"servicios/{s['slug']}.html", page(
        f"servicios/{s['slug']}.html", 1, s["meta_title"], s["meta_desc"], body,
        active="Servicios", og_image=f"assets/img/{s['img']}.webp", extra_ld=extra))


# ---------------------------------------------------------------- ZONAS
def zonas_index():
    cards = ""
    for slug, nombre, desc in ZONAS:
        cards += f'''
<a class="card reveal" href="{slug}.html">
  <div class="icon">{icon("pin")}</div>
  <h3>{nombre}</h3>
  <p>{html.escape(desc)}</p>
  <span class="card-link">Ver cobertura {icon("arrow")}</span>
</a>'''
    body = f'''
<section class="page-hero">
  <div class="wrap">
    {breadcrumbs(1, [("Inicio", "index.html"), ("Zonas", None)])}
    <h1>Service técnico por barrio en CABA</h1>
    <p>Atendemos Palermo, Belgrano, Caballito, Almagro, Villa Urquiza y Recoleta. Si tu barrio no está en la lista, escribinos igual: coordinamos según disponibilidad.</p>
  </div>
</section>
<section class="section"><div class="wrap"><div class="grid-3">{cards}</div></div></section>
{cta_band(1)}'''
    write("zonas/index.html", page(
        "zonas/index.html", 1,
        "Service Técnico por Barrio en CABA | Frig Zone",
        "Atendemos Palermo, Belgrano, Caballito, Almagro, Villa Urquiza y Recoleta. Elegí tu barrio y pedí visita.",
        body, active="Zonas"))


def zona_page(z):
    slug, nombre, desc = z
    servicios = "".join(
        f'<li><a href="../servicios/{s["slug"]}.html">{html.escape(s["nombre"])}</a></li>' for s in SERVICIOS)
    otras = "".join(
        f'<a class="zone" href="{x[0]}.html">{icon("pin")}{x[1]}</a>' for x in ZONAS if x[0] != slug)
    body = f'''
<section class="page-hero">
  <div class="wrap">
    {breadcrumbs(1, [("Inicio", "index.html"), ("Zonas", "zonas/index.html"), (nombre, None)])}
    <h1>Service técnico en {nombre}</h1>
    <p>{html.escape(desc)}</p>
    <div class="hero-actions">
      <a class="btn btn-primary" href="{wa("Hola Frig Zone, necesito un técnico en " + nombre)}" target="_blank" rel="noopener">{icon("wa")}Pedir visita en {nombre}</a>
    </div>
  </div>
</section>
<section class="section">
  <div class="wrap">
    <div class="grid-2" style="align-items:start">
      <div class="prose">
        <h2>Qué hacemos en {nombre}</h2>
        <ul>{servicios}</ul>
        <h2>Cómo coordinamos</h2>
        <p>Nos escribís con el tipo de equipo y el síntoma. Te confirmamos disponibilidad para {nombre} y coordinamos un turno de 2 horas. Si es urgente, lo evaluamos como prioridad.</p>
        <div class="note"><strong>Zona de cobertura:</strong> {nombre} y alrededores. Para direcciones fuera de CABA, consultanos antes de reservar.</div>
      </div>
      <div>
        <img src="../assets/img/camara-frio.webp" alt="Servicio técnico en {nombre}" loading="lazy" width="1200" height="900"
             style="border-radius:16px;border:1px solid var(--line);width:100%;aspect-ratio:4/3;object-fit:cover">
      </div>
    </div>
  </div>
</section>
<section class="section section-alt"><div class="wrap">
  <div class="section-head"><div class="eyebrow">Otras zonas</div><h2>También atendemos</h2></div>
  <div class="zones">{otras}</div>
</div></section>
{cta_band(1)}'''
    write(f"zonas/{slug}.html", page(
        f"zonas/{slug}.html", 1,
        f"Service Técnico en {nombre} | Frig Zone",
        f"Instalación, service y mantenimiento de aires, heladeras y cámaras en {nombre}. Garantía escrita y presupuesto sin cargo.",
        body, active="Zonas"))


# ---------------------------------------------------------------- OBRAS
def obras_page():
    figs = ""
    for img, tag, titulo, desc in OBRAS:
        figs += f'<figure><img src="assets/img/{img}.webp" alt="{html.escape(titulo)}" loading="lazy" width="800" height="600"><figcaption><strong>{html.escape(titulo)}</strong><br>{html.escape(desc)}</figcaption></figure>'
    body = f'''
<section class="page-hero">
  <div class="wrap">
    {breadcrumbs(0, [("Inicio", "index.html"), ("Obras", None)])}
    <h1>Obras e instalaciones reales</h1>
    <p>Una selección de trabajos en CABA: cámaras de frío, montajes en obra, equipamiento comercial y mantenimiento. Fotos reales, sin stock.</p>
  </div>
</section>
<section class="section"><div class="wrap"><div class="gallery">{figs}</div>
<p class="brand-note" style="margin-top:20px">Los textos de cada obra son de referencia. Se completan con el barrio, el problema y el resultado de cada trabajo.</p>
</div></section>
{cta_band(0)}'''
    write("obras.html", page(
        "obras.html", 0,
        "Obras e Instalaciones en CABA | Frig Zone",
        "Cámaras frigoríficas, montajes en obra y equipamiento comercial. Fotos reales de trabajos en CABA.",
        body, active="Obras"))


# ---------------------------------------------------------------- PRECIOS
def precios_page():
    filas = [
        ("Diagnóstico en domicilio", "Visita, medición y presupuesto por escrito", "Se descuenta si hacés el trabajo"),
        ("Instalación de split", "Materiales normalizados, vacío y prueba de fugas", "Según metros de cañería y altura"),
        ("Service inverter", "Diagnóstico de placa, sensores y compresor", "Según falla y repuesto"),
        ("Limpieza profunda", "Hidro-funda, desinfección y revisión", "Por equipo"),
        ("Cámara frigorífica", "Diseño, paneles, evaporador y montaje", "Según medidas y temperatura"),
        ("Mantenimiento comercial", "Plan mensual o bimestral con informe", "Según cantidad de equipos"),
    ]
    rows = "".join(f"<tr><td><strong>{a}</strong></td><td>{b}</td><td>{c}</td></tr>" for a, b, c in filas)
    body = f'''
<section class="page-hero">
  <div class="wrap">
    {breadcrumbs(0, [("Inicio", "index.html"), ("Precios", None)])}
    <h1>Precios y formas de trabajo</h1>
    <p>No publicamos un precio único porque cada equipo y cada instalación son distintos. Esto es lo que sí podemos asegurarte: presupuesto escrito, sin cargo y sin sorpresas.</p>
  </div>
</section>
<section class="section"><div class="wrap">
  <div class="table-scroll">
  <table class="price-table">
    <thead><tr><th>Trabajo</th><th>Qué incluye</th><th>Cómo se cotiza</th></tr></thead>
    <tbody>{rows}</tbody>
  </table>
  </div>
  <div class="note"><strong>Por qué no hay precios fijos:</strong> un split en un primer piso con balcón no es lo mismo que uno en un décimo piso con arnés; una cámara de +2 °C no es lo mismo que una de -25 °C. Publicar un número sería engañarte.</div>
  <div class="hero-actions" style="margin-top:26px">
    <a class="btn btn-primary" href="{wa()}" target="_blank" rel="noopener">{icon("wa")}Pedir presupuesto sin cargo</a>
  </div>
</div></section>
{faq_section()}
{cta_band(0)}'''
    write("precios.html", page(
        "precios.html", 0,
        "Precios de Service y Instalación | Frig Zone",
        "Rangos orientativos de service, instalación y limpieza en CABA. Qué incluye cada trabajo y cómo se presupuesta.",
        body, active="Precios"))


# ---------------------------------------------------------------- SOBRE
def sobre_page():
    body = f'''
<section class="page-hero">
  <div class="wrap">
    {breadcrumbs(0, [("Inicio", "index.html"), ("Nosotros", None)])}
    <h1>Un técnico, no un call center</h1>
    <p>Frig Zone es el trabajo de Mati, técnico en refrigeración y climatización. La misma persona que te responde es la que va a tu casa o comercio.</p>
  </div>
</section>
<section class="section"><div class="wrap">
  <div class="about">
    <div class="about-media">
      <img src="assets/img/camara-instalacion.webp" alt="Mati trabajando en una instalación" loading="lazy" width="800" height="880">
      <div class="badge-card"><div class="avatar">M</div><div><strong>Mati</strong><span>Técnico en refrigeración · CABA</span></div></div>
    </div>
    <div class="prose">
      <h2>Por qué trabajo con instrumental</h2>
      <p>Muchos técnicos “purgan” el gas o no hacen vacío para terminar antes. Ese ahorro de una hora se paga después con un compresor quemado. La humedad y los gases incondensables dentro del circuito son la causa silenciosa de la mayoría de las fallas caras.</p>
      <p>Por eso mido el vacío con vacuómetro digital, presurizo con nitrógeno y cargo el gas por balanza. No es marketing: es la diferencia entre una instalación que dura y una que vuelve al año.</p>
      <h2>Cómo trabajo</h2>
      <ul>
        <li>Presupuesto escrito antes de empezar, con alcance y exclusiones.</li>
        <li>Garantía escrita en mano de obra.</li>
        <li>Factura A o B para particulares y comercios.</li>
        <li>Explicación de lo que se hizo y por qué, sin tecnicismos innecesarios.</li>
      </ul>
      <div class="note"><strong>Marcas:</strong> trabajamos con equipos Surrey, BGH, Samsung, LG, Midea, Philco, Carrier, Daikin, Electra, TCL y otras. No implicamos servicio oficial de ninguna marca.</div>
    </div>
  </div>
</div></section>
{brands_carousel()}
{cta_band(0)}'''
    write("sobre-nosotros.html", page(
        "sobre-nosotros.html", 0,
        "Sobre Frig Zone | Técnico en Refrigeración CABA",
        "Quién está detrás de Frig Zone: Mati, técnico en refrigeración y climatización en CABA. Instrumentación, garantía escrita y factura.",
        body, active="Nosotros"))


# ---------------------------------------------------------------- GUÍAS
def guias_index():
    cards = ""
    for g in GUIAS:
        cards += f'''
<a class="card reveal" href="{g["slug"]}.html">
  <img src="../assets/img/{g["img"]}.webp" alt="" loading="lazy" width="800" height="500" style="border-radius:10px;margin-bottom:16px;aspect-ratio:16/10;object-fit:cover">
  <h3>{html.escape(g["titulo"])}</h3>
  <p>{html.escape(g["extracto"])}</p>
  <span class="card-link">Leer guía {icon("arrow")}</span>
</a>'''
    body = f'''
<section class="page-hero">
  <div class="wrap">
    {breadcrumbs(1, [("Inicio", "index.html"), ("Guías", None)])}
    <h1>Guías técnicas de refrigeración</h1>
    <p>Explicaciones cortas para entender qué le pasa a tu equipo y qué esperar de un service. Sin tecnicismos innecesarios.</p>
  </div>
</section>
<section class="section"><div class="wrap"><div class="grid-3">{cards}</div></div></section>
{cta_band(1)}'''
    write("guias/index.html", page(
        "guias/index.html", 1,
        "Guías de Refrigeración y Climatización | Frig Zone",
        "Guías técnicas sobre limpieza de aires, cámaras frigoríficas y códigos de error inverter. Información útil antes de llamar a un técnico.",
        body, active="Guías"))


def guia_page(g):
    cuerpo = "".join(f"<h2>{html.escape(h)}</h2><p>{html.escape(p)}</p>" for h, p in g["cuerpo"])
    ld = {
        "@context": "https://schema.org", "@type": "Article",
        "headline": g["titulo"], "datePublished": g["fecha"],
        "author": {"@type": "Person", "name": "Mati"},
        "publisher": {"@type": "Organization", "name": "Frig Zone"},
        "mainEntityOfPage": f"https://frigzone.com.ar/guias/{g['slug']}.html",
    }
    body = f'''
<section class="page-hero">
  <div class="wrap">
    {breadcrumbs(1, [("Inicio", "index.html"), ("Guías", "guias/index.html"), (g["titulo"], None)])}
    <h1>{html.escape(g["titulo"])}</h1>
    <p>{html.escape(g["extracto"])}</p>
  </div>
</section>
<section class="section"><div class="wrap">
  <div class="prose">
    <img src="../assets/img/{g["img"]}.webp" alt="" loading="lazy" width="800" height="500" style="border-radius:14px;margin-bottom:24px">
    {cuerpo}
    <div class="note"><strong>¿Necesitás que lo vea un técnico?</strong> Escribinos con el tipo de equipo y tu barrio y coordinamos una visita.</div>
  </div>
</div></section>
{cta_band(1)}'''
    write(f"guias/{g['slug']}.html", page(
        f"guias/{g['slug']}.html", 1, f"{g['titulo']} | Frig Zone", g["extracto"],
        body, active="Guías", extra_ld=json.dumps(ld, ensure_ascii=False)))


# ---------------------------------------------------------------- CONTACTO
def contacto_page():
    body = f'''
<section class="page-hero">
  <div class="wrap">
    {breadcrumbs(0, [("Inicio", "index.html"), ("Contacto", None)])}
    <h1>Contacto y turnos</h1>
    <p>Contanos qué equipo es, qué le pasa y en qué barrio estás. Te respondemos con un diagnóstico y disponibilidad.</p>
  </div>
</section>
<section class="section"><div class="wrap">
  <div class="grid-2" style="align-items:start">
    <form class="form-panel" data-wa-form>
      <h3>Escribinos</h3>
      <p class="hint">Respondemos en el día, dentro del horario de atención.</p>
      <div class="field"><label for="nombre">Nombre</label><input id="nombre" name="nombre" data-label="Nombre" required></div>
      <div class="field-row">
        <div class="field"><label for="telefono">Teléfono</label><input id="telefono" name="telefono" data-label="Teléfono" inputmode="tel"></div>
        <div class="field"><label for="zona2">Barrio</label><input id="zona2" name="zona" data-label="Barrio" required></div>
      </div>
      <div class="field"><label for="equipo2">Equipo</label>
        <select id="equipo2" name="equipo" data-label="Equipo">
          <option value="">Elegir</option>
          <option>Aire split</option><option>Inverter</option><option>Heladera comercial</option>
          <option>Cámara frigorífica</option><option>Multisplit / piso techo</option><option>Otro</option>
        </select>
      </div>
      <div class="field"><label for="mensaje">Mensaje</label><textarea id="mensaje" name="mensaje" data-label="Mensaje" rows="3" required></textarea></div>
      <button class="btn btn-primary btn-block" type="submit">{icon("wa")}Enviar por WhatsApp</button>
      <p class="form-msg" role="status"></p>
    </form>
    <div>
      <div class="card" style="margin-bottom:16px">
        <div class="icon">{icon("wa")}</div>
        <h3>WhatsApp</h3>
        <p><a href="{wa()}" target="_blank" rel="noopener" style="color:var(--cyan);font-weight:700">{TEL}</a></p>
      </div>
      <div class="card" style="margin-bottom:16px">
        <div class="icon">{icon("mail")}</div>
        <h3>Email</h3>
        <p><a href="mailto:{EMAIL}" style="color:var(--cyan);font-weight:700">{EMAIL}</a></p>
      </div>
      <div class="card">
        <div class="icon">{icon("clock")}</div>
        <h3>Horarios</h3>
        <p>Lunes a viernes de 9 a 18 h.<br>Sábados de 9 a 13 h.<br>Urgencias: según disponibilidad.</p>
      </div>
    </div>
  </div>
</div></section>
{cta_band(0)}'''
    write("contacto.html", page(
        "contacto.html", 0,
        "Contacto y Turnos | Frig Zone",
        "Pedí turno para service, instalación o presupuesto en CABA. Respondemos por WhatsApp en el día.",
        body, active="Contacto"))


# ---------------------------------------------------------------- LINKS
def links_page():
    items = [
        ("wa", "Pedir visita por WhatsApp", wa(), "primary"),
        ("phone", "Llamar ahora", "tel:+5491173719821", "ghost"),
        ("snow", "Ver servicios", "servicios/index.html", "ghost"),
        ("spark", "Calcular frigorías", "precios.html", "ghost"),
        ("building", "Ver obras", "obras.html", "ghost"),
        ("info", "Guías técnicas", "guias/index.html", "ghost"),
    ]
    botones = "".join(
        f'<a class="btn btn-{cls} btn-block" style="margin-bottom:10px;justify-content:flex-start" href="{href}"'
        + (' target="_blank" rel="noopener"' if href.startswith("http") else "") + f'>{icon(ic)}{label}</a>'
        for ic, label, href, cls in items)
    body = f'''
<section class="section"><div class="wrap" style="max-width:560px;text-align:center">
  <img src="assets/img/snowflake.svg" alt="" width="64" height="64" style="margin:0 auto 14px">
  <h1 style="font-size:32px;letter-spacing:-.02em">Frig Zone</h1>
  <p style="color:var(--muted);margin:8px 0 26px">Refrigeración y climatización en CABA</p>
  {botones}
  <p class="brand-note" style="margin-top:22px">Garantía escrita · Factura A/B · Lun a Vie 9-18 h</p>
</div></section>'''
    write("links.html", page(
        "links.html", 0, "Links | Frig Zone", "Todos los accesos de Frig Zone en un solo lugar.",
        body, noindex=True))


# ---------------------------------------------------------------- LEGALES
def privacidad_page():
    body = f'''
<section class="page-hero"><div class="wrap">
  {breadcrumbs(0, [("Inicio", "index.html"), ("Privacidad", None)])}
  <h1>Política de privacidad</h1>
  <p>Última actualización: octubre de 2026.</p>
</div></section>
<section class="section"><div class="wrap"><div class="prose">
  <h2>Responsable</h2>
  <p>Frig Zone — [Titular / CUIT]. Contacto: <a href="mailto:{EMAIL}" style="color:var(--cyan)">{EMAIL}</a> · {TEL} · CABA, Argentina.</p>
  <h2>Datos que recopilamos</h2>
  <p>Este sitio no tiene backend propio. Los formularios arman un mensaje y abren WhatsApp: los datos que cargás se envían por ese canal y quedan en la conversación. Además, si aceptás, usamos Google Analytics 4 para medir visitas de forma agregada.</p>
  <h2>Para qué los usamos</h2>
  <p>Para responder tu consulta, coordinar una visita y enviarte un presupuesto. No vendemos ni compartimos datos personales con terceros.</p>
  <h2>Cookies</h2>
  <p>Usamos cookies de Google Analytics solo si aceptás el aviso. Podés rechazarlas o desactivarlas desde tu navegador.</p>
  <h2>Tus derechos</h2>
  <p>En los términos de la Ley 25.326 podés solicitar acceso, rectificación o supresión de tus datos escribiendo a {EMAIL}.</p>
</div></div></section>'''
    write("privacidad.html", page(
        "privacidad.html", 0, "Política de Privacidad | Frig Zone",
        "Cómo trata Frig Zone los datos personales recolectados a través del sitio y WhatsApp.",
        body, noindex=True))


def notfound_page():
    body = f'''
<section class="section"><div class="wrap" style="text-align:center;max-width:640px">
  <div style="font-size:80px;font-weight:800;color:var(--cyan);line-height:1">404</div>
  <h1 style="margin:10px 0 12px">No encontramos esa página</h1>
  <p style="color:var(--muted)">Puede que el enlace esté viejo o mal escrito. Probá desde el inicio o escribinos directamente.</p>
  <div class="hero-actions" style="justify-content:center;margin-top:26px">
    <a class="btn btn-primary" href="index.html">Volver al inicio</a>
    <a class="btn btn-ghost" href="{wa()}" target="_blank" rel="noopener">{icon("wa")}Escribir por WhatsApp</a>
  </div>
</div></section>'''
    write("404.html", page("404.html", 0, "Página no encontrada | Frig Zone",
                           "La página que buscás no existe.", body, noindex=True))


# ---------------------------------------------------------------- SEO FILES
def sitemap():
    paths = ["", "servicios/", "obras.html", "precios.html", "sobre-nosotros.html",
             "zonas/", "guias/", "contacto.html"]
    paths += [f"servicios/{s['slug']}.html" for s in SERVICIOS]
    paths += [f"zonas/{z[0]}.html" for z in ZONAS]
    paths += [f"guias/{g['slug']}.html" for g in GUIAS]
    urls = ""
    for p in paths:
        urls += f"  <url><loc>{SITE}/{p}</loc><lastmod>2026-10-21</lastmod><changefreq>monthly</changefreq></url>\n"
    xml = f'<?xml version="1.0" encoding="UTF-8"?>\n<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">\n{urls}</urlset>\n'
    write("sitemap.xml", xml)
    write("robots.txt", f"User-agent: *\nAllow: /\n\nSitemap: {SITE}/sitemap.xml\n")
    write(".nojekyll", "")
    write("manifest.webmanifest", json.dumps({
        "name": "Frig Zone — Refrigeración y Climatización",
        "short_name": "Frig Zone",
        "start_url": "./",
        "display": "standalone",
        "background_color": "#060c16",
        "theme_color": "#060c16",
        "icons": [{"src": "assets/img/snowflake.svg", "sizes": "any", "type": "image/svg+xml"}],
    }, ensure_ascii=False, indent=2))


def main():
    home()
    servicios_index()
    for s in SERVICIOS:
        servicio_page(s)
    zonas_index()
    for z in ZONAS:
        zona_page(z)
    obras_page()
    precios_page()
    sobre_page()
    guias_index()
    for g in GUIAS:
        guia_page(g)
    contacto_page()
    links_page()
    privacidad_page()
    notfound_page()
    sitemap()
    print("OK", len(WRITTEN), "archivos")
    for p in WRITTEN:
        print("  ", p)


if __name__ == "__main__":
    main()
