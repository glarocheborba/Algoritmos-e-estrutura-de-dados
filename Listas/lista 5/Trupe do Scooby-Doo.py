# Wes decidiu entrar na trupe do Scooby Doo e uma das fases do processo seletivo era um problema um tanto quanto simples porém com um tom de complexidade... Serão entregue para ele dois baús: um repleto de chaves e outro repleto de cadeados trancados. Cada chave e cada cadeado possuia uma inscrição única, indicando qual chave abre qual cadeado.

# A função de Wes é, diversas vezes, organizar de maneira sequencial as chaves e os cadeados de maneira que a i-ésima chave da sequencia de chaves abra o i-ésimo cadeado da sequência de cadeados.

# Os baús são entregues de maneira separada - as chaves ficam em uma partição a esquerda e os cadeados em uma partição a direita. Para encontrar a sequência correta, Wes não pode comparar as chaves entre si ou os cadeados entre si. Dessa forma, a decisão de mover ou não uma chave deve ser tomada exclusivamente olhando para os cadeados e vice versa.

# Scooby sabe que Wes é compuyteiro e decidiu contradizer a comum (e errada cof cof) opinião de que a disciplina não serve para nada. Assim, ele determinou que Wes deveria utilizar os seus conhecimentos aprendidos na disciplina de Algoritmos e Estrutura de Dados para solucionar o problema e, portanto, que deveria utilizar um método de ordenação que seja um algoritmo de divisão e conquista que utilize o conceito de pivôs.

# Descrição do Problema
# Dado k conjuntos de n chaves diferentes e n cadeados diferentes, crie duas sequências onde a i-ésima chave da sequencia de chaves abra o i-ésimo cadeado da sequência de cadeados.

# Restrição 1: A comparação de uma chave com outra chave ou um cadeado com outro cadeado não é permitida. Isso significa que a chave só pode ser comparada com o cadeado e o cadeado só pode ser comparado com a chave para ver qual deles é maior / menor.

# Restrição 2: A metodologia de resolução deve seguir os requisito impostos por Scooby.

# Para cada iteração, você deve exibir a sequência organizada das chaves e a sequência organizada dos cadeados.

def particao(v,esq,dir,vi):
    pivo = vi[esq]
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
        if i >= j:
            break
        v[i], v[j] = v[j],v[i]
    v[esq],v[j] = v[j],v[esq]
    return j

def qs(v,esq,dir,vi):
    if esq < dir:
        p = particao(v,esq,dir,vi)
        qs(v,esq,p-1,vi)
        qs(v,p+1,dir,vi)

def quicksort(v,n,vi):
    qs(v,0,n-1,vi)


def main():
    comando = int(input())
    cont = 0
    while cont < comando:
        lista_entrada1 = input()
        lista1 = lista_entrada1.split()
        n1 = len(lista1)

        lista_entrada2 = input()
        lista2 = lista_entrada2.split()
        n2 = len(lista2)

        for i in range(40):
            quicksort(lista1,n1,lista2)
            quicksort(lista2,n2,lista1)

        qtd = 0
        while qtd < n1:
            if n1 - qtd == 1:
                print(lista2[qtd])
            else:
                print(lista2[qtd], end=' ')
            qtd += 1
        qtd1 = 0
        while qtd1 < n2:
            if n2 - qtd1 == 1:
                print(lista2[qtd1])
            else:
                print(lista2[qtd1], end=' ')
            qtd1 += 1
        cont += 1

if __name__ == '__main__':
    main()
