import sys
from pathlib import Path

import pandas as pd
import pytest

sys.path.append(str(Path(__file__).resolve().parents[1]))
from src.data_handler import load_metrics


def test_load_metrics_missing_columns(tmp_path):
    data = {
        "Expectativa_Pontos": [1],
        "Fator_Lucro_MME": [1],
        "Taxa_Acerto": [1],
        "N_Trades": [1],
        "ATR14_Medio": [1],
        # Missing OR10_Medio
        "Drawdown_Medio": [1],
        "Fechamento_Ant_Medio": [1],
        "Ticker": ["ABC"],
        # Missing Dia_Semana
    }
    df = pd.DataFrame(data)
    csv_file = tmp_path / "metrics.csv"
    df.to_csv(csv_file, index=False)

    with pytest.raises(ValueError) as exc_info:
        load_metrics(str(csv_file))

    message = str(exc_info.value)
    assert "OR10_Medio" in message
    assert "Dia_Semana" in message
