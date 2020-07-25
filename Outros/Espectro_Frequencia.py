# # Espectro de Frequência de um sinal

import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

data = pd.read_csv('HC-1.csv', header=None) # ou pd.read_csv('out.csv',header=None)

plt.plot(data.iloc[:,0])
plt.show()

#Metodo 1 - Usando Numpy
sinal = data.iloc[0:,0].to_list()
tamanho = len(sinal)
tx = 0.001
freq = np.fft.fftfreq(tamanho, d=tx)
mascara = freq > 0
fft_calculo = np.fft.fft(sinal)
fft_abs = 2.0*np.abs(fft_calculo/tamanho)
plt.plot(freq[mascara],fft_abs[mascara])
plt.xlim(0,150)
plt.ylim(0.00000, 0.00006)
plt.show()

#Metodo 2 - Usando scipy
from scipy.fftpack import fft
N = len(sinal)
tx = 0.001
y = data.iloc[0:,1].to_list()
yf = fft(y)
xf = np.linspace(0.0, 1.0/(2.0*tx), int(N/2))
plt.plot(xf, 2.0/N*np.abs(yf[0:int(N/2)]))
plt.xlim(0,150)
plt.ylim(0.00000, 0.00006)
plt.show()

#Metodo 3 - Usando matplotlib
plt.magnitude_spectrum(sinal, Fs=1/tx)
plt.xlim(0,150)
plt.ylim(0.00000, 0.00006)
plt.show()

