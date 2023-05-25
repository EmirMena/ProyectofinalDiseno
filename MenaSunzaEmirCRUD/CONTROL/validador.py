import re

class Validador:
    REGEXP = "^[0-9]+,([a-zA-Z]+[ ]?){1,2},[0-9]{16},[0-9]+$"

    def validarExistencia(self, indice, nombre, cuenta, saldo, clientes):
        for cliente in clientes:
            if cliente.getNombre() == nombre:
                return cliente
        return None
    """""
    def validarIndiceUnico(self, indice, clientes):
        for cliente in clientes:
            if indice == cliente.getIndice():
                return False
        return True
    """

    def validarNombreExistencia(self, nombre, cliente):
        if nombre == cliente.getNombre():
            return True
        return False

    def validarCuentaExistencia(self, cuenta, clientes):
        for cliente in clientes:
            for cuenta_cliente in cliente.getCuentas():
                if cuenta_cliente.getNumero() == cuenta:
                    return True
        return False

    def validarEntradaRegistroAgregar(self, indice="0", nombre="Nombre Defecto", cuenta="0000000000000000", saldo="00"):
        string = f"{indice},{nombre},{cuenta},{saldo}"
        if re.match(self.REGEXP, string) is not None:
            return True
        else:
            return False
        
    def validarCuentaEnCero(self,cuenta):
        if cuenta.getSaldo() <= 0.0:
            return True