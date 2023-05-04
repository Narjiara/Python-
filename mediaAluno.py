confirmaçao = "s"
while confirmaçao == "s":

    nota1 = float(input("nota da 1 avaliaçao:"))

    while nota1 > 10 or nota1 < 1:
     nota1 = float(input("digite uma nota de 1 a 10: "))
     if nota1 <= 10 and nota1 >= 1:
        break

    nota2 = float(input("nota da 2 avaliaçao:"))

    while nota2 > 10 or nota2 < 1:
        nota2 = float(input("digite uma nota de 1 a 10: "))
        if nota2 < 10 and nota2 > 1:
            break

    media = (nota1+nota2)/2
    print ("a media foi", media)
    confirmaçao = input("deseja continuar:\ns/n:")

    if confirmaçao == "s":
        print()
    elif confirmaçao == "n":
        print("encerrando...")
    else:
        confirmaçao = input("por favor digite s ou n:")









