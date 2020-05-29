<<<<<<< HEAD
<<<<<<< HEAD

# función que corrobora que el número ingresado este en el rango correcto
=======
import collections

#función que corrobora que el número ingresado este en el rango correcto
>>>>>>> Spalenza-
def rango (num):
    if num < 1 or num > 9999:
        print("Debe ingresar un número entre 1 y 9999")
        return False
    else:
        return True 
 
<<<<<<< HEAD
# función que cuenta las iteraciones 
def kaprekar(num):
    numS = str(num)

    # Agrega los 0 necesarios
    numS = '0' * (4 - len(numS)) + numS
=======
#función que cuenta las iteraciones 
def kaprekar(num):        
    numS = str(num)

    # Agrega los 0 necesarios
    numS = '0' * (4 - len(numS)) + numS    
>>>>>>> Spalenza-

    # Tiene que haber 2 digitos diferentes por lo menos, sino arroja 8
    if len(collections.Counter(numS)) == 1:
        print("8 iteraciones.")
        return 8

    n = 0
<<<<<<< HEAD

    # si el número ingresado es 6174 arroja el número 0
=======
    
    #si el número ingresado es 6174 arroja el número 0
>>>>>>> Spalenza-
    if num ==6174:
        print("0 iteración." )
        return 0

    else:
        while (num != 6174):
            n += 1

            numS = str(num)

            # completa con 0 si tiene menos de 4 dígitos
            numS = '0' * (4 - len(numS)) + numS

            # ordena los número de manera ascendente
            mayor = int(''.join(sorted(numS)[::-1]))

            # ordena los número de manera ascendente
            menor = int(''.join(sorted(numS)))
<<<<<<< HEAD

            # resta el mayor menos el menor
            num = mayor - menor

=======
           
            # resta el mayor menos el menor        
            num = mayor - menor
           
>>>>>>> Spalenza-
            if n == 8:
                print("Error")
                return -1

        print(n," iteraciones.")
        return n

<<<<<<< HEAD
=======
#MAIN
while True:
    numero = int(input("Ingresa el numero de casos de prueba: "))
    if rango (numero) == True:
        break

kaprekar (numero)

>>>>>>> Spalenza-
