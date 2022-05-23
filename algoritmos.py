#Referencia: https://web.eecs.umich.edu/~aprakash/eecs282/lectures/11-recursion.pdf

from re import I

def dac_factorial(i):
    if i == 0 :
        return 1
    if i<0:
        return "Error: No existe el factorial de un número negativo"
    else:
        return i * dac_factorial(i-1)

    
def factorialBottomUp(n):
    #Asignamos tamano de array
    array = [0] * (n+1)
    #mejor caso de 0! =  1
    array[0] = 1
    #iterar la cantidad de veces hasta llegar al valor de n
    i = 1
    while i <= n:
        array[i] = i * array[i - 1]
        i += 1
    return array[n]

