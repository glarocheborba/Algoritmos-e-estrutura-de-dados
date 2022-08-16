import time
import numpy as np
import matplotlib.pyplot as plt

def f3(n):
    return 2*n**2 + 2*n +2 

qtdeInstrucoes = []
ns = [10,20,30,40,50,60]

for N in range(0,61):

    contInstrucao = 0

    vetor1= range(N) #nao conta como instrucao pq é a entrada
    vetor2 = range(N)
    
    encontrou=False
    contInstrucao+=1
    
    for i in range(N):
        contInstrucao+=1
        for j in range(N):
            contInstrucao+=1
            contInstrucao+=1
            if (vetor1[i] == vetor2[j]):
                encontrou=True
        contInstrucao+=1 #para o ultimo for
    contInstrucao+=1 #para o primeiro for
    
    qtdeInstrucoes.append(contInstrucao)

qtdeInstrucoesTeorica = [f3(N) for N in range(0,61)]

print(qtdeInstrucoes)
print(qtdeInstrucoesTeorica)

plt.plot(range(len(qtdeInstrucoes)),qtdeInstrucoes , label="probl")
plt.plot(range(len(qtdeInstrucoesTeorica)),qtdeInstrucoesTeorica , label="f3")

plt.legend()
plt.show()