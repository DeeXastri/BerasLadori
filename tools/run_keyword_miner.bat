@echo off
chcp 65001 >nul
echo ====================================================================
echo  Menjalankan Google Indonesia Deep Search Keyword Miner
echo ====================================================================
echo.
python "%~dp0google_keyword_miner.py"
echo.
echo ====================================================================
echo  Selesai! Buka folder 'data' untuk melihat hasil JSON dan Markdown.
echo ====================================================================
pause
