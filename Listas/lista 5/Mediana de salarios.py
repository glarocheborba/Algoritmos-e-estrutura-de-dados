# Guilherme está no processo seletivo para a empresa de software CInderela. A recrutadora perguntou a sua expectativa salarial, mas ele não soube responder na hora.

# Ele resolveu que vai pedir um salário de acordo com a mediana dos salários da empresa que ele trabalha atualmente e da CInderela, e precisa da sua ajuda para isso.

# Dados dois arrays ordenados salarios_m e salarios_n, representando respectivamente os salários da empresa atual e os salários da empresa CInderela, retorne a mediana dos dois arrays ordenados.

def mergesort(lista,n,meio):
    global aux
    aux = list(lista)
    merge(lista,0,meio,n-1)
    del aux

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
            

def montar(lista1,lista2):
    lista_ordenada1 = []
    lista_ordenada2 = []
    n1 = 0
    n2 = 0
    for j in lista1:
        lista_ordenada1.append(int(j))
        n1 += 1
    for i in lista2:
        lista_ordenada2.append(int(i))
        n2 += 1
    lista_ordenada = lista_ordenada1 + lista_ordenada2
    n = n1 + n2
    mergesort(lista_ordenada,n,n1-1)
    return n,lista_ordenada 

def main():
    comando1 = input()
    lista1 = comando1.split()
    comando2 = input()
    lista2 = comando2.split()
    n,lista_ordenada = montar(lista1,lista2)
    if n%2 != 0:
        elem = lista_ordenada[(n//2)]
        print('{:.2f}'.format(elem))
    else:
        elem = (lista_ordenada[(n//2)-1]+lista_ordenada[n//2])/2
        print('{:.2f}'.format(elem))

if __name__ == '__main__':
    main()
    
