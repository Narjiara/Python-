time1 = input("Digite o nome do primeiro time: ")
time2 = input("Digite o nome do segundo time: ")

goltime1 = float(input("Digite o gol do primeiro time: "))
goltime2 = float(input("Digite o gol do segunda time: "))

if goltime1 != goltime2:

    if goltime1 > goltime2:
        print(time1,"Venceu com ", goltime1, "Gols!")

    else:
        print(time2,"Ganhou com ", goltime2, "Gols!")

else:
    print("O jogo empatou!")