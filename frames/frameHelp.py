from sys import version

if version[0] == "3":
    from tkinter import Tk, Menu
elif version[0] == "2":
    from Tkinter import (Tk, Menu)
else:
    print("Wtf que porongas paso aqui?!")

class Frame5:
    
    def __init__(self,
                VentanaPadre,                                       # aqui se especifica la ventana que llamo a este frame
                # parametro por defecto para la clase:
                InstanciaPadre,
                color_fondo=15,                                     # color de fondo por defecto de la venta
                tamano_ventana=[400, 250],                          # tamaño de la ventana por defecto [x, y]
            ):
        
        
        self.Frame = Tk()
        self.Frame.resizable(False,False)  
        self.VentanaPadre = VentanaPadre
        self.InstanciaPadre = InstanciaPadre
        
        x = int((self.Frame.winfo_screenwidth()/2) - (tamano_ventana[0]/2)) # calculando la posicion de la ventana para que aparezca en la mitad de la pantalla
        y = int((self.Frame.winfo_screenheight()/2) - (tamano_ventana[1]/2))
        self.Frame.geometry('{}x{}+{}+{}'.format(tamano_ventana[0], tamano_ventana[1], x, y))  # Establecer un tamano a la ventana
        
        self.Frame.title("Ventana de ayuda") # titulo de la ventana
        self.Frame.config(bd=color_fondo) # Color de fondo
        
        
        self.menu_frame = Menu(self.Frame) # crear un menu donde poner pestanas
        self.Frame.config(menu=self.menu_frame) # agregarle el menu
        
        self.menu_frame.add_command(label="Salir", command=self.killThisWindows)
    
    
    def killThisWindows(self):
        self.Frame.destroy()