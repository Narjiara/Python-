from animal import Animal
class Gato(Animal):
    def __init__(self,nome,cor):
        super().__init__(nome,cor)
    def emitirSom(self):
        print(f'{self.nome} foi miando')

    def comer(self,comer):
          print(f'{self.nome} comendo {comer} ')



class Vaca(Animal):

    def __init__(self,nome,cor):
         super().__init__(nome,cor)

    def emitirSom(self):
        print(f'{self.nome} foi muu')


class Cachorro(Animal):
    def __init__(self,nome,cor):
        super().__init__(nome,cor)
    def emitirSom(self):
        print(f'{self.nome} foi latindo')

    def comer(self,comer):
          print(f'{self.nome} comendo {comer} ')
class Coelho(Animal):
    def __init__(self,nome,cor):
        super().__init__(nome,cor)
    def emitirSom(self):
        print(f'{self.nome} foi pulando')





gato = Gato("gato","preto")
vaca = Vaca("vaca","branca e preta")
cachorro = Cachorro("cachorro", "caramelo")
coelho = Coelho("coelho","branco")

print(f'{gato.nome} {gato.cor}')
gato.emitirSom()
gato.comer("sushi")
cachorro.comer("raçao")


