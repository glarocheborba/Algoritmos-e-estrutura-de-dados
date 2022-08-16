def troca(v,i,j):
    v[i],v[j] = v[j],v[i]

def selectionsort(v,n):
    for i in range(0,n):
        min = i
        for j in range(i+1,n):
            if v[min] > v[j]:
                min = j
        troca(v,i,min)

def main():
    comando = input()
    lista = comando.split()
    lista_ordenada = []
    n = 0
    for j in lista:
        lista_ordenada.append(int(j))
        n += 1
    selectionsort(lista_ordenada, n)

    print(lista_ordenada)

if __name__ == '__main__':
    main()