from conta import Conta

class ContaCorrente(Conta):
    def __init__(self,agencia,conta,saldo,limite=100):
        super().__init__(agencia,conta,saldo)
        self._limite = limite
    def limite(self):
        return self._limite
    def sacar(self,valor):
        if not isinstance(valor,(int,float)):
            print('O valor a ser sacado precisa ser um número.')
            return
        if self.saldo + self.limite < valor:
            print(f'Seu salado é R${self.saldo}, você não pode sacar R${valor}.\n Saldo insuficiente')
            return
        self.saldo -= valor
        self.detalhes()