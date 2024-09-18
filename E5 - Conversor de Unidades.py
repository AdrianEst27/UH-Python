from pint import UnitRegistry

ureg = UnitRegistry()

# Definir cantidades con unidades
distancia = ureg.kilometer
tiempo = 30 * ureg.minute

# Realizar conversiones
distancia_en_metros = distancia.to(ureg.meter)
tiempo_en_segundos = tiempo.to(ureg.second)

# Realizar cálculos con unidades
velocidad = distancia / tiempo

print(f' >Distancia: {distancia}')
print(f' > Distancia en metros: {distancia_en_metros}')
print(f' > Tiempo: {tiempo}')
print(f' > Tiempo en segundos: {tiempo_en_segundos}')
print(f' > Velocidad: {velocidad}')