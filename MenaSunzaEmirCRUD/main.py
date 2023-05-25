from MODELO.banco import Banco
from VISTA.gui import GUI2

#NOTA
"""""
Mi programa tiene un fallo que se originó al intentar agregarle(erroneamente) una interfaz gráfica,
el problema consiste en que la ventana insertar y eliminar debe ser cerrada para que se guarden
correctamente los datos, es decir, de no hacerlo se presenta un fallo en la escritura que no he sido
capaz de corregir en el plazo dado, sin embargo el programa funciona correctamente en la implementacion del PD-2 

Una disculpa enorme, Emir.
"""
# Crear una instancia delm banco y la interfaz GUI
gui = GUI2()
banco = Banco(gui)
gui.setContexto(banco)
