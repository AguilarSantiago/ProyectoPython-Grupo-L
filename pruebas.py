import collections

#función que corrobora que el número ingresado este en el rango correcto
def rango (num):
    if num < 1 or num > 9999:
        print("Debe ingresar un número entre 1 y 9999")
        return False
    else:
        return True 
 