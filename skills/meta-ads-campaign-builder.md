# SKILL: Meta Ads Campaign Builder — Miss Roure

version: 1.0
last_updated: 2026-05-29

Playbook paso a paso para crear campañas en Meta Ads Manager.
Este skill conecta estrategia + audiencias + creative + tracking en una secuencia de ejecución.
Leer antes de crear cualquier campaña nueva.

---

## Antes de Abrir el Ads Manager

Responder estas cuatro preguntas. Si alguna no tiene respuesta clara, no crear la campaña todavía.

1. **¿Qué producto voy a pautar?** → Verificar en `context/catalog-context.md` que esté en stock ✅
2. **¿A quién le voy a mostrar el ad?** → Elegir el ID de audiencia de `metads/audiences/audience-library.md`
3. **¿Cuánto budget tengo?** → Mínimo $7.000 ARS/semana por ad set para tener datos útiles
4. **¿El brief del creative está listo?** → Completar `metads/templates/ad-brief-template.md` primero

---

## PASO 1 — Nivel de Campaña

### 1.1 Elegir el objetivo

| Situación | Objetivo a elegir |
|---|---|
| Pixel instalado y evento Purchase activo | **Ventas** → Conversiones → Compras |
| Sin pixel todavía | **Tráfico** → Clics en el enlace |
| Lanzamiento de nueva colección (semana 1) | **Reconocimiento** → Alcance o Video Views |
| Recolectar engagement para armar audiencia MOFU | **Interacción** → Interacción con la publicación |

> ⚠️ El objetivo de campaña es lo más difícil de cambiar después. Si te equivocás, tenés que crear una campaña nueva.

### 1.2 Naming de la campaña

Formato exacto:
```
[Producto/Colección] — [Tipo de Campaña] — [YYYY-MM-DD]
```

Ejemplos:
```
Sweater Vienne — Prospección CBO — 2026-06-05
Essentials Evergreen — ASC — 2026-06-05
Audiencias Calientes — Retargeting ABO — 2026-06-05
Compradoras Históricas — Retención — 2026-06-05
```

Reglas:
- Fecha = fecha de lanzamiento, no de creación.
- Tipo de Campaña: Prospección CBO / ASC / Retargeting ABO / Retención.
- Si es un A/B test creativo dentro del Sandbox: agregar `[TEST-XXX]` al final.

### 1.3 CBO vs ABO

| Situación | Decisión |
|---|---|
| Un solo ad set | ABO — budget directamente en el ad set |
| Dos o más ad sets probando audiencias distintas | CBO — budget en la campaña, Meta lo distribuye |
| Querés controlar exactamente cuánto va a cada audiencia | ABO |
| Querés escalar rápido con menos fricción | CBO |

### 1.4 Configuración de campaña

- **Límite de gasto de campaña**: dejar en blanco (controlás por ad set o por tiempo, no por límite de campaña)
- **A/B test integrado de Meta**: NO usar — hace el test Meta, no vos. Usar el proceso manual de `metads/templates/creative-test-log.md`
- **Advantage Campaign Budget**: activar solo si elegiste CBO

---

## PASO 2 — Nivel de Ad Set

Crear un ad set por audiencia. No mezclar audiencias distintas en el mismo ad set.

### 2.1 Naming del ad set

Formato exacto:
```
[ID de audiencia] — [Descripción corta]
```

Ejemplos:
```
TOFU-INT-01 — Mujeres Moda GBA 22-35
BOFU-CA-01 — Carrito Abandonado 7d
MOFU-CA-04 — IG Engagers 60d
```

Usar el ID de `metads/audiences/audience-library.md` — así podés cruzar datos entre campañas.

### 2.2 Conversión

- **Ubicación de conversión**: Sitio web → roure.tiendanegocio.com
- **Evento de conversión**: Compras (si el pixel está activo)
- **Ventana de atribución**: 7 días tras clic, 1 día tras visualización ← no cambiar esto nunca

### 2.3 Presupuesto del ad set

| Situación | Budget diario |
|---|---|
| Ad set nuevo, sin datos | $1.000 – $2.000 ARS/día ($7.000 – $14.000/semana) |
| Ad set en optimización activa | $2.000 – $4.000 ARS/día |
| Ad set probado con ROAS > 3x | Escalar 20% cada 48hs desde el valor actual |

- **Tipo**: Budget diario (no de por vida — perdés control si Meta gasta de golpe)
- **Fecha de fin**: NO configurar. Pausar manualmente cuando corresponda.

### 2.4 Audiencia

Abrir `metads/audiences/audience-library.md` y copiar la configuración exacta del ID elegido.

**Ubicaciones**:
- Seleccionar **Ubicaciones automáticas de Advantage+** — Meta optimiza mejor que la selección manual
- Excepción: si el presupuesto es muy bajo (< $1.000 ARS/día), limitar a Instagram Feed + Instagram Reels para no fragmentar

**Segmentación detallada**:
- Para TOFU de intereses: usar los intereses documentados en `meta-ads-audience.md` → sección "Intereses base Miss Roure"
- Para Lookalike: crear la audiencia en Meta BM primero, luego seleccionarla acá
- Para retargeting: seleccionar la Custom Audience correspondiente

**Exclusiones**: aplicar siempre las exclusiones estándar del `audiences/audience-library.md`

**Tamaño mínimo operacional**:
- BOFU: 1.000 – 50.000 personas
- MOFU: 100.000 – 1.000.000 personas
- TOFU: 500.000 – 3.000.000 personas

Si la audiencia queda fuera de rango → revisar segmentación antes de continuar.

### 2.5 Optimización y entrega

- **Optimización para**: Conversiones → Compras (si hay pixel) / Clics en el enlace (si no hay pixel)
- **Estrategia de puja**: Costo más bajo (default) — no tocar hasta tener > 50 conversiones en el ad set
- **Cuando SÍ usar Cost Cap**: cuando tenés un CPP máximo que no podés superar (ej: categoría accesorios → CPP máx $2.500 ARS) y ya tenés datos históricos del ad set

---

## PASO 3 — Nivel de Anuncio (el Ad)

### 3.1 Naming del anuncio

Formato exacto:
```
[Formato] — [Producto] — [Descripción del hook o variante]
```

Ejemplos:
```
Video — Tapado Perla — Hook precio directo
Imagen — Sweater Rose — Modelo usando prenda
Carrusel — Colección Cozy — 5 productos con precio
Video — Tapado Perla — [TEST-001-A] Hook precio
Video — Tapado Perla — [TEST-001-B] Hook emocional
```

### 3.2 Creative

- Usar el creative producido según `metads/templates/ad-brief-template.md`
- Formato recomendado por etapa:

| Etapa | Formato recomendado | Por qué |
|---|---|---|
| TOFU | Video 9:16 (Reel) | Máximo alcance, construye brand |
| MOFU | Video 9:16 o Carrusel | Muestra más de la colección |
| BOFU | Imagen 1:1 con precio visible o Video corto | Decisión rápida — la persona ya conoce la marca |

- **No usar el mismo creative en más de un ad set a la vez** — contamina los resultados del A/B

### 3.3 Copy del anuncio

Estructura del texto principal:

```
[Hook — primera línea visible antes del "ver más"]
[Beneficio del producto en una oración]
[Oferta — precio con transferencia y/o envío gratis]
→ [URL de la tienda]
```

- Precio con transferencia SIEMPRE visible en BOFU y MOFU
- Un solo CTA → roure.tiendanegocio.com/[producto específico]
- No enviar a la homepage — link directo al producto del brief

Consultar templates completos en `skills/meta-ads-creative.md`.

### 3.4 URL de destino

1. Copiar la URL del producto en roure.tiendanegocio.com
2. Agregar UTMs según `metads/setup/utm-convention.md`:

```
https://roure.tiendanegocio.com/productos/[nombre-producto]?utm_source=instagram&utm_medium=paid_social&utm_campaign=[nombre-campaña]&utm_content=[nombre-ad]&utm_term=[ID-audiencia]
```

3. Verificar que la URL cargue correctamente ANTES de guardar el ad
4. Verificar que el precio sea el correcto y el producto esté en stock

### 3.5 CTA Button

| Objetivo de campaña | CTA recomendado |
|---|---|
| Conversiones / Ventas | "Comprar ahora" |
| Tráfico | "Más información" o "Ver más" |
| Engagement (TOFU) | "Más información" |

---

## PASO 4 — Antes de Publicar

Completar el checklist en `metads/checklists/pre-launch.md`.

Los ítems que NO se pueden saltear:
- [ ] Pixel activo y evento Purchase verificado en Events Manager
- [ ] URL de destino abre el producto correcto con precio visible
- [ ] Producto en stock confirmado
- [ ] Exclusión de compradores recientes aplicada
- [ ] UTMs configurados y verificados
- [ ] Nombre de campaña, ad set y ad siguen la convención de este skill
- [ ] Budget ≥ $7.000 ARS/semana por ad set

---

## PASO 5 — Monitoreo Post-Lanzamiento

### A las 24 horas

Verificar:
- ¿El ad está en estado "Activo"? Si dice "En revisión" por más de 24hs → revisar política de Meta
- ¿Está gastando? Si el gasto es $0 → problema de entrega (revisar audiencia o puja)
- ¿El pixel registra eventos? Ir a Events Manager y verificar que estén llegando

### A las 72 horas (primera decisión)

Correr `metads/scripts/analyze.py --csv [export.csv]` y evaluar:

| Situación | Acción |
|---|---|
| CTR < 0.3% y > 2.000 impresiones | Pausar — creative o audiencia con problema grave |
| CTR 0.3%–0.8% | Esperar hasta día 7 antes de pausar |
| CTR > 0.8% | Bien — continuar |
| 0 conversiones con > $15.000 ARS en BOFU | Pausar inmediatamente |
| Fase de aprendizaje activa (< 50 eventos) | No tocar — dejar correr |

### A los 7 días (decisión de escala)

Correr `metads/scripts/weekly_report.py` y aplicar la decisión Q3 del reporte.
Registrar en `memory/campaign-log.md`.

---

## Guía de Configuración: Advantage+ Shopping Campaign (ASC)

Las campañas Advantage+ Shopping (ASC) automatizan la segmentación combinando prospección y retargeting en un único flujo de optimización. Sigue estos pasos para configurarlas correctamente en Miss Roure:

### 1. Creación en Ads Manager
- Clic en **Crear**.
- Selecciona el objetivo **Ventas** (Sales) y haz clic en **Continuar**.
- Selecciona **Campaña de compras de Advantage+ (Recomendado)** y haz clic en **Continuar**.

### 2. Configuración de Campaña
- **Nombre de Campaña**: `[Colección/Evergreen] — ASC — [YYYY-MM-DD]` (ej. `Knitwear Essentials — ASC — 2026-06-05`).
- **Destino**: Sitio web (`roure.tiendanegocio.com`).
- **Ubicación del pixel**: Seleccionar el píxel de Miss Roure y el evento de optimización **Comprar** (Purchase).
- **Ubicaciones geográficas**: Argentina. (Meta optimizará la entrega, priorizando zonas con mayor conversión como CABA y GBA).

### 3. Límites Presupuestarios de Clientes Existentes
- Ve a la sección **Configuración de la cuenta de anuncios** > **Base de clientes existentes**.
- Define tu audiencia de clientes existentes seleccionando el Custom Audience de compradores históricos subido de WhatsApp/Tienda (`Custom-Compradores-Historicos`).
- En la configuración del presupuesto de la campaña ASC, activa **Límite de presupuesto para clientes existentes** y configúralo en un **10%** (máximo **20%** en épocas de liquidación). Esto obliga a Meta a destinar el 80%-90% del presupuesto a adquirir clientas nuevas (prospección fría).

### 4. Estructura y Carga de Creativos
- Cargar entre **5 y 10 anuncios activos** simultáneamente en la campaña.
- **Mix de Formatos Requerido**:
  - Al menos 2 videos verticales (9:16) con hooks diferentes (UGC/Founder).
  - Al menos 2 carruseles de productos de colección (1:1).
  - Al menos 1 o 2 imágenes estáticas limpias con precio y oferta visible.
- **Importación de Ads Existentes**: Utiliza la opción "Importar anuncios sugeridos" si Meta identifica creatividades de campañas previas con alto rendimiento orgánico o pago.

---

## Guía de Configuración: Creative Testing Sandbox (Método 3:2:2)

Para probar hooks, copies y formatos sin perturbar el aprendizaje de las campañas principales (ASC o Prospección CBO), se debe implementar un Sandbox de testeo creativo siguiendo el método unificado **3:2:2**.

### 1. Configuración de Campaña Sandbox
- Clic en **Crear**.
- Selecciona el objetivo **Ventas** (Conversiones).
- Elige **Configuración manual de campaña de ventas** (NO Advantage+).
- **Nombre de Campaña**: `[Sandbox] — Creative Testing — [YYYY-MM-DD]`.
- **Presupuesto (ABO)**: Desactivar Advantage Campaign Budget (CBO). La campaña debe usar **ABO (presupuesto a nivel de Ad Set)** para controlar el presupuesto de cada test.

### 2. Estructura del Ad Set de Test (Método 3:2:2)
- **Nombre del Ad Set**: `[ID-Audiencia] — [Hipótesis de Test] — [Nombre del Producto]` (ej. `AB-Mujeres-18-35 — Test 3:2:2 — Sweater Vienne`).
- **Ubicación de Conversión**: Sitio web (roure.tiendanegocio.com) > Evento: Comprar.
- **Audiencia**: Broad / Abierta (Argentina, Mujeres, 18-35). Sin intereses ni lookalikes. *Nota: La audiencia debe ser idéntica a la campaña de escala Broad CBO para que los resultados sean transferibles.*
- **Presupuesto**: Asignar un presupuesto mínimo diario equivalente al CPA Máximo ($10.000 ARS) o al menos el 50% de este ($5.000 ARS).
- **Dynamic Creative (DCO)**: Activar **Contenido Creativo Dinámico** a nivel de Ad Set. Esto nos permite configurar de manera exacta:
  - **3 Creatividades (Videos o Imágenes)**: Deben ser visualmente distintas (ej. Variante A: Styling/Outfits, Variante B: Textura y close-up, Variante C: UGC/Founder hablando).
  - **2 Textos Principales (Primary Texts)**: Ángulos de copy diferenciados (ej. Ángulo 1: Emocional/Lifestyle con "sentite linda", Ángulo 2: Racional/Focalizado en 20% OFF transferencia y beneficios de la tela).
  - **2 Títulos (Headlines)**: Con enfoques distintos (ej. Título 1: Nombre de la prenda + precio, Título 2: Llamado a la acción con urgencia suave o beneficio).

### 3. Reglas de Ejecución y Traspaso de Ganadores (Scaling Protocol)
- **Duración del test**: Dejar correr de 3 a 5 días o hasta alcanzar al menos **1.000 impresiones por variación**.
- **Métricas Clave de Decisión**:
  - *Ganador por Atractivo (Top Funnel)*: Mayor **Hook Rate (≥35%)** y **CTR (link) (≥1.2%)**.
  - *Ganador por Conversión (Bottom Funnel)*: Menor **CPA (Costo por Adquisición) (≤$10.000 ARS)** y **Hold Rate (≥15%)**.
- **Cómo escalar la variante ganadora**:
  - Obtener el **Post ID** exacto del ad ganador desde el Sandbox.
  - Cargar el ad ganador en la campaña **Advantage+ Shopping (ASC)** o **Prospección CBO Manual** de escala usando la opción "Utilizar publicación existente" con el Post ID correspondiente. Esto conserva la prueba social (likes, compartidos y comentarios acumulados).
  - Pausar el Ad Set de testeo en el Sandbox una vez finalizado el análisis.

---

## Skills Relacionados

- `meta-ads-strategist.md` — arquitectura y tipos de campaña
- `meta-ads-audience.md` — segmentación y configuración de audiencias
- `meta-ads-creative.md` — formatos, copy y reglas visuales
- `meta-ads-analyst.md` — análisis y decisiones post-campaña
- `metads/SKILL.md` — metodología 3Qs para análisis con datos reales
- `metads/audiences/audience-library.md` — IDs de audiencias activas
- `metads/templates/ad-brief-template.md` — brief del creative
- `metads/setup/utm-convention.md` — parámetros de tracking
- `metads/checklists/pre-launch.md` — verificación antes de publicar
