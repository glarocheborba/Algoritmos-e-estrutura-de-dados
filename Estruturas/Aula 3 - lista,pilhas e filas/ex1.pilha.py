class pilha: 
    def __init__(self):
        self.pilha = [None]*6
        self.topo = 0
    
    def stack_empty(self):
        if self.topo == 0:
            return True
        else: 
            return False
        
    def push(self,x):
        self.pilha[self.topo] = x
        self.topo += 1

    def pop(self):
        if self.stack_empty() == True:
            print('Pilha vazia.')
        else: 
            self.pilha[self.topo - 1] == None
            self.topo -= 1

def Comandos(): 
    print('"push" - para adicionar em sua pilha.')
    print('"pop" - para eleiminar um elemento de sua pilha' )

S = pilha()

while True: 
    Comandos()
    if len(S.pilha) == S.topo:
        print('Pilha cheia!')
    else: 
        S.push(int(input('Digite um valor: ')))
        print(S.pilha)
        



# S = [1,2,3,4,5,6]

# def push(conjunto, elemento):
#     conjunto.append(elemento)

# def pop(conjunto):
#     if  conjunto == []:
#         print('Pilha Vazia')
#     else:
#         conjunto.remove(conjunto[-1])
