# Você bateu a cabeça com bastante força enquanto andava de bicicleta pelo Centro de Informática da UFPE. Felizmente, você passa bem. Há um porém: você agora é viciado no jogo dos extremos. O jogo é muito simples: você recebe uma sequência de inteiros S e uma constante A, e a cada rodada você deve realizar a seguinte operação:

# Seja max o maior elemento de S e min o menor elemento de S :

# Remova max de S

# Faça: K = max - | min * A |

# Se K > 0, coloque K em S e parta para a próxima rodada.

# Senão, parta para a próxima rodada.

# O jogo acaba quando não há mais nenhum elemento em S. Recebendo S e A, descubra em quantas rodada o jogo acabará!

# Exemplo:
# Entrada: 5 5 8 11 2

# Rodada 1:

# S (Em ordem decrescente): 11 8 5 5
# Operação: 11 - |5 * 2| = 1
# Rodada 2:

# S: 8 5 5 1
# Operação: 8 - |1 * 2| = 6
# Rodada 3:

# S: 6 5 5 1
# Operação: 6 - |1 * 2| = 4
# Rodada 4:

# S: 5 5 4 1
# Operação: 5 - |1 * 2| = 3
# [...]

# Rodada 10:

# S: 1 1 1
# Operação: 1 - |1 * 2| = -1
# Rodada 11:

# S: 1 1
# Operação: 1 - |1 * 2| = -1
# Rodada 12:

# S: 1
# Operação: 1 - |1 * 2| = -1
# Após a 12 segunda rodada, S está vazia. Logo, foram necessárias 12 rodadas para o jogo acabar.

def esquerda(i):
    return 2 * i

def direita(i):
    return 2 * i + 1

def pai(i):
    return i//2

def heapfy(v,i,n):
    esq = esquerda(i)
    dir = direita(i)

    if esq < n and v[esq] > v[i]:
        maior = esq
    else:
        maior = i

    if dir < n and v[dir] > v[maior]:
        maior = dir

    if maior != i:
        v[i], v[maior] = v[maior], v[i]
        heapfy(v,maior,n)   

# def montarHeapmax(v,n):
#     for i in range((n//2),0,-1):
#         heapfy(v,i,n)

def heap_increase(v,i):
    while i > 1 and v[pai(i)] < v[i]:
        p1 = pai(i)
        v[i], v[p1] = v[p1], v[i]
        i = pai(i)
        
def max_heap_insert(v,elem,n):
    v.append(elem)
    heap_increase(v,n)

def heap_delete(v,n):
    n -= 1
    v[1],v[n] = v[n], v[1]
    heapfy(v,1,n)
    return n

def verificaJogada(lista,constante):
    num_jogadas = 0
    lista_jogo = [99999999]
    min = 100001
    n = 1
    for j in lista:
        max_heap_insert(lista_jogo,int(j),n)
        if min > int(j):
            min = int(j)
        n += 1

    while n > 1 :
        lista_jogo, n, min = joga(lista_jogo,constante,n,min)
        num_jogadas += 1
    print('{} rodadas!'.format(num_jogadas))

def joga(lista,constante,n,min):
    elem_substiui = (lista[1] - abs(min*constante))
    if elem_substiui > 0:
        lista[1] = elem_substiui
        heapfy(lista,1,n)
        if elem_substiui <= min:
            min = elem_substiui
    else:
        n = heap_delete(lista,n)
    
    return lista,n,min

def main():
    comando = input()
    lista = comando.split()
    constante_a = int(input())
    verificaJogada(lista,constante_a,)
    

if __name__ == '__main__':
    main()
