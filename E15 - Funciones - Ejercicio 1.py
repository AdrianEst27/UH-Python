# TODO: Biblioteca Digital

#* Lista para guardar los libros.
biblioteca = []

def Registrar(titulo, autor, anio, genero):
    """
        Función Registrar:
            Se encarga de registrar los libros en la lista "biblioteca".
        
        Parámetros:
            titulo: El título del libro a registrar.
            autor : El nombre del autor del libro.
            anio  : El año de publicación del libro.
            genero: El género literario del libro (por ejemplo, Novela, Fantasía, Ciencia ficción).

        Retorno:
            La función no retorna ningún valor, pero agrega el libro a la lista "biblioteca".
    """
    libro = {
        'titulo': titulo,
        'autor': autor,
        'año': anio,  # Año
        'genero': genero
    }
    biblioteca.append(libro)
    print(f" > El libro '{titulo}', ha sido agregado exitosamente.")

def Buscar(titulo):
    """
        Función Buscar:
            La función recorre la lista "biblioteca" para encontrar un libro cuyo
            título coincida con el título proporcionado.
            Si se encuentra el libro, se imprimen sus detalles (título, autor, año, género).
            Si no se encuentra, se imprime un mensaje indicando que el libro no está registrado.

        Parámetros:
            titulo : El título del libro a buscar.

        Retorno:
            La función no retorna ningún valor, solo imprime el resultado de la búsqueda.
    """
    for libro in biblioteca:
        if libro['titulo'].lower() == titulo.lower():
            print(f"\n > Libro encontrado: {libro['titulo']}, Autor: {libro['autor']}, Año: {libro['año']}, Género: {libro['genero']}")
            return
    print(f"\n > El libro '{titulo}' no existe en la biblioteca.")

def Edad_libro(anio):
    """
        Función Edad_libro:
            La función toma el año en que se publicó el libro y calcula cuántos años han pasado
            desde entonces hasta el año actual. Utiliza una función lambda para realizar el cálculo 
            y datetime para obtener la fecha actual.

        Parámetros:
            anio : El año de publicación del libro.

        Retorno:
            La cantidad de años que han pasado desde el año de publicación hasta el año actual.
    """
    from datetime import datetime
    edad = lambda x: datetime.now().year - x
    return edad(anio)

def Categorias(genero):
    """
        Función Categorias:
            Esta función busca en la lista "biblioteca" todos los libros que pertenecen 
            al género especificado. Compara el género de cada libro de manera insensible a mayúsculas,
            y si encuentra libros en ese género, imprime una lista con sus títulos. 
            Si no se encuentran libros en el género, se imprime un mensaje indicando 
            que no hay libros disponibles en esa categoría.

        Parámetros:
            genero : El género literario que se desea buscar (por ejemplo, "Novela", "Fantasía").

        Retorno: 
            La función no retorna ningún valor, pero imprime el resultado de la búsqueda.
    """
    libros_en_genero = [libro['titulo'] for libro in biblioteca if libro['genero'].lower() == genero.lower()]
    
    if libros_en_genero: 
        print(f" > Libros en el género '{genero}': {', '.join(libros_en_genero)}")
    else: 
        print(f" > No hay libros en el género '{genero}'.")

def ContarLibros():
    """
        Función ContarLibros:
            Esta función utiliza una función recursiva interna llamada 'contar' para iterar
            a través de la lista "biblioteca". Devuelve el total de libros registrados 
            sumando 1 por cada libro en la lista. Si no hay libros, devuelve 0.

        Retorno:
            El número total de libros en la biblioteca. Devuelve 0 si no hay libros registrados.

    """
    def contar(lista):
        if not lista:
            return 0  # Si no hay libros, devuelve 0.
        return 1 + contar(lista[1:])  # Suma 1 por cada libro.
    
    return contar(biblioteca)

def DecoradorMayusculas(funcion):
    """
        Decorador:
            Este decorador toma una función como argumento (en este caso la función Buscar)
            y devuelve una nueva función que modifica el comportamiento de la función original. 
            Convierte el título del libro a mayúsculas antes de pasarlo a la función original. 

        Parámetros:
            funcion : La función que se va a decorar. Debe aceptar un argumento de tipo str.

        Retorno:
            La función decorada que toma un título en minúsculas o una mezcla de mayúsculas 
            y minúsculas y lo convierte a mayúsculas antes de invocar la función original.
    """
    def wrapper(titulo):
        tituloMAYUSCULAS = titulo.upper()
        return funcion(tituloMAYUSCULAS)
    return wrapper

@DecoradorMayusculas
def BuscarLibroEnMayusculas(titulo):
    """
        Función BuscarLibroEnMayusculas:
            Esta función utiliza el decorador `DecoradorMayusculas` para convertir el título del libro
            a mayúsculas antes de pasarlo a la función `Buscar`. Esto asegura que la búsqueda sea
            insensible a las variaciones de mayúsculas y minúsculas en el título.

        Parámetros:
            titulo : El título del libro a buscar. Puede estar en cualquier combinación de mayúsculas y minúsculas.

        Retorno:
            La función no retorna ningún valor, pero llama a la función `Buscar` para realizar la búsqueda.
    """
    Buscar(titulo)

#* Ejecuciones para comprobar funcionamiento.
print("\n")
Registrar("Cien Años de Soledad", "Gabriel García Márquez", 1967, "Novela")
Registrar("Harry Potter y la piedra filosofal", "J.K. Rowling", 1997, "Fantasía")
Registrar("Klara y el sol", "Kazuo Ishiguro", 2021, "Ciencia ficción")

Buscar("El Quijote")  # Este libro no está, así que veremos el mensaje de error.

print("\n > La edad del libro de 1967 es: ", Edad_libro(1967), "\n")

Categorias("Novela")

print(f"\n > Total de libros registrados: {ContarLibros()}.")

BuscarLibroEnMayusculas("cien años de soledad")
print("\n")
