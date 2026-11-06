# Frig Zone — Sitio web 2026

Sitio estático de **Frig Zone** (refrigeración y climatización en CABA), reconstruido a partir de la auditoría del sitio anterior.

- **Sin frameworks ni CDNs.** CSS y JS propios.
- **26 páginas**: home, 6 servicios, 6 barrios, obras, precios, guías, contacto y legales.
- **Carrusel de 32 marcas** de equipos de refrigeración y climatización.
- **Formularios** que arman el mensaje y abren WhatsApp (sin backend).
- **SEO**: títulos y descripciones por página, canonical, Open Graph, JSON-LD (LocalBusiness, Service, FAQPage, BreadcrumbList, Article), sitemap y robots.

---

## Verlo

**Opción 1 — doble clic:** abrí `index.html` en cualquier navegador.

**Opción 2 — servidor local** (recomendado para probar rutas y formularios):

```powershell
python -m http.server 8765 --directory .
```

Después abrí <http://127.0.0.1:8765>.

**Opción 3 — VS Code:** abrí esta carpeta y usá la extensión *Live Server*.

---

## Resultados frente al sitio anterior

| Métrica | Antes | Ahora |
|---|---|---|
| Peso de imágenes | 14,15 MB (9 PNG) | **0,91 MB** (WebP) |
| Peso total del sitio | ~14,5 MB | **~1,93 MB** |
| Páginas indexables | 1 | **26** |
| Dependencias externas | Tailwind CDN, Lucide CDN, fonts | **0** |
| Lazy loading | No | **Sí, en todas las imágenes** |
| Píxel de Meta | No | Pendiente (se instala al publicar) |
| Datos estructurados | 2 incompletos | **5 completos por página** |

---

## Estructura

```
frigzone-web/
├── index.html                    Home
├── servicios/                    6 páginas de servicio
├── zonas/                        6 páginas de barrio
├── guias/                        3 guías técnicas
├── obras.html  precios.html  sobre-nosotros.html  contacto.html
├── links.html  privacidad.html  404.html
├── assets/
│   ├── css/styles.css            Diseño completo
│   ├── js/main.js                Menú, carrusel, formularios, FAQ
│   └── img/                      WebP optimizados + logo SVG
├── _src/                         Generador del sitio (Python)
│   ├── data.py                   Textos, marcas, servicios, zonas
│   ├── layout.py                 Header, footer y componentes
│   ├── build_site.py             Genera las 26 páginas
│   └── qa.py                     Verifica enlaces, metadatos y schema
├── sitemap.xml  robots.txt  manifest.webmanifest
└── README.md
```

### Editar contenido

1. Cambiá los textos en `_src/data.py` (servicios, zonas, marcas, FAQ, guías).
2. Regenerá el sitio:

```powershell
python _src/build_site.py
python _src/qa.py
```

`qa.py` tiene que devolver **0 errores**. Verifica 1.228 enlaces internos, títulos, descripciones y JSON-LD.

---

## Publicar en GitHub Pages

El repo local ya está inicializado. Para publicarlo:

```powershell
# 1. Crear el repositorio vacío en GitHub (sin README) y luego:
git remote add origin https://github.com/TU-USUARIO/frigzone-web.git
git push -u origin main
```

Después, en GitHub: **Settings → Pages → Source: Deploy from a branch → main / (root) → Save**.

En 1-2 minutos queda en `https://TU-USUARIO.github.io/frigzone-web/`.

### Dominio propio (frigzone.com.ar)

1. En GitHub Pages, **Custom domain**: `frigzone.com.ar`.
2. En el DNS del dominio, apuntar a GitHub Pages:
   - `A` → `185.199.108.153`, `185.199.109.153`, `185.199.110.153`, `185.199.111.153`
   - `CNAME` para `www` → `TU-USUARIO.github.io`
3. Esperar la propagación y activar **Enforce HTTPS**.

> Importante: el dominio actual apunta a un servidor IIS. Hacé el cambio de DNS recién cuando el sitio esté probado en `github.io`, para no dejar el dominio sin servicio.

---

## Qué falta completar (datos reales)

Estos puntos están marcados en el sitio y hay que reemplazarlos antes de publicar:

- [ ] **CUIT y titular** en el footer y en `privacidad.html`.
- [ ] **Precios reales** o rangos en `precios.html` (hoy explica cómo se cotiza, sin cifras).
- [ ] **Reseñas reales de Google** (las 3 actuales son de ejemplo).
- [ ] **Fotos propias** de Mati y de obras recientes (las actuales son del sitio anterior).
- [ ] **Horarios reales** de atención.
- [ ] **Meta Pixel** y evento de lead.
- [ ] **Google Business Profile** con el mismo NAP.
- [ ] **Email** `contacto@frigzone.com.ar` (hoy es un placeholder).
- [ ] **WhatsApp Business** con catálogo y respuestas rápidas.
- [ ] **Logos oficiales de marcas**: hoy son wordmarks tipográficos de referencia. Para usar logos reales hace falta autorización de cada marca.

---

## Notas

- Los **formularios** no tienen backend: guardan una copia en `localStorage` (solo demo) y abren WhatsApp. Al conectar un CRM o Google Sheets, se reemplaza esa parte en `assets/js/main.js`.
- El **carrusel de marcas** es accesible: se puede arrastrar, usar las flechas del teclado y se pausa al pasar el mouse. Respeta `prefers-reduced-motion`.
- Las **marcas** listadas son las principales del mercado argentino, no “todas” las que existen: es una selección ampliable en `_src/data.py`.
- El sitio **no afirma** ser service oficial de ninguna marca. Esa frase del sitio anterior se reemplazó por “servicio técnico especializado”.

---

© 2026 Frig Zone. Contenido y fotos del sitio anterior, reutilizados para esta propuesta.
