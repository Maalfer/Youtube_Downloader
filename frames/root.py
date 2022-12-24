from tkinter import messagebox, Tk, Menu
from sys import platform

# Cargamos los modulos donde se han configurado cada Frame:
from frames.frame1 import Frame1
from frames.frame2 import Frame2
from frames.frame3 import Frame3
from frames.frame4 import Frame4

class root:
    
    def __init__(self,                                              # parametro por defecto para la clase
                titulo_ventana = "programa para descargar vídeos",  # titulo por defecto de la ventana
                color_fondo    = 15,                                # color de fondo por defecto de la venta
                tamano_ventana = [500, 350]                         # tamaño de la ventana por defecto [x, y]
            ):
        
        self.root = Tk() # instancia de ventana principal
        self.FrameActual = None
        self.InstanciaRoot = self
        
        self.Frames = [ # instancias de los frames que contendra nuestra ventana raiz
            Frame1(self.root, self.InstanciaRoot),
            Frame2(self.root, self.InstanciaRoot),
            Frame3(self.root, self.InstanciaRoot),
            Frame4(self.root, self.InstanciaRoot)
        ]
        
        self.root.config(bd=15) # Color de fondo
        self.root.geometry("{}x{}".format(tamano_ventana[0], tamano_ventana[1]))  # Establecer un tamaño a la ventana
        #self.root.resizable(False, False) # no permitir que puedan redimensionar la ventana
        self.root.title(titulo_ventana) # titulo de la ventana
        
        self.menu_root = Menu(self.root) # crear un menu donde poner nuestras pestañas
        self.root.config(menu=self.menu_root) # agregarle el menu a la venta principal
        
        self.menuInformacion = Menu(self.menu_root, tearoff=0)
        self.menu_root.add_cascade( label="Para más información",  menu=self.menuInformacion)
        self.menuInformacion.add_command(label="Información del autor", command=self.Sobre_mi)

        self.menu_root.add_command(label="Salir", command=self.root.destroy)

        self.menuHerramientas = Menu(self.menu_root, tearoff=0)
        self.menu_root.add_cascade(label="Herramientas-Extras", menu=self.menuHerramientas)
        self.menuHerramientas.add_command(label="Descargar un unico video",         command=self.Frames[0].setToFrame1)
        self.menuHerramientas.add_command(label="Descargar una playlist de videos", command=self.Frames[1].setToFrame2)
        self.menuHerramientas.add_command(label="Descargar un unico archivo .mp3",  command=self.Frames[2].setToFrame3)
        self.menuHerramientas.add_command(label="Descargar una playlist de musica", command=self.Frames[3].setToFrame4)
        
    def Sobre_mi(self):
        messagebox.showinfo("Sobre mí", "Enlace a mi perfil de GitHub:\nhttps://github.com/Maalfer")

            