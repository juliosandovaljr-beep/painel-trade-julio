import streamlit as st
import pandas as pd
import numpy as np

st.set_page_config(page_title="Painel de Trade", layout="wide")

st.title("📈 Painel de Trade do Dr. Julio Sandoval")

# Gerar dados simulados
data = pd.DataFrame({
    'Data': pd.date_range(start='2024-01-01', periods=30),
    'Preço': np.random.normal(50, 5, size=30).round(2)
})

st.line_chart(data.set_index('Data'))

st.write("📊 Tabela de dados:")
st.dataframe(data)
