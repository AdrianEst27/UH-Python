# Pedir al usuario su nombre y edad y mostrar un mensaje

nombre = input(" > Ingrese su nombre: ")

"""
edad = int(input(" > Ingrese su edad: "))

print(" > Hola ", nombre, " tienes ", edad, " años.")
if edad <= 18:
    print(" > Eres menor de edad.")
else:
    print(" > Eres mayor de edad.")
"""

while True:
    try:
        edad = int(input(" > Ingrese su edad: "))
        if edad > 0:
            break
        else:
            print(" > Ingrese valor correcto.")
    except ValueError:
        print(" > Por favor, ingrese un numero entero válido para la edad. ")