# Brief: Sweater Vienne — ASC — 2026-06-05

**Versión**: 1.1
**Fecha de creación**: 2026-06-05
**Última actualización**: 2026-06-06
**Creado por**: Antigravity (Orchestrator)
**Estado**: Aprobado (Listo para implementar)

---

## Información General

| Campo | Detalle |
|---|---|
| Colección | ROURE ESSENTIALS |
| Nombre del drop / producto | Sweater Vienne (Cuello Bote) |
| Fecha de lanzamiento | 2026-06-05 |
| Fecha de cierre / evaluación | 2026-06-19 (2 semanas después) |
| Canales | Meta Ads (Advantage+ Shopping Campaign - ASC) |

---

## Narrativa de Campaña

**Concepto central**:
> "Cozy pero sexy: el sweater que vas a querer usar siempre 🧸"

**Historia emocional**:
Para esos días de frío donde querés sentirte abrigada, cómoda y súper sexy al mismo tiempo. Un abrigo suave como un abrazo que realza tu figura y te hace sentir arreglada sin esfuerzo.

**Tono específico de esta campaña**:
Cercano, cálido, de amiga a amiga ("voseo"), apelando al bienestar físico y a la belleza natural en el día a día.

---

## Productos Estrella

| Producto | Precio | Con transferencia | Stock |
|---|---|---|---|
| Sweater Vienne (Cuello Bote) | $37.500 ARS | $30.000 ARS (20% OFF) | ✅ EN STOCK |

---

## Configuración técnica en Ads Manager

### Campaña: Advantage+ Shopping Campaign (ASC)
* **Nombre de Campaña**: `Sweater Vienne — ASC — 2026-06-05`
* **Presupuesto Diario**: $5.000 ARS/día
* **Destino**: `https://roure.tiendanegocio.com/productos/sweater-cuello-bote`
* **Límite de Clientes Existentes**: 10% (utilizando el Custom Audience `Custom-Compradores-Historicos`).
* **Optimización**: Conversiones → evento **Purchase**. Ventana de atribución: **7-day click + 1-day view** (verificar en la configuración del Ad Set que no quede en 1-day click por defecto).
* **UTMs dinámicos**: `utm_source={{site_source_name}}&utm_medium=paid_social&utm_campaign={{campaign.name}}&utm_content={{ad.name}}`

---

## Creativos y Copies

### Ad 1: Showcase de Producto (Aesthetic)
* **Video**: referencia histórica `Ads 1.mp4` no encontrada; consultar [variantes originales](../assets/videos/) y elegir la versión antes de usarla. (Showcase estético mostrando variantes de color en percha y modelo: bordo, negro, crema, chocolate). **Formato requerido: 9:16 vertical** (Reels + Stories).
* **Texto Principal 1 (Emocional)**:
  > 🌷 Tan suave que no vas a querer sacártelo — y tan lindo que no vas a tener que hacerlo. El Sweater Vienne es de hilado grueso friz, con cuello bote caído y viene en 4 colores. ¿Con cuál te quedás? ✨
* **Texto Principal 2 (Racional)**:
  > 🌷 Hilado grueso friz — eso significa que es suave, cálido y no pica. El Sweater Vienne con cuello bote caído en 4 colores. Para los días de frío donde igual querés verte bien. Pedilo con 20% OFF. ✨
* **Título 1 (Headline)**: `Tu color favorito te está esperando 🌷`
* **Título 2 (Headline)**: `20% OFF con transferencia — $30.000 ✨`
* **CTA Button**: Comprar ahora

### Ad 2: UGC / Voiceover (Conversión)
* **Video**: referencia histórica `ads2.mp4` no encontrada; consultar [variantes originales](../assets/videos/) y elegir la versión antes de usarla. (Video con locución en off sobre ser "cozy pero sexy" usando el Vienne negro). **Formato requerido: 9:16 vertical** (Reels + Stories).
* **Texto Principal 1 (Emocional)**:
  > 🌷 Una cita romántica y no sabés qué ponerte — te entiendo. Yo lo resolví con el Sweater Vienne: suave, con cuello bote caído y en 4 colores. Spoiler: vas a querer usarlo siempre. Pedilo ahora. ✨
* **Texto Principal 2 (Racional)**:
  > Cozy, sexy y de hilado grueso friz. Conseguí tu Sweater Vienne con 20% OFF por solo $30.000 ARS. Comprá ahora. 🧸
* **Título 1 (Headline)**: `El outfit de tu próxima cita 🌷`
* **Título 2 (Headline)**: `20% OFF — solo $30.000 ARS ✨`
* **CTA Button**: Comprar ahora

---

## Post-Launch (primeras 24hs)

- [ ] Confirmar que ambos ads están en estado "Activo" (no rechazados)
- [ ] Verificar en **Events Manager** que el pixel registra eventos `Purchase` reales
- [ ] Anotar fecha de inicio en `memory/campaign-log.md` ← ya completado
- [ ] Revisar métricas el **8 de junio** (72hs post-lanzamiento)

---

## KPIs de Éxito (Evaluación en 7 días)

| Métrica | Objetivo |
|---|---|
| CPM (Campaña general) | < $4.500 ARS |
| CTR (Promedio) | > 1.2% |
| Hook Rate (Ad 1 y Ad 2) | ≥ 35% |
| Hold Rate (Ad 1 y Ad 2) | ≥ 15% |
| CPP (Costo por Compra) | ≤ $10.000 ARS |
| ROAS de plataforma | ≥ 3x |
