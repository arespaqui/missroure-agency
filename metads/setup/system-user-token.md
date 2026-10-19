# System User Token — Meta Business Manager

last_updated: 2026-05-25
estado: ⏳ PENDIENTE
responsable: Ares
propósito: Conectar 3Qs scripts con la API de Meta Ads para análisis automatizado

---

## Para qué sirve esto

El System User Token es una credencial de larga duración (no expira) que le permite a los scripts de `metads/scripts/` leer datos de campañas directamente desde la API de Meta, sin tener que exportar CSVs manualmente.

Permisos necesarios:
- `ads_read` — leer métricas de campañas, ad sets, ads
- `business_management` — leer estructura de la cuenta de negocio

---

## Paso 1 — Acceder a la configuración de usuarios del sistema

1. Ir a **Meta Business Manager** → business.facebook.com
2. Menú izquierdo: **Configuración del negocio** → **Usuarios** → **Usuarios del sistema**
3. Si no ves esta opción, necesitás rol de **Administrador** en el Business Manager

---

## Paso 2 — Crear el System User

1. Clic en **"Agregar"** (botón azul)
2. Configurar:
   - **Nombre**: `roure-3qs-api` (o similar — sin espacios para fácil referencia)
   - **Rol**: **Empleado** (no necesita Admin — menos permisos = más seguro)
3. Clic en **"Crear usuario del sistema"**

---

## Paso 3 — Asignar activos al System User

El System User necesita acceso explícito a los activos que va a leer.

1. En la pantalla del System User recién creado → clic en **"Asignar activos"**
2. Asignar los siguientes activos con los permisos indicados:

| Activo | Tipo | Permiso |
|---|---|---|
| Cuenta publicitaria de Miss Roure (ARS) | Cuenta publicitaria | Analista de anuncios (Solo lectura) |
| Miss Roure Pixel | Píxel | Ver |
| Página de Miss Roure (Instagram/FB) | Página | Solo lectura |

> **Importante**: No dar permisos de edición ni de administrador. Los scripts solo necesitan leer datos.

---

## Paso 4 — Generar el token

1. En la pantalla del System User → clic en **"Generar token nuevo"**
2. Seleccionar la **App** (si no tenés app de Meta creada, ver nota abajo)
3. Seleccionar los permisos:
   - ✅ `ads_read`
   - ✅ `business_management`
   - ✅ `ads_management` (opcional — solo si querés poder crear/pausar desde scripts en el futuro)
4. Clic en **"Generar token"**
5. **COPIAR EL TOKEN INMEDIATAMENTE** — Meta solo lo muestra una vez

---

## Nota: ¿Qué app usar?

Si no tenés una app de Meta creada para este negocio:

1. Ir a **developers.facebook.com** → **Mis apps** → **Crear app**
2. Tipo de app: **Negocio**
3. Nombre: `MissRoure3Qs` (sin espacios)
4. Cuenta de Business Manager: seleccionar la de Miss Roure
5. Crear la app
6. Volver al paso 4 y seleccionar esta app al generar el token

> La app no necesita pasar revisión de Meta para uso interno/personal. Puede quedarse en modo Desarrollo.

---

## Paso 5 — Guardar el token de forma segura

**NUNCA commitear el token en git.** Guardarlo en:

```
# En el directorio metads/ crear un archivo .env (ya está en .gitignore)
META_ACCESS_TOKEN=EAAxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx
META_AD_ACCOUNT_ID=act_XXXXXXXXXXXXXXXX  # la cuenta en ARS
META_PIXEL_ID=XXXXXXXXXXXXXXXX
META_BUSINESS_ID=XXXXXXXXXXXXXXXX
```

El archivo `.env` debe estar en `.gitignore`. Verificar:

```
# En missroure-agency/.gitignore agregar si no está:
metads/.env
metads/scripts/.env
*.env
```

---

## Paso 6 — Probar el token

```bash
# Verificar que el token funciona
curl "https://graph.facebook.com/v21.0/me?access_token=TU_TOKEN_AQUI"
# Debe devolver: {"id":"...", "name":"roure-3qs-api"}

# Verificar acceso a la cuenta de ads
curl "https://graph.facebook.com/v21.0/act_TU_AD_ACCOUNT_ID/campaigns?access_token=TU_TOKEN"
# Debe devolver lista de campañas
```

---

## Paso 7 — Configurar los scripts para usar el token

Una vez que tenés el `.env` creado, los scripts de Python lo van a leer automáticamente cuando se agregue soporte de API (v2 de los scripts).

Por ahora los scripts usan CSV export. La integración con API viene en la próxima iteración.

---

## Si el token expira o se revoca

Los System User Tokens **no expiran** a menos que:
- Elimines el System User
- Revoques manualmente el token
- La app sea eliminada o deshabilitada

Si necesitás regenerar: volver al paso 4.

---

## Checklist

- [ ] System User `roure-3qs-api` creado en Business Manager
- [ ] Activos asignados (cuenta publicitaria ARS, píxel, página)
- [ ] Token generado con permisos `ads_read` + `business_management`
- [ ] Token guardado en `metads/.env` (fuera de git)
- [ ] `.gitignore` actualizado para excluir `.env`
- [ ] Token verificado con curl o Postman
