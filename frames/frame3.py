from sys import version

from PIL import ImageTk, Image

if version[0] == "3":
    from tkinter import Canvas
elif version[0] == "2":
    from Tkinter import Canvas
else:
    print("Wtf que porongas paso aqui?!")
    
from .load_config import calcular_file, load_file

from .imagenes import Imagenes

    
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
        
    def img_resize(self, event):
        global image, resized, image2
        image = Image.open(self.imagenes.nameBackground)
        
        # redimensionar la imagen:
        resized = image.resize((event.width, event.height), Image.ANTIALIAS)
        print(event.width, event.height)

        image2 = ImageTk.PhotoImage(resized)
        self.Frame.create_image(0, 0, image=image2, anchor='nw')