num = int(input("digite um numero:"))
if num % 2 == 0 and num > 0:
    print("é um numero par e positivo")
elif num % 2 != 0 and num > 0:
    print("é um numero impar e positivo")

elif num % 2 == 0 and num < 0:
    print("é um numero par e negativo")
else:
    print("é um numero impar e negativo")