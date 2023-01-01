from sys import version
from threading import Thread, RLock, _active
from time import sleep
from ctypes import pythonapi,  py_object
from os import chdir, getcwd

if version[0] == "3":
    from http.server import HTTPServer, SimpleHTTPRequestHandler
elif version[0] == "2":
    #from BaseHTTPServer import (HTTPServer)
    # error
    pass
else:
    print("Wtf que porongas paso aqui?!")

class serverHTTP:
    
    def __init__(
            self,
            host="127.0.0.1",
            port=8000,
            _dir=".",
            protocolo= "HTTP/1.0",
            sys_version='YTServer',
            server_version="undefine", 
            HandlerClass=SimpleHTTPRequestHandler,
            ServerClass=HTTPServer
        ):
        self.dir = _dir
        self.port = port
        self.host = host
        self.sys_version = sys_version
        self.server_version = server_version
        self.HandlerClass = HandlerClass
        self.ServerClass = ServerClass
        self.protocolo = protocolo
        self.NumeroInstanciasDelServidor = 0
        self.status = False
        
        self.InstanciasDelServidor = [
            # Aqui se almacena las distintas instancias de servidores HTTP
        ]
    

    def InitServidor(self):
        """
            Crea una instancia de un servicio HTTP
        """
        class Hilo(Thread):
            
            def __init__(self, clasePadre):
                self.lock = RLock()
                self.clasePadre = clasePadre
                super(Hilo, self).__init__()
            
                self.instanciaServer = None
                """class ServerFile(SimpleHTTPRequestHandler):
                    def __init__(self, *args, **kwargs):
                        super().__init__(*args, **kwargs, directory=_dir)
                self.instanciaServer.HandlerClass = ServerFile()"""
                
            def get_id(self):
                if hasattr(self, "_thread_id"):
                    return self._thread_id
                for id, thread in _active.items():
                    if thread is self:
                        return id
                    
            def run(self):
                """
                    Codigo que ejecuta el hilo
                """ 
                sleep(0.1) # esperamos 0.1s
                server_address = (self.clasePadre.host, self.clasePadre.port)
                #chdir(self.clasePadre.dir)
                print("server iniciado en: ({}) ruta({})".format(self.clasePadre.getPortAndHost(), getcwd()))
                self.clasePadre.HandlerClass.protocol_version = self.clasePadre.protocolo
                self.clasePadre.HandlerClass.server_version = self.clasePadre.server_version
                self.clasePadre.HandlerClass.sys_version = self.clasePadre.sys_version
                self.clasePadre.HandlerClass.directory = self.clasePadre.dir
                print(">>> ",self.clasePadre.HandlerClass.directory)
                
                try:
                    self.instanciaServer = self.clasePadre.ServerClass(server_address, self.clasePadre.HandlerClass)
                    self.instanciaServer.serve_forever()
                except OSError:
                    return -1
            
            def kill(self):
                
                hilo_id = self.get_id()
                EstadoHilo = pythonapi.PyThreadState_SetAsyncExc(hilo_id, py_object(SystemExit))
                if EstadoHilo > 1:
                    pythonapi.PyThreadState_SetAsyncExc(hilo_id, 0)
                
            def getInstanciaServer(self):
                return self.instanciaServer

        hilo = Hilo(self)
        hilo.setDaemon(True) # deja la posibilidad de que el codigo principal sea ejecutado y mata los procesos cuando finaliza el code principal
        hilo.setName("Servidor HTTP({})".format(self.NumeroInstanciasDelServidor))
        
        hilo.start()
        sleep(0.2) # Dejar el hilo corriendo 0.2 segundos minimo, importante!!!
        
        httpd = {self.NumeroInstanciasDelServidor:hilo}
        self.NumeroInstanciasDelServidor+=1
        self.InstanciasDelServidor.append(httpd)
        return httpd

        
    def getPortAndHost(self):
        return "{}:{}".format(self.host, self.port)
    def getStatus(self):
        return self.status