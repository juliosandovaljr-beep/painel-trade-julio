
import streamlit as st
import pandas as pd
import plotly.express as px
import os

st.set_page_config(page_title="Painel de Análise Estatística - Day Trade", layout="wide")

st.title("📊 Painel de Análise Estatística - 30 Ativos Bovespa (Day Trade)")
st.markdown("Visualização interativa de métricas estatísticas com base em gaps, liquidez, rentabilidade e volatilidade diária.")

# Carregar os dados
@st.cache_data
def carregar_dados():
    try:
        # Tentar carregar arquivos de análise se existirem
        if os.path.exists("dashboard_analise_ativos.csv"):
            df_stats = pd.read_csv("dashboard_analise_ativos.csv")
        else:
            # Criar dados mock se não existir
            df_stats = pd.DataFrame({
                "Ativo": ["POMO4", "BRFS3", "WEGE3", "MGLU3"],
                "Dia_Semana": ["Segunda", "Terça", "Quarta", "Quinta"] * 1,
                "Gap_Alto": [10, 15, 8, 12],
                "Gap_Baixo": [5, 8, 3, 7],
                "Sem_Gap": [85, 77, 89, 81]
            })
        
        if os.path.exists("quartis_por_tipo_gap.csv"):
            df_quartis = pd.read_csv("quartis_por_tipo_gap.csv")
        else:
            # Criar dados mock se não existir
            df_quartis = pd.DataFrame({
                "Tipo_Gap": ["Alta", "Baixa", "Sem Gap"],
                "Q1": [0.5, -1.5, -0.2],
                "Q2": [1.0, -0.5, 0.1],
                "Q3": [2.0, 0.5, 0.8]
            })
        
        # Carregar arquivos diários se existirem
        csv_files = [f for f in os.listdir() if f.endswith(".csv") and "diario" in f]
        if csv_files:
            df_all = pd.concat([pd.read_csv(f) for f in csv_files], ignore_index=True)
        else:
            # Criar dados mock se não existir
            df_all = pd.DataFrame({
                "Ticker": ["POMO4", "BRFS3", "WEGE3", "MGLU3"] * 100,
                "Date": pd.date_range("2020-01-01", periods=400),
                "Variação_%": [1.2, -0.8, 2.1, -1.5] * 100,
                "Tipo_Gap": ["Alta", "Baixa", "Sem Gap", "Alta"] * 100,
                "Dia_Semana": ["Segunda", "Terça", "Quarta", "Quinta"] * 100
            })
            
        return df_stats, df_quartis, df_all
    except Exception as e:
        st.error(f"Erro ao carregar dados: {e}")
        return pd.DataFrame(), pd.DataFrame(), pd.DataFrame()

df_stats, df_quartis, df_all = carregar_dados()

# Filtros
ativos = sorted(df_stats["Ativo"].unique())
dias = sorted(df_stats["Dia_Semana"].unique())
gaps = ["Alta", "Baixa", "Sem Gap"]

col1, col2, col3 = st.columns(3)
with col1:
    ativo_sel = st.selectbox("🔎 Selecione o ativo", ativos)
with col2:
    dia_sel = st.selectbox("📅 Dia da Semana", dias)
with col3:
    gap_sel = st.selectbox("⛳ Tipo de Gap", gaps)

st.markdown("---")

# Tabela principal
st.subheader("📋 Tabela Estatística do Ativo Selecionado")
tabela_filtrada = df_stats[(df_stats["Ativo"] == ativo_sel) & (df_stats["Dia_Semana"] == dia_sel)]
st.dataframe(tabela_filtrada)

# Rentabilidade por tipo de gap
st.subheader("💰 Rentabilidade Média por Tipo de Gap")
rent_df = df_all[df_all["Ticker"] == ativo_sel].groupby("Tipo_Gap")["Variação_%"].mean().reset_index()
fig_rent = px.bar(rent_df, x="Tipo_Gap", y="Variação_%", color="Tipo_Gap", title="Rentabilidade Média (%)")
st.plotly_chart(fig_rent, use_container_width=True)

# Quartis do ativo selecionado por gap
st.subheader("📦 Quartis de Variação % por Tipo de Gap")
qdf = df_all[df_all["Ticker"] == ativo_sel]
fig_box = px.box(qdf, x="Tipo_Gap", y="Variação_%", color="Tipo_Gap", title="Distribuição de Variação (%) por Tipo de Gap")
st.plotly_chart(fig_box, use_container_width=True)

# Frequência de gaps por dia
st.subheader("📈 Frequência de Gaps por Dia da Semana")
freq = df_all[df_all["Ticker"] == ativo_sel].groupby(["Dia_Semana", "Tipo_Gap"]).size().reset_index(name="Frequência")
fig_freq = px.bar(freq, x="Dia_Semana", y="Frequência", color="Tipo_Gap", barmode="group", title="Frequência de Gaps")
st.plotly_chart(fig_freq, use_container_width=True)

# Exportação
st.markdown("📤 Baixe os dados filtrados para Excel:")
st.download_button("⬇️ Exportar CSV", tabela_filtrada.to_csv(index=False), file_name=f"{ativo_sel}_{dia_sel}_estatisticas.csv")
