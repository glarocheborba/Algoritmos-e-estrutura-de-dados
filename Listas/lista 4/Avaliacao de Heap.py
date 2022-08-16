# Crie um programa que recebe 1 sequencia de inteiros sem repetições, e retorna uma mensagem descrevendo a sequencia como sendo um Heap de máximo, um Heap de minímo ou não sendo um Heap.

# A sequencia não possuirá repetições

def esquerda(i):
    return ((2*(i+1)) - 1)

def direita(i):
    return (((2*(i+1)) + 1) - 1)

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
        return 0
    return 1

def minheap(v,i,n):
    esq = esquerda(i)
    dir = direita(i)
    if (esq < n) and (v[esq] < v[i]):
        menor = esq
    else:
        menor = i
    
    if (dir < n) and (v[dir] < v[menor]):
        menor = dir

    if menor != i:
        return 0
    return 1

def verifica_heapmax(heap,n):
    for i in range(n//2):
        condicao = maxheap(heap,i,n)
        if condicao == 0:
            return 0
    return 1

def verifica_heapmin(heap,n):
    for i in range(n//2):
        condicao = minheap(heap,i,n)
        if condicao == 0:
            return 0
    return 1

def main():
    comando = input()
    lista = comando.split()
    heap = []
    n = 0
    for j in lista:
        heap.append(int(j))
        n += 1
    
    verifica_max = verifica_heapmax(heap, n)
    verifica_min = verifica_heapmin(heap, n)

    if verifica_max == 1:
        print("E uma Heap de maximo!")
    elif verifica_min == 1:
        print("E uma Heap de minimo!")
    else:
        print('Nao e uma Heap!')
    
if __name__ == '__main__':
    main()
