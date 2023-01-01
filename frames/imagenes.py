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
        
        self.youtubePNG = PhotoImage(file="youtube.png") # agregar una imagen
        
    def addImagenes(self, _PhotoImage, frame):
        """
            se espera un objeto de la clase PhotoImage
            para agregarlo a un frame
        """
        _Label = Label(frame, image=_PhotoImage, bd=0)
        self.ImagenesAnadidas.append(_Label)
        return _Label