# Registro de decisiones

Para no volver a discutir lo mismo dos veces. Cada decisión tiene su motivo y la alternativa que descartamos.

---

## Marca y comunicación

| Decisión | Elección | Por qué | Alternativa descartada |
|---|---|---|---|
| Nombre público | **Frig Zone** | Es el que ya usás y el que está en el dominio. | «Frigzone» o «frig.zone» (dificultan dictarlo por teléfono). |
| Handle único | **@frig.zone** (o @frigzone si se libera) | Un solo nombre en las tres redes. | Dejar tres identidades distintas. |
| Tono | Técnico, directo, rioplatense, sin grandilocuencia. | El cliente valora que le expliques, no que le vendas humo. | Tono corporativo o publicitario. |
| Frase «Servicio Técnico Oficial» | **Eliminada** | Sin marca que lo respalde, es publicidad engañosa. | Mantenerla y arriesgar un reclamo. |
| «Normas IRAM» | Se mantiene como **«según normas IRAM»** | Es una práctica, no una certificación. | Decir «certificado IRAM» (falso). |

---

## Sitio web

| Decisión | Elección | Por qué | Alternativa descartada |
|---|---|---|---|
| Arquitectura | **Sitio de 26 páginas** | Permite rankear por servicio y por barrio. | One-page con anclas (techo bajo). |
| Home | Landing fuerte con CTA arriba | El 70% del tráfico es móvil y la urgencia manda. | Home folleto con todo el contenido. |
| Stack | **HTML + CSS + JS propios** | Cero dependencias, carga rápida, sin CDNs. | Tailwind CDN + Lucide CDN (lo que tenía). |
| Imágenes | **WebP + lazy + srcset** | 14,15 MB → 0,91 MB. | PNG sin comprimir. |
| Precios | **No publicar cifras**, explicar cómo se cotiza | No hay datos reales; inventar un número genera reclamos. | Poner «desde $X» inventado. |
| Reseñas | **De ejemplo, marcadas** | No hay reseñas reales todavía. | Inventar testimonios como si fueran reales. |
| Marcas | **32 wordmarks tipográficos** | No hay autorización para usar logos oficiales. | Usar logos de las marcas sin permiso. |
| Formularios | Abren WhatsApp y guardan copia local | No hay backend ni CRM todavía. | Formulario que no hace nada. |

---

## Redes y campañas

| Decisión | Elección | Por qué | Alternativa descartada |
|---|---|---|---|
| Canal principal | **WhatsApp** | Es donde el cliente cierra. | Formulario web como canal principal. |
| Automatización | Empezar por **ManyChat + WhatsApp Business** | Bajo costo y alto impacto. | Contratar un CRM caro desde el día uno. |
| Grupos de Facebook | **1 post cada 7-10 días por grupo** | Evita bans y mantiene presencia. | Publicar todos los días el mismo texto. |
| Link en publicaciones | **No** en el cuerpo; solo «MP» | Facebook castiga links y los admins los borran. | Link directo a la web en cada post. |

---

## Implementación

| Decisión | Elección | Por qué | Alternativa descartada |
|---|---|---|---|
| Editor | **VS Code** | Es el que está instalado. | Visual Studio (no está y no aplica a web estática). |
| Git | **MinGit portable** | No había Git instalado. | Descargar el instalador completo (más pesado). |
| Repositorio | **Local, rama main, 3 commits** | No hay credenciales para push. | Crear repo remoto sin autenticación (imposible). |
| Capturas | **No generadas** | El sandbox bloqueó el navegador y la escalación fue rechazada. | Insistir con otro método (no correspondía). |
| Servidor de prueba | **localhost:8765** | Para verlo en vivo sin publicar. | Subirlo a un hosting temporal sin permiso. |

---

## Decisiones que quedan pendientes

| Decisión | Cuándo tomarla | Opciones |
|---|---|---|
| ¿GitHub Pages o mantener el hosting actual? | Antes de publicar | Pages es gratis y simple; el hosting actual ya tiene el dominio. |
| ¿Dominio `frigzone.com.ar` apunta a Pages? | Después de probar en `github.io` | Cambiar DNS con cuidado para no dejar el dominio caído. |
| ¿Precios públicos o «a consultar»? | Cuando tengas los rangos | Mostrar «desde» filtra consultas; «a consultar» genera más mensajes. |
| ¿Meta Ads o solo grupos? | Después de 30 días de métricas | Sin píxel, Ads es a ciegas. |
| ¿Quién atiende WhatsApp? | Antes de escalar | Mati solo, o un asistente con respuestas rápidas. |
