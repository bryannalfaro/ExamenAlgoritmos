#Referencia> https://stackoverflow.com/questions/41725808/graphing-the-time-of-computing-of-a-particular-function-in-python
from operator import le
from algoritmos import *
import matplotlib.pyplot as plt
import timeit
import sys

# estableciendo el maximo de recursion, default 1000
sys.setrecursionlimit(10000)

# Calculando tiempos
data = list(range(1, 1000))
times = []
for i in data:
    # Tiempo de ejecucion de cada factorial
    start_time = timeit.default_timer()
    dac_factorial(i)
    times.append(timeit.default_timer()-start_time)

# Algunos tiempos quedan excesivamente grandes, por lo que se eliminan
max_rem = False
while not max_rem:
    max_time = max(times)
    max_i = times.index(max_time)
    # Si el tiempo es mayor no es el ultimo elemento
    if max_i != len(times)-1:
        # Si el tiempo mayor es dos veces mas grande que el ultimo elemento
        if max_time * 2 > times[len(times)-1]:
            times.remove(max_time)
            data.remove(data[max_i])
        else:
            max_rem = True
    else:
        max_rem = True

# Graficando
plt.plot(data, times)
plt.show()