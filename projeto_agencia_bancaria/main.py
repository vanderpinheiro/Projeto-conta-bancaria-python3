from banco import Banco
from conta import ContaCorrente, ContaPoupanca
from pessoa import Cliente

banco = Banco()
cliente1 = Cliente('Vander Pinheiro',27)
banco.adicionar_cliente(cliente1)

conta1 = ContaCorrente(agencia=1111,num_conta=87653,saldo=0,limite=200)
banco.adicionar_conta(conta1)


cliente1.criar_conta(conta1)
cliente1.detalhe_cliente()
conta1.sacar(100)

cliente1.detalhe_cliente()

conta1.depositar(1000)

if banco.autenticar(cliente1):
    conta1.sacar(600)
else:
    print('Você não pode sacar,baby.')



# cliente1 = Cliente('Vander Pinheiro', 27)
# cliente2 = Cliente('Luiz Otávio', 34)
# cliente3 = Cliente('Isabella Lima', 26)
#
# conta1 = ContaPoupanca(1111, 234567, 0)
# conta2 = ContaCorrente(2222, 234123, 0)
# conta3 = ContaPoupanca(1178, 653456, 0)
#
# cliente1.criar_conta(conta1)
# cliente2.criar_conta(conta2)
# cliente3.criar_conta(conta3)
#
# banco.adicionar_cliente(cliente1)
# banco.adicionar_conta(conta1)
#
# # if banco.autenticar(cliente1):
# #     cliente1.conta.depositar(20)
# #     cliente1.conta.sacar(10)
# # else:
# #     print('Cliente não atenticado')
# #
# # print('##################' * 3)
# #
# banco.adicionar_cliente(cliente2)
# banco.adicionar_conta(conta2)
# #
# # if banco.autenticar(cliente2):
# #     cliente2.conta.depositar(20)
# #     cliente2.conta.sacar(100)
# # else:
# #     print('Cliente não atenticado')
#
# banco.listar_clientes()