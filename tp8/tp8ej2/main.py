from cola_de_pacientes import *

def menu():
    print("¿que desea hacer?")
    global opc
    opc = int(input("ingrese 1 para añadir un nuevo paciente o 2 para hacer pasar a un paciente al consultorio: "))


deseo = 1
while deseo == 1:
    menu()
    if opc == 1:
        cola.Nuevo_paciente()
        deseo = int(input("ingrese 1 si desea continuar o 0 si desea finalizar: "))
    elif opc == 2:
        cola.Proximo_paciente()
        deseo = int(input("ingrese 1 si desea continuar o 0 si desea finalizar: "))