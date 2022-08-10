
class File:
    def Copy_cont(self,file1,file2):
        import shutil
        shutil.copyfile(file1, file2)

    def read_file2(self):
        self.file = open("destino.txt", "r")
        return self.file.read()

file = File()
file.Copy_cont("nombre_archivo.txt", "destino.txt")
print(file.read_file2())
