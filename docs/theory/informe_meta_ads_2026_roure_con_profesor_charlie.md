---
title: "Meta Ads 2026: investigación junio–octubre y análisis del Profesor Charley T"
author: "Investigación para Roure"
date: "2026-10-16"
lang: es-AR
coverage: "2026-06-16 a 2026-10-16"
status: "Investigación pública; no es auditoría de una cuenta publicitaria"
---

# Meta Ads 2026: qué cambió y qué conviene hacer

**Informe extendido en Markdown — 16 de junio al 16 de octubre de 2026**  
**Mercado:** Argentina, con contexto global  
**Áreas:** Andromeda, GEM, Advantage+, IA, creatividad, segmentación, campañas, Pixel, Conversions API, atribución, presupuestos, escalado, políticas y Marketing API  
**Aplicación:** Roure, marca de moda femenina juvenil  
**Edición ampliada:** añade un capítulo de investigación sobre **Professor Charley T / Charles Tichenor IV**, basado en publicaciones fechadas de junio a octubre de 2026.

> **Alcance y método.** Este archivo ofrece una versión estructurada y ampliada del informe en PDF. Los anuncios oficiales, la investigación de ingeniería, las observaciones de especialistas y las hipótesis operativas están diferenciados. No se utilizaron resultados privados de la cuenta publicitaria de Roure. Las disponibilidades pueden variar por país, objetivo y cuenta.

## Índice

1. [Resumen ejecutivo](#1-resumen-ejecutivo)
2. [Cronología de cambios](#2-cronología-de-cambios)
3. [Andromeda, GEM e infraestructura](#3-andromeda-gem-e-infraestructura)
4. [Advantage+, segmentación y estructura](#4-advantage-segmentación-y-estructura)
5. [Creatividad, IA, formatos y fatiga](#5-creatividad-ia-formatos-y-fatiga)
6. [Catálogo, comercio, creadores y conversiones](#6-catálogo-comercio-creadores-y-conversiones)
7. [Pixel, Conversions API y atribución](#7-pixel-conversions-api-y-atribución)
8. [Métricas, ROAS y rentabilidad](#8-métricas-roas-y-rentabilidad)
9. [Asistentes de IA, MCP, Marketing API y gobernanza](#9-asistentes-de-ia-mcp-marketing-api-y-gobernanza)
10. [Cambios regulatorios y situación de Argentina](#10-cambios-regulatorios-y-situación-de-argentina)
11. [Professor Charley T: análisis de sus métodos de 2026](#11-professor-charley-t-análisis-de-sus-métodos-de-2026)
12. [Roure: estrategia recomendada](#12-roure-estrategia-recomendada)
13. [Experimentos, tablero y plan de 90 días](#13-experimentos-tablero-y-plan-de-90-días)
14. [Mitos, controversias y evaluación de evidencia](#14-mitos-controversias-y-evaluación-de-evidencia)
15. [Fuentes y videos originales](#15-fuentes-y-videos-originales)

---

## 1. Resumen ejecutivo

La evolución de Meta Ads en estos cuatro meses se explica por **tres fuerzas simultáneas**: modelos de recomendación publicitaria cada vez más complejos; una interfaz que automatiza y simplifica configuraciones antes manuales; y nuevas herramientas de IA para crear, analizar y administrar anuncios.

### Cinco conclusiones ejecutivas

1. **Andromeda no nació entre junio y octubre de 2026.** La arquitectura de recuperación de anuncios fue presentada públicamente por Meta en diciembre de 2024. Presentarla como un lanzamiento nuevo sería históricamente erróneo. [S14]
2. **GEM sí tiene una actualización central publicada el 13 de octubre de 2026.** Meta pasó a describir un modelo central capaz de aprovechar datos de varias superficies y objetivos de campaña. Reportó ganancias de conversión y CTR agregadas, que **no** son una promesa de mejor ROAS individual. [S10]
3. **Las herramientas de creación y administración publicitaria con IA avanzaron en junio y octubre.** Hay mejoras disponibles ampliamente y otras en beta o despliegue progresivo. [S02][S09]
4. **Las señales comerciales propias ganan importancia.** Catálogo, compra confirmada, valor del pedido, disponibilidad, datos de producto y deduplicación entre Pixel/CAPI determinan lo útil que resulta una optimización automática. [S01][S12]
5. **Los métodos de media buyers —incluido Professor Charley T— son hipótesis útiles, no normas de Meta.** Su estructura “Andromeda 1”, el formato 3:2:2 y el análisis 4Pi son marcos tácticos que conviene someter a prueba según tamaño, presupuesto y márgenes. [C01][C02][C03]

**Diagnóstico recomendado para Roure:** antes de rediseñar campañas, cruzar gasto publicitario, pedidos efectivamente pagados, margen de contribución, catálogo, anuncios y stock. Los cambios de estructura solo deberían responder a un problema probado.

### Matriz de confianza

| Código | Tipo de evidencia | Cómo se interpreta |
|---|---|---|
| A | Comunicado oficial de Meta o nota de Meta Engineering | Se confirma el anuncio y la descripción; no disponibilidad para cada cuenta |
| B | Documentación técnica accesible parcialmente o experto independiente verificable | Evidencia operativa valiosa, con limitaciones de alcance |
| C | Notificación de anunciantes, testimonio o despliegue no documentado universalmente | Requiere validación dentro de la cuenta |
| H | Hipótesis, método de experto o propuesta para Roure | Recomendación que debe evaluarse experimentalmente |

---

## 2. Cronología de cambios

| Fecha | Cambio o anuncio | Evidencia | Qué revisar |
|---|---|---|---|
| **16 jun.** | Comercio integrado, Live Video Ads, afiliación, checkout y mayor uso de datos de catálogo en campañas de Ventas | A [S01] | Calidad del feed, stock, destinos |
| **23 jun.** | IA creativa, memoria de marca, colaboraciones con creadores y Creator Marketing Hub | A [S02] | Derechos de uso y consistencia creativa |
| **13 jul.** | Infraestructura de servicio de anuncios: mejoras técnicas de latencia y recuperación | A [S04] | No confundir mejoras del backend con ahorro individual garantizado |
| **15 jul.** | Investigación sobre representación jerárquica de intereses (HIR) | A, investigación [S03] | Entender la dirección técnica; no asumir rollout universal |
| **29 jul.** | Marketing API v26.0 y cambios/deprecaciones técnicas | B [S16][S17] | Compatibilidad de integraciones propias |
| **19 ago.** | Meta AI conectada con datos empresariales y publicitarios para consultas y reportes | A [S05] | Herramientas disponibles para la cuenta |
| **20 ago.** | Pruebas de reducción de controles manuales de placements por conjunto | B [S06] | Objetivos afectados y controles a nivel cuenta |
| **Fin de ago.** | Reportes de métrica de diversidad creativa y cambios de breakdowns | B [S15] | Etiquetas experimentales y reporting |
| **15 sep.** | Meta One y funciones profesionales/de IA asociadas a suscripciones | A [S07] | Elegibilidad y precio local |
| **28 sep.** | Reportes de ampliaciones en mensajería WhatsApp vía API | B [S15] | Configuración y términos aplicables |
| **29 sep.** | Muse para pequeños negocios, inicialmente EE. UU. y Canadá | A [S08] | No asumir disponibilidad argentina |
| **6 oct.** | Ads Creative Studio, generación de video, asistentes agénticos, MCP, Customer Lifecycle Strategy | A [S09] | Accesos, aprobaciones y pruebas de formatos |
| **13 oct.** | Meta Engineering publica evolución de GEM | A [S10] | Implicaciones de predicción cruzada entre superficies |
| **14 oct.** | Avisos a algunas cuentas sobre activación futura de product browsing | C [S15] | Revisar notificación particular de Business Suite |

**Importante:** que una función aparezca en una publicación de Meta no demuestra que estuviera habilitada ese mismo día para anunciantes argentinos.

---

## 3. Andromeda, GEM e infraestructura

### 3.1. Qué es Andromeda y qué no es

Andromeda es una arquitectura de **recuperación de anuncios candidatos** (*retrieval*). Reduce un universo gigantesco de anuncios elegibles a un conjunto manejable que participa en etapas posteriores de selección y ranking. Fue presentada en diciembre de 2024 [S14]. No es sinónimo de todo el sistema de subasta ni una nueva opción visible en Ads Manager.

Consecuencias prudentes:

- La **diversidad significativa** de mensajes puede ayudar a cubrir necesidades distintas; no existe un número obligatorio universal de anuncios por conjunto.
- La IA publicitaria no evita la necesidad de obtener datos de compras confiables.
- Optimizar la combinación correcta de **producto + propuesta + creatividad + destino** es más importante que intentar descifrar reglas ocultas de la plataforma.

### 3.2. Representación jerárquica de intereses (15 de julio)

Meta Engineering publicó investigación sobre *Hierarchical Interest Representation* (HIR): aprovechar señales de interacciones, relaciones semánticas y representaciones jerárquicas para comprender mejor intereses implícitos, incluso cuando escasean las compras observadas. La nota discute posibles conexiones con otros sistemas publicitarios. Es evidencia sobre investigación y arquitectura, **no** prueba de una funcionalidad nueva disponible para cada anunciante. [S03]

### 3.3. GEM de octubre: novedad central

El **13 de octubre de 2026**, Meta describió una nueva generación de GEM como modelo central para aprender de señales de Facebook, Instagram, Reels y múltiples objetivos de publicidad. Incluye aprendizaje entre superficies, una arquitectura que procesa secuencias largas y transferencia de representaciones a modelos especializados. [S10]

Meta reportó **+18,9 % en conversiones y +12 % en CTR** en su evaluación agregada. Es información atribuida a Meta; no equivale a que todos los anunciantes obtendrán esas mismas ganancias, ni permite predecir el CPA de Roure. La publicación detalla además mejoras por superficie y objetivo, con bases de evaluación específicas. [S10]

Un modelo simplificado de la entrega:

```text
Señales y elegibilidad: objetivo, reglas, Pixel/CAPI, catálogo, anuncios
            ↓
Andromeda: recuperación de candidatos relevantes
            ↓
Ranking y predicción: GEM y otros modelos
            ↓
Subasta y entrega: determina anuncio e impresión
            ↓
Medición y atribución: reporta interacciones y conversiones
```

### 3.4. Infraestructura (13 de julio)

Meta publicó mejoras internas que redujeron latencia de cola y optimizaron la recuperación/ordenación de anuncios. Son resultados de capacidad del sistema; un porcentaje de mejora del backend **no** puede interpretarse directamente como un descuento equivalente de CPM o CPA. [S04]

---

## 4. Advantage+, segmentación y estructura

### 4.1. Tendencia general

Meta impulsa audiencias menos fragmentadas, optimización automática y más señales de comportamiento. No obstante, **no existe una norma oficial según la cual toda campaña debe usar únicamente segmentación amplia**. La adecuación depende de región, objetivo, reglas regulatorias, stock, margen y tamaño de la cuenta. [S09][S18]

### 4.2. Controles de ubicaciones

Jon Loomer documentó en agosto pruebas de reducción de exclusiones manuales de ubicaciones dentro de determinados objetivos publicitarios. Dependiendo de la cuenta, pueden existir controles a nivel cuenta o reglas de valor. **Una regla que ajusta pujas no equivale necesariamente a excluir una ubicación de forma absoluta.** [S06]

Para Roure: no retirar Facebook, Instagram, Reels o Audience Network solo porque se perciben “de menor calidad”. Analizar compras pagadas y márgenes por ubicación, con un volumen mínimo suficiente, antes de decidir.

### 4.3. Customer Lifecycle Strategy

Meta anunció en octubre mayor acceso a estrategias de ciclo de vida del cliente y herramientas para distinguir adquisición de compradores nuevos frente a actuales. Su utilidad depende de la calidad de las listas y eventos, y de que el negocio pueda identificar realmente clientes existentes. [S09]

### 4.4. Estructura inicial sugerida (hipótesis H)

| Nivel | Sugerencia para una marca de presupuesto contenido | Separar solamente si… |
|---|---|---|
| Campaña | Una campaña principal de **Ventas / compra web** como referencia | Hay prueba controlada, geografía u objetivos incompatibles |
| Conjunto principal | Audiencia suficientemente amplia, regiones atendidas y exclusiones indispensables | Hay diferentes economías (retail/mayorista) o limitaciones reales |
| Anuncios | Varios conceptos creativos claramente diferenciados | Se demuestra saturación o se justifica un test |
| Retención | Mantener integrada o específica, según datos y presupuesto | La recurrencia y volumen justifican separación |

Esta es una **propuesta de partida**, no la arquitectura obligatoria para Roure ni un criterio oficial de Meta.

---

## 5. Creatividad, IA, formatos y fatiga

### 5.1. Funciones confirmadas

En junio Meta detalló nuevos desarrollos para memoria de marca, textos y video, traducciones, aprobaciones y trabajo con creadores. En octubre anunció disponibilidad general de generación de video desde imágenes dentro de Advantage+ creative, mientras que otras soluciones masivas de video-catálogo continuaban limitadas a beta y elegibilidad. También se amplió Ads Creative Studio, con análisis y herramientas de modificación de hooks, subtítulos, audio, duración y escenas finales. [S02][S09]

Que el video consuma mucho tiempo de uso de Instagram y Facebook **no demuestra** que un video supere siempre a una fotografía de producto. La prueba debe medir compras, margen y costo real.

### 5.2. Diversidad creativa aplicable a Roure

| Idea | Necesidad de la compradora | Formato candidato |
|---|---|---|
| Outfit completo | “¿Cómo me quedaría?” | Modelo usando prendas en Reel |
| Tres combinaciones | “¿Me sirve para distintos planes?” | Video con 3 looks |
| Tela y calce | “¿Será como se ve en fotos?” | Detalles y medidas reales |
| Precio/conjunto | “¿Vale la pena?” | Estático o carrusel con precio final |
| Novedades | “¿Qué llegó?” | Reel de nuevos ingresos |
| Prueba social | “¿Puedo confiar?” | Reseña real y autorizada |
| Envíos y cambios | “¿Qué pasa si no me queda?” | Anuncio que responde objeciones |

La diversidad importante es entre **promesas, beneficios, dudas y ocasiones de uso**, no en cambios mínimos de color o tipografía. [S18]

### 5.3. Fatiga: cómo diagnosticarla

- Considerar evolución conjunta de **frecuencia, CPM, CTR de enlace, CPA y conversión de la tienda**.
- Controlar stock, cambios de precio, promociones, estacionalidad y fallos del checkout.
- No declarar “fatiga” por un solo número alto de frecuencia; una pieza dirigida a personas próximas a comprar puede mostrar frecuencia alta y buen CPA.
- Si varios anuncios del mismo artículo empeoran al mismo tiempo, revisar también oferta, precio, disponibilidad y competencia.

### 5.4. Control de calidad de creatividad generada por IA

Revisar especialmente fidelidad de prenda, color, textura, caída de tela y talle. La IA puede crear nuevas interpretaciones del producto que resultan atractivas pero no representan lo que efectivamente recibirá la compradora. La coherencia visual es crítica para disminuir devoluciones y reclamos.

---

## 6. Catálogo, comercio, creadores y conversiones

### 6.1. Comercio (16 de junio)

Meta informó mayor protagonismo del catálogo de productos en campañas de Ventas y experiencias comerciales, además de formatos de compra en vivo, afiliación, creadores y opciones de checkout. Algunas alianzas regionales incluyeron Brasil y México, lo que **no equivale a habilitación en Argentina**. [S01]

### 6.2. Auditoría de feed

- `id` de producto y variante estable; en prendas diferenciar artículo, color y talle según la estructura elegida.
- Nombre comercial legible: tipo de prenda, modelo, atributo real.
- Precio, moneda y stock iguales a la ficha web.
- Imagen principal fiel al producto y fotos adicionales de uso y detalles.
- Enlace a la ficha correcta, no a una portada genérica.
- Políticas visibles de cambios, envíos y pagos.
- `content_ids` / `contents` de Pixel y CAPI coherentes con el catálogo.
- Grupos de productos por margen, colección o disponibilidad real.

### 6.3. Product browsing

Se reportaron avisos a determinados anunciantes sobre nuevas experiencias de exploración de productos y una posible activación predeterminada futura desde el **28 de octubre**. No se confirmó su aplicación universal a todas las cuentas en la fecha de corte. Acción: inspeccionar las notificaciones y destinos personalizados de la cuenta de Roure antes de asumir impacto. [S15]

---

## 7. Pixel, Conversions API y atribución

### 7.1. Cambios de atribución: atención a la fecha

El anuncio oficial de marzo de 2026 ajustó la definición de atribución por clic para conversiones web y tienda física, haciendo foco en **clics en enlaces**. Otros tipos de interacción pasaron a categorías de atribución de engagement; además se modificó el umbral de visualización de video para esas interacciones. Fue anunciado **antes** de los cuatro meses estudiados, aunque pudo afectar comparaciones realizadas posteriormente. [S13]

Meta también anunció en abril simplificaciones de Pixel y Conversions API; tampoco son novedades originadas en junio-octubre. [S12]

### 7.2. Checklist técnico

1. Registrar `Purchase` **solo** cuando corresponda a una compra confirmada, no cada vez que alguien recarga una página de agradecimiento.
2. Pasar valor económico correcto, `currency: ARS`, ID de pedido y datos de items.
3. Usar el mismo `event_id` entre navegador y servidor para facilitar deduplicación de Pixel/CAPI.
4. Revisar que `content_ids` coincida con los IDs del catálogo.
5. Separar pedidos aprobados, pendientes, cancelados y devueltos.
6. Agregar UTMs persistentes para conciliar campañas con pedidos en la tienda.
7. Comparar Conversiones de Meta con registros comerciales; no exigir equivalencia exacta si usan métodos de atribución distintos.
8. Aplicar prácticas de privacidad y consentimiento necesarias, sin enviar datos sensibles innecesarios.

### 7.3. Advertencia metodológica

Más compras **atribuidas** por Meta no significa necesariamente más compras **incrementales** generadas por Meta. Para decisiones relevantes de presupuesto, contrastar con facturación total, tendencia orgánica y, cuando el volumen lo permita, pruebas de incrementalidad.

---

## 8. Métricas, ROAS y rentabilidad

| Métrica | Fórmula | Utilidad |
|---|---|---|
| ROAS | Ingresos atribuidos ÷ gasto en Meta | Eficiencia atribuida dentro de la plataforma |
| CPA por compra | Gasto en Meta ÷ compras atribuidas | Costo de compra atribuida |
| AOV | Ventas ÷ pedidos | Ticket medio |
| MER | Facturación total ÷ gasto publicitario total | Relación agregada negocio/publicidad |
| Margen de contribución antes de anuncios | Precio menos costos variables no publicitarios | Espacio disponible para adquirir al cliente |
| Contribución posterior a ads | Margen de contribución menos CPA real | Si una venta aporta antes de costos fijos |
| ROAS de equilibrio aproximado | 1 ÷ margen de contribución porcentual | Umbral económico si la atribución coincide con ventas y costos |

### Ejemplo ilustrativo (no datos de Roure)

Un pedido por ARS 40.000 tiene costo de producto ARS 20.000 y ARS 4.000 de otros gastos variables. Su margen de contribución previo a publicidad es ARS 16.000 (**40 %**). El ROAS de equilibrio aproximado es **2,5x**. Si el CPA de compra es ARS 5.500, la contribución posterior a publicidad es ARS 10.500, antes de costos fijos y tributos no incluidos.

**Precaución:** una promoción puede subir el ROAS y al mismo tiempo deteriorar el margen. Por eso el CPA máximo admisible debe calcularse por categoría o grupo de productos, no necesariamente con un valor fijo para toda la tienda.

---

## 9. Asistentes de IA, MCP, Marketing API y gobernanza

El 19 de agosto Meta comunicó funciones para utilizar información empresarial y publicitaria dentro de experiencias de Meta AI con fines de análisis y reportes. En octubre anunció capacidades experimentales para planificar campañas, generar material, explorar audiencias y proponer cambios mediante asistentes, con vistas previas y mecanismos de autorización/aprobación. También describió ampliaciones del servidor MCP de Meta Ads. [S05][S09]

### Buen gobierno para agentes que acceden a anuncios

- Conceder **solo lectura** por defecto; escritura únicamente cuando sea imprescindible.
- Requerir aprobación humana para cambios de presupuesto, activación, publicación, geografía y segmentación.
- Definir límites de inversión por campaña y por período.
- Registrar hora, autor, campaña, versión previa y posterior y razón de cada modificación.
- No compartir tokens ni datos personales por mensajes o archivos abiertos.
- Auditar semanalmente las creatividades y claims generados por IA.

### Marketing API v26.0

Los resúmenes de actualización situaron v26.0 el 29 de julio de 2026 e informaron deprecaciones y cambios de algunos placements/campos. Como algunos changelogs para desarrolladores exigen autenticación, el detalle debe **volver a comprobarse en el panel de Meta for Developers antes de modificar una integración**. [S16][S17]

### Meta One y Muse

Meta One fue anunciado en septiembre con funcionalidades asociadas a suscripciones y condiciones variables. Muse se presentó inicialmente para EE. UU. y Canadá. Ninguno de los dos debe tratarse como una prestación universal ya activa para Roure en Argentina. [S07][S08]

---

## 10. Cambios regulatorios y situación de Argentina

Meta comunicó en octubre acciones específicas de revisión publicitaria para bloquear promociones ilegales vinculadas a explotación infantil. Esa publicación describe un área de seguridad concreta; **no demuestra** un endurecimiento indiscriminado de campañas normales de indumentaria femenina. [S19]

Para un anunciante argentino:

- Revisar el método de pago y la moneda de la cuenta.
- Conciliar factura publicitaria, cargos bancarios, impuestos y tipos de cambio efectivamente aplicados; no asumir una alícuota fija universal.
- Verificar políticas de productos, derechos de imagen y derechos de contenido UGC.
- Mantener personas, permisos, autenticación y verificación comercial al día.
- Inspeccionar las vistas previas de cada anuncio para evitar que mejoras automáticas alteren claims u ofertas.
- Distinguir cambios globales de anuncios de Meta de funcionalidades que sólo operan en mercados seleccionados.

---

## 11. Professor Charley T: análisis de sus métodos de 2026

### 11.1. Identidad, materiales y alcance

Se investigó al especialista conocido públicamente como **Professor Charley T**, identificado como **Charles Tichenor IV** y creador de Disrupter School. Las fuentes son sus propios videos publicados entre junio y octubre, sumarios o transcripciones públicas y datos de sus canales. Sus experiencias y casos comerciales son **afirmaciones del especialista**, no resultados independientemente auditados para la marca Roure. [C01]–[C08]

Su propuesta consiste en pasar de buscar “un anuncio ganador” a construir un sistema de anuncios que desempeñen funciones complementarias, acompañado de presupuestos que aumentan solo cuando el negocio puede sostenerlos.

**Cuidado:** “Andromeda 1” es el nombre de un método de Charley, **no** una versión o lanzamiento oficial de Andromeda por Meta.

### 11.2. Su método “Andromeda 1” (julio de 2026)

En su curso del **18 de julio** propone una arquitectura de hasta **una campaña con tres conjuntos**:

| Elemento | Función según Charley |
|---|---|
| Conjunto de control | Mantiene los anuncios que ya demostraron estabilidad; habitualmente un grupo limitado, con imagen y video |
| Conjunto de prueba A | Introduce una creatividad experimental tipo 3:2:2 |
| Conjunto de prueba B | Permite otro experimento 3:2:2 con una idea concreta |
| Evaluación | Observa si las pruebas reciben distribución, qué anuncios del control pierden inversión y cómo cambia el negocio completo |
| Escalado | Aumenta inversión cuando la contribución del sistema mejora; vuelve a testear si deja de mejorar |

**Matiz importantísimo:** el propio Charley dice que con **presupuesto insuficiente** el control y los tests pueden convivir en **un solo conjunto**. A medida que crece el presupuesto, propone separar gradualmente. Copiar sus tres conjuntos desde el día uno sin volumen puede empeorar la fragmentación que intenta evitar. [C01]

**Qué sí tomar:** línea base estable, pruebas acotadas, revisión del resultado global y disciplina de aprendizaje.

**Qué no tomar literalmente:** que una sola campaña o exactamente tres conjuntos sean óptimos para todos los negocios. El mix de margen, catálogo, regiones y volumen importa.

### 11.3. Formato creativo 3:2:2

El esquema **3:2:2** combina:

- **3 creatividades** —por ejemplo, tres fotografías comparables o tres videos comparables; él recomienda no mezclar ambos tipos dentro de un mismo test.
- **2 textos principales** con enfoques realmente diferentes.
- **2 titulares** con diferentes propuestas de valor.

Eso implica **3 × 2 × 2 = 12 combinaciones posibles**. Charley lo plantea como alternativa a repartir presupuesto entre numerosos anuncios separados. Su implementación concreta depende de las funciones flexibles o multimediales disponibles para el objetivo y la interfaz de Ads Manager. **No implica que Meta publique doce anuncios independientes ni que entregue cada combinación con igual presupuesto.** [C01][C02]

#### Ejemplo 3:2:2 para Roure

**Hipótesis:** mostrar cómo combinar una misma prenda mejora la contribución económica frente a una ficha visual aislada.

| Componente | Variante |
|---|---|
| Creatividad 1 | Foto frontal de outfit completo |
| Creatividad 2 | Foto lateral con caída de la tela |
| Creatividad 3 | Foto usando el conjunto en contexto diario |
| Texto A | Corto: versatilidad y facilidad para combinar |
| Texto B | Más extenso: cómo elegir talla, detalles y ocasión de uso |
| Titular A | “Un look, muchas formas de usarlo” |
| Titular B | “Conocé los nuevos conjuntos de Roure” |

**Buenas prácticas:** mantener la misma propuesta comercial, enlazar a stock real, respetar el producto y revisar las combinaciones antes de publicar.

### 11.4. “Olympic Rings”: cinco funciones creativas

En sus publicaciones de julio y agosto Charley plantea que, para ampliar el mercado, no basta con producir copias de una creatividad de prospección. Su método **Olympic Rings** agrupa **cinco conceptos** interconectados: tres de descubrimiento/prospección y dos de cierre o segundo contacto. [C01][C02]

```text
       R1: Deseo / estilo       R2: Uso / versatilidad      R3: Valor / ocasión
                  \                  |                  /
                   \                 |                 /
                    R4: Prueba / confianza   R5: Objeciones / cierre
```

El esquema es **conceptual**, no una obligación de separar en cinco conjuntos ni un mecanismo garantizado de secuenciación individual. Los anuncios de segundo contacto pueden convivir en campañas más amplias; Meta no asegura que una persona vea los mensajes en un orden determinado.

**Adaptación razonada para Roure:**

| Anillo | Rol | Idea de anuncio |
|---|---|---|
| R1 | Descubrimiento emocional | Outfit completo con una modelo |
| R2 | Versatilidad | Tres maneras de combinar una prenda |
| R3 | Propuesta económica | Conjunto, nuevos ingresos o valor real |
| R4 | Confianza | Tela, medidas y reseña autorizada |
| R5 | Resolver dudas | Cambios, envíos, medios de pago y disponibilidad |

### 11.5. Análisis 4Pi: las cuatro señales

En su publicación del **23 de junio** y el curso de julio, Charley explica un análisis de cuatro indicadores que denomina **4Pi**. Las cuatro señales que él enumera son **gasto, frecuencia, CPM y costo por resultado**; las compara entre anuncios para inferir qué rol cumple cada pieza. [C03][C01]

| Señal | Pregunta relevante | Qué no demuestra por sí sola |
|---|---|---|
| Gasto / participación del gasto | ¿Meta está distribuyendo presupuesto hacia esta pieza? | Que tenga ventas incrementales |
| Frecuencia | ¿Cuántas veces la está viendo la gente alcanzada? | Que haya fatiga por superar un umbral fijo |
| CPM | ¿Qué costo tiene alcanzar esas impresiones? | Que el anuncio sea bueno/malo sin contexto de subasta |
| Costo por resultado | ¿El gasto genera el resultado optimizado eficientemente? | Que sea rentable después de costos variables |

**Lecturas hipotéticas:** una pieza con distribución alta y frecuencia relativamente baja puede actuar como adquisición; una con frecuencia y CPM elevados, pero CPA competitivo, puede estar contribuyendo a cerrar compras; una que recibe inversión y empeora el CPA podría necesitar revisión. Son **señales diagnósticas**, no una manera infalible de identificar qué usuario pertenece a cada etapa del embudo.

**Mi crítica técnica:** el reparto de gasto no ofrece causalidad; la plataforma puede concentrarlo por estimaciones iniciales o por diferencias de oportunidad. Hay que usar 4Pi con muestras significativas y contrastarlo con órdenes, rentabilidad, estacionalidad y resultados agregados. No conviene apagar un anuncio únicamente porque recibió poco gasto tras un período corto.

### 11.6. Profit Volume y GPT: la idea más valiosa, con una corrección contable

Charley critica evaluar campañas exclusivamente por **ROAS**. En su curso usa expresiones como **Profit Volume** y una métrica que llama **GPT (gross profit per transaction)**, ilustrándolas frecuentemente con **ingresos atribuidos menos gasto publicitario**. Esa operación puede ayudar a comparar eficiencia publicitaria, pero **no equivale al beneficio bruto contable ni a la contribución real** si no descuenta el costo de mercadería, comisiones, logística y otras variables. [C01][C05]

Para Roure proponemos reemplazar el atajo por:

```text
Contribución después de publicidad
= Ventas netas cobradas
- Costo de mercadería vendida
- Comisiones de cobro
- Costo variable logístico asumido por la marca
- Descuentos y devoluciones atribuibles
- Inversión publicitaria
```

**Ejemplo con números hipotéticos:**

| Anuncio | Pedido medio | CPA | ROAS | Ingreso menos CPA | Si otros costos son 65% del pedido, contribución tras CPA |
|---|---:|---:|---:|---:|---:|
| A | $40.000 | $10.000 | 4,0x | $30.000 | $4.000 |
| B | $120.000 | $60.000 | 2,0x | $60.000 | -$18.000 |

Este ejemplo muestra por qué el criterio “ingreso menos CPA” podría favorecer un anuncio B que destruye margen, aun cuando su cifra aparente es mayor. La prioridad es medir **valor económico real**, no elegir una ratio ni una resta parcial de manera aislada.

### 11.7. Cómo escalar: lineal, porcentual y marginal

En material del período Charley describe tres vías de escalado [C01][C04]:

1. **Lineal:** agregar un importe fijo al presupuesto periódicamente cuando el sistema es estable.
2. **Fraccional o porcentual:** aumentar un porcentaje periódico; crece más rápido y puede introducir volatilidad.
3. **Marginal:** incrementar solo cuando CPA, margen y rendimiento reciente justifican ampliar el gasto.

En ejemplos públicos menciona incrementos pequeños, como un importe diario fijo o un porcentaje reducido. **No debe interpretarse como una orden de incrementar un determinado 2 %, 10 % o 20 % a diario:** el ritmo admisible depende de presupuesto, variabilidad, stock y margen. Una regla automática que usa un CPA atribuido defectuoso puede escalar pérdidas.

### 11.8. Lifetime value, retención y “revenue floor”

En un video publicado el **21 de septiembre**, Charley insiste en observar el valor de los clientes después de la primera compra y el peso de los ingresos provenientes de compradores recurrentes. Su idea de *revenue floor* apunta a una base recurrente que sostiene el negocio aun cuando varíe la adquisición. [C05]

Para Roure puede medirse con:

- Porcentaje de facturación neta procedente de clientas existentes.
- Recompra a 30, 60, 90 y 180 días.
- Margen de la primera compra frente al margen acumulado por cohorte.
- Productos de primera compra asociados a mejores tasas futuras de recompra.
- CAC de clienta nueva frente a costo de reactivación.

**Advertencia:** no todo ROAS alto significa baja lealtad. Es un riesgo plausible si solo se optimizan compras fáciles de clientas que ya habrían comprado; hay que demostrarlo con datos de cohortes e incrementalidad.

### 11.9. Ideas nuevas de octubre

En publicaciones del **6 y 14 de octubre**, Charley enfatiza no convertir Black Friday en una carrera de descuentos indiscriminados y pensar el escalado como un sistema comercial que conecta ofertas, adquisición y futuras ventas. El video del 14 de octubre menciona un modelo de **dos campañas y un flywheel**. Esto muestra que sus estructuras son **métodos tácticos que él mismo actualiza**, no leyes permanentes de Andromeda. La documentación pública recuperada del video de octubre contiene su temario; no permite auditar cada detalle de implementación. [C06][C07]

**Aplicación para Roure en eventos promocionales:** diseñar descuentos sobre margen conocido, separar productos de atracción de productos rentables, validar stock y medir la calidad de las nuevas clientas; no perseguir ingresos altos sacrificando contribución.

### 11.10. Matriz crítica: ¿qué adoptar de Charley?

| Recomendación de Charley | Evaluación | Decisión sugerida para Roure |
|---|---|---|
| Menos fragmentación | Consistente con buena asignación de señales, pero depende del volumen | **Adoptar como principio, no como regla absoluta** |
| Control + pruebas acotadas | Ordena la experimentación | **Adoptar cuando haya anuncios de control confiables** |
| 3:2:2 | Framework útil para testear insumos creativos | **Probar** si la funcionalidad de Meta está disponible |
| Tres anillos para captar + dos para cerrar | Ayuda a pensar en funciones distintas | **Adoptar la lógica narrativa**, sin imponer cinco conjuntos |
| 4Pi | Diagnóstico práctico de la distribución | **Usarlo junto a margen y compras reales**, no como ranking definitivo |
| “ROAS no es rentabilidad” | Correcto conceptualmente | **Adoptar y perfeccionar el cálculo contable** |
| Escalar cuando crece el valor real | Orientación sólida | **Adoptar** con contribución después de costos variables |
| Un número preciso de anuncios/conjuntos | No está demostrado como óptimo universal | **No copiar ciegamente** |
| Dejar que Meta se ocupe de todo | Automatizar no sustituye control de calidad | **Exigir QA y límites** |

---

## 12. Roure: estrategia recomendada

### 12.1. Objetivo comercial

Roure comercializa indumentaria femenina juvenil. El objetivo declarado de esta investigación es **vender más, bajar CPA y escalar sin sacrificar rentabilidad**. Para eso, evitaría reconstrucciones masivas de campaña sin datos de compras confirmadas.

### 12.2. Qué medir antes de tocar Ads Manager

1. Ingresos efectivamente pagados por semana y por categoría.
2. Costo variable por artículo/conjunto, comisión y logística.
3. Ticket medio por pedido, proporción de compras de clientas nuevas y recurrentes.
4. CPA de adquisición de nuevas clientas y contribución por pedido.
5. Eventos, catálogo, stocks, fichas, tasa de compra de la tienda.
6. Creatividades agrupadas por *mensaje* y *formato*, con fecha de lanzamiento y gasto.

### 12.3. Prioridades visuales

- **Control de calidad:** imágenes de prendas sin cambios de color, textura o detalles.
- **Oferta legible:** producto, talles y precio final accesibles.
- **Pruebas narrativas:** deseo, versatilidad, valor, prueba social y resolución de dudas.
- **Destino correcto:** ficha con stock real y proceso de compra sencillo.
- **Realidad de entrega:** no prometer stock, cambio o plazo que no pueda cumplirse.

### 12.4. Ejemplo de estructura basada en principios de Charley (solo hipótesis)

**Escenario A — presupuesto limitado, pocas compras:** una campaña y un conjunto con anuncios estables y nuevas pruebas controladas dentro de él. Evitar crear conjuntos adicionales solo para replicar el esquema de un especialista.

**Escenario B — volumen suficiente y creatividades probadas:** una campaña con conjunto de control y uno de pruebas. Segundo conjunto de pruebas únicamente si el presupuesto y frecuencia de experimentación lo permiten.

**Escenario C — retail y mayorista mezclados:** valorar campañas separadas por economías realmente distintas. La lógica de un solo embudo puede deteriorar la medición cuando cambia drásticamente el ticket, el proceso comercial o los márgenes.

---

## 13. Experimentos, tablero y plan de 90 días

### 13.1. Calendario de implementación

| Fase | Días | Acciones prioritarias | Evidencia de éxito |
|---|---:|---|---|
| Auditoría | 1–14 | Pedidos, costos, Pixel/CAPI, catálogo, estructura, anuncios, stock | CPA máximo calculado y medición coherente |
| Creatividad | 15–30 | Probar conceptos con producto/oferta comparables y variantes 3:2:2 si corresponde | Compras válidas y contribución, no solo clics |
| Optimización | 31–60 | Iterar 2–3 conceptos prometedores, revisar destinos y escalar gradualmente | Margen incremental no negativo |
| Sistema | 61–90 | Cohortes, repetición de compra, inventario, documentación de experimentos y automatización controlada | Facturación, recompra y contribución estables |

### 13.2. Ocho ideas concretas para pruebas creativas

1. Reel de outfit completo con precio y CTA.
2. Video de la prenda en movimiento para mostrar caída y calce.
3. Detalles de tela y terminaciones en plano cercano.
4. Carrusel comparando combinación individual y conjunto real.
5. Novedades en tres piezas con enlace a productos correctos.
6. Testimonio autorizado de una compradora genuina.
7. La misma prenda estilizada para distintas ocasiones.
8. Respuesta visual a dudas sobre talles, cambios y entrega.

**Regla de prueba:** si querés medir qué *concepto* vende mejor, no cambies simultáneamente el precio, la landing, la segmentación, el formato y el producto. Cuando no haya un A/B real aleatorizado, informá el resultado como una observación, no como causalidad probada.

### 13.3. Tablero semanal

| KPI | Fuente | Frecuencia de lectura | Decisión |
|---|---|---|---|
| Pedidos pagados / devoluciones | Tienda y facturación | Semanal | Verificar ventas reales |
| Inversión Meta y total | Factura + Ads Manager | Semanal | Control presupuestario |
| ROAS, CPA, MER y contribución | Meta + datos propios | 7, 14 y 28 días | Escalado / recorte |
| Gasto, CPM, frecuencia y CPA por anuncio (4Pi) | Ads Manager | Semanal, según volumen | Diagnóstico creativo |
| CTR de enlace, CPC de enlace, CVR | Ads Manager + analítica web | Semanal | Separar problema anuncio vs. sitio |
| Ventas y margen por producto/variante | ERP o planilla | Semanal | Selección de artículos |
| Recompra por cohorte | Pedidos/clientes | Mensual | Calidad de adquisición |

### 13.4. Protocolo de experimentos

Para cada hipótesis registrar: fecha, nombre, decisión comercial buscada, cambio realizado, campaña/conjunto, inversión, volumen esperado, ventana de evaluación, metricas primarias, variables de control, resultado y siguiente acción. Una prueba sin volumen suficiente debe terminar como **inconclusa** cuando corresponda, y no como “ganadora” o “perdedora”.

---

## 14. Mitos, controversias y evaluación de evidencia

| Afirmación | Evaluación |
|---|---|
| “Andromeda salió hace cuatro meses” | **Falso.** Anunciado en 2024. [S14] |
| “GEM garantiza +18,9 % de ventas a Roure” | **No.** Es una cifra de Meta en contextos agregados. [S10] |
| “Meta exige al menos 20–50 anuncios” | **No demostrado** como obligación general. [S18] |
| “Professor Charley T descubrió Andromeda 1.0 de Meta” | **Impreciso.** “Andromeda 1” es una metodología del profesor, no un lanzamiento oficial. [C01] |
| “3:2:2 es obligatorio y siempre gana” | **No demostrado.** Es un método de experimentación. [C01][C02] |
| “El mejor ROAS es siempre el mejor anuncio” | **Falso como regla económica.** Margen y volumen importan. |
| “Ingresos menos ads es ganancia neta” | **Falso.** Faltan costos variables y fijos. |
| “Frecuencia alta siempre significa fatiga” | **Falso.** Depende de etapa, oferta, CPA y tendencias. |
| “Todas las exclusiones manuales desaparecieron en agosto” | **Exagerado.** Hubo pruebas y cambios según objetivos/cuentas. [S06] |
| “Meta AI modifica presupuestos automáticamente en todas las cuentas” | **Falso.** Capacidades anunciadas como pruebas y controles. [S09] |
| “La redefinición de click-through fue anunciada en octubre” | **Fecha incorrecta.** Meta la anunció en marzo. [S13] |
| “Toda Argentina tiene Muse y Meta One del mismo modo” | **No confirmado.** Elegibilidad regional variable. [S07][S08] |
| “El cambio de ROAS de octubre se debe necesariamente a GEM” | **No demostrado.** Correlación temporal no prueba causalidad. |

### Síntesis estratégica

La mayor ventaja competitiva de Roure no será acertar una cantidad secreta de campañas, conjuntos o creatividades. Será mantener **producto real + oferta rentable + señales de compra confiables + conceptos creativos diferenciados + seguimiento del margen**.

Los marcos de Charley son una capa útil para el trabajo cotidiano: control de campañas, diseño de un equipo de anuncios, 3:2:2, 4Pi y escalado por beneficio. Deben integrarse con la contabilidad y pedidos reales de Roure, no reemplazarlos.

---

## 15. Fuentes y videos originales

### 15.1. Fuentes oficiales, técnicas e independientes utilizadas en el informe original

- **[S01]** Meta, 16 jun. 2026, comercio y datos de catálogo: https://about.fb.com/ltam/news/2026/06/cannes-2026-nuevas-formas-de-convertir-el-descubrimiento-en-compra/amp/
- **[S02]** Meta, 23 jun. 2026, IA creativa y creadores: https://about.fb.com/ltam/news/2026/06/cannes-lions-2026-nuevas-herramientas-creativas-y-para-creadores-que-facilitan-el-salto-hacia-la-ia/
- **[S03]** Meta Engineering, 15 jul. 2026, Hierarchical Interest Representation: https://engineering.fb.com/2026/07/15/ai-research/exploring-hierarchical-interest-representation-for-meta-ads-deep-funnel-optimization/
- **[S04]** Meta Engineering, 13 jul. 2026, infraestructura publicitaria: https://engineering.fb.com/2026/07/13/ml-applications/modernizing-the-meta-ads-service-with-an-open-source-kernel-scheduler/
- **[S05]** Meta, 19 ago. 2026, nuevas funciones de Meta AI: https://about.fb.com/ltam/news/2026/08/nuevas-funciones-de-meta-ai-para-pequenas-empresas/
- **[S06]** Jon Loomer, 20 ago. 2026, controles de ubicaciones: https://www.jonloomer.com/meta-removing-placement-controls-ad-sets/
- **[S07]** Meta, 15 sep. 2026, Meta One: https://about.fb.com/ltam/news/2026/09/presentamos-meta-one-un-servicio-de-suscripcion-con-mas-funciones-e-ia-para-crear-conectar-y-destacar/
- **[S08]** Meta, 29 sep. 2026, Muse Small Business: https://about.fb.com/news/2026/09/introducing-muse-small-business
- **[S09]** Meta, 6 oct. 2026, Advertising Week y herramientas IA: https://about.fb.com/ltam/news/2026/10/advertising-week-new-york-2026-nuevas-capacidades-de-ia-para-guiar-campanas-y-llegar-a-los-clientes/
- **[S10]** Meta Engineering, 13 oct. 2026, GEM: https://engineering.fb.com/2026/10/13/ml-applications/generative-ads-model-gem-scaling-frontier-ads-ai/
- **[S11]** Meta, 13 oct. 2026, Your Algorithm (contexto orgánico): https://about.fb.com/news/2026/10/introducing-your-algorithm-facebook/
- **[S12]** Meta, 15 abr. 2026, Pixel/CAPI (antecedente): https://about.fb.com/ltam/news/2026/04/eliminar-barreras-tecnicas-para-ayudar-a-empresas-de-todos-los-tamanos-a-aprovechar-mas-sus-anuncios/
- **[S13]** Meta, 3 mar. 2026, atribución (antecedente): https://about.fb.com/ltam/news/2026/03/simplificando-la-medicion-de-anuncios-para-un-mundo-social-first/
- **[S14]** Meta Engineering, 2 dic. 2024, Andromeda original: https://engineering.fb.com/2024/12/02/production-engineering/meta-andromeda-advantage-automation-next-gen-personalized-ads-retrieval-engine/
- **[S15]** Ads Uploader, cronología no oficial de cambios: https://adsuploader.com/blog/meta-ads-updates
- **[S16]** Ads Uploader, archivo junio-julio: https://adsuploader.com/es/blog/meta-ads-updates-2026
- **[S17]** AdAdvisor, seguimiento independiente 2026: https://adadvisor.ai/blog/meta-ads-updates-2026
- **[S18]** Jon Loomer, 20 oct. 2025, diversidad creativa (antecedente): https://www.jonloomer.com/meta-andromeda-creative-diversification/
- **[S19]** Meta, 7 oct. 2026, revisión y seguridad publicitaria: https://about.fb.com/news/2026/10/measures-weve-put-in-place-to-fight-child-exploitation/
- **[S20]** Meta, 9 jun. 2026, actividad de otros negocios (antecedente): https://about.fb.com/ltam/news/2026/06/mejor-personalizacion-y-cambios-en-los-controles-de-tu-actividad-de-otros-negocios/
- **[S21]** Meta, 3 jun. 2026, agente empresarial (antecedente): https://about.fb.com/news/2026/06/meta-business-agent
- **[S22]** Meta, 4 jun. 2025, herramientas de valor e incrementalidad (antecedente): https://about.fb.com/ltam/news/2025/06/obten-mas-de-tus-conversiones-presentando-nuevas-herramientas-para-optimizar-lo-que-mas-valora-tu-negocio/
- **[S23]** Meta, 26 mar. 2026, Shoptalk (antecedente): https://about.fb.com/ltam/news/2026/03/del-comercio-a-la-cultura-como-la-ia-impulsa-la-conexion-personalizada-y-el-crecimiento-a-lo-largo-del-funnel/
- **[S24]** Reddit, testimonios de volatilidad (anecdótico, no causal): https://www.reddit.com/r/FacebookAds/comments/1x47zlo/for_advertisers_barely_doing_1_roas_for_since/
- **[S25]** Estado operativo de Meta, contexto de incidencias: https://metastatus.com/

### 15.2. Profesor Charley T: publicaciones del período analizado

- **[C01]** 18 jul. 2026 — *New BEST 2026 Meta Ads Course After Andromeda*: https://www.youtube.com/watch?v=s6PyrJpBJwA ; transcripción con tiempos: https://youtube2text.diguardia.org/v/new-best-2026-meta-ads-course-after-andromeda-s6PyrJpBJwA
- **[C02]** 10 ago. 2026 — *Copy This Simple Meta Ads Strategy, It'll Blow Up Your Business*: https://www.youtube.com/watch?v=4DutxlMzqgc ; descripción fechada: https://zolotube.com/watch?v=4DutxlMzqgc
- **[C03]** 23 jun. 2026 — *The NEW BEST Way to Analyze Facebook Ads in 2026 (4Pi after Andromeda)*: https://www.youtube.com/watch?v=yMsy5O1af2g ; descripción: https://zolotube.com/watch?v=yMsy5O1af2g
- **[C04]** 14 sep. 2026 — *The NEW BEST Way To Scale Facebook Ads*: https://www.youtube.com/watch?v=yJS_tqi642Y ; descripción: https://zolotube.com/watch?v=yJS_tqi642Y
- **[C05]** 21 sep. 2026 — *This Facebook Ads Lie is Killing Your Business!*: https://www.youtube.com/watch?v=42YQvNrr4gI ; resumen temático: https://glasp.co/youtube/42YQvNrr4gI
- **[C06]** 6 oct. 2026 — *Your Black Friday Facebook Ads Strategy Sucks*: https://www.youtube.com/watch?v=6G3g-HZ2E_I ; descripción fechada: https://zolotube.com/watch?v=6G3g-HZ2E_I
- **[C07]** 14 oct. 2026 — *How to Scale Facebook Ads SO FAST It Feels Like CHEATING*: https://www.youtube.com/watch?v=ZfsuUCHVI4U ; descripción y temario: https://zolotube.com/watch?v=ZfsuUCHVI4U
- **[C08]** Canal principal de Professor Charley T: https://www.youtube.com/@CTtheDisrupter

**Notas sobre las fuentes del profesor:** [C01] dispone de transcripción pública extensa; otros materiales fueron verificados mediante títulos, fechas, descripciones y resúmenes accesibles. Las explicaciones aquí son paráfrasis analíticas, **no** reproducción de sus cursos ni transcripción completa. Los títulos de los videos pueden contener lenguaje promocional y no deben confundirse con pruebas experimentales auditadas.

---

*Fin del informe. Fecha de corte de investigación: 16 de octubre de 2026. Elaborado para uso estratégico y evaluación, no como garantía de resultados publicitarios.*
