import collections

#función que corrobora que el número ingresado este en el rango correcto
def rango (num):
    if num < 1 or num > 9999:
        print("Debe ingresar un número entre 1 y 9999")
        return False
    else:
        return True 
 
#función que cuenta las iteraciones 
def kaprekar(num):        
    numS = str(num)

    # Agrega los 0 necesarios
    numS = '0' * (4 - len(numS)) + numS    

    # Tiene que haber 2 digitos diferentes por lo menos, sino arroja 8
    if len(collections.Counter(numS)) == 1:
        print("8 iteraciones.")
        return 8

    n = 0

