from tkinter import Frame, Label, Entry, Button, messagebox
from .lib_download import descargarPlaylistVideo

class Frame2:
    
    def __init__(self,
                VentanaPadre,                                       # aqui se especifica la ventana que llamo a este frame
                InstanciaPadre,
                # parametro por defecto para la clase:
                grosor_borde=1,                                     # Grosor para el Frame por defecto
                color_fondo="white",                                # color de fondo por defecto de la venta
                tamano_ventana=[400, 250],                          # tamaño de la ventana por defecto [x, y]
                tipo_cursor="tcross",                               # Cursor por defecto(cruz)
                tipo_borde="sunken"                                 # tipo de borde por defecto
            ):
        
        self.Frame2 = Frame() # Creamos un frame2. este para la parte de descargar varios videos de una playlist
        self.VentanaPadre = VentanaPadre
        VentanaPadre.FrameActual = self.Frame2
        self.InstanciaPadre = InstanciaPadre
        
        self.Frame2.config(
            width=tamano_ventana[0], 
            height=tamano_ventana[1], # Cambiar tamaño del Frame 
            bg=color_fondo,           # Cambiando color de fondo
            bd=grosor_borde,          # Cambiando grosor del borde
            relief=tipo_borde,        # Cambiar el tipo de borde
            cursor=tipo_cursor        # Cambiar el cursor
        )
        
        self.Frame2.pack(
            fill="both", 
            anchor="center", # centramos el frame
            expand=1, # permitimos expandir el Frame
            side="top",
        )

        """self.EqtiquetaInformacion1 = Label(self.Frame2, text="Programa creado en Python para \ndescargar vídeos de Youtube\n")
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
        
        self.videos = Entry(self.Frame2)
        self.videos.grid(row=1, column=1)

        self.boton = Button(self.Frame2, text="Descargar :)", command=self.downloadPlayListVideo, relief="groove")
        self.boton.grid(row=2, column=1)"""
        
    def setToFrame2(self):
        self.VentanaPadre.FrameActual.destroy()
        self.__init__(self.VentanaPadre, self.InstanciaPadre)
        

    def downloadPlayListVideo(self):
        descargarPlaylistVideo(self.videos.get(), messagebox=messagebox, Frame=self.Frame2)