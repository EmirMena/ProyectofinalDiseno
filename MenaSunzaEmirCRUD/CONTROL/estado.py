
# Clase estado base
class Estado:
    def __init__(self, contexto, controlDatos,GUI):
        self.GUI= GUI 
        self.controlDatos = controlDatos
        self.contexto = contexto
    def realizarAccion(self,textoAIngresar="",ClienteElegido= None, Cuenta=None):
        pass

# Estado esperar
class EstadoEsperar(Estado):
    def realizarAccion(self):
        self.GUI.ventanaEsperar()
# Estado insertar clientes
class EstadoInsertar(Estado):
    def realizarAccion(self):
        self.GUI.ventanaInsertar()
        textoAIngresar= self.GUI.getNuevoRegistro()
        self.controlDatos.leerRegistro()
        self.controlDatos.agregarRegistro(textoAIngresar)
       
# Estado imprimir clientes
class EstadoImprimir(Estado):
    def realizarAccion(self):
        self.controlDatos.leerRegistro()
        self.texto = self.controlDatos.getRegistro()
        self.GUI.setTextosInfo(self.texto)
        self.GUI.ventanaImprimir()
        #self.contexto.cambiarEstado(EstadoEsperar(self.contexto, self.controlDatos))
# Estado ver clientes
class EstadoVerCliente(Estado):
    def realizarAccion(self, ClienteElegido):
        cuentas = self.controlDatos.getDatosCliente(ClienteElegido)
        self.GUI.setCuentasInfo(cuentas)
        self.GUI.ventanaCliente(ClienteElegido)
        #self.contexto.cambiarEstado(EstdoEsperar(self.contexto, self.controlDatos))
class EstadoVerCuenta(Estado):
    def realizarAccion(self, ClienteElegido, Cuenta):
        self.GUI.ventanaCuenta(ClienteElegido,Cuenta)
class EstadoBorrarCuenta(Estado):
    def realizarAccion(self, ClienteElegido, Cuenta):
        self.controlDatos.borrarCuenta(ClienteElegido, Cuenta)     
# Estado eliminar clientes
class EstadoModificar(Estado):
    def realizarAccion(self):
        self.controlDatos.leerRegistro()
        self.texto = self.controlDatos.getClientesInfo()
        self.clientes = self.controlDatos.getClientes()
        self.GUI.setTextosInfo(self.texto)
        self.GUI.setObjetosInfo(self.clientes)
        self.GUI.ventanaModificar()
        #self.contexto.cambiarEstado(EstadoEsperar(self.contexto, self.controlDatos))


