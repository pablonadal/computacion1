class Libro:

    def __init__(self,titulo,autor,precio):
        self.__titulo = titulo
        self.__autor = autor
        self.__precio = precio
    def get_titulo(self):
        return self.__titulo
    def get_autor(self):
        return self.__autor
    def get_precio(self):
        return self.__precio
    def set_titulo(self,titulo):
        self.__titulo = titulo
    def set_autor(self,autor):
        self.__autor = autor
    def set_precio(self,precio):
        self.__precio = precio
    def agregar_libro(self):
        deseo = str(input("desea agregar libros? (responda si o no): "))
        global list_obj
        list_obj = []
        if deseo == "si":
            cant = int(input("cuantos?"))
            for i in range(cant):
                obj = Libro(str(input("agrege titulo: ")), str(input("agrege autor: ")),str(input("agrege precio: ")))
                list_obj.append(obj)
        else:
            pass
    def view(self):
        k = 0
        deseo = str(input("desea ver los libros? (responda si o no): "))
        if deseo == "si":
            for i in list_obj:
                print("numero de libro:", str(k), "   Titulo:",i.get_titulo(),"   autor:", i.get_autor(),"   precio:", i.get_precio())
                k = k+1

objetobase = Libro("","",0)
Libro.agregar_libro(objetobase)
Libro.view(objetobase)
