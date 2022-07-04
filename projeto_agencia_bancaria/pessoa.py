from datetime import datetime


class Pessoa:
    data_hoje = datetime.today().strftime('%d/%m/%Y')

    def __init__(self, nome, idade):
        self._nome = nome
        self._idade = idade

    @property
    def nome(self):
        return self._nome

    @property
    def idade(self):
        return self._idade


class Cliente(Pessoa):
    def __init__(self, nome: str, idade: int):
        super().__init__(nome, idade)
        self.conta = None

    def criar_conta(self, conta):
        self.conta = conta
        # print(f'Conta de {self.nome} criada com sucesso.')

    def detalhe_cliente(self):
        print(f'Nome: {self.nome}')
        print(f'Idade: {self.idade}')
        self.conta.detalhes()
