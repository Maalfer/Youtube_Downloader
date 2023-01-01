from .idiomas import Idiomas

class PortError(Exception):
    def __init__(self, port, msg=None, idioma=Idiomas()):
        self.idioma = idioma
        if msg == None: self.msg = self.idioma.TextPortError
        else: self.msg = msg
        
        self.port = port
        super().__init__(self.msg)
        
class HostError(Exception):
    def __init__(self, host, msg=None, idioma=Idiomas()):
        self.idioma = idioma
        if msg == None: self.msg = self.idioma.TextHostError
        else: self.msg = msg
        
        self.host = host
        super().__init__(self.msg)

class DirErrorNotFoundOrNotExists(Exception):
    def __init__(self, _dir, msg=None, idioma=Idiomas()):
        self.idioma = idioma
        if msg == None: self.msg = self.idioma.TextDirErrorNotFoundOrNotExists
        
        else: self.msg = msg
        self.dir = _dir
        super().__init__(self.dir)
    
class ThisNotDir(Exception):
    def __init__(self, _dir, msg=None, idioma=Idiomas()):
        self.idioma = idioma
        if msg == None: self.msg = self.idioma.TextThisNotDir
        
        else: self.msg = msg
        self.dir = _dir
        super().__init__(self.dir)
        
class UrlNotFound(Exception):
    def __init__(self, url, msg=None, idioma=Idiomas()):
        self.idioma = idioma
        if msg == None: self.msg = self.idioma.TextUrlNotFound
        
        else: self.msg = msg
        self.url = url
        super().__init__(self.url)
        
class UnknownError(Exception):
    def __init__(self, msg=None, idioma=Idiomas()):
        self.idioma = idioma
        if msg == None: self.msg = self.idioma.TextUnknownError
        
        else: self.msg = msg
        super().__init__()
        
class ErrorDeConexion(Exception):
    def __init__(self, msg=None, idioma=Idiomas()):
        self.idioma = idioma
        if msg == None: self.msg = self.idioma.TextErrorDeConexion
        
        else: self.msg = msg
        super().__init__()
        
class UnknownOS(Exception):
    def __init__(self, ThisOs, msg=None, idioma=Idiomas()):
        self.idioma = idioma
        if msg == None: self.msg = self.idioma.TextUnknownOS
        
        else: self.msg = msg
        self.ThisOS = ThisOs
        super().__init__(self.ThisOS)