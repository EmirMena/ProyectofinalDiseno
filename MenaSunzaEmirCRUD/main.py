from MODELO.banco import Banco
from VISTA.gui import GUI2

# Crear una instancia delm banco y la interfaz GUI
gui = GUI2()
banco = Banco(gui)
gui.setContexto(banco)
