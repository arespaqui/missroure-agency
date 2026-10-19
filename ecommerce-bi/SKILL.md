---
name: ecommerce-bi
description: "Genera informes de Business Intelligence para eCommerce a partir de un CSV de ventas de Miss Roure. Auto-detecta plataforma (Tiendanube, Shopify, WooCommerce, o genérico para Tienda Negocio) y produce 21 (Lite), 39 (Full) o análisis individuales: Market Basket, RFM, cohortes, CLV, cross-sell, churn, producto gateway de retención, estacionalidad, forecast y más. Output: JSON estructurado + informe HTML branded. Usar cuando el usuario mencione 'business intelligence', 'BI', 'análisis de ventas', 'market basket', 'RFM', 'cohortes', 'CLV', 'lifetime value', 'cross-sell', 'basket analysis', 'afinidad de productos', 'análisis ecommerce', 'informe de ventas', 'análisis de clientes', 'qué producto retiene mejor', 'quiénes son mis clientas VIP', 'quién está por perderse'."
---

# eCommerce Business Intelligence Skill — Miss Roure

> Adaptado de [mathiaschu/ecommerce-bi](https://github.com/mathiaschu/ecommerce-bi) (MIT license) para el contexto de Miss Roure.

Genera informes de Business Intelligence a partir de un CSV de órdenes de eCommerce. Detecta automáticamente la plataforma, normaliza columnas y corre desde **un análisis individual** hasta **39 análisis completos**, en 6 categorías (Producto, Cliente, Revenue, Geográfico, Operativo, Estratégico).

Puede correr en tres modos: **Lite** (21 análisis core), **Full** (39 análisis completos) o **Individual** (uno o varios análisis específicos).

---

## ⚠️ Nota de plataforma — Miss Roure usa Tienda Negocio

El script auto-detecta **Tiendanube, Shopify o WooCommerce** por headers de columna. **Tienda Negocio (roure.tiendanegocio.com) no está en esa lista** — no hay fingerprint dedicado.

Antes de correr cualquier análisis:

1. Pedir el export de órdenes de Tienda Negocio.
2. Revisar sus headers contra las columnas canónicas de `references/csv_mapping.md` (sección "Columnas Canonicas").
3. Si los headers no matchean directamente, renombrar columnas al mapeo genérico o crear un `custom_mapping.json` (ver sección "Fallback si no se detecta plataforma" en `references/csv_mapping.md`).
4. Mínimo indispensable para que el análisis sirva: `order_id`, `date`, `total`, `product_name`. Sumar `email` para desbloquear RFM/CLV/cohortes/churn (ver `references/required_columns.md`).

Si Tienda Negocio no permite exportar CSV de órdenes de forma nativa, avisar al usuario — puede necesitar pedirlo por soporte de la plataforma o armarlo manualmente desde el panel de pedidos.

---

## Análisis disponibles

Los 39 análisis que puede generar la skill, ordenados de mayor a menor impacto típico al negocio. Cada uno se puede correr individualmente o como parte de los modos Lite / Full.

Formato de cada bloque:
- **Qué hace**: la mecánica.
- **Para qué sirve**: la decisión que habilita.
- **Necesita**: columnas mínimas en el CSV.
- **ID + modo**: el ID interno del script (para `--analysis N`) y en qué modos aparece.

---

### 1. Segmentación RFM
- **Qué hace**: clasifica a cada cliente en uno de 11 segmentos según Recency (cuándo compró por última vez), Frequency (cuántas veces) y Monetary (cuánto gastó). Segmentos: Champions, Loyal, Potential Loyal, New, Promising, Need Attention, About to Sleep, At Risk, Can't Lose, Hibernating, Lost.
- **Para qué sirve**: es la base de toda estrategia de CRM y email. A quién mimar (Champions, Loyal), a quién reactivar (At Risk, About to Sleep), a quién dar bienvenida (New) y a quién dejar de gastar pauta (Lost). Sin RFM, mandás los mismos mails a todo el mundo.
- **Necesita**: `email`, `date`, `total`
- **ID interno**: #7 · Lite + Full

### 2. Ranking de productos
- **Qué hace**: ordena el catálogo por revenue, unidades vendidas y tendencia (últimos 3 meses vs 3 anteriores). Identifica héroes y estrellas emergentes.
- **Para qué sirve**: te dice qué *es* tu negocio. De acá salen las decisiones de qué destacar en home, qué pautar, qué reabastecer prioritariamente y dónde concentrar el esfuerzo creativo. Cruzar contra "Productos Estrella" de `context/catalog-context.md`.
- **Necesita**: `product_name`, `product_price`, `product_qty`, `date`
- **ID interno**: #3 · Lite + Full

### 3. Análisis de cohortes (retención)
- **Qué hace**: matriz mensual de retención (últimas 12 cohortes × 12 meses). Para cada grupo de clientes adquiridos en un mes, qué porcentaje sigue comprando 1, 2, 3 meses después.
- **Para qué sirve**: te dice si el negocio realmente *funciona*. Si la retención cae a cero al M1, cada cliente nuevo es un gasto. Si la cohorte nueva retiene peor que la vieja, algo se está rompiendo.
- **Necesita**: `email`, `date`
- **ID interno**: #9 · Lite + Full

### 4. Customer Lifetime Value (CLV)
- **Qué hace**: estima el CLV a 3 años por cliente (AOV × frecuencia × lifespan). Reporta promedio, mediana, cuartiles y top 10.
- **Para qué sirve**: establece tu techo de CAC. Si un cliente vale $100.000 en 3 años, no podés pagar $80.000 para adquirirlo (comparar contra CPA Máximo de `meta-ads-analyst.md`).
- **Necesita**: `email`, `date`, `total`
- **ID interno**: #8 · Lite + Full

### 5. Evolución mensual de revenue
- **Qué hace**: serie mensual de revenue, órdenes y AOV. Calcula tendencia y detecta picos/valles.
- **Para qué sirve**: es la línea de base. Toda lectura de las demás métricas se contextualiza contra esta tendencia.
- **Necesita**: `date`, `total`
- **ID interno**: #11 · Lite + Full

### 6. Tasa de recompra
- **Qué hace**: porcentaje de clientes que compraron más de una vez y tiempo medio entre compras (mediana y promedio).
- **Para qué sirve**: health metric esencial. Si la recompra es &lt;20%, sos un negocio de adquisición pura. Si es &gt;40%, podés invertir más en retención. La mediana entre compras le da el ritmo a las reglas de email de `ecommerce-specialist.md`.
- **Necesita**: `email`, `date`
- **ID interno**: #10 · Lite + Full

### 7. Producto gateway de retención
- **Qué hace**: para cada producto, calcula qué porcentaje de los clientes que lo tuvieron como su *primera* compra volvieron a comprar al menos una vez más. Filtra por muestra mínima estadísticamente razonable y compara cada producto contra el baseline global de recompra.
- **Para qué sirve**: te dice qué meter primero en pauta. No el producto que más vende, sino el que mejor *captura* clientes que vuelven — distinto a "Productos Estrella" (que es solo por revenue/stock). Decisión clave para definir hero products en home y campañas de adquisición (`meta-ads-strategist.md`).
- **Necesita**: `email`, `date`, `product_name`
- **ID interno**: #39 · Lite + Full

### 8. Productos ancla (gateway de carrito)
- **Qué hace**: identifica los productos que más aparecen en órdenes multi-producto. Para cada ancla, lista los 5 co-productos más frecuentes.
- **Para qué sirve**: son los productos gateway *de carrito* (distintos al gateway de retención): abren la primera compra y arrastran otros productos a la misma orden. Insumo directo para `AOV Bundles` en `ecommerce-specialist.md`.
- **Necesita**: `order_id`, `product_name`
- **ID interno**: #4 · Lite + Full

### 9. Market Basket Analysis
- **Qué hace**: identifica qué productos se compran juntos. Calcula pares y tríos con support (frecuencia), confidence (probabilidad condicional) y lift (cuánto más probable que por azar).
- **Para qué sirve**: cross-sell directo, bundles, recomendaciones en PDP, módulos "compraron junto". Cualquier combo con lift &gt; 2 es una oportunidad de revenue incremental — insumo para definir nuevos combos tipo "Cozy Coquette" en `ecommerce-specialist.md`.
- **Necesita**: `order_id`, `product_name`
- **ID interno**: #1 · Lite + Full

### 10. Oportunidades de bundling
- **Qué hace**: filtra los combos del Market Basket con mejor lift y propone bundles concretos con precio combinado.
- **Para qué sirve**: cierra el bucle del análisis en una acción concreta, alineado a la lógica de AOV Bundles ($80.000 ARS threshold de envío gratis) que ya usa Roure.
- **Necesita**: `order_id`, `product_name`, `product_price`
- **ID interno**: #19 · Lite + Full

### 11. Clientes VIP (top 10%)
- **Qué hace**: identifica el top 10% de clientes por revenue. Reporta su AOV, frecuencia, productos preferidos y mes de adquisición.
- **Para qué sirve**: el VIP suele hacer 40-60% del revenue total. Saber quiénes son habilita programas VIP, ofertas tempranas, acceso anticipado y customer service diferenciado.
- **Necesita**: `email`, `total`, `product_name`
- **ID interno**: #26 · Full only

### 12. Análisis de churn
- **Qué hace**: identifica clientes que dejaron de comprar (sin actividad por más del doble de su intervalo medio). Reporta cuáles, su valor histórico y los últimos productos comprados antes del churn.
- **Para qué sirve**: detección temprana de fuga. Los últimos productos comprados antes del churn muchas veces revelan problemas de calidad o experiencia. Habilita campañas de reactivación con oferta dirigida (Campaña 4 — Retención en `meta-ads-strategist.md`).
- **Necesita**: `email`, `date`, `total` (idealmente ≥6 meses de histórico)
- **ID interno**: #27 · Full only

### 13. Estacionalidad
- **Qué hace**: detecta picos y valles por mes y por día de la semana. Identifica mes pico, mes valle y día más fuerte.
- **Para qué sirve**: planificación anual de pauta y stock — contrastar contra el calendario estacional ya definido en `meta-ads-strategist.md` (otoño-invierno = tapados/sweaters, etc.).
- **Necesita**: `date`, `total`
- **ID interno**: #20 · Lite + Full

### 14. Long tail 80/20
- **Qué hace**: cuántos SKUs hacen el 80% del revenue. Distribución Pareto del catálogo.
- **Para qué sirve**: decisiones de stock e inversión. Si el 10% de los SKUs hace el 80%, el resto puede ser candidato a descatalogar, liquidar o pasar a print-on-demand.
- **Necesita**: `product_name`, `product_price`, `product_qty`
- **ID interno**: #5 · Lite + Full

### 15. Ticket promedio (AOV)
- **Qué hace**: AOV global, AOV mediano, distribución por tramo y evolución mensual. Compara AOV de clientes nuevos vs recurrentes.
- **Para qué sirve**: KPI core — comparar contra el objetivo Roure de $80.000 ARS (umbral de envío gratis) ya definido en `ecommerce-specialist.md` y `meta-ads-strategist.md`.
- **Necesita**: `total`
- **ID interno**: #12 · Lite + Full

### 16. Revenue por categoría
- **Qué hace**: mix de revenue por categoría (extraída del nombre del producto). Top N categorías + % de mix.
- **Para qué sirve**: balance del catálogo. Si una categoría concentra 70%, hay riesgo de dependencia. Si todas reparten parejo, oportunidad de empujar una para crecer.
- **Necesita**: `product_name`, `product_price`, `product_qty`
- **ID interno**: #13 · Lite + Full

### 17. Impacto de descuentos
- **Qué hace**: AOV con cupón vs sin cupón, % de órdenes con descuento, top cupones usados, monto total descontado.
- **Para qué sirve**: medir si el 20% OFF por transferencia (u otros descuentos activos) *agrega* valor o *canibaliza* margen.
- **Necesita**: `total`, `discount` (idealmente `coupon`)
- **ID interno**: #14 · Lite + Full

### 18. Afinidad entre categorías
- **Qué hace**: market basket pero a nivel categoría: qué categorías se combinan en la misma orden.
- **Para qué sirve**: cross-merchandising en home y landings. Categorías afines son material para colecciones combinadas y carruseles "outfit completo".
- **Necesita**: `order_id`, `product_name`
- **ID interno**: #2 · Lite + Full

### 19. Recomendaciones de cross-sell
- **Qué hace**: para cada producto top, qué otro recomendar (basado en lift y co-ocurrencia).
- **Para qué sirve**: tabla lista para alimentar recomendaciones en la tienda, derivada del dato real.
- **Necesita**: `order_id`, `product_name`
- **ID interno**: #36 · Full only

### 20. Análisis de pricing
- **Qué hace**: identifica productos sobre-precio o sub-precio comparados con el promedio de su categoría.
- **Para qué sirve**: detecta candidatos a ajuste de precio.
- **Necesita**: `product_name`, `product_price`
- **ID interno**: #37 · Full only

### 21. Análisis de precio (distribución)
- **Qué hace**: histograma de precios y unidades vendidas por tramo. Identifica price points con mejor performance.
- **Para qué sirve**: encontrar el sweet spot del catálogo para curar futuras colecciones.
- **Necesita**: `product_price`, `product_qty`
- **ID interno**: #29 · Full only

### 22. Heatmap por provincia
- **Qué hace**: revenue, órdenes y AOV por provincia/estado.
- **Para qué sirve**: decisiones de pauta geo (Roure ya prioriza CABA + GBA en `meta-ads-audience.md`) — validar con datos reales si esa priorización sigue siendo correcta.
- **Necesita**: `state`, `total`
- **ID interno**: #15 · Lite + Full

### 23. Costo de envío vs conversión
- **Qué hace**: distribución del costo de envío por tramo y correlación con cancelación.
- **Para qué sirve**: el envío es uno de los principales drivers de abandono. Valida si el umbral de envío gratis de $80.000 ARS está bien calibrado.
- **Necesita**: `shipping_cost`, `order_status`
- **ID interno**: #16 · Lite + Full

### 24. Penetración por ciudad
- **Qué hace**: top ciudades por revenue, AOV y órdenes (granularidad más fina que provincia).
- **Para qué sirve**: pauta geográfica fina, patrones de concentración urbana.
- **Necesita**: `city`, `total`
- **ID interno**: #30 · Full only

### 25. Eficiencia de envío gratis
- **Qué hace**: compara AOV y conversión de órdenes con envío gratis vs con envío pago.
- **Para qué sirve**: evaluar si el umbral de $80.000 ARS de `ecommerce-specialist.md` está empujando AOV o si conviene ajustarlo.
- **Necesita**: `shipping_cost`, `total`
- **ID interno**: #34 · Full only

### 26. Tiempo de fulfillment
- **Qué hace**: días entre orden y despacho. Distribución, mediana y outliers.
- **Para qué sirve**: SLA operativo. Si la mediana sube mes a mes, hay un problema de logística por venir.
- **Necesita**: `date`, `shipping_date`
- **ID interno**: #32 · Full only

### 27. Tasa de cancelación
- **Qué hace**: % global de canceladas, top motivos de cancelación, evolución mensual, mix por medio de pago.
- **Para qué sirve**: health metric operativo. Tendencia ascendente = problema (stock, pricing, expectativa).
- **Necesita**: `order_status`
- **ID interno**: #17 · Lite + Full

### 28. Productos con alta cancelación
- **Qué hace**: identifica productos con tasa de cancelación significativamente sobre la media.
- **Para qué sirve**: detectar productos problemáticos (calidad, stock, expectativa vs realidad).
- **Necesita**: `product_name`, `order_status`
- **ID interno**: #6 · Lite + Full

### 29. Mix de medios de pago
- **Qué hace**: distribución de órdenes y revenue por medio de pago.
- **Para qué sirve**: relevante en Roure porque el 20% OFF por transferencia es el driver de conversión principal — medir cuánto realmente se usa.
- **Necesita**: `payment_method`, `total`
- **ID interno**: #18 · Lite + Full

### 30. Medio de envío por zona
- **Qué hace**: mix de shipping methods por provincia.
- **Para qué sirve**: detectar dónde la oferta de envíos está incompleta.
- **Necesita**: `state`, `shipping_method`
- **ID interno**: #31 · Full only

### 31. Forecast de ventas
- **Qué hace**: proyección de revenue a 3 meses con ajuste estacional (mínimo 6 meses de histórico).
- **Para qué sirve**: planificación financiera y de stock para temporada alta (invierno/Hot Sale/Navidad).
- **Necesita**: `date`, `total`
- **ID interno**: #35 · Full only

### 32. Identificación de nichos
- **Qué hace**: clusters de productos con alta afinidad interna y bajo overlap entre sí.
- **Para qué sirve**: detectar sub-líneas implícitas dentro del catálogo (ej. Paris Collection, Douceur Trendy).
- **Necesita**: `order_id`, `product_name`
- **ID interno**: #38 · Full only

### 33. Patrón de upgrade
- **Qué hace**: detecta si los clientes aumentan su AOV en compras sucesivas.
- **Para qué sirve**: si el AOV crece, el storytelling de marca funciona y se puede empujar premium (Tapados, Paris Collection).
- **Necesita**: `email`, `date`, `total`
- **ID interno**: #25 · Full only

### 34. Análisis de SKU/variantes
- **Qué hace**: performance por variante (color, talle, SKU). Detecta variantes muertas y heroínas.
- **Para qué sirve**: discontinuar lo que no rota, reforzar lo que sí — insumo directo para gestión de stock sin stock (`ecommerce-specialist.md`).
- **Necesita**: `sku`, `product_name`, `product_qty`
- **ID interno**: #23 · Full only

### 35. Ciclo de vida del producto
- **Qué hace**: clasifica productos en emergente, madurez o declive según evolución de unidades.
- **Para qué sirve**: promover emergentes, exprimir maduros, liquidar declive antes de que generen stock muerto.
- **Necesita**: `product_name`, `product_qty`, `date`
- **ID interno**: #24 · Full only

### 36. Revenue por canal
- **Qué hace**: distribución de revenue por canal (web, mobile, POS).
- **Para qué sirve**: priorizar inversión en UX por canal.
- **Necesita**: `channel`, `total`
- **ID interno**: #28 · Full only

### 37. Análisis de canal (profundo)
- **Qué hace**: comparativa profunda por canal — AOV, tasa de cancelación, mix de productos.
- **Para qué sirve**: detectar diferencias de comportamiento no obvias entre canales.
- **Necesita**: `channel`, `total`, `order_status`
- **ID interno**: #33 · Full only

### 38. Afinidad entre colores
- **Qué hace**: combos de colores comprados juntos (parsea el nombre del producto buscando colores conocidos).
- **Para qué sirve**: merchandising fino — qué paletas funcionan, qué colores agregar al próximo drop.
- **Necesita**: `order_id`, `product_name`
- **ID interno**: #21 · Full only

### 39. Afinidad entre talles
- **Qué hace**: combos de talles en la misma orden.
- **Para qué sirve**: decisiones de curva de stock por talle y detección de compra para pareja/familia.
- **Necesita**: `order_id`, `product_name`
- **ID interno**: #22 · Full only

---

## Cuándo usar esta skill

Activar cuando el usuario mencione cualquiera de:

- "business intelligence", "BI", "análisis de ventas"
- "market basket", "basket analysis", "afinidad de productos", "cross-sell"
- "RFM", "segmentación de clientes", "clientes VIP", "churn"
- "CLV", "lifetime value", "valor del cliente"
- "cohortes", "retención", "recompra"
- "informe de ventas", "análisis ecommerce", "diagnóstico de tienda"
- Un análisis puntual: "armame un RFM", "quiero ver el market basket", "necesito un análisis de cohortes"

Inputs aceptados:

- CSV de exportación de pedidos de **Tienda Negocio** (mapear manualmente, ver nota arriba) — o Tiendanube/Shopify/WooCommerce si Roure migra de plataforma en el futuro.
- CSV genérico si las columnas matchean los nombres canónicos (ver `references/csv_mapping.md`).

---

## Modos disponibles

Antes de ejecutar, preguntar al usuario cuál quiere con `AskUserQuestion`:

### Modo Lite (21 análisis)

Los 21 análisis core. Default cuando el usuario no especifica. ~30 segundos.

### Modo Full (39 análisis)

Lite + 18 análisis avanzados (forecasting, clustering, variantes, churn detallado, etc.). Para deep dives.

### Modo Individual

El usuario pide un análisis puntual ("armame un RFM", "solo el market basket"). Resuelve dependencias automáticamente (si pedís #19 Bundling, el script corre #1 Market Basket como dependencia interna).

---

## Workflow

### Paso 1 — Detectar y validar el CSV

1. Identificar el archivo CSV (path indicado por el usuario).
2. Detectar encoding y delimitador.
3. Fingerprint de plataforma comparando headers contra `references/csv_mapping.md`.
4. **Si no matchea Tiendanube/Shopify/WooCommerce (caso esperado con Tienda Negocio)**: aplicar mapeo manual a columnas canónicas o pedir al usuario un `custom_mapping.json`.
5. Confirmar al usuario: plataforma detectada (o "genérico/mapeado manual"), cantidad de filas, rango de fechas.

### Paso 2 — Determinar qué correr (AskUserQuestion)

Tres opciones a ofrecer: **Lite**, **Full**, o **Individual** (resolver nombres mencionados a IDs internos usando el catálogo de arriba).

### Paso 3 — Ejecutar el script

**Modo Lite o Full:**

```bash
python scripts/bi_analysis.py \
  --csv "PATH_AL_CSV" \
  --mode lite \
  --output "/tmp/bi_results.json"
```

**Modo Individual:**

```bash
python scripts/bi_analysis.py --csv "PATH_AL_CSV" --analysis 7 --output "/tmp/bi_results.json"
python scripts/bi_analysis.py --csv "PATH_AL_CSV" --analysis 1,4,7,9 --output "/tmp/bi_results.json"
```

**Listar análisis disponibles:**

```bash
python scripts/bi_analysis.py --list
```

El script auto-detecta encoding/delimitador/plataforma, normaliza columnas, ejecuta los análisis, resuelve dependencias y genera un JSON con `mode`, `analysis_ids`, `platform`, `summary` y `analyses`. Cada análisis devuelve `status: "ok"`, `"skipped"` (con razón) o `"error"`.

### Paso 4 — Generar el HTML

1. Leer el JSON de resultados.
2. Tomar `references/html_template.md` como base (adaptar a paleta de `context/brand-context.md` si se pide).
3. Armar el informe con header, métricas hero, secciones por categoría (Producto → Cliente → Revenue → Geográfico → Operativo → Estratégico), cada análisis con título/tabla/insight accionable.
4. Guardar el HTML en el path indicado por el usuario.

---

## Reglas

- **SIEMPRE** correr `bi_analysis.py` — no calcular análisis manualmente. El script ya maneja normalización de columnas.
- Si un análisis falla por columnas faltantes, queda `status: "skipped"` con el motivo. **Mostrarlo en el HTML**, no ocultarlo.
- **Market Basket**: solo mostrar asociaciones con `support > 1%` y `lift > 1.0`.
- **RFM**: usar los 11 labels estándar (Champions, Loyal, Potential Loyal, New, Promising, Need Attention, About to Sleep, At Risk, Can't Lose, Hibernating, Lost).
- **Cohortes**: limitar a últimas 12 cohortes × 12 meses.
- **Insights accionables**: no describir el dato (eso ya está en la tabla). Decir qué hacer con él.
- **Privacidad**: el script no envía datos a ningún servicio externo. Todo corre local. No commitear CSVs con datos reales de clientas al repo — usar `.gitignore` (ya excluye `_real.csv` y `_client.csv` por convención del repo original).
- **Registro**: después de correr un análisis con hallazgos accionables, registrar en `memory/wins.md` o `memory/losses.md` según corresponda, siguiendo el protocolo estándar de las demás skills de Roure.

---

## Requisitos técnicos

- Python 3.9+ (el entorno ya tiene Python 3.12 instalado)
- `pandas` y `numpy` — **no instalados todavía**, requiere `pip install pandas numpy` antes del primer uso
- Sin servicios cloud, sin API keys. Todo corre local.

---

## Estructura

```
ecommerce-bi/
├── SKILL.md                          ← Este archivo
├── scripts/
│   └── bi_analysis.py                ← Motor (Python 3 + pandas)
└── references/
    ├── analysis_catalog.md           ← Metodología detallada de los 39 análisis
    ├── csv_mapping.md                ← Mapeo de columnas por plataforma + fallback genérico
    ├── html_template.md              ← Template HTML del informe (adaptado a brand Roure)
    └── required_columns.md           ← Qué columnas habilita cada análisis
```

## Skills Relacionados

- `ecommerce-specialist.md` — combos, descuentos, gestión de stock que este análisis puede validar o corregir
- `meta-ads-strategist.md` / `meta-ads-audience.md` — targeting geográfico y de retención que estos datos pueden afinar
- `growth-analyst.md` — experimentos que se pueden originar de un hallazgo de BI
