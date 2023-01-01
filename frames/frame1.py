from sys import platform, version

if version[0] == "3":
    from tkinter import Frame, Label, Button, Entry, messagebox
elif version[0] == "2":
    from Tkinter import (Frame, Label, Button, Entry, messagebox)
else:
    print("Wtf que porongas paso aqui?!")

from .lib_download import descargarUnUnicoVideo
from .imagenes import Imagenes
from .error import UrlNotFound, UnknownError, ErrorDeConexion

class Frame1:
    
    def __init__(self,                                              
            VentanaPadre,                                       # aqui se especifica la ventana que llamo a este frame
            InstanciaPadre,                                     # Clase root
            # parametro por defecto para la clase:
            grosor_borde=1,                                     # Grosor para el Frame por defecto
            color_fondo="white",                                # color de fondo por defecto de la venta
            tamano_ventana=[400, 250],                          # tamano de la ventana por defecto [x, y]
            tipo_cursor="tcross",                               # Cursor por defecto(cruz)
            tipo_borde="sunken"                                 # tipo de borde por defecto
        ):
        
        self.VentanaPadre = VentanaPadre
        self.Frame = Frame(self.VentanaPadre) # Creamos un frame1. Este es para la parte de descargar videos uno a uno
        VentanaPadre.FrameActual = 1
        self.InstanciaPadre = InstanciaPadre
    
        self.Frame.config(
            width=tamano_ventana[0], 
            height=tamano_ventana[1], # Cambiar tamano del Frame 
            bg=color_fondo,           # Cambiando color de fondo
            bd=grosor_borde,          # Cambiando grosor del borde
            relief=tipo_borde,        # Cambiar el tipo de borde
            cursor=tipo_cursor        # Cambiar el cursor
        )
        
        self.Frame.pack(
            fill="both", 
            anchor="center", # centramos el frame
            expand=1, # permitimos expandir el Frame
            side="top",
        )
        
        self.imagenes = Imagenes() # hacemos una instancia a la clase imagenes
        """self.botonImagen = Button(
            self.VentanaPadre,
            image=self.imagen,
            command=self.click_imagen
        )"""
        
        foto = self.imagenes.addImagenes(self.imagenes.youtubePNG, self.Frame)
        foto.grid(row=0, column=0)

        self.EqtiquetaInformacion1 = Label(self.Frame, text="Programa creado en Python para \ndescargar videos de Youtube\n")
        self.EqtiquetaInformacion1.grid(row=0, column=1)
        # texto1 = StringVar()
        # texto1.set("") 3 Nos permite cambiar el texto a lo largo de la ejecucion del programa
        self.EqtiquetaInformacion1.config(
            bg="#aaaaaa",         # Color de fondo
            fg="black",         # Color de letras
            font=("Console", 10), # Tipo y tamano de letra
            padx=10, pady=10    # Margene
            #textvariable=texto1 # texto variable
        )  
        

        self.EqtiquetaInformacion2 = Label(self.Frame, text="Url del video -> ")
        self.EqtiquetaInformacion2.grid(row=1, column=0)
        self.videos = Entry(self.Frame)
        self.videos.grid(row=1, column=1)

        self.EqtiquetaInformacion3 = Label(self.Frame, text="Carpeta donde ingresar el archivo -> ")
        self.EqtiquetaInformacion3.grid(row=2, column=0)
        self.carpeta = Entry(self.Frame)
        self.carpeta.grid(row=2, column=1)

        self.boton = Button(self.Frame, text="Descargar :)", command=self.downloadVideo, relief="groove")
        self.boton.grid(row=3, column=1)
        
    def CarpetaActual(self):
        if platform == "Win32":
            return ".\\"
        elif platform == "linux" or platform == "linux2":
            return "./"
    def downloadVideo(self):
        carpeta = self.carpeta.get()
        if len(carpeta) == 0:
            carpeta = self.CarpetaActual()
            
        error = None
        try:
            try:
                try:
                    descargarUnUnicoVideo(self.videos.get(), carpetaDescarga=carpeta,  messagebox=messagebox)
                except ErrorDeConexion:
                    # No se puede conectar a internet
                    error = ErrorDeConexion(idioma=self.InstanciaPadre.idiomas)
            except UnknownError:
                # Ocurrio un error desconocido
                error = UnknownError(idioma=self.InstanciaPadre.idiomas)
        except UrlNotFound:
            # Esta url no existe o no se encuentra
            error = UrlNotFound(self.videos.get(), idioma=self.InstanciaPadre.idiomas)
            
        if error != None:
            # Si ocurrio algun error de algun tipo mostrar una ventana con la informacion:
            messagebox.showerror("Error", error.msg)
    
    """def click_imagen(self):
        messagebox.INFO("Este programa aun esta en desarollo.")"""