class Pessoa:
    def __init__(self,nome,peso,idade,comendo=False,andar=False,falar=False):
        self.nome=nome
        self.peso=peso
        self.idade=idade
        self.comendo=comendo
        self.andando=andar
        self.falando=falar

    def comer(self, comendo):
        self.comida=comendo
        if self.comendo == False:
            print(f'{self.nome} esta comendo {self.comida}')
            self.comendo = True
        else:
            print(f'{self.nome} ja esta comendo')
    def paradecomer(self):
        if self.comendo==True:
            print(f"{self.nome} parou de comer")
            self.comendo=False
        else:
            print(f"{self.nome} nao esta comendo")
    def falar(self):
        if self.comendo == True:
            print(f'{self.nome} nao pode falar')
        elif self.falando == True:
            print(f"{self.nome} ja esta falando")
        else:
            self.falando = True
            print(f'{self.nome} esta falando')
    def parardefalar(self):
        if self.falando == True:
            print(f'{self.nome} parou de falar ')
            self.falando = False
        else:
            (f'({self.nome} nao esta falando')
    def andar(self):
        if self.andando == False:
            print(f'{self.nome} esta andando ')
            self.andando = True
        else:
            print(f'{self.nome} nao esta andando')

    def paradeandar(self):
        if self.andando == True:
            self.andando == False
            print(f'{self.nome} parou de andar')
        else:
            print(f'{self.nome} nao esta andando')

p1 =  Pessoa("joao",80,19)
p2 =  Pessoa("maria",56,22,comendo=True)
print(p1.nome)
print(p1)
print(vars(p1))
print(p2.nome)
print(vars(p2))

p1.comer("pipoca")
p1.paradecomer()
p1.comer("chocolate")
p1.andar()
p1.paradecomer()
p1.falar()
p1.parardefalar()
p1.andar()
p1.paradeandar()