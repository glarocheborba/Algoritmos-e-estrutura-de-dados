def particao(v,esq,dir):
    pivo = v[esq]
    i = esq 
    j = dir + 1
    while True:
        i += 1
        while v[i] < pivo:
            if i >= dir:
                break
            i += 1
        j -= 1
        while v[j] > pivo:
            if j <= esq:
                break
            j -= 1
        if i >=j:
            break
        v[i], v[j] = v[j],v[i]
    v[esq],v[j] = v[j],v[esq]
    return j

def qs(v,esq,dir):
    if esq < dir:
        p = particao(v,esq,dir)
        qs(v,esq,p-1)
        qs(v,p+1,dir)

def quicksort(v,n):
    qs(v,0,n-1)


def main():
    comando = input()
    lista = comando.split()
    lista_ordenada = []
    n = 0
    for j in lista:
        lista_ordenada.append(int(j))
        n += 1
    quicksort(lista_ordenada,n)
    print(lista_ordenada)

if __name__ == '__main__':
    main()
