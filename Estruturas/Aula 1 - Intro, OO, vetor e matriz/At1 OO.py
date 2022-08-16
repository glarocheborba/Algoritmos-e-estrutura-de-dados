class Aluno:
    def __init__(self, initNome, initCPF):
        self.nome = initNome
        self.CPF = initCPF
    def inicializarNota(self, nota, numeroProva):
        
    def verificaSituacaoMedia(self):

        

continuaPrograma = True
while continuaPrograma:
    nomeAluno = input('Digite o nome do aluno: ')
    cpfAluno = input('digite o CPF desse aluno: ')
    while cpfAluno < 0 :
        cpfAluno = input('digite o CPF desse aluno: ')
    aluno = Aluno(nomeAluno, cpfAluno)
    numeroProva = int(input('Digite o numero da prova: '))
    while numeroProva < 1 or numeroProva > 3:
        numeroProva = int(input('Digite o numero da prova: '))   
    notaAluno = int(input('Digite a nota do aluno: '))
    aluno.inicializarNota(notaAluno, numeroProva)
       