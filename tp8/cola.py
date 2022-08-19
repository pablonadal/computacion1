
class Cola:
    def __init__(self):
        self.items = []
    def agregar(self):
        x = 1
        while x != 0:
            x = int(input("agregar elemento: "))
            self.items.append(x)
        self.items.pop()
        print(self.items)
    def sacar(self):
        n = self.items.pop(0)
        print("se saco el elemento: ", n)
        print("nueva cola: ", self.items)


pil = Cola()
pil.agregar()
pil.sacar()