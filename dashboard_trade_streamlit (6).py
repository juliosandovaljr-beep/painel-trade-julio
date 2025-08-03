import streamlit as st
import pandas as pd
import requests
import plotly.graph_objects as go

st.set_page_config(page_title="Painel de Ações B3", layout="wide")
st.title("📈 Painel Interativo - Análise de Ativos B3 via BRAPI")

# Input para o token
token = st.text_input("🔐 Cole seu token da BRAPI:", type="password")

# Dropdowns
ticker = st.selectbox("Escolha o ativo", [
    "VALE3", "PETR4", "BBAS3", "ITUB4", "BBDC4", "WEGE3", "POMO4", "MGLU3", "RENT3", "LREN3"
])

intervalo = st.selectbox("Intervalo", {
    "15 minutos": "15m",
    "30 minutos": "30m",
    "1 hora": "60m",
    "4 horas": "60m",  # agrupamento local
    "Diário": "1d"
})

range_map = {
    "15m": "5d",
    "30m": "5d",
    "60m": "5d",
    "1d": "1y"
}
interval_api = intervalo
if intervalo == "4 horas":
    interval_api = "60m"

def buscar_dados(ticker, token, intervalo, range_):
    url = f"https://brapi.dev/api/quote/{ticker}?range={range_}&interval={intervalo}&token={token}"
    resp = requests.get(url)
    if resp.status_code == 200:
        hist = resp.json()["results"][0]["historicalDataPrice"]
        df = pd.DataFrame(hist)
        df["date"] = pd.to_datetime(df["date"], unit="s")
        df.rename(columns={"open": "Abertura", "high": "Máxima", "low": "Mínima", "close": "Fechamento", "volume": "Volume"}, inplace=True)
        df["Variação R$"] = df["Fechamento"] - df["Abertura"]
        df["Variação %"] = (df["Variação R$"] / df["Abertura"]) * 100
        df["Volatilidade %"] = (df["Máxima"] - df["Mínima"]) / df["Abertura"] * 100
        return df[["date", "Abertura", "Máxima", "Mínima", "Fechamento", "Volume", "Variação R$", "Variação %", "Volatilidade %"]]
    else:
        return pd.DataFrame()

# Botão de execução
if token and st.button("🔎 Consultar"):
    st.info("Consultando dados...")
    df = buscar_dados(ticker, token, interval_api, range_map[interval_api])
    if not df.empty:
        st.success("✅ Dados carregados com sucesso!")
        st.dataframe(df.tail(30), use_container_width=True)

        fig = go.Figure()
        fig.add_trace(go.Scatter(x=df["date"], y=df["Fechamento"], name="Fechamento", mode="lines+markers"))
        fig.update_layout(title=f"{ticker} - {intervalo}", xaxis_title="Data", yaxis_title="Preço (R$)")
        st.plotly_chart(fig, use_container_width=True)

        # Download CSV
        csv = df.to_csv(index=False).encode("utf-8")
        st.download_button("📥 Baixar CSV", data=csv, file_name=f"{ticker}_{interval_api}_historico.csv", mime="text/csv")
    else:
        st.error("Erro ao carregar os dados. Verifique o token ou ticker.")