class Perro:
    # Atributos
    def __init__(self, nombre, raza):
        self.nombre = nombre
        self.raza = raza

    # Metodos
    def ladrar(self):
        print("¡GUAU!")

    def presentar(self):
        print(f"¡Hola! Soy {self.nombre} y soy un {self.raza}.")

# Crear instancias de la clase Perro
mi_perro = Perro("Fido", "Labrador")
otro_perro = Perro("Luna", "Pastor Alemán")
otro_perro_mas = Perro("Charro", "Chihuahua")

# Acceder a atributos y métodos
print(mi_perro.nombre)
mi_perro.ladrar()
Perro.presentar(otro_perro)
Perro.presentar(otro_perro_mas)