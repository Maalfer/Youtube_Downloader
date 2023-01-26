from sys import version, platform
from threading import Thread
from PIL import ImageTk, Image

if version[0] == "3":
    from tkinter import  Label, Entry, Button, messagebox, Canvas, StringVar
    from tkinter.ttk import Combobox
elif version[0] == "2":
    from Tkinter import ( Label, Button, Entry)
else:
    print("Wtf que porongas paso aqui?!")
    
from .load_config import calcular_file, load_file
from .lib_download import downloadArchivoMusica
from .imagenes import Imagenes
from .error import ErrorDeConexion, UnknownError, UrlNotFound
    
class Frame3:
    
    def __init__(self,
                VentanaPadre,                                       # aqui se especifica la ventana que llamo a este frame
                # parametro por defecto para la clase:
                InstanciaPadre,
                grosor_borde=1,                                     # Grosor para el Frame por defecto
                color_fondo="white",                                # color de fondo por defecto de la venta
                tamano_ventana=[400, 250],                          # tamaño de la ventana por defecto [x, y]
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
        self.Frame = Canvas(self.VentanaPadre) # Creamos un frame3. Este sera para descarga musica de una en una
        VentanaPadre.FrameActual = 3
        self.InstanciaPadre = InstanciaPadre
        
        self.imagenes = Imagenes() # hacemos una instancia a la clase imagenes
        #foto = self.imagenes.addImagenes(self.imagenes.backgroundIMG, self.Frame)
        self.Frame.create_image(0,0,image=self.imagenes.backgroundIMG, anchor="nw")
        
        # si se aumenta la ventana, redimensionar la imagen de fondo:
        self.Frame.bind('<Configure>',self.img_resize)
        
        self.Frame.config(
            width=tamano_ventana[0], 
            height=tamano_ventana[1], # Cambiar tamaño del Frame 
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
        
        foto = self.imagenes.addImagenes(self.imagenes.youtubePNG, self.Frame)
        foto.place(relx=0.1, rely=0.05)
        
        self.EqtiquetaInformacion1 = Label(self.Frame, text=self.InstanciaPadre.idiomas.info3)
        self.EqtiquetaInformacion1.place(relx=0.5, rely=0.1, relwidth=0.45)
        # texto1 = StringVar()
        # texto1.set("") 3 Nos permite cambiar el texto a lo largo de la ejecucion del programa
        self.EqtiquetaInformacion1.config(
            bg="#aaaaaa",         # Color de fondo
            fg="black",         # Color de letras
            font=("Console", 10), # Tipo y tamaño de letra
            padx=10, pady=10    # Margene
            #textvariable=texto1 # texto variable
        )  
        
        self.EqtiquetaInformacion2 = Label(self.Frame, text=self.InstanciaPadre.idiomas.url_playlist)
        self.EqtiquetaInformacion2.place(relx=0.1, rely=0.5)
        
        self.EqtiquetaInformacion3 = Label(self.Frame, text=self.InstanciaPadre.idiomas.dir_file_playlist)
        self.EqtiquetaInformacion3.place(relx=0.1, rely=0.6)
        
        
        self.videos = Entry(self.Frame)
        self.videos.place(relx=0.6, rely=0.5)
        
        self.carpeta = Entry(self.Frame)
        self.carpeta.place(relx=0.6, rely=0.65)

        self.boton = Button(self.Frame, text=self.InstanciaPadre.idiomas.download_text, command=self.downloadArchivoMusica, relief="groove")
        self.boton.place(relx=0.6, rely=0.83) 

    def CarpetaActual(self):
        if platform == "win32":
            return ".\\"
        elif platform == "linux" or platform == "linux2":
            return "./"

    def downloadArchivoMusica(self):
        carpeta = self.carpeta.get()
        if len(carpeta) == 0:
            carpeta = self.CarpetaActual()
        try: 
            try:
                try:
                    Thread(target=downloadArchivoMusica, args=(self.videos.get(), carpeta, messagebox), daemon=True).start()
                except UrlNotFound as error:
                    # Esta url no existe o no se encuentra
                    messagebox.showerror("Error", error.msg)
            except UnknownError as error:
                # Ocurrio un error desconocido
                messagebox.showerror("Error", error.msg)
        except ErrorDeConexion as error:
            # No se puede conectar a internet
            messagebox.showerror("Error", error.msg)
            
    def img_resize(self, event):
        global image, resized, image2
        image = Image.open(self.imagenes.nameBackground)
        
        # redimensionar la imagen:
        resized = image.resize((event.width, event.height), Image.ANTIALIAS)
        print(event.width, event.height)

        image2 = ImageTk.PhotoImage(resized)
        self.Frame.create_image(0, 0, image=image2, anchor='nw')
