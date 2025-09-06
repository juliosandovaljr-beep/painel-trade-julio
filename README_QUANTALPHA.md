# 🤖 QuantAlpha - Analista de Dados Quantitativos B3

[![Streamlit](https://img.shields.io/badge/Streamlit-FF4B4B?style=for-the-badge&logo=streamlit&logoColor=white)](https://streamlit.io/)
[![Python](https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white)](https://python.org/)
[![Yahoo Finance](https://img.shields.io/badge/Yahoo%20Finance-7B68EE?style=for-the-badge&logo=yahoo&logoColor=white)](https://finance.yahoo.com/)

## 📊 Visão Geral

**QuantAlpha** é um analista de dados quantitativos sênior especializado no mercado de ações brasileiro (B3/Bovespa). O sistema transforma dados históricos e resultados de backtests em insights acionáveis para traders, servindo como a ponte entre a complexidade matemática e a tomada de decisão humana.

## ✨ Características Principais

### 🧠 Personalidade QuantAlpha
- **Analítico e Preciso**: Análises baseadas em dados estatísticos, probabilidades e resultados matemáticos
- **Clareza Didática**: Traduz complexidade dos números em linguagem clara e objetiva
- **Contextualizador**: Conecta resultados quantitativos com cenários de mercado
- **Equilibrado**: Apresenta sempre argumentos positivos E negativos
- **Focado em Ação**: Preparação específica para o próximo pregão

### 📈 Funcionalidades Técnicas
- **Backtests Automatizados**: Estratégias de retorno à média com dados históricos
- **Métricas Quantitativas**: Taxa de acerto, fator de lucro, drawdown, expectativa matemática
- **Análise de Volatilidade**: Faixas de preço esperadas (1σ e 2σ)
- **Níveis Técnicos**: Suportes, resistências e médias móveis
- **Indicadores**: RSI, médias móveis, análise de tendência

## 🚀 Como Usar

### 1. Interface Web (Streamlit)
```bash
streamlit run app_quantalpha.py
```

### 2. Análise Programática
```python
from quantalpha import QuantAlpha

# Inicializar QuantAlpha
qa = QuantAlpha()

# Análise completa de um ativo
analysis = qa.analyze_asset('PETR4')

# Relatório formatado seguindo o prompt mestre
report = qa.get_quantalpha_prompt_response('PETR4')
print(report)
```

### 3. Demonstração Interativa
```bash
python demo_quantalpha.py
```

## 📋 Estrutura da Análise

Cada análise segue a estrutura definida no "Prompt Mestre":

### 1️⃣ **Resumo Quantitativo do Ativo**
- Métrica principal do backtest
- Volatilidade esperada (68% e 95% de probabilidade)
- Preço atual e contexto histórico

### 2️⃣ **Contexto Positivo (Argumentos para COMPRA)**
- Sinais matemáticos favoráveis
- Argumentos subjetivos baseados em dados
- Oportunidades estatísticas

### 3️⃣ **Contexto Negativo (Argumentos para CAUTELA/VENDA)**
- Sinais de risco elevado
- Drawdowns históricos
- Limitações da estratégia

### 4️⃣ **Soluções e Estratégias Acionáveis**
- Níveis de preço chave (entrada, stop, alvos)
- Cenário mais provável
- Condições de invalidação

## 🎯 Métricas Calculadas

| Métrica | Descrição |
|---------|-----------|
| **Taxa de Acerto** | Percentual de operações lucrativas |
| **Fator de Lucro** | Razão entre lucros totais e perdas totais |
| **Drawdown Máximo** | Maior perda consecutiva observada |
| **Expectativa Matemática** | Retorno esperado por operação |
| **Payoff Ratio** | Razão entre ganho médio e perda média |
| **RSI** | Índice de Força Relativa |
| **Volatilidade Anualizada** | Desvio padrão dos retornos |

## 📊 Exemplo de Saída

```
📊 ANÁLISE QUANTALPHA - PETR4
═══════════════════════════════

💰 Preço Atual: R$ 30.65
📈 Taxa de Acerto: 51.0%
🎯 Fator de Lucro: 0.96
⚠️ Drawdown Máximo: -26.6%

🎯 Faixas de Volatilidade:
   68% Prob (1σ): R$ 30.16 - R$ 31.13
   95% Prob (2σ): R$ 29.67 - R$ 31.62

🧠 CONCLUSÃO: 🔴 PERFIL DE RISCO ELEVADO
```

## 🛠️ Instalação

### Dependências
```bash
pip install -r requirements.txt
```

### Estrutura de Arquivos
```
painel-trade-julio/
├── quantalpha.py          # Classe principal QuantAlpha
├── app_quantalpha.py      # Interface Streamlit
├── sample_data.py         # Dados de amostra para teste
├── demo_quantalpha.py     # Script de demonstração
├── requirements.txt       # Dependências Python
└── README.md             # Esta documentação
```

## 🎨 Interface

### Tela Inicial
![QuantAlpha Interface](https://github.com/user-attachments/assets/2b545843-64bc-41e2-b6eb-bd669337c352)

### Análise Completa
![QuantAlpha Analysis](https://github.com/user-attachments/assets/d7a09213-6fc5-48ed-b305-97b29ac5d134)

## 🔧 Configurações

### Ativos Suportados
- Todos os ativos da B3 (sufixo .SA no Yahoo Finance)
- Lista pré-configurada com 30+ ativos populares
- Entrada personalizada para qualquer ticker

### Períodos de Análise
- **1y**: 1 ano de dados históricos
- **2y**: 2 anos (padrão)
- **5y**: 5 anos para análises de longo prazo

## 🚨 Fallback System

O sistema inclui dados de amostra realistas quando o Yahoo Finance não está disponível, garantindo funcionamento contínuo para demonstrações e testes.

## 📈 Casos de Uso

- **Day Traders**: Níveis de entrada e saída para o próximo pregão
- **Swing Traders**: Análise de médio prazo com suportes/resistências
- **Analistas Quantitativos**: Métricas estatísticas detalhadas
- **Educação Financeira**: Compreensão de análise quantitativa

## 🎯 Próximos Desenvolvimentos

- [ ] Integração com dados em tempo real
- [ ] Múltiplas estratégias de backtest
- [ ] Análise de correlação entre ativos
- [ ] Alertas automáticos por email/SMS
- [ ] API REST para integração externa

## 🤝 Contribuição

Este projeto implementa o "Prompt Mestre" para análise quantitativa do mercado brasileiro. Contribuições são bem-vindas para:

- Novas estratégias de backtest
- Métricas adicionais
- Melhorias na interface
- Otimizações de performance

## 📄 Licença

Desenvolvido para traders que valorizam análise quantitativa rigorosa.

---

**💭 "Sou a ponte entre a complexidade matemática e sua tomada de decisão humana."**

*QuantAlpha - Analista de Dados Quantitativos Sênior*