class Biblioteca:
    def __init__(self):
        self.lista = []

    def agregar_libro(self, libro):
        self.lista.append(libro)

    def buscar_libro(self, titulo_buscado):
        for libro_buscado in self.lista:
            if titulo_buscado.lower() in libro_buscado.titulo.lower():
                return libro_buscado
        return None

    def devolver_libro(self, titulo_devuelto):
        return self.buscar_libro(titulo_devuelto)


"""

biblioteca = Biblioteca()

mi_libro = libro.Libro("Harry Potter", "J.K. Rowling", "1997")
biblioteca.agregar_libro(mi_libro)

print(mi_libro) // Dispara correctamente mi_libro
"""
