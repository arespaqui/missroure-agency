#!/usr/bin/env python3
"""
Weekly Report Generator — Miss Roure Meta Ads
Generates a structured weekly performance report in ARS.

Usage:
    python weekly_report.py                  # interactive input
    python weekly_report.py --demo           # sample report
    python weekly_report.py --csv data.csv   # from Meta Ads CSV export
    python weekly_report.py --out report.md  # save to file
"""

import argparse
import csv
import sys
from dataclasses import dataclass, field
from datetime import date
from pathlib import Path
from typing import Optional

sys.path.insert(0, str(Path(__file__).parent))
from utils import fmt_ars, fmt_pct, fmt_roas, evaluate, check_stop_rules, cpp_target


# ─── Data model ───────────────────────────────────────────────────────────────

@dataclass
class AdSetResult:
    name: str
    funnel_stage: str       # tofu / mofu / bofu
    spend_ars: float
    impressions: int
    link_clicks: int
    conversions: int
    revenue_ars: float
    reach: int = 0

    roas: float = field(init=False)
    ctr: float = field(init=False)
    cpm: float = field(init=False)
    cpp: float = field(init=False)
    frequency: float = field(init=False)

    def __post_init__(self):
        self.roas = (self.revenue_ars / self.spend_ars) if self.spend_ars else 0
        self.ctr = (self.link_clicks / self.impressions * 100) if self.impressions else 0
        self.cpm = (self.spend_ars / self.impressions * 1000) if self.impressions else 0
        self.cpp = (self.spend_ars / self.conversions) if self.conversions else 0
        self.frequency = (self.impressions / self.reach) if self.reach else 0


@dataclass
class WeeklyReport:
    period: str
    week_number: int
    ad_sets: list[AdSetResult]
    notes: str = ""

    # Totals (computed)
    total_spend: float = field(init=False)
    total_impressions: int = field(init=False)
    total_clicks: int = field(init=False)
    total_conversions: int = field(init=False)
    total_revenue: float = field(init=False)
    overall_roas: float = field(init=False)
    overall_ctr: float = field(init=False)
    overall_cpm: float = field(init=False)
    overall_cpp: float = field(init=False)

    def __post_init__(self):
        self.total_spend = sum(a.spend_ars for a in self.ad_sets)
        self.total_impressions = sum(a.impressions for a in self.ad_sets)
        self.total_clicks = sum(a.link_clicks for a in self.ad_sets)
        self.total_conversions = sum(a.conversions for a in self.ad_sets)
        self.total_revenue = sum(a.revenue_ars for a in self.ad_sets)
        self.overall_roas = (self.total_revenue / self.total_spend) if self.total_spend else 0
        self.overall_ctr = (self.total_clicks / self.total_impressions * 100) if self.total_impressions else 0
        self.overall_cpm = (self.total_spend / self.total_impressions * 1000) if self.total_impressions else 0
        self.overall_cpp = (self.total_spend / self.total_conversions) if self.total_conversions else 0


# ─── Report generator ─────────────────────────────────────────────────────────

def generate_report(r: WeeklyReport) -> str:
    lines = []
    today = date.today().strftime("%d/%m/%Y")

    # Header
    lines += [
        f"# Reporte Semanal Meta Ads — Miss Roure",
        f"**Semana {r.week_number}** | {r.period} | Generado: {today}",
        "",
        "---",
        "",
    ]

    # Summary table
    roas_emoji, _ = evaluate("roas", r.overall_roas)
    ctr_emoji, _ = evaluate("ctr", r.overall_ctr)
    cpm_emoji, _ = evaluate("cpm", r.overall_cpm)

    lines += [
        "## Resumen Ejecutivo",
        "",
        "| Métrica | Resultado | Estado |",
        "|---|---|---|",
        f"| Budget invertido | {fmt_ars(r.total_spend)} | — |",
        f"| Impresiones totales | {r.total_impressions:,} | — |",
        f"| Clicks en enlace | {r.total_clicks:,} | — |",
        f"| Conversiones | {r.total_conversions} | — |",
        f"| Revenue atribuido | {fmt_ars(r.total_revenue)} | — |",
        f"| ROAS general | {fmt_roas(r.overall_roas)} | {roas_emoji} |",
        f"| CTR general | {fmt_pct(r.overall_ctr)} | {ctr_emoji} |",
        f"| CPM general | {fmt_ars(r.overall_cpm)} | {cpm_emoji} |",
        f"| CPP general | {fmt_ars(r.overall_cpp) if r.total_conversions else 'N/A'} | — |",
        "",
    ]

    # Alertas urgentes
    alerts = check_stop_rules(
        roas=r.overall_roas,
        ctr=r.overall_ctr,
        frequency=None,
        cpp=r.overall_cpp if r.total_conversions else None,
        spend_ars=r.total_spend,
        conversions=r.total_conversions,
        funnel_stage="general",
        days_running=7,
    )
    if alerts:
        lines += ["## ⚠️ Alertas Urgentes", ""]
        for a in alerts:
            lines.append(f"- {a}")
        lines.append("")

    # Per ad set breakdown
    lines += ["## Desglose por Ad Set", ""]

    winner = max(r.ad_sets, key=lambda a: a.roas) if r.ad_sets else None
    loser = min(r.ad_sets, key=lambda a: a.roas) if r.ad_sets else None

    for ads in r.ad_sets:
        roas_e, _ = evaluate("roas", ads.roas)
        ctr_e, _ = evaluate("ctr", ads.ctr)
        freq_key = "frequency_bofu" if ads.funnel_stage == "bofu" else "frequency_tofu"

        tag = ""
        if winner and ads.name == winner.name and len(r.ad_sets) > 1:
            tag = " 🏆 GANADOR"
        elif loser and ads.name == loser.name and len(r.ad_sets) > 1:
            tag = " ⚠️ REVISAR"

        lines += [
            f"### {ads.name}{tag}",
            f"Etapa: `{ads.funnel_stage.upper()}` | Budget: {fmt_ars(ads.spend_ars)}",
            "",
            f"| ROAS | CTR | CPM | Conversiones | CPP |",
            f"|---|---|---|---|---|",
            f"| {roas_e} {fmt_roas(ads.roas)} "
            f"| {ctr_e} {fmt_pct(ads.ctr)} "
            f"| {fmt_ars(ads.cpm)} "
            f"| {ads.conversions} "
            f"| {fmt_ars(ads.cpp) if ads.conversions else 'N/A'} |",
            "",
        ]

    # Decisiones de la semana
    lines += ["## Decisiones para Próxima Semana", ""]
    decisions = _weekly_decisions(r)
    for d in decisions:
        lines.append(f"- {d}")
    lines.append("")

    # Notes
    if r.notes:
        lines += ["## Notas", "", r.notes, ""]

    # Log template
    lines += [
        "---",
        "",
        "## Para memory/campaign-log.md",
        "",
        "```",
        f"## Semana {r.week_number} | {r.period}",
        f"Budget: {fmt_ars(r.total_spend)} | ROAS: {fmt_roas(r.overall_roas)} | "
        f"Conversiones: {r.total_conversions} | CPP: {fmt_ars(r.overall_cpp) if r.total_conversions else 'N/A'}",
        "",
        "### Ad Set Ganador",
        f"{winner.name if winner else 'N/A'} — ROAS {fmt_roas(winner.roas) if winner else 'N/A'}",
        "",
        "### Aprendizajes",
        "- [completar]",
        "",
        "### Acción Next",
        f"- {decisions[0] if decisions else '[completar]'}",
        "```",
    ]

    return "\n".join(lines)


def _weekly_decisions(r: WeeklyReport) -> list[str]:
    decisions = []

    if r.overall_roas >= 3.0:
        best = max(r.ad_sets, key=lambda a: a.roas)
        decisions.append(
            f"ESCALAR {best.name} — ROAS {fmt_roas(best.roas)}: "
            f"aumentar budget 20% ({fmt_ars(best.spend_ars * 1.2 / 7)}/día)"
        )

    if r.overall_roas < 2.0:
        worst = min(r.ad_sets, key=lambda a: a.roas) if r.ad_sets else None
        if worst:
            decisions.append(
                f"PAUSAR {worst.name} — ROAS {fmt_roas(worst.roas)}: "
                f"redistribuir {fmt_ars(worst.spend_ars)} a los ad sets con mejor performance"
            )

    for ads in r.ad_sets:
        if ads.ctr < 0.5:
            decisions.append(
                f"ROTAR creative de {ads.name} — CTR {fmt_pct(ads.ctr)} está por debajo del piso"
            )

    if not decisions:
        decisions.append(
            "MANTENER configuración actual — performance estable. "
            "Revisar el lunes siguiente con foco en frecuencia."
        )

    return decisions[:3]  # max 3 decisions per week


# ─── Input ────────────────────────────────────────────────────────────────────

def from_interactive() -> WeeklyReport:
    print("Weekly Report Generator — Miss Roure")
    period = input("Período (ej: 19/05 – 25/05/2026): ").strip()
    week_n = int(input("Número de semana: ").strip() or "1")
    n_adsets = int(input("¿Cuántos ad sets a reportar? ").strip() or "1")

    ad_sets = []
    for i in range(n_adsets):
        print(f"\n--- Ad Set {i + 1} ---")
        name = input("Nombre: ").strip()
        stage = input("Etapa [tofu/mofu/bofu]: ").strip() or "tofu"
        spend = float(input("Budget invertido (ARS): ").replace(".", "").replace(",", "."))
        impressions = int(input("Impresiones: ").replace(".", ""))
        link_clicks = int(input("Clicks en enlace: ").replace(".", ""))
        conversions = int(input("Conversiones: "))
        revenue = float(input("Revenue atribuido (ARS, 0 si sin píxel): ")
                        .replace(".", "").replace(",", "."))
        reach = int(input("Alcance (0 si no tenés): ").replace(".", "") or "0")

        ad_sets.append(AdSetResult(
            name=name, funnel_stage=stage, spend_ars=spend,
            impressions=impressions, link_clicks=link_clicks,
            conversions=conversions, revenue_ars=revenue, reach=reach,
        ))

    notes = input("\nNotas adicionales (Enter para omitir): ").strip()
    return WeeklyReport(period=period, week_number=week_n, ad_sets=ad_sets, notes=notes)


def from_meta_csv(filepath: str, period: str = "", week_n: int = 1) -> WeeklyReport:
    with open(filepath, encoding="utf-8-sig") as f:
        reader = csv.DictReader(f)
        rows = list(reader)

    def g(row: dict, *keys: str) -> float:
        for k in keys:
            if k in row and row[k].strip() not in ("", "-"):
                return float(row[k].replace(".", "").replace(",", "."))
        return 0.0

    ad_sets = []
    for row in rows:
        ad_sets.append(AdSetResult(
            name=row.get("Nombre del conjunto de anuncios", row.get("Nombre de la campaña", "Ad set")),
            funnel_stage="tofu",
            spend_ars=g(row, "Importe gastado (ARS)", "Importe gastado"),
            impressions=int(g(row, "Impresiones")),
            link_clicks=int(g(row, "Clics en el enlace")),
            conversions=int(g(row, "Compras", "Resultados")),
            revenue_ars=g(row, "Valor de conversión de compras"),
            reach=int(g(row, "Alcance")),
        ))

    if not period:
        period = (
            rows[0].get("Inicio del informe", "?")
            + " — "
            + rows[0].get("Fin del informe", "?")
        )

    return WeeklyReport(period=period, week_number=week_n, ad_sets=ad_sets)


def demo_data() -> WeeklyReport:
    return WeeklyReport(
        period="19/05/2026 – 25/05/2026",
        week_number=21,
        ad_sets=[
            AdSetResult(
                name="Tapados — Mujeres 25-34 GBA",
                funnel_stage="tofu",
                spend_ars=28_000,
                impressions=14_200,
                link_clicks=210,
                conversions=4,
                revenue_ars=250_000,
                reach=9_800,
            ),
            AdSetResult(
                name="Retargeting — Visitantes 7d",
                funnel_stage="bofu",
                spend_ars=12_000,
                impressions=4_800,
                link_clicks=180,
                conversions=3,
                revenue_ars=105_000,
                reach=1_600,
            ),
            AdSetResult(
                name="Cozy Cute — Lookalike 1%",
                funnel_stage="tofu",
                spend_ars=20_000,
                impressions=11_000,
                link_clicks=120,
                conversions=1,
                revenue_ars=38_000,
                reach=7_400,
            ),
        ],
        notes="Semana con lanzamiento del Tapado Bella. CTR más alto que semana anterior.",
    )


# ─── Main ─────────────────────────────────────────────────────────────────────

def main():
    parser = argparse.ArgumentParser(description="Weekly Report Generator — Miss Roure")
    group = parser.add_mutually_exclusive_group()
    group.add_argument("--csv", metavar="FILE")
    group.add_argument("--demo", action="store_true")
    parser.add_argument("--out", metavar="FILE", help="Save report to markdown file")
    parser.add_argument("--period", default="")
    parser.add_argument("--week", type=int, default=1)
    args = parser.parse_args()

    if args.csv:
        data = from_meta_csv(args.csv, args.period, args.week)
    elif args.demo:
        data = demo_data()
    else:
        data = from_interactive()

    report = generate_report(data)
    print(report)

    if args.out:
        Path(args.out).write_text(report, encoding="utf-8")
        print(f"\n✅ Reporte guardado en {args.out}")


if __name__ == "__main__":
    main()
