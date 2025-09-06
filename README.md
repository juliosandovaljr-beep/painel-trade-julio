# 📈 Painel de Análise Estatística - QuantAlpha

Este repositório contém um sistema completo de análise quantitativa para o mercado de ações brasileiro (B3/Bovespa), featuring o **QuantAlpha** - um analista de dados quantitativos sênior especializado.

## 🚀 Novidades - QuantAlpha

**🤖 QuantAlpha** é o novo sistema de análise quantitativa que transforma dados históricos e backtests em insights acionáveis para traders. Implementa o "Prompt Mestre" para análise rigorosa do mercado brasileiro.

### ✨ Características Principais:
- **📊 Análise Estatística Completa**: Taxa de acerto, fator de lucro, drawdown, expectativa matemática
- **📈 Backtests Automatizados**: Estratégias de retorno à média com dados históricos reais  
- **🎯 Níveis de Preço Precisos**: Entradas, stops e alvos baseados em volatilidade estatística
- **⚖️ Visão Equilibrada**: Argumentos positivos E negativos para cada análise
- **💡 Insights Acionáveis**: Complexidade matemática traduzida em decisões práticas

### 🎯 Como Usar:
```bash
# Interface web interativa
streamlit run app_quantalpha.py

# Demonstração completa
python demo_quantalpha.py

# Análise programática
from quantalpha import QuantAlpha
qa = QuantAlpha()
analysis = qa.get_quantalpha_prompt_response('PETR4')
```

## 📊 Sistema Original

### Baixar Histórico Diário de 5 Anos - Ações B3

Este script permite baixar automaticamente os dados históricos **diários dos últimos 5 anos** para os seguintes ativos da B3:

- POMO4 (Marcopolo)
- BRFS3 (BRF)
- WEGE3 (WEG)
- MGLU3 (Magazine Luiza)

Os dados são obtidos via Yahoo Finance utilizando a biblioteca `yfinance`.

---

## ✅ Como usar

### 1. Instale as dependências:

```bash
pip install -r requirements.txt
```

### 2. Execute o QuantAlpha (Recomendado):

```bash
streamlit run app_quantalpha.py
```

### 3. Ou execute o dashboard original:

```bash
streamlit run app_streamlit_dashboard.py
```

### 4. Para baixar dados históricos:

```bash
python baixar_diario_5anos_yfinance.py
```

## 📁 Estrutura do Projeto

```
painel-trade-julio/
├── quantalpha.py              # 🤖 Sistema QuantAlpha principal
├── app_quantalpha.py          # 🎯 Interface Streamlit do QuantAlpha  
├── sample_data.py             # 📊 Dados de amostra para demonstração
├── demo_quantalpha.py         # 🚀 Script de demonstração
├── README_QUANTALPHA.md       # 📖 Documentação detalhada do QuantAlpha
├── app_streamlit_dashboard.py # 📈 Dashboard original
├── baixar_diario_5anos_yfinance.py # 💾 Script de download de dados
├── requirements.txt           # 📦 Dependências
└── README.md                 # 📄 Este arquivo
```

## 🎨 Screenshots

### Interface QuantAlpha
![QuantAlpha Interface](https://github.com/user-attachments/assets/2b545843-64bc-41e2-b6eb-bd669337c352)

### Análise Completa
![QuantAlpha Analysis](https://github.com/user-attachments/assets/d7a09213-6fc5-48ed-b305-97b29ac5d134)

## ℹ️ Observações

- O Yahoo Finance não oferece dados **intraday históricos de longo prazo**.
- Os arquivos são ideais para análises estatísticas, gráficos, dashboards e estudos de variação de preço e volume.
- O QuantAlpha inclui sistema de fallback com dados de amostra para demonstrações.

---

## ✨ Desenvolvido por

**Dr. Julio Sandoval**  
Projeto Painel de Análise Estatística de Ativos B3

### 🚀 Powered by QuantAlpha
*Sua ponte entre a complexidade matemática e a tomada de decisão humana*
