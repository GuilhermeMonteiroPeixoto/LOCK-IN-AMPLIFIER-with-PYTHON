import numpy as np
import math
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import statistics

Vref_f = 150 
Vref_A = 1 # recomendavel deixar 1
Vref_w = 2*np.pi*Vref_f
pontos = 20000 # afeta na resulocao da curva

array_seno_ref = np.array([Vref_A*(np.sin(Vref_f*2*np.pi*a/pontos)) for a in range(pontos)])
array_seno_ref2 = np.array([(7*np.cos(Vref_f*30*2*np.pi*a/pontos)) for a in range(pontos)])
array_seno_ref3 = np.array([(4*np.cos(Vref_f*10*2*np.pi*a/pontos + 5)) for a in range(pontos)])

# filtro passa-baixo substitui um integrador
def lowpass(x, alpha):
    data = [x[0]]
    for a in x[1:]:
        data.append(data[-1] + (alpha*(a-data[-1])))
    return np.array(data)

passa_baixo = lowpass(array_seno_ref, 0.001)

plt.plot(array_seno_ref)

plt.plot(passa_baixo)
plt.show()
