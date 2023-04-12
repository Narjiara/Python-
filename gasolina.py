combustivel = input("Digite G para Gasolina e E para Etanol: ")
litros = float(input("Digite a quantidade de litros: "))


if combustivel == 'G':
    valor_total = litros *5.8
    print(valor_total)
elif combustivel == 'E':
    valor_total = litros * 4.9
    print(valor_total)

else:
    print("Invalido!")