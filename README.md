# FrigZone · Deep

Esta carpeta guarda todo lo que trabajamos juntos: el historial de la conversación, los documentos entregados, el sitio web y una guía para que cada vez hagas mejores preguntas.

**Sesión:** 21 de octubre de 2026
**Con:** Mati (Frig Zone) y Deep

---

## Qué hay acá

| Archivo / carpeta | Qué es |
|---|---|
| `01_Conversacion_Completa.md` | El registro de la sesión: qué pediste, qué hice y qué salió de cada turno. |
| `02_Guia_Preguntas_Efectivas.md` | Método para pedir mejor: plantilla, ejemplos y checklist. |
| `03_Datos_Pendientes.md` | Todo lo que falta completar para publicar el sitio y cómo conseguirlo. |
| `04_Registro_de_Decisiones.md` | Las decisiones que tomamos y por qué (para no revisarlas dos veces). |
| `Guia_de_Aplicacion.docx` | El paso a paso para aplicar todo, con checklist imprimible. |
| `documentos/` | El plan maestro (Word), el calendario (Excel) y los textos (Markdown). |
| `sitio-web/` | El sitio nuevo completo, listo para abrir o publicar. |
| `flyers/` | Piezas para redes, grupos y el flyer 10×15 para imprenta (PDF con sangrado). |
| `facebook/` | Guía de automatización y script para publicar en la página. |

---

## Cómo abrir el sitio

**Doble clic** en `sitio-web/index.html`.

Si querés probarlo como si estuviera publicado:

```powershell
cd "sitio-web"
python -m http.server 8765
```

Y abrís <http://127.0.0.1:8765>.

---

## Cómo se actualiza esta carpeta

Al final de cada sesión, decime:

> «Deep, actualizá la carpeta FrigZone · Deep con lo de hoy.»

Yo agrego el turno nuevo a `01_Conversacion_Completa.md`, actualizo pendientes y decisiones, y copio los archivos nuevos.

También podés pedirme:
- «Resumime en 10 líneas lo que hicimos hoy» → queda como cierre de sesión.
- «¿Qué decisiones tomamos y por qué?» → revisión rápida.
- «¿Qué me falta para publicar?» → checklist actualizado.

---

## Regla de oro

Esta carpeta es **tuya**. No guarda contraseñas, tokens ni datos sensibles. Si alguna vez necesitás compartirla, revisá primero `03_Datos_Pendientes.md` (ahí hay placeholders, no datos reales).
