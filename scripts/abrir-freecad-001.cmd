@echo off
setlocal
set "EVS_ROOT=%~dp0..\.."
set "EVS_FREECAD=%EVS_ROOT%\tools\freecad-1.1.4-001\FreeCAD_1.1.4-Windows-x86_64-py311\FreeCAD.exe"
if not exist "%EVS_FREECAD%" (
  echo FreeCAD portatil nao encontrado em tools.
  exit /b 1
)
set "FREECAD_USER_HOME=%EVS_ROOT%\tools\freecad-profile-001"
set "FREECAD_USER_DATA=%FREECAD_USER_HOME%\data"
set "FREECAD_USER_TEMP=%FREECAD_USER_HOME%\temp"
if not exist "%FREECAD_USER_HOME%" mkdir "%FREECAD_USER_HOME%"
if not exist "%FREECAD_USER_DATA%" mkdir "%FREECAD_USER_DATA%"
if not exist "%FREECAD_USER_TEMP%" mkdir "%FREECAD_USER_TEMP%"
start "" "%EVS_FREECAD%" --user-cfg "%FREECAD_USER_HOME%\user.cfg" --system-cfg "%FREECAD_USER_HOME%\system.cfg"
endlocal
