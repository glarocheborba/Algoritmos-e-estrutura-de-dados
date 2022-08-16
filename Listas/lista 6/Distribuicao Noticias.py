# Em uma rede social, há n usuários se comunicando entre si e m conexões de amizade. O processo de distribuição de notícias funciona da seguinte maneira:

# Um usuário i (1 <= i <= n) recebe a notícia de alguma fonte. Então, esse usuário passa a notícia para seus amigos, os amigos repassam para seus amigos e assim em diante. O processo acaba quando não há um par de amigos em que um sabe a notícia e o outro não.

# Para cada usuário i (1 <= i <= n), determine a quantidade de usuários que saberia a notícia se i iniciasse a distruição.

class Grafo:
    def __init__(self, vertices):
        self.vertices = vertices
        self.grafo = [[] for i in range(self.vertices)]

    def add_aresta(self, V_init, V_fim):
        self.grafo[V_init-1].append(V_fim)
        self.grafo[V_fim-1].append(V_init)
    
    def qtd_distribuidos(self, v, lista):
        for i in self.adj(v):
            if i not in lista:
                lista.append(i)
                self.qtd_distribuidos(i-1, lista)
        return lista
        
    def adj(self,V):
        return self.grafo[V]


def main():
    qtd_vertices = input()
    vert_are = qtd_vertices.split()
    conexoes = int(vert_are[1])
    G = Grafo(int(vert_are[0]))
    for j in range(conexoes):
        comando = input()
        vertices = comando.split()
        G.add_aresta(int(vertices[0]), int(vertices[1]))
    lista_print = [0]*G.vertices
    for i in range(G.vertices):
        lista = [i+1]
        lista = G.qtd_distribuidos(i,lista)
        lista_print[i] = str(len(lista))
    
    resultado = ' '.join(lista_print)
    print(resultado)

    

if __name__ == '__main__':
    main()
