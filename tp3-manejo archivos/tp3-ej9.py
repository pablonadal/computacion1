class File:
    def analysis(self, file):

        contLineas = 0
        contPalabras = 0
        contCaracteres = 0

        with open(file) as ar:
            for line in ar:
                contLineas+=1
                for word in line.split():
                    contPalabras+=1
                    for caracteres in word:
                        contCaracteres+=1

        ar.close()

        print('numero de lineas: ' + str(contLineas))
        print('numero de palabras: ' + str(contPalabras))
        print('numero de caracteres: ' + str(contCaracteres))

file = File()
file.analysis('nombre_archivo.txt')
