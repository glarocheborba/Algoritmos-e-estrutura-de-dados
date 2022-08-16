# Você foi contratado por uma empresa de aviação na tentativa de diminuir o custo de sua malha aérea. Eles querem que você desenvolva um sistema que irá receber todos os trechos (ida e volta) com seus respectivos custos, e retorne qual o menor custo possível para a empresa, de modo que, partindo de qualquer cidade, os destinos diretos ou indiretos antes das alterações se mantenham.

class Grafo:
    def __init__(self, vertices):
        self.vertices = vertices
        self.grafo = []

    def add_aresta(self, V_init, V_fim, custo):
        self.grafo.append([V_init, V_fim, custo])
    
    def procurar(self, antecessor, i):
        if antecessor[i] == i:
            return i
        return self.procurar(antecessor, antecessor[i])

    def uniao(self, antecessor, rank, x, y):
        xraiz = self.procurar(antecessor, x)
        yraiz = self.procurar(antecessor, y)

        if rank[xraiz] < rank[yraiz]:
            antecessor[xraiz] = yraiz
        elif rank[xraiz] > rank[yraiz]:
            antecessor[yraiz] = xraiz
        else:
            antecessor[yraiz] = xraiz
            rank[xraiz] += 1
        
    def Kruskal(self):
        result = []
        custo_min = 0
        i = 0
        e = 0
        
        def particao(v,esq,dir):
            pivo = v[esq][2]
            i = esq 
            j = dir + 1
            while True:
                i += 1
                while v[i][2] < pivo:
                    if i >= dir:
                        break
                    i += 1
                j -= 1
                while v[j][2] > pivo:
                    if j <= esq:
                        break
                    j -= 1
                if i >=j:
                    break
                v[i], v[j] = v[j],v[i]
            v[esq],v[j] = v[j],v[esq]
            return j

        def qs(v,esq,dir):
            if esq < dir:
                p = particao(v,esq,dir)
                qs(v,esq,p-1)
                qs(v,p+1,dir)

        def quicksort(v,n):
            qs(v,0,n-1)

        quicksort(self.grafo, len(self.grafo))

        antecessor = []
        rank = [0] * self.vertices

        for i in range(self.vertices):
            antecessor.append(i)
        
        j = 0
        while e < self.vertices - 1:
            V_init, V_fim, custo = self.grafo[j]
            j += 1
            x = self.procurar(antecessor, V_init)
            y = self.procurar(antecessor, V_fim)

            if x != y:
                e += 1
                result.append([V_init, V_fim, custo])
                custo_min += custo
                self.uniao(antecessor, rank, x, y)
        return custo_min
            
def main():
    comando = input()
    vert_e_ares = comando.split()
    G = Grafo(int(vert_e_ares[0]))
    for i in range(int(vert_e_ares[1])):
        entrada = input()
        vInit_vFim_custo = entrada.split()
        G.add_aresta(int(vInit_vFim_custo[0]),int(vInit_vFim_custo[1]), int(vInit_vFim_custo[2]))

    custo_min = G.Kruskal()
    print(custo_min)
    
if __name__ == '__main__':
    main()
