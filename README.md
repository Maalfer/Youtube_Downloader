# Programa para descargar vídeos de YouTube

----

Script creado en Python para descargar vídeos de YouTube en la máxima resolución, simplemente copiando y pegando el enlace del vídeo.

<p align="center">
  <img src="youtube.png" alt="youtube.png"/>
</p>

Tenemos disponible la versión .exe (la que viene comprimida en formato zip) y la versión .py para tener acceso al código del programa.

Los vídeos de YouTube se descargarán en el mismo directorio donde se encuentra ubicado el programa.

----

### Clonar con:
```batch
git clone https://github.com/Maalfer/Youtube_Downloader.git
```
y acceder a la carpeta con:
```batch
cd Youtube_Downloader
```
----

### Instalacion de librerias:

```batch
pip install -r requirements.txt
```

----

### Lectura del archivo README.md y LICENSE
- Para Windows:

```batch
type README.md | more
type LICENSE | more
```

- Para Linux:
```bash
cat README.md | more
cat LICENSE | more
```
----
### Ejecutar con:

```batch
python Youtube_Downloader.py
```

- En caso de que usted use Windows y no tenga `python` instalado:
```batch
start Youtube_Downloader.exe
```