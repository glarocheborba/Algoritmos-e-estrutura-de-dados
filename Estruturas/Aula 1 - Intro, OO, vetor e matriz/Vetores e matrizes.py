import numpy as np

v = np.empty(4,int)
print(v)

matriz = []

for i in range(5):
    matriz.append([0] * 2)

print(matriz)

matrizNumpy = np.zeros((10,10), int)


for i in range(len(matrizNumpy)):
    for j in range(len(matrizNumpy[i])):
        if i == j:
            matrizNumpy[i][j] = 1
        else:
            matrizNumpy[i][j] = 10
print(matrizNumpy)
