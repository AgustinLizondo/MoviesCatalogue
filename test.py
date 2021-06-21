from Pelicula import *
Opciones = 0

while Opciones != 4:
    Opciones = int(input("Que opcion deseas utilizar? 1: Agregar pelicula, 2: Mostrar peliculas, 3: Eliminar Catálogo, 4: Salir "))

    if Opciones == 1:
        Name = input("Que película deseas agregar? ")
        Movie = Pelicula(Name)
        Catalogo.addMovie(Movie)
    elif Opciones == 2: 
        print(Catalogo.listMovie())
    elif Opciones == 3: 
        try:
            Catalogo.delMovie()
            print("El catálogo ha sido eliminado correctamente")
        except Exception as e:
            print(f"Ha ocurrido un error: {e}")
    elif Opciones ==4:
        print("Saliendo...")
        break
    else:
        print("Usted ha seleccionado una opcion incorrecta.")
