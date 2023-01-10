from sys import platform, version

from PIL import ImageTk, Image

if version[0] == "3":
    from tkinter import Label, Button, Entry, messagebox, Canvas, StringVar
    from tkinter.ttk import Combobox
elif version[0] == "2":
    from Tkinter import (Label, Button, Entry, messagebox)
else:
    print("Wtf que porongas paso aqui?!")

from .lib_download import descargarUnUnicoVideo, calidades_video_posibles, chek_calidad
from .imagenes import Imagenes
from .error import UrlNotFound, UnknownError, ErrorDeConexion, NotExistsResolution
from .load_config import calcular_file, load_file

class Frame1:
    
    def __init__(self,                                              
            VentanaPadre,                                       # aqui se especifica la ventana que llamo a este frame
            InstanciaPadre,                                     # Clase root
            # parametro por defecto para la clase:
            grosor_borde=1,                                     # Grosor para el Frame por defecto
            color_fondo="white",                                # color de fondo por defecto de la venta
            tamano_ventana=[400, 250],                          # tamano de la ventana por defecto [x, y]
            tipo_cursor="tcross",                               # Cursor por defecto(cruz)
            tipo_borde="sunken",                                # tipo de borde por defecto
            load_json=True                                      # cargar la configuracion del .json
        ):
        
        if load_json:
            ruta = calcular_file(__file__, "config-GUI")
            print("[[ ",ruta)
            config_data = load_file(ruta)
            print(config_data)
            
            grosor_borde = config_data["grosor-borde"]
            color_fondo = config_data["color-background"]
            tamano_ventana = config_data["size"]
            tipo_cursor = config_data["tipo-cursor"]
            tipo_borde = config_data["tipo-borde"]
        
        self.VentanaPadre = VentanaPadre
        self.Frame = Canvas(self.VentanaPadre) # Creamos un frame1. Este es para la parte de descargar videos uno a uno
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
        #foto = self.imagenes.addImagenes(self.imagenes.backgroundIMG, self.Frame)
        self.Frame.create_image(0,0,image=self.imagenes.backgroundIMG, anchor="nw")
        
        # si se aumenta la ventana, redimensionar la imagen de fondo:
        self.Frame.bind('<Configure>',self.img_resize)
        """self.botonImagen = Button(
            self.VentanaPadre,
            image=self.imagen,
            command=self.click_imagen
        )"""
        
        foto = self.imagenes.addImagenes(self.imagenes.youtubePNG, self.Frame)
        foto.place(relx=0.1, rely=0.05)

        self.EqtiquetaInformacion1 = Label(self.Frame, text=self.InstanciaPadre.idiomas.info)
        self.EqtiquetaInformacion1.place(relx=0.5, rely=0.1,relwidth=0.45)
        
        # texto1 = StringVar()
        # texto1.set("") 3 Nos permite cambiar el texto a lo largo de la ejecucion del programa
        self.EqtiquetaInformacion1.config(
            bg="#aaaaaa",         # Color de fondo
            fg="black",         # Color de letras
            font=("Console", 10), # Tipo y tamano de letra
            padx=10, pady=10    # Margene
            #textvariable=texto1 # texto variable
        )  

        self.EqtiquetaInformacion2 = Label(self.Frame, text=self.InstanciaPadre.idiomas.url_video)
        self.EqtiquetaInformacion2.place(relx=0.1, rely=0.5)
        
        self.EqtiquetaInformacion3 = Label(self.Frame, text=self.InstanciaPadre.idiomas.dir_file)
        self.EqtiquetaInformacion3.place(relx=0.1, rely=0.6 )
        
        self.EqtiquetaInformacion4 = Label(self.Frame, text=self.InstanciaPadre.idiomas.calidad_video_text)
        self.EqtiquetaInformacion4.place(relx=0.1, rely=0.7)
        
        self.videos = Entry(self.Frame)
        self.videos.place(relx=0.6, rely=0.5)
        
        self.carpeta = Entry(self.Frame)
        self.carpeta.place(relx=0.6, rely=0.6)

        var = StringVar()
        self.comb = Combobox(self.Frame,textvariable=var,values=calidades_video_posibles)
        self.comb.set(calidades_video_posibles[int(len(calidades_video_posibles)/2)]) # usar la calidade de video intermedia
        self.comb.place(relx=0.6, rely=0.7, relwidth=0.2)
        self.comb.bind('<<ComboboxSelected>>', self._chek_calidad)

        self.boton = Button(self.Frame, text=self.InstanciaPadre.idiomas.download_text, command=self.downloadVideo, relief="groove")
        self.boton.place(relx=0.6, rely=0.8)
        
        
        

            

    def _chek_calidad(self, event):
        try:
            url = self.videos.get()
            try:
                chek_calidad(calidades_video_posibles[self.comb.current()], url)
            except NotExistsResolution as error:
                messagebox.showerror("Error", error.msg+error.calidad)
        except UrlNotFound as error:
            messagebox.showerror("Error", error.msg)
            
    def img_resize(self, event):
        global image, resized, image2
        image = Image.open(self.imagenes.nameBackground)
        
        # redimensionar la imagen:
        resized = image.resize((event.width, event.height), Image.ANTIALIAS)
        print(event.width, event.height)

        image2 = ImageTk.PhotoImage(resized)
        self.Frame.create_image(0, 0, image=image2, anchor='nw')
        
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
                    try:
                        descargarUnUnicoVideo(self.videos.get(), carpetaDescarga=carpeta,  messagebox=messagebox, res=calidades_video_posibles[self.comb.current()])
                    except ErrorDeConexion as error:
                        # No se puede conectar a internet
                        messagebox.showerror("Error", error.msg)
                except UnknownError as error:
                    # Ocurrio un error desconocido
                    messagebox.showerror("Error", error.msg)
            except UrlNotFound as error:
                # Esta url no existe o no se encuentra
                messagebox.showerror("Error", error.msg)
        except NotExistsResolution as error:
            # La resolucion seleccionada no se encuentra
            messagebox.showerror("Error", error.msg+error.calidad)

    
    """def click_imagen(self):
        messagebox.INFO("Este programa aun esta en desarollo.")"""