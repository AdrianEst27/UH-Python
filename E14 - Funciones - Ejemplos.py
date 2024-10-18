#TODO: Tipos de funciones en python. Categorizadas por complejidad.

#* Función nivel 1: Definición básica.
"""
?   Esta es la función más simple, que no toma argumentos 
?   y siempre devuelve la cadena "Hello, World!".
"""
def greet():
    return "Hello, World!"

#* Función nivel 2: Función con argumentos.
"""
?   Esta función toma un argumento name y devuelve un saludo 
?   personalizado en la forma "Hello, {name}!".
"""
def greet(name):
    return f"Hello, {name}!"

#* Función nivel 3: Función con argumentos y valores.
"""
?   Similar a la anterior, pero name tiene un valor predeterminado de "World". 
?   Si no se proporciona ningún argumento, la función devolverá "Hello, World!".
"""
def greet(name="World"):
    return f"Hello, {name}!"

#* Función nivel 4: Función con argumentos de longitud variable.
"""
?   Esta función acepta un número variable de argumentos (cualquier cantidad de nombres) 
?   y devuelve un saludo para todos los nombres proporcionados, concatenando cada uno en un solo string.
"""
def greet(*names):
    return "Hello, " + ", ".join(names) + "!"

#* Función nivel 5: Función que regresa multiples valores.
"""
?   Esta función toma dos argumentos, a y b, y calcula la división entera (cociente)
?   y el residuo de a dividido por b, devolviendo ambos como una tupla
"""
def divide(a, b):
    cociente = a // b
    residuo = a % b
    return cociente, residuo

#* Función nivel 6: Funciones de primera clase.
"""
?   La función apply_function toma otra función (func) y un valor, 
?   y aplica esa función al valor dado. En este caso, se aplica la función square, 
?   que calcula el cuadrado del número, al valor 5, resultando en 25.
"""
def apply_function(func, value):
    return func(value)

def square(x):
    return x * x

result = apply_function(square, 5)

#* Función nivel 7: Funciones Lambda.
"""
?   Aquí se utiliza una función lambda (una función anónima) que también calcula el cuadrado de un número. 
?   Se pasa directamente a la función apply_function, aplicándola al valor 5, resultando nuevamente en 25.
"""
def apply_function(func, value):
    return func(value)

result = apply_function(lambda x: x * x, 5)

#* Función nivel 8: Decoradores.
"""
?   Este código define un decorador que envuelve otra función, en este caso greet. 
?   El decorador imprime un mensaje antes y después de la ejecución de la función envuelta. 
?   Cuando se llama a greet, se verá el mensaje "Before the function" antes del saludo y "After the function" después.
"""
def decorator(func):
    def wrapper(*args, **kwargs):
        print("Before the function")
        result = func(*args, **kwargs)
        print("After the function")
        return result
    return wrapper

@decorator
def greet(name):
    return f"Hello, {name}!"

greet("World")