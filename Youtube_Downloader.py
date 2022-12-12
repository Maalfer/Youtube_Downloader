# Cargamos los modulos donde se han configurado cada Frame:
from frames.root import root


__version__ = 2.0
__doc__ = "programa para descargar videos y musica"
__autor__ =  {
            "usuario":"Mario", 
            "github":"https://github.com/Maalfer?tab=repositories"
        }

__contribuidores__ = [
        {
            "usuario":"desmon", 
            "github":"https://github.com/desmonHak/Youtube_Downloader"
        },
    ]

# Codigo principal a ejecutar:
if __name__ == "__main__":

    print ("propietario -> {}".format(__autor__))
    print ("contribuidores -> {}".format(__contribuidores__))
    print ("version del software -> {}".format(__version__))
    print ("doc -> {}".format(__doc__))

    root = root() # instancia a la clase root
    root.root.mainloop()
