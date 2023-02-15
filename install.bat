@echo off           // Desactiva la visualización del comando que se está ejecutando en la consola.
cls                 // Limpia la consola.
color A             // Cambia el color de la consola a verde claro.

// Instala los paquetes listados en el archivo de requisitos.
pip install -r requirements.txt  

// Empaqueta el script en un archivo ejecutable y define el icono para el archivo. 
pyinstaller --onefile -i imagenes\youtube.ico  Youtube_Downloader.py  
echo [*] Archivo .exe generado  

// Mueve el archivo ejecutable generado al directorio actual.
move dist\Youtube_Downloader.exe .\Youtube_Downloader.exe  

// Elimina los directorios de construcción del proyecto.
rmdir /s /q dist build     

// Elimina el archivo de autogenerado de configuración del script.
del Youtube_Downloader.spec   

// Establece la variable ruta_instalacion con la ruta del directorio de instalación.
set ruta_instalacion=C:\Users\%username%   

// Crea un nuevo directorio para el script en la ruta de instalación definida.
mkdir "%ruta_instalacion%\Youtube_Downloader" 

// Muestra un mensaje indicando que se ha creado la carpeta en la ruta de instalación. 
echo "carpeta creada en %ruta_instalacion%"   

// Copia todos los archivos en el directorio actual al directorio de instalación.
xcopy /e * "%ruta_instalacion%\Youtube_Downloader"  

// Establece permisos para todos los usuarios en la carpeta de instalación.
icacls "%ruta_instalacion%\Youtube_Downloader" /grant Todos:(OI)(CI)F /T  

// Se mueve al directorio de instalación del script.
cd "%ruta_instalacion%\Youtube_Downloader"   

set dir=%cd%                     // Establece la variable dir con el directorio actual.
set sof=Youtube_Downloader.exe   // Establece la variable sof con el nombre del archivo ejecutable.
set name=Youtube_Downloader      // Establece la variable name con el nombre del script.

// Verifica si la carpeta Escritorio existe en la ruta del usuario actual.
if not exist %USERPROFILE%\Desktop\ (     
    set shortcut_folder=Escritorio   // Si la carpeta no existe, establece shortcut_folder como Escritorio.
) else (                             // Si la carpeta existe,
    set shortcut_folder=Desktop      // establece shortcut_folder como Desktop.
)

// Crea un objeto de shell para crear el acceso directo y lo redirige a un archivo .vbs en la carpeta de acceso directo.
echo Set objShell = WScript.CreateObject("WScript.Shell") >>%USERPROFILE%%shortcut_folder%\accsdirecto.vbs    

// Define la ubicación del archivo de acceso directo en la carpeta seleccionada.
echo ficheroAccesoDirecto = "%USERPROFILE%%shortcut_folder%%name%.lnk" >>%USERPROFILE%%shortcut_folder%\accsdirecto.vbs 

// Crea un objeto de acceso directo utilizando la ubicación definida.
echo Set objAccesoDirecto = objShell.CreateShortcut(ficheroAccesoDirecto) >>%USERPROFILE%%shortcut_folder%\accsdirecto.vbs 

// Define la ruta del archivo ejecutable para el acceso directo.
echo objAccesoDirecto.TargetPath = "%dir%%sof%" >>%USERPROFILE%%shortcut_folder%\accsdirecto.vbs 

// Define la ruta del archivo ejecutable para el acceso directo.
echo objAccesoDirecto.Arguments = "" >>%USERPROFILE%%shortcut_folder%\accsdirecto.vbs

// Define la ruta del archivo ejecutable para el acceso directo.
echo objAccesoDirecto.IconLocation = "%cd%\imagenes\youtube.ico,0" >>%USERPROFILE%%shortcut_folder%\accsdirecto.vbs

// Define la ruta del archivo ejecutable para el acceso directo.
echo objAccesoDirecto.Description = "%name%" >>%USERPROFILE%%shortcut_folder%\accsdirecto.vbs

// Define la ruta del archivo ejecutable para el acceso directo.
echo objAccesoDirecto.HotKey = "ALT+CTRL+N" >>%USERPROFILE%%shortcut_folder%\accsdirecto.vbs

// Define el estilo de ventana para el acceso directo.
echo objAccesoDirecto.WindowStyle = "1" >>%USERPROFILE%%shortcut_folder%\accsdirecto.vbs

// Define el estilo de ventana para el acceso directo.
echo objAccesoDirecto.WorkingDirectory = "%dir%" >>%USERPROFILE%%shortcut_folder%\accsdirecto.vbs

// Guarda el archivo de acceso directo.
echo objAccesoDirecto.Save >>%USERPROFILE%%shortcut_folder%\accsdirecto.vbs

// Oculta y establece los atributos de sistema para el archivo de acceso directo.
attrib +h +s "%USERPROFILE%%shortcut_folder%\accsdirecto.vbs"

// Inicia el archivo de acceso directo en segundo plano y espera a que termine.
start /B /WAIT %USERPROFILE%%shortcut_folder%\accsdirecto.vbs

// Inicia el archivo de acceso directo en segundo plano y espera a que termine.
erase /Q /a h s "%USERPROFILE%%shortcut_folder%\accsdirecto.vbs"

echo presione una tecla para finalizar 
pause > nul
