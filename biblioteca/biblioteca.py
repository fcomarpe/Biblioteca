import libro

class Biblioteca:
    def __init__(self):
        self.lista = []
        
    def agregar_libro(self, libro):
        self.lista.append(libro)
        
"""

biblioteca = Biblioteca()

mi_libro = libro.Libro("Harry Potter", "J.K. Rowling", "1997")
biblioteca.agregar_libro(mi_libro)

print(mi_libro) // Dispara correctamente mi_libro      
"""