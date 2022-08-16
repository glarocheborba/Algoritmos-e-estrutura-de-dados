# Uma das partes mais cruciais nos sistemas operacionais é a forma que o sistema escalona o tempo de execução para um processo. Em outras palavras, é como o SO divide o tempo que o processador vai executar um certo programa.

# Você será encarregado de, ao receber uma lista de Processos, agenda-los em uma linha de execução e executa-los de acordo com o tempo que o processador disponibilizar. Um processo termina de executar quando seu tempo requerido chega à zero. Cada processo tem um id e um tempo requerido. Ao fim de cada execução, você deve informar quantos processos ainda estão na linha de execução.

# A primeira linha do Input será sempre um inteiro N que diz o número de comandos que serão enviados.

# Comandos:
# ADD ID T -> Insere uma música de id ID e tempo requerido T.
# EXE D -> O processador disponibiliza D segundos para a execução.
# OBS:
# Os processos são executados de acordo com a frente da linha de execução.
# Se um processo não terminou a execução, ele deve ser enviado para o fim da linha de execução, com o seu tempo requerido atualizado.
# Todos os processos, ao serem agendados, devem ser enviados para o fim da linha de execução.
# Se sobrar tempo disponibilizado e o atual processo na frente da linha finalizar, o próximo da linha deve ser executado, até que a linha esteja vazia ou o tempo disponibilizado finalize.

class nodeList:
    def __init__(self, id, tempo):
        self.id = id
        self.tempo = tempo
        self.proximo = None

class fila:
    def __init__(self):
        self.cabeca = None
        self.cauda = None
        self.linha = 0

    def add(self, id, tempo):
        node = nodeList(id,tempo)
        if self.cabeca == None:
            self.cabeca = node
            self.cauda = node
        else:
            self.cauda.proximo = node
            self.cauda = node
        self.linha += 1
        print('O programa {} foi agendado com sucesso!'.format(node.id))
        
    def exe(self, D):
        while self.cabeca != None and D != 0:    
            if 0 < D < self.cabeca.tempo:
                t = self.cabeca.tempo
                t = t - D
                print('O programa {} executou por {} segundos.'.format(self.cabeca.id,D))
                self.cabeca.tempo = t
                D = 0
                if self.cabeca.proximo != None:
                    primeiroDaFila = self.primeiroFila()
                    self.cabeca = self.cabeca.proximo
                    self.cauda.proximo = primeiroDaFila
                    self.cauda = primeiroDaFila
                elif self.cabeca.proximo == None:
                    primeiroDaFila = self.primeiroFila()
                    self.cabeca = primeiroDaFila
                    self.cauda = primeiroDaFila
            elif D >= self.cabeca.tempo:
                print('O programa {} executou por {} segundos.'.format(self.cabeca.id,self.cabeca.tempo))
                print('O programa {} terminou.'.format(self.cabeca.id))
                D -= self.cabeca.tempo
                self.remove()
                self.linha -= 1

    def remove(self):
        self.cabeca = self.cabeca.proximo
        if self.cabeca == None:
            self.cauda = None
    
    def primeiroFila(self):
        primeiroFila = self.cabeca
        return primeiroFila

def main():
    n = int(input())
    Fila = fila()
    for i in range(n):
        comando = input()
        if 'ADD' in comando:
            separa = comando.split()
            id = int(separa[1])
            tempo = int(separa[2])
            Fila.add(id, tempo)
        elif 'EXE' in comando:
            separa = comando.split()
            D = int(separa[1])
            Fila.exe(D)
            linha = Fila.linha
            print('A linha possui {} programas.'.format(linha))

if __name__ == '__main__':
    main()
