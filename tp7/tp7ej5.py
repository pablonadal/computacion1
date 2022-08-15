
def consecutive(lista, a, b):
    na = a
    nb = b
    consecutivo = 0
    for i in range(len(lista)-1):
       # print(lista[i],"es igual a", na, " y ",lista[i+1], "es igual a", nb, " O ", lista[i] , "es igual a", nb, " y ", lista[i+1] , "es igual", na)
        if (lista[i] == na and lista[i+1] == nb) or (lista[i] == nb and lista[i+1] == na):
            #print("consecutivo")
            
            consecutivo =+ 1
        else:
            pass
    if consecutivo > 0:
        return True
    else:
        return False