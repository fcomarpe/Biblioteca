# Biblioteca
Prácticas de las prácticas (Café para cafeteros)

## Descripción

Esta aplicación de consola está desarrollada en Python y permite gestionar el catálogo de una pequeña biblioteca. El usuario puede consultar los libros, añadir nuevos títulos, buscar libros por su título, gestionar préstamos y devoluciones, y consultar estadísticas del catálogo.

El proyecto se ha desarrollado de forma incremental, utilizando Git y GitHub para controlar los cambios mediante ramas, commits y pull requests.

## Requisitos

- Tener Python instalado.
- Disponer de una terminal para ejecutar el programa.

## Cómo ejecutar el programa

Desde la carpeta raíz del proyecto, ejecuta el siguiente comando:

```bash
python3 biblioteca/main.py
```

El programa mostrará un menú interactivo desde el que se podrán seleccionar las distintas operaciones disponibles.

## Funcionalidades

- **Ver catálogo:** muestra los libros registrados, incluyendo su título, autor, año de publicación y estado.
- **Añadir libros:** permite introducir nuevos libros en el catálogo.
- **Buscar libros:** permite localizar libros por su título, sin distinguir entre mayúsculas y minúsculas.
- **Prestar libros:** permite prestar libros que estén disponibles e informa si el libro ya está prestado.
- **Devolver libros:** permite devolver libros prestados e informa del resultado de la operación.
- **Consultar estadísticas:** muestra el número total de libros, cuántos están disponibles y cuántos están prestados.
- **Control de errores:** controla la introducción de años no numéricos y de opciones no válidas en el menú.

## Estructura del proyecto

```text
Biblioteca/
├── biblioteca/
│   ├── main.py
│   ├── libro.py
│   └── biblioteca.py
└── README.md
```

- `main.py`: contiene el menú interactivo y coordina las operaciones del programa.
- `libro.py`: define la clase `Libro` y los datos de cada libro.
- `biblioteca.py`: define la clase `Biblioteca`, encargada de gestionar el catálogo.
