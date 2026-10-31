# Datos pendientes para publicar

Todo lo que falta para que el sitio deje de tener placeholders y pueda salir a la calle. Está ordenado por prioridad.

---

## Prioridad alta (sin esto no se publica)

| # | Dato | Para qué se usa | Dónde está el placeholder | Cómo conseguirlo |
|---|---|---|---|---|
| 1 | **CUIT y nombre del titular** | Footer, política de privacidad y presupuestos. | `privacidad.html` y footer de todas las páginas. | Constancia de inscripción en AFIP. |
| 2 | **Email corporativo** `contacto@frigzone.com.ar` | Contacto y confianza. | Footer y `contacto.html`. | Zoho Mail (gratis con dominio propio) o Google Workspace. |
| 3 | **Precios o rangos** | Filtrar consultas y responder «¿cuánto sale?». | `precios.html`. | Definí: diagnóstico, instalación desde, limpieza desde. |
| 4 | **Reseñas reales de Google** | Prueba social. | `index.html` (3 reseñas de ejemplo). | Crear/reclamar Google Business Profile y pedir reseñas. |
| 5 | **Fotos propias** de Mati y de obras | Humanizar y demostrar. | Hero, `sobre-nosotros.html`, `obras.html`. | Fotos del trabajo real, con permiso del cliente. |
| 6 | **Horarios reales** | Evitar promesas falsas. | Footer, `contacto.html`, schema. | Definir y sostener. |
| 7 | **¿Sos service oficial de alguna marca?** | Si sí, decirlo con respaldo; si no, evitar la frase. | Ya se cambió a «servicio técnico especializado». | Revisar contratos o autorizaciones. |
| 8 | **Acceso al hosting o DNS** | Publicar el sitio nuevo. | — | Panel del proveedor actual (IIS) o cambiar a GitHub Pages. |
| 9 | **Usuario de GitHub** | Subir el repo y publicar. | — | Crear cuenta y repositorio `frigzone-web`. |

---

## Prioridad media (mejora la conversión)

| # | Dato | Para qué | Cómo |
|---|---|---|---|
| 10 | Años de experiencia y cantidad de obras | Prueba en el hero. | Dato real; si es poco, usar «+X obras» en vez de años. |
| 11 | Matrícula o habilitación | Credibilidad y schema. | Certificado o constancia profesional. |
| 12 | Ticket promedio y tasa de cierre | Calcular la economía de las campañas. | Planilla de métricas de las últimas 8 semanas. |
| 13 | Zonas reales de cobertura | Páginas de barrio y grupos. | Lista de barrios donde efectivamente trabajás. |
| 14 | WhatsApp Business verificado | Catálogo y respuestas automáticas. | App WhatsApp Business, verificación del número. |
| 15 | Meta Pixel ID | Medir campañas y hacer retargeting. | Business Manager → Orígenes de datos → Píxel. |

---

## Prioridad baja (cuando haya movimiento)

| # | Dato | Para qué |
|---|---|---|
| 16 | Fotos de antes/después | Contenido para redes. |
| 17 | Testimonios en video | Prueba social fuerte. |
| 18 | Casos de estudio con nombre del cliente | Autoridad y SEO. |
| 19 | Catálogo de cámaras con medidas | Página de producto. |
| 20 | Lista de marcas con autorización para usar logos | Reemplazar los wordmarks tipográficos. |

---

## Checklist de publicación

- [ ] CUIT y titular en el footer.
- [ ] Email corporativo funcionando.
- [ ] Precios o rangos definidos.
- [ ] 10 reseñas reales cargadas.
- [ ] Fotos propias reemplazando las del sitio anterior.
- [ ] Horarios reales.
- [ ] Frase «servicio oficial» revisada.
- [ ] Píxel de Meta instalado y probado.
- [ ] Google Business Profile creado y verificado.
- [ ] Dominio apuntando al hosting nuevo (con HTTPS).
- [ ] Sitemap enviado a Search Console.
- [ ] Formulario probado en celular y en computadora.

---

## Cómo pedirme que complete esto

Cuando tengas los datos, pegame esto en el chat:

> «Deep, actualizá el sitio con estos datos: CUIT …, email …, precios …, horarios …, años …»

Y yo los reemplazo en `_src/data.py` o directamente en las páginas, regenero y vuelvo a pasar el QA.
