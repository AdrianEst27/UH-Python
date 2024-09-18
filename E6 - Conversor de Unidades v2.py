from pint import UnitRegistry, DimensionalityError

ureg = UnitRegistry()

print(' > C O N V E R S O R  D E  U N I D A D E S <')

while True:
    try:
        unidad_entrada = input(" > Ingrese la unidad de entrada (ej: m, cm, in, g, kg, degC, degF, day, h, s, min): ")
        unidad_salida = input(" > Ingrese la unidad de salida (ej: m, cm, in, g, kg, degC, degF, day, h, s, min): ")
        valor = float(input(" > Ingrese el valor a convertir: "))

        resultado = valor * ureg(unidad_entrada).to(unidad_salida)

        print(f" > {valor} {unidad_entrada} equivalen a {resultado:.2f} {unidad_salida}")
        break
    except ValueError:
        print(" > Por favor, ingrese un valor numérico válido.")
    except DimensionalityError:
        print(" > Las unidades ingresadas no son compatibles.")