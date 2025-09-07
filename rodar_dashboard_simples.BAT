@echo off
echo ================================
echo  Painel Trade Julio - Dashboard
echo ================================
echo.
echo Verificando e instalando dependencias...
pip install -r requirements.txt
if %errorlevel% neq 0 (
    echo ERRO: Falha ao instalar dependencias!
    pause
    exit /b 1
)
echo.
echo Iniciando dashboard Streamlit...
echo.
echo IMPORTANTE: Acesse no seu navegador:
echo    http://localhost:8501
echo.
echo Para parar o dashboard, pressione Ctrl+C
echo.
streamlit run app_streamlit_dashboard.py --server.headless=false --server.port=8501
pause