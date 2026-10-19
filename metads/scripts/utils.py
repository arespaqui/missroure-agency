"""
Shared utilities for Miss Roure Meta Ads analysis scripts.
All monetary values are in ARS (Argentine Pesos).
"""

from dataclasses import dataclass
from typing import Optional


# ─── Currency ────────────────────────────────────────────────────────────────

def fmt_ars(amount: float, decimals: int = 0) -> str:
    """Format a number as Argentine pesos.

    >>> fmt_ars(93750)
    '$93.750 ARS'
    >>> fmt_ars(1234567.5, decimals=2)
    '$1.234.567,50 ARS'
    """
    if decimals == 0:
        rounded = round(amount)
        formatted = f"{rounded:,}".replace(",", ".")
        return f"${formatted} ARS"
    else:
        integer_part = int(amount)
        decimal_part = round((amount - integer_part) * (10 ** decimals))
        int_formatted = f"{integer_part:,}".replace(",", ".")
        return f"${int_formatted},{decimal_part:0{decimals}d} ARS"


def fmt_pct(value: float, decimals: int = 1) -> str:
    """Format a ratio (0-1 or 0-100) as percentage string."""
    if value > 1:
        return f"{value:.{decimals}f}%"
    return f"{value * 100:.{decimals}f}%"


def fmt_roas(roas: float) -> str:
    return f"{roas:.2f}x"


# ─── Benchmarks ──────────────────────────────────────────────────────────────

@dataclass
class Benchmark:
    metric: str
    market_min: float
    market_max: float
    roure_target: float
    unit: str  # "ars", "pct", "x", "raw"
    higher_is_better: bool = True


BENCHMARKS: dict[str, Benchmark] = {
    "roas": Benchmark(
        metric="ROAS",
        market_min=2.0,
        market_max=3.0,
        roure_target=3.0,
        unit="x",
        higher_is_better=True,
    ),
    "ctr": Benchmark(
        metric="CTR (link click)",
        market_min=0.8,
        market_max=1.5,
        roure_target=1.2,
        unit="pct",
        higher_is_better=True,
    ),
    "cpm": Benchmark(
        metric="CPM",
        market_min=2000.0,
        market_max=6000.0,
        roure_target=4500.0,
        unit="ars",
        higher_is_better=False,
    ),
    "cpc": Benchmark(
        metric="CPC",
        market_min=200.0,
        market_max=800.0,
        roure_target=500.0,
        unit="ars",
        higher_is_better=False,
    ),
    "hook_rate": Benchmark(
        metric="Hook rate (3s)",
        market_min=25.0,
        market_max=40.0,
        roure_target=35.0,
        unit="pct",
        higher_is_better=True,
    ),
    "hold_rate": Benchmark(
        metric="Hold rate (15s)",
        market_min=10.0,
        market_max=20.0,
        roure_target=15.0,
        unit="pct",
        higher_is_better=True,
    ),
    "completion_rate": Benchmark(
        metric="Completion rate",
        market_min=15.0,
        market_max=30.0,
        roure_target=25.0,
        unit="pct",
        higher_is_better=True,
    ),
    "frequency_tofu": Benchmark(
        metric="Frecuencia TOFU/semana",
        market_min=1.0,
        market_max=2.0,
        roure_target=2.0,
        unit="x",
        higher_is_better=False,
    ),
    "frequency_bofu": Benchmark(
        metric="Frecuencia BOFU/semana",
        market_min=2.0,
        market_max=6.0,
        roure_target=4.0,
        unit="x",
        higher_is_better=False,
    ),
}

# CPP target is 25% of AOV — defined per category
CATEGORY_AOV_ARS: dict[str, float] = {
    "accesorios": 10_000,
    "maquillaje": 9_000,
    "paris_collection": 20_000,
    "douceur_trendy": 27_000,
    "cozy_cute": 38_000,
    "essentials": 42_000,
    "tapados": 78_000,
}

CPP_TARGET_PCT = 0.25  # 25% of AOV


def cpp_target(category: str) -> float:
    aov = CATEGORY_AOV_ARS.get(category, 35_000)
    return aov * CPP_TARGET_PCT


# ─── Status evaluation ───────────────────────────────────────────────────────

def evaluate(metric: str, value: float, category: Optional[str] = None) -> tuple[str, str]:
    """Return (status_emoji, assessment) for a metric value.

    status_emoji: ✅ good, ⚠️ warning, ❌ bad
    """
    if metric == "cpp" and category:
        target = cpp_target(category)
        if value <= target:
            return "✅", f"Bajo el objetivo de {fmt_ars(target)} (25% AOV)"
        elif value <= target * 1.3:
            return "⚠️", f"Cerca del límite — objetivo {fmt_ars(target)}"
        else:
            return "❌", f"Por encima del objetivo — objetivo {fmt_ars(target)}"

    bench = BENCHMARKS.get(metric)
    if not bench:
        return "—", "Sin benchmark"

    if bench.higher_is_better:
        if value >= bench.roure_target:
            return "✅", f"Supera objetivo Roure ({bench.roure_target}{_unit_suffix(bench.unit)})"
        elif value >= bench.market_min:
            return "⚠️", f"En rango de mercado, bajo objetivo ({bench.roure_target}{_unit_suffix(bench.unit)})"
        else:
            return "❌", f"Por debajo del mercado — mínimo {bench.market_min}{_unit_suffix(bench.unit)}"
    else:
        if value <= bench.roure_target:
            return "✅", f"Bajo objetivo Roure ({bench.roure_target}{_unit_suffix(bench.unit)})"
        elif value <= bench.market_max:
            return "⚠️", f"En rango de mercado, sobre objetivo ({bench.roure_target}{_unit_suffix(bench.unit)})"
        else:
            return "❌", f"Por encima del máximo de mercado — máximo {bench.market_max}{_unit_suffix(bench.unit)}"


def _unit_suffix(unit: str) -> str:
    return {"ars": " ARS", "pct": "%", "x": "x", "raw": ""}.get(unit, "")


# ─── Immediate stop rules ────────────────────────────────────────────────────

def check_stop_rules(
    roas: Optional[float],
    ctr: Optional[float],
    frequency: Optional[float],
    cpp: Optional[float],
    spend_ars: Optional[float],
    conversions: Optional[int],
    funnel_stage: str = "tofu",  # "tofu" or "bofu"
    days_running: int = 0,
) -> list[str]:
    """Return list of urgent action alerts. Empty list = no immediate action needed."""
    alerts = []

    if roas is not None and roas < 1.0 and days_running >= 2:
        alerts.append("🚨 PAUSAR URGENTE — ROAS < 1x por 2+ días: se está perdiendo dinero")

    if (conversions == 0 and spend_ars is not None
            and spend_ars > 15_000 and funnel_stage == "bofu"):
        alerts.append(
            f"🚨 PAUSAR — 0 conversiones con {fmt_ars(spend_ars)} gastados en BOFU"
        )

    if ctr is not None and ctr < 0.3 and (spend_ars or 0) > 0:
        alerts.append("❌ CTR < 0.3% — Creative o audiencia con serio problema")

    if frequency is not None and frequency > 8:
        alerts.append(f"❌ Frecuencia {frequency:.1f}x — Saturación total, renovar audiencia/creative")

    return alerts
