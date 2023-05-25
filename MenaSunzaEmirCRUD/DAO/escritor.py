from MODELO.cliente import Cliente
class Escritor():
    def __init__(self):
        pass
    def guardarDatos(self, datos):
        archivo = open("./MenaSunzaEmirCRUD/DAO/BaseDatos.txt","w",encoding="utf-8")
        for i in datos:
            archivo.write(i)
        archivo.close()