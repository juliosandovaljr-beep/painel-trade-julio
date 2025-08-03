import streamlit as st
import pandas as pd

# Lista de ativos e links extraída do txt
ativos = {
    "ABEV3": "https://finance.yahoo.com/quote/ABEV3.SA/history",
    "BBAS3": "https://finance.yahoo.com/quote/BBAS3.SA/history",
    "BBDC4": "https://finance.yahoo.com/quote/BBDC4.SA/history",
    "BRFS3": "https://finance.yahoo.com/quote/BRFS3.SA/history",
    "BRKM5": "https://finance.yahoo.com/quote/BRKM5.SA/history",
    "CMIG4": "https://finance.yahoo.com/quote/CMIG4.SA/history",
    "CPLE6": "https://finance.yahoo.com/quote/CPLE6.SA/history",
    "CSAN3": "https://finance.yahoo.com/quote/CSAN3.SA/history",
    "CSNA3": "https://finance.yahoo.com/quote/CSNA3.SA/history",
    "ECOR3": "https://finance.yahoo.com/quote/ECOR3.SA/history",
    "ELET3": "https://finance.yahoo.com/quote/ELET3.SA/history",
    "GGBR4": "https://finance.yahoo.com/quote/GGBR4.SA/history",
    "GRND3": "https://finance.yahoo.com/quote/GRND3.SA/history",
    "ITSA4": "https://finance.yahoo.com/quote/ITSA4.SA/history",
    "ITUB4": "https://finance.yahoo.com/quote/ITUB4.SA/history",
    "LREN3": "https://finance.yahoo.com/quote/LREN3.SA/history",
    "MGLU3": "https://finance.yahoo.com/quote/MGLU3.SA/history",
    "MRVE3": "https://finance.yahoo.com/quote/MRVE3.SA/history",
    "PETR4": "https://finance.yahoo.com/quote/PETR4.SA/history",
    "POMO4": "https://finance.yahoo.com/quote/POMO4.SA/history",
    "VIVT3": "https://finance.yahoo.com/quote/VIVT3.SA/history",
    "PRIO3": "https://finance.yahoo.com/quote/PRIO3.SA/history",
    "RADL3": "https://finance.yahoo.com/quote/RADL3.SA/history",
    "RAPT4": "https://finance.yahoo.com/quote/RAPT4.SA/history",
    "RENT3": "https://finance.yahoo.com/quote/RENT3.SA/history",
    "SANB11": "https://finance.yahoo.com/quote/SANB11.SA/history",
    "SUZB3": "https://finance.yahoo.com/quote/SUZB3.SA/history",
    "TAEE3": "https://finance.yahoo.com/quote/TAEE3.SA/history",
    "VALE3": "https://finance.yahoo.com/quote/VALE3.SA/history",
    "WEGE3": "https://finance.yahoo.com/quote/WEGE3.SA/history"
}

estrategias = {
    "POMO4": "Abertura acima da máxima anterior OU quartil inferior com gap de baixa ou sem gap",
    "BRFS3": "Quartil inferior OU gap de baixa ou sem gap",
    "WEGE3": "Quartil inferior OU gap de baixa",
    "MGLU3": "Quartil inferior OU gap de baixa"
}

st.set_page_config(page_title="Estatísticas de Trade Bovespa", layout="wide")
st.title("📊 Painel Estatístico de Ações Bovespa")

ativo = st.selectbox("Selecione um ativo para análise:", sorted(ativos.keys()))

st.markdown(f"🔗 [Histórico completo no Yahoo Finance]({ativos[ativo]})")

if ativo in estrategias:
    st.info(f"🧠 Estratégia aplicada: {estrategias[ativo]}")
else:
    st.warning("📌 Nenhuma estratégia específica definida para este ativo no plano estratégico.")

st.markdown("🚧 Funcionalidades futuras: leitura automática dos preços históricos, cálculos de retorno e gráficos de performance.")

st.success("✅ Projeto reestruturado e pronto para expansão com dados reais.")
