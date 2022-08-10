class File:

    def open_file(self, file):
        self.file = open(file, "a")

    def add_text(self):
        self.file.write(str(input("add text: ")))

    def read_file(self,file):
        self.file = open(file, "r")
        return self.file.read()

file1 = File()
file1.open_file("nombre_archivo.txt")
file1.add_text()
print(file1.read_file("nombre_archivo.txt"))
