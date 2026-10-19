# Cuenta de Meta Ads en ARS — Guía de Resolución

last_updated: 2026-05-25
estado: ⏳ PENDIENTE
responsable: Ares

---

## Contexto del Problema

La cuenta de ads conectada actualmente es **act_428789502681260** — está en **PEN (soles peruanos)**, es una cuenta personal de Ares, y tiene $0 gastados. No es la cuenta de negocio de Miss Roure Argentina.

**No se puede cambiar la moneda de una cuenta existente.** Una vez creada en PEN, queda en PEN para siempre. La solución es crear una cuenta nueva en ARS.

---

## Opciones

### Opción A — Crear una cuenta de anuncios nueva en ARS (recomendada)

Es la opción correcta. La cuenta vieja en PEN no se usa para Roure.

**Paso a paso:**

1. Ir a **Meta Business Manager** → business.facebook.com
2. En el menú izquierdo: **Configuración del negocio** → **Cuentas** → **Cuentas publicitarias**
3. Clic en **"Agregar"** → **"Crear una cuenta publicitaria nueva"**
4. Configurar:
   - **Nombre**: "Miss Roure Argentina" (o "Roure - Ads")
   - **Moneda**: **ARS — Peso argentino** ← esto es lo crítico
   - **Zona horaria**: America/Argentina/Buenos_Aires (UTC-3)
   - **País**: Argentina
5. Asignar a la cuenta de negocio de Miss Roure (no a perfil personal)
6. Agregar método de pago argentino (tarjeta de débito/crédito argentina o transferencia)

> **Importante sobre el método de pago**: Meta acepta tarjetas Visa/Mastercard emitidas en Argentina. También acepta PayPal. Si usás tarjeta argentina, los cargos van directo en ARS y el banco puede aplicar recargo del 30% PAIS o similar — tenerlo en cuenta al calcular el budget real.

---

### Opción B — Usar la cuenta en PEN adaptando los presupuestos

**No recomendada.** Vas a confundir ARS con PEN en todos los reportes y las métricas de los scripts van a estar incorrectas. La deuda técnica vale más que el tiempo de configurar una nueva cuenta.

---

## Sobre los impuestos en Argentina (importante)

Meta cobra un **impuesto adicional sobre servicios digitales** en Argentina. Al 2026, los cargos de Meta Ads en Argentina tienen:

- IVA 21% sobre el gasto
- Percepción SICORE / RG 2 según situación fiscal

Si Miss Roure está como **Monotributista**: el cargo de Meta viene con IVA incluido, no recuperable.
Si está como **Responsable Inscripto**: puede usar el IVA como crédito fiscal.

**Recomendación**: coordinar con contador antes de invertir sumas grandes.

---

## Método de pago recomendado para Argentina

1. **Tarjeta de crédito argentina** (Visa/Mastercard) — más simple, cargos automáticos
2. **Tarjeta prepaga** (ej: Mercado Pago) — más control del gasto, sin sorpresas en la factura

**Agregar el método de pago:**
- En Business Manager → Configuración del negocio → Pagos
- O directamente desde el Administrador de Anuncios al crear la primera campaña

---

## Budget inicial recomendado para Roure

Para testear sin riesgo y acumular datos para el píxel:

| Fase | Budget semanal | Objetivo |
|---|---|---|
| Test inicial (semana 1-2) | $14.000 – $21.000 ARS | Validar audiencias y creative |
| Escala lenta (semana 3-4) | $28.000 – $42.000 ARS | Optimización con datos |
| Escala real (semana 5+) | $56.000+ ARS | ROAS objetivo ≥ 3x |

> Recordá: Meta necesita al menos 50 compras/semana para optimizar bien. Al principio el ROAS va a ser bajo — es normal. El crecimiento viene con datos.

---

## Checklist de creación de cuenta

- [ ] Cuenta creada en ARS, huso horario Argentina
- [ ] Asignada al Business Manager de Miss Roure (no a perfil personal)
- [ ] Método de pago argentino configurado
- [ ] Píxel de Miss Roure asignado a esta cuenta (ver `pixel-install.md`)
- [ ] System User Token con permisos sobre esta cuenta (ver `system-user-token.md`)
- [ ] Cuenta vieja (PEN) desvinculada o ignorada para campañas de Roure
