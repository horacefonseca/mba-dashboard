@echo off
echo ========================================
echo   Market Basket Analysis Dashboard
echo   Local Testing Script
echo ========================================
echo.

echo Checking Python installation...
python --version
if %errorlevel% neq 0 (
    echo ERROR: Python is not installed or not in PATH
    echo Please install Python 3.8+ from python.org
    pause
    exit /b 1
)
echo.

echo Installing/Updating dependencies...
pip install -r requirements.txt
if %errorlevel% neq 0 (
    echo ERROR: Failed to install dependencies
    pause
    exit /b 1
)
echo.

echo Starting Streamlit app...
echo.
echo Dashboard will open in your browser at: http://localhost:8501
echo.
echo Press Ctrl+C to stop the server
echo ========================================
echo.

streamlit run app.py

pause
