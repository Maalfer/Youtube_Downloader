from tkinter import Frame, Label, PhotoImage, Button, Entry, messagebox
from sys import platform

from lib_download import descargarUnUnicoVideo

class Frame1:
    
    def __init__(self,                                              
            VentanaPadre,                                       # aqui se especifica la ventana que llamo a este frame
            InstanciaPadre,                                     # Clase root
            # parametro por defecto para la clase:
            grosor_borde=1,                                     # Grosor para el Frame por defecto
            color_fondo="white",                                # color de fondo por defecto de la venta
            tamano_ventana=[400, 250],                          # tamaño de la ventana por defecto [x, y]
            tipo_cursor="tcross",                               # Cursor por defecto(cruz)
            tipo_borde="sunken"                                 # tipo de borde por defecto
        ):
        
        self.Frame1 = Frame() # Creamos un frame1. Este es para la parte de descargar videos uno a uno
        self.VentanaPadre = VentanaPadre
        VentanaPadre.FrameActual = self.Frame1
        self.InstanciaPadre = InstanciaPadre
        self.InstanciaPadre.FrameActual = self.Frame1
        
        self.Frame1.config(
            width=tamano_ventana[0], 
            height=tamano_ventana[1], # Cambiar tamaño del Frame 
            bg=color_fondo,           # Cambiando color de fondo
            bd=grosor_borde,          # Cambiando grosor del borde
            relief=tipo_borde,        # Cambiar el tipo de borde
            cursor=tipo_cursor        # Cambiar el cursor
        )
        
        self.Frame1.pack(
            fill="both", 
            anchor="center", # centramos el frame
            expand=1, # permitimos expandir el Frame
            side="top",
        )
        
        self.imagen = PhotoImage(file="youtube.png") # agregar una imagen
        """self.botonImagen = Button(
            self.VentanaPadre,
            image=self.imagen,
            command=self.click_imagen
        )"""
        
        self.foto = Label(self.Frame1, image=self.imagen, bd=0)
        self.foto.grid(row=0, column=0)

        self.EqtiquetaInformacion1 = Label(self.Frame1, text="Programa creado en Python para \ndescargar vídeos de Youtube\n")
        self.EqtiquetaInformacion1.grid(row=0, column=1)
        # texto1 = StringVar()
        # texto1.set("") 3 Nos permite cambiar el texto a lo largo de la ejecucion del programa
        self.EqtiquetaInformacion1.config(
                        bg="#aaaaaa",         # Color de fondo
                        fg="black",         # Color de letras
                        font=("Console", 10), # Tipo y tamaño de letra
                        padx=10, pady=10    # Margene
                        #textvariable=texto1 # texto variable
                    )  
        

        self.EqtiquetaInformacion2 = Label(self.Frame1, text="Url del video -> ")
        self.EqtiquetaInformacion2.grid(row=1, column=0)
        self.videos = Entry(self.Frame1)
        self.videos.grid(row=1, column=1)

        self.EqtiquetaInformacion3 = Label(self.Frame1, text="Carpeta donde ingresar el archivo -> ")
        self.EqtiquetaInformacion3.grid(row=2, column=0)
        self.carpeta = Entry(self.Frame1)
        self.carpeta.grid(row=2, column=1)

        self.boton = Button(self.Frame1, text="Descargar :)", command=self.downloadVideo, relief="groove")
        self.boton.grid(row=3, column=1)
        
    def setToFrame1(self):
        self.InstanciaPadre.FrameActual.destroy()
        self.InstanciaPadre.Frames[0] = Frame1(self.InstanciaPadre, self.InstanciaPadre)
        self.InstanciaPadre.FrameActual = self.InstanciaPadre.Frames[0].Frame1
        self.__init__(self.VentanaPadre, self.InstanciaPadre)
    def CarpetaActual(self):
        if platform == "Win32":
            return ".\\"
        elif platform == "linux" or platform == "linux2":
            return "./"
    def downloadVideo(self):
        carpeta = self.carpeta.get()
        if len(carpeta) == 0:
            carpeta = self.CarpetaActual()
        descargarUnUnicoVideo(self.videos.get(), carpetaDescarga=carpeta,  messagebox=messagebox)
    
    """def click_imagen(self):
        messagebox.INFO("Este programa aun esta en desarollo.")"""