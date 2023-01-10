from pytube import YouTube, exceptions, Playlist
from pytube.cli import on_progress
from os import rename, path, remove, listdir
from socket import gethostbyaddr, gaierror

from .error import ErrorDeConexion, UnknownError, UrlNotFound, NotExistsResolution

calidades_video_posibles = [
    "144p", 
    "240p",
    "360p",
    "480p",
    "720p",  # HD
    "1080p", # HD
    "1440p", # 2K
    "2160p", # 4K
    "4320p"  # 8K
]

def GetSize(stream):
    """_summary_

        Devuelve el tamño de un archivo de video o musica en Mb

    Args:
        stream (strean): se recibe un objeto de tipo stream para calcular el tamaño

    Returns:
        int: se retorna el tamaño del archivo en Mb
    """
    return stream.filesize_approx/1024/1024

def ComprobarConectividadConInternet():
    try:
        info = gethostbyaddr("www.google.com")
        print(info)
    except gaierror:
        raise ErrorDeConexion()

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
                
def chek_calidad(calidad, url):
    
    calidades = get_calidades(url)
    if calidad not in calidades:
        raise NotExistsResolution(calidad, calidades)
    else: True

def get_calidades(url):
    try:
        streams = YouTube(url).streams
        calidades = []
        
        for stream in streams:
            temp = stream.resolution
            if temp == None:
                pass
            elif temp in calidades:
                pass
            else: 
                calidades.append(stream.resolution)
    except exceptions.RegexMatchError:
        raise UrlNotFound(url)
    
    return calidades

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
    print(stream)
    try:
        try:
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
        except KeyError:
                info = {
                
                "size-gb":0,
                "size-mb":0,
                "size-kb":0,
                "name-default":stream.default_filename,
                "codecs":stream.codecs,
                "codecs-audio":stream.audio_codec,
                "tipo":stream.type,
                "resolucion":stream.resolution,
                "fps":fps,
        
            }
    except AttributeError:
        pass
                
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

def downloadPlayList(url, carpeta, messagebox=None):
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
    
    ComprobarConectividadConInternet()
    delFile(carpeta)
    try:
        playlist = Playlist(url)
        informacion = 'Numero de videos en la playlist: %s' % len(playlist.video_urls)
        if messagebox == None: print(informacion)
        else: messagebox.showinfo("Exito", informacion)
        
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


def downloadArchivoMusica(url, carpeta, messagebox=None):
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
    ComprobarConectividadConInternet()
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
        

        
def descargarUnUnicoVideo(enlace, carpetaDescarga=".", messagebox=None, res=None):
    """_summary_
    
        Esta funcion recibe un enlace en forma de string del video a descargar en maxima calida.
        Como segundo argumento recibe la carpeta donde se guardara el archivo descargado.
        Como tercer argumento, se espera recibir el modulo messagebox de tkinter para poder
        imprimir los mensajes informativos por ventanas emergentes. En el caso de no especificarle
        este modulo, por defecto se asigna el valo None, en cullo caso, la informacion se mostrata por 
        terminal.
        
    Args:
        enlace (str): url de donde descargar el video
        carpetaDescarga (str, optional): carpeta donde guardar el archivo descargado. Defaults to ".".
        messagebox (Tk, optional): instancia padre. Defaults to None.
        res (str, optional): calidad de video a descargar, por defecto, la maxima

    Raises:
        UrlNotFound: La url no se pudo encontrar

    Returns:
        int: se retorna un 0 si todo fue correcto
    """
    ComprobarConectividadConInternet()
    informacion = "" # una variable para mostrar informacion al usuario
    try:
        video = YouTube(enlace, on_progress_callback=on_progress)
        
        info = GetInfo(video)
        if res == None: size = PrintInfoStream(info["resoluciones-posibles"].get_highest_resolution())
        else: 
            chek_calidad(res, enlace)
            size = PrintInfoStream(info["resoluciones-posibles"].filter(res=res).first())
        PrintInfo(info)

        informacion = "Se va a descargar el video con nombre \"{}\" el cual pesa {} MB.".format(info["titulo"], size["size-mb"])
        if messagebox != None: messagebox.showinfo("Exito", informacion)
        else: print(informacion)
        
        if res == None: descarga = video.streams.get_highest_resolution()
        else: 
            descarga = video.streams.filter(res=res).first()
        
        descarga.download(carpetaDescarga)
        informacion =  "El video fue descargado con exito en el directorio actual."
        if messagebox != None: messagebox.showinfo("Exito", informacion)
        else: print(informacion)
        return 0 # 0 si todo salio bien
        
    except exceptions.RegexMatchError:
        raise UrlNotFound(enlace)

            
def descargarPlaylistVideo(url, carpeta=".", res=None, messagebox=None):
    """_summary_
    
    Descarga videos de una playlist. Si se le especifica una calidad, intentara descargar todos los videos en esa calidad,
    en el caso de que no pueda ser ya que ese video no soporte esa calidad, se descargar con la mejor.

    Args:
        url (str): url de la playlist a usar
        carpeta (str): Ruta de la carpeta en la que guardar el archivo
        res (str, optional): Resolucion con la que descargar los videos, por defecto, la mejor calidad disponible

    Raises:
        UnknownError: Se muestra al ocurrir un error desconocido
        UrlNotFound: Se muestra cuando la url no se pudo encontrar o esta fuera de servicio
        
    Returns:
        int: se retorna un 0 si todo fue correcto
    """
    ComprobarConectividadConInternet()
    try:
        playlist = Playlist(url)
        print('Numero de videos en la playlist: %s' % len(playlist.video_urls))
        for video_url in playlist.video_urls:
            music = YouTube(video_url, on_progress_callback=on_progress)
            PrintInfo(GetInfo(music))
            if path.exists(carpeta+music.title + ".mp4") == False:  # si el archivo no existe descargarlo
                try:
                    try:
                        # si el video selecionado no tiene la calidad que se escogio disponible, se descarga con la mayor calidad
                        if res == None: music = music.streams.get_highest_resolution()
                        else: 
                            chek_calidad(res, url)
                            music.streams.filter(res=res).first()
                    except NotExistsResolution:
                        music = music.streams.get_highest_resolution()
                    music.download(carpeta)
                    informacion = "[+] Archivo descargado -> {}".format(carpeta+music.title + ".mp4")
                    if messagebox == None: print(informacion)
                    else: messagebox.showinfo("Exito", informacion)
                except KeyError:
                    raise UnknownError()
            else:
                informacion = "[!] Ya existe el archivo -> {}".format(carpeta+music.title + ".mp3")
                if messagebox == None: print(informacion)
                else: messagebox.showinfo("Exito", informacion)
        # Todo salio correcto:            
        return 0
    except exceptions.RegexMatchError:
        raise UrlNotFound(url)
