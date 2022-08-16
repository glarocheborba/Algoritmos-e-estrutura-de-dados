def esquerda(i):
    return 2 * i + 1

def direita(i):
    return 2 * i + 2

def pai(i):
    return (((i+1)//2) - 1)

def maxheap(v,i,n):
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
        maxheap(v,maior,n)

def montarMaxHeap(v):
    n = len(v)
    for i in range((n//2)-1,-1,-1):
        maxheap(v,i,n)

def main():
    comando = input()
    lista = comando.split()
    heap = []
    for j in lista:
        heap.append(int(j))
    montarMaxHeap(heap)
    print(heap)

if __name__ == '__main__':
    main()
    