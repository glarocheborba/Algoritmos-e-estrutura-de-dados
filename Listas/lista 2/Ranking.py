# Isolado em casa sem nada pra fazer, você descobre perambulando pela internet um jogo extremamente viciante chamando "GAME OF THE ANIMAL". Nele, os jogadores competem apostando em números representados por animais, e, se sorteados, ganham pontuação.

# Por ser muito popular, o jogo conta com uma ampla comunidade de jogadores. Mas, infelizmente, não há nenhuma organização entre as pontuações, tornando impossível saber quem é melhor jogador que quem.

# Comovido por essa triste realidade e motivado a por em prática seus conhecimentos de programação, você decide implementar um sistema de rankings que recebe o nome e a pontuação de jogadores e os organiza de uma maneira eficiente.

# Descrição do Problema
# No começo do programa, vocẽ receberá um inteiro K e logo após K comandos do tipo ADD, para adicionar jogadores no sistema, ou PROX, que pede ao sistema que informe as proximidades de um jogador particular.

# As proximidades de um jogador são definidas pelo sucessor e predecessor do jogador, se existirem, em ordem crescente de pontuação.

class Node:
    def __init__(self, ponto, nome):
        self.ponto = ponto
        self.nome = nome
        self.esquerda = None 
        self.direita = None
        self.pai = None

class ArvoreBinaria:
    def __init__(self, ponto, nome):
        if ponto != None:
            node = Node(ponto,nome)
            self.raiz = node
        else:
            self.raiz = None

    def minArvore(self,node):
        while node.esquerda:
            node = node.esquerda
        return node

    def maxArvore(self,node):
        while node.direita:
            node = node.direita
        return node

    def sucessor(self,node):
        if node.direita != None:
            return ArvoreBinaria.minArvore(self,node.direita)
        y = node.pai
        while y != None and node == y.direita:
            node = y
            y = y.pai
        return y

    def antecessor(self,node):
        if node.esquerda != None:
            return ArvoreBinaria.maxArvore(self,node.esquerda)
        y = node.pai
        while y != None and node == y.esquerda:
            node = y 
            y = y.pai
        return y
    
    def add(self,node):
        pai = None
        x = self.raiz
        while (x):
            pai = x
            if node.ponto < x.ponto:
                x =  x.esquerda
            else:
                x = x.direita
        node.pai = pai
        if pai is None:
            self.raiz = node
        elif node.ponto < pai.ponto:
            pai.esquerda = node
        else:
            pai.direita = node

    def procurar(self,ponto):
        return self._procurar(self.raiz,ponto)

    def _procurar(self, node, ponto):
        if (node == None) or (ponto == node.ponto):
            return node
        if ponto < node.ponto:
            return self._procurar(node.esquerda, ponto)
        if ponto > node.ponto:
            return self._procurar(node.direita, ponto)

def main():
    n = int(input())
    node = None
    arvore = ArvoreBinaria(None,None)
    for i in range(n):
        comando = input()
        if 'ADD' in comando:
            separa = comando.split()
            nome = separa[1]
            ponto = int(separa[2])
            procura_node = arvore.procurar(ponto)
            if procura_node == None:
                node = Node(ponto,nome)
                arvore.add(node)
                print('{} inserido com sucesso!'.format(nome))
            else:
                print('{} ja esta no sistema.'.format(nome))

        elif 'PROX' in comando:
            separa = comando.split()
            ponto = int(separa[1])
            no = arvore.procurar(ponto)
            antecessor = arvore.antecessor(no)
            sucessor = arvore.sucessor(no)
            if antecessor == None and sucessor == None:
                print('Apenas {} existe no sistema...'.format(no.nome))
            elif antecessor == None and sucessor != None:
                print('{} e o menor! e logo apos vem {}'.format(no.nome, sucessor.nome))
            elif antecessor != None and sucessor == None:
                print('{} e o maior! e logo atras vem {}'.format(no.nome, antecessor.nome))
            elif antecessor != None and sucessor != None:
                print('{} vem apos {} e antes de {}'.format(no.nome, antecessor.nome, sucessor.nome))


if __name__ == '__main__':
    main()