# Um estudante da disciplina de Algoritmos e Estruturas de Dados resolveu treinar suas habilidades com grafos. Basicamente, a ideia foi implementar um algoritmo com o objetivo de encontrar a rota com menor custo em um grafo conexo e determinar a existência de ciclos negativos. Os grafos utilizados sempre serão conexos, dirigidos e pesados (com um custo associado a cada uma das arestas do grafo).

class Grafo:
    def __init__(self, vertices):
        self.vertices = vertices
        self.grafo = []

    def add_aresta(self, V_init, V_fim, custo):
        self.grafo.append([V_init, V_fim, custo])
    
    def bellman_ford(self, init):
        distan = [9999999999999999] * self.vertices
        distan[init] = 0
        antecessor = [-1] * self.vertices

        for i in range(self.vertices - 1 ):
            for V_init, V_fim, custo in self.grafo:
                if distan[V_init] != 9999999999999999 and distan[V_fim] > distan[V_init] + custo:
                    distan[V_fim] = distan[V_init] + custo
                    antecessor[V_fim] = V_init

        for V_init, V_fim, custo in self.grafo:
            if distan[V_init] != 9999999999999999 and distan[V_fim] > distan[V_init] + custo:
                print('Ciclo negativo encontrado!')
                return
        
        for i in range(self.vertices):
            print('Vertice: {} Antecessor: {} Distancia: {}'.format(i, antecessor[i], distan[i]))


def main():
    qtd_grafos = int(input())
    for i in range(qtd_grafos):
        comando = input()
        vert_e_ares = comando.split()
        G = Grafo(int(vert_e_ares[0]))
        for i in range(int(vert_e_ares[1])):
            entrada = input()
            vInit_vFim_custo = entrada.split()
            G.add_aresta(int(vInit_vFim_custo[0]),int(vInit_vFim_custo[1]), int(vInit_vFim_custo[2]))
        init = int(input())
        G.bellman_ford(init)

if __name__ == '__main__':
    main()
