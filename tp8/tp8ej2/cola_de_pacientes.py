class Cola_de_pacientes:
    def __init__(self):
        self.items = []
    def Nuevo_paciente(self):
        x = 1
        while x != 0 and x != "0":
            x = str(input("agregar nuevo paciente: "))
            self.items.append(x)
        self.items.pop()
        print("estado de cola de pacientes: ",self.items)
    def Proximo_paciente(self):
        n = self.items.pop(0)
        print("el paciente ", n, "paso al consultorio")
        print("estado de cola de pacientes: ", self.items)

cola = Cola_de_pacientes()
