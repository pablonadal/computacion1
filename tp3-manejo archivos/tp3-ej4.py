class File:

    def open_file(self, file):
        self.file = open(file, "r")

    def read_n_lines_file(self):
        n = int(input("ingrese numero de lineas para leer: "))
        cont = 0
        for i in self.file:
            if cont < n:
                print(i)
                cont += 1
            else:
                pass
    def store_in_list(self):
        self.file = open("nombre_archivo.txt", "r")
        list = []
        for i in self.file:
            k = i
            list.append(k)
        print(list)
file1 = File()
file1.open_file("nombre_archivo.txt")
file1.read_n_lines_file()
file1.store_in_list()
