# Pre-Launch Checklist — Miss Roure Meta Ads

Completar ANTES de activar cualquier campaña nueva o ad set nuevo.
No se lanza nada sin pasar por esta lista. Cada ítem tiene una razón.

---

## Checklist de Campaña

### Configuración de Cuenta

- [ ] Cuenta de ads configurada en ARS (ver `setup/ads-account-ars.md`)
- [ ] Pixel instalado y verificado en roure.tiendanegocio.com (ver `setup/pixel-install.md`)
- [ ] Evento `Purchase` disparando correctamente en Test Events del BM
- [ ] Ventana de atribución: **7-day click, 1-day view** ← no cambiar esto

### Estructura de Campaña

- [ ] Objetivo de campaña correcto: **Conversiones** (si hay pixel) o **Tráfico** (si no hay pixel aún)
- [ ] CBO o ABO documentado — si es CBO, anotar el budget total; si es ABO, anotar budget por ad set
- [ ] Nombre de campaña sigue la convención: `[Producto/Colección] — [Etapa] — [Fecha inicio]`
  - Ejemplo: `Tapados Otoño — TOFU — 2026-05-27`

### Configuración del Ad Set

- [ ] Audiencia elegida de `audiences/audience-library.md` — no crear audiencias ad hoc
- [ ] Exclusiones estándar aplicadas (ver sección "Exclusiones Estándar" en audience-library.md)
- [ ] Ubicaciones: **Automáticas** (no manual — Meta optimiza mejor)
- [ ] Presupuesto mínimo operacional: **$7.000 ARS/semana** por ad set
- [ ] Fecha de fin: NO configurar (dejar correr hasta decisión manual)
- [ ] Budget mínimo para salir del aprendizaje: **$14.000 ARS en 7 días**

### El Creative

- [ ] Brief completado en `templates/ad-brief-template.md`
- [ ] Producto en stock confirmado en `context/catalog-context.md`
- [ ] URL de destino verificada: abrir el link y confirmar que carga el producto correcto con precio visible
- [ ] Precio visible en el ad (ya sea en el copy o en el visual) — es el driver #1 en Argentina
- [ ] 20% OFF por transferencia mencionado si aplica
- [ ] Formato correcto para la ubicación (9:16 para Stories/Reels, 1:1 para Feed)
- [ ] Sin texto que tape caras o el producto principal
- [ ] Copy: headline ≤ 40 caracteres que se ven antes del "ver más"

### Tracking

- [ ] UTM configurado según `setup/utm-convention.md`
  - `utm_source=facebook&utm_medium=paid&utm_campaign=[nombre-campaña]`
- [ ] Nombre del ad incluye el ID del test si es parte de un A/B (ej: `[TEST-001-A]`)

---

## Checklist Express (ads de urgencia — mínimo indispensable)

Si hay que lanzar rápido, al menos verificar:

- [ ] Stock del producto confirmado
- [ ] URL de destino funciona y carga el producto correcto
- [ ] Pixel instalado y evento Purchase activo
- [ ] Exclusión de compradores recientes aplicada
- [ ] Budget > $7.000 ARS/semana

---

## Post-Launch (primeras 24-48hs)

- [ ] Confirmar que el ad está en estado "Activo" (no rechazado)
- [ ] Verificar que el pixel está registrando eventos (verificar en Events Manager)
- [ ] Anotar el ad en `memory/campaign-log.md` con fecha de inicio y objetivo
- [ ] Poner reminder para revisar a las 72hs con `scripts/analyze.py`
