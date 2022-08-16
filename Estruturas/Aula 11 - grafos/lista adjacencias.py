class Grafo:
    def __init__(self, vertices):
        self.vertices = vertices
        self.grafo = [[] for i in range(self.vertices)]

    def add_aresta(self, V_init, V_fim):
        self.grafo[V_init-1].append(V_fim)
        #self.grafo[V_fim-1].append(V_init)

    def print_lista(self):
        for i in range(self.vertices):
            print(f'{i+1}:', end=' ')
            for j in self.grafo[i]:
                print(f'{j} > ', end=' ')
            print()
    
    def adj(self,V):
        return self.grafo[V]


def main():
    qtd_vertices = int(input('Digite a quantidade de vertices: '))
    Graf = Grafo(qtd_vertices)
    comando = input()
    while comando != 'fim':
        if 'add' in comando:
            vertices = comando.split()
            Graf.add_aresta(int(vertices[1]), int(vertices[2])) 
        elif 'print' in comando: 
            Graf.print_lista()
        comando = input()

if __name__ == '__main__':
    main()
