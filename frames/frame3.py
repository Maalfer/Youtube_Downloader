from sys import version

if version[0] == "3":
    from tkinter import Frame
elif version[0] == "2":
    from Tkinter import Frame
else:
    print("Wtf que porongas paso aqui?!")
    
class Frame3:
    
    def __init__(self,
                VentanaPadre,                                       # aqui se especifica la ventana que llamo a este frame
                # parametro por defecto para la clase:
                InstanciaPadre,
                grosor_borde=1,                                     # Grosor para el Frame por defecto
                color_fondo="white",                                # color de fondo por defecto de la venta
                tamano_ventana=[400, 250],                          # tamaño de la ventana por defecto [x, y]
                tipo_cursor="tcross",                               # Cursor por defecto(cruz)
                tipo_borde="sunken"                                 # tipo de borde por defecto
            ):
        
        
        self.Frame = Frame() # Creamos un frame3. Este sera para descarga musica de una en una
        self.VentanaPadre = VentanaPadre
        VentanaPadre.FrameActual = 3
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
