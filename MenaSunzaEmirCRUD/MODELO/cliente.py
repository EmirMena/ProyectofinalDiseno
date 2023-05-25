from MODELO.cuenta import Cuenta
class Cliente():
    def __init__(self, datos):
        self.indice = datos[0].strip()
        self.nombre = datos[1].strip()
        self.cuenta = []  # Crear una lista vacía para las cuentas
        self.agregarCuenta(datos[2].strip(), datos[3].strip())  # Agregar la primera cuenta al crear el objeto

    def agregarCuenta(self, numero, saldo):
        self.cuenta.append(Cuenta(numero, saldo))

    def getCuentas(self):
        return self.cuenta

    def getIndice(self):
        return self.indice

    def getNombre(self):
        return self.nombre