# Configuración de Dual Tracking: Píxel de Meta & Conversions API (CAPI)

last_updated: 2026-06-05
estado: 🟢 ACTIVO
responsable: growth-specialist
changelog: v1.1 — Redefinido como guía de configuración de rastreo dual (Píxel en navegador + CAPI del servidor) en Tienda Negocio con deduplicación por event_id.

---

## Por qué es prioridad #1: Mitigación del 30% de Pérdida de Señal

El rastreo tradicional basado únicamente en el navegador (Browser Pixel) pierde hasta un 30% de los eventos debido a bloqueadores de anuncios (ad-blockers), políticas de privacidad (iOS 14+) y restricciones de cookies. 
Para optimizar campañas de conversiones de manera eficiente en Roure (AOV objetivo $80.000 ARS y CPA máx $10.000 ARS), implementamos un sistema de **rastreo dual**:
1. **Píxel de Meta (Navegador)**: Captura las interacciones directas del lado del cliente.
2. **Conversions API / CAPI (Servidor)**: Envía los mismos eventos desde el servidor de Tienda Negocio de forma directa a Meta, garantizando la entrega del dato.

Para evitar la duplicación de métricas, ambos canales deben enviar un parámetro `event_id` coincidente para cada acción, permitiendo que Meta deduplique los eventos duplicados en tiempo real.

---

## Requisitos Previos

- [ ] Acceso de administrador al panel de `roure.tiendanegocio.com`.
- [ ] **Pixel ID** de Meta.
- [ ] **System User Token** (Token de Acceso de Usuario del Sistema) generado en el Business Manager de Meta (ver `system-user-token.md`).
- [ ] Acceso de administrador al Administrador de Eventos (Events Manager) de Meta.

---

## Paso 1: Configurar la Integración Nativa en Tienda Negocio

Tienda Negocio ofrece una integración nativa de rastreo dual que maneja la inyección de `event_id` automáticamente para la deduplicación.

1. Iniciar sesión en el panel administrador de **Tienda Negocio**.
2. Ir a **Configuración** → **Integraciones** o **Marketing** → **Meta Ads / Píxel**.
3. Activar la opción **Facebook Pixel & Conversions API (CAPI)**.
4. Pegar el **Pixel ID** de Meta (número de 15-16 dígitos).
5. Pegar el **System User Token** en el campo **Access Token (Token de Acceso CAPI)**.
6. Guardar los cambios.

---

## Paso 2: Parámetros Requeridos para Calidad de Evento y Deduplicación

Para que los eventos tengan una calificación de coincidencia (Event Match Quality - EMQ) óptima, Tienda Negocio envía:
* **Parámetros de Deduplicación**:
  * `event_name` (ej: `Purchase`, `InitiateCheckout`, `AddToCart`, `PageView`)
  * `event_id` (debe ser idéntico en el evento de navegador y en el de servidor para cada acción de la clienta)
* **Datos del Cliente (User Data)**:
  * Dirección IP del cliente (`client_ip_address`)
  * Agente de usuario del navegador (`client_user_agent`)
  * Correo electrónico (`em`), Teléfono (`ph`), Nombre/Apellido (hasheados en SHA-256)

---

## Paso 3: Protocolo de Verificación y Deduplicación (Test Events)

Es mandatorio verificar la correcta recepción y deduplicación de eventos usando la herramienta de prueba de Meta.

1. Ir al **Administrador de Eventos de Meta** → **Fuentes de datos** → Seleccionar el píxel de Roure.
2. Hacer click en la pestaña **"Probar eventos"** (Test Events).
3. Copiar el **Código de Prueba de Servidor** (ej: `TEST12345`).
4. Si Tienda Negocio lo solicita en su panel, pegar este código temporal para forzar los eventos de prueba del servidor.
5. Colocar la URL `https://roure.tiendanegocio.com` en el campo de prueba y abrir el sitio web.
6. Realizar las siguientes acciones simuladas:
   * Navegar por la página de inicio (`PageView`).
   * Ver un producto estrella como el *Sweater Bear* (`ViewContent`).
   * Agregar el producto al carrito (`AddToCart`).
   * Iniciar el proceso de compra (`InitiateCheckout`).
   * Completar una compra de prueba / simulación (`Purchase`).
7. **Verificar en la tabla de Eventos de Prueba**:
   * Cada evento debe mostrarse **dos veces**: uno con método "Navegador" (Browser) y otro con "Servidor" (Server).
   * En la columna de estado de deduplicación, debe decir: **"Deduplicado" (Deduplicated)**.
   * Expandir los detalles del evento para corroborar que el parámetro `event_id` es idéntico en ambas fuentes de señal.

---

## Monitoreo de Eventos en Producción

| Evento | Origen dual | Disparador en Tienda Negocio | Meta EMQ Target |
|---|---|---|---|
| `PageView` | Browser + Server | Carga de cualquier sección de la tienda | ≥ 6.0 |
| `ViewContent` | Browser + Server | Vista de ficha de producto individual | ≥ 6.5 |
| `AddToCart` | Browser + Server | Clic en el botón "Agregar al carrito" | ≥ 6.5 |
| `InitiateCheckout` | Browser + Server | Carga del primer paso del checkout | ≥ 7.0 |
| `Purchase` | Browser + Server | Carga de la página de confirmación/éxito | ≥ 8.0 |

Si el estado de deduplicación muestra advertencias o el EMQ cae por debajo de los targets establecidos, auditar la configuración de cookies y el System User Token de inmediato.

---

## Referencias

- Meta Pixel Helper (Extensión de Chrome)
- [Administrador de Eventos de Meta](https://business.facebook.com/events_manager2)
- Guía oficial de Conversions API de Meta: developers.facebook.com/docs/marketing-api/conversions-api
