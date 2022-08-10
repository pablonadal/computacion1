class File:

    def open_file(self, file):
        self.file = open(file, "r")

    def read_file(self):
        return self.file.read()

file1 = File()
file1.open_file("nombre_archivo_tp3_ej1.txt")
print(file1.read_file())
