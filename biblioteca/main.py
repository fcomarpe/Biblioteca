import libro
import biblioteca

# Creo una variable cuyo valor es la clase Biblioteca.
mi_catalogo = biblioteca.Biblioteca()

# Creo tres variables distintas, con el valor de la clase Libro.
mi_libro_uno = libro.Libro("Harry Potter y la piedra filosofal", "J.K. Rowling", "1997")
mi_libro_dos = libro.Libro("Nacidos de la bruma", "Brandon Sanderson", "2006")
mi_libro_tres = libro.Libro("El Principito", "Antoine de Saint-Exupéry", "1943")

# Dentro de la variable, llamo al método agregar y selecciono los libros.
mi_catalogo.agregar_libro(mi_libro_uno)
mi_catalogo.agregar_libro(mi_libro_dos)
mi_catalogo.agregar_libro(mi_libro_tres)

print("Catálogo de la biblioteca:\n")

for libro in mi_catalogo.lista:
    print(libro) # Dispara el catálogo correctamente.