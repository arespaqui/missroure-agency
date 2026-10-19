# Strategy: Sweater Vienne — ASC — Junio 2026

**Versión**: 1.0
**Fecha**: 2026-06-05
**Producto**: Sweater Vienne (Cuello Bote) — 4 colores
**Campaña base**: Ver `brief-vienne-asc.md`

---

## Objetivo de la campaña

Generar ventas directas del Sweater Vienne con un CPA ≤ $10.000 ARS y ROAS ≥ 3x, usando una única campaña ASC que maneja prospecting y remarketing automáticamente.

---

## Estructura de Presupuesto por Fases

### Fase 1 — Aprendizaje (Días 1 al 7)

**Budget**: $5.000 ARS/día  
**Total estimado**: $35.000 ARS  
**Regla de oro**: NO tocar nada — ni presupuesto, ni creativos, ni configuración.

Meta necesita tiempo para optimizar la entrega. Cualquier cambio en esta fase puede resetear el algoritmo y desperdiciar los datos acumulados.

#### Lectura diagnóstica en Día 3 (8 de junio)

Esta lectura es para detectar desastres, no para tomar decisiones de escala.

| Señal | Métrica | Umbral de alarma |
|---|---|---|
| Creativos no funcionan | Hook Rate | < 20% en ambos ads |
| Nadie llega al producto | CTR | < 0.5% |
| CPM anómalo | CPM | > $6.000 ARS |
| El pixel no dispara | Compras registradas | 0 con tráfico real |

**Si se dispara una alarma** → pausar y revisar antes de continuar. No aumentar budget.  
**Si todo está dentro de rango** → cerrar el dashboard y no volver hasta el Día 7.

---

### Fase 2 — Evaluación y Decisión (Día 7 — 12 de junio)

Con 7 días de datos, se toma la primera decisión real de escala.

#### Métricas de evaluación completa

| Métrica | Objetivo | Mínimo aceptable |
|---|---|---|
| Hook Rate | ≥ 35% | ≥ 25% |
| Hold Rate | ≥ 15% | ≥ 10% |
| CTR | > 1.2% | > 0.8% |
| CPP (Costo por Compra) | ≤ $10.000 ARS | ≤ $15.000 ARS |
| ROAS | ≥ 3x | ≥ 2x |
| CPM | < $4.500 ARS | < $6.000 ARS |

#### Árbol de decisión

```
¿CPP ≤ $10.000 ARS y ROAS ≥ 3x?
├── SÍ → Escenario A: Escalar
└── NO
    ├── CPP entre $10k-$15k y ROAS ≥ 2x → Escenario B: Mantener
    └── CPP > $15k o ROAS < 2x → Escenario C: Pausar y diagnosticar
```

#### Escenario A — Escalar

Budget diario objetivo según performance:

| ROAS obtenido | Incremento | Budget nuevo |
|---|---|---|
| 3x - 4x | +20% | $6.000 ARS/día |
| 4x - 5x | +40% | $7.000 ARS/día |
| > 5x | +60% | $8.000 ARS/día |

**Regla de escalado**: nunca subir más del 40-50% en un solo cambio — Meta puede interpretar un aumento brusco como una campaña nueva y resetear la entrega. Esperar 3 días después de cada cambio antes del próximo.

#### Escenario B — Mantener

Dejar el budget en $5.000 ARS/día por 7 días más y revisar si el algoritmo mejora con más datos. Evaluar si el problema es el creativo (Hook/Hold Rate bajos) o el precio/producto (CTR alto pero CPP alto).

#### Escenario C — Pausar y diagnosticar

| Síntoma | Diagnóstico probable | Acción |
|---|---|---|
| Hook Rate < 20% | El primer segundo del video no engancha | Nuevo creativo con hook más directo |
| CTR < 0.8% | El copy o el precio no convence | Revisar copy racional, agregar precio visible en el visual |
| CTR alto pero CPP alto | La landing page no convierte | Revisar URL de destino, precio visible, proceso de compra |
| CPM > $6.000 | Poca demanda o audiencia saturada | Revisar si hay otras campañas activas compitiendo |

---

### Fase 3 — Consolidación (Día 14 en adelante)

Si la campaña tuvo buen rendimiento en Fase 2:

- Evaluar si escalar más budget o abrir una segunda ASC con creativos frescos
- Revisar el límite de clientes existentes (10%) — si el ROAS es alto, se puede subir al 20-25% para aprovechar el remarketing automático
- No crear una campaña de retargeting separada — Meta lo maneja dentro de la ASC con el cap de clientes existentes

---

## Lo que NO hacer

- Cambiar el budget antes del Día 7 salvo alarma en Día 3
- Crear una campaña de retargeting separada (genera overlap de audiencia y fragmenta el learning)
- Pausar y reactivar la campaña (resetea el aprendizaje completamente)
- Editar el copy o los creativos durante Fase 1 (Meta vuelve a empezar a probar)
- Tocar las audiencias o placements (la ASC las maneja sola)

---

## Timeline

| Fecha | Acción |
|---|---|
| 2026-06-05 | Lanzamiento — activar campaña en Meta Ads Manager |
| 2026-06-08 (Día 3) | Lectura diagnóstica — solo mirar, no tocar salvo alarma |
| 2026-06-12 (Día 7) | Evaluación completa — decisión de escala según árbol de decisión |
| 2026-06-19 (Día 14) | Revisión de consolidación — ¿escalar más o abrir segundo creativo? |

---

## Referencia de archivos

- Brief completo: `memory/brief-vienne-asc.md`
- Log de campaña: `memory/campaign-log.md`
- Checklist pre-launch: `metads/checklists/pre-launch.md`
- Convención UTM: `metads/setup/utm-convention.md`
- Script de análisis: `metads/scripts/analyze.py`
