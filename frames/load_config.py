from ast import literal_eval
from sys import platform

from .error import UnknownOS, NotFoundThisFile

def calcular_file(file, ruta):
    
    # El archivo root.py tiene su archivo root.json
    file = file.split(".")
    file[-1] ="json" # cambiamos el .py por .json
    file = ".".join(file)
    
    # convertimos la ruta recibida a la plataforma para la plataforma selecionada para evitar problemas
    ruta = calcular_ruta_format_linux_to_win(ruta)
    
    if platform == "win32": splas = "\\"
    elif platform == "linux" or platform == "linux2": splas = "/"
    else: raise UnknownOS(platform)
    
    # el nombre de frames lo cambiamos por el de la carpeta config-GUI
    _ruta = file.split(splas)
    _ruta[-2] = ruta
    ruta = splas.join(_ruta)
    
    return ruta 
   
        
def calcular_ruta_format_linux_to_win(ruta):
    """_summary_
        trasmoforma una ruta de linux a windows(sustituir las barras)
    Args:
        ruta (_type_): _description_
    """
    # volvemos a convertir la ruta a un string:
    if platform == "win32": return "\\".join(ruta.split("/"))
    elif platform == "linux" or platform == "linux2": return "/".join(ruta.split("/"))
    else: raise UnknownOS(platform)
        

def load_file(file):
    """_summary_
        Cargamos el archivo json y lo formateamos a un dict
    Args:
        file (str): Nombre del archivo .json
    """
    
    try:
        file = open(file, "r")
        # convertimos el json en un ficionario
        _file = literal_eval(file.read())
        # cerrar el archivo 
        file.close()
    
        return _file
    except FileNotFoundError: 
        print("Archivo de configuracion no encontrado: {}".format(file))
        raise NotFoundThisFile(file)
