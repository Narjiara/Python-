inicio = int(input("digite o inicio do jogo:"))
fim = int(input("digite o fim do jogo:"))

if fim < inicio:
    print(fim+24-inicio)

else:
    print(fim-inicio)