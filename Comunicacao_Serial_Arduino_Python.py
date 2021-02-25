# -*- coding: utf-8 -*-

import serial
import time
import matplotlib.pyplot as plt
import numpy as np
from datetime import datetime

print("\t\t________________________________________________________________________________________________________________________________________")
print("\t\t                                  _      _   _   _   _   _ .  _           _  _  ___  _   _   _   _  _             ")
print("\t\t                             |_| | | |  | | |   |_/ |_| |_ | |_| P       |_ | |  |  | | |_/ |_/ |_ |_                                 ")
print("\t\t                             | | |_| |_ |_| |_| | \ | | |  | | | Y 1.0.0 |  |_|  |  |_| | \ | \ |_ |  RATIVA                ")
print("\t\t________________________________________________________________________________________________________________________________________")
print("\t\t[100%]                                           FEITO POR GUILHERME O. MONTEIRO PEIXOTO")
while 1==1:
    now = datetime.now()
    dt_string = now.strftime("%d_%m_%Y_%H_%M_%S")
    print("\n")
    print("[Aperte Enter apenas quando quiser iniciar a gravação]")
    print("Informe o Tempo de Gravação holográfica:", end=" ")
    tempogravacao = float(input()) #tempo de gravacao em segundos
    ser = serial.Serial('COM3',2000000) #importar serial
    ser.close()
    ser.open()

    text_file = open("Dados_{}.dat".format(dt_string),"a") #abrir arquivo txt
    i=0.0
    start = time.process_time() #iniciar tempo
    while i<tempogravacao*0.7: #enquanto tempo < tempo de gravacao
        data = ser.readline() #lendo serial
        i = time.process_time() - start #quanto tempo passou
        text_file.write(data.decode())
    text_file.close()
    print("Dados Salvos com sucesso!")
    X, Y = [], []
    for line in open('Dados_{}.dat'.format(dt_string), 'r'):
      values = [float(s) for s in line.split()]
      X.append(values[0])
      Y.append(values[1])
    plt.xlabel("Tempo(s)") #nomear eixo x
    plt.ylabel("V") #nomear eixo y
    plt.title('V x Tempo') #nomear titulo
    #plt.grid(True)
    plt.plot(X, Y)
    #plt.ylim(-0.5, 5.0)
    plt.show()
    plt.pause(0.0001)
    ser.close()
