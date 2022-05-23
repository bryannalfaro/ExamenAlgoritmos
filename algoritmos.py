#Referencia: https://web.eecs.umich.edu/~aprakash/eecs282/lectures/11-recursion.pdf

from re import I

def dac_factorial(i):
    if i == 0 :
        return 1
    if i<0:
        return "Error: No existe el factorial de un número negativo"
    else:
        return i * dac_factorial(i-1)
