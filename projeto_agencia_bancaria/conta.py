from abc import ABC, abstractmethod


class Conta(ABC):
    def __init__(self, agencia, num_conta, saldo):
        # if len(agencia) != 4:
        #     raise Exception('A agência deve ser um número inteiro de 4 dígitos')
        # if len(num_conta) != 6:
        #     raise Exception('A agência deve ser um número inteiro de  dígitos')
        self._agencia = agencia
        self._num_conta = num_conta
        self._saldo = saldo

    @property
    def agencia(self):
        return self._agencia

    @property
    def num_conta(self):
        return self._num_conta

    @property
    def saldo(self):
        return self._saldo

    @saldo.setter
    def saldo(self, valor):
        if not isinstance(valor, (int, float)):
            print('O saldo deve ser somente um valor numérico')
            return
        self._saldo = valor

    def depositar(self, valor: int):
        if not isinstance(valor, int):
            print('O valor a ser depositado precisa ser um número inteiro.')
            return
        self.saldo += valor
        print(f'Você depoisitou R${valor}.')
        self.detalhes()

    def detalhes(self):
        print(f'Tipo de Conta: {self.__class__.__name__}')
        print(f'Agência:{self.agencia}, Conta:{self.num_conta}, Saldo:R${self.saldo} \n')
        if self.saldo < 0:
            print('Atenção, você está usando o limite da sua conta!\n')

    @abstractmethod
    def sacar(self, valor):
        pass


class ContaCorrente(Conta):
    def __init__(self, agencia, num_conta, saldo, limite=100):
        super().__init__(agencia, num_conta, saldo)
        self.limite = limite

    def sacar(self, valor):
        if valor > self.saldo + self.limite:
            print(f'Saldo insuficiente para sacar R${valor}.')
            return
        self.saldo -= valor
        self.detalhes()


class ContaPoupanca(Conta):
    def sacar(self, valor):
        if valor > self.saldo:
            print(f'Saldo insuficiente para sacar R${valor}.')
            return
        self.saldo -= valor
        print(f'Você sacou R${valor}.')
        self.detalhes()
