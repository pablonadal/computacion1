#renombrar los archivos sin los numero iniciales
import os
lista = os.listdir(r"C:\Users\marbi\Documents\ing inf 2do\computacion\tp2-archivos\SecretKey\SecretKey")
#print(lista)
lista2 = []
for i in lista:
   # print(i)
    lista2.append(i)
Strlista = ",".join(lista2)
#print(Strlista2)
Strlista0 = Strlista.replace("0", "")
Strlista1 = Strlista0.replace("1", "")
Strlista2 = Strlista1.replace("2", "")
Strlista3 = Strlista2.replace("3", "")
Strlista4 = Strlista3.replace("4", "")
Strlista5 = Strlista4.replace("5", "")
Strlista6 = Strlista5.replace("6", "")
Strlista7 = Strlista6.replace("7", "")
Strlista8 = Strlista7.replace("8", "")
Strlista9 = Strlista8.replace("9", "")
#print(Strlista9)
listanombres = Strlista9.split(",")
#print(listanombres)
os.chdir(r"C:\Users\marbi\Documents\ing inf 2do\computacion\tp2-archivos\SecretKey\SecretKey")
for i, k in zip(os.listdir(),listanombres):
    os.replace(i,k)
