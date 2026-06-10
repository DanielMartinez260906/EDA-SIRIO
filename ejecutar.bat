@echo off
REM Script para ejecutar la aplicación

echo.
echo ╔════════════════════════════════════════════════════════════╗
echo ║  Iniciando Análisis Laboratorio Microbiología Veterinaria
echo ║  🧬 Laboratorio de Microbiología Veterinaria
echo ╚════════════════════════════════════════════════════════════╝
echo.

REM Verificar si el entorno virtual existe
if not exist "venv\Scripts\activate.bat" (
    echo ❌ ERROR: El entorno virtual no existe
    echo.
    echo Por favor, ejecuta primero: instalar.bat
    echo.
    pause
    exit /b 1
)

REM Activar entorno virtual
call venv\Scripts\activate.bat

REM Ejecutar la aplicación
echo 🚀 Lanzando la aplicación...
echo.
echo La aplicación se abrirá en tu navegador en: http://localhost:8501
echo.
echo Para detener la aplicación, presiona Ctrl+C
echo.

streamlit run app.py

pause
