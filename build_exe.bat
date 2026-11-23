@echo off
REM ===== PROJECT: ECLIPSE - EXE build script =====
REM Put this file in the same folder as main.py and double-click it.

python --version
if errorlevel 1 (
    set PY=py
) else (
    set PY=python
)

echo [1/2] Installing PyInstaller...
%PY% -m pip install --upgrade pyinstaller
if errorlevel 1 goto FAIL

echo [2/2] Building ECLIPSE.exe ...
%PY% -m PyInstaller --onefile --name ECLIPSE main.py
if errorlevel 1 goto FAIL

echo.
echo SUCCESS! Your game is here: dist\ECLIPSE.exe
goto END

:FAIL
echo.
echo BUILD FAILED. Check that Python is installed and that main.py is in this folder.

:END
pause
