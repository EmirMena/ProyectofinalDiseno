import customtkinter as ctk
from PIL import ImageTk, Image
from MODELO.banco import Banco
from MODELO.cuenta import Cuenta
from MODELO.cliente import Cliente

class GUI2:
    def __init__(self):
        self.window = None
        self.banco = None 
        self.textosInfo=[]
        self.textoIngresado=""

    def setContexto(self,contexto):
        self.banco = contexto
        self.banco.peticionEsperar()

    def crearVentana(self, title):
        self.window = ctk.CTk()
        self.window.geometry("1280x720")
        self.window.title(title)
        self.font = ctk.CTkFont(family="Bahnschrift light", size=55)
        self.frame = ctk.CTkFrame(master=self.window, fg_color="#1B112C")
        self.frame.pack(pady=10, padx=10, fill="both", expand=True)
        self.label = ctk.CTkLabel(master=self.frame, text=title, font=self.font, bg_color="transparent", text_color="#DD8D9F")
        self.label.pack(pady=12, padx=0)
        self.contentFrame = ctk.CTkFrame(master=self.frame, fg_color="#731F7A")
        self.contentFrame.pack(pady=12, padx=0)
        

    def ventanaEsperar(self):
        if self.window != None:
            self.window.destroy()
        self.crearVentana("Ventana Esperar")

        agregar_image = ctk.CTkImage(Image.open("./MenaSunzaEmirCRUD/VISTA/Agregar.jpeg"), size=(426, 500))
        imprimir_image = ctk.CTkImage(Image.open("./MenaSunzaEmirCRUD/VISTA/Imprimir.jpeg"), size=(426, 500))
        eliminar_image = ctk.CTkImage(Image.open("./MenaSunzaEmirCRUD/VISTA/Eliminar.jpeg"), size=(426, 500))

        botonImprimir = ctk.CTkButton(master=self.contentFrame, image=imprimir_image,fg_color="#731F7A", bg_color="transparent", hover_color="#6B9BCF",command=self.banco.peticionImprimir, text="", corner_radius=0)
        botonImprimir.pack(side="left", padx=0)
        botonInsertar = ctk.CTkButton(master=self.contentFrame, image=agregar_image, fg_color="#731F7A",hover_color="#6B9BCF", bg_color="transparent",command=self.banco.peticionInsertar, text="", corner_radius=0)
        botonInsertar.pack(side="left", padx=0)
        botonEliminar = ctk.CTkButton(master=self.contentFrame, image=eliminar_image, fg_color="#731F7A",hover_color="#6B9BCF", bg_color="transparent",command=self.banco.peticionModificar, text="", corner_radius=0)
        botonEliminar.pack(side="left", padx=0)

        self.window.mainloop()
    def ventanaImprimir(self):
        self.window.destroy()
        self.crearVentana("Imprimir Base De Datos")
        #Creamos la lista de clientes y cuentas
        contador=0
        caracteresInutiles= "(){}''"
        tabla= str.maketrans("","", caracteresInutiles)
        self.font = ctk.CTkFont(family="Bahnschrift light", size=20)
        for texto in self.textosInfo:
            botonLista=ctk.CTkButton(
                master=self.contentFrame,
                text= str(texto).translate(tabla),
                font=self.font,
                corner_radius=0,
                fg_color="#544C70",
                text_color="#6EBDEA",
                hover_color="#544C70",
                height=30,width=180)
            botonLista.grid(row=contador//3,column=contador%3,padx=10,pady=5)
            contador +=1

        #Boton para salir
        botonSalir= ctk.CTkButton(master=self.contentFrame,fg_color="#2A143D",hover_color="#1B112C",bg_color="transparent", text="VOLVER",command=self.banco.peticionEsperar)
        botonSalir.grid(column=0, padx=0, pady=20)

        self.window.mainloop()
    def ventanaInsertar(self):
        self.window.destroy()
        self.crearVentana("Insertar Nuevo Cliente")

        # Creamos el frame para la insercion
        insercionFrame = ctk.CTkFrame(master=self.contentFrame, bg_color="#5B5F90",fg_color="#544C70",width=120,height=40)
        insercionFrame.pack(padx=15,pady=20)

        #NUEVAS ENTRADAS
        self.nuevaEntradaIndice= ctk.CTkEntry(master=insercionFrame,width=50, placeholder_text="00")
        self.nuevaEntradaIndice.pack(side="left",padx=10, pady=20)
        self.nuevaEntradaNombre= ctk.CTkEntry(master=insercionFrame,width=150,placeholder_text="Pedro Espinacas")
        self.nuevaEntradaNombre.pack(side="left",padx=10)
        self.nuevaEntradaCuenta= ctk.CTkEntry(master=insercionFrame,width=300, placeholder_text="0011223344556677")
        self.nuevaEntradaCuenta.pack(side="left",padx=10)
        self.nuevaEntradaSaldo= ctk.CTkEntry(master=insercionFrame,width=80,placeholder_text="100")
        self.nuevaEntradaSaldo.pack(side="left",padx=10)
        def wrapper():
            indice=(self.nuevaEntradaIndice.get())
            nombre=(self.nuevaEntradaNombre.get())
            cuenta=(self.nuevaEntradaCuenta.get())
            saldo=(self.nuevaEntradaSaldo.get())
            self.nuevoRegistro = indice + ", "+nombre +", "+ cuenta + ", "+saldo
            self.banco.peticionRealizarAccion()


        botonFrame = ctk.CTkFrame(master=self.contentFrame, bg_color="transparent",fg_color="transparent")
        botonFrame.pack(side="bottom", pady=0,padx=0)
        #boton entrada
        botonFrameEntrada = ctk.CTkFrame(master=self.contentFrame, bg_color="#5B5F90",fg_color="#544C70")
        botonFrameEntrada.pack(side="top", pady=0)
        botonEntrada= ctk.CTkButton(master=botonFrameEntrada,fg_color="#731F7A",hover_color="#6B9BCF",
                                    bg_color="transparent", text="Ingresar", command=wrapper)
        botonEntrada.pack(side="left", padx=0, pady=0)

        #Boton para salir
        botonSalir= ctk.CTkButton(master=botonFrame,fg_color="#2A143D",hover_color="#1B112C",
                                    bg_color="transparent", text="VOLVER",command=self.banco.peticionEsperar)
        botonSalir.pack(side="bottom", pady=25)

        self.window.mainloop()
    def ventanaModificar(self):
        self.window.destroy()
        self.crearVentana("Ventana Modificar Clientes")

        # Creamos el frame para la lista
        listaFrame = ctk.CTkFrame(master=self.contentFrame, bg_color="#2A143D",fg_color="#544C70")
        listaFrame.pack(pady=12, padx=20)
        self.font = ctk.CTkFont(family="Bahnschrift light", size=20)
        contador=0
        caracteresInutiles= "(){}''"
        tabla= str.maketrans("","", caracteresInutiles)
        for objeto, texto in zip(self.objetosInfo, self.textosInfo):
            botonLista = ctk.CTkButton(
            master=listaFrame,
            text=str(texto).translate(tabla),
            font=self.font,
            corner_radius=0,
            fg_color="#544C70",
            text_color="#6EBDEA",
            hover_color="#9E2083",
            height=30,
            width=180,
            command=lambda cliente=objeto: self.banco.peticionVerCliente(cliente)
            )
            botonLista.grid(row=contador // 3, column=contador % 3, padx=10, pady=5)
            contador += 1
         #Boton para salir
        botonSalir= ctk.CTkButton(master=listaFrame,fg_color="#2A143D",hover_color="#1B112C",
                                    bg_color="transparent", text="VOLVER",command=self.banco.peticionEsperar)
        botonSalir.grid(column=0, padx=0, pady=20)


        self.window.mainloop()
    def ventanaCliente(self,cliente):
        #self.banco.peticionVerCliente(cliente)
        self.window.destroy()
        self.crearVentana(str(cliente.getNombre()))
        #self.crearVentana(str(self.textosInfo[1][1]).strip("()"))
        listaFrame = ctk.CTkFrame(master=self.contentFrame, bg_color="#2A143D",fg_color="#544C70")
        listaFrame.pack(pady=12, padx=20)
        self.font = ctk.CTkFont(family="Bahnschrift light", size=20)
        contador=0
        for i in range(2,len(self.cuentasInfo)):
            for j in range(0,len(self.cuentasInfo[i])):
                cuenta=self.cuentasInfo[i][j]
                botonLista = ctk.CTkButton(
                master=listaFrame,
                text=str(cuenta.getNumero())+": $"+ str(cuenta.getSaldo()),
                font=self.font,
                corner_radius=0,
                fg_color="#544C70",
                text_color="#6EBDEA",
                hover_color="#9E2083",
                height=30,
                width=180,
                command=lambda cuentaElegida=cuenta: self.banco.peticionVerCuenta(cliente,cuentaElegida)
                )
                botonLista.grid(row=contador // 1, column=contador % 1, padx=10, pady=5)
                contador += 1

        #Boton para salir
        botonSalir= ctk.CTkButton(master=listaFrame,fg_color="#2A143D",hover_color="#1B112C",
                                    bg_color="transparent", text="VOLVER",command=self.banco.peticionModificar)
        botonSalir.grid(column=0, padx=0, pady=20)
        self.window.mainloop()

    def ventanaCuenta(self,cliente,cuentaElegida):
        #self.banco.peticionVerCuenta(cuentaElegida)
        self.window.destroy()
        self.crearVentana(str(cuentaElegida.getNumero()))
        listaFrame = ctk.CTkFrame(master=self.contentFrame, bg_color="#2A143D",fg_color="#544C70")
        listaFrame.pack(pady=12, padx=20)
        self.font = ctk.CTkFont(family="Bahnschrift light", size=20)

        def wrapper():
            self.banco.peticionBorrarCuenta(cliente, cuentaElegida)

        botonEliminar = ctk.CTkButton(master=listaFrame, fg_color="#731F7A", bg_color="transparent", hover_color="#6B9BCF",
                                      command=wrapper, text="EliminarCuenta", corner_radius=0)
        botonEliminar.pack(side="left", padx=0)

        #Boton para salir
        botonSalir= ctk.CTkButton(master=listaFrame,fg_color="#2A143D",hover_color="#1B112C",
                                    bg_color="transparent", text="VOLVER",command=self.banco.peticionModificar)
        botonSalir.pack(padx=0, pady=20)

        self.window.mainloop()

    def setCuentasInfo(self,listaCuentas):
        self.cuentasInfo=listaCuentas
    def setTextosInfo(self, lista):
        self.textosInfo=lista
    def setObjetosInfo(self,listaObjeto):
        self.objetosInfo= listaObjeto
    def getTextoIngresado(self):
        return self.textoIngresado
    def botonAccion(self):
        indice=(self.nuevaEntradaIndice.get())
        nombre=(self.nuevaEntradaNombre.get())
        cuenta=(self.nuevaEntradaCuenta.get())
        saldo=(self.nuevaEntradaSaldo.get())
        self.nuevoRegistro = indice + ", "+nombre +", "+ cuenta + ", "+saldo
        self.banco.peticionRealizarAccion()
    def getNuevoRegistro(self):
        return self.nuevoRegistro