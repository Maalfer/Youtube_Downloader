from sys import platform


from .error import UnknownOS, NotFoundThisFile, NotExistsThisLenguaje

class Textos():
    
    def __init__(self, idiomas, file="helpText.txt", carpeta="data"):
        
        # Abrimos el archivo en modo lectura
        self.idioma = idiomas.idioma
        self.carpeta = carpeta
        
        # Añadimos al nombre base helpText.txt, el idioma escogido helpText-es_ES.txt por ejemplo:
        file = file.split(".")
        file[0] = file[0]+"-"+self.idioma
        file = ".".join(file)
        try:
            try:
                self.file = open(self.getFileRuta(__file__, file), "r", encoding="utf-8")
            except FileNotFoundError: 
                from .load_config import calcular_file
                self.file = open("\\".join(calcular_file(__file__, "frames\\data").split("\\")[:-1])+"\\"+file, "r", encoding="utf-8")
            self.text = self.file.read()
            self.file.close()
        except FileNotFoundError:
            if (idiomas.idioma in idiomas.ALL_LENGUAJE) == False:
                # No existe este idioma en la lista de idiomas
                raise NotExistsThisLenguaje(self.idioma) # Esto de aqui no tiene mucho sentido xd
            else:    
                # Si el idioma esta en la lista, quiere decir que no existe un archivo con la doc en el idioma escogido
                error = NotFoundThisFile(file)
                print(error.msg)
                raise NotFoundThisFile(file)
        
    def getFileRuta(self, ruta, archivo):
        """_summary_

            Esta funcion calcula la ruta del archivo que se quiere abrir usando
            de referencia la ruta de este archivo.
            
        Args:
            ruta (str): ruta de este archivo
            archivo (str): nombre del archivo
        """
        if platform == "win32":
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
        if platform == "win32":
            ruta = "\\".join(ruta)
        elif platform == "linux" or platform == "linux2":
            ruta = "/".join(ruta)
        print(ruta)
        
        return ruta
