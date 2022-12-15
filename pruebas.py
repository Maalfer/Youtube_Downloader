from pytube import YouTube, exceptions, Playlist
from pytube.cli import on_progress
from os import rename, path, remove, listdir


            
def downloadPlayList(url, carpeta):
    
    def delFile(ruta, extension=".3gpp"):
        # obtenemos todos los archivos de la ruta especificada
        archivos = listdir(ruta)
        for archivo in archivos:
            if archivo.endswith(extension) == True and path.isfile(ruta+archivo) == True:
                # si es un archivo con la extension deseada eliminamos el archivo
                remove(ruta+archivo)
                print("[!] Archivo inecesario eliminado -> {}".format(ruta+archivo))
    
    delFile(carpeta)
    try:
        playlist = Playlist(url)
        print('Numero de videos en la playlist: %s' % len(playlist.video_urls))
        for video_url in playlist.video_urls:
            music = YouTube(video_url, on_progress_callback=on_progress)
            print("Nombre del audio: ({})\nurl: ({})\n".format(
                music.title, video_url))
            if path.exists(carpeta+music.title + ".mp3") == False:  # si el archivo no existe descargarlo
                try:
                    music = music.streams.filter().first()
                    out_file = music.download(carpeta)
                    base, ext = path.splitext(out_file)
                    new_file = base + '.mp3'
                    try:
                        rename(out_file, new_file)
                    except FileExistsError: # si el archivo .mp3 ya existe
                        try:
                            remove(carpeta+music.title+".3gpp") # elimina el archivo .3gpp
                        except (FileNotFoundError, OSError):
                            pass # si no existe, ya fue eliminado anetiormente
                except KeyError:
                    print("[!] Ocurrio un error desconocido")
            else:
                print("[!] Ya existe el archivo -> {}".format(carpeta+music.title + ".mp3"))
                
        delFile(carpeta)

    except exceptions.RegexMatchError:
        print("[!] Usted no introducio ningun enlace o este no es valido :(")


downloadPlayList(
    "https://youtube.com/playlist?list=PLp5g4uTTQZoi5OXdspcjP2VVvLOxrGpns", ".\\DownloadsMusic\\")
