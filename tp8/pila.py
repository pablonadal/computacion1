
class Pila:
    def __init__(self):
        self.items = []
    def agregar(self):
        x = 1
        while x != 0:
            x = int(input("agregar elemento: "))
            self.items.append(x)
        self.items.pop()
        print(self.items)
    def desapilar(self):
        n = self.items.pop()
        print("se saco el elemento: ", n)
        print("nueva pila: ", self.items)


pil = Pila()
pil.agregar()
pil.desapilar()