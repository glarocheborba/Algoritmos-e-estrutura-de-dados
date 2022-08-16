from msvcrt import heapmin


class Grafo:
    def __init__(self, vertices):
        self.vertices = vertices
        self.grafo = [[] for i in range(self.vertices)]

    def add_aresta(self, V_init, V_fim):
        self.grafo[V_init-1].append(V_fim)
        # self.grafo[V_fim-1].append(V_init)

    def print_lista(self):
        for i in range(self.vertices):
            print(f'{i+1}:', end=' ')
            for j in self.grafo[i]:
                print(f'{j} > ', end=' ')
            print()
    
    def adj(self,V):
        return self.grafo[V]

def esquerda(i):
    return 2 * i

def direita(i):
    return 2 * i + 1

def pai(i):
    return i//2

def heapfy(v,i,n):
    esq = esquerda(i)
    dir = direita(i)

    if esq < n and v[esq] < v[i]:
        menor = esq
    else:
        menor = i

    if dir < n and v[dir] < v[menor]:
        menor = dir

    if menor != i:
        v[i], v[menor] = v[menor], v[i]
        heapfy(v,menor,n)   

def montarHeapmin(v,n):
    for i in range((n//2),0,-1):
        heapfy(v,i,n)

def heap_increase(v,i):
    while i > 1 and v[pai(i)] < v[i]:
        p1 = pai(i)
        v[i], v[p1] = v[p1], v[i]
        i = pai(i)
        
def max_heap_insert(v,elem,n):
    v.append(elem)
    heap_increase(v,n)

def heap_delete(v):
    n = len(v)
    n -= 1
    v[1],v[n] = v[n], v[1]
    v = v[:-1]
    heapfy(v,1,n)
    return n

def DIJKSTRA(G, w, s):
    p = [999999999999999]*G.vertices
    antecessor = [-1]*G.vertices
    F = []
    for v in range(G.vertices):
        F.append(v)
    p[s] = 0
    S = []
    montarHeapmin(F,G.vertices)
    while F != []:
        u = heap_delete(F)
        S.append(u)
        for v in G.adj(u):
            relaxa(u,v,w)
    
def relaxa()


def main():
    qtd_vertices = int(input('Digite a quantidade de vertices: '))
    G = Grafo(qtd_vertices)
    comando = input()
    while comando != 'fim':
        if 'add' in comando:
            vertices = comando.split()
            G.add_aresta(int(vertices[1]), int(vertices[2])) 
        elif 'print' in comando: 
            G.print_lista()
        elif 'dijkstra' in comando:
            DIJKSTRA(G,1,2)
        comando = input()

if __name__ == '__main__':
    main()