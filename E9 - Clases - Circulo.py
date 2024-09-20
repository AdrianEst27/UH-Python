import math

class Circulo:
    def __init__(self, r):
        self.r = r
    def area(self):
        return self.r*self.r

    def circunferencia(self):
        return self.r*2*math.pi

MiCirculo = Circulo(7)
area = MiCirculo.area()
circunferencia = MiCirculo.circunferencia()

print(f" > El área del circulo es: {area}")
print(f" > La circunferencia es: {circunferencia}")
