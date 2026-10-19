# metads — Meta Ads Analytics para Miss Roure

Módulo de análisis de campañas Meta basado en la metodología **3Qs** (felipeverce/3Qs),
adaptado para el contexto de Miss Roure: moda argentina, precios en ARS, flujo tienda-first.

---

## Estructura

```
metads/
├── SKILL.md                        ← Skill principal para Claude — cargar esto al analizar campañas
│
├── scripts/
│   ├── utils.py                    ← Formateo ARS, benchmarks, evaluación de métricas
│   ├── analyze.py                  ← Analizador 3Qs de una campaña
│   └── weekly_report.py            ← Reporte semanal en markdown
│
├── audiences/
│   └── audience-library.md         ← Todas las audiencias TOFU/MOFU/BOFU documentadas
│
├── templates/
│   ├── ad-brief-template.md        ← Brief de creative antes de producir cualquier ad
│   └── creative-test-log.md        ← Registro de tests A/B de creatives
│
├── checklists/
│   ├── pre-launch.md               ← Verificar antes de lanzar cualquier campaña
│   └── landing-qa.md               ← Diagnosticar cuando CTR bueno pero ROAS malo
│
└── setup/
    ├── pixel-install.md            ← Instalar píxel en tiendanegocio.com ⏳
    ├── ads-account-ars.md          ← Crear/migrar cuenta de ads a ARS ⏳
    ├── system-user-token.md        ← System User Token en Meta BM ⏳
    └── utm-convention.md           ← Parámetros UTM para tracking post-click
```

---

## Setup requerido (pendiente)

| Paso | Guía | Estado |
|---|---|---|
| 1. Crear cuenta de ads en ARS | `setup/ads-account-ars.md` | ⏳ |
| 2. Instalar píxel en tienda | `setup/pixel-install.md` | ⏳ |
| 3. Crear System User Token | `setup/system-user-token.md` | ⏳ |

Completar en ese orden — el píxel requiere la cuenta ARS, y el token requiere ambos.

---

## Uso rápido

### Analizar una campaña (modo demo)

```bash
cd metads/scripts
python analyze.py --demo
```

### Analizar desde CSV exportado de Meta Ads Manager

```bash
python analyze.py --csv ruta/al/export.csv
```

### Generar reporte semanal

```bash
python weekly_report.py --demo
python weekly_report.py --csv export.csv --week 21 --out reporte-semana-21.md
```

### Modo interactivo (ingresar datos a mano)

```bash
python analyze.py
python weekly_report.py
```

---

## La Metodología 3Qs

Cada análisis responde tres preguntas en orden:

1. **Q1 — ¿Qué pasó?**: Diagnóstico numérico. Métricas clave en ARS, sin interpretación aún.
2. **Q2 — ¿Por qué?**: Comparación contra benchmarks. Identificar el factor limitante principal.
3. **Q3 — ¿Qué vamos a hacer?**: Una sola acción concreta. No listas — una decisión.

---

## Benchmarks de referencia (moda argentina, 2026)

| Métrica | Objetivo Roure |
|---|---|
| ROAS | ≥ 3x |
| CTR | > 1.2% |
| CPM | < $4.500 ARS |
| CPC | < $500 ARS |
| CPP | < 25% del AOV por categoría |
| Hook rate | > 35% |

> Actualizar benchmarks en ARS trimestralmente por inflación. Los porcentuales son estables.

---

## Canal de conversión

- **Primario**: roure.tiendanegocio.com — todos los CTAs de ads apuntan ahí
- **Secundario**: WhatsApp 1153837478 — solo consultas, nunca objetivo de campaña
- **Ventana de atribución**: 7-day click, 1-day view
