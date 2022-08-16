
class dicionario:
    def __init__(self,chave, dado):
        self.chave = chave
        self.dado = dado 
        self.proximo = None

    def rank(self,chave):
        inicio = 0 
        fim = self.N-1 
        while inicio <= fim:
            meio = (fim + inicio)/2
            if chave 

d = dicionario()
palavra = input()
while palavra != '':
    if d.contem(palavra):
        d.inserir(palavra, d.valor(palavra)+1)
    else:
        d.inserir(palavra,0)

pMax = ''
freqMax = 0
for palavra in d.chaves():
    if d.valor(palavra) > freqMax:
        pMax = palavra
        freqMax = d.valor(palavra)
print(f'A palavra mais frequente é {pMax} e com {freqMax} ocorrencias.')

