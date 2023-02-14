@echo off

cls
color A

pip install -r requirements.txt

pyinstaller --onefile -i imagenes\youtube.ico  Youtube_Downloader.py
echo [*] Archivo .exe generado

move dist\Youtube_Downloader.exe .\Youtube_Downloader.exe
rmdir /s /q dist build
del Youtube_Downloader.spec

set ruta_instalacion=C:\Users\%username%

mkdir "%ruta_instalacion%\Youtube_Downloader"
echo "carpeta creada en %ruta_instalacion%"

xcopy /e * "%ruta_instalacion%\Youtube_Downloader"
icacls "%ruta_instalacion%\Youtube_Downloader" /grant Todos:(OI)(CI)F /T
cd "%ruta_instalacion%\Youtube_Downloader"


set dir=%cd%
set sof=Youtube_Downloader.exe
set name=Youtube_Downloader

echo Set objShell = WScript.CreateObject("WScript.Shell") >>%USERPROFILE%\Desktop\accsdirecto.vbs
echo ficheroAccesoDirecto = "%USERPROFILE%\Desktop\%name%.lnk" >>%USERPROFILE%\Desktop\accsdirecto.vbs
echo Set objAccesoDirecto = objShell.CreateShortcut(ficheroAccesoDirecto) >>%USERPROFILE%\Desktop\accsdirecto.vbs
echo objAccesoDirecto.TargetPath = "%dir%\%sof%" >>%USERPROFILE%\Desktop\accsdirecto.vbs
echo objAccesoDirecto.Arguments = "" >>%USERPROFILE%\Desktop\accsdirecto.vbs
echo objAccesoDirecto.IconLocation = "%cd%\imagenes\youtube.ico,0" >>%USERPROFILE%\Desktop\accsdirecto.vbs
echo objAccesoDirecto.Description = "%name%" >>%USERPROFILE%\Desktop\accsdirecto.vbs
echo objAccesoDirecto.HotKey = "ALT+CTRL+N" >>%USERPROFILE%\Desktop\accsdirecto.vbs
echo objAccesoDirecto.WindowStyle = "1" >>%USERPROFILE%\Desktop\accsdirecto.vbs
echo objAccesoDirecto.WorkingDirectory = "%dir%" >>%USERPROFILE%\Desktop\accsdirecto.vbs
echo objAccesoDirecto.Save >>%USERPROFILE%\Desktop\accsdirecto.vbs
attrib +h +s "%USERPROFILE%\Desktop\accsdirecto.vbs"

start /B /WAIT %USERPROFILE%\Desktop\accsdirecto.vbs

erase /Q /a h s "%USERPROFILE%\Desktop\accsdirecto.vbs"


echo presione una tecla para finalizar 
pause > nul
