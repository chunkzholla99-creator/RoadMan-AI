@echo off
cd /d "%~dp0"
C:\Users\pc\AppData\Local\Python\pythoncore-3.14-64\python.exe -m streamlit run app.py --server.headless=true --server.enableCORS=false --server.enableXsrfProtection=false --browser.gatherUsageStats=false
pause
