# 📈 Baixar Histórico Diário de 5 Anos - Ações B3

Este script permite baixar automaticamente os dados históricos **diários dos últimos 5 anos** para os seguintes ativos da B3:

- POMO4 (Marcopolo)
- BRFS3 (BRF)
- WEGE3 (WEG)
- MGLU3 (Magazine Luiza)

Os dados são obtidos via Yahoo Finance utilizando a biblioteca `yfinance`.

---

## ✅ Como usar

### 1. Instale a biblioteca `yfinance`:

```bash
pip install yfinance
```

### 2. Execute o script Python:

```bash
python baixar_diario_5anos_yfinance.py
```

### 3. O script vai gerar automaticamente:

- `POMO4_diario_5anos.csv`
- `BRFS3_diario_5anos.csv`
- `WEGE3_diario_5anos.csv`
- `MGLU3_diario_5anos.csv`

Cada arquivo contém as colunas: `Date, Open, High, Low, Close, Adj Close, Volume`

---

## ℹ️ Observações

- O Yahoo Finance não oferece dados **intraday históricos de longo prazo**.
- Esses arquivos são ideais para análises estatísticas, gráficos, dashboards e estudos de variação de preço e volume.

---

## ✨ Desenvolvido por

**Dr. Julio Sandoval**  
Projeto Painel de Análise Estatística de Ativos B3
