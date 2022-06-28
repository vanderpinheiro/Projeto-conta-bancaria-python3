from conta import Conta

class ContaPoupanca(Conta):
    def sacar(self,valor):
        if not isinstance(valor,(int,float)):
            print('O valor a ser sacado precisa ser um número')
            return
        if self.saldo < valor:
            print(f'Seu salado é R${self.saldo}, você não pode sacar R${valor}.\n Saldo insuficiente')
            return
        self.saldo -= valor
        print(f'Você sacou {valor}')
        self.detalhes()