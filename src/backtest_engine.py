"""Backtest engine module.

This module provides utilities to calculate trade results based on OHLC data.
"""
from __future__ import annotations

import pandas as pd


def calculate_trade_results(df_diario: pd.DataFrame) -> pd.DataFrame:
    """Calculate trade results for a given daily dataframe.

    The function expects OHLC columns named in English (Open, High, Low, Close)
    and renames them to the Portuguese standard used across the project.
    It ensures the ``Fechamento`` column exists before proceeding.

    Args:
        df_diario: DataFrame containing OHLC price data.

    Returns:
        DataFrame with renamed columns ready for further processing.

    Raises:
        ValueError: If the ``Fechamento`` column is absent after renaming.
    """
    df_diario = df_diario.rename(
        columns={
            "Open": "Abertura",
            "High": "Maxima",
            "Low": "Minima",
            "Close": "Fechamento",
        }
    )

    if "Fechamento" not in df_diario.columns:
        raise ValueError("Coluna 'Fechamento' ausente no DataFrame.")

    # Further processing would occur here, e.g., grouping or calculations.
    return df_diario
