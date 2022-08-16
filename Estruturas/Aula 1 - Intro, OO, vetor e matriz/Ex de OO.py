# class Conta:
#     def __init__(self, initCPF, initValorInicial):
#         self.cpf = initCPF
#         self.saldo = initValorInicial
#         self.taxaSaque = 0.25
#     def fazerSaque(self, valor):
#         self.saldo -= valor + self.taxaSaque
#     def retornaSaldo(self):
#         return self.saldo

# conta1 = Conta("111-222-333-4", 100)
# conta1.fazerSaque(40)
# print(conta1.retornaSaldo())

class Conta:
    def __init__(self, initCPF, initValorInicial):
        self.__cpf = initCPF
        self.__saldo = initValorInicial
        self.__taxaSaque = 0.001
    def fazerSaque(self, valor):
        self.__saldo -= valor + valor*self.__taxaSaque
    def retornaSaldo(self):
        return self.__saldo

conta1 = Conta("111-222-333-4", 100)
conta1.fazerSaque(40)
print(conta1.retornaSaldo())
conta1.__saldo=2
print(conta1.__saldo)
print(conta1.retornaSaldo())