@echo off
title Origens - Iniciar
cd /d "%~dp0"

echo ==============================================
echo         ORIGENS - PROTOTIPO DJANGO
echo ==============================================
echo.

where python >nul 2>nul
if errorlevel 1 (
    echo Python nao foi encontrado.
    echo Instale o Python e marque "Add Python to PATH".
    pause
    exit /b
)

if not exist "venv\Scripts\python.exe" (
    echo [1/4] Criando ambiente virtual...
    python -m venv venv
)

echo [2/4] Ativando ambiente virtual...
call venv\Scripts\activate.bat

echo [3/4] Instalando dependencias...
python -m pip install -r requirements.txt

echo [4/4] Preparando banco e dados demonstrativos...
python manage.py migrate

echo.
echo Site:  http://127.0.0.1:8000/
echo Admin: http://127.0.0.1:8000/admin/
echo.
echo Mantenha esta janela aberta enquanto estiver usando o sistema.
echo Para encerrar, pressione CTRL+C.
echo.
python manage.py runserver

pause
