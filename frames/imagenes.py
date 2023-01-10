from sys import version

if version[0] == "3":
    from tkinter import PhotoImage, Label
elif version[0] == "2":
    from Tkinter import (PhotoImage, Label)
else:
    print("Wtf que porongas paso aqui?!")
    
class Imagenes:
    
    def __init__(self):
        
        self.ImagenesAnadidas = []
        
        self.nameYoutubePNG = "imagenes/youtube.png"
        self.youtubePNG = PhotoImage(file=self.nameYoutubePNG) # agregar una imagen
        
        self.nameBackground = "imagenes/UseThisTooltoMake2DPixelSpritesOnlineforFree.png"
        self.backgroundIMG = PhotoImage(file=self.nameBackground) # origen: https://br.pinterest.com/pin/404620347766483651/
        
    def addImagenes(self, _PhotoImage, frame):
        """
            se espera un objeto de la clase PhotoImage
            para agregarlo a un frame
        """
        _Label = Label(frame, image=_PhotoImage, bd=0)
        self.ImagenesAnadidas.append(_Label)
        return _Label