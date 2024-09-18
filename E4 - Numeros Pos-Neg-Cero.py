#Determinar si un número ingresado por el usuario es positivo, negativo o cero.

numero = float(input(" > Ingrese un numero: "))

if numero > 0:
    print(" > El numero es positivo")
elif numero < 0:
    print(" > El numero es negativo")
elif numero == 0:
    print(" > El numero es cero")
