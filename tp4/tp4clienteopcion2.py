class Cliente:

    def __init__(self,nombre,edad,direccion):
        self.__nombre = nombre
        self.__edad = edad
        self.__direccion = direccion
    def get_nombre(self):
        return self.__nombre
    def get_edad(self):
        return self.__edad
    def get_direccion(self):
        return self.__direccion
    def set_nombre(self,nombre):
        self.__nombre = nombre
    def set_edad(self,edad):
        self.__edad = edad
    def set_direccion(self,direccion):
        self.__direccion = direccion
    def agregar_cliente(self):
        deseo = str(input("desea agregar cliente? (responda si o no): "))
        global list_obj
        list_obj = []
        if deseo == "si":
            cant = int(input("cuantos?"))
            for i in range(cant):
                obj = Cliente(str(input("agrege nombre: ")), str(input("agrege edad: ")),str(input("agrege direccion: ")))
                list_obj.append(obj)
        else:
            pass
    def view(self):
        k=0
        deseo = str(input("desea ver los clientes? (responda si o no): "))
        if deseo == "si":
            for i in list_obj:
                print("numero del cliente:", str(k), "   nombre:",i.get_nombre(),"   edad:", i.get_edad(),"   direccion:", i.get_direccion())
                k = k+1
        else:
            pass

objetobase = Cliente("","",0)
Cliente.agregar_cliente(objetobase)
Cliente.view(objetobase)
