# Flyers Frig Zone

Piezas gráficas para redes y para imprenta. Todas usan la identidad del sitio: azul noche, cian y el copo de nieve.

> **Nota de diseño:** los flyers son tipográficos, sin fotos. Las imágenes del sitio anterior son infografías con texto incrustado y se veían mal en una pieza limpia. Si querés fotos, usá fotos propias de obras (sin texto) y las incorporamos.

---

## Qué hay

### `feed/` — para publicar en grupos y redes
- **6 flyers** de 1080 × 1350 px (4:5), en PNG y JPG.
- Ángulos: urgencia, limpieza, instalación, cámaras, comercio y mantenimiento.
- Listos para Facebook, Instagram y grupos de compra/venta.

### `grupos/` — flyer general cuadrado
- **1080 × 1080 px**, para el feed y para grupos donde la imagen vertical se recorta.
- Resume los 6 servicios + marcas + garantías + QR.

### `imprenta/10x15/` — el flyer para repartir
- **Formato final: 10 × 15 cm** (100 × 150 mm), vertical.
- **Con sangrado:** 106 × 156 mm (3 mm por lado).
- **300 DPI**, RGB, con **marcas de corte**.
- Frente y dorso, más un PDF de 2 caras.
- Archivos: `Flyer_10x15_Frente.pdf` / `_Dorso.pdf` / `_2caras.pdf` (y los PNG).

### `imprenta/A4/` — versión grande (opcional)
- A4 con sangrado, 300 DPI, frente y dorso. Para cartelería o para imprimir en casa y recortar.

---

## Especificaciones para la imprenta

| Ítem | Valor |
|---|---|
| Formato final | 10 × 15 cm (vertical) |
| Tamaño con sangrado | 106 × 156 mm |
| Resolución | 300 DPI |
| Color | RGB (pedir conversión a CMYK si la imprenta lo exige) |
| Sangrado | 3 mm por lado |
| Marcas de corte | Incluidas en el PDF |
| Papel sugerido | Ilustración 150 g o 170 g |
| Impresión | Doble faz, 4/4 |
| Cantidad sugerida | 500 a 1.000 (baja el costo unitario) |

**Importante:** el PDF ya viene con el tamaño correcto. Decile a la imprenta: *“archivo con sangrado de 3 mm y marcas de corte, formato final 10×15 cm”*. Si piden CMYK, que lo conviertan ellos o pedime una versión adaptada.

---

## Qué dice cada flyer

| Archivo | Gancho | Cuándo usarlo |
|---|---|---|
| `01-urgencia` | ¿Tu aire dejó de enfriar? | Lunes a jueves, 9-11 h. |
| `02-limpieza` | Tu aire limpio consume 30% menos. | Martes y miércoles. |
| `03-instalacion` | Instalación con vacío real. | Septiembre a diciembre y marzo. |
| `04-camaras` | Cámara de frío a medida. | Comercios y gastronómicos. |
| `05-comercio` | Tu heladera no enfría. | Comercios con mercadería en riesgo. |
| `06-mantenimiento` | Plan de mantenimiento. | Fin y principio de mes. |
| `general-1080` | Refrigeración y climatización. | Grupos y feed en general. |
| `10x15` | Frío que funciona. Sin atajos. | Reparto en la calle y en comercios. |

---

## Textos para acompañar la publicación

**Urgencia**
> ¿Tu aire prende pero no enfría? No lo dejes andando: se fuerza el compresor y la reparación sale el doble. Atiendo en CABA con garantía escrita. Mandame MP con tu barrio.

**Limpieza**
> Tu aire limpio consume hasta 30% menos. Limpieza profunda con hidro-funda, sin ensuciar tu casa. Turnos esta semana en CABA. Escribime por privado.

**Cámaras**
> Cámaras de frío a medida para tu comercio. Diseño, paneles de alta densidad y montaje incluido. Presupuesto sin cargo. Mandame MP con el rubro y las medidas.

**General**
> Refrigeración y climatización en CABA: aires, heladeras comerciales y cámaras de frío. Garantía escrita y factura. Escaneá el QR o mandame MP.

---

## El QR

Todos los flyers tienen un QR que abre WhatsApp con el mensaje *“Hola Frig Zone, vi el flyer”*. Si cambia el número, hay que regenerar los QR y volver a generar las piezas (`flyers_src/flyers.py`).

---

## Cómo regenerar

```powershell
python flyers_src/flyers.py
```

Los textos y los ángulos están en la lista `FLYERS`, al principio del archivo.
