class Node:
    def __init__(self, ponto):
        self.ponto = ponto
        self.esquerda = None 
        self.direita = None
        self.pai = None

class ArvoreBinaria:
    def __init__(self, ponto):
        if ponto != None:
            node = Node(ponto)
            self.raiz = node
        else:
            self.raiz = None

    def em_ordem(self, node=None):
        if node == None:
            node = self.raiz
        if node.esquerda:
            self.em_ordem(node.esquerda)
        print(node.ponto)
        if node.direita:
            self.em_ordem(node.direita)
    
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


def main():
    node = None
    arvore = ArvoreBinaria(None)
    comando = input()
    lista = comando.split()
    for i in lista:
        node = Node(int(i))
        arvore.inserir(node)
    print('-------------------------------------')
    arvore.em_ordem(None)

if __name__ == '__main__':
    main()

