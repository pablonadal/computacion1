file = open("nombre_archivo.txt", "r")
#print(file.readlines())
lista = file.readlines()
variable = []
for i in lista:
    x = i.replace("\n", "")
    variable.append(x)
print(variable)
