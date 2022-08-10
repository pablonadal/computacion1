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
file1 = File()
file1.open_file("nombre_archivo.txt")
file1.read_n_lines_file()
