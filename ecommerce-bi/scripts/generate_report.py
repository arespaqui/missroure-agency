#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Renders the bi_analysis.py JSON output into a branded HTML report for Miss Roure."""

import json
import html
import sys

CATEGORIES = ['Producto', 'Cliente', 'Revenue', 'Geográfico', 'Operativo', 'Estratégico']

CURRENCY_KEYS = {'revenue', 'aov', 'amount', 'clv', 'price', 'ticket', 'discount',
                  'shipping', 'spend', 'value', 'total_revenue', 'avg_order_total'}
PCT_KEYS = {'pct', 'rate', 'percentage'}
COUNT_SUFFIXES = ('orders', 'customers', 'products', 'cohorts', 'provinces', 'cities',
                   'rows', 'items', 'count', 'uses', 'qty', 'quantity', 'clusters',
                   'segments', 'days', 'churned', 'active', 'upgraders', 'downgraders')
# Exact-key overrides for names that would otherwise be misclassified by substring
# matching (e.g. "orders_with_discount" is a COUNT, not a currency amount, even
# though it contains "discount").
FORCE_COUNT_KEYS = {'orders_with_discount', 'overlap_with_payment_method_discount'}
FORCE_CURRENCY_KEYS = {'total_discount_amount', 'total_discount_amount_on_these_orders'}


def fmt_ars(v):
    try:
        return f"${v:,.0f}".replace(',', '.')
    except (TypeError, ValueError):
        return str(v)


def fmt_num(v):
    if isinstance(v, float):
        if v == int(v):
            return f"{int(v):,}".replace(',', '.')
        return f"{v:,.2f}".replace(',', '@').replace('.', ',').replace('@', '.')
    if isinstance(v, int):
        return f"{v:,}".replace(',', '.')
    return html.escape(str(v))


def fmt_value(key, v):
    if v is None:
        return '—'
    kl = key.lower()
    if isinstance(v, bool):
        return 'Sí' if v else 'No'
    if isinstance(v, (int, float)):
        if kl in FORCE_COUNT_KEYS:
            return fmt_num(v)
        if kl in FORCE_CURRENCY_KEYS:
            return fmt_ars(v)
        if any(p in kl for p in PCT_KEYS):
            return f"{v:.1f}%"
        if any(kl == s or kl.endswith('_' + s) for s in COUNT_SUFFIXES):
            return fmt_num(v)
        if any(c in kl for c in CURRENCY_KEYS):
            return fmt_ars(v)
        return fmt_num(v)
    if isinstance(v, list):
        if not v:
            return '—'
        if isinstance(v[0], dict):
            name_key = next((k for k in ('product', 'product_name', 'name', 'category', 'coupon') if k in v[0]), None)
            if name_key:
                shown = ', '.join(str(item.get(name_key, '')) for item in v[:3])
                extra = f' (+{len(v) - 3})' if len(v) > 3 else ''
                return html.escape(shown + extra)
            return f'{len(v)} items'
        return html.escape(', '.join(str(x) for x in v[:5]))
    if isinstance(v, dict):
        if not v:
            return '—'
        return html.escape(', '.join(f'{k}: {vv}' for k, vv in list(v.items())[:3]))
    return html.escape(str(v))


LABEL_ES = {
    'total_orders': 'Órdenes totales', 'multi_product_orders': 'Órdenes multi-producto',
    'multi_product_pct': 'Multi-producto %', 'items': 'Productos', 'support': 'Support',
    'confidence': 'Confidence', 'lift': 'Lift', 'count': 'Cantidad',
    'total_products': 'Productos totales', 'products_80_pct': 'Productos (80% revenue)',
    'pct_products_80': '% del catálogo', 'total_revenue': 'Revenue total',
    'overall_cancel_rate': 'Tasa cancelación general', 'total_products_analyzed': 'Productos analizados',
    'total_customers': 'Clientas totales', 'avg_clv': 'CLV promedio', 'median_clv': 'CLV mediano',
    'avg_aov': 'AOV promedio', 'avg_orders': 'Órdenes promedio', 'avg_lifespan_days': 'Vida promedio (días)',
    'repeat_customers': 'Clientas recurrentes', 'repurchase_rate': 'Tasa de recompra',
    'overall_aov': 'Ticket promedio', 'median_aov': 'Ticket mediano', 'category': 'Categoría',
    'revenue': 'Revenue', 'units': 'Unidades', 'trend_pct': 'Tendencia', 'pct': '%',
    'aov': 'Ticket promedio', 'orders_with_discount': 'Con descuento',
    'total_discount_amount': 'Descuento total', 'avg_order_total': 'Ticket promedio',
    'pct_with_discount': '% con descuento', 'cancel_rate': 'Tasa de cancelación',
    'cancelled_orders': 'Órdenes canceladas', 'peak_month': 'Mes pico', 'low_month': 'Mes valle',
    'peak_day': 'Día pico', 'vip_count': 'Clientas VIP', 'vip_pct': '% VIP',
    'vip_revenue': 'Revenue VIP', 'vip_revenue_pct': '% revenue VIP', 'churn_rate': 'Tasa de churn',
    'churned': 'En churn', 'active': 'Activas', 'churn_threshold_days': 'Umbral churn (días)',
    'avg_purchase_interval': 'Intervalo de compra promedio', 'min_price': 'Precio mín',
    'max_price': 'Precio máx', 'mean_price': 'Precio promedio', 'median_price': 'Precio mediano',
    'total_items': 'Items totales', 'total_cities': 'Ciudades totales',
    'total_provinces': 'Provincias totales', 'global_repurchase_rate': 'Recompra global',
    'min_sample_size': 'Muestra mínima', 'orders': 'Órdenes', 'order_count': 'Órdenes',
    'payment_method': 'Medio de pago', 'state': 'Provincia', 'product_name': 'Producto',
    'coupon': 'Cupón', 'uses': 'Usos', 'total_cohorts': 'Cohortes', 'avg_retention': 'Retención promedio',
    'products': 'Productos', 'product': 'Producto', 'anchors': 'Productos ancla',
    'pct_of_orders': '% de órdenes', 'orders_with_discount': 'Con descuento',
    'total_discount_amount_on_these_orders': 'Descuento acumulado en estas órdenes',
    'overlap_with_payment_method_discount': 'También con descuento por transferencia',
    'avg_order_total': 'Ticket promedio', 'pct_with_discount': '% con descuento',
}


def label(key):
    if key in LABEL_ES:
        return html.escape(LABEL_ES[key])
    return html.escape(key.replace('_', ' ').replace('pct', '%').strip().capitalize())


def render_scalar_grid(d):
    items = {k: v for k, v in d.items() if not isinstance(v, (list, dict))}
    if not items:
        return ''
    cells = ''.join(
        f'<div class="stat"><div class="stat-num">{fmt_value(k, v)}</div>'
        f'<div class="stat-lbl">{label(k)}</div></div>'
        for k, v in items.items()
    )
    return f'<div class="stat-grid">{cells}</div>'


def render_table(records, max_rows=12):
    if not records:
        return '<p class="skipped">Sin filas.</p>'
    cols = list(records[0].keys())
    head = ''.join(f'<th>{label(c)}</th>' for c in cols)
    rows = ''
    for rec in records[:max_rows]:
        cells = ''.join(f'<td>{fmt_value(c, rec.get(c))}</td>' for c in cols)
        rows += f'<tr>{cells}</tr>'
    more = f'<p class="skipped">+ {len(records) - max_rows} filas más en el JSON.</p>' if len(records) > max_rows else ''
    return f'<table><thead><tr>{head}</tr></thead><tbody>{rows}</tbody></table>{more}'


def render_nested_dict(d):
    """For dicts-of-dicts like {'with_discount': {...}, 'without_discount': {...}}."""
    out = '<div class="stat-grid">'
    for sub_key, sub_val in d.items():
        if isinstance(sub_val, dict):
            inner = ' · '.join(f'{label(k)}: {fmt_value(k, v)}' for k, v in sub_val.items())
            out += f'<div class="stat"><div class="stat-lbl">{label(sub_key)}</div><div class="kpi-row">{inner}</div></div>'
    out += '</div>'
    return out


def render_generic(data):
    """Fallback: render every field of an analysis's data dict."""
    parts = []
    scalars = {k: v for k, v in data.items() if not isinstance(v, (list, dict)) and k != 'status'}
    if scalars:
        parts.append(render_scalar_grid(scalars))
    for k, v in data.items():
        if k == 'status':
            continue
        if isinstance(v, list) and v and isinstance(v[0], dict):
            parts.append(f'<p class="kpi-row"><strong>{label(k)}</strong></p>')
            parts.append(render_table(v))
        elif isinstance(v, dict) and v:
            if all(isinstance(vv, dict) for vv in v.values()):
                parts.append(f'<p class="kpi-row"><strong>{label(k)}</strong></p>')
                parts.append(render_nested_dict(v))
            else:
                parts.append(f'<p class="kpi-row"><strong>{label(k)}</strong></p>')
                parts.append(render_scalar_grid(v))
    return ''.join(parts)


def insight_for(aid, data):
    """Hand-written, business-specific insight per analysis, grounded in the real numbers."""
    try:
        if aid == 1:
            pairs = data.get('pairs') or []
            if pairs:
                top = pairs[0]
                items = ' + '.join(top['items'])
                return (f"El combo con mejor lift es <strong>{html.escape(items)}</strong> "
                        f"(lift {top['lift']}). Armá un bundle explícito con estos productos y ofrecelo "
                        f"en el carrito — es la señal más fuerte de cross-sell que tenés hoy.")
            return "Sin pares con lift &gt;1 y support &gt;1% todavía — normal con 53 órdenes; revisar de nuevo con más volumen."
        if aid == 3:
            prods = data.get('products') or []
            if prods:
                top = prods[0]
                return (f"<strong>{html.escape(top.get('product_name',''))}</strong> lidera el ranking. "
                        f"Cruzalo contra los \"Productos Estrella\" de catalog-context.md — si no coincide, "
                        f"puede que estés subpromocionando algo que ya vende solo.")
            return ''
        if aid == 5:
            return (f"{data.get('products_80_pct')} de {data.get('total_products')} productos "
                    f"({data.get('pct_products_80')}%) generan el 80% del revenue. El resto es candidato "
                    f"a liquidar o achicar reposición — no lo trates igual que al núcleo.")
        if aid == 7:
            segs = data.get('segments') or {}
            champions = segs.get('Champions', {}).get('count', 0) if isinstance(segs.get('Champions'), dict) else 0
            at_risk = segs.get('At Risk', {}).get('count', 0) if isinstance(segs.get('At Risk'), dict) else 0
            return (f"Con {data.get('total_customers')} clientas mapeadas: priorizá campañas de retención VIP "
                    f"para \"Champions\" y una campaña de reactivación específica para \"At Risk\" antes de "
                    f"seguir gastando en adquisición fría — retener sale más barato que adquirir.")
        if aid == 8:
            return (f"CLV promedio a 3 años: {fmt_ars(data.get('avg_clv', 0))}. Tu CPA máximo actual "
                    f"(objetivo $10.000 ARS en meta-ads-analyst.md) tiene margen de sobra contra este techo — "
                    f"el límite real no es cuánto pagás por adquirir, es la calidad de la audiencia.")
        if aid == 9:
            return ("Con ~2 meses de historial las cohortes todavía no muestran retención a M+2/M+3 de forma "
                    "confiable. Volver a correr este análisis en 3-4 meses para que sea representativo.")
        if aid == 10:
            return (f"Tasa de recompra: {data.get('repurchase_rate')}%. "
                    f"{'Por encima del 40%, hay margen para invertir más en retención que en adquisición pura.' if (data.get('repurchase_rate') or 0) > 40 else 'Todavía por debajo del 40% — el negocio depende fuerte de adquisición nueva; las reglas de email de ecommerce-specialist.md son la palanca más directa acá.'}")
        if aid == 11:
            return "Serie mensual de referencia — usarla como línea de base antes de leer cualquier otro análisis de este informe."
        if aid == 12:
            aov = data.get('overall_aov', 0)
            gap = 80000 - aov
            return (f"AOV real: {fmt_ars(aov)} vs. objetivo Roure de $80.000 ARS "
                    f"(umbral de envío gratis) — faltan {fmt_ars(gap)} en promedio por orden. "
                    f"Los combos de ecommerce-specialist.md (Cozy Coquette, etc.) están diseñados justo para cerrar esta brecha.")
        if aid == 13:
            cats = data.get('categories') or []
            if cats:
                top = cats[0]
                return (f"\"{html.escape(str(top.get('category','')))}\" concentra {top.get('pct')}% del revenue. "
                        f"{'Riesgo de dependencia de una sola línea — vale diversificar el mix de contenido/pauta.' if (top.get('pct') or 0) > 60 else 'Mix relativamente balanceado entre categorías.'}")
            return ''
        if aid == 15:
            provs = data.get('provinces') or []
            if provs:
                top = provs[0]
                return (f"\"{html.escape(str(top.get('state','')))}\" es la provincia con más volumen — "
                        f"validar si la segmentación geo de meta-ads-audience.md (CABA+GBA prioritario) "
                        f"sigue siendo la correcta con datos reales, no solo supuestos.")
            return ''
        if aid == 17:
            rate = data.get('cancel_rate', 0)
            return (f"Tasa de cancelación: {rate}%. "
                    f"{'Ojo: este export puede no incluir canceladas — no lo tomes como el número real hasta confirmarlo con Tienda Negocio.' if rate == 0 else 'Revisar los motivos principales antes de escalar pauta a los productos más cancelados.'}")
        if aid == 18:
            pms = data.get('payment_methods') or []
            if pms:
                top = pms[0]
                return (f"\"{html.escape(str(top.get('payment_method','')))}\" domina el mix — "
                        f"coherente con que el 20% OFF por transferencia es el driver de conversión principal.")
            return ''
        if aid == 19:
            bundles = data.get('bundles') or []
            return (f"{len(bundles)} oportunidades de bundle detectadas por lift real de compra conjunta — "
                    f"usarlas para definir el próximo combo antes de inventar uno a criterio.") if bundles else "Sin bundles con lift suficiente todavía."
        if aid == 20:
            return (f"Mes pico: {data.get('peak_month')} · Mes valle: {data.get('low_month')} · "
                    f"Día más fuerte: {data.get('peak_day')}. Con solo 2 meses de datos esto es apenas una "
                    f"tendencia inicial, no un patrón estacional confirmado — revisar de nuevo con un año completo.")
        if aid == 26:
            return (f"El {data.get('vip_pct')}% de clientas (top 10% por revenue) genera el "
                    f"{data.get('vip_revenue_pct')}% del revenue total. Esa concentración justifica un programa "
                    f"VIP dedicado — acceso anticipado a drops, atención diferenciada.")
        if aid == 27:
            return (f"{data.get('churned')} de {data.get('total_customers')} clientas están en churn "
                    f"(sin comprar hace más del doble de su intervalo habitual). Revisar qué productos "
                    f"compraron antes de irse — a veces revela un problema de calidad puntual, no solo desinterés.")
        if aid == 30:
            return "Nivel de detalle más fino que provincia — útil para decisiones de pauta geo hiper-local si el volumen lo justifica."
        if aid == 34:
            return "Compara AOV y conversión con/sin envío gratis — valida si el umbral de $80.000 ARS de ecommerce-specialist.md está bien calibrado con datos reales."
        if aid == 36:
            recs = data.get('recommendations') or []
            return f"{len(recs)} recomendaciones de cross-sell listas para alimentar módulos \"también te puede interesar\" en la tienda." if recs else ''
        if aid == 38:
            clusters = data.get('clusters') or []
            return f"{len(clusters)} clusters de afinidad de producto detectados — posibles sub-líneas o landings temáticas dentro del catálogo." if clusters else ''
        if aid == 39:
            top = data.get('top_product')
            if top:
                return (f"\"{html.escape(str(top.get('product_name','')))}\" es tu mejor producto gateway de retención "
                        f"— no necesariamente el que más vende, pero sí el que mejor convierte primera compra en clienta recurrente. "
                        f"Priorizarlo en pauta de adquisición, no solo en pauta de catálogo general.")
            return ''
    except Exception:
        return ''
    return ''


def render_discount_special(data):
    """Analysis #14 gets bespoke rendering: payment-method (automatic) discount vs promo-code
    discount as two clearly separate blocks, per explicit Roure business rule."""
    pm = data.get('discount_by_payment_method') or []
    promo = data.get('promo_code_summary')
    comparison = data.get('comparison', {})

    out = '<p class="insight" style="border-left-color:#7a4a5c;margin-bottom:20px;">'
    out += ('<strong>Importante:</strong> el 20% OFF por transferencia/billetera digital es un descuento '
            'automático de política de precio, no una promoción — se separa acá del uso real de códigos '
            'promocionales para no mezclar ambas señales.</p>')

    out += '<h4 style="margin:18px 0 8px;font-size:14px;color:#4b5563;">Descuento automático por medio de pago</h4>'
    out += render_table(pm)

    out += '<h4 style="margin:18px 0 8px;font-size:14px;color:#4b5563;">Códigos promocionales (cupones)</h4>'
    if promo and promo.get('orders'):
        out += render_scalar_grid(promo)
        overlap = promo.get('overlap_with_payment_method_discount')
        if overlap:
            out += (f'<p class="kpi-row" style="margin-top:8px;">De esas {promo["orders"]} órdenes con cupón, '
                     f'{overlap} <strong>también</strong> pagaron por transferencia — ambos descuentos se '
                     f'acumularon en el monto final, no se pueden separar centavo a centavo desde el export.</p>')
    else:
        out += '<p class="skipped">Sin uso de códigos promocionales en este período.</p>'

    top_coupons = data.get('top_coupons')
    if top_coupons:
        out += '<h4 style="margin:18px 0 8px;font-size:14px;color:#4b5563;">Detalle por código</h4>'
        out += render_table(top_coupons)

    out += ('<p class="insight" style="margin-top:16px;">'
            f'Lectura correcta: <strong>{comparison.get("with_discount",{}).get("pct_orders","—")}% de las órdenes</strong> '
            'tuvo algún descuento, pero eso está dominado casi por completo por el 20% automático de transferencia '
            f'(no por promociones puntuales). El uso real de códigos como MISSWINTER es mucho más chico '
            f'({promo.get("pct_of_orders","—") if promo else 0}% de las órdenes) — si el objetivo es medir el '
            'impacto de una campaña de cupón específica, mirar siempre el bloque de "Códigos promocionales", '
            'nunca el "% con descuento" general.</p>')
    return out


def render_analysis(aid, entry):
    data = entry['data']
    name = entry['name']
    if aid == 14:
        body = render_discount_special(data)
    else:
        body = render_generic(data)
        ins = insight_for(aid, data)
        if ins:
            body += f'<p class="insight">{ins}</p>'
    return f'<div class="analysis"><h3>#{aid} · {html.escape(name)}</h3>{body}</div>'


def main():
    src = sys.argv[1] if len(sys.argv) > 1 else 'data/bi_results_full.json'
    out_path = sys.argv[2] if len(sys.argv) > 2 else 'data/Roure_Informe_BI.html'

    with open(src, encoding='utf-8') as f:
        result = json.load(f)

    summary = result.get('summary', {})
    analyses = result['analyses']

    by_category = {c: [] for c in CATEGORIES}
    skipped = []
    cat_lookup = {}
    for aid_str, entry in analyses.items():
        cat_lookup[int(aid_str)] = entry['category']

    for aid_str, entry in sorted(analyses.items(), key=lambda kv: int(kv[0])):
        aid = int(aid_str)
        cat = entry['category']
        if entry['data'].get('status') == 'ok':
            by_category.setdefault(cat, []).append((aid, entry))
        else:
            skipped.append((aid, entry))

    sections_html = ''
    for cat in CATEGORIES:
        items = by_category.get(cat, [])
        if not items:
            continue
        cards = ''.join(render_analysis(aid, entry) for aid, entry in items)
        sections_html += f'<section class="category"><h2>{html.escape(cat)}</h2>{cards}</section>'

    skipped_html = ''
    if skipped:
        rows = ''.join(
            f'<li><strong>#{aid} {html.escape(e["name"])}</strong> — {html.escape(e["data"].get("reason",""))}</li>'
            for aid, e in skipped
        )
        skipped_html = (f'<section class="category"><h2>No disponibles en este período</h2>'
                         f'<div class="analysis"><ul class="skipped-list">{rows}</ul></div></section>')

    html_doc = f"""<!DOCTYPE html>
<html lang="es">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>Miss Roure — Informe de Business Intelligence</title>
<style>
:root {{
  --bg: #ffffff; --bg-card: #ffffff; --bg-card-emphasis: #faf5f7;
  --border: #ecdfe4; --text: #2b1f24; --text-secondary: #6b5560; --text-muted: #9c8890;
  --accent: #a24868; --accent-soft: #fbeef2;
  --font: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, 'Helvetica Neue', Arial, sans-serif;
}}
* {{ box-sizing: border-box; margin:0; padding:0; }}
body {{ background:var(--bg); color:var(--text); font-family:var(--font); font-size:15px; line-height:1.55; padding:56px 24px; }}
.container {{ max-width:1100px; margin:0 auto; }}
header {{ margin-bottom:40px; padding-bottom:28px; border-bottom:1px solid var(--border); }}
h1 {{ font-size:30px; font-weight:600; margin:4px 0 6px; }}
.subtitle {{ color:var(--text-secondary); font-size:14px; }}
.mode-badge {{ display:inline-block; background:var(--accent-soft); color:var(--accent); font-size:11px; font-weight:600;
  letter-spacing:.08em; padding:3px 9px; border-radius:4px; margin-left:8px; text-transform:uppercase; }}
.hero-grid {{ display:grid; grid-template-columns:repeat(4,1fr); gap:12px; margin-top:24px; }}
.hero {{ background:var(--bg-card); border:1px solid var(--border); border-radius:6px; padding:16px; }}
.hero-num {{ font-size:24px; font-weight:600; }}
.hero-lbl {{ color:var(--text-muted); font-size:11px; text-transform:uppercase; letter-spacing:.08em; margin-top:4px; }}
section.category {{ margin:48px 0 20px; }}
section.category h2 {{ font-size:12px; font-weight:600; text-transform:uppercase; letter-spacing:.12em;
  color:var(--text-secondary); margin-bottom:16px; border-top:1px solid var(--border); padding-top:20px; }}
.analysis {{ background:var(--bg-card); border:1px solid var(--border); border-radius:6px; padding:22px; margin-bottom:14px; }}
.analysis h3 {{ font-size:17px; font-weight:600; margin-bottom:12px; }}
.kpi-row {{ color:var(--text-secondary); font-size:13.5px; margin:8px 0; }}
.stat-grid {{ display:grid; grid-template-columns:repeat(auto-fit,minmax(150px,1fr)); gap:8px; margin:10px 0; }}
.stat {{ background:var(--bg-card-emphasis); border:1px solid var(--border); border-radius:4px; padding:10px; }}
.stat-num {{ font-size:18px; font-weight:600; }}
.stat-lbl {{ color:var(--text-muted); font-size:10.5px; text-transform:uppercase; letter-spacing:.06em; margin-top:3px; }}
table {{ width:100%; border-collapse:collapse; margin:8px 0; font-size:13px; }}
th, td {{ text-align:left; padding:7px 10px; border-bottom:1px solid var(--border); }}
th {{ color:var(--text-muted); font-weight:500; text-transform:uppercase; font-size:10px; letter-spacing:.06em; }}
.insight {{ background:var(--bg-card-emphasis); border-left:3px solid var(--accent); padding:10px 14px; margin-top:12px; font-size:13.5px; }}
.skipped {{ color:var(--text-muted); font-style:italic; font-size:12.5px; }}
.skipped-list {{ list-style:none; }}
.skipped-list li {{ padding:6px 0; border-bottom:1px solid var(--border); font-size:13.5px; }}
footer {{ text-align:center; color:var(--text-muted); font-size:12px; padding:32px 0 0; border-top:1px solid var(--border); margin-top:48px; }}
footer a {{ color:var(--text-secondary); }}
</style>
</head>
<body>
<div class="container">
<header>
  <h1>Miss Roure <span class="mode-badge">FULL</span></h1>
  <p class="subtitle">{summary.get('date_min')} → {summary.get('date_max')} · Plataforma: Tienda Negocio · {summary.get('total_orders')} órdenes</p>
  <div class="hero-grid">
    <div class="hero"><div class="hero-num">{fmt_ars(summary.get('total_revenue',0))}</div><div class="hero-lbl">Revenue</div></div>
    <div class="hero"><div class="hero-num">{summary.get('total_orders')}</div><div class="hero-lbl">Órdenes</div></div>
    <div class="hero"><div class="hero-num">{summary.get('unique_customers')}</div><div class="hero-lbl">Clientas únicas</div></div>
    <div class="hero"><div class="hero-num">{fmt_ars(summary.get('avg_ticket',0))}</div><div class="hero-lbl">Ticket promedio</div></div>
  </div>
</header>
{sections_html}
{skipped_html}
<footer>Reporte generado con ecommerce-bi (adaptado de mathiaschu/ecommerce-bi, MIT) para Miss Roure</footer>
</div>
</body>
</html>"""

    with open(out_path, 'w', encoding='utf-8') as f:
        f.write(html_doc)
    print(f"Written: {out_path}")


if __name__ == '__main__':
    main()
