import pandas as pd
import numpy as np
from datetime import datetime, timedelta

# Criar dados simulados para demonstração
def criar_dados_simulados():
    ativos = ["POMO4", "BRFS3", "WEGE3", "MGLU3"]
    
    # Dados simulados de 5 anos
    start_date = datetime.now() - timedelta(days=5*365)
    dates = pd.date_range(start=start_date, periods=1000, freq='D')
    
    for ativo in ativos:
        # Simular preços base
        base_price = np.random.uniform(10, 100)
        
        # Simular dados históricos
        data = []
        current_price = base_price
        
        for i, date in enumerate(dates):
            # Simular variação diária
            variation = np.random.normal(0, 0.02)  # 2% de volatilidade
            current_price = current_price * (1 + variation)
            
            # Garantir que preços não fiquem negativos
            current_price = max(current_price, 1.0)
            
            # OHLC simulado
            high = current_price * (1 + abs(np.random.normal(0, 0.01)))
            low = current_price * (1 - abs(np.random.normal(0, 0.01)))
            open_price = current_price * (1 + np.random.normal(0, 0.005))
            
            volume = np.random.randint(100000, 1000000)
            
            data.append({
                'Date': date.strftime('%Y-%m-%d'),
                'Open': round(open_price, 2),
                'High': round(high, 2),
                'Low': round(low, 2),
                'Close': round(current_price, 2),
                'Adj Close': round(current_price, 2),
                'Volume': volume
            })
        
        # Salvar CSV
        df = pd.DataFrame(data)
        df.to_csv(f"{ativo}_diario_5anos.csv", index=False)
        print(f"✅ Dados simulados salvos: {ativo}_diario_5anos.csv")

if __name__ == "__main__":
    criar_dados_simulados()