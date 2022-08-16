def troca(v,i,j):
    v[i],v[j] = v[j],v[i]

def bubblesort(v,n):
    for i in range(n-1,0,-1):
        for j in range(0,i):
            if v[j] > v[j+1]:
                troca(v,j,j+1)

def main():
    comando = input()
    lista = comando.split()
    lista_ordenada = []
    n = 0
    for j in lista:
        lista_ordenada.append(int(j))
        n += 1

    bubblesort(lista_ordenada, n)

    print(lista_ordenada)

if __name__ == '__main__':
    main()