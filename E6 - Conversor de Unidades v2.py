import pint
from pint import UnitRegistry

ureg = UnitRegistry()

def convertir_unidad(valor, unidades_validas, tipo_conversion):
    try:
        unientrada = input(f" > Ingrese la unidad de entrada {unidades_validas}: ").strip()
        unisalida = input(f" > Ingrese la unidad de salida {unidades_validas}: ").strip()

        entrada = valor * ureg(unientrada)
        resultado = entrada.to(unisalida)

        print(f" > {valor} {unientrada} equivalen a {resultado:.2f} {unisalida}")
    except (KeyError, ValueError):
        print(" > Las unidades ingresadas no son compatibles.")


# Funciones específicas para cada tipo
def Longitud(valor):
    convertir_unidad(valor, "(m, cm, mm, km, in, ft, yd, mi)", "longitud")


def Temperatura(valor):
    try:
        unientrada = input(" > Ingrese la unidad de entrada (degC, degF, K): ").strip()
        unisalida = input(" > Ingrese la unidad de salida (degC, degF, K): ").strip()

        # Usamos ureg.Quantity para manejar el valor y la unidad de entrada
        entrada = ureg.Quantity(valor, unientrada)

        # Convertimos directamente con .to
        resultado = entrada.to(unisalida)

        print(f" > {valor} {unientrada} equivalen a {resultado:.2f} {unisalida}")
    except pint.errors.DimensionalityError:
        print(" > Las unidades de temperatura no son compatibles.")
    except (ValueError, KeyError):
        print(" > Las unidades ingresadas no son válidas.")


def Masa(valor):
    convertir_unidad(valor, "(g, kg, oz, lb)", "masa")


def Tiempo(valor):
    convertir_unidad(valor, "(s, min, h, day, year)", "tiempo")


# El main
print(' > C O N V E R S O R  D E  U N I D A D E S <')

while True:
    try:
        valor = float(input(' > Ingrese el valor a convertir: '))

        print(' 1. Longitud')
        print(' 2. Temperatura')
        print(' 3. Masa')
        print(' 4. Tiempo')
        print(' 5. SALIR')

        op = int(input(' > Seleccione una opción: '))

        if op == 1:
            Longitud(valor)
        elif op == 2:
            Temperatura(valor)
        elif op == 3:
            Masa(valor)
        elif op == 4:
            Tiempo(valor)
        elif op == 5:
            print(" > Saliendo del programa.")
            break
        else:
            print(" > Opción inválida. Intente de nuevo.")
    except ValueError:
        print(' > Por favor, ingrese un valor numérico válido.')
