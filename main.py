#Referencia> https://stackoverflow.com/questions/41725808/graphing-the-time-of-computing-of-a-particular-function-in-python
from algoritmos import *
import matplotlib.pyplot as plt
import timeit

start_time = timeit.default_timer()

data = range(1, 300)
times = []
for i in data:
    dac_factorial(i)
    times.append(timeit.default_timer()-start_time)
plt.plot(data, times)
plt.show()