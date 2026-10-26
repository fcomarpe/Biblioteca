import libro
import biblioteca


def main():
    mi_catalogo = biblioteca.Biblioteca()

    libros_iniciales = [
        libro.Libro(
            "Harry Potter y la piedra filosofal",
            "J.K. Rowling",
            1997
        ),
        libro.Libro(
            "Nacidos de la bruma",
            "Brandon Sanderson",
            2006
        ),
        libro.Libro(
            "El Principito",
            "Antoine de Saint-Exupéry",
            1943
        ),
    ]
    for libro_actual in libros_iniciales:
        mi_catalogo.agregar_libro(libro_actual)

    activo = True

    while activo:
        opcion = menu_interactivo()

        if opcion == "1":
            ver_catalogo(mi_catalogo)
        elif opcion == "2":
            aniadir_libro(mi_catalogo)
        elif opcion == "3":
            buscar_libro(mi_catalogo)
        elif opcion == "4":
            prestar_libro(mi_catalogo)
        elif opcion == "5":
            devolver_libro(mi_catalogo)
        elif opcion == "6":
            activo = False
            print("\nHa salido del programa con éxito.")
        elif opcion != "6":
            print("ERROR. Debe de introducir un número válido (1, 2, 3 o 4).")


def menu_interactivo():
    print("\n----- Menú de la biblioteca -----\n")
    print("1. Ver catálogo")
    print("2. Añadir libro")
    print("3. Buscar libro")
    print("4. Préstamo de libro.")
    print("5. Devolición de libro.")
    print("6. Salir")
    return input("\nPor favor, seleccione una opción: ")

def ver_catalogo(catalogo_recibido):
    print("\n----- Catálogo de la biblioteca -----\n")
    for libro in catalogo_recibido.lista:
        print(libro)

def aniadir_libro(catalogo_recibido):
    titulo = input("Por favor, introduzca el título del libro: ")
    autor = input("Por favor, introduzca el autor del libro: ")

    while True:
        try:
           anio = int(input("Por favor, introduzca el año de del libro: "))
           break
        except ValueError:
            print("ERROR. Debe de introducir un número.")

    nuevo_libro = libro.Libro(titulo, autor, anio)
    catalogo_recibido.agregar_libro(nuevo_libro)
    print("\nEl libro se ha introducido correctamente.")

def buscar_libro(catalogo_recibido):
    titulo = input("Por favor, introduzca el título del libro: ")
    existe = catalogo_recibido.buscar_libro(titulo)
    if not existe:
        print("\nLamentablemente, no disponemos de dicho libro.")
    else:
        print(f"\n{existe}")

def prestar_libro(catalogo_recibido):
    titulo = input("Por favor, introduzca el título del libro: ")
    estado = catalogo_recibido.buscar_libro(titulo)
    if not estado:
        print("\nNo disponemos del libro que ha introducido.")
    elif not estado.disponible:
        print("\nLamentablemente, este libro ya está prestado.")
    else:
        print("\nEl libro que ha buscado está disponible.")
        estado.disponible = False

def devolver_libro(catalogo_recibido):
    titulo = input("Por favor, introduzca el título del libro que desea devolver: ")
    estado = catalogo_recibido.devolver_libro(titulo)
    if not estado:
        print("\nERROR. El libro que trata de devolver no existe.")
    elif not estado.disponible:
        print("\nLibro devuelto con éxito.")
        estado.disponible = True
    else:
        print("\nERROR. El libro introducido ya ha sido devuelto.")


main()