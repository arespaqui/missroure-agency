# Organización del proyecto — 2026-10-16

Los entregables se agrupan por función; los contratos de los agentes permanecen en sus rutas originales.

| Carpeta | Contenido |
|---|---|
| `inventory/` | Inventario operativo y ofertas de verano |
| `reports/2026-05/` | Informes de mayo, sin alterar sus archivos |
| `reports/scripts/` | Generador histórico y sus limitaciones preexistentes |
| `campaigns/2026-vienne/` | Material de estrategia de Vienne |
| `campaigns/2026-world-cup/` | Guías y fichas históricas del Mundial |
| `campaigns/meta-ads/` | Presentaciones y guías generales de creatividades |
| `research/competitors/` | Investigación de competidores |
| `assets/videos/`, `assets/creatives/` | Medios originales, sin conversiones |
| `data/meta-ads/` | Exportaciones CSV originales |
| `docs/theory/`, `docs/roadmap/`, `docs/sessions/` | Referencias, hoja de ruta y sesiones históricas |

`context/`, `memory/`, `skills/`, `metads/`, `templates/`, `ecommerce-bi/`, `odd/`, `AGENTS.md` y la configuración oculta no se trasladaron. Los informes y datos de Meta que ya estaban dentro de `metads/` siguen allí para conservar sus enlaces; no hay una copia paralela de esos datos.

## Trazabilidad
- [Manifiesto de movimientos](moves-2026-10-16.json): origen, destino, tamaño y SHA256 de los 30 archivos trasladados.
- Todos los destinos se comprobaron dentro del proyecto y sin colisiones antes del primer movimiento. No se sobrescribieron ni borraron entregables.
- Las fuentes históricas se preservan. Las referencias a archivos inexistentes se documentan, no se sustituyen por versiones supuestas.
- Los scripts históricos no se ejecutaron; sus dependencias externas preexistentes no forman parte de esta reorganización.
- [Seguimiento y verificación](../../odd/tasks/folder-structure-summer-inventory.md).
