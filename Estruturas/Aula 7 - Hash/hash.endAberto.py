from tkinter import N


def hashFuncao(elem):
    return (elem**2+30*elem)%20

def hashColisao(elem, i):
    return (hashFuncao(elem)+i)%20

def hashInserir(T,elem,N):
    i = 0
    while i < N:
        posicao = hashColisao(elem,i)
        if T[posicao] == None or T[posicao] == 'disponivel':
            T[posicao] = elem
            return posicao
        else:
            i += 1
    return print('Tabela cheia')

def hashProcurar(T,elem,N):
    i = 0
    while i < N:
        posicao = hashColisao(elem,i)
        if T[posicao] == elem:
            return posicao
        elif T[posicao] == None or T[posicao] == 'disponivel':
            return None
        else:
            i += 1
    return None
    
def delete(T,elem,N):
    i = 0
    while i < N:
        posicao = hashColisao(elem,i)
        if T[posicao] == elem:
            T[posicao] = 'disponivel'
            return posicao
        else:
            i += 1
    return None

N = int(input('Digite o tamanho da tabela Hash: '))
T = [None]*N
comando = input()
while comando != 'end':
    if 'add' in comando:
        separa = comando.split()
        num = int(separa[1])
        posicao = hashInserir(T,num,N)
        print(T)
    elif 'del' in comando:
        separa = comando.split()
        num = int(separa[1])
        posicao = delete(T,num,N)
        if posicao != None:
            print(T)
        else:
            print('Nao encotrado')
    elif 'procurar' in comando:
        separa = comando.split()
        num = int(separa[1])
        posicao = hashProcurar(T,num,N)
        if posicao != None:
            print(f'O elemento esta na posicao {posicao}')
        else:
            print(f'Nao encontrado')
    comando = input()
