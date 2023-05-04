
while True:
    num = int(input("digite um numero:"))
    while num == 0:
     num = int(input("numero invalido, digite novamente:"))
    if num >= 0:
        print(num, "positivo")
    elif num < 0:
        print(num, "negativo")
    confirmar = input("deseja continuar:")
    if confirmar == "Nao":
      break
