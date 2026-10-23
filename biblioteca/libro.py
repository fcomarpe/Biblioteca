class Libro:
    def __init__(self, titulo, autor, anio: int):
        self.titulo = titulo
        self.autor = autor
        self.anio = anio
        self.disponible = True
        
    def __str__(self):
        estado = "Disponible" if self.disponible else "Prestado"
        return f"{self.titulo} --- {self.autor} ({self.anio}) | {estado}"


"""

mi_libro = Libro("Nacidos de la bruma", "Brandon Sanderson", "2006")
print(mi_libro) // Dispara mi_libro correctamente. """
    