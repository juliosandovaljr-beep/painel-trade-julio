"""
Sample data generator for QuantAlpha testing
Creates realistic sample data when Yahoo Finance is not available
"""

import pandas as pd
import numpy as np
from datetime import datetime, timedelta
import random

def generate_sample_stock_data(ticker: str, days: int = 500) -> pd.DataFrame:
    """Gera dados de amostra realistas para teste do QuantAlpha"""
    
    # Parâmetros específicos por ativo para realismo
    ativo_params = {
        'PETR4': {'price': 35.50, 'volatility': 0.35, 'trend': -0.0002},
        'VALE3': {'price': 55.80, 'volatility': 0.40, 'trend': 0.0001},
        'ITUB4': {'price': 28.90, 'volatility': 0.30, 'trend': 0.0001},
        'BBDC4': {'price': 12.45, 'volatility': 0.32, 'trend': -0.0001},
        'WEGE3': {'price': 42.15, 'volatility': 0.28, 'trend': 0.0003},
        'MGLU3': {'price': 8.20, 'volatility': 0.45, 'trend': -0.0005},
        'ABEV3': {'price': 11.85, 'volatility': 0.25, 'trend': 0.0000},
        'BBAS3': {'price': 26.30, 'volatility': 0.31, 'trend': 0.0001}
    }
    
    # Usar parâmetros específicos ou default
    params = ativo_params.get(ticker, {'price': 30.0, 'volatility': 0.35, 'trend': 0.0})
    
    # Gerar datas
    end_date = datetime.now()
    start_date = end_date - timedelta(days=days)
    dates = pd.date_range(start=start_date, end=end_date, freq='D')
    dates = dates[dates.dayofweek < 5]  # Apenas dias úteis
    
    # Simulação de preços com caminhada aleatória + tendência
    np.random.seed(42)  # Para reprodutibilidade
    returns = np.random.normal(params['trend'], params['volatility']/16, len(dates))
    
    # Preços
    prices = [params['price']]
    for ret in returns[1:]:
        new_price = prices[-1] * (1 + ret)
        prices.append(max(new_price, 1.0))  # Preço mínimo de R$ 1,00
    
    # Calcular OHLC realista
    df = pd.DataFrame(index=dates)
    df['Close'] = prices
    
    # Gerar High/Low/Open baseados no Close
    daily_ranges = np.random.lognormal(0, 0.02, len(dates))  # Variação intraday
    
    df['High'] = df['Close'] * (1 + daily_ranges/2)
    df['Low'] = df['Close'] * (1 - daily_ranges/2)
    
    # Open baseado no close anterior + gap pequeno
    gaps = np.random.normal(0, 0.005, len(dates))
    df['Open'] = df['Close'].shift(1) * (1 + gaps)
    df['Open'].iloc[0] = df['Close'].iloc[0]
    
    # Ajustar High/Low para consistência
    df['High'] = df[['High', 'Open', 'Close']].max(axis=1)
    df['Low'] = df[['Low', 'Open', 'Close']].min(axis=1)
    
    # Volume realista
    base_volume = random.randint(10000000, 50000000)
    volume_multipliers = np.random.lognormal(0, 0.3, len(dates))
    df['Volume'] = (base_volume * volume_multipliers).astype(int)
    
    # Adj Close = Close (simplificado)
    df['Adj Close'] = df['Close']
    
    return df

def get_sample_analysis_result(ticker: str) -> dict:
    """Retorna resultado de análise simulada para demonstração"""
    
    # Simular dados baseados no ticker
    sample_results = {
        'PETR4': {
            'current_price': 35.48,
            'current_volatility': 0.324,
            'current_rsi': 45.2,
            'backtest': {
                'hit_rate': 0.678,
                'profit_factor': 1.85,
                'max_drawdown': -0.184,
                'expectativa_matematica': 0.0023,
                'payoff_ratio': 1.32,
                'num_trades': 87
            }
        },
        'VALE3': {
            'current_price': 56.12,
            'current_volatility': 0.398,
            'current_rsi': 52.8,
            'backtest': {
                'hit_rate': 0.712,
                'profit_factor': 2.14,
                'max_drawdown': -0.156,
                'expectativa_matematica': 0.0031,
                'payoff_ratio': 1.48,
                'num_trades': 92
            }
        },
        'ITUB4': {
            'current_price': 28.76,
            'current_volatility': 0.289,
            'current_rsi': 38.5,
            'backtest': {
                'hit_rate': 0.645,
                'profit_factor': 1.67,
                'max_drawdown': -0.201,
                'expectativa_matematica': 0.0018,
                'payoff_ratio': 1.28,
                'num_trades': 103
            }
        }
    }
    
    return sample_results.get(ticker, sample_results['PETR4'])