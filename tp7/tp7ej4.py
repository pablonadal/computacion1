# clases: bingo (funcion que se le de como argumento una lista
# de 10 numeros y compare  con estos 5 numeros [2,7,9,14,15],
# si estan almenos una vez cada uno de los numeros retorne "WIN",
# si no que retorne "LOSE")


def verificar(x):
    if 2 in x and 7 in x and 9 in x and 14 in x and 15 in x:
        return True
    else:
        return False