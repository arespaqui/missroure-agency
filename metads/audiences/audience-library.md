# Audience Library — Miss Roure Meta Ads

version: 1.0
last_updated: 2026-05-29

Biblioteca de todas las audiencias activas y pasivas organizadas por etapa del funnel.
Actualizar cada vez que se cree, archive o modifique una audiencia en el Ads Manager.

---

## TOFU — Audiencias Frías (prospección)

### Intereses

| ID interno | Nombre en Ads Manager | Segmentación | Tamaño est. | Estado | Notas |
|---|---|---|---|---|---|
| TOFU-INT-01 | Mujeres Moda GBA 22-35 | Mujeres 22-35 \| AMBA \| Moda, ropa, tendencias | ~800k | ⏳ pendiente | Audiencia base de prospección |
| TOFU-INT-02 | Mujeres Moda GBA 35-50 | Mujeres 35-50 \| AMBA \| Moda, estilo | ~600k | ⏳ pendiente | Segmento comprador frecuente |
| TOFU-INT-03 | Compradoras Online Arg | Mujeres 22-45 \| Argentina \| Compras online, ecommerce | ~1.2M | ⏳ pendiente | Prospección nacional |

### Lookalike

| ID interno | Nombre en Ads Manager | Base | % | Estado | Notas |
|---|---|---|---|---|---|
| TOFU-LAL-01 | LAL Compradores 1% | Custom: compradores 180d | 1% | ⏳ pendiente | Crear cuando pixel tenga ≥ 1.000 eventos purchase |
| TOFU-LAL-02 | LAL Compradores 3% | Custom: compradores 180d | 3% | ⏳ pendiente | Volumen alto, menor precisión |
| TOFU-LAL-03 | LAL Visitantes Tienda 1% | Custom: visitantes tiendanegocio.com 30d | 1% | ⏳ pendiente | Requiere pixel instalado |

---

## MOFU — Audiencias Tibias (consideración)

### Custom Audiences

| ID interno | Nombre en Ads Manager | Tipo | Ventana | Estado | Notas |
|---|---|---|---|---|---|
| MOFU-CA-01 | Visitantes Tienda 30d | Website visitors | 30 días | ⏳ pendiente pixel | Todos los que entraron a tiendanegocio.com |
| MOFU-CA-02 | Visitantes Producto 30d | Website: Product page views | 30 días | ⏳ pendiente pixel | Vieron un producto sin comprar (Alineado 2026) |
| MOFU-CA-03 | Video Views 25%+ 30d | Video engagement 25%+ | 30 días | ⏳ pendiente | Audiencia de interacción con videos de Reels |
| MOFU-CA-04 | IG Engagers 14d | Instagram account: Engaged | 14 días | Crear en BM | Interactuaron con la cuenta IG (Retargeting activo) |
| MOFU-CA-05 | FB Engagers 14d | Facebook page: Engaged | 14 días | Crear en BM | Interactuaron con la página FB |

---

## BOFU — Audiencias Calientes (retargeting / conversión)

### Custom Audiences

| ID interno | Nombre en Ads Manager | Tipo | Ventana | Estado | Notas |
|---|---|---|---|---|---|
| BOFU-CA-01 | Carrito Abandonado 90d | Add to cart, no purchase | 90 días | ⏳ pendiente pixel | Máxima intención, ampliado en 2026 para volumen |
| BOFU-CA-02 | Checkout Iniciado 30d | Initiate checkout, no purchase | 30 días | ⏳ pendiente pixel | Un paso más cerca que carrito |
| BOFU-CA-03 | Visitantes Tienda 30d | Website visitors | 30 días | ⏳ pendiente pixel | Ventana estándar para volumen de retargeting |
| BOFU-CA-04 | Compradores 180d | Purchase event | 180 días | ⏳ pendiente pixel | Para exclusión en prospección y cross-sell |

---

## Exclusiones Estándar

Aplicar estas exclusiones en TODOS los ad sets para evitar gastar en personas que ya convirtieron o que no corresponden al objetivo.

| Exclusión | Aplicar en | Motivo |
|---|---|---|
| Compradores 14d | TOFU y MOFU | No molestar a quien acaba de comprar |
| Compradores 30d | TOFU | Periodo de "descanso" post-compra |
| Empleados / propietarios | Todos | Excluir a Damaris y equipo |

---

## Reglas de Exclusión Cruzada por Etapa

```
TOFU ad sets → EXCLUIR: MOFU-CA-04, MOFU-CA-05, BOFU-CA-01, BOFU-CA-02, BOFU-CA-04
MOFU ad sets → EXCLUIR: BOFU-CA-01, BOFU-CA-02, BOFU-CA-04
BOFU ad sets → No excluir otras BOFU (puede superponerse en retargeting)
```

---

## Prioridad de Construcción

1. `MOFU-CA-04` y `MOFU-CA-05` — se pueden crear YA sin pixel (son de engagement IG/FB)
2. `BOFU-CA-01` al `BOFU-CA-04` — apenas instale pixel
3. `TOFU-LAL-01` — cuando haya ≥ 1.000 eventos purchase en el pixel
4. `TOFU-LAL-03` — cuando haya ≥ 1.000 visitantes únicos en pixel

---

## Actualización de este Archivo

Cada vez que se cree una audiencia nueva en Meta Business Manager:
1. Agregar fila a la tabla correspondiente
2. Cambiar Estado de ⏳ a ✅ cuando esté activa
3. Anotar fecha de creación y tamaño real en Notas
