# Landing QA Checklist — Miss Roure

Usar cuando: CTR > 1.2% pero ROAS < 2x.
Eso significa que el ad funciona pero la tienda no está convirtiendo. Este checklist diagnostica dónde se rompe el funnel después del click.

---

## Diagnóstico Rápido (5 minutos)

Abrir roure.tiendanegocio.com en **modo incógnito** (simular experiencia de cliente nueva) y verificar:

### 1. Acceso y Carga

- [ ] La página carga en menos de 3 segundos (si tarda más, la gente se va)
- [ ] La URL del ad llega al producto correcto — no a la homepage
- [ ] El producto sigue en stock (no hay mensaje de "agotado")
- [ ] La página carga bien en celular (revisar desde el teléfono, no desde la PC)

### 2. El Precio

- [ ] El precio está visible SIN hacer scroll — si hay que buscar el precio, se pierde la venta
- [ ] El descuento del 20% por transferencia está visible y claro
- [ ] No hay discrepancia entre el precio en el ad y el precio en la tienda
- [ ] El precio en ARS está actualizado (en Argentina los precios cambian)

### 3. El Producto

- [ ] Las fotos muestran el producto con detalle (frente, espalda, detalle de tela)
- [ ] Hay al menos una foto con la prenda puesta (no solo plano)
- [ ] La descripción menciona la composición de la tela y el talle
- [ ] Hay tabla de talles accesible o visible (sin esto, la gente no compra online)
- [ ] Los talles disponibles están correctamente marcados

### 4. El Proceso de Compra

- [ ] El botón de compra / "Agregar al carrito" está visible sin hacer scroll
- [ ] El proceso de checkout tiene menos de 5 pasos
- [ ] El método de pago por transferencia está claro y con instrucciones
- [ ] El envío gratis desde $80.000 ARS está mencionado en la página del producto
- [ ] Hay número de WhatsApp visible para consultas (no oculto en el footer)

### 5. Confianza

- [ ] Hay reseñas o testimonios de clientes visibles
- [ ] La política de cambios es visible o hay un link a ella
- [ ] El tiempo de envío estimado está indicado
- [ ] La cuenta de Instagram `@missroure` tiene actividad reciente (se puede verificar desde el link en la tienda)

---

## Resultados del QA

Después de completar el checklist, documentar:

**Ítems que fallaron:**
```
[Listar los ítems marcados como fallidos]
```

**Diagnóstico:**
- Si fallaron ítems de **Precio o Proceso de Compra** → problema de conversión crítico, pausar el ad hasta resolver
- Si fallaron ítems de **Confianza** → resolver antes de escalar budget
- Si fallaron ítems de **Carga** → problema técnico urgente, reportar a Damaris inmediatamente
- Si todo está OK en la landing → el problema es la audiencia o el creative, no la tienda

**Acción concreta:**
```
[Una sola acción — qué se va a hacer y para cuándo]
```

---

## QA Express (2 minutos — antes de lanzar cualquier ad)

Mínimo indispensable antes de gastar presupuesto:

- [ ] URL carga el producto correcto
- [ ] Precio visible sin scroll
- [ ] Talles disponibles marcados
- [ ] Botón de compra visible
- [ ] Página funciona en celular
