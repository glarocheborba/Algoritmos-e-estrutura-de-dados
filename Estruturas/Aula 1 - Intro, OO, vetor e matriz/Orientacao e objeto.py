class pessoa:
    def __init__(self, initNome, initIdade, initEndereco):
        self.nome = initNome
        self.idade = initIdade
        self.endereco = initEndereco
    def imprimeDados(self):
        print(self.nome, self.idade, self.endereco)
    def fazAniversario(self):
        self.idade += 1
    def atualizaEndereco(self, novoEndereco):
        self.endereco = novoEndereco
    def retornarAnoNascimento(self):
        return 2022-self.idade

def moraMesmoEndereco(pessoa1, pessoa2):
    if (pessoa1.endereco == pessoa2.endereco):
        return True
    else:
        return False

p1 = pessoa('Gabriel Laroche Borba', 18, 'Recife-PE')
p2 = pessoa('Miguel Borba', 11, 'Recife-PE')

print(p1.nome)
print(p2.nome)
p1.imprimeDados()
p2.imprimeDados()
print('-'*50)
p1.fazAniversario()
p1.atualizaEndereco('Sao paulo-SP')
p1.imprimeDados()

print(moraMesmoEndereco(p1, p2))

print(p1.retornarAnoNascimento())