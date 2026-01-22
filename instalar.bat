@echo off
echo ========================================
echo Fitness App Academy - Instalacao
echo ========================================
echo.

echo [1/3] Instalando dependencias...
pip install -r requirements.txt
if errorlevel 1 (
    echo ERRO: Falha ao instalar dependencias
    pause
    exit /b 1
)

echo.
echo [2/3] Corrigindo bcrypt...
pip uninstall bcrypt -y
pip install bcrypt==4.0.1

echo.
echo [3/3] Inicializando banco de dados...
python init_db.py
if errorlevel 1 (
    echo ERRO: Falha ao inicializar banco
    pause
    exit /b 1
)

echo.
echo ========================================
echo Instalacao concluida com sucesso!
echo ========================================
echo.
echo Para iniciar a API, execute:
echo   uvicorn main:app --reload
echo.
pause
