class Idiomas:
    
    def __init__(self, idioma="es_ES"):
        """_summary_

            Por defecto, el idioma es Espanol

        Args:
            idioma (str, optional): _description_. Defaults to "es_ES".

        Raises:
            Exception: _description_
        """
        
        self.es_ES = "es_ES" # Español
        self.en_US = "en_US" # Ingles
        self.zh_CN = "zh_CN" # Chino
        self.ru_RU = "ru_RU" # Ruso 
        self.fr_FR = "fr_FR" # Frances(Francia)
        self.ar_EG = "ar_EG" # Arabe Egipto(el mas similar al estandar)
        self.ja_JP = "ja_JP" # Japones
        self.de_DE = "de_DE" # Aleman(Alemania)
        self.esperanto = "esperanto" # esperanto
        
        self.ALL_LENGUAJE = [
            self.es_ES, 
            self.en_US, 
            self.zh_CN,
            self.ru_RU,
            self.fr_FR,
            self.ar_EG,
            self.ja_JP,
            self.de_DE,
            self.esperanto
        ]
        
        self.idioma = idioma
        print(self.idioma)
        
        if self.es_ES == self.idioma: # Español
            self.TextPortError = "El puerto introducido no se encuentra en el rango 1 - 2**16"
            self.TextHostError = "Este no es un host valido, introduzca 'localhost' o una direcion IPv4 valida"
            self.TextDirErrorNotFoundOrNotExists = "Este directorio no existe o no se pudo encontrar"
            self.TextThisNotDir = "Lo introducido no es un directorio, es un archivo posiblemente."
            self.TextUrlNotFound = "Usted no introducio ningun enlace o este no es valido :("
            self.TextUnknownError = "Ocurrio un error desconocido"
            self.TextErrorDeConexion = "No se pudo conectar a internet"
            self.TextUnknownOS = "No se pudo identificar el OS en el que se esta trabajando"
            
        elif self.en_US == self.idioma: # Ingles
            self.TextPortError = "The entered port is not in the range 1 - 2**16"
            self.TextHostError = "This is not a valid host, enter 'localhost' or a valid IPv4 address"
            self.TextDirErrorNotFoundOrNotExists = "This directory does not exist or could not be found"
            self.TextThisNotDir = "What is entered is not a directory, it is a file possibly."
            self.TextUrlNotFound = "You did not enter any link or it is not valid :("
            self.TextUnknownError = "An unknown error occurred"
            self.TextErrorDeConexion = "Could not connect to the internet"
            self.TextUnknownOS = "Could not identify the OS being worked on"
            
        elif self.zh_CN == self.idioma: # Chino
            self.TextPortError = "输入的端口不在 1 - 2**16 范围内"
            self.TextHostError = "这不是有效的主机，请输入“localhost”或有效的 IPv4 地址"
            self.TextDirErrorNotFoundOrNotExists = "该目录不存在或找不到"
            self.TextThisNotDir = "输入的不是目录，可能是文件。"
            self.TextUrlNotFound = " 您没有输入任何链接或者您输入都是链接无效 :("
            self.TextUnknownError = "出现未知错误"
            self.TextErrorDeConexion = "无法连接到互联网"
            self.TextUnknownOS = "无法识别正在使用的操作系统"
            
        elif self.ru_RU == self.idioma: # Ruso 
            self.TextPortError = "Введенный порт не находится в диапазоне 1–2**16"
            self.TextHostError = "Это недопустимый хост, введите «localhost» или действительный адрес IPv4."
            self.TextDirErrorNotFoundOrNotExists = "Этот каталог не существует или не может быть найден"
            self.TextThisNotDir = "То, что вводится, не является каталогом, возможно, это файл."
            self.TextUrlNotFound = "Вы не ввели ссылку или она недействительна :("
            self.TextUnknownError = "Произошла неизвестная ошибка"
            self.TextErrorDeConexion = "Не удалось подключиться к Интернету"
            self.TextUnknownOS = "Не удалось определить ОС, над которой ведется работа"
            
        elif self.fr_FR == self.idioma: # Frances(Francia)
            self.TextPortError = "Le port saisi n'est pas dans la plage 1 - 2**16"
            self.TextHostError = "Ce n'est pas un hôte valide, entrez 'localhost' ou une adresse IPv4 valide"
            self.TextDirErrorNotFoundOrNotExists = "Ce répertoire n'existe pas ou est introuvable"
            self.TextThisNotDir = "Ce qui est entré n'est pas un répertoire, c'est éventuellement un fichier."
            self.TextUrlNotFound = "Vous n'avez entré aucun lien ou il est invalide :("
            self.TextUnknownError = "Une erreur inconnue est survenue"
            self.TextErrorDeConexion = "Impossible de se connecter à Internet"
            self.TextUnknownOS = "Impossible d'identifier le système d'exploitation sur lequel on travaille"
            
        elif self.ar_EG == self.idioma: # Arabe Egipto(el mas similar al estandar)
            self.TextPortError = "المنفذ الذي تم إدخاله ليس في النطاق 1 - 2 ** 16"
            self.TextHostError = """هذا ليس مضيفًا صالحًا ، أدخل "localhost" أو عنوان IPv4 صالحًا"""
            self.TextDirErrorNotFoundOrNotExists = "هذا الدليل غير موجود أو تعذر العثور عليه"
            self.TextThisNotDir = "ما تم إدخاله ليس دليلاً ، ربما يكون ملفًا."
            self.TextUrlNotFound = "لم تقم بإدخال أي ارتباط أو أنه غير صالح :( "
            self.TextUnknownError = "حدث خطأ غير معروف"
            self.TextErrorDeConexion = "تعذر الاتصال بالإنترنت"
            self.TextUnknownOS = "تعذر تحديد نظام التشغيل قيد العمل"
            
        elif self.ja_JP == self.idioma: # Japones
            self.TextPortError = "入力されたポートは 1 から 2**16 の範囲にありません"
            self.TextHostError = "これは有効なホストではありません。「localhost」または有効な IPv4 アドレスを入力してください"
            self.TextDirErrorNotFoundOrNotExists = "このディレクトリは存在しないか、見つかりませんでした"
            self.TextThisNotDir = "入力されるのはディレクトリではなく、おそらくファイルです。"
            self.TextUrlNotFound = "リンクを入力していないか、有効ではありません:("
            self.TextUnknownError = "不明なエラーが発生しました"
            self.TextErrorDeConexion = "インターネットに接続できませんでした"
            self.TextUnknownOS = "動作しているOSを特定できませんでした"
            
        elif self.de_DE == self.idioma: # Aleman(Alemania)
            self.TextPortError = "Der eingegebene Port liegt nicht im Bereich 1 - 2**16"
            self.TextHostError = "Dies ist kein gültiger Host, geben Sie „localhost“ oder eine gültige IPv4-Adresse ein"
            self.TextDirErrorNotFoundOrNotExists = "Dieses Verzeichnis existiert nicht oder konnte nicht gefunden werden"
            self.TextThisNotDir = "Was eingetragen wird, ist kein Verzeichnis, sondern möglicherweise eine Datei."
            self.TextUrlNotFound = "Sie haben keinen Link eingegeben oder er ist ungültig :("
            self.TextUnknownError = "Ein unbekannter Fehler ist aufgetreten"
            self.TextErrorDeConexion = "Es konnte keine Verbindung zum Internet hergestellt werden"
            self.TextUnknownOS = "Das Betriebssystem, an dem gearbeitet wird, konnte nicht identifiziert werden"
            
        elif self.esperanto == self.idioma: # esperanto
            self.TextPortError = "La enigita haveno ne estas en la intervalo 1 - 2**16"
            self.TextHostError = "Ĉi tio ne estas valida gastiganto, enigu 'localhost' aŭ validan IPv4-adreson"
            self.TextDirErrorNotFoundOrNotExists = "Ĉi tiu dosierujo ne ekzistas aŭ ne troveblas"
            self.TextThisNotDir = "Kio estas enigita ne estas dosierujo, ĝi estas dosiero eble."
            self.TextUrlNotFound = "Vi enigis neniun ligilon aŭ ĝi ne validas :("
            self.TextUnknownError = "Nekonata eraro okazis"
            self.TextErrorDeConexion = "Ne eblis konekti al la interreto"
            self.TextUnknownOS = "Ne eblis identigi la OS prilaborata"

        
        
        
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