# Organización de carpetas e inventario de verano
Objetivo: ordenar entregables existentes y habilitar una zona de ofertas vigentes. Rama: master; Git no permite crear la rama de trabajo en esta sesión.
Entrega: local, sin publicación; rutas canónicas preservadas. Previsión: menos de 300 líneas nuevas, movimientos sin cambios de contenido y manifiesto generado excluidos. Verificación: SHA256, enlaces y auditoría independiente de rutas.

## Specs
- S1: "che primero quiero que estructures bien las carpetas porfavor" — separar reportes, campañas, investigación, recursos, datos y referencias; conservar todos los archivos y las carpetas canónicas context, memory, skills, metads, templates, ecommerce-bi y odd. Actualizar README y referencias de los archivos trasladados.
- S2: "y añade en inventario una zona para nuestros porudcos en iferta de verano que tenemos ahora" — crear inventory con ofertas de verano publicadas y espacio para cantidades, variantes y validación. Fuente pública fechada; no inventar stock físico ni descuentos acumulables.

## Tasks
- T1 | S1 | inline; mapa delegado por presupuesto de evidencia | completado localmente: 30 archivos trasladados y README actualizado; commit pendiente por bloqueo de Git.
- T2 | S2 | inline; escritura entendida con catálogo público | completado localmente: inventario con 21 productos publicados, zona de variantes y acceso desde catálogo; stock físico pendiente, commit pendiente.
- T3 | S1–S2 | verificación propia y verificador independiente por riesgo de referencias compartidas | verificado: S1 PASS y S2 PASS; 30 hashes/tamaños intactos y 17 enlaces válidos.

## Log
L1 — Solicitud original: "che primero quiero que estructures bien las carpetas porfavor, y añade en inventario una zona para nuestros porudcos en iferta de verano que tenemos ahora"
L2 — Estado inicial: numerosos cambios y archivos no versionados previos del usuario. No se restablecen ni sobrescriben. Se mantiene master porque el intento anterior de crear una rama falló incluso con ejecución aprobada; no se repite ni se modifican permisos Git. Commit pendiente.
L3 — Explorador folder_map: rutas canónicas se conservan. Videos 8 archivos, creativos 3, CSV 1, teoría 2. Dos enlaces de videos del brief Vienne ya apuntaban a nombres inexistentes; no seleccionar variantes en nombre del usuario. Generador de informe JS conserva dependencias y destino absolutos de otro entorno: incidencia preexistente, fuera del ordenamiento.
L4 — Pruebas: no aplica RED/GREEN funcional a movimientos de documentos y medios. Capturar hashes antes del traslado y compararlos después; verificar referencias existentes y explicar enlaces ya rotos. Ningún borrado ni sobrescritura de destinos.
L5 — Tienda pública consultada 2026-10-16: Spring Summer, tops/sets/vestidos en oferta. Solo la ficha Top Princesa se pudo leer en detalle; el resto se carga como productos publicados, sin inventar cantidades o precio final por variante.
L6 — Movimientos registrados antes de ejecutarlos en docs/organization/moves-2026-10-16.json: 30 archivos, destinos comprobados dentro del proyecto y sin colisiones. Todos conservan SHA256 y tamaño. No se borraron entregables ni se cambió el contenido de archivos trasladados. Pasada de referencias relativas: cero enlaces adicionales requirieron ajuste; dos referencias de video ya rotas ahora remiten al directorio de variantes con advertencia, y una ruta de foto se actualizó explícitamente.
L7 — Inventario: 21 productos publicados (8 tops, 4 sets, 9 vestidos), sin afirmar existencias. Top Princesa lista $7.000 y transferencia $5.600, importes anteriores separados; conflicto de color Negro/amarillo documentado. Fichas restantes y cantidades pendientes. No se tocó la tienda ni Meta.
L8 — Verificación propia observada: 30 hashes sin cambios, 17 enlaces locales válidos, ruta de foto válida, carpetas canónicas presentes y git diff --check sin errores (solo aviso LF/CRLF). Sin ejecución del generador histórico no portable ni renderizado de binarios: contenido de esos archivos intacto.
L9 — Verificador independiente folder_inventory_verify, modelo gpt-5.6-sol/medium, probes desde scratch en temp: S1 PASS y S2 PASS; 30/30 tamaños/hashes, cero rutas faltantes o fuera del workspace, 17 enlaces y 21 productos confirmados como registro publicado. No encontró bloqueadores causados por el cambio. skill_resolution: paths-injected.
L10 — Espejo Engram rechazado: "Codex host session is not registered; start a new Codex session to register it." No se inventó identidad. Entrega local verificada; commit y copia persistente pendientes por entorno. No se afirma aprobación nativa, push o publicación.
