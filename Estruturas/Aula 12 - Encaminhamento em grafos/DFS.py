class Grafo:
    def __init__(self, vertices, arestas):
        self.V = vertices
        self.qtdV = len(vertices)
        self.A = arestas
    def adj(self, v):
        return self.A[v]
    def qtdeVertices(self):
        return len(self.V)
    # def imprimeGrafo(self):
    #     for v in self.V:
    #       print("vertice", v, "-> ", self.adj(v))

def buscaProfundidade(g, listaOT):
    marcado =  [False]*g.qtdV
    antecessor = [-1]*g.qtdV
    for v in range(g.qtdV):
        if not marcado[v]:
            dfs(g,v,antecessor,marcado)
    for i in range(g.qtdV):
        antecessor[i]
    del marcado
    del antecessor

def dfs(g,v,antecessor,marcado):
    marcado[v] = True
    for u in g.adj(v):
        if not marcado[u]:
            antecessor[u] = v
            dfs(g,u,antecessor,marcado)


vertices=[0,1,2,3,4,5,6,7]
arestas = {0:[1,3], 1:[2,5], 2:[], 3:[], 4:[], 5:[6], 6:[], 7:[]}
g = Grafo(vertices, arestas)
listaOT = []
buscaProfundidade(g,listaOT)
print(listaOT)

# buscaProfundidade(g)
# g.imprimeGrafo()