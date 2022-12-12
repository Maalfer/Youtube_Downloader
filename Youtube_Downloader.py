from pytube import YouTube, exceptions, Playlist
from pytube.cli import on_progress
from tkinter import *
from tkinter import messagebox
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


def accion():
    try:
        enlace = videos.get()
        video = YouTube(enlace, on_progress_callback=on_progress)
        datos = video.streams
        datos = datos.get_highest_resolution()
        datos = round(datos.filesize/1000000)
        messagebox.showinfo(
            "Exito", "Se va a descargar el video con nombre \"{}\" el cual pesa {} MB.".format(video.title, datos))

        descarga = video.streams.get_highest_resolution()
        descarga.download()
        messagebox.showinfo(
            "Exito", "El video fue descargado con exito en el directorio actual.")
    except exceptions.RegexMatchError:
        messagebox.showerror(
            "Error", "Usted no introducio ningun enlace o este no es valido :(")


if __name__ == "__main__":
    def popup():
        messagebox.showinfo(
            "Sobre mí", "Enlace a mi perfil de GitHub:\nhttps://github.com/Maalfer")

    root = Tk()
    root.config(bd=15)
    root.geometry("400x250")
    root.resizable(False, False)
    root.title("Script para descargar vídeos")

    imagen = PhotoImage(file="youtube.png")
    foto = Label(root, image=imagen, bd=0)
    foto.grid(row=0, column=0)

    menubar = Menu(root)
    root.config(menu=menubar)
    helpmenu = Menu(menubar, tearoff=0)

    menubar.add_cascade(label="Para más información", menu=helpmenu)
    helpmenu.add_command(label="Información del autor", command=popup)

    menubar.add_command(label="Salir", command=root.destroy)

    instrucciones = Label(
        root, text="Programa creado en Python para \ndescargar vídeos de Youtube\n")
    instrucciones.grid(row=0, column=1)

    videos = Entry(root)
    videos.grid(row=1, column=1)

    boton = Button(root, text="Descargar :)", command=accion, relief="groove")
    boton.grid(row=2, column=1)

    root.mainloop()
