@echo off
REM Script de instalación para Windows

echo.
echo ╔════════════════════════════════════════════════════════════╗
echo ║  Instalacion - Análisis Laboratorio Microbiología Veterinaria
echo ║  🧬 Laboratorio de Microbiología Veterinaria
echo ╚════════════════════════════════════════════════════════════╝
echo.

REM Verificar si Python está instalado
python --version >nul 2>&1
if errorlevel 1 (
    echo ❌ ERROR: Python no está instalado o no está en el PATH
    echo.
    echo Por favor, descarga Python desde: https://www.python.org/
    echo Asegúrate de marcar "Add Python to PATH" durante la instalación
    echo.
    pause
    exit /b 1
)

echo ✅ Python encontrado
echo.

REM Crear entorno virtual
echo 📦 Creando entorno virtual...
python -m venv venv

REM Activar entorno virtual
echo 🔄 Activando entorno virtual...
call venv\Scripts\activate.bat

REM Instalar dependencias
echo 📥 Instalando dependencias...
pip install -r requirements.txt

if errorlevel 1 (
    echo ❌ Error al instalar dependencias
    pause
    exit /b 1
)

echo.
echo ╔════════════════════════════════════════════════════════════╗
echo ║           ✅ INSTALACIÓN COMPLETADA
echo ╚════════════════════════════════════════════════════════════╝
echo.
echo Para ejecutar la aplicación, usa:
echo.
echo   streamlit run app.py
echo.
pause
