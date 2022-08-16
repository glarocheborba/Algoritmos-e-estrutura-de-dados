# Crie um programa que recebe duas sequências numéricas positivas, onde a primeira sequência está ordenada, 
# e retorna duas sequências: T, que é formada pelos números da 2ª sequência que estão contidos na 1ª e F, 
# formada pelos numeros da 2ª sequência que não estão contidos na 1ª.

def busca(sequencia, elem, inicio=0, fim=None):
    if fim == None:
        fim = len(sequencia)-1
    if inicio <= fim:
        meio = (inicio+fim)//2
        if sequencia[meio] == elem:
            return meio
        if elem < sequencia[meio]:
            return busca(sequencia,elem,inicio,meio-1)
        else: 
            return busca(sequencia,elem, meio+1, fim)
    return None  

def main():
    lista1 = []
    lista2 = []
    for i in range(2):
        lista = input()
        if i == 0:
            for elem in lista.split():
                lista1.append(int(elem))
        else:
            for elem in lista.split():
                lista2.append(int(elem))
    listaT = []
    listaF = []
    for elem in lista2:
        item = busca(lista1, elem)
        if item != None:
            listaT.append(elem)
        else:
            listaF.append(elem)
    qtd = 0
    while qtd < len(listaT):
        if len(listaT) - qtd == 1:
            print(listaT[qtd])
        else:
            print(listaT[qtd], end=' ')
        qtd += 1
    qtd1 = 0
    while qtd1 < len(listaF):
        if len(listaF) - qtd1 == 1:
            print(listaF[qtd1])
        else:
            print(listaF[qtd1], end=' ')
        qtd1 += 1

if __name__ == '__main__':
    main()