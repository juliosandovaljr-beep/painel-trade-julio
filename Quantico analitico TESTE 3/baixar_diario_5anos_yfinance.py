import yfinance as yf
import pandas as pd

# Lista de ativos com sufixo .SA para B3 no Yahoo Finance
ativos = ["POMO4.SA", "BRFS3.SA", "WEGE3.SA", "MGLU3.SA"]

for ativo in ativos:
    print(f"🔄 Baixando dados para {ativo}")
    df = yf.download(ativo, period="5y", interval="1d")
    df.reset_index(inplace=True)
    nome_arquivo = f"{ativo.replace('.SA','')}_diario_5anos.csv"
    df.to_csv(nome_arquivo, index=False)
    print(f"✅ Salvo: {nome_arquivo}")
