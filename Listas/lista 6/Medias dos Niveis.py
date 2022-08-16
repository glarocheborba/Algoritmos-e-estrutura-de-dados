# Dado um array representando uma árvore binária, calcule a média dos valores em cada nível da árvore.

# Dois nós estão num mesmo nível se a sua altura em relação à raiz é igual.

# A representação da árvore se dará por uma sequência de inteiros positivos, tal que:

# Para todos os nós "i":
# 2 * i + 1 é a posição do seu filho esquerdo.
# 2 * i + 2 é a posição do seu filho direito.

# Considere que o nível da raiz é "1". Logo, o nível dos filhos da raiz é "2", e assim em diante.

def esquerda(i):
    return 2 * i + 1

def direita(i):
    return 2 * i + 2

def mediaNiveis(heap,tamanhoheap):
    media1 = heap[0]
    print('Media do nivel {} = {:.2f}'.format(1,media1))
    index = 0
    indexesq = 0
    nivel = 1
    while index < tamanhoheap:
        dir = direita(index)
        esq = esquerda(indexesq)
        index = dir
        indexesq = esq
        soma = 0
        qtd = 0
        if dir >= tamanhoheap:
            dir = tamanhoheap-1
        for i in range(esq,dir+1):
            if heap[i] == -1:
                pass
            else:
                soma += heap[i]
                qtd += 1
        media = soma/qtd
        nivel += 1
        print('Media do nivel {} = {:.2f}'.format(nivel,media))
        
        
def main():
    comando = input()
    lista = comando.split()
    heap = []
    n = 0
    for i in lista:
        heap.append(int(i))
        n += 1
    mediaNiveis(heap,n)


if __name__ == '__main__':
    main()

