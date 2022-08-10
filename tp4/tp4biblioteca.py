import tp4libroopcion2
import tp4clienteopcion2
def ShowBooks():
    tp4libroopcion2.Libro.view(tp4libroopcion2.objetobase)
def ShowClients():
    tp4clienteopcion2.Cliente.view((tp4clienteopcion2.objetobase))
ShowBooks()
ShowClients()
def Assign():
    decision = str(input("desea asignar un libro a un cliente? (responda si o no)"))
    if decision == "si":
        dic = {}
        client = int(input("numero de cliente: "))
        lib = int(input("numero de libro: "))
        dic["nombre de cliente: " + tp4clienteopcion2.list_obj[client].get_nombre()] = "titulo del libro: " + tp4libroopcion2.list_obj[lib].get_titulo()
        print(dic)
    else:
        pass
Assign()
