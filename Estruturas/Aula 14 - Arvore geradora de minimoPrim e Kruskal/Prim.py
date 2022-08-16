class Grafo:
    def __init__(self, vertices):
        self.vertices = vertices
        self.grafo = []

    def add_aresta(self, V_init, V_fim, custo):
        self.grafo.append([V_init, V_fim, custo])
    
    def minkey(self, key, mstSet):
        min = 99999999999
        for i in range(self.vertices):
            if key[i] < min and mstSet[i] == False:
                min = key[i]
                min_index = i
        
        return min_index
        
    def PrimMST(self):
        key = [999999999999] * self.vertices
        antecessor = [None] * self.vertices

        key[0] = 0
        mstSet = [False] *self.vertices

        antecessor[0] = -1

        for cout in range(self.vertices):
            u = self.minkey(key, mstSet)
            mstSet[u] = True

            for v in range(self.vertices):
                if self.grafo[u][v] > 0 and mstSet[v] == False and key[v] > self.grafo[u][v]:
                    key[v] = self.grafo[u][v]
                    antecessor[v] = [u]

        
           
def main():
    comando = input()
    vert_e_ares = comando.split()
    G = Grafo(int(vert_e_ares[0]))
    for i in range(int(vert_e_ares[1])):
        entrada = input()
        vInit_vFim_custo = entrada.split()
        G.add_aresta(int(vInit_vFim_custo[0]),int(vInit_vFim_custo[1]), int(vInit_vFim_custo[2]))


if __name__ == '__main__':
    main()