#!/usr/bin/env python3
"""
3Qs Campaign Analyzer — Miss Roure
Analyzes a Meta Ads campaign using the 3 Questions methodology.
All monetary output is in ARS.

Usage:
    python analyze.py                         # interactive prompt
    python analyze.py --csv export.csv        # analyze from Meta Ads CSV export
    python analyze.py --json campaign.json    # analyze from JSON data
    python analyze.py --demo                  # run with sample data
"""

import argparse
import csv
import json
import sys
from dataclasses import dataclass, field
from pathlib import Path
from typing import Optional

# Set UTF-8 encoding for stdout/stderr to support emojis on Windows
if hasattr(sys.stdout, 'reconfigure'):
    sys.stdout.reconfigure(encoding='utf-8')
if hasattr(sys.stderr, 'reconfigure'):
    sys.stderr.reconfigure(encoding='utf-8')

# Add parent dir so we can import utils
sys.path.insert(0, str(Path(__file__).parent))
from utils import (
    fmt_ars,
    fmt_pct,
    fmt_roas,
    evaluate,
    check_stop_rules,
    cpp_target,
    CATEGORY_AOV_ARS,
)


# ─── Data model ──────────────────────────────────────────────────────────────

@dataclass
class CampaignData:
    name: str
    period: str
    objective: str  # "conversiones" | "trafico" | "mensajes"
    funnel_stage: str  # "tofu" | "mofu" | "bofu"
    category: str  # key from CATEGORY_AOV_ARS, or "general"
    days_running: int

    # Spend & reach
    spend_ars: float
    reach: int
    impressions: int

    # Click metrics
    clicks: int
    link_clicks: int

    # Conversion metrics
    conversions: int
    revenue_ars: float

    # Video metrics (optional)
    video_3s_views: Optional[int] = None
    video_15s_views: Optional[int] = None
    video_completions: Optional[int] = None

    # Derived — computed in __post_init__
    cpm: float = field(init=False)
    cpc: float = field(init=False)
    ctr: float = field(init=False)
    cpp: float = field(init=False)
    roas: float = field(init=False)
    frequency: float = field(init=False)
    hook_rate: Optional[float] = field(init=False, default=None)
    hold_rate: Optional[float] = field(init=False, default=None)
    completion_rate: Optional[float] = field(init=False, default=None)

    def __post_init__(self):
        self.cpm = (self.spend_ars / self.impressions * 1000) if self.impressions else 0
        self.cpc = (self.spend_ars / self.link_clicks) if self.link_clicks else 0
        self.ctr = (self.link_clicks / self.impressions * 100) if self.impressions else 0
        self.cpp = (self.spend_ars / self.conversions) if self.conversions else 0
        self.roas = (self.revenue_ars / self.spend_ars) if self.spend_ars else 0
        self.frequency = (self.impressions / self.reach) if self.reach else 0

        if self.video_3s_views is not None and self.impressions:
            self.hook_rate = self.video_3s_views / self.impressions * 100
        if self.video_15s_views is not None and self.impressions:
            self.hold_rate = self.video_15s_views / self.impressions * 100
        if self.video_completions is not None and self.impressions:
            self.completion_rate = self.video_completions / self.impressions * 100


# ─── 3Qs Engine ──────────────────────────────────────────────────────────────

def q1_que_paso(d: CampaignData) -> str:
    lines = [
        "=" * 60,
        "Q1: ¿QUÉ PASÓ?",
        "=" * 60,
        f"Campaña   : {d.name}",
        f"Período   : {d.period}",
        f"Objetivo  : {d.objective.upper()} | Etapa: {d.funnel_stage.upper()}",
        f"Categoría : {d.category}",
        "",
        f"BUDGET INVERTIDO : {fmt_ars(d.spend_ars)}",
        f"ALCANCE          : {d.reach:,} personas",
        f"IMPRESIONES      : {d.impressions:,}",
        f"FRECUENCIA       : {d.frequency:.1f}x",
        "",
        f"CTR              : {fmt_pct(d.ctr)}",
        f"CPC              : {fmt_ars(d.cpc)}",
        f"CPM              : {fmt_ars(d.cpm)}",
        "",
        f"CONVERSIONES     : {d.conversions}",
        f"CPP              : {fmt_ars(d.cpp) if d.conversions else 'N/A (sin conversiones)'}",
        f"REVENUE ATRIB.   : {fmt_ars(d.revenue_ars)}",
        f"ROAS             : {fmt_roas(d.roas)}",
    ]

    video_lines = []
    if d.hook_rate is not None:
        video_lines.append(f"HOOK RATE (3s)   : {fmt_pct(d.hook_rate)}")
    if d.hold_rate is not None:
        video_lines.append(f"HOLD RATE (15s)  : {fmt_pct(d.hold_rate)}")
    if d.completion_rate is not None:
        video_lines.append(f"COMPLETION RATE  : {fmt_pct(d.completion_rate)}")

    if video_lines:
        lines += [""] + video_lines

    return "\n".join(lines)


def q2_por_que(d: CampaignData) -> str:
    lines = [
        "",
        "=" * 60,
        "Q2: ¿POR QUÉ?",
        "=" * 60,
    ]

    # Stop rules first
    alerts = check_stop_rules(
        roas=d.roas,
        ctr=d.ctr,
        frequency=d.frequency,
        cpp=d.cpp if d.conversions else None,
        spend_ars=d.spend_ars,
        conversions=d.conversions,
        funnel_stage=d.funnel_stage,
        days_running=d.days_running,
    )
    if alerts:
        lines.append("⚠️  ALERTAS INMEDIATAS:")
        for a in alerts:
            lines.append(f"   {a}")
        lines.append("")

    # Metric-by-metric evaluation
    lines.append("Evaluación contra benchmarks Roure:")
    lines.append("")

    metrics_to_eval = [
        ("roas", d.roas),
        ("ctr", d.ctr),
        ("cpm", d.cpm),
        ("cpc", d.cpc),
    ]
    if d.hook_rate is not None:
        metrics_to_eval.append(("hook_rate", d.hook_rate))
    if d.hold_rate is not None:
        metrics_to_eval.append(("hold_rate", d.hold_rate))
    if d.completion_rate is not None:
        metrics_to_eval.append(("completion_rate", d.completion_rate))

    freq_key = "frequency_bofu" if d.funnel_stage == "bofu" else "frequency_tofu"
    metrics_to_eval.append((freq_key, d.frequency))

    for key, val in metrics_to_eval:
        emoji, assessment = evaluate(key, val)
        # Format value nicely
        if key == "roas":
            val_str = fmt_roas(val)
        elif key in ("cpm", "cpc"):
            val_str = fmt_ars(val)
        else:
            val_str = fmt_pct(val)
        lines.append(f"  {emoji} {key.upper():20s} {val_str:>15s}  {assessment}")

    if d.conversions and d.category != "general":
        cpp_t = cpp_target(d.category)
        emoji, assessment = evaluate("cpp", d.cpp, d.category)
        lines.append(
            f"  {emoji} {'CPP':20s} {fmt_ars(d.cpp):>15s}  {assessment}"
        )

    # Diagnóstico principal
    lines.append("")
    lines.append("Diagnóstico principal:")
    diagnosis = _diagnose(d)
    for line in diagnosis:
        lines.append(f"  → {line}")

    return "\n".join(lines)


def q3_que_haremos(d: CampaignData) -> str:
    lines = [
        "",
        "=" * 60,
        "Q3: ¿QUÉ VAMOS A HACER?",
        "=" * 60,
    ]

    action, detail = _recommend_action(d)
    lines.append(f"ACCIÓN: {action}")
    lines.append("")
    lines.append(detail)

    if d.roas >= 3.0 and d.conversions > 0:
        new_budget = d.spend_ars / d.days_running * 1.2
        lines.append("")
        lines.append(f"Budget actual/día: {fmt_ars(d.spend_ars / d.days_running)}")
        lines.append(f"Budget propuesto/día (+20%): {fmt_ars(new_budget)}")

    return "\n".join(lines)


# ─── Diagnosis helpers ───────────────────────────────────────────────────────

def _diagnose(d: CampaignData) -> list[str]:
    reasons = []

    if d.roas < 2.0 and d.days_running >= 3:
        if d.ctr >= 1.2:
            reasons.append(
                "ROAS bajo con CTR bueno → el problema está en la tienda/landing, "
                "no en el ad. Revisar precio visible y proceso de compra en tiendanegocio.com."
            )
        elif d.cpm > 6_000:
            reasons.append(
                "CPM alto + CTR bajo → audiencia demasiado pequeña o saturada. "
                "Ampliar segmentación."
            )
        else:
            reasons.append(
                "ROAS bajo con CTR bajo y CPM normal → el creative no conecta. "
                "Testear nuevo formato o copy."
            )

    if d.frequency > 5 and d.funnel_stage == "bofu":
        reasons.append(
            f"Frecuencia {d.frequency:.1f}x en retargeting → audiencia saturada. "
            "Ampliar ventana temporal o rotar creative."
        )

    if d.hook_rate is not None and d.hook_rate < 35:
        reasons.append(
            f"Hook rate {fmt_pct(d.hook_rate)} por debajo del objetivo (35%) → los primeros 3s no enganchan. "
            "Rotar creativo de inmediato."
        )

    if d.hold_rate is not None and d.hold_rate < 15:
        reasons.append(
            f"Hold rate {fmt_pct(d.hold_rate)} por debajo del objetivo (15%) → la creatividad pierde la atención rápidamente. "
            "Rotar creativo de inmediato."
        )

    if d.conversions == 0 and d.days_running < 3:
        reasons.append(
            "Sin conversiones pero con pocos días corriendo → aún en fase de aprendizaje. "
            "Meta necesita al menos 50 eventos/semana para optimizar. No pausar todavía."
        )

    if d.roas >= 3.0:
        reasons.append(
            f"ROAS {fmt_roas(d.roas)} por encima del objetivo → campaña rentable. "
            "Analizar si hay margen para escalar."
        )

    if not reasons:
        reasons.append("Performance dentro de rangos normales. Mantener y monitorear.")

    return reasons


def _recommend_action(d: CampaignData) -> tuple[str, str]:
    # Urgent stop
    if d.roas < 1.0 and d.days_running >= 2:
        return (
            "🚨 PAUSAR URGENTE",
            "ROAS por debajo de 1x — se está perdiendo dinero por cada peso invertido. "
            "Pausar inmediatamente y revisar targeting + creative.",
        )

    if d.conversions == 0 and d.spend_ars > 15_000 and d.funnel_stage == "bofu":
        return (
            "🚨 PAUSAR",
            f"Sin conversiones con {fmt_ars(d.spend_ars)} gastados en BOFU. "
            "Pausar y revisar si la audiencia de retargeting es correcta.",
        )

    # Scale
    if d.roas >= 3.0 and d.days_running >= 3:
        return (
            "📈 ESCALAR",
            "ROAS ≥ 3x sostenido. Aumentar budget 20% cada 48hs. "
            "No duplicar de un día para el otro — respeta el período de aprendizaje.",
        )

    # Learning phase
    if d.conversions < 10 and d.days_running < 7:
        return (
            "⏳ MANTENER",
            "Campaña en fase de aprendizaje. Meta necesita 50 eventos/semana para "
            "optimizar. No hacer cambios hasta completar la semana.",
        )

    # Rotate creative
    if (d.hook_rate is not None and d.hook_rate < 35) or (d.hold_rate is not None and d.hold_rate < 15):
        return (
            "🔄 ROTAR CREATIVE",
            f"Hook Rate ({fmt_pct(d.hook_rate) if d.hook_rate is not None else 'N/A'}) < 35% o "
            f"Hold Rate ({fmt_pct(d.hold_rate) if d.hold_rate is not None else 'N/A'}) < 15% → "
            "indica fatiga creativa o falla de estructura. Rotar creativo de inmediato.",
        )

    if d.ctr < 0.5 and d.frequency > 3:
        return (
            "🔄 ROTAR CREATIVE",
            "CTR bajo con frecuencia alta → creative fatigado. "
            "Lanzar nuevo ad con diferente formato (si venías con imagen, probar Reels y viceversa).",
        )

    # Expand audience
    if d.cpm > 6_000:
        return (
            "🎯 AMPLIAR AUDIENCIA",
            f"CPM {fmt_ars(d.cpm)} demasiado alto — audiencia muy chica o saturada. "
            "Ampliar intereses o aumentar rango etario en el ad set.",
        )

    # Low CTR, weak creative
    if d.ctr < 0.8:
        return (
            "🔄 TESTEAR NUEVO CREATIVE",
            "CTR por debajo del piso del mercado (0.8%). "
            "Testear copy nuevo con precio y descuento por transferencia visible en los primeros 3 segundos.",
        )

    # Retargeting fatigue
    if d.frequency > 5 and d.funnel_stage == "bofu":
        return (
            "👥 RENOVAR AUDIENCIA",
            f"Frecuencia {d.frequency:.1f}x en retargeting. "
            "Ampliar ventana de audiences (7d → 14d) o agregar visitors del último mes.",
        )

    # Default: monitor
    return (
        "👁️ MONITOREAR",
        "Performance dentro de rangos normales. Revisar en 48hs. "
        "Si ROAS sigue estable, evaluar escalado la próxima semana.",
    )


# ─── Input parsers ────────────────────────────────────────────────────────────

def from_meta_csv(filepath: str) -> CampaignData:
    """Parse a Meta Ads Manager CSV export (standard column names in Spanish)."""
    cleaned_lines = []
    with open(filepath, encoding="utf-8-sig") as f:
        for line in f:
            line = line.strip()
            # Remove outer quotes if present
            if line.startswith('"') and line.endswith('"'):
                line = line[1:-1]
            # Replace double-double quotes with single-double quotes
            line = line.replace('""', '"')
            if line:
                cleaned_lines.append(line)

    reader = csv.DictReader(cleaned_lines)
    rows = list(reader)

    if not rows:
        raise ValueError("CSV vacío")

    # Aggregate all rows (multiple ad sets → single campaign total)
    def get_float(row: dict, *keys: str) -> float:
        for k in keys:
            if k in row and row[k].strip() not in ("", "-"):
                val_str = row[k].strip()
                if "," in val_str and "." in val_str:
                    if val_str.find(",") > val_str.find("."):
                        val_str = val_str.replace(".", "").replace(",", ".")
                    else:
                        val_str = val_str.replace(",", "")
                elif "," in val_str:
                    if len(val_str.split(",")[-1]) == 3:
                        val_str = val_str.replace(",", "")
                    else:
                        val_str = val_str.replace(",", ".")
                elif "." in val_str:
                    if len(val_str.split(".")[-1]) == 3 and len(val_str) > 4:
                        val_str = val_str.replace(".", "")
                return float(val_str)
        return 0.0

    def get_int(row: dict, *keys: str) -> int:
        return int(get_float(row, *keys))

    spend = sum(get_float(r, "Importe gastado (ARS)", "Importe gastado") for r in rows)
    reach = sum(get_int(r, "Alcance") for r in rows)
    impressions = sum(get_int(r, "Impresiones") for r in rows)
    clicks = sum(get_int(r, "Clics (todos)") for r in rows)

    first_row = rows[0]
    indicator = first_row.get("Indicador de resultado", "").lower()

    if "link_click" in indicator or "clics en el enlace" in indicator:
        objective = "trafico"
        link_clicks = sum(get_int(r, "Resultados", "Clics en el enlace") for r in rows)
        conversions = 0
    else:
        objective = "conversiones"
        link_clicks = sum(get_int(r, "Clics en el enlace") for r in rows)
        conversions = sum(get_int(r, "Compras", "Resultados") for r in rows)

    revenue = sum(get_float(r, "Valor de conversión de compras") for r in rows)

    campaign_name = first_row.get("Nombre de la campaña", "Campaña importada")
    period = first_row.get("Inicio del informe", "?") + " — " + first_row.get("Fin del informe", "?")

    thruplay_keys = ["ThruPlays", "ThruPlay", "Reproducciones de video de 15 s", "15-second video views"]
    has_thruplays = any(k in first_row for k in thruplay_keys)
    video_15s = sum(get_int(r, *thruplay_keys) for r in rows) if has_thruplays else None

    video_3s_keys = ["Vistas de video de 3 segundos", "Reproducciones de video de 3 s", "3-second video views", "3-second video plays"]
    has_video_3s = any(k in first_row for k in video_3s_keys)
    video_3s = sum(get_int(r, *video_3s_keys) for r in rows) if has_video_3s else None

    video_comp_keys = ["Reproducciones de video al 100%", "Vistas al 100% (completions)", "Video completions", "100% video views"]
    has_video_comp = any(k in first_row for k in video_comp_keys)
    video_comp = sum(get_int(r, *video_comp_keys) for r in rows) if has_video_comp else None

    return CampaignData(
        name=campaign_name,
        period=period,
        objective=objective,
        funnel_stage="tofu",
        category="general",
        days_running=7,
        spend_ars=spend,
        reach=reach,
        impressions=impressions,
        clicks=clicks,
        link_clicks=link_clicks,
        conversions=conversions,
        revenue_ars=revenue,
        video_3s_views=video_3s,
        video_15s_views=video_15s,
        video_completions=video_comp,
    )


def from_json(filepath: str) -> CampaignData:
    with open(filepath, encoding="utf-8") as f:
        data = json.load(f)
    return CampaignData(**data)


def from_interactive() -> CampaignData:
    print("3Qs Campaign Analyzer — Miss Roure")
    print("Ingresá los datos de la campaña (en ARS):\n")

    name = input("Nombre de la campaña: ").strip() or "Campaña"
    period = input("Período (ej: 19/05 – 25/05): ").strip() or "esta semana"
    objective = input("Objetivo [conversiones/trafico/mensajes]: ").strip() or "conversiones"
    funnel_stage = input("Etapa [tofu/mofu/bofu]: ").strip() or "tofu"

    print(f"\nCategorías disponibles: {', '.join(CATEGORY_AOV_ARS.keys())}, general")
    category = input("Categoría del producto: ").strip() or "general"
    days_running = int(input("Días corriendo: ").strip() or "7")

    print("\n--- Métricas ---")
    spend_ars = float(input("Budget invertido (ARS): ").replace(".", "").replace(",", "."))
    reach = int(input("Alcance (personas): ").replace(".", ""))
    impressions = int(input("Impresiones: ").replace(".", ""))
    link_clicks = int(input("Clicks en enlace: ").replace(".", ""))
    clicks = link_clicks
    conversions = int(input("Conversiones (compras): "))
    revenue_ars = float(
        input("Revenue atribuido (ARS, 0 si no tenés píxel): ")
        .replace(".", "")
        .replace(",", ".")
    )

    video = input("\n¿Tenés datos de video? [s/n]: ").strip().lower() == "s"
    video_3s = None
    video_15s = None
    video_comp = None
    if video:
        video_3s = int(input("Vistas de 3 segundos: ").replace(".", ""))
        video_15s = int(input("Vistas de 15 segundos (ThruPlays): ").replace(".", ""))
        video_comp = int(input("Vistas al 100% (completions): ").replace(".", ""))

    return CampaignData(
        name=name,
        period=period,
        objective=objective,
        funnel_stage=funnel_stage,
        category=category,
        days_running=days_running,
        spend_ars=spend_ars,
        reach=reach,
        impressions=impressions,
        clicks=clicks,
        link_clicks=link_clicks,
        conversions=conversions,
        revenue_ars=revenue_ars,
        video_3s_views=video_3s,
        video_15s_views=video_15s,
        video_completions=video_comp,
    )


def demo_data() -> CampaignData:
    """Sample campaign data for testing."""
    return CampaignData(
        name="Tapados Otoño 2026 — TOFU",
        period="19/05/2026 – 25/05/2026",
        objective="conversiones",
        funnel_stage="tofu",
        category="tapados",
        days_running=7,
        spend_ars=35_000,
        reach=12_500,
        impressions=18_900,
        clicks=340,
        link_clicks=280,
        conversions=3,
        revenue_ars=187_500,
        video_3s_views=5_670,
        video_15s_views=3024,
        video_completions=2_835,
    )


# ─── Main ─────────────────────────────────────────────────────────────────────

def run_analysis(data: CampaignData) -> None:
    print(q1_que_paso(data))
    print(q2_por_que(data))
    print(q3_que_haremos(data))
    print()
    print("=" * 60)
    print("Para registrar esta campaña: copiar output a memory/campaign-log.md")
    print("=" * 60)


def main():
    parser = argparse.ArgumentParser(description="3Qs Campaign Analyzer — Miss Roure")
    group = parser.add_mutually_exclusive_group()
    group.add_argument("--csv", metavar="FILE", help="Meta Ads CSV export")
    group.add_argument("--json", metavar="FILE", help="Campaign JSON file")
    group.add_argument("--demo", action="store_true", help="Run with sample data")
    args = parser.parse_args()

    if args.csv:
        data = from_meta_csv(args.csv)
    elif args.json:
        data = from_json(args.json)
    elif args.demo:
        data = demo_data()
    else:
        data = from_interactive()

    run_analysis(data)


if __name__ == "__main__":
    main()
