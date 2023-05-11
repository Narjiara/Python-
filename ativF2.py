from funcoes import inserir
from funcoes import produto
from funcoes import pre


while True:
        n1 = input("digite o produto:")
        n2 = int(input("digite o valor:"))
        inserir(n1, n2)
        confirmar = input("deseja continuar:")

        if confirmar == "nao":
            print("encerrado")
            break

print(produto)
print(pre)
