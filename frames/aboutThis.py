from sys import version

if version[0] == "3":
    from tkinter import Toplevel, Menu, PhotoImage, Label, Frame
elif version[0] == "2":
    from Tkinter import (Toplevel, Menu,PhotoImage, Label, Frame)
else:
    print("Wtf que porongas paso aqui?!")
    
from .imagenes import Imagenes

class Frame6:
    
    def __init__(self,
                VentanaPadre,                                       # aqui se especifica la ventana que llamo a este frame
                # parametro por defecto para la clase:
                InstanciaPadre,
                color_fondo=15,                                     # color de fondo por defecto de la venta
                tamano_ventana=[400, 250],                          # tamaño de la ventana por defecto [x, y]
            ):
        
        # creamos una ventana nueva:
        self.Frame = Toplevel()
        
        self.Frame.resizable(False,False)  
        self.VentanaPadre = VentanaPadre
        self.InstanciaPadre = InstanciaPadre
        
        self.Frame.title("Acerca de este software") # titulo de la ventana
        
        x = int((self.Frame.winfo_screenwidth()/2) - (tamano_ventana[0]/2)) # calculando la posicion de la ventana para que aparezca en la mitad de la pantalla
        y = int((self.Frame.winfo_screenheight()/2) - (tamano_ventana[1]/2))
        self.Frame.geometry('{}x{}+{}+{}'.format(tamano_ventana[0], tamano_ventana[1], x, y))  # Establecer un tamano a la ventana
        
        frame = Frame(self.Frame)
        frame.config(
            width=tamano_ventana[0], 
            height=tamano_ventana[1], # Cambiar tamano del Frame 
            bg="white",           # Cambiando color de fondo
            bd=1,          # Cambiando grosor del borde
            relief="sunken",        # Cambiar el tipo de borde
            cursor="tcross"         # Cambiar el cursor
        )
        
        frame.pack(
            fill="both", 
            anchor="center", # centramos el frame
            expand=1, # permitimos expandir el Frame
            side="top",
        )
        
        self.menu_frame = Menu(self.Frame) # crear un menu donde poner pestanas
        self.Frame.config(menu=self.menu_frame) # agregarle el menu
        self.menu_frame.add_command(label="Salir", command=self.killThisWindows)
        
        self.imagenes = Imagenes()
        foto = self.imagenes.addImagenes(self.imagenes.youtubePNG, frame)
        foto.grid()
        
    
    def killThisWindows(self):
        self.Frame.destroy()