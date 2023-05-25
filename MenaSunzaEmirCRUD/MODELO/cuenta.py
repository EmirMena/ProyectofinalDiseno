class Cuenta():
    def __init__(self,numero,saldo):
        self.numero = numero
        self.saldo = float(saldo)
    def getSaldo(self):
        return self.saldo
    def getNumero(self):
        return self.numero