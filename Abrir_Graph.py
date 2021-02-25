# -*- coding: utf-8 -*-
import matplotlib.pyplot as plt
import numpy as np

print("\t_____________________________________________________________________________________________________________________________________________________")
print("\t___________                                                                                                                               ___________")
print("\t___________                                                         GRAFICX 1.0.0                                                         ___________")
print("\t_____________________________________________________________________________________________________________________________________________________")
print("\t                                                      FEITO POR GUILHERME O. MONTEIRO PEIXOTO")
print("\n")
while(True):
    nome_arquivo = input("Digite o nome do Arduivo: ")
    X, Y = [], []
    for line in open('{}.dat'.format(nome_arquivo), 'r'):
        values = [float(s) for s in line.split()]
        Y.append(values[0])
        X.append(values[1])
    plt.xlabel("tempo") #nomear eixo x
    plt.ylabel("infectados") #nomear eixo y
    plt.title('tempo x infectados') #nomear titulo
    #plt.grid(True)

    # GRAFICO LINHA LISTRADA
    #plt.plot(X, Y, label = "line", color='blue', linestyle='dashed', linewidth = 1)
                                                # linestyle='solid'
                                                # linestyle='dotted'
                                                # linestyle='dashdot'

    # GRAFICO PONTOS
    plt.scatter(X, Y, label= "stars", color= "green", marker="o", s=5)
                                                      #marker="."
                                                      #marker="*"
                                                      #marker="v"

    # GRAFICO PONTO E LINHA
    #plt.plot(X, Y, label = "line", color='red', linestyle='dashed', linewidth = 1, marker='o', markerfacecolor='blue', markersize=3)
                                        #blue
                                        #green
                                        #cyan
                                        #magenta
                                        #yellow
                                        #black

    #plt.ylim(-0.5, 5.0)
    plt.legend()
    plt.show()
    plt.pause(0.0001)
