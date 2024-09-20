class Cuenta:
    def __init__(self, titular, cuenta, saldo):
        self.titular = titular
        self.cuenta = cuenta
        self.saldo = saldo

    def consultar(self):
        return self.saldo
    def depositar(self, saldo):
        self.saldo += saldo
    def retirar(self, saldo):
        self.saldo -= saldo

MiCuenta = Cuenta("Adrián", "001jase", 50)

print("\n > Consultar <")
print(f" > Su cuenta a nombre de {MiCuenta.titular}, con el numero de cuenta {MiCuenta.cuenta}, tiene un saldo de ${MiCuenta.saldo}")

print("\n > Depositar <")
MiCuenta.depositar(100)
print(f" > Ahora su saldo es: ${MiCuenta.saldo}")

print("\n > Retirar <")
MiCuenta.retirar(50)
print(f" > Ahora su saldo es: ${MiCuenta.saldo}")