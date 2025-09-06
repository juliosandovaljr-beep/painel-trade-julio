"""Data handling utilities for metric loading."""

from __future__ import annotations

from typing import List
import pandas as pd

REQUIRED_COLUMNS: List[str] = [
    "Expectativa_Pontos",
    "Fator_Lucro_MME",
    "Taxa_Acerto",
    "N_Trades",
    "ATR14_Medio",
    "OR10_Medio",
    "Drawdown_Medio",
    "Fechamento_Ant_Medio",
    "Ticker",
    "Dia_Semana",
]


def load_metrics(csv_path: str) -> pd.DataFrame:
    """Load metrics from a CSV file ensuring required columns are present.

    Args:
        csv_path: Path to the metrics CSV file.

    Returns:
        DataFrame containing the metrics.

    Raises:
        ValueError: If any required columns are missing from the file.
    """
    df = pd.read_csv(csv_path)
    missing = [col for col in REQUIRED_COLUMNS if col not in df.columns]
    if missing:
        raise ValueError(f"Missing columns in metrics file: {', '.join(missing)}")
    return df
