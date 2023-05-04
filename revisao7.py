escolha = 0
while True:
    escolha = int(input("digite 1 para base, digite 2 para retangulo,digite 3 para sair:"))

    if escolha == 1:
        base = int(input("digite o valor da base:"))
        altura = int(input("digite o valor da altura:"))
        print((base * altura)/2)

    elif escolha == 2:
        retangulo = int(input("digite o valor do retangulo:"))
        alturaRetangulo = int(input("digite o valor da altura:"))
        print(retangulo * alturaRetangulo)

    elif escolha == 3:
        print("sair")
        break

    else:
        print("invalido")
