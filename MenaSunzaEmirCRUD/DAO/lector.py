from MODELO.cliente import Cliente
from MODELO.cuenta import Cuenta
from CONTROL.validador import Validador
class Lector():
    __arregloLinea=[]
    __datoCliente=[]
    __datoClienteAux=[]
    __cliente=[]
    
    def __init__(self):
        self.validador = Validador()  # Crear una instancia de Validador
    
    def leerArchivo(self):
        try:
            archivo = open("./MenaSunzaEmirCRUD/DAO/BaseDatos.txt", "rt", encoding="utf-8")
            for linea in archivo:
                self.__arregloLinea.append(linea.strip())  # Utilizar strip() para eliminar los espacios en blanco y el salto de línea
            archivo.close()
        except FileNotFoundError:
            print("Error: el archivo no ha sido encontrado")
    
    def crearCliente(self):
        self.__datoCliente.clear()
        self.__datoClienteAux.clear()
        self.__cliente.clear()
        
        for row in self.__arregloLinea:
            self.__datoCliente.append(row.split(","))
        
        for i in self.__datoCliente:
            if i[0] in self.__datoClienteAux:
                cliente_existente = self.validador.validarExistencia(i[0].strip(), i[1].strip(), i[2].strip(), i[3].strip(), self.__cliente)
                if cliente_existente is not None:
                    cuenta_existente = False
                    for cuenta in cliente_existente.getCuentas():
                        if cuenta.getNumero() == i[2].strip() and cuenta.getSaldo() == float(i[3].strip()):
                            cuenta_existente = True
                            break
                    if not cuenta_existente:
                        cliente_existente.agregarCuenta(i[2].strip(), i[3].strip())
            else:
                self.__cliente.append(Cliente(i))
                self.__datoClienteAux.append(i[0])
    
    def buscarCliente(self, indice):
        for i in self.__cliente:
            if i.indice == str(indice):
                return i
    
    def getClientes(self):
        return self.__cliente
    