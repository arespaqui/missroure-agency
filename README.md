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

- Cada vez que haya un nuevo ingreso de colección → actualizar `context/catalog-context.md`
- Cada vez que un post funcione bien → pedirle al agente que registre en `memory/wins.md`
- Cada vez que algo no funcione → pedirle que registre en `memory/losses.md`
- Una vez por mes → pedirle al agente el reporte mensual de performance

---

## Estructura del Sistema

```
missroure-agency/
│
├── AGENTS.md                       ← Leer SIEMPRE primero
├── README.md                       ← Esta guía
│
├── context/                        ← ADN permanente de la marca
│   ├── brand-context.md            ← Identidad, tono, canales, colecciones
│   ├── catalog-context.md          ← Catálogo completo con precios y stock
│   ├── audience-context.md         ← Perfil de la clienta ideal
│   ├── commercial-calendar.md      ← Fechas estratégicas del año
│   └── competitive-landscape.md    ← Radar de competencia
│
├── skills/                         ← Un archivo por rol de agencia
│   ├── brand-strategist.md         ← Posicionamiento, drops, campañas
│   ├── tiktok-strategist.md        ← Videos, hooks, scripts TikTok
│   ├── instagram-curator.md        ← Feed, reels, carruseles, estética IG
│   ├── copywriter.md               ← Captions, copies, descripciones
│   ├── ecommerce-specialist.md     ← Tienda, fichas de producto, conversión
│   ├── growth-analyst.md           ← KPIs, experimentos, métricas
│   ├── community-manager.md        ← UGC, respuestas, comunidad
│   └── editorial-calendar.md       ← Planificación semanal/mensual
│
├── memory/                         ← Sistema de aprendizaje continuo
│   ├── wins.md                     ← Lo que funcionó (con datos reales)
│   ├── losses.md                   ← Lo que no funcionó
│   ├── campaign-log.md             ← Registro cronológico de todo el contenido
│   ├── content-performance.md      ← Métricas acumuladas por formato y canal
│   └── experiments.md              ← Hipótesis activas y cerradas
│
└── templates/                      ← Estructuras reutilizables
    ├── weekly-calendar-template.md ← Planificación semanal
    ├── caption-template.md         ← Captions por canal y pilar
    ├── campaign-brief-template.md  ← Brief de cada campaña o drop
    └── product-description-template.md ← Descripciones para la tienda
```

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
