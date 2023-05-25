class Conta:

   def __init__(self,numConta,nome,tipoConta):
       self.numConta=numConta
       self.saldo=0
       self.statusdaConta=False
       self.nome=nome
       self.tipoConta=tipoConta
       self.valorLimite=0


   def depositar (self,depositar):
       self.saldo += depositar
       if self.statusdaConta == False:
           print(f'nao foi possivel realizar o deposito')

       else:
           print(f'{self.saldo} saldo total')

   def sacar (self, valorsacar):
       self.saldo -= valorsacar
       if self.statusdaConta == True :
           print(f'{self.saldo}')
           print(f'saque realizado')

       else:
           print(f'{self.saldo} saldo total')


   def verifSaldo(self):
          print(f'{self.saldo}')

   def ativar(self):
       if self.statusdaConta == False:
           print(f' conta ativa')
           self.statusdaConta= True
       else:
           print(f'conta ja ativa')

   def desativar(self):
       if self.saldo == True:
           print(f'{self.desativar} conta desativada')
           self.desativar = False
       else:
           print(f'conta desativada')

   def ativarcredito(self,valorLiberado):
       if self.statusdaConta:
           self.valorLimite = valorLiberado
           print(f'valor de limite liberado: {self.valorLimite}')
       else:
           print(f'nao e possivel liberar limite. a conta esta desativada.')

   def desativarcredito(self):
       if self.statusdaConta:
           self.valorLimite=0
           print(f'valor do limite bloqueado')
       else:
           print('nao é possivel bloquear limite. a conta esta desativada')

cont = Conta(20,"narjiara","corrente")

cont.ativar()
cont.depositar(10)
cont.verifSaldo()
cont.sacar(5)
cont.verifSaldo()
cont.desativar()
cont.verifSaldo()
cont.ativarcredito(50)
cont.sacar(5)
cont.verifSaldo()
cont.desativar()
cont.desativarcredito()
