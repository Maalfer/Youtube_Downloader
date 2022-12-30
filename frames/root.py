from sys import platform, version

if version[0] == "3":
    from tkinter import messagebox, Tk, Menu, TclError
elif version[0] == "2":
    from Tkinter import (messagebox, Tk, Menu, TclError)
else:
    print("Wtf que porongas paso aqui?!")

# Cargamos los modulos donde se han configurado cada Frame:
from .frame1 import Frame1
from .frame2 import Frame2
from .frame3 import Frame3
from .frame4 import Frame4
from .frameHelp import Frame5
from .aboutThis import Frame6
from .frameHTTP import Frame7
class root:
    
    def __init__(self,                                              # parametro por defecto para la clase
                titulo_ventana = "programa para descargar videos",  # titulo por defecto de la ventana
                color_fondo    = 15,                                # color de fondo por defecto de la venta
                tamano_ventana = [550, 350]                         # tamano de la ventana por defecto [x, y]
            ):
    
    
        self.root = Tk() # instancia de ventana principal
        self.FrameActual = 1
        self.InstanciaRoot = self
        self.killAll = False # esto en True cierra todas las pestañas
        
        self.Frames = [ # instancias de los frames que contendra nuestra ventana raiz
            Frame1(self.root, self.InstanciaRoot),
        ]
        self.VentanasAbiertas = {   # Aqui se almacenan todas las ventanas que se han abierto
            0:  [
                self.root
            ], # usamos 0 para indicar cuales son las ventanas principales
            1: [
                
            ],
        } # 1 para ventanas no principales
        


        self.root.config(bd=15) # Color de fondo
        self.sizeWindows = tamano_ventana
        
        x = int((self.root.winfo_screenwidth()/2) - (tamano_ventana[0]/2)) # calculando la posicion de la ventana para que aparezca en la mitad de la pantalla
        y = int((self.root.winfo_screenheight()/2) - (tamano_ventana[1]/2))
        self.root.geometry('{}x{}+{}+{}'.format(tamano_ventana[0], tamano_ventana[1], x, y))  # Establecer un tamano a la ventana
        self.root.resizable(False, False) # no permitir que puedan redimensionar la ventana
        self.root.title(titulo_ventana) # titulo de la ventana
        
        self.menu_root = Menu(self.root) # crear un menu donde poner nuestras pestanas
        self.root.config(menu=self.menu_root) # agregarle el menu a la venta principal
        
        self.menuInformacion = Menu(self.menu_root, tearoff=4)
        self.menu_root.add_cascade( label="Para mas informacion",  menu=self.menuInformacion)
        self.menuInformacion.add_command(label="Informacion del autor", command=self.Sobre_mi)
        self.menuInformacion.add_command(label="Ayuda", command=self.setFrame5)
        self.menuInformacion.add_command(label="Sobre este software", command=self.setFrame6)

        self.menuHerramientas = Menu(self.menu_root, tearoff=2)
        self.menu_root.add_cascade(label="Herramientas-Extras", menu=self.menuHerramientas)
        self.menuHerramientas.add_command(label="Descargar un unico video",         command=self.setFrame1)
        self.menuHerramientas.add_command(label="Descargar una playlist de videos", command=self.setFrame2)
        self.menuHerramientas.add_command(label="Descargar un unico archivo .mp3",  command=self.setFrame3)
        self.menuHerramientas.add_command(label="Descargar una playlist de musica", command=self.setFrame4)
        self.menuHerramientas.add_command(label="Servidores HTTP", command=self.setFrame7)

        
        self.menu_root.add_command(label="Salir", command=self.killAllWindows)
    
    def killAllWindows(self):
        self.killAll = True
        self.killWindows()
        
    def killWindows(self):
        """
            Esta funcion mata todas las ventanas menos las principal
        """
        for ventanas in self.VentanasAbiertas.keys():
            # el diccionario de ventanas princiaples(1) y no principales(0)
            if self.killAll == False: # si la variable no fue activada
                print(self.VentanasAbiertas)        
            elif self.killAll == True: # si la variable estado killAll esta activada, matamos todas las ventanas
                for ventana in self.VentanasAbiertas[ventanas]: # obtenemos las instancias Tk()
                    try:
                        if str(type(ventana)) != "<class 'int'>":
                            ventana.destroy() # matamos cada ventana
                    except TclError:
                        print("Esta ventana ya fue destruida")
            print(ventanas)
            print(self.VentanasAbiertas[ventanas])
            
    
    # con esta funciones podremos indicarle al programa a que ventana queremos cambiar:
    def setFrame1(self): self.FrameActual = 1; self.hide() 
    def setFrame2(self): self.FrameActual = 2; self.hide()
    def setFrame3(self): self.FrameActual = 3; self.hide()
    def setFrame4(self): self.FrameActual = 4; self.hide()
    def setFrame5(self): self.FrameActual = 5; self.hide()
    def setFrame6(self): self.FrameActual = 6; self.hide()
    def setFrame7(self): self.FrameActual = 7; self.hide()
    
    # Esta funcion se encarga de cambiar de ventana dependiendo de lo que se haya indicado con los botones del menu
    def hide(self):
        # esconder los desmas frames
        if  self.FrameActual == 1:
            for frameAnterior in self.Frames:
                # eliminar todos los frames anteriores
                frameAnterior.Frame.destroy()
            # agregar el frame 1 y pasarle la clase root por si necesita acceder a sus valores
            self.Frames.append(Frame1(self.root, self.InstanciaRoot))
            
        elif self.FrameActual == 2:
            for frameAnterior in self.Frames:
                frameAnterior.Frame.destroy()
            self.Frames.append(Frame2(self.root, self.InstanciaRoot))
            
        elif self.FrameActual == 3:
            for frameAnterior in self.Frames:
                frameAnterior.Frame.destroy()
            self.Frames.append(Frame3(self.root, self.InstanciaRoot))
            
        elif self.FrameActual == 4:
            for frameAnterior in self.Frames:
                frameAnterior.Frame.destroy()
            self.Frames.append(Frame4(self.root, self.InstanciaRoot))
        
        elif self.FrameActual == 5:
            #for frameAnterior in self.Frames:
                #frameAnterior.Frame.destroy()
            #self.Frames.append(Frame5(self.root, self.InstanciaRoot))
            # añadimos el elemento al list contenido dentro del dict, 1 ventana no principal:
            self.VentanasAbiertas[1].append(Frame5(self.root, self.InstanciaRoot).Frame)
            
        elif self.FrameActual == 6:
            #for frameAnterior in self.Frames:
                #frameAnterior.Frame.destroy()
            #self.Frames.append(Frame6(self.root, self.InstanciaRoot))
            # añadimos el elemento al list contenido dentro del dict, 1 ventana no principal:
            self.VentanasAbiertas[1].append(Frame6(self.root, self.InstanciaRoot).Frame)
            
        elif self.FrameActual == 7:
            #for frameAnterior in self.Frames:
                #frameAnterior.Frame.destroy()
            #self.Frames.append(Frame7(self.root, self.InstanciaRoot))
            # añadimos el elemento al list contenido dentro del dict, 1 ventana no principal:
            self.VentanasAbiertas[1].append(Frame7(self.root, self.InstanciaRoot).Frame)
            
    def Sobre_mi(self):
        messagebox.showinfo("Sobre mi", "Enlace a mi perfil de GitHub:\nhttps://github.com/Maalfer")

            