# UTM Convention — Miss Roure Meta Ads

Convención de parámetros UTM para todo el tráfico pago de Meta.
Aplicar en cada ad desde el primer día — sin UTMs no sabés qué pasa después del click de Meta.

---

## Por Qué Importan los UTMs

Meta atribuye conversiones con su propia ventana (7-day click / 1-day view).
Los UTMs te permiten ver en Google Analytics 4 (GA4) o en la analítica de tiendanegocio.com:
- Qué campaña realmente trajo tráfico que convirtió
- Cuánto tiempo tarda la clienta en comprar después del primer click
- Comparar el dato de Meta vs el dato real de la tienda

---

## Estructura Base

```
?utm_source=facebook&utm_medium=paid_social&utm_campaign=[CAMPAIGN]&utm_content=[CREATIVE]&utm_term=[AUDIENCE]
```

---

## Parámetros y Valores

### `utm_source` — origen del tráfico

| Valor | Cuándo usar |
|---|---|
| `facebook` | Ads en Facebook (Feed, Stories, Reels, Messenger) |
| `instagram` | Ads en Instagram (Feed, Stories, Reels, Explore) |

> Si usás Advantage+ Placements, usá el Dynamic UTM de Meta: `{{site_source_name}}` — se reemplaza automáticamente.

### `utm_medium` — tipo de tráfico

| Valor | Cuándo usar |
|---|---|
| `paid_social` | Siempre para Meta Ads |

### `utm_campaign` — nombre de campaña

Usar el mismo nombre que en el Ads Manager, en minúsculas y con guiones.

| Ejemplo en Ads Manager | UTM campaign |
|---|---|
| `Tapados Otoño — TOFU — 2026-05-27` | `tapados-otono-tofu` |
| `Retargeting Visitantes 7d` | `retargeting-visitantes-7d` |
| `Cozy Cute — Lookalike` | `cozy-cute-lookalike` |

### `utm_content` — identificación del creative

Permite saber qué ad específico trajo el tráfico. Usar el ID del brief o del test.

| Formato | Ejemplo |
|---|---|
| `[tipo]-[producto]-[formato]` | `video-tapado-perla-reel` |
| `[TEST-ID]-[variante]` | `test-001-a` |
| `[tipo]-[descripción corta]` | `imagen-precio-visible` |

### `utm_term` — audiencia (opcional pero recomendado)

| Valor | Cuándo usar |
|---|---|
| `tofu-intereses` | Audiencias de intereses frías |
| `tofu-lookalike-1pct` | Lookalike 1% |
| `mofu-ig-engagers` | Audiencia de engagement IG |
| `bofu-retargeting-7d` | Retargeting visitantes 7 días |
| `bofu-carrito-7d` | Retargeting carrito abandonado |

---

## Ejemplos Completos

**Campaña TOFU — Video — Tapado Perla:**
```
https://roure.tiendanegocio.com/productos/tapado-perla?utm_source=instagram&utm_medium=paid_social&utm_campaign=tapados-otono-tofu&utm_content=video-tapado-perla-reel&utm_term=tofu-intereses
```

**Retargeting BOFU — Imagen:**
```
https://roure.tiendanegocio.com/productos/tapado-perla?utm_source=facebook&utm_medium=paid_social&utm_campaign=retargeting-visitantes-7d&utm_content=imagen-precio-20off&utm_term=bofu-retargeting-7d
```

**A/B Test:**
```
Creative A: utm_content=test-002-a-precio-visible
Creative B: utm_content=test-002-b-sin-precio
```

---

## Cómo Agregar UTMs en Meta Ads Manager

1. En el nivel del **Ad** → sección "Tracking"
2. En "URL parameters" pegar los parámetros (sin el `?` inicial)
3. Meta agrega automáticamente el `?` antes del UTM
4. Usar **URL Builder** de Meta para validar: no romper la URL de destino

**Tip**: Usar los parámetros dinámicos de Meta cuando sea posible:
```
utm_source={{site_source_name}}&utm_medium=paid_social&utm_campaign={{campaign.name}}&utm_content={{ad.name}}
```
Esto se autocompletaría en cada impression con los datos reales.

---

## Verificación

Después de lanzar un ad, verificar en 24-48hs:
- [ ] El tráfico aparece en la analítica de tiendanegocio.com con la fuente correcta
- [ ] El nombre de campaña matchea el de Ads Manager
- [ ] No hay tráfico marcado como "direct" que debería venir de Meta
