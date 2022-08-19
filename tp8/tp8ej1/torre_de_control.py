
class Torre_de_control:
    def __init__(self):
        self.cola_ingresantes = []
        self.cola_ingresados = []
    
    def reconocimiento(self):
        print("cola ingresantes: ", self.cola_ingresantes
        , "\ncola ingresados: ", self.cola_ingresados)
        
    def agregar_a_ingresantes(self):
        x = 1
        while x != 0:
            x = int(input("(escriba el numero del avion, 0 para finalizar)\nagregar ingresante: "))
            self.cola_ingresantes.append(x)
        self.cola_ingresantes.pop()
        print("nueva cola de ingresantes: ",self.cola_ingresantes)
    
    def añadir_a_cola_ingresados(self):
        n = self.cola_ingresantes.pop(0)
        self.cola_ingresados.append(n)
        print("se ingreso: ", n)
        print("nueva cola de ingresantes: ", self.cola_ingresantes
        , "\n nueva cola de ingresados: ", self.cola_ingresados)
    
    def despegar_avion(self):
        n = self.cola_ingresados.pop(0)
        print("el avion", n ,"despego")

control = Torre_de_control()
