# Miss Roure — Brand Agency OS

> "Romantic life starts in your closet" 🌷

Sistema operativo de agencia de marca completa para **@missroure**.
Un solo comando activa una agencia completa que conoce la marca, recuerda lo que funcionó y ejecuta sin fricción.

---

## Cómo Usar Este Sistema

### Para cualquier agente de IA (Claude Code, Cursor, Windsurf, etc.)

1. **Leer `AGENTS.md`** — el entry point universal. Todo arranca ahí.
2. El agente activará automáticamente el skill correcto según la tarea.
3. El sistema aprende solo — cada output queda registrado en `memory/`.

### Para Damaris

- Cada vez que haya un nuevo ingreso o cambio de stock → actualizar `inventory/`; usar `context/catalog-context.md` como referencia histórica hasta revalidarlo
- Cada vez que un post funcione bien → pedirle al agente que registre en `memory/wins.md`
- Cada vez que algo no funcione → pedirle que registre en `memory/losses.md`
- Una vez por mes → pedirle al agente el reporte mensual de performance

---

## Estructura del Sistema

```text
missroure-agency/
├── AGENTS.md                 # Instrucciones de entrada, sin cambio de ubicación
├── README.md                 # Mapa y accesos rápidos
├── inventory/                # Inventario operativo
│   └── summer-offers.md      # Ofertas de verano y stock por variante
├── context/                  # Marca, audiencia, catálogo histórico y temporada
├── campaigns/                # Entregables históricos por campaña
│   ├── 2026-vienne/
│   ├── 2026-world-cup/
│   └── meta-ads/
├── reports/                  # Informes entregables
│   ├── 2026-05/
│   └── scripts/              # Generador histórico, no portable todavía
├── research/competitors/     # Análisis de competencia
├── assets/
│   ├── videos/               # Videos originales
│   └── creatives/            # Fotos y piezas originales
├── data/meta-ads/             # Exportaciones CSV originales
├── docs/
│   ├── theory/               # Material de referencia
│   ├── roadmap/
│   ├── sessions/
│   └── organization/         # Manifiesto de movimientos y trazabilidad
├── metads/                   # Análisis, datos, guías y herramientas de Meta Ads
├── ecommerce-bi/             # Análisis de e-commerce
├── skills/                   # Roles de agencia
├── memory/                   # Historial y aprendizajes
├── templates/                # Plantillas reutilizables
└── odd/                      # Seguimiento de trabajo
```

### Estrategia vigente de esta campaña

[Fuente de verdad estratégica y aplicación a Roure](metads/strategy/2026-10-source-of-truth.md), basada en el [informe completo aportado por la marca](docs/theory/informe_meta_ads_2026_roure_con_profesor_charlie.md). Una campaña de Ventas y un conjunto inicial: buzos protagonistas más estáticas de ofertas de verano/invierno; **ARS $7.000 diarios en total**. Esta definición reemplaza las recetas anteriores de cuatro campañas y umbrales fijos para este lanzamiento. No hay publicación ni gasto remoto autorizado.

### Accesos rápidos
- [Inventario y ofertas de verano](inventory/README.md).
- [Temporada actual](context/season-2026-10.md).
- [Análisis de Meta Ads](metads/season-2026-10-index.md).
- [Informes de mayo](reports/2026-05/).
- [Registro de organización](docs/organization/README.md).

Las rutas históricas de `context/`, `skills/`, `memory/` y los módulos se conservan. Las carpetas ocultas de configuración no se movieron. Los precios antiguos no se trasladan al inventario actual como hechos confirmados.

---

## Convención de Commits

```
feat(context):    Actualización de archivos de contexto
feat(skill):      Nuevo skill o mejora de skill existente
memory(win):      Registro de contenido exitoso
memory(loss):     Registro de contenido fallido
memory(exp):      Nuevo experimento o cierre de experimento
chore(template):  Actualización de templates
```

**Ejemplo de commit al actualizar el catálogo:**
```
feat(catalog): ingreso colección invierno 2026 — 8 nuevos productos
```

---

## El Loop de Aprendizaje

```
Publicar contenido
      ↓
Registrar en campaign-log.md
      ↓
Medir a las 48-72h
      ↓
WIN → wins.md + regla confirmada
LOSS → losses.md + hipótesis
      ↓
El agente lee esto antes del próximo contenido
      ↓
El sistema mejora solo
```

---

## Stack Técnico

| Componente | Tecnología |
|---|---|
| Repositorio | GitHub Privado |
| Formato de archivos | Markdown (.md) |
| Agente principal | Claude Code |
| Entry point | AGENTS.md |
| Versionado | Git con convención de commits |
| Compatible con | Cursor, Windsurf, cualquier agente que lea markdown |
