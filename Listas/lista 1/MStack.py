# Uma pilha é um tipo abstrato de dado e estrutura de dados baseado no princípio de Last In First Out (LIFO), ou seja "o último que entra é o primeiro que sai" caracterizando um empilhamento de dados. Pilhas são fundamentalmente compostas por duas operações: push que adiciona um elemento no topo da pilha e pop que remove o último elemento adicionado. Seu objetivo é desenvolver um tipo diferente de pilha, a qual é composta pelas seguintes operações:

# push x : Insere um novo elemento.
# getMax : Consulta o maior elemento da pilha.
# getMin : Consulta o menor elemento da pilha.
# pop : Remove o elemento no topo da pilha.

class nodeList:
    def __init__(self,elem):
        self.elem = elem
        self.next = None
        self.last = None

def push(nodeStart,elem):
    node = nodeList(elem)
    if nodeStart == None:
        nodeStart = node
    else:
        nodeStart.next = node
        node.last = nodeStart
        nodeStart = node
    return nodeStart

def pop(nodeStart):
    if nodeStart == None:
        print('empty stack')
    elif nodeStart.last == None:
        print(nodeStart.elem)
        nodeStart = None
    else:
        print(nodeStart.elem)
        nodeStart = nodeStart.last
        nodeStart.next = None
    return nodeStart


def getMin(nodeStart):
    y = nodeStart
    elemMin = 999999999
    if nodeStart == None:
        print('empty stack')
    else:
        while y!= None:
            if y.elem < elemMin:
                elemMin = y.elem
            y = y.last
        print(elemMin)

def getMax(nodeStart):
    y = nodeStart
    elemMax = -999999999
    if nodeStart == None:
        print('empty stack')
    else:
        while y!= None:
            if y.elem > elemMax:
                elemMax = y.elem
            y = y.last
        print(elemMax)

def main():
    nodeStart = None
    n = int(input())
    for i in range(n):
        comando = input()
        if 'push' in comando:
            separa = comando.split()
            num = int(separa[1])
            nodeStart = push(nodeStart, num)
        elif 'pop' in comando:
            nodeStart = pop(nodeStart)
        elif 'getMax' in comando:
            getMax(nodeStart)
        elif 'getMin' in comando:
            getMin(nodeStart)
        
if __name__ == '__main__':
    main()