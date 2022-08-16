# Você é um ladrão de alto calibre, que pelos anos de experiência no ramo sabe exatamente quanto dinheiro existe em cada casa da rua mais rica da região. Mas, antes de realizar o roubo que te tornará dono do quadrilionário, você deve ter precaução: é conhecimento comum de todo bom ladrão que não se rouba duas casas consecutivas, pois o vizinho já terá alertado a polícia. Sabendo disso, descubra qual o maior valor em reais que você pode adquirir roubando a rua, sem alertar a polícia.

def maximo_ganho(lista_loot, qtd):
    if qtd == 0:
        return 0
    elif qtd == 1:
        return lista_loot[0]
    elif qtd == 2:
        if lista_loot[0] >= lista_loot[1]:
            return lista_loot[0]
        return lista_loot[1]

    max_ganho = [0] * qtd

    max_ganho[0] = lista_loot[0]

    if lista_loot[0] >= lista_loot[1]:
            max_ganho[1] = lista_loot[0]
    else:
        max_ganho[1] = lista_loot[1]

    for i in range(2,qtd):
        if (lista_loot[i] + max_ganho[i-2]) >= max_ganho[i-1] :
            max_ganho[i] = lista_loot[i] + max_ganho[i-2]
        else:
            max_ganho[i] = max_ganho[i-1]

    return max_ganho[-1]

     

def main():
    qtd_casas = int(input())
    input_loot_casas = input()
    lista_loot_casas = input_loot_casas.split()
    for i in range(qtd_casas):
        lista_loot_casas[i] = int(lista_loot_casas[i])

    roubado = maximo_ganho(lista_loot_casas, qtd_casas)

    print('{} reais podem ser roubados hoje!'.format(roubado))

if __name__ == '__main__':
    main()
