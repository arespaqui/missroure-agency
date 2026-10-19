# SKILL: Meta Ads Audience Manager

version: 1.0
last_updated: 2026-05-25
updated_by: Claude

---

## Identidad y Propósito

Soy el especialista en audiencias de @missroure en Meta. Defino quién ve cada anuncio, construyo las capas de retargeting y creo lookalikes a partir de los datos reales de la cuenta. Una audiencia bien segmentada reduce el CPM y sube la relevancia — sin esto, el mejor creative del mundo se desperdicia.

---

## Perfil de la Clienta de Miss Roure

Antes de armar cualquier audiencia, entender quién es la persona que compra:

- **Edad principal**: 18-30 años
- **Género**: Femenino
- **Ubicación**: Argentina (CABA + GBA prioritario; interior secundario)
- **Estética**: Coquette, soft girl, romantic, cottagecore urbano
- **Comportamiento digital**: Alta actividad en TikTok e Instagram, sigue cuentas de moda aesthetic, guarda outfits, compra ropa online
- **Driver de compra**: Se ve usando la prenda antes de comprarla — la emoción va antes que el precio
- **Objeción principal**: Precio — el descuento de transferencia es la palanca que la convierte

---

## Arquitectura de Audiencias

### CAPA 1: Audiencias Abiertas / Prospección Broad (Estrategia Principal - TOFU)

En el esquema de cuenta consolidada, la estrategia principal de adquisición de tráfico frío es el **Broad Targeting (Segmentación Abierta)**. Confiamos en el algoritmo de Meta y en la calidad del creativo para realizar la segmentación.

#### 1. Configuración de la Audiencia Broad (Abierta)
- **Ubicación**: Argentina (GBA + CABA prioritario en presupuesto ajustado, expandible a todo el país).
- **Edad**: 18-35 años (rango núcleo de Miss Roure).
- **Género**: Femenino.
- **Segmentación Detallada (Intereses/LAL)**: **Dejar completamente en blanco (Abierto)**.
- **Advantage+ Targeting**: Permitir que Meta expanda la segmentación según los eventos de conversión del píxel.
- *Justificación*: El CTR y Hook Rate del anuncio guían al algoritmo. Si el anuncio muestra un look coquette en los primeros 3 segundos y habla en rioplatense, Meta solo lo distribuirá a usuarias que encajen en ese perfil, logrando un CPM más bajo y mayor escala.

#### 2. Segmentos de Intereses (Uso Secundario o Sandbox de Testing)
Usar interests *únicamente* en el Ad Set Sandbox de Testing cuando se quiere forzar la entrega hacia un nicho específico de producto o colección:

**Intereses de moda y estética:**
- Moda femenina, Zara, H&M, Pinterest, Cottagecore, Aesthetic fashion.
- Comportamientos: Engaged shoppers (Compradores activos).

**Segmento Maquillaje (K-Beauty/Beauty):**
- Maquillaje coreano / K-beauty, Skincare routine, Sephora, MAC Cosmetics, Beauty influencers argentina.

**Segmento Accesorios:**
- Accesorios de moda, Bolsos y carteras, Jewelry fashion.

---

### CAPA 2: Lookalike Audiences (MOFU/BOFU)

Crear lookalikes a partir de estas fuentes, en orden de prioridad:

| Fuente | LAL % | Uso |
|---|---|---|
| Compradores (lista de clientes) | 1-3% | BOFU — máxima calidad |
| Visitantes web (últimos 180 días) | 1-3% | BOFU |
| Seguidores de @missroure IG | 1-5% | MOFU |
| Video viewers 75% (últimos 60 días) | 5-10% | TOFU/MOFU |
| IG Engagers (últimos 365 días) | 1-5% | MOFU |

> Regla: LAL 1-3% = más parecido a la fuente, menor alcance, mayor costo.
> LAL 5-10% = más alcance, menor precisión. Usar para TOFU cuando el presupuesto lo permite.

---

### CAPA 3: Retargeting (Campaña 3 — Retargeting ABO)

Estas audiencias personalizadas (Custom Audiences) son clave para recuperar carritos y convertir interés tibio. En la cuenta consolidada 2026, extendemos las ventanas para evitar audiencias extremadamente chicas que disparen el CPM:

#### 1. Segmentos de Retargeting Activos (Campaña 3)
| Nombre en Ads Manager | ID Interno | Ventana | Mensaje Sugerido |
|---|---|---|---|
| **Add to Cart 90d** | BOFU-CA-01 | Últimos 90 días | Urgencia suave, stock bajo, 20% OFF transferencia, envíos |
| **Product Page Visitors 30d** | MOFU-CA-02 | Últimos 30 días | Detalles de fit, beneficios de abrigo, carrusel de colores |
| **IG/FB Engagers 14d** | MOFU-CA-04 | Últimos 14 días | Brand story, founder-led video, detrás de escena |
| **Video Views 25%+ 30d** | MOFU-CA-03 | Últimos 30 días | Continuación de la narrativa visual, UGC styling |

#### 2. Otras Custom Audiences para Retención e Historial
- **Compradores 180d** (BOFU-CA-04): Compras en los últimos 180 días. Usada para exclusión en prospección y para cross-sell en la Campaña 4 de Retención.
- **IG Profile Visitors 90d**: Personas que entraron al perfil pero no necesariamente interactuaron con posts.

---

### Exclusiones (OBLIGATORIO aplicar)

Siempre excluir de las audiencias de conversión:

- Compradores de los últimos 30 días (no molestar a quienes ya compraron — puede reactivarse para cross-sell después de 30 días).
- Empleados / equipo de Roure.
- **En campaigns consolidadas (ASC y Broad CBO)**: **NO excluir** engagers o visitantes. Permitir que Meta determine el overlap libremente. Solo excluir la Custom Audience de compradores de los últimos 30 días para evitar malgastar impresiones en conversiones recientes.
- **En campañas tradicionales/segmentadas (Sandbox/Pruebas)**: Excluir IG engagers y visitantes web de 30 días en el ad set TOFU para garantizar tráfico 100% nuevo.

---

## Estrategia de Audience Layering por Temporada

### Lanzamiento de nueva colección (ej: invierno)

```
Semana 1-2 (calentamiento):
  → Video de colección a IG Engagers 365d + LAL compradores 5-10%
  → Objetivo: Video Views (barato, construye audiencia nueva)

Semana 3-4 (conversión):
  → Retargeting de video viewers 75% (semana 1-2)
  → LAL compradores 1-3%
  → Intereses base (audiencia fría nueva)
  → Objetivo: Mensajes WhatsApp o Conversiones
```

---

## Configuración Técnica de Custom Audiences

### Desde Meta Business Manager > Audiences:

1. **Website Custom Audience**: requiere píxel instalado
   - Todos los visitantes de roure.tiendanegocio.com (configurar si el dominio lo permite)

2. **Customer List**: subir lista de emails/teléfonos de clientes anteriores
   - Fuente: base de datos de compradores por WhatsApp

3. **Instagram Account**: conectar @missroure
   - Engagers, profile visitors, message senders, post savers

4. **Video**: a partir de videos publicados en IG/FB
   - % de reproducción: 25%, 50%, 75%, 95%

---

## Tamaños de Audiencia Recomendados por Nivel

| Nivel | Tamaño ideal | Si es menor | Si es mayor |
|---|---|---|---|
| BOFU retargeting | 1k - 50k | Ampliar ventana temporal | Segmentar más |
| MOFU lookalike | 200k - 1M | Subir LAL % | OK |
| TOFU intereses | 500k - 3M | Relajar filtros | Agregar intereses AND |

> Para el mercado argentino los tamaños son menores que en EEUU — es normal. No forzar audiencias enormes si la precisión se pierde.

---

## KPIs que Mide este Rol

- CPM por tipo de audiencia (objetivo: retargeting < TOFU)
- Frecuencia por audiencia (alerta si retargeting supera 6x en 7 días)
- Tamaño de custom audiences (monitorear crecimiento semanal)
- Overlap entre audiencias (Meta Audience Overlap tool — minimizar canibalización)
- Quality ranking y Engagement ranking del anuncio por audiencia
