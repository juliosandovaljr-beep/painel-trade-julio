@echo off
echo ================================
echo  Setup Inicial - Painel Trade
echo ================================
echo.
echo Instalando dependencias Python...
pip install -r requirements.txt
if %errorlevel% neq 0 (
    echo ERRO: Falha ao instalar dependencias!
    pause
    exit /b 1
)
echo.
echo Tentando baixar dados historicos reais...
python baixar_diario_5anos_yfinance.py
echo.
echo Gerando dados simulados como backup...
python gerar_dados_simulados.py
echo.
echo ================================
echo  SETUP CONCLUIDO COM SUCESSO!
echo ================================
echo.
echo Agora execute 'rodar_dashboard_simples.BAT' para iniciar o dashboard
echo.
pause