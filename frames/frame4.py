from sys import version

if version[0] == "3":
    from tkinter import Frame
elif version[0] == "2":
    from Tkinter import Frame
else:
    print("Wtf que porongas paso aqui?!")

from .load_config import calcular_file, load_file

class Frame4:
    
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
        self.Frame = Frame(self.VentanaPadre) # Creamos un frame4. Este sera para descargar musica de una playlist
        VentanaPadre.FrameActual = 4
        self.InstanciaPadre = InstanciaPadre
        
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
