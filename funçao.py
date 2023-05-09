def somar (num1,num2):
  print(num1+num2)
def subtrair (num1, num2):
  print(num1-num2)
def multiplicar(num1, num2):
    print(num1*num2)
def dividir(num1, num2):
    print(num1/num2)

while True:

    escolha = int(input("digite 1 para somar,2 para subtrair,3 para multiplicar,4 para dividir, 5 sair:"))
    while escolha>5:
        escolha = int(input("digite 1 para somar,2 para subtrair,3 para multiplicar,4 para dividir, 5 sair:"))
    if escolha == 5:
        print("sair")
        break


    num1 = int(input("digite um numero:"))
    num2 = int(input("digite um numero:"))

    if escolha == 1:
        somar(num1,num2)
    if escolha == 2:
        subtrair(num1,num2)
    if escolha == 3:
        multiplicar(num1,num2)
    if escolha == 4:
        dividir(num1,num2)


print("finalizado")