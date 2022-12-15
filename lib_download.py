from pytube import YouTube, exceptions, Playlist
from pytube.cli import on_progress
from os import rename, path, remove, listdir

def downloadPlayList(url, carpeta):
    """
        Esta funcion permite descargar una PlayList en formato mp3.
        se le especifica como primer parametro la url de la playlist
        y como segundo, la ruta de la carpeta donde se guardara los archivos creados
    """
    def delFile(ruta, extension=".3gpp"):
        """
            Elimina los archivos de una extension especifica
        """
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


    except exceptions.RegexMatchError:
        print("[!] Usted no introducio ningun enlace o este no es valido :(")
        
        
def descargarUnUnicoVideo(enlace, carpetaDescarga=".", messagebox=None):
    """
        Esta funcion recibe un enlace en forma de string del video a descargar en maxima calida.
        Como segundo argumento recibe la carpeta donde se guardara el archivo descargado.
        Como tercer argumento, se espera recibir el modulo messagebox de tkinter para poder
        imprimir los mensajes informativos por ventanas emergentes. En el caso de no especificarle
        este modulo, por defecto se asigna el valo None, en cullo caso, la informacion se mostrata por 
        terminal
    """
    
    informacion = "" # una variable para mostrar informacion al usuario
    try:
        video = YouTube(enlace, on_progress_callback=on_progress)
        
        datos = video.streams
        datos = datos.get_highest_resolution()
        datos = round(datos.filesize/1000000)
        
        informacion = "Se va a descargar el video con nombre \"{}\" el cual pesa {} MB.".format(video.title, datos)
        if messagebox != None: messagebox.showinfo("Exito", informacion)
        else: print(informacion)

        descarga = video.streams.get_highest_resolution()
        descarga.download()
        
        informacion =  "El video fue descargado con exito en el directorio actual."
        if messagebox != None: messagebox.showinfo("Exito", informacion)
        else: print(informacion)
        return 0 # 0 si todo salio bien
        
    except exceptions.RegexMatchError:
        informacion =  "Usted no introducio ningun enlace o este no es valido :("
        if messagebox != None: messagebox.showerror("Error", informacion)
        else: print(informacion) 
        return -1 # -1 si ocurrio algun fallo en el proceso