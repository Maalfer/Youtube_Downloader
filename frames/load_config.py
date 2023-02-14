from ast import literal_eval
from sys import platform


from .error import UnknownOS, NotFoundThisFile

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

def calcular_file(file, ruta, rutaWin="C:\\Users\\{}\\Youtube_Downloader"):
    
    
    print(ruta)
    # El archivo root.py tiene su archivo root.json
    file = file.split(".")
    file[-1] ="json" # cambiamos el .py por .json
    file = ".".join(file)

    
    
    
    if platform == "win32": 
        from os.path import expanduser
        print(expanduser('~').split("\\")[-1])
        rutaWin = rutaWin.format(expanduser('~').split("\\")[-1])
        ruta = calcular_ruta_format_linux_to_win(rutaWin)+"\\"+ruta+ "\\" + file.split("\\")[-1]
        print(ruta)
        print(rutaWin)

        #ruta = rutaWin + "\\" + "config-GUI" + "\\" + file.split("\\")[-1]
        #print(ruta)
    
    elif platform == "linux" or platform == "linux2": 
        # convertimos la ruta recibida a la plataforma para la plataforma selecionada para evitar problemas
        ruta = calcular_ruta_format_linux_to_win(ruta)
        
        # el nombre de frames lo cambiamos por el de la carpeta config-GUI
        _ruta = file.split("/")
        _ruta[-2] = ruta
        ruta = "/".join(_ruta)
        
    else: raise UnknownOS(platform)
    
    return ruta 
   
        

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
