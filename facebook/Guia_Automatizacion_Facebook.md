# Automatización de Facebook — Frig Zone

## Respuesta corta

**Sí se puede automatizar, pero no sin tu autorización.** No puedo entrar a tu cuenta ni publicar en tu página sin un permiso de Meta (un token de página). Lo que sí puedo hacer es dejarte el sistema armado, los flujos escritos y un script listo para ejecutar en cuanto conectes la cuenta.

Hay tres niveles. Empezá por el 1, que es gratis y se configura en una tarde.

---

## Nivel 1 — Meta Business Suite (gratis)

Es la herramienta oficial de Meta. No requiere programar.

### A. Programar publicaciones
1. Entrá a [business.facebook.com](https://business.facebook.com) con la cuenta que administra la página.
2. **Contenido → Crear publicación**.
3. Escribí el texto, subí el flyer y elegí **Programar**.
4. Repetí para la semana. Se publica solo.

**Frecuencia sugerida:** 3 publicaciones por semana en la página y 2 en grupos.

### B. Respuestas automáticas
En **Configuración → Mensajes automáticos**:
- **Mensaje de bienvenida:** “¡Hola! Soy Mati, de Frig Zone. Contame qué equipo es, qué le pasa y en qué barrio estás.”
- **Respuesta de ausencia:** “Gracias por escribir. Te respondo hoy dentro del horario de atención (9 a 18 h). Si es urgente, escribí URGENTE.”
- **Preguntas frecuentes:** precio, zona, garantía, formas de pago.

### C. Bandeja unificada
En **Bandeja de entrada** ves Messenger, comentarios e Instagram en un solo lugar. Respondé desde ahí y no se te escapa ninguna consulta.

---

## Nivel 2 — ManyChat (automatización de DMs)

ManyChat conecta la página de Facebook y responde por vos cuando alguien comenta o escribe una palabra clave.

### Flujo 1: comentario “PRECIO”
1. Crear un flujo con disparador **“Comentario en publicación”**.
2. Palabra clave: `PRECIO`, `INFO`, `CUANTO`.
3. Acción: enviar DM con:
   > “¡Hola! Para pasarte un precio real necesito tres datos: ¿qué equipo es?, ¿qué le pasa? y ¿en qué barrio estás?”
4. Agregar botones: **Escribir por WhatsApp** / **Ver servicios**.

### Flujo 2: palabra “CÁMARA”
1. Disparador: mensaje directo con `CÁMARA`.
2. Enviar ficha breve + preguntas: rubro, medidas y temperatura.
3. Derivar a WhatsApp con los datos cargados.

### Flujo 3: post-servicio
1. Disparador manual (etiqueta “terminado”).
2. Mensaje a las 24 h pidiendo reseña en Google.
3. Si responde “sí”, enviar el link.

**Costo:** ManyChat tiene plan gratis limitado; el plan Pro ronda los USD 15/mes.

---

## Nivel 3 — API de Meta (publicación automática)

Esto es lo que permite publicar o programar desde un archivo, sin entrar a la web de Meta. Requiere configurar una app.

### Requisitos
1. Una **página de Facebook** (no perfil personal).
2. Una **app en Meta for Developers** ([developers.facebook.com](https://developers.facebook.com)).
3. Permisos: `pages_manage_posts`, `pages_read_engagement`.
4. Un **token de página de larga duración**.

### Cómo obtener el token (resumen)
1. Crear la app en Meta for Developers (tipo “Empresa”).
2. Agregar el producto **Facebook Login**.
3. En **Herramientas → Graph API Explorer**, elegir la página y los permisos.
4. Generar el token y extenderlo a 60 días.
5. Guardarlo en una variable de entorno, **nunca en el chat ni en un archivo compartido**.

```powershell
$env:FB_PAGE_ID = "1234567890"
$env:FB_TOKEN   = "EAAB..."
```

### Script incluido
`publicar_facebook.py` lee un JSON de publicaciones y las programa.

```powershell
# Ver qué haría, sin publicar
python facebook/publicar_facebook.py --file facebook/posts_ejemplo.json --dry-run

# Publicar de verdad (con el token cargado)
python facebook/publicar_facebook.py --file facebook/posts_ejemplo.json
```

Formato del JSON:

```json
[
  {
    "message": "¿Tu aire dejó de enfriar? ...",
    "link": "https://frigzone.com.ar",
    "scheduled_iso": "2026-10-25T10:00:00-03:00"
  }
]
```

Si `scheduled_iso` está vacío, publica en el momento.

---

## Checklist de automatización

- [ ] Página con nombre unificado: **Frig Zone — Refrigeración y Climatización CABA**.
- [ ] Botón de acción: “Enviar mensaje por WhatsApp”.
- [ ] Mensaje de bienvenida y de ausencia configurados.
- [ ] Preguntas frecuentes cargadas.
- [ ] Meta Business Suite con 2 semanas de publicaciones programadas.
- [ ] ManyChat conectado con el flujo “PRECIO”.
- [ ] Píxel de Meta instalado en el sitio.
- [ ] Token de página guardado en variable de entorno.
- [ ] Probar el script en `--dry-run` antes de publicar.
- [ ] Revisar métricas semanales (alcance, mensajes, clics).

---

## Riesgos y límites

- **El token caduca.** Los de larga duración duran ~60 días; hay que renovarlo.
- **Meta limita publicaciones.** No spamees: 1-3 por día como máximo.
- **Automatizar todo genera rechazo.** Los flujos cerrados (precio, zona, garantía) funcionan; las respuestas largas con IA conviene revisarlas.
- **Nunca compartas el token.** Si se filtra, cualquiera puede publicar en tu página.
- **Los grupos no se automatizan por API.** Facebook no permite publicar en grupos de terceros de forma automática; eso se hace a mano (o con el calendario que ya tenés).

---

## Qué puedo hacer yo

| Tarea | ¿Puedo? | Qué necesito |
|---|---|---|
| Escribir los textos y el calendario | Sí | Nada. |
| Diseñar los flyers | Sí | Nada. |
| Configurar ManyChat | No directamente | Que vos conectes la página; yo te guío paso a paso. |
| Publicar por API | Sí, cuando esté el token | `FB_PAGE_ID` y `FB_TOKEN` en tu máquina. |
| Administrar la cuenta | No | Requiere acceso y autorización explícita. |
