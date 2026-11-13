@echo off
title Origens - Criar administrador
cd /d "%~dp0"

if not exist "venv\Scripts\python.exe" (
    echo Execute INICIAR.bat pelo menos uma vez antes.
    pause
    exit /b
)

call venv\Scripts\activate.bat
python manage.py createsuperuser
pause
