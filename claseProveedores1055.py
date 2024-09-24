class Proveedores1055():
    Id_proveedores = ""
    NombreProveedor = ""
    Horarios = ""
    Email = ""
    Celular = 0
    Tipo = ""
    Tiempo_Entrega = ""

    def mostrarDatos(self,a,b,c,d,e,f,g):
        print("---DATOS---")
        print(f"Id: {a}")
        print(f"Nombre proveedor: {b}")
        print(f"Horario: {c}")
        print(f"Email: {d}")
        print(f"Celular: {e}")
        print(f"Tipo: {f}")
        print(f"Tiempo entrega: {g}")
        print("")


    def listaNombreProveedores(self):
        print("---LISTA---")
        lista_proveedores = ["Walmart", "Provete45", "Adolumin", "Provt6", "Provecias"]
        for x in lista_proveedores:
            print(x)
        print("")

    def tupla_EmailProveedroes(self):
        print("---TUPLA---")
        tupla_nombre = ("abc@gmail.com", "awaefc@gmail.com", "awefc@gmail.com", "awetra@gmail.com", "awefwef@gmail.com")
        for x in tupla_nombre:
            print(x)
        print("")

    def diccionario_horarios(self):
        print("---DICCIONARIO---")
        diccionario_Horarios = {
            "Lunes": "9am - 8pm",
            "Martes": "8am - 12pm",
            "Miercoles": "7am - 5pm",
            "Jueves": "9am - 12pm",
            "Viernes": "10am - 1pm",  
        }
        for x,y in diccionario_Horarios.items():
            print(x,y)
        print("")

    def altas(self):
        print("---OPERACIONES---")
        print("")
        print("La operacion se realizo correctamente")
        print("")

    def bajas(self):
        print("La operacion NO se realizo correctamente")
        print("")


obj = Proveedores1055()

obj.Id_proveedores = "1"
obj.NombreProveedor = "Walmart"
obj.Horarios = "8am - 1pm"
obj.Email = "Walmart@gmail.com"
obj.Celular = 6561234567
obj.Tipo = "ProductosComida"
obj.Tiempo_Entrega = "1-20 dias habiles"

obj.mostrarDatos(obj.Id_proveedores,obj.NombreProveedor,obj.Horarios,obj.Email,obj.Celular,obj.Tipo,obj.Tiempo_Entrega)
obj.listaNombreProveedores()
obj.tupla_EmailProveedroes()
obj.diccionario_horarios()
obj.altas()
obj.bajas()



