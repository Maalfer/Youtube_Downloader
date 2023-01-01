class Idiomas:
    
    def __init__(self, idioma="es_ES"):
        """_summary_

            Por defecto, el idioma es Espanol

        Args:
            idioma (str, optional): _description_. Defaults to "es_ES".

        Raises:
            Exception: _description_
        """
        
        self.es_ES = "es_ES"
        self.en_US = "en_US"
        self.zh_CN = "zh_CN"
        self.ru_RU = "ru_RU"
        self.ALL_LENGUAJE = [
            self.es_ES, 
            self.en_US, 
            self.zh_CN,
            self.ru_RU
        ]
        
        self.idioma = idioma
        print(self.idioma)
        
        if self.es_ES == self.idioma:
            self.TextPortError = "El puerto introducido no se encuentra en el rango 1 - 2**16"
            self.TextHostError = "Este no es un host valido, introduzca 'localhost' o una direcion IPv4 valida"
            self.TextDirErrorNotFoundOrNotExists = "Este directorio no existe o no se pudo encontrar"
            self.TextThisNotDir = "Lo introducido no es un directorio, es un archivo posiblemente."
            self.TextUrlNotFound = "Usted no introducio ningun enlace o este no es valido :("
            self.TextUnknownError = "Ocurrio un error desconocido"
            self.TextErrorDeConexion = "No se pudo conectar a internet"
            self.TextUnknownOS = "No se pudo identificar el OS en el que se esta trabajando"
        elif self.en_US == self.idioma:
            self.TextPortError = "The entered port is not in the range 1 - 2**16"
            self.TextHostError = "This is not a valid host, enter 'localhost' or a valid IPv4 address"
            self.TextDirErrorNotFoundOrNotExists = "This directory does not exist or could not be found"
            self.TextThisNotDir = "What is entered is not a directory, it is a file possibly."
            self.TextUrlNotFound = "You did not enter any link or it is not valid :("
            self.TextUnknownError = "An unknown error occurred"
            self.TextErrorDeConexion = "Could not connect to the internet"
            self.TextUnknownOS = "Could not identify the OS being worked on"
        elif self.zh_CN == self.idioma:
            self.TextPortError = "输入的端口不在 1 - 2**16 范围内"
            self.TextHostError = "这不是有效的主机，请输入“localhost”或有效的 IPv4 地址"
            self.TextDirErrorNotFoundOrNotExists = "该目录不存在或找不到"
            self.TextThisNotDir = "输入的不是目录，可能是文件。"
            self.TextUrlNotFound = " 您没有输入任何链接或者您输入都是链接无效 :("
            self.TextUnknownError = "出现未知错误"
            self.TextErrorDeConexion = "无法连接到互联网"
            self.TextUnknownOS = "无法识别正在使用的操作系统"
        elif self.ru_RU == self.idioma:
            self.TextPortError = "Введенный порт не находится в диапазоне 1–2**16"
            self.TextHostError = "Это недопустимый хост, введите «localhost» или действительный адрес IPv4."
            self.TextDirErrorNotFoundOrNotExists = "Этот каталог не существует или не может быть найден"
            self.TextThisNotDir = "То, что вводится, не является каталогом, возможно, это файл."
            self.TextUrlNotFound = "Вы не ввели ссылку или она недействительна :("
            self.TextUnknownError = "Произошла неизвестная ошибка"
            self.TextErrorDeConexion = "Не удалось подключиться к Интернету"
            self.TextUnknownOS = "Не удалось определить ОС, над которой ведется работа"
        else:
            raise Exception("Este idioma no se encuentra {}".format(self.idioma))
            
    def setIdioma(self, idioma):
        """_summary_
            Esta funcion cambia de idioma el programa
        Args:r
            idioma (str): se recibe el idioma a cambiar
        """
        print("Cambiando de idioma a:"+idioma)
        self.__init__(idioma)