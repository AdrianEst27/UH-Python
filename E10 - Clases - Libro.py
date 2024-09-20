class Libro:
    def __init__(self, titulo, autor, paginas):
        self.titulo = titulo
        self.autor = autor
        self.paginas = paginas

MiLibro = Libro("El Libro Troll", "ElRubius", 504)
OtroLibro = Libro("La Biblia", "Dios", 1800000)

print(f"\n > Mi Libro {MiLibro.titulo} del autor {MiLibro.autor}, tiene {MiLibro.paginas} páginas.")
print(f" > Mi otro libro {OtroLibro.titulo} del autor {OtroLibro.autor}, tiene {OtroLibro.paginas} paginas.")