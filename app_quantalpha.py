"""
Interface Streamlit para o QuantAlpha
Análise quantitativa especializada em B3/Bovespa
"""

import streamlit as st
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
from quantalpha import QuantAlpha
import yfinance as yf
from datetime import datetime, timedelta
import numpy as np

# Configuração da página
st.set_page_config(
    page_title="QuantAlpha - Análise Quantitativa B3",
    page_icon="📊",
    layout="wide",
    initial_sidebar_state="expanded"
)

# CSS personalizado
st.markdown("""
<style>
    .main-header {
        font-size: 2.5rem;
        font-weight: bold;
        color: #1f77b4;
        text-align: center;
        margin-bottom: 1rem;
    }
    .metric-card {
        background-color: #f0f2f6;
        padding: 1rem;
        border-radius: 0.5rem;
        border-left: 4px solid #1f77b4;
    }
    .positive {
        color: #00D100;
        font-weight: bold;
    }
    .negative {
        color: #FF6B6B;
        font-weight: bold;
    }
    .neutral {
        color: #FFA500;
        font-weight: bold;
    }
</style>
""", unsafe_allow_html=True)

# Inicializar QuantAlpha
@st.cache_resource
def init_quantalpha():
    return QuantAlpha()

quantalpha = init_quantalpha()

# Header principal
st.markdown('<div class="main-header">🤖 QuantAlpha - Analista Quantitativo B3</div>', unsafe_allow_html=True)
st.markdown("**Sua ponte entre a complexidade matemática e a tomada de decisão humana**")

# Sidebar
st.sidebar.header("🎯 Configurações de Análise")

# Lista de ativos populares da B3
ativos_populares = [
    "PETR4", "VALE3", "ITUB4", "BBDC4", "ABEV3", "WEGE3", "MGLU3", "BBAS3",
    "SUZB3", "RENT3", "RAIL3", "CCRO3", "CSAN3", "RADL3", "UGPA3", "VIVT3",
    "GOAU4", "NTCO3", "TIMP3", "SBSP3", "ELET3", "CPLE6", "EMBR3", "LREN3",
    "BRFS3", "JBSS3", "MRFG3", "BEEF3", "POMO4", "AZUL4"
]

# Input de ativo
col1, col2 = st.sidebar.columns([3, 1])
with col1:
    ativo_input = st.selectbox(
        "📈 Selecione o Ativo",
        ativos_populares,
        index=0,
        help="Escolha um ativo da B3 para análise quantitativa"
    )
with col2:
    ativo_custom = st.text_input("Ou digite:", placeholder="XXXX4")

# Usar ativo customizado se fornecido
ativo_selecionado = ativo_custom.upper() if ativo_custom else ativo_input

# Período de análise
periodo = st.sidebar.selectbox(
    "⏰ Período de Análise",
    ["1y", "2y", "5y"],
    index=1,
    help="Período histórico para cálculos estatísticos"
)

# Botão de análise
if st.sidebar.button("🚀 Executar Análise QuantAlpha", type="primary"):
    st.session_state.executar_analise = True
    st.session_state.ativo_analise = ativo_selecionado

# Verificar se deve executar análise
if hasattr(st.session_state, 'executar_analise') and st.session_state.executar_analise:
    with st.spinner(f"🔄 QuantAlpha analisando {st.session_state.ativo_analise}..."):
        try:
            # Executar análise
            analysis_data = quantalpha.analyze_asset(st.session_state.ativo_analise)
            
            if 'error' in analysis_data:
                st.error(f"❌ {analysis_data['error']}")
            else:
                # Gerar relatório completo
                relatorio = quantalpha.get_quantalpha_prompt_response(st.session_state.ativo_analise)
                
                # Exibir relatório principal
                st.markdown("---")
                st.markdown(relatorio)
                
                # Seção de métricas visuais
                st.markdown("---")
                st.header("📊 Dashboard Quantitativo")
                
                # Métricas principais em colunas
                col1, col2, col3, col4, col5 = st.columns(5)
                
                with col1:
                    hit_rate = analysis_data['backtest']['hit_rate'] * 100
                    color = "positive" if hit_rate > 60 else "negative" if hit_rate < 50 else "neutral"
                    st.markdown(f'<div class="metric-card"><h4>Taxa de Acerto</h4><p class="{color}">{hit_rate:.1f}%</p></div>', unsafe_allow_html=True)
                
                with col2:
                    profit_factor = analysis_data['backtest']['profit_factor']
                    color = "positive" if profit_factor > 1.5 else "negative" if profit_factor < 1.2 else "neutral"
                    st.markdown(f'<div class="metric-card"><h4>Fator de Lucro</h4><p class="{color}">{profit_factor:.2f}</p></div>', unsafe_allow_html=True)
                
                with col3:
                    max_dd = analysis_data['backtest']['max_drawdown'] * 100
                    color = "positive" if max_dd > -10 else "negative" if max_dd < -20 else "neutral"
                    st.markdown(f'<div class="metric-card"><h4>Drawdown Máx</h4><p class="{color}">{max_dd:.1f}%</p></div>', unsafe_allow_html=True)
                
                with col4:
                    expectativa = analysis_data['backtest']['expectativa_matematica'] * 100
                    color = "positive" if expectativa > 0 else "negative"
                    st.markdown(f'<div class="metric-card"><h4>Expectativa Mat.</h4><p class="{color}">{expectativa:.3f}%</p></div>', unsafe_allow_html=True)
                
                with col5:
                    rsi = analysis_data['current_rsi']
                    color = "negative" if rsi > 70 else "positive" if rsi < 30 else "neutral"
                    st.markdown(f'<div class="metric-card"><h4>RSI Atual</h4><p class="{color}">{rsi:.1f}</p></div>', unsafe_allow_html=True)
                
                # Gráfico de volatilidade esperada
                st.subheader("📈 Faixas de Volatilidade Esperada")
                
                fig_vol = go.Figure()
                
                # Preço atual
                current_price = analysis_data['current_price']
                fig_vol.add_hline(y=current_price, line_dash="solid", line_color="blue", 
                                annotation_text=f"Preço Atual: R$ {current_price:.2f}")
                
                # Faixas de volatilidade
                vol_ranges = analysis_data['volatility_ranges']
                
                # 2 desvios padrão (95%)
                fig_vol.add_hrect(y0=vol_ranges['lower_2std'], y1=vol_ranges['upper_2std'],
                                fillcolor="lightblue", opacity=0.2, line_width=0,
                                annotation_text="95% Probabilidade (2σ)")
                
                # 1 desvio padrão (68%)
                fig_vol.add_hrect(y0=vol_ranges['lower_1std'], y1=vol_ranges['upper_1std'],
                                fillcolor="lightgreen", opacity=0.3, line_width=0,
                                annotation_text="68% Probabilidade (1σ)")
                
                # Níveis técnicos
                tech_levels = analysis_data['technical_levels']
                fig_vol.add_hline(y=tech_levels['ma20'], line_dash="dash", line_color="orange",
                                annotation_text=f"MA20: R$ {tech_levels['ma20']:.2f}")
                fig_vol.add_hline(y=tech_levels['support'], line_dash="dot", line_color="red",
                                annotation_text=f"Suporte: R$ {tech_levels['support']:.2f}")
                fig_vol.add_hline(y=tech_levels['resistance'], line_dash="dot", line_color="green",
                                annotation_text=f"Resistência: R$ {tech_levels['resistance']:.2f}")
                
                fig_vol.update_layout(
                    title=f"Faixas de Preço Esperadas - {analysis_data['ticker']}",
                    yaxis_title="Preço (R$)",
                    xaxis_title="Probabilidade Estatística",
                    height=400,
                    showlegend=False
                )
                
                st.plotly_chart(fig_vol, use_container_width=True)
                
                # Tabela de níveis chave
                st.subheader("🎯 Níveis de Preço Estratégicos")
                
                niveis_df = pd.DataFrame({
                    'Nível': [
                        'Entrada Estatística (1σ Inferior)',
                        'Stop Loss Matemático', 
                        'Preço Atual',
                        'Alvo Primário (MA20)',
                        'Alvo Secundário (1σ Superior)',
                        'Resistência Técnica'
                    ],
                    'Preço (R$)': [
                        f"{vol_ranges['lower_1std']:.2f}",
                        f"{tech_levels['support']:.2f}",
                        f"{current_price:.2f}",
                        f"{tech_levels['ma20']:.2f}",
                        f"{vol_ranges['upper_1std']:.2f}",
                        f"{tech_levels['resistance']:.2f}"
                    ],
                    'Distância (%)': [
                        f"{((vol_ranges['lower_1std'] - current_price) / current_price * 100):+.1f}%",
                        f"{((tech_levels['support'] - current_price) / current_price * 100):+.1f}%",
                        "0.0%",
                        f"{((tech_levels['ma20'] - current_price) / current_price * 100):+.1f}%",
                        f"{((vol_ranges['upper_1std'] - current_price) / current_price * 100):+.1f}%",
                        f"{((tech_levels['resistance'] - current_price) / current_price * 100):+.1f}%"
                    ]
                })
                
                st.dataframe(niveis_df, use_container_width=True)
                
                # Download do relatório
                st.subheader("📥 Exportar Análise")
                col1, col2 = st.columns(2)
                
                with col1:
                    st.download_button(
                        "📄 Download Relatório (TXT)",
                        relatorio,
                        file_name=f"quantalpha_{analysis_data['ticker']}_{datetime.now().strftime('%Y%m%d_%H%M')}.txt",
                        mime="text/plain"
                    )
                
                with col2:
                    # Dados estruturados para CSV
                    export_data = {
                        'Métrica': [
                            'Taxa de Acerto (%)',
                            'Fator de Lucro',
                            'Drawdown Máximo (%)',
                            'Expectativa Matemática (%)',
                            'RSI Atual',
                            'Preço Atual (R$)',
                            'Volatilidade Anual (%)',
                            'Entrada Sugerida (R$)',
                            'Stop Loss (R$)',
                            'Alvo Primário (R$)'
                        ],
                        'Valor': [
                            f"{hit_rate:.1f}",
                            f"{profit_factor:.2f}",
                            f"{max_dd:.1f}",
                            f"{expectativa:.3f}",
                            f"{rsi:.1f}",
                            f"{current_price:.2f}",
                            f"{analysis_data['current_volatility']*100:.1f}",
                            f"{vol_ranges['lower_1std']:.2f}",
                            f"{tech_levels['support']:.2f}",
                            f"{tech_levels['ma20']:.2f}"
                        ]
                    }
                    
                    export_df = pd.DataFrame(export_data)
                    st.download_button(
                        "📊 Download Métricas (CSV)",
                        export_df.to_csv(index=False),
                        file_name=f"quantalpha_metricas_{analysis_data['ticker']}_{datetime.now().strftime('%Y%m%d_%H%M')}.csv",
                        mime="text/csv"
                    )
                
                # Reset flag
                st.session_state.executar_analise = False
                
        except Exception as e:
            st.error(f"❌ Erro durante a análise: {str(e)}")
            st.session_state.executar_analise = False

else:
    # Tela inicial
    st.markdown("---")
    st.markdown("""
    ## 🎯 Bem-vindo ao QuantAlpha!
    
    Sou seu **analista de dados quantitativos sênior**, especializado no mercado de ações brasileiro (B3/Bovespa). 
    Minha missão é transformar dados históricos e resultados de backtests em **insights acionáveis** para o próximo pregão.
    
    ### 🔬 O que faço por você:
    
    - **📊 Análise Estatística Completa:** Calculo taxa de acerto, fator de lucro, drawdown e expectativa matemática
    - **📈 Backtests Automatizados:** Testo estratégias de retorno à média com dados históricos reais
    - **🎯 Níveis de Preço Precisos:** Determino entradas, stops e alvos baseados em volatilidade estatística
    - **⚖️ Visão Equilibrada:** Apresento argumentos positivos E negativos para cada análise
    - **💡 Insights Acionáveis:** Traduzo complexidade matemática em decisões práticas
    
    ### 🚀 Como usar:
    
    1. **Selecione um ativo** da B3 no painel lateral
    2. **Configure o período** de análise histórica
    3. **Clique em "Executar Análise"** e aguarde os resultados
    4. **Revise os insights** e níveis de preço sugeridos
    5. **Baixe o relatório** completo para seus estudos
    
    ### 📋 Estrutura da Análise:
    
    ✅ **Resumo Quantitativo** - Métricas principais e volatilidade esperada  
    ✅ **Contexto Positivo** - Argumentos matemáticos para compra  
    ✅ **Contexto Negativo** - Sinais de cautela e risco  
    ✅ **Estratégias Acionáveis** - Níveis de preço e cenários prováveis  
    
    ---
    
    **💭 "Sou a ponte entre a complexidade matemática e sua tomada de decisão humana."**
    
    *Selecione um ativo no painel lateral para começar! 👈*
    """)

# Footer
st.markdown("---")
st.markdown("""
<div style='text-align: center; color: #666; font-size: 0.9em;'>
    🤖 <strong>QuantAlpha</strong> - Desenvolvido para traders que valorizam análise quantitativa rigorosa<br>
    📊 Baseado em dados históricos do Yahoo Finance | 🇧🇷 Especializado em B3/Bovespa
</div>
""", unsafe_allow_html=True)