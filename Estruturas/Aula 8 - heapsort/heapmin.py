def esquerda(i):
    return 2 * i + 1

def direita(i):
    return 2 * i + 2

def pai(i):
    return (((i+1)//2) - 1)

def minheap(v,i,n):
    esq = esquerda(i)
    dir = direita(i)
    if (esq < n) and (v[esq][2] < v[i][2]):
        menor = esq
    else:
        menor = i
    
    if (dir < n) and (v[dir][2] < v[menor][2]):
        menor = dir

    if menor != i:
        v[i], v[menor] = v[menor], v[i]
        minheap(v,menor,n)

def montarMinHeap(v):
    n = len(v)
    for i in range((n//2)-1,-1,-1):
        minheap(v,i,n)

def heap_delete(v):
    n = len(v)
    v = v[1:]
    n -= 1
    minheap(v,0,n)
    return v

def main():
    heap = []
    n = int(input())
    while n > 0:
        comando = input()
        o, d, w = comando.split()
        heap.append([o, d, int(w)])
        n -= 1
    montarMinHeap(heap)
    print(heap)

    comando = input()
    while comando != 'stop':
        heap = heap_delete(heap)
        print(heap)
        comando = input()

if __name__ == '__main__':
    main()