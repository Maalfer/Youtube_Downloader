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


def descargarUnUnicoVideo():
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

def popup():
    messagebox.showinfo("Sobre mí", "Enlace a mi perfil de GitHub:\nhttps://github.com/Maalfer")

if __name__ == "__main__":

    root = Tk() # instancia de ventana principal
    root.config(bd=15) # Color de fondo
    root.geometry("400x250")  # Establecer un tamaño a la ventana
    #root.resizable(False, False) # no permitir que puedan redimensionar la ventana
    root.title("programa para descargar vídeos") # titulo de la ventana

    
    menubar = Menu(root) # crear un menu
    root.config(menu=menubar) # agregarle
    
    helpmenu = Menu(menubar, tearoff=0)
    menubar.add_cascade(label="Para más información", menu=helpmenu)
    helpmenu.add_command(label="Información del autor", command=popup)

    menubar.add_command(label="Salir", command=root.destroy)
    
    menuHerramientas = Menu(menubar, tearoff=0)
    menubar.add_cascade(label="Herramientas-Extras", menu=menuHerramientas)
    menuHerramientas.add_command(label="Descargar un unico video", command=descargarUnUnicoVideo)
    menuHerramientas.add_command(label="Descargar una playlist de videos", command=descargarUnUnicoVideo)
    menuHerramientas.add_command(label="Descargar un unico archivo .mp3", command=descargarUnUnicoVideo)
    menuHerramientas.add_command(label="Descargar una playlist de musica", command=descargarUnUnicoVideo)
    

    Frame1 = Frame() # Creamos un frame1. Este es para la parte de descargar videos uno a uno
    Frame1.config(
            width="300", height="200", # Cambiar tamaño del Frame 
            bg="white",  # Cambiando color de fondo
            bd=1,  # Cambiando grosor del borde
            relief="sunken", # Cambiar el tipo de borde
            cursor="tcross" # Cambiar el cursor
        )
    Frame2 = Frame() # Creamos un frame2. este para la parte de descargar varios videos de una playlist
    Frame2.config(
            width="300", height="200", # Cambiar tamaño del Frame 
            bg="white",  # Cambiando color de fondo
            bd=1,  # Cambiando grosor del borde
            relief="sunken", # Cambiar el tipo de borde
            cursor="tcross" # Cambiar el cursor
        )
    Frame3 = Frame() # Creamos un frame3. Este sera para descarga musica de una en una
    Frame3.config(
            width="300", height="200", # Cambiar tamaño del Frame 
            bg="white",  # Cambiando color de fondo
            bd=1,  # Cambiando grosor del borde
            relief="sunken", # Cambiar el tipo de borde
            cursor="tcross" # Cambiar el cursor
        )
    Frame4 = Frame() # Creamos un frame4. Este sera para descargar musica de una playlist
    Frame4.config(
            width="300", height="200", # Cambiar tamaño del Frame 
            bg="white",  # Cambiando color de fondo
            bd=1,  # Cambiando grosor del borde
            relief="sunken", # Cambiar el tipo de borde
            cursor="tcross" # Cambiar el cursor
        )

    imagen = PhotoImage(file="youtube.png") # agregar una imagen
    foto = Label(Frame1, image=imagen, bd=0)
    foto.grid(row=0, column=0)



    instrucciones = Label(Frame1, text="Programa creado en Python para \ndescargar vídeos de Youtube\n")
    instrucciones.grid(row=0, column=1)
    # texto1 = StringVar()
    # texto1.set("") 3 Nos permite cambiar el texto a lo largo de la ejecucion del programa
    instrucciones.config(
                    bg="#aaaaaa",         # Color de fondo
                    fg="black",         # Color de letras
                    font=("Console", 10), # Tipo y tamaño de letra
                    padx=10, pady=10    # Margene
                    #textvariable=texto1 # texto variable
                )  
    
    
    videos = Entry(Frame1)
    videos.grid(row=1, column=1)

    boton = Button(Frame1, text="Descargar :)", command=descargarUnUnicoVideo, relief="groove")
    boton.grid(row=2, column=1)

    f2 = Frame(width=100, height=100, background="blue")


    Frame1.pack(
                    fill="both", 
                    anchor="center", # centramos el frame
                    expand=1, # permitimos expandir el Frame
                    side="top",
                )
    # Empacar el Frame ajusta todos sus elementos a la ventana raiz
    

    root.mainloop()
