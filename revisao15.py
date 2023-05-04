
while True:
    num1 = int(input("digite um numero:"))
    num2 = int(input("digite um numero:"))

    if num1 != num2:
        if num1 > num2:
            print(num2,num1)

        else:
            print(num1,num2)

    else:
        print("numeros iguais")

    confirmar = input("deseja continuar:")
    if confirmar == "nao":
          break