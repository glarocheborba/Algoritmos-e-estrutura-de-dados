def divide_mergesort(lista,esq,dir):
    if esq < dir:
        meio = (esq+dir)//2
        divide_mergesort(lista,esq,meio)
        divide_mergesort(lista,meio+1,dir)
        merge(lista,esq,meio,dir)

def mergesort(lista,n):
    global aux
    aux = list(lista)
    divide_mergesort(lista,0,n-1)
    del aux

# def BU_mergesort(lista,n):
#     global aux 
#     aux = list(lista)
#     k = 1
#     while k < n:
#         for esq in range(0,n-k,2*k):
#             merge(lista,esq,esq+k-1,min(esq+(2*k)-1,n-1))
#         k *= 2
#     del aux

def merge(lista,esq,meio,dir):
    i = esq
    j = meio+1
    for k in range(esq,dir+1):
        aux[k] = lista[k]
    for k in range(esq,dir+1):
        if i > meio:
            lista[k] = aux[j]
            j += 1
        elif j > dir:
            lista[k] = aux[i]
            i += 1
        elif aux[i] > aux[j]:
            lista[k] = aux[j]
            j += 1
        else:
            lista[k] = aux[i]
            i += 1 

# def mergeSort(v):
#     if len(v) > 1:
#         meio = len(v)//2
#         esq = v[:meio]
#         dir = v[meio:]

#         mergeSort(esq)

#         mergeSort(dir)
  
#         i = j = k = 0
  
#         while i < len(esq) and j < len(dir):
#             if esq[i] < dir[j]:
#                 v[k] = esq[i]
#                 i += 1
#             else:
#                 v[k] = dir[j]
#                 j += 1
#             k += 1

#         while i < len(esq):
#             v[k] = esq[i]
#             i += 1
#             k += 1
  
#         while j < len(dir):
#             v[k] = dir[j]
#             j += 1
#             k += 1

def main():
    comando = input()
    lista = comando.split()
    lista_ordenada = []
    n = 0
    for j in lista:
        lista_ordenada.append(int(j))
        n += 1
    mergesort(lista_ordenada,n)
    print(lista_ordenada)

if __name__ == '__main__':
    main()
    