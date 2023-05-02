while True:
    base = int(input("digite o valor da base:"))
    altura = int(input("digite o valor da altura:"))
    print(base * altura / 2)

    confirmar = input("deseja continuar:")
    if confirmar == "nao":
        break