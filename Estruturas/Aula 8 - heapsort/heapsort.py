def esquerda(i):
    return 2 * i + 1

def direita(i):
    return 2 * i + 2

def pai(i):
    return (((i+1)//2) - 1)

def heapfy(v,i,n):
    esq = esquerda(i)
    dir = direita(i)
    if esq < n and v[esq] > v[i]:
        maior = esq
    else:
        maior = i

    if dir < n and v[dir] > v[maior]:
        maior = dir

    if maior != i:
        v[i], v[maior] = v[maior], v[i]
        heapfy(v,maior,n)

def montarHeapsort(v):
    n = len(v)
    
    for i in range((n//2)-1,-1,-1):
        heapfy(v,i,n)

    # for i in range(n-1, 0, -1):
    #     v[i],v[0] = v[0] , v[i]
    #     heapfy(v, 0, i)

def heap_increase(v,i):
    while i > 0 and v[pai(i)] < v[i]:
        v[i], v[pai(i)] = v[pai(i)], v[i]
        i = pai(i)

        
def max_heap_insert(v,elem):
    n = len(v)
    v.append(elem)
    heap_increase(v,n)

def heap_delete(v,n):
    n = len(v)
    lista[0],lista[-1] = lista[-1], lista[0]
    lista = lista[:-1]
    n -= 1
    heapfy(lista,0,n)

def main():
    comando = input()
    lista = comando.split()
    heap = []
    for j in lista:
        heap.append(int(j))
    montarHeapsort(heap)
    print(heap)
    while comando != 'end':
        if comando == 'insert':
            elem = int(input())
            max_heap_insert(heap,elem)
        comando = input()
    
    print(heap)

if __name__ == '__main__':
    main()