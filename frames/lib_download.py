from pytube import YouTube, exceptions, Playlist
from pytube.cli import on_progress
from os import rename, path, remove, listdir
from .error import *

def GetSize(stream):
    """_summary_

        Devuelve el tamño de un archivo de video o musica en Mb

    Args:
        stream (strean): se recibe un objeto de tipo stream para calcular el tamaño

    Returns:
        int: se retorna el tamaño del archivo en Mb
    """
    return stream.filesize_approx/1024/1024



def delFile(ruta, extension=".3gpp"):
    """_summary_
        
        Elimina los archivos de una extension especifica
            
    Args:
        ruta (str): ruta donde realizar la operacion
        extension (str, optional): _description_. Defaults to ".3gpp".
    """

    # obtenemos todos los archivos de la ruta especificada
    try:
        archivos = listdir(ruta)
        for archivo in archivos:
            if archivo.endswith(extension) == True and path.isfile(ruta+archivo) == True:
                # si es un archivo con la extension deseada eliminamos el archivo
                remove(ruta+archivo)
                print("[!] Archivo inecesario eliminado -> {}".format(ruta+archivo))
    except FileNotFoundError:
        pass
                


def GetInfo(YouTube):
    """_summary_
    
        Permite obtener informacion acerca de un objeto de tipo
        <pytube.__main__.YouTube object: videoId=ewfwrEideFc>
    
    Args:
        YouTube (TouTube()): Se recibe un argumento que es una instancia de la clase YouTube()

    Returns:
        dict: retorna un valor de tipo diccionario con informacion hacerla de la url introducida
    """
    
    info = {
        
        # si tiene restricion de edad True:
        "retricion-edad":YouTube.age_restricted,
        
        # da informacion acerca de las distintas resoluciones:
        "resoluciones-posibles": YouTube.streams,
        
        # author del video o musica
        "author": YouTube.author,
        
        # titulo de la descarga
        "titulo": YouTube.title,
        
        # url del link
        "url":YouTube.watch_url,
    }
    
    return info

def PrintInfoStream(stream):
    """_summary_
    
        Obtenemos informacion hacerca de un stream(video o musica)
    
    Args:
        stream (stream): se recibe un objeto de tipo stream

    Returns:
        dict: Se retorna un diccionario con la informacion hacerla del stream
    """
    try:
        fps = stream.fps
    except AttributeError:
        fps = 0 # si es musica no tiene fps xd
    info = {
        
        "size-gb":stream.filesize_gb,
        "size-mb":stream.filesize_mb,
        "size-kb":stream.filesize_kb,
        "name-default":stream.default_filename,
        "codecs":stream.codecs,
        "codecs-audio":stream.audio_codec,
        "tipo":stream.type,
        "resolucion":stream.resolution,
        "fps":fps,
        
    }
    for key in info.keys():
        print("{} : {}". format(key, info[key]))
    return info

def PrintAllInfoStream(Streams):
    """_summary_
    
        imprimimos informacion hacerca de una lista de streams(video o musica)
    
    Args:
        Streams (list(streams)): Se recibe una lista con objetos de tipo StreamQuery() con informacion

    Returns:
        int: se retorna 0 si todo es correcto
    """
    for stream in Streams:
        print("--------------------------------")
        PrintInfoStream(stream)
    print("--------------------------------")
    return 0


def PrintInfo(info):
    """_summary_

        Imprimimos informacion hacerca de un diccionario con informacion
        del objeto de tipo YouTube

    Args:
        info (dict): diccionario con informacion
        
    Returns:
        int: retorna un valor 0 de todo correcto
    """
    for key in info.keys():
        if str(type(info[key])) == "<class 'pytube.query.StreamQuery'>":
            # si detectamos una lista de streams ejecutar esta
            PrintAllInfoStream(info[key])
        else:
            print("{} : {}". format(key, info[key]))
    return 0

def downloadPlayList(url, carpeta):
    """_summary_
    
        Esta funcion permite descargar una PlayList en formato mp3.
        se le especifica como primer parametro la url de la playlist
        y como segundo, la ruta de la carpeta donde se guardara los archivos creados
    
    Args:
        url (str): Url de la playlist de la que descargar musica
        carpeta (str): carpeta donde guardar todos los archivos

    Raises:
        UnknownError: Error desconocido
        UrlNotFound: No se encontro una url funcional
        
    Returns:
        int: retorna un valor 0 de todo correcto
    """
    delFile(carpeta)
    try:
        playlist = Playlist(url)
        print('Numero de videos en la playlist: %s' % len(playlist.video_urls))
        for video_url in playlist.video_urls:
            music = YouTube(video_url, on_progress_callback=on_progress)
            PrintInfo(GetInfo(music))
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
                    raise UnknownError()
            else:
                print("[!] Ya existe el archivo -> {}".format(carpeta+music.title + ".mp3"))
                
        delFile(carpeta)
        # retorna el valor 0 si todo es correcto
        return 0
    except exceptions.RegexMatchError:
        raise UrlNotFound(url)


def downloadArchivoMusica(url, carpeta):
    """_summary_
    
        Esta funcion permite descargar una cancion en formato mp3.
        se le especifica como primer parametro la url del video al que obtener el audio
        y como segundo, la ruta de la carpeta donde se guardara los archivos creados
    
    Args:
        url (str): url de donde descargar la musica
        carpeta (str): carpeta dibde guardar los archivos
    
    Returns:
        int: retorna un valor 0 de todo correcto
    """
    delFile(carpeta)
    try:
        music = YouTube(url, on_progress_callback=on_progress)
        PrintInfo(GetInfo(music))
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
                raise UnknownError()
        else:
            print("[!] Ya existe el archivo -> {}".format(carpeta+music.title + ".mp3"))
                
        delFile(carpeta)
        # retorna 0 si todo es correcto
        return 0
    except exceptions.RegexMatchError:
        raise UrlNotFound(url)
        

        
def descargarUnUnicoVideo(enlace, carpetaDescarga=".", messagebox=None):
    """_summary_
    
        Esta funcion recibe un enlace en forma de string del video a descargar en maxima calida.
        Como segundo argumento recibe la carpeta donde se guardara el archivo descargado.
        Como tercer argumento, se espera recibir el modulo messagebox de tkinter para poder
        imprimir los mensajes informativos por ventanas emergentes. En el caso de no especificarle
        este modulo, por defecto se asigna el valo None, en cullo caso, la informacion se mostrata por 
        terminal.
        
    Args:
        enlace (str): _description_
        carpetaDescarga (str, optional): _description_. Defaults to ".".
        messagebox (Tk, optional): _description_. Defaults to None.

    Raises:
        UrlNotFound: La url no se pudo encontrar

    Returns:
        int: se retorna un 0 si todo fue correcto
    """
    
    informacion = "" # una variable para mostrar informacion al usuario
    try:
        video = YouTube(enlace, on_progress_callback=on_progress)
        
        info = GetInfo(video)
        size = PrintInfoStream(info["resoluciones-posibles"].get_highest_resolution())
        PrintInfo(info)

        informacion = "Se va a descargar el video con nombre \"{}\" el cual pesa {} MB.".format(info["titulo"], size["size-mb"])
        if messagebox != None: messagebox.showinfo("Exito", informacion)
        else: print(informacion)

        descarga = video.streams.get_highest_resolution()
        descarga.download(carpetaDescarga)
        informacion =  "El video fue descargado con exito en el directorio actual."
        if messagebox != None: messagebox.showinfo("Exito", informacion)
        else: print(informacion)
        return 0 # 0 si todo salio bien
        
    except exceptions.RegexMatchError:
        raise UrlNotFound(enlace)

            
def descargarPlaylistVideo(url, carpeta="."):
    """_summary_
    
    Descarga videos de una playlist.

    Args:
        url (str): _description_
        carpeta (str): _description_

    Raises:
        UnknownError: Se muestra al ocurrir un error desconocido
        UrlNotFound: Se muestra cuando la url no se pudo encontrar o esta fuera de servicio
        
    Returns:
        int: se retorna un 0 si todo fue correcto
    """
    try:
        playlist = Playlist(url)
        print('Numero de videos en la playlist: %s' % len(playlist.video_urls))
        for video_url in playlist.video_urls:
            music = YouTube(video_url, on_progress_callback=on_progress)
            PrintInfo(GetInfo(music))
            if path.exists(carpeta+music.title + ".mp4") == False:  # si el archivo no existe descargarlo
                try:
                    music = music.streams.get_highest_resolution()
                    music.download(carpeta)
                    print("[+] Archivo descargado -> {}".format(carpeta+music.title + ".mp4"))
                except KeyError:
                    raise UnknownError()
            else:
                print("[!] Ya existe el archivo -> {}".format(carpeta+music.title + ".mp3"))
        # Todo salio correcto:            
        return 0
    except exceptions.RegexMatchError:
        raise UrlNotFound(url)
