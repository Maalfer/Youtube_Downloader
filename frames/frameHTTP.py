from sys import version
from os import chdir, getcwd
from os.path import exists, isfile

if version[0] == "3":
    from tkinter import Tk, Menu, Entry, Label, Frame, Button, messagebox
elif version[0] == "2":
    from Tkinter import (Tk, Menu, Entry, Label, Frame, Button, messagebox)
else:
    print("Wtf que porongas paso aqui?!")
    
from .serverHTTP import serverHTTP
from .error import PortError, HostError, DirErrorNotFoundOrNotExists, ThisNotDir

class Frame7:
    
    def __init__(self,
                VentanaPadre,                                       # aqui se especifica la ventana que llamo a este frame
                # parametro por defecto para la clase:
                InstanciaPadre,
                color_fondo=15,                                     # color de fondo por defecto de la venta
                tamano_ventana=[400, 250],                          # tamaño de la ventana por defecto [x, y]
            ):
        
        
        self.Frame = Tk()
        self.error = 0 # se usa para indicar si hubo un error, 0 es todo correcto
        self.Frame.resizable(False,False)  
        self.VentanaPadre = VentanaPadre
        self.InstanciaPadre = InstanciaPadre
        self.serviciosHTTP = [] # instancias de servidores HTTP
        #self.ruta_actual = getcwd()
        self.Frame.title("Servicios HTTP") # titulo de la ventana
        
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
        self.menu_frame.add_command(label="Instancias Anteriores", command=self.killThisWindows)
        
        self.EqtiquetaInformacion1 = Label(frame, text="Host del servicio ")
        self.EqtiquetaInformacion1.grid(row=1, column=0)
        self.host = Entry(frame)
        self.host.grid(row=1, column=1)
        
        self.EqtiquetaInformacion2 = Label(frame, text="Puerto del servicio")
        self.EqtiquetaInformacion2.grid(row=2, column=0)
        self.port = Entry(frame)
        self.port.grid(row=2, column=1)    
    
        self.EqtiquetaInformacion3 = Label(frame, text="Directorio donde iniciar el servicio ")
        self.EqtiquetaInformacion3.grid(row=3, column=0)
        self.dir = Entry(frame)
        self.dir.grid(row=3, column=1)   
            
        self.boton = Button(frame, text="Iniciar", command=self.initService, relief="groove")
        self.boton.grid(row=4, column=1)

    def initService(self):
        
        try:
            try:
                _port = int(self.port.get())
                error = PortError(_port)
                # convertimos el string a un int
                
                if _port > 2**16:
                    # si el puerto es mayor que 65536 levantamos una excepcion
                    raise PortError(_port)
            except ValueError:
                messagebox.showerror("Error", "Usted introdujo un valor que no es un numero entero")
        except PortError:
            # si el puerto no se encuentra dentro del rango, causamos una excepcion
            messagebox.showerror("Error", error.msg)
            self.error = 1
            return self.error
            
        
        _host = self.host.get()
        try:
            if len(_host.split(".")) != 4 and _host != "localhost":
                # comprobamos que la direcion IP de host tenga 4 numeros decimales, o sea "localhost"
                error = HostError(_host)
                raise HostError(_host)
        except HostError:
            # si no sacamos un mensaje de error
            messagebox.showerror("Error", error.msg)
            self.error = 2
            return self.error
        
        try:
            _dir = self.dir.get()
            if len(_dir) == 0 or len(_dir.split(" ")) == 0:
                # si no se introdujo ningun valor en el campo _dir o se introdujo solo espacios se usa el directorio actual
                _dir = "."
                messagebox.showinfo("Informacio", "Como no se especifico ninguna ruta, se ejecutara la instancia en la carpeta donde este archivo se encuentra")
            elif exists(_dir) == False:
                # Comprobamos si el archivo existe, en caso contrario mostramos un mensaje de error de tipo DirErrorNotFoundOrNotExists
                error = DirErrorNotFoundOrNotExists(_dir) # Aqui asignamos el error que mostraremos en el except mediante una ventana
                self.error = 3
                raise DirErrorNotFoundOrNotExists(_dir)
            elif isfile(_dir) == True:
                # Comprobamos que no es un archivo, de caso contrario causamos un error de tipo ThisNotDir
                error = ThisNotDir(_dir)
                self.error = 4
                raise ThisNotDir(_dir)
        except (DirErrorNotFoundOrNotExists, ThisNotDir):
            messagebox.showerror("Error", error.msg) # Aqui mostramos el mensaje de eerror corespondiente
            return self.error
        
        _serverHTTP = serverHTTP(
            host=_host,
            port=_port,
            _dir=_dir,
            #protocolo= "HTTP/1.0",
            #HandlerClass=SimpleHTTPRequestHandler,
            #ServerClass=HTTPServer
        )
        #print(">> > ", self.ruta_actual)
        #chdir(self.ruta_actual) # volvemos a la misma ruta despues de ejecutar la instancia
        
        instancia = _serverHTTP.InitServidor() # ejecutamos una instancia del servidor y la guardamos
        print("ip&port({}), ruta({}), instancia({}), numero de instancias({})".format(_serverHTTP.getPortAndHost(), _serverHTTP.dir, instancia,len(self.serviciosHTTP)))
        self.serviciosHTTP.append(_serverHTTP)
        print(self.serviciosHTTP)

    def killThisWindows(self):
        for instancia in self.serviciosHTTP:
            print( instancia.InstanciasDelServidor)
            for servicio in instancia.InstanciasDelServidor:
                # Estos servicios HTTP son multiservicios, es decir pueden ejecutar mas de una instancia de ellos mismos
                # que hay que matar.
                for hilo in servicio.keys():
                    servicio[hilo].kill()
        self.Frame.destroy()
