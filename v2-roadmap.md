# Roadmap v2.0 — Miss Roure Brand Agency OS

version: 0.1
last_updated: 2026-05-04
updated_by: Ares Palomino

---

## Problema identificado en v1.0

El sistema actual usa archivos MD con contexto fijo. Esto genera dos riesgos:

1. **Ventana de contexto**: AGENTS.md + skills + memory se cargan en cada sesión y consumen contexto rápidamente.
2. **Respuestas predecibles**: contexto fijo = respuestas que repiten los mismos patrones. El sistema no itera ni sorprende.

---

## Opciones evaluadas para v2.0

### Opción A — Contexto dinámico por tarea
El agente carga solo los archivos relevantes para la tarea puntual.
- TikTok script → solo tiktok-strategist + wins TikTok
- Calendario → solo editorial-calendar + commercial-calendar
- **Pro**: contexto mínimo y específico, nunca fijo
- **Con**: requiere protocolo claro de qué cargar cada vez; si falla, pierde aprendizaje

### Opción B — Memory como motor de evolución
El sistema mejora porque wins.md y losses.md crecen con cada publicación.
- El contexto "fijo" es solo la identidad de marca
- Lo que cambia y evoluciona es la memoria acumulada
- **Pro**: simple, sin desarrollo técnico adicional
- **Con**: depende de que Damaris actualice la memoria regularmente

### Opción C — Arquitectura con agentes especializados (recomendada)
Agentes separados construidos con Claude API:
- Un agente por rol (TikTok, análisis, calendario, copy)
- Cada uno tiene contexto mínimo propio
- Se comunican entre sí para tareas complejas
- El contexto no es fijo — cada agente recibe solo lo que necesita
- **Pro**: escala bien, elimina el problema de contexto fijo, respuestas más variadas y contextuales
- **Con**: requiere desarrollo real con Claude API — ya no es un sistema de archivos MD

---

## Decisión pendiente para v2.0

Evaluar Opción C como arquitectura target. Requiere:
- [ ] Definir qué agentes se construyen (mínimo: TikTok, Instagram, Growth, Editorial)
- [ ] Diseñar cómo se pasan contexto entre agentes
- [ ] Decidir dónde vive la memoria (base de datos vs archivos vs embeddings)
- [ ] Definir la interfaz para Damaris (¿chat? ¿formulario? ¿WhatsApp bot?)

---

## Estado

v1.0 completa y operativa. v2.0 en evaluación.
