from conta import ContaCorrente, ContaPoupanca


class Banco:
    def __init__(self):
        self.agencias = [1111, 2222, 3333]
        self.clientes = []
        self.contas_bank = []

    def autenticar(self, cliente):
        if cliente not in self.clientes:
            return False
        if cliente.conta not in self.contas_bank:
            return False
        if cliente.conta.agencia not in self.agencias:
            return False
        return True

    def adicionar_cliente(self, cliente):
        self.clientes.append(cliente)

    def adicionar_conta(self, conta):
        self.contas_bank.append(conta)

    def listar_contas(self):
        for conta in self.contas_bank:
            print(f'{conta.agencia, conta.num_conta, conta.saldo}')

    def listar_clientes(self):
        for cliente in self.clientes:
            print(f'Nome: {cliente.nome}, Idade:{cliente.idade}')
            cliente.conta.detalhes()
