class Grafo:
    def __init__(self, vertices, arestas):
        self.V = vertices
        self.qtdV = len(vertices)
        self.A = arestas
    def adj(self, v):
        return self.A[v]
    def qtdeVertices(self):
        return len(self.V)


def bfs(g,V_init,v_fim ): 
    marcado = g.qtdV*[False]
    antecessor = g.qtdV*[-1]
    vertices = list()
    for i in range(V_init,g.qtdV):
        if not marcado[i]:
            vertices.append(i)
            marcado[i] = True
            while len(vertices) > 0:
                v = vertices.pop(0)
                for u in g.adj(v):
                    if not marcado[u]:
                        marcado[u] = True
                        antecessor[u] = v
                        vertices.append(u)
    # for i in range(V_init,g.qtdV):
    #     print(antecessor[i])
    caminho(V_init,v_fim,antecessor)
    del marcado
    del antecessor

def caminho(origem,v,antecessor):
    if origem == v:
        print(v)
    elif antecessor[v] == -1:
        print('nao ha caminho')
    else:
        caminho(origem,antecessor[v],antecessor)
        print(v)

vertices=[0,1,2,3,4,5,6,7]
arestas = {0:[2], 1:[0,2,3], 2:[5,6], 3:[7], 4:[7], 5:[7], 6:[4,7], 7:[]}

g = Grafo(vertices, arestas)
bfs(g,0,7)