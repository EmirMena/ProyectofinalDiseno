from CONTROL.estado import *
# Clase contexto
class Banco:
    def __init__(self,GUI):
        #Estado inicial del programa
        self.controlador=ControladorDatos()
        #self.infoObjetos=[]
        self.GUI = GUI 

    #ESTABLECER LOS ESTADOS
    def peticionImprimir(self):
        self.cambiarEstado(EstadoImprimir(self,self.controlador,self.GUI))
        self.estado.realizarAccion()

    def peticionModificar(self):
        self.cambiarEstado(EstadoModificar(self,self.controlador,self.GUI))
        self.estado.realizarAccion()

    def peticionVerCliente(self,Cliente):
        self.cambiarEstado(EstadoVerCliente(self,self.controlador,self.GUI))
        self.estado.realizarAccion(Cliente)

    def peticionInsertar(self):
        self.cambiarEstado(EstadoInsertar(self,self.controlador,self.GUI))
        self.estado.realizarAccion()
        #self.estado.realizarAccion()
    def peticionVerCuenta(self,cliente,cuenta):
        self.cambiarEstado(EstadoVerCuenta(self,self.controlador,self.GUI))
        self.estado.realizarAccion(cliente,cuenta)
    def peticionRealizarAccion(self):
        self.estado.realizarAccion()
    def peticionEsperar(self):
        self.cambiarEstado(EstadoEsperar(self,self.controlador,self.GUI))
        self.estado.realizarAccion()

    def peticionBorrarCuenta(self,cliente,cuenta):
        self.cambiarEstado(EstadoBorrarCuenta(self,self.controlador,self.GUI))
        self.estado.realizarAccion(cliente,cuenta)
    def cambiarEstado(self, nuevoEstado):
        self.estado = nuevoEstado
    

#------------------------------------------------------------------------------------------------------------------------------------
#------------------------------------------------------------------------------------------------------------------------------------
#------------------------------------------------------------------------------------------------------------------------------------
#------------------------------------------------------------------------------------------------------------------------------------
#funciones necesarias---------------------------------------------------------------------------------------------------------------------------------------
from DAO.escritor import Escritor
from DAO.lector import Lector
from CONTROL.validador import Validador
from MODELO.cliente import Cliente
from MODELO.cuenta import Cuenta

class ControladorDatos():
    def __init__(self):
        self.escritor = Escritor()
        self.lector = Lector()
        self.validador = Validador()
        self.__clientes = []  # Lista de clientes
        self.clienteInfo= []

    def leerRegistro(self):
        # Indica al lector que devuelva los datos convertidos de texto al controlador para poder trabajarlos
        self.lector.leerArchivo()
        self.lector.crearCliente()
        self.__clientes.clear()  # Reiniciar la lista de clientes
        self.__clientes.extend(self.lector.getClientes())  # Agregar los nuevos clientes a la lista

    def getRegistro(self):
        registro = []
        for cliente in self.__clientes:
            cliente_info = (cliente.getIndice(), cliente.getNombre())
            self.clienteInfo.append(cliente_info)
            for cuenta in cliente.getCuentas():
                cuenta_info = (cuenta.getNumero(), cuenta.getSaldo())
                registro.append((cliente_info, cuenta_info))
        return tuple(registro)
    
    def agregarRegistro(self, datos):
        indice,nombre,cuenta,saldo= datos.split(", ")
        # Valida si la entrada dada es correcta y cumple con los parámetros para agregar el registro correspondiente
        if self.validador.validarEntradaRegistroAgregar(indice, nombre, cuenta, saldo):
            # Valida si el índice y nombre del cliente existen
            cliente_existente = self.validador.validarExistencia(indice, nombre, cuenta, saldo, self.__clientes)

            if cliente_existente is not None:
                self.agregarCuenta(cliente_existente, cuenta, saldo)
            else:
                # Valida si la cuenta que desea ingresar ya existe
                if self.validador.validarCuentaExistencia(cuenta, self.__clientes):
                    raise Exception("La cuenta ya existe.")
                else:
                    self.agregarCliente(indice, nombre, cuenta, saldo)
                    self.guardarCambiosRegistro()
        else:
            raise Exception("Verifique la entrada")

    def guardarCambiosRegistro(self):
        #guarda en el archivo los cambios a los clientes y cuentas realizados sobreescribiendo el archivo (ESTE METODO SE UTILIZA ANTES DE FINALIZAR EL PROGRAMA)
        nuevosDatos=[]
        for cliente in self.__clientes:
            for cuenta in cliente.getCuentas():
                entradaNueva = [cliente.getIndice(),cliente.getNombre(),cuenta.getNumero(),cuenta.getSaldo()]
                cadenaNueva = str(entradaNueva).replace("[", "").replace("]", "").replace("'", "") + "\n"
                nuevosDatos.append(cadenaNueva)
        self.escritor.guardarDatos(nuevosDatos)
        print("Base Actualizada")

    def borrarCuenta(self,cliente,cuentaABorrar):
        cuentaEncontrada = False
        if self.validador.validarCuentaEnCero(cuentaABorrar):
            for clienteActual in self.__clientes:
                if clienteActual == cliente:
                    cuentas = clienteActual.getCuentas()
                    for cuenta in cuentas:
                        if cuenta.getNumero() == cuentaABorrar.getNumero():
                            cuentas.remove(cuenta)
                            cuentaEncontrada = True
                            break
                    break
        if cuentaEncontrada:
            self.guardarCambiosRegistro()
            print("Cuenta eliminada exitosamente.")
        else:
            print("No fue posible eliminar la cuenta.")

    def agregarCuenta(self, cliente, numero, saldo):
        cliente.getCuentas().append(Cuenta(numero,saldo))
    def agregarCliente(self, indice, nombre, cuenta, saldo):
        datos= (indice, nombre, cuenta, saldo)
        self.__clientes.append(Cliente(datos))
    def getDatosCliente(self,Cliente):
        datos= (Cliente.getIndice(), Cliente.getNombre(), Cliente.getCuentas())
        return datos
    def getClientesInfo(self):
        self.getRegistro()
        return self.clienteInfo
    def getClientes(self):
        return self.__clientes
    