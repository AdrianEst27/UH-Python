# TODO 1: Crea una lista que contenga los cuadrados de los números del 1 al 20 

Cuadrado = [x**2 for x in range(21)]
print(Cuadrado)

# TODO 2: Crea una lista que contenga solo los números pares del 1 al 50

Pares = [x for x in range(50) if(x % 2 == 0)]
print(Pares)

# TODO 3: Dada una lista de cadenas, crea una nueva lista con todas las cadenas en minúsculas

cadenas = ["CHALINO", "ADRIAN", "PULSAR", "BURGUER"]
minusculas = [cadena.lower() for cadena in cadenas]
print(minusculas)

# TODO 4: Dada una lista de diccionarios que representan estudiantes con sus nombres y calificaciones, 
# TODO 4: usa comprensiones de listas para crear una lista de nombres de estudiantes que tiene una calificación mayor de 70

estudiantes = [
    {"Nombre": "Adrian", "Calificacion": 97},
    {"Nombre": "Angel", "Calificacion": 80},
    {"Nombre": "Diana", "Calificacion": 90},
    {"Nombre": "Mauricio", "Calificacion": 84},
    {"Nombre": "Juan", "Calificacion": 70},
    {"Nombre": "Matias", "Calificacion": 50}
]

ListaEstudiantes = [estudiante["Nombre"] for estudiante in estudiantes if estudiante["Calificacion"] > 70]
print(ListaEstudiantes)

