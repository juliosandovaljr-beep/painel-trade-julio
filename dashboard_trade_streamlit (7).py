
import streamlit as st
import pandas as pd
import requests

st.set_page_config(layout="wide")

st.title("📈 Painel Interativo - Análise de Ativos B3 via BRAPI")

st.markdown("### 🔐 Cole seu token da BRAPI:")
token = st.text_input("Token", type="password")

st.markdown("### 🎯 Escolha o ativo")
ticker = st.selectbox("Escolha o ativo", ["VALE3", "PETR4", "ITUB4", "BBDC4", "MGLU3", "BBAS3", "WEGE3", "ABEV3", "B3SA3", "LREN3"])

range_map = {
    "15 minutos": ("5y", "15m"),
    "30 minutos": ("5y", "30m"),
    "1 hora": ("5y", "60m"),
    "4 horas": ("5y", "240m"),
    "Diário": ("5y", "1d")
}

st.markdown("### ⏱️ Intervalo")
interval_api = st.selectbox("Intervalo", list(range_map.keys()))

def buscar_dados(ticker, token, interval, range_):
    url = f"https://brapi.dev/api/quote/{ticker}?range={range_}&interval={interval}&token={token}"
    response = requests.get(url)
    response.raise_for_status()
    data = response.json()
    prices = data["results"][0]["historicalDataPrice"]
    df = pd.DataFrame(prices)
    df["date"] = pd.to_datetime(df["date"], unit="s")
    df.set_index("date", inplace=True)
    df.sort_index(inplace=True)
    df.rename(columns={
        "open": "Abertura",
        "high": "Máxima",
        "low": "Mínima",
        "close": "Fechamento",
        "volume": "Volume"
    }, inplace=True)
    return df

if st.button("🔍 Consultar"):
    if not token:
        st.error("Por favor, insira seu token da BRAPI.")
    else:
        with st.spinner("Consultando dados..."):
            try:
                range_value, interval_value = range_map[interval_api]
                df = buscar_dados(ticker, token, interval_value, range_value)
                st.success("Dados carregados com sucesso!")
                st.dataframe(df.tail(100))
            except Exception as e:
                st.error(f"Ocorreu um erro ao carregar os dados: {e}")
