class Ingresso:
    def __init__(self,reais):
        self.reais=reais

    def imprimeValor(self):
        print(f'{self.reais}')

class Vip (Ingresso):
    def __init__(self,reais):
         super(). __init__(reais)


    def imprimeValor(self,valorAdicional):
        self.valorAdicional = valorAdicional
        self.reais += valorAdicional
        print(f'{self.reais}')


ingresso = Ingresso(10)
vip = Vip (15)
ingresso.imprimeValor()
vip.imprimeValor(50)
