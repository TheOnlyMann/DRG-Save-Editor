@echo off
setlocal enabledelayedexpansion
set "PYTHON_FILE=./src/main/python/main.py"
set "REQUIREMENTS_FILE=./requirements.txt"
cd /d "%~dp0"

echo Installing requirements...
call activate DRG_SaveEdit
pip install -r %REQUIREMENTS_FILE%

echo Running script...
python %PYTHON_FILE%