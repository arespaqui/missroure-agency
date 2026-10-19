# Generadores históricos de informes

`roure_informe_mayo2026.js` se conserva sin cambios de contenido como fuente del informe de mayo. El documento generado está en [reports/2026-05](../2026-05/).

No se considera un generador portable: ya dependía de `docx` bajo `/tmp/npm_global/` y escribía a una ruta absoluta de otro entorno bajo `/sessions/`. El ordenamiento no instala dependencias ni ejecuta o repara este script. No usarlo para regenerar entregables sin una adaptación explícita posterior.
