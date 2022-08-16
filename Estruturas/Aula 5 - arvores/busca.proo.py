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
        if node is None:
            node = self.raiz
        print(node)
        while node.esquerda:
            node = node.esquerda
        return node

    def maxArvore(self,node):
        if node is None:
            node = self.raiz
        print(node)
        while node.direita:
            node = node.direita
        return node

    def em_ordem(self, node=None):
        if node == None:
            node = self.raiz
        if node.esquerda:
            self.em_ordem(node.esquerda)
        print(node.nome,node.ponto)
        if node.direita:
            self.em_ordem(node.direita)

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
    
    def inserir(self,node):
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


    def transplante(self,node,novo_node):
        if node.pai == None:
            self.raiz = novo_node
        elif node == node.pai.esquerda:
            node.pai.esquerda = novo_node
        else:
            node.pai.direita = novo_node
        if novo_node != None:
            novo_node.pai = node.pai

    def remover(self,node):
        if node.esquerda == None:
            ArvoreBinaria.transplante(self,node,node.direita)
        elif node.direita == None:
            ArvoreBinaria.transplante(self,node,node.esquerda)
        else:
            y = ArvoreBinaria.minArvore(self,node.direita)
            if y.pai != node:
                ArvoreBinaria.transplante(self,y,y.direita)
                y.direita = node.direita
                y.direita.pai = y
            ArvoreBinaria.transplante(self,node,y)
            y.esquerda = node.esquerda
            y.esquerda.pai = y

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
                arvore.inserir(node)
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

        elif 'REMOVE' in comando:
            separa = comando.split()
            ponto = int(separa[1])
            no = arvore.procurar(ponto)
            arvore.remover(no)
            print('{} removido com sucesso'.format(no.nome))
    
        elif 'MIN' in comando:
            min = arvore.minArvore(None)
            print(min.nome, min.ponto)

        elif 'MAX' in comando:
            node = Node(None,None)
            max = arvore.maxArvore(node)
            print(max.nome, max.ponto)

if __name__ == '__main__':
    main()