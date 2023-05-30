class atleta:
    def __init__(self,peso):
        self.peso=peso
        self.aquecer=False

class Corredor(atleta):

    def __init__(self,peso):
        super(). __init__(peso)
    def correr(self):

        if self.correr == False:
            print(f' esta correndo' )
            self.correr = True
        else:
            print(f'ja esta correndo')

    def  parardecorrer(self):
        if self.correr==True:
            print(f'parou de correr')
            self.correr=False
        else:
            print(f'nao esta correndo')

class Nadador(atleta):
    def __init__(self, peso):
        super().__init__(peso)
    def nadar(self,nadar):
        if self.corredor == True:
            print(f'nao pode nadar')
        elif self.nadar == True:
            print(f'ja esta nadando')
        else:
            print(f' esta nadando')

    def parardenadar(self):
        if self.nadar==True:
            print(f'parou de nadar')
            self.nadar=False
        else:
            print(f'nao esta nadando')
class Ciclista(atleta):
    def __init__(self, peso):
        super().__init__(peso)
    def bike(self):
        if self.bike == False:
            print(f'esta andando de bike')
            self.bike=True
        else:
            print(f'nao esta andando de bike')

    def parardebike(self):
        if self.bike==True:
            self.bike==False
            print(f'parou de andar de bike')
        else:
            print(f'nao esta andando de bike')

atleta = atleta(59)
atleta.bike()