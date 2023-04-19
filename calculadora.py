resposta = 5
while resposta!=6:
    num = float(input("digite o primeiro numero:"))
    num2 = float(input("digite o segundo numero:"))

    while True:
     resposta=int(input("escolha a operacao: 1- soma//2- subtracao//3- multiplicacao//4- divisao//5-mudar numero//6-sair:"))
     match resposta:
        case 1:
            print(num + num2)
        case 2:
            print(num - num2)
        case 3:
            print(num * num2)
        case 4:
            print(num / num2)
        case 5:
            break
        case 6:
            resposta=6
            break



