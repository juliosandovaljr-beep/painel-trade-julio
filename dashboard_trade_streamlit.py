import streamlit as st
import pandas as pd
import plotly.graph_objects as go

# Carregar dados
df = pd.read_csv('Ativos historicos de preços.txt', sep=';')

# Lista de ativos disponíveis
ativos = df['ativo'].unique()

# Sidebar: selecionar ativo
ativo_selecionado = st.sidebar.selectbox('Selecione o ativo:', ativos)

# Filtrar dados do ativo escolhido
df_ativo = df[df['ativo'] == ativo_selecionado].copy()
df_ativo['data'] = pd.to_datetime(df_ativo['data'])
df_ativo.sort_values('data', inplace=True)

# Selecionar último candle
ultimo = df_ativo.iloc[-1]

# Calcular quartis
q1 = df_ativo['fechamento'].quantile(0.25)
q2 = df_ativo['fechamento'].quantile(0.50)
q3 = df_ativo['fechamento'].quantile(0.75)
minimo = df_ativo['fechamento'].min()
maximo = df_ativo['fechamento'].max()

# Mostrar estatísticas
st.title(f'Análise Estatística - {ativo_selecionado}')
st.metric('Último Fechamento', f"R$ {ultimo['fechamento']:.2f}")
st.write(f"Máxima: R$ {ultimo['maxima']:.2f} | Mínima: R$ {ultimo['minima']:.2f}")
st.write(f"Abertura: R$ {ultimo['abertura']:.2f} | Volume: {int(ultimo['volume']):,}")

# Plotly: gráfico com quartis
fig = go.Figure()

# Área de quartis
fig.add_shape(type="rect", x0=0, x1=1, y0=minimo, y1=q1,
              fillcolor="lightblue", opacity=0.3, line_width=0)
fig.add_shape(type="rect", x0=0, x1=1, y0=q1, y1=q2,
              fillcolor="lightgreen", opacity=0.3, line_width=0)
fig.add_shape(type="rect", x0=0, x1=1, y0=q2, y1=q3,
              fillcolor="khaki", opacity=0.3, line_width=0)
fig.add_shape(type="rect", x0=0, x1=1, y0=q3, y1=maximo,
              fillcolor="lightcoral", opacity=0.3, line_width=0)

# Candle do último dia
fig.add_trace(go.Candlestick(
    x=[str(ultimo['data'].date())],
    open=[ultimo['abertura']],
    high=[ultimo['maxima']],
    low=[ultimo['minima']],
    close=[ultimo['fechamento']],
    name='Último Candle'
))

# Quartis como linhas
fig.add_hline(y=q1, line_dash="dot", line_color="blue", annotation_text="Q1")
fig.add_hline(y=q2, line_dash="dot", line_color="green", annotation_text="Mediana (Q2)")
fig.add_hline(y=q3, line_dash="dot", line_color="red", annotation_text="Q3")

fig.update_layout(title=f"Distribuição dos preços - {ativo_selecionado}", height=600)
st.plotly_chart(fig, use_container_width=True)
