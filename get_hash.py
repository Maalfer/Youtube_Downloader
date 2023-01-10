from os import walk, getcwd
from sys import platform
from hashlib import md5
from requests import request, ConnectionError
from zipfile import ZipFile
from io import BytesIO
from random import randint

from frames.error import UnknownOS, ErrorDeConexion
from frames.load_config import load_file

excluir_directorios = [
    # directorios a excluir de la recopilacion
    "__pycache__",
    ".dist", 
    ".vscode",
    ".git",
]

def get_directory(ruta=".", debug=False):
    
    """_summary_

        Esta funcion obtiene la ruta de los archivos y los 
        archivos de forma recursiva y lo retorna en forma de diccionario
        

    Raises:
        UnknownOS: Error que se lanza cuando la plataforma no puede ser identificada

    Returns:
        dict: diccionario con las rutas y los archivos, ruta:lista_archivos
    """
    
    arbol_directorios = dict()
    
    if platform == "Win32": splas = "\\"
    elif platform == "linux" or platform == "linux2": splas = "/"
    else: raise UnknownOS(platform)
    
    dire = list(walk(ruta, topdown=False))
            
    for carpeta in dire: 
        estado = 0 # variable para controlar cuando anadir o no cambios al diccionario
        # ('./.git/logs/refs/remotes/origin', [], ['HEAD'])
        
        ruta_format_list = carpeta[0].split(splas)
        # (".", "frames", "__pycache__")
        
        for carpetaAExcluir in excluir_directorios:
            if carpetaAExcluir in ruta_format_list:
                estado = 1 # si se encontro el nombre de la carpeta a excluir en la ruta, se pone 
                # la variable estado a 1 para no anadirlo al bucle
                break
            
        if estado == 0:
            arbol_directorios.update({carpeta[0]:carpeta[2]})
    
    return arbol_directorios


def print_tree(tree_dir):
    """_summary_
        Imprimimos la ruta y cada archivo de un arbol en formato diccionaario
    Args:
        tree_dir (dict): arbol diccionario con archivos y rutas
    """
    
    for ruta in tree_dir.keys():
        
        #print("-> {}".format(ruta))
        
        for archivo in tree_dir[ruta]:
            
            print("[*] ruta -> ({}) archivo -> ({})".format(ruta, archivo))
    
def get_hash(tree_dir, debug=False, excluir_files=["file.json", "get_hash.py", "file_check_update.json"]):
    """_summary_
        Esta funcion obtiene los hash's de los archivos de un arbol de archivos
        y los almacena en un dicionario
    Args:
        tree_dir (dict): arbol de directorios
        debug (bool, optional): modo debug. Defaults to False.
        excluir_files (list, optional): lista de archivos a excluir

    Raises:
        UnknownOS: error que ocurre cuando la plataforma no puede identificarse

    Returns:
        dict: se retorna un diccionario con los hash y la ruta mas el archivo, hash:archivo_ruta
    """
    dict_hash_dir = dict()

    if platform == "Win32": splas = "\\"
    elif platform == "linux" or platform == "linux2": splas = "/"
    else: raise UnknownOS(platform)
    
    for ruta in tree_dir.keys():
        for archivo in tree_dir[ruta]:
            
            if (archivo in excluir_files) == False:
                # si el archivo no se encuentra en la lista de archivos a excluir lo añadimos
                
                _file_ = "{}{}{}".format(ruta, splas, archivo)
                _file = open(_file_, "rb")
                hashString = md5(_file.read()).hexdigest()
                if debug:
                    print("hash del archivo ({}): {}".format(_file_, hashString))
                _file.close()
                dict_hash_dir.update({hashString:_file_})
    
    return dict_hash_dir

def print_dict_hash_dir(dict_hash_dir):
    """_summary_
        Se imprime un diccionario de hash's y archivos
    Args:
        dict_hash_dir (dict): diccionario de hash's y archivos
    """
    for _hash in dict_hash_dir.keys():
        print("hash -> ({}) ruta -> ({})".format(_hash, dict_hash_dir[_hash]))

def write_dict_hash_dir(dict_hash_dir, file_name="file.json"):
    """_summary_
        Se escribe los datos de un diccionario hash's y archivos en formato json,
        por defecto en un archivo llamado "file.json"
    Args:
        dict_hash_dir (dict): diccionario de hash's y archivos
        file_name (str, optional): nombre del archivo .json de salida. Defaults to "file.json".
    """
    _file = open(file_name, "w")
    _file.write(str(dict_hash_dir))
    _file.close()

def cheack_updates(users=["desmonHak", "Maalfer"], url="https://raw.githubusercontent.com/{}/Youtube_Downloader/main/file.json", filename="file_check_update.json", debug=False, fileCheck="file.json"):
    # https://github.com/desmonHak/Youtube_Downloader/archive/refs/heads/main.zip
    # https://github.com/Maalfer/Youtube_Downloader/archive/refs/heads/main.zip
    
    if platform == "Win32": splas = "\\"
    elif platform == "linux" or platform == "linux2": splas = "/"
    else: raise UnknownOS(platform)
    
    _file = None
    
    for user in users:
        
        try:
            useragents = [
                "Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 5.1; .NET CLR 1.1.4322; .NET CLR 2.0.50727; .NET CLR 3.0.04506.30)",
                "Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.1; .NET CLR 1.1.4322)",
                "Googlebot/2.1 (http://www.googlebot.com/bot.html)",
                "Opera/9.20 (Windows NT 6.0; U; en)",
                "Mozilla/5.0 (X11; U; Linux i686; en-US; rv:1.8.1.1) Gecko/20061205 Iceweasel/2.0.0.1 (Debian-2.0.0.1+dfsg-2)",
                "Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 5.1; Trident/4.0; FDM; .NET CLR 2.0.50727; InfoPath.2; .NET CLR 1.1.4322)",
                "Opera/10.00 (X11; Linux i686; U; en) Presto/2.2.0",
                "Mozilla/5.0 (Windows; U; Windows NT 6.0; he-IL) AppleWebKit/528.16 (KHTML, like Gecko) Version/4.0 Safari/528.16",
                "Mozilla/5.0 (compatible; Yahoo! Slurp/3.0; http://help.yahoo.com/help/us/ysearch/slurp)", 
                "Mozilla/5.0 (X11; U; Linux x86_64; en-US; rv:1.9.2.13) Gecko/20101209 Firefox/3.6.13"
                "Mozilla/4.0 (compatible; MSIE 9.0; Windows NT 5.1; Trident/5.0)",
                "Mozilla/5.0 (compatible; MSIE 8.0; Windows NT 5.1; Trident/4.0; .NET CLR 1.1.4322; .NET CLR 2.0.50727)",
                "Mozilla/4.0 (compatible; MSIE 7.0b; Windows NT 6.0)",
                "Mozilla/4.0 (compatible; MSIE 6.0b; Windows 98)",
                "Mozilla/5.0 (Windows; U; Windows NT 6.1; ru; rv:1.9.2.3) Gecko/20100401 Firefox/4.0 (.NET CLR 3.5.30729)",
                "Mozilla/5.0 (X11; U; Linux x86_64; en-US; rv:1.9.2.8) Gecko/20100804 Gentoo Firefox/3.6.8",
                "Mozilla/5.0 (X11; U; Linux x86_64; en-US; rv:1.9.2.7) Gecko/20100809 Fedora/3.6.7-1.fc14 Firefox/3.6.7",
                "Mozilla/5.0 (compatible; Googlebot/2.1; http://www.google.com/bot.html)",
                "Mozilla/5.0 (compatible; Yahoo! Slurp; http://help.yahoo.com/help/us/ysearch/slurp)",
                "YahooSeeker/1.2 (compatible; Mozilla 4.0; MSIE 5.5; yahooseeker at yahoo-inc dot com ; http://help.yahoo.com/help/us/shop/merchant/)"
            ]
            
            headers = {
                "User-Agent": useragents[randint(0, len(useragents)-1)],
                "accept": "*/*",               
                "accept-encoding": "gzip;deflate;br" 
            }
            response = request("GET", url.format(user), headers = headers)
            
            _file = open(filename, "w")
            _file.write(response.text)
            _file.close()
            
            _file = response.text
            
            """carpetaDescargas = "{}{}{}".format(getcwd(), splas, tempDir)
            print(carpetaDescargas)
            archivo = ZipFile(BytesIO(response.content))
            archivo.extractall(carpetaDescargas)        
            print(dir(archivo)    )
            if debug: print(archivo.printdir())
            
            
            # obtenemos el nombre de la carpeta donde esta todos los archivos descargados:
            file_name = archivo.infolist()[0].filename"""
            
            dataDownload = load_file(filename)
            dataOriginal = load_file(fileCheck)
            
            if len(dataDownload) != len(dataOriginal):
                # son diferentes, retornar True, hay actualizacion
                return True
            else:
                for _hash in dataOriginal.keys():
                    if _hash in dataDownload:
                        print("El hash ({}) del archivo ({}) es correcto".format(_hash, dataDownload[_hash]))
                    else:
                        print("Al parecer hubo cambios de esta version ({})".format(_hash))
                        return True # hay hash's diferentes, actualizacion
                return False # si no se detecto hash's diferenetes y el diccionario es el mismo, no hay actualizacion
            
            break
        except ConnectionError:
            print("No se pudo obtener los datos desde ({})".format(url.format(user)))
        
    if _file != None:
        return _file
    else:
        raise ErrorDeConexion
    

if __name__ == "__main__":
    print(cheack_updates())
    
    print()
    
    tree_dir = get_directory(debug=False)
    #print_tree(tree_dir)
    
    dict_hash_dir = get_hash(tree_dir)
    #print_dict_hash_dir(dict_hash_dir)
    write_dict_hash_dir(dict_hash_dir)
    
    