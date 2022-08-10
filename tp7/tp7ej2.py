def pin_atm(self):
    cadena = str(self)
    print(cadena)
    if str.isdigit(cadena) and (len(cadena) == 4 or len(cadena) == 6):
        return True
    else:
        return False
pin_atm("123l")
