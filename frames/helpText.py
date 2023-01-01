from os.path import exists
from sys import platform

from .error import UnknownOS

class Textos():
    
    def __init__(self, file="helpText.txt", carpeta="data"):
        
        # Abrimos el archivo en modo lectura
        self.carpeta = carpeta
        self.file = open(self.getFileRuta(__file__, file), "r")
        self.text = self.file.read()
        self.file.close()
        
    def getFileRuta(self, ruta, archivo):
        """_summary_

            Esta funcion calcula la ruta del archivo que se quiere abrir usando
            de referencia la ruta de este archivo.
            
        Args:
            ruta (str): ruta de este archivo
            archivo (str): nombre del archivo
        """
        if platform == "Win32":
            ruta = ruta.split("\\") 
        elif platform == "linux" or platform == "linux2":
            ruta = ruta.split("/") 
        else:
            # Este error se produce cuando no se puede identificar el OS en el que se trabaja
            raise UnknownOS(platform)
        
        print(ruta)
        # Cambiamos e nombre de este archivo en la ruta, por el nombre de la carpeta(data) que esta en el mismo directorio que ese archivo.
        ruta[len(ruta)-1] = self.carpeta
        # agregamos el nombre del archivo a la ruta:
        ruta.append(archivo)
        # volvemos a convertir la ruta a un string:
        if platform == "Win32":
            ruta = "\\".join(ruta)
        elif platform == "linux" or platform == "linux2":
            ruta = "/".join(ruta)
        print(ruta)
        
        return ruta