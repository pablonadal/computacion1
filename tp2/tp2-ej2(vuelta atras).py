#renombrar los archivos sin los numero iniciales
import os
lista = os.listdir(r"C:\Users\marbi\Documents\ing inf 2do\computacion\tp2-archivos\copia de seguridad\SecretKey\SecretKey")
#print(lista)


os.chdir(r"C:\Users\marbi\Documents\ing inf 2do\computacion\tp2-archivos\SecretKey\SecretKey")
for i, k in zip(os.listdir(),lista):
    os.replace(i,k)
