class Grafo:
    def __init__(self, vertices):
        self.vertices = vertices
        self.grafo = [[0]*self.vertices for i in range(self.vertices)]

    def add_aresta(self, V_init, V_fim):
        self.grafo[V_init-1][V_fim-1] = 1
        # self.grafo[V_fim-1][V_init-1] = 1

    def print_matriz(self):
        for i in range(self.vertices):
            print(self.grafo[i])

def main():
    qtd_vertices = int(input('Digite a quantidade de vertices: '))
    Graf = Grafo(qtd_vertices)
    comando = input()
    while comando != 'fim':
        if 'add' in comando:
            vertices = comando.split()
            Graf.add_aresta(int(vertices[1]), int(vertices[2])) 
        elif 'print' in comando: 
            Graf.print_matriz()
        comando = input()

if __name__ == '__main__':
    main()
