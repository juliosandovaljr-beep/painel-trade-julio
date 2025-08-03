import streamlit as st
import pandas as pd
import requests
from datetime import datetime, timedelta

# Lista de 30 ações da B3
acoes_b3 = [
    "PETR4", "VALE3", "ITUB4", "BBDC4", "ABEV3", "BBAS3", "WEGE3", "MGLU3",
    "B3SA3", "LREN3", "RENT3", "SUZB3", "JBSS3", "GGBR4", "EQTL3", "RADL3",
    "HAPV3", "ASAI3", "PRIO3", "RAIZ4", "CSAN3", "BRFS3", "ELET3", "UGPA3",
    "KLBN11", "PETZ3", "ALPA4", "TIMS3", "ENEV3", "POMO4"
]

# Token da BRAPI (deve estar no Streamlit Secrets ou variável local)
TOKEN = "5rAQpiweG1TKbvBwBidopz"

def obter_dados_acao(ticker):
    fim = datetime.now().date()
    inicio = fim - timedelta(days=5*365)  # Últimos 5 anos

    url = f"https://brapi.dev/api/quote/{ticker}?range=5y&interval=1d&token={TOKEN}"
    resposta = requests.get(url)

    if resposta.status_code == 200:
        dados = resposta.json()
        historico = dados["results"][0]["historicalDataPrice"]
        df = pd.DataFrame(historico)
        df["date"] = pd.to_datetime(df["date"], unit="s").dt.date
        df["ticker"] = ticker
        return df
    else:
        st.error(f"Erro ao carregar dados para {ticker}")
        return pd.DataFrame()

# Interface do Streamlit
st.title("📈 Análise Histórica de Ações - B3 (5 Anos)")
st.write("Selecione uma ação para visualizar seu histórico de preços com base na API BRAPI.")

acao_selecionada = st.selectbox("Escolha uma ação", acoes_b3)

if acao_selecionada:
    st.info(f"Carregando dados históricos da ação {acao_selecionada}...")
    dados = obter_dados_acao(acao_selecionada)

    if not dados.empty:
        st.success("Dados carregados com sucesso!")
        st.line_chart(data=dados.set_index("date")[["close"]], height=400)
        st.dataframe(dados.tail(30))
    else:
        st.warning("Não foi possível obter os dados. Verifique o token ou conexão.")
