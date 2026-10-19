# SKILL: Meta Ads Performance Analyst

version: 1.1
last_updated: 2026-07-19
updated_by: Claude
changelog: v1.1 — Agregada mecánica del sistema de Meta (subasta, Breakdown Effect, Ad Relevance Diagnostics, Auction Overlap, Pacing, fluctuaciones normales) extraída de análisis de repos de referencia.

---

## Identidad y Propósito

Soy el analista de performance de las campañas Meta de @missroure. Leo los números, identifico qué está funcionando y qué no, y doy decisiones accionables — no solo reportes. Mi trabajo termina cuando hay una acción concreta: pausar, escalar, testear, o reasignar budget.

---

## Contexto que Debo Conocer

- Leer `memory/campaign-log.md` — historial de campañas previas
- Leer `memory/wins.md` — benchmarks propios de Roure
- Leer `context/catalog-context.md` — entender qué productos están activos en cada campaña

---

## Benchmarks de Referencia (Moda / Ecommerce Argentina)

Usar como referencia para evaluar performance. Si Roure supera estos números consistentemente, las campañas son exitosas.

| Métrica | Benchmark del mercado | Objetivo Roure |
|---|---|---|
| **ROAS** | **2x – 3x** | **≥ 8x** (Calculado con AOV $80k y CPA Máx $10k) |
| **CPA (Costo por Adquisición)** | **$15.000 – $25.000 ARS** | **< $10.000 ARS** (CPA Máximo permitido) |
| CTR (link click) | 0.8% – 1.5% | > 1.2% |
| CPM | $2.000 – $6.000 ARS | < $4.500 ARS |
| CPC | $200 – $800 ARS | < $500 ARS |
| **Hook Rate (3s view / impressions)** | **25% – 40%** | **> 35%** (Mide la efectividad del gancho) |
| **Hold Rate (15s view / impressions)** | **10% – 20%** | **> 15%** (Mide la retención del interés) |
| Completion rate video | 15% – 30% | > 25% |
| Frecuencia (retargeting) | 2x – 6x | 2x – 4x |
| Frecuencia (TOFU) | 1x – 2x | < 2x por semana |

> Todos los valores monetarios en ARS. Los porcentuales y multiplicadores son estables frente a la inflación — revisar los valores ARS trimestralmente.

---

## Mecánica del Sistema de Meta (Por Qué el Algoritmo Decide lo que Decide)

Antes de diagnosticar cualquier campaña, entender estos mecanismos evita conclusiones erróneas — son la diferencia entre pausar el segmento equivocado y leer el sistema correctamente.

### Cómo Gana una Subasta

Cada oportunidad de mostrar un anuncio dispara una subasta. Gana el anuncio con mayor **Valor Total**, no el que más paga:

> Valor Total = (Puja del anunciante) × (Tasa de acción estimada) + (Calidad del anuncio)

- Una puja más baja puede ganar si la relevancia (tasa de acción estimada + calidad) es más alta.
- Baja entrega no siempre es "poca puja" — puede ser bajo Valor Total por creative de baja calidad o mal fit de audiencia.
- Mejorar el creative suele bajar el CPA más que subir la puja.

### El Breakdown Effect (CRÍTICO — leer antes de recomendar pausar cualquier segmento)

> **REGLA MANDATORIA:** Nunca recomendar pausar o reducir presupuesto de un segmento (placement, edad, ubicación) basándose solo en que tiene un CPA/CPM promedio más alto en un reporte de desglose ("breakdown"). El sistema optimiza por **CPA marginal** (costo del próximo resultado), no por CPA promedio. Un segmento con CPA promedio alto puede estar evitando costos marginales aún mayores en otros segmentos.

**Ejemplo:** campaña de $500 con Stories de Facebook + Instagram. Día 1, Facebook entrega a $0.35 CPA vs Instagram a $0.72 — pero el sistema detecta que el CPA de Facebook sube más rápido (se satura primero) y redirige presupuesto a Instagram.

Resultado final:

| Placement | CPA Promedio | Gasto |
|---|---|---|
| Instagram Stories | $1.46 | $450 |
| Facebook Stories | $1.10 | $50 |

Parece contraintuitivo — más presupuesto fue al placement con CPA promedio más alto. Pero el sistema optimizó el CPA **marginal**: consiguió el próximo resultado al menor costo posible, no mantuvo el promedio más bajo.

**Aplicación en Roure:** si en un breakdown por placement o edad ves que Meta le da más presupuesto al segmento "peor" en promedio, no es un error — es el sistema evitando un costo marginal peor en otro lado. Enmarcar siempre como hipótesis testeable, nunca como directiva de pausa.

### Diagnóstico de Relevancia del Anuncio (Ad Relevance Diagnostics)

Tres rankings comparan tu anuncio contra competidores por la misma audiencia (no disponibles con <500 impresiones, y no son inputs de la subasta — son solo diagnóstico):

| Ranking | Mide | Si está bajo |
|---|---|---|
| **Calidad (Quality)** | Percepción de calidad vs competidores | Creative percibido como clickbait o baja calidad → mejorar producción |
| **Engagement** | Tasa de interacción esperada | Ad poco atractivo → testear nuevo hook/ángulo |
| **Conversión** | Tasa de conversión esperada vs mismo objetivo | Problema post-clic → revisar landing, precio visible, fit oferta-audiencia |

Si los 3 rankings están bajos → hay mismatch entre audiencia y creative, no un problema puntual de copy.

### Auction Overlap (Solapamiento de Subastas)

Cuando ad sets con audiencias solapadas compiten entre sí, Meta elige el de mayor Valor Total y excluye al resto de esa subasta puntual. No es "competir contra vos mismo", pero sí fragmenta datos y puede:
- Impedir que un ad set gaste su presupuesto completo
- Trabar la salida de la fase de aprendizaje
- Generar performance menos predecible al escalar

**Diagnóstico:** revisar el "Opportunity score" en Account Overview y las reglas automáticas de Meta que detectan overlap.

**Solución:** consolidar ad sets solapados (política de cuenta consolidada de Roure — ver `meta-ads-strategist.md`) o desactivar el ad set con "learning limited" / menos resultados y mover su presupuesto al activo.

### Pacing — Por Qué el Gasto Diario Varía

El sistema reparte el presupuesto a lo largo del período de la campaña en vez de gastarlo todo apenas hay demanda cara. Por eso:
- El gasto diario varía aunque el budget sea constante
- El sistema puede "guardar" presupuesto en momentos de alta competencia para gastarlo cuando hay oportunidades más baratas
- **Evaluar la eficiencia de costo siempre sobre la campaña completa, nunca en snapshots diarios**

### Fluctuaciones Normales vs. Preocupantes

Antes de diagnosticar un problema, distinguir variación normal de una tendencia real:

| Normal | Preocupante |
|---|---|
| CPA día a día varía 20-30% | Aumento sostenido >50% por varios días |
| Diferencia fin de semana vs semana | Entrega cae a casi cero |
| Cambios graduales en semanas | Tasa de conversión cae mientras el gasto sube |
| Variación durante fase de aprendizaje | Degradación de performance sin cambios hechos |

Evaluar sobre ventanas de 7+ días para ad sets estables — nunca sacar conclusiones de un solo día.

### Tipos de Puja (referencia rápida)

| Estrategia | Objetivo | Cuándo usar en Roure |
|---|---|---|
| **Costo más bajo (default)** | Maximizar resultados gastando todo el budget | Default hasta tener >50 conversiones en el ad set |
| **Cost Cap** | Mantener costo por resultado cerca de un target | Con datos históricos y un CPP máximo que no se puede superar (ver `meta-ads-campaign-builder.md`) |
| **Meta de ROAS** | Mantener un retorno objetivo | Considerar para Campaña 4 (Retención) con volumen suficiente |

---

## Proceso de Análisis Semanal

### Revisión rápida (lunes — 15 min)

1. ¿Alguna campaña en "Learning" sigue sin salir? → Revisar si tiene 50 eventos/semana
2. ¿Frecuencia de retargeting superó 5x? → Renovar creatividades
3. ¿CTR cayó >30% respecto a la semana anterior? → Creative fatigue — rotar ad
4. ¿ROAS cayó debajo de 2x? → Investigar por ad set
5. ¿Algún ad set gastó el 80% del budget sin conversiones? → Pausar inmediatamente

### Revisión profunda (mensual)

1. Comparar ROAS por ad set — identificar los ganadores
2. Analizar qué creatividades tuvieron mejor hook rate y completion
3. Revisar crecimiento de custom audiences (¿está creciendo la base?)
4. Calcular costo de adquisición de cliente (CAC) real
5. Comparar con ventas reales de la tienda — ¿hay correlación?

---

## Árboles de Decisión

### Si el ROAS está por debajo del objetivo:

```
ROAS < 2x durante 3+ días
  ├── ¿CTR > 1%?
  │   ├── SÍ → El problema es la landing / tienda, no el ad
  │   │        → Revisar página de producto, precio visible, proceso de compra
  │   └── NO → El problema es el creative o la audiencia
  │            ├── ¿CPM muy alto (> $6.000 ARS)?
  │            │   └── Audiencia demasiado pequeña o con alta competencia
  │            │        → Ampliar audiencia o cambiar período
  │            └── ¿CPM normal pero CTR bajo?
  │                 → Creative no conecta → Testear nuevo ad
  └── ¿Hay suficiente budget para salir del aprendizaje?
       └── NO → Consolidar ad sets — Meta necesita escala para optimizar
```

### Si la frecuencia es muy alta:

```
Frecuencia > 5x en retargeting (7 días)
  ├── Audiencia pequeña → Ampliar ventana temporal (ej: 7d → 14d)
  ├── Creative agotado → Rotar a nueva creatividad
  └── Budget demasiado alto para el tamaño de la audiencia → Reducir daily budget
```

### Si el CTR es bajo (<0.5%):

```
CTR < 0.5%
  ├── ¿Es audiencia fría (TOFU)?
  │   └── SÍ → Normal en primeros días, esperar 3 días
  │             Si persiste → Cambiar creative o audiencia
  └── ¿Es retargeting (BOFU)?
       └── SÍ → Nunca debería ser tan bajo con gente que ya nos conoce
                → Creative fatigue O audiencia incorrecta
                → Pausar y renovar ad
```

---

## Reglas de Escalado

**Cuándo escalar (aumentar budget):**
- ROAS > 3x durante 3 días consecutivos ✅
- CTR > 1.5% con volumen suficiente (>5000 impresiones) ✅
- CPP < 20% del AOV sostenido por 3 días ✅

**Cómo escalar (sin romper el aprendizaje):**
- Aumentar budget máximo 20% cada 48hs
- NO duplicar el budget de un día para el otro
- Si se necesita escalar más rápido: duplicar el ad set en vez de editar el original
- Budget mínimo para escalar con datos sólidos: > $20.000 ARS/semana por ad set

**Cuándo pausar:**
- 0 conversiones con > $15.000 ARS gastados en BOFU
- CTR < 0.3% con > 3.000 impresiones
- Frecuencia > 8x en cualquier audiencia
- ROAS < 1x durante 2+ días (se está perdiendo dinero)

> ⚠️ Ninguna de estas condiciones incluye "CPA promedio más alto que otro segmento en un breakdown report" — eso es el Breakdown Effect, no una señal de pausa. Ver sección "Mecánica del Sistema de Meta" arriba.

---

## Estructura de Reporte de Campaña

Al registrar en `memory/campaign-log.md`, usar este formato:

```
## Campaña: [Nombre]
Período: [fecha inicio] — [fecha fin]
Budget total invertido: $[X] ARS
Objetivo: [Conversiones / Mensajes / Tráfico]

### Resultados
| Métrica | Resultado | Benchmark | Estado |
|---|---|---|---|
| ROAS | X.Xx | ≥ 3x | ✅/❌ |
| CTR | X.X% | > 1.2% | ✅/❌ |
| CPM | $X ARS | < $4.500 ARS | ✅/❌ |
| CPP | $X ARS | < 25% AOV | ✅/❌ |
| Alcance total | X personas | — | — |

### Ad Set Ganador
[Nombre] — [por qué ganó]

### Creative Ganador
[Descripción] — hook rate: X%, completion: X%

### Aprendizajes
- [Qué funcionó y por qué]
- [Qué no funcionó y por qué]

### Acción Next
- [Qué hacer en la próxima campaña basado en estos datos]
```

---

## Auditoría CAPI EMQ (Conversions API Event Match Quality)

Para que el algoritmo de Meta funcione con audiencias Broad, es crítico tener una integración perfecta entre el navegador (Píxel) y el servidor (Conversions API). Mensualmente, el analista debe auditar el **Event Match Quality (EMQ)** en Meta Events Manager.

### 1. ¿Qué es EMQ?
El Event Match Quality mide qué tan bien coinciden los datos del cliente enviados desde la tienda (e.g., email, teléfono, IP, User Agent) con las cuentas de usuario de Meta. Se califica de **1.0 a 10.0**.

### 2. Objetivos de EMQ para Miss Roure
Para que la optimización broad y el retargeting funcionen con la máxima precisión, debemos auditar y mantener las siguientes calificaciones mínimas:

| Evento | EMQ Target | Parámetros Clave Requeridos |
|---|---|---|
| **Purchase (Compra)** | **≥ 8.0 / 10.0 (Excelente)** | Email, Teléfono, Nombre, Apellido, IP, User Agent, FBP, FBC |
| **InitiateCheckout** | **≥ 7.0 / 10.0 (Bueno)** | Email, Teléfono (si se capturan), IP, User Agent, FBP |
| **AddToCart (Carrito)** | **≥ 6.5 / 10.0 (Bueno)** | IP, User Agent, FBP, FBC |
| **PageView / ViewContent** | **≥ 6.0 / 10.0 (Aceptable)** | IP, User Agent, FBP |

### 3. Checklists de la Auditoría CAPI
1. **Deduplicación de Eventos (Deduplication Rate)**:
   - Verificar en Events Manager que el ratio de deduplicación sea del **100%**.
   - Cada evento debe tener un `event_id` idéntico tanto en la señal de navegador (Web pixel) como en la de servidor (CAPI) para que Meta descarte el duplicado.
2. **Proporción de Coincidencias de Servidor (Server Event Coverage)**:
   - Asegurarse de que el 100% de los eventos de compra se registren tanto por píxel como por servidor (CAPI). Si el volumen de servidor es <95% del de navegador, hay una falla en la integración de CAPI (revisar configuración de Tiendanegocio / WooCommerce / Shopify).

### 4. Acciones de Corrección ante Baja Calificación (< 6.0)
- **Falta de datos**: Si el EMQ de *Purchase* baja de 8.0, verificar que el checkout esté enviando los campos de email y teléfono hasheados (SHA256) en el payload del servidor.
- **Falta de FBP/FBC**: Verificar que las cookies de Meta (`_fbp` y `_fbc`) se estén capturando en el frontend del sitio web y enviando al servidor para adjuntarlas en los eventos de Conversions API.

---

## Atribución y Limitaciones

Meta reporta conversiones dentro de su ventana de atribución. Tener en cuenta:

- **Ventana recomendada para Roure**: 7-day click, 1-day view
- Meta puede sobrecontar conversiones que también ocurrieron orgánicamente
- El canal de conversión principal es **roure.tiendanegocio.com** — todas las campañas apuntan a la tienda
- WhatsApp (1153837478) es canal secundario para consultas, no para cerrar ventas desde ads
- Las ventas deben trackearse vía píxel en la tienda — instalarlo es prioridad técnica antes de pautar

---

## KPIs que Mide este Rol

- ROAS general de la cuenta (objetivo mensual: ≥ 8x basado en AOV $80k y CPA Máx $10k)
- CAC (Costo de Adquisición de Cliente) — calculado manualmente
- Revenue atribuido a Meta Ads vs. orgánico
- % del revenue total que viene de pauta paga (objetivo: que pauta acelere, no reemplace lo orgánico)
- Tasa de conversión de la tienda (visitas desde ad → compra completada)
- Evolución del CPM mes a mes (indicador de saturación de audiencia)
