# 📊 Quantico Analítico TESTE 3 - Painel de Trade

Este é o sistema de análise quantitativa para trading de ações da B3, desenvolvido pelo Dr. Julio Sandoval.

## 🚀 Como Executar

### 1️⃣ **Setup Inicial (Execute apenas uma vez)**
```
setup_inicial.BAT
```
Este comando irá:
- Instalar todas as dependências Python necessárias
- Tentar baixar dados históricos reais via Yahoo Finance
- Gerar dados simulados como backup para demonstração

### 2️⃣ **Executar o Dashboard**
```
rodar_dashboard_simples.BAT
```
Este comando irá:
- Verificar e instalar dependências (se necessário)
- Iniciar o dashboard Streamlit
- Abrir automaticamente no navegador em: http://localhost:8501

## 📁 Arquivos Importantes

- `rodar_dashboard_simples.BAT` - **ARQUIVO PRINCIPAL** para executar o dashboard
- `setup_inicial.BAT` - Setup inicial do sistema
- `app_streamlit_dashboard.py` - Aplicação principal do dashboard
- `baixar_diario_5anos_yfinance.py` - Script para baixar dados reais da B3
- `gerar_dados_simulados.py` - Gerador de dados simulados para testes
- `requirements.txt` - Lista de dependências Python

## 🔧 Solução de Problemas

### Problema: "pip não é reconhecido"
**Solução:** Instale Python do site oficial (python.org) e certifique-se que está no PATH

### Problema: "Erro ao instalar dependências"
**Solução:** Execute como administrador ou use:
```
python -m pip install -r requirements.txt
```

### Problema: "Porta 8501 já está em uso"
**Solução:** Feche outras instâncias do Streamlit ou reinicie o computador

### Problema: "Não consegue baixar dados"
**Solução:** O sistema usa dados simulados automaticamente se não conseguir baixar dados reais

## 📈 Funcionalidades do Dashboard

- 📊 Análise estatística de 4 ativos principais (POMO4, BRFS3, WEGE3, MGLU3)
- 📅 Filtragem por dia da semana
- ⛳ Análise de gaps (Alta, Baixa, Sem Gap)
- 💰 Rentabilidade média por tipo de gap
- 📦 Distribuição de variações por quartis
- 📈 Frequência de gaps por dia da semana
- 📤 Exportação de dados para CSV

## ✨ Desenvolvido por
**Dr. Julio Sandoval**  
Projeto Quantico Analítico TESTE 3