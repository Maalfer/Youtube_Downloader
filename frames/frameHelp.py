from sys import version, platform

if version[0] == "3":
    from tkinter import Toplevel, Menu, Text, END, TOP, Message, GROOVE, Scrollbar, VERTICAL, Listbox, RIGHT, Y, messagebox
elif version[0] == "2":
    from Tkinter import (Toplevel, Menu, Text, END, TOP, Message, GROOVE, messagebox)
else:
    print("Wtf que porongas paso aqui?!")


from .helpText import Textos
from .error import UnknownOS

from .load_config import calcular_file, load_file

class Frame5:
    
    def __init__(self,
                VentanaPadre,                                       # aqui se especifica la ventana que llamo a este frame
                # parametro por defecto para la clase:
                InstanciaPadre,
                color_fondo=15,                                     # color de fondo por defecto de la venta
                tamano_ventana=[400, 250],                          # tamaño de la ventana por defecto [x, y]
                load_json=True                                      # cargar la configuracion del .json
        ):
        
        if load_json:
            ruta = calcular_file(__file__, "config-GUI")
            print("[[ ",ruta)
            config_data = load_file(ruta)
            print(config_data)
            
            color_fondo = config_data["color-background"]
            tamano_ventana = config_data["size"]
            
        
        self.VentanaPadre = VentanaPadre
        self.InstanciaPadre = InstanciaPadre
        self.Frame = Toplevel()
        self.color_fondo = color_fondo
        self.Frame.resizable(config_data["resizable"][0], config_data["resizable"][1])  
        
        try:
            self.TextHelp = Textos(self.InstanciaPadre.idiomas)
        except UnknownOS:
            error = UnknownOS(platform)
            messagebox.showerror("Error", error.msg)
            self.InstanciaPadre.killAllWindows()
        
        x = int((self.Frame.winfo_screenwidth()/2) - (tamano_ventana[0]/2)) # calculando la posicion de la ventana para que aparezca en la mitad de la pantalla
        y = int((self.Frame.winfo_screenheight()/2) - (tamano_ventana[1]/2))
        self.Frame.geometry('{}x{}+{}+{}'.format(tamano_ventana[0], tamano_ventana[1], x, y))  # Establecer un tamano a la ventana
        
        self.Frame.title("Ventana de ayuda. Idioma:{}".format(self.InstanciaPadre.idiomas.idioma)) # titulo de la ventana
        self.Frame.config(bd=self.color_fondo) # Color de fondo
        
        self.menu_frame = Menu(self.Frame) # crear un menu donde poner pestanas
        self.Frame.config(menu=self.menu_frame) # agregarle el menu
        
        self.menu_frame.add_command(label="Salir", command=self.killThisWindows)
    
        # crear una barra de desplazamiento:
        barraDesplazamiento = Scrollbar(self.Frame)
        barraDesplazamiento.pack(side = RIGHT, fill = Y )
        
        # Creacion de un cuadro de texto:
        self.cuadroConInfo = Text(self.Frame, width=40, height=10, yscrollcommand=barraDesplazamiento.set)
        
        # Configurar la barra de desplzamiento:
        barraDesplazamiento.config( command = self.cuadroConInfo.yview )
        
        # Eliminar todo el contenido anterior del cuadro de texto:
        self.cuadroConInfo.delete("1.0", END)
        
        self.cuadroConInfo.insert("1.0", self.TextHelp.text)
        self.cuadroConInfo.pack(side=TOP)
    
    
        """msg1 = Message(self.Frame,text='' '' '',relief=GROOVE)
        msg1.place(width=40, height=10)
        msg1.pack(side=TOP)"""
    
    def killThisWindows(self):
        self.Frame.destroy()