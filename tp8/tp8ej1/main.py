from torre_de_control import *

def menu():
    print("que desea hacer? \ningrese 1 para agregar avion a cola de ingresantes \n ingrese 2 para añadir avion a cola ingresados \n ingrese 3 para hacer despegar un avion \n ingrese 4 para ver estado actual de las colas ")
    global opc
    opc = int(input("ingrese opcion: "))
    print("ingreso la opcion:", opc)

deseo = 1
while deseo == 1:
    menu()
    if opc == 1:
        control.agregar_a_ingresantes()
        deseo = int(input("¿desea continuar? \n ingrese 0 si su respuesta es NO o 1 si su respuesta es SI: "))
    elif opc == 2:
        control.añadir_a_cola_ingresados()
        deseo = int(input("¿desea continuar? \n ingrese 0 si su respuesta es NO o 1 si su respuesta es SI: "))
    elif opc == 3:
        control.despegar_avion()
        deseo = int(input("¿desea continuar? \n ingrese 0 si su respuesta es NO o 1 si su respuesta es SI: "))
    elif opc == 4:
        control.reconocimiento()
        deseo = int(input("¿desea continuar? \n ingrese 0 si su respuesta es NO o 1 si su respuesta es SI: "))
