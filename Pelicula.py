import os

class Pelicula:
    def __init__(self, nombre):
        self.nombre = nombre
    def __str__(self):
        return f"Película [{self.nombre}]"

class Catalogo:
    Ruta = "C:\\Users\\AgusB\\Downloads\\Descargas\\Python\\PYTHON\\Catalogo\\Peliculas.txt"
    @classmethod
    def addMovie(cls, pelicula):
        with open(cls.Ruta, "a", encoding="UTF8") as archivo:
            archivo.write(f"{pelicula.nombre} \n")
    @classmethod
    def listMovie(cls):
        with open(cls.Ruta, "r", encoding="UTF8") as archivo:
            print("Catálogo: \n")
            print(archivo.read())
    @classmethod
    def delMovie(cls):
        os.remove(cls.Ruta)
        print("Archivo eliminado correctamente.")