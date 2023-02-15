#! /bin/sh

clear
sudo apt-get update -y && sudo apt-get upgrade -y
sudo apt-get install tree python3 python3-pip -y

echo "[*] Instalando dependencias: "
pip3 install -r requirements.txt

echo "[*] Generando ejecutable: "
pyinstaller --onefile -D -i imagenes/youtube.ico  Youtube_Downloader.py

ruta_instalacion="/opt/Youtube_Downloader"

sudo mv dist/Youtube_Downloader "${ruta_instalacion}"
cd "${ruta_instalacion}"

echo "" > Youtube_Downloader_exec.py
echo "from os import system\n" >> Youtube_Downloader_exec.py
echo "system('$(pwd)/Youtube_Downloader')" >> Youtube_Downloader_exec.py
rm -rf *.spec build dist

pyinstaller --onefile -D  Youtube_Downloader_exec.py
rm -rf *.spec build dist