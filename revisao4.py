num1 = int(input("digite o numero:"))
num2 = int(input("digite o numero:"))
num3 = int(input("digite o numero:"))

if num1 > num2 and num1 > num3:
    print(num1, "é o maior numero")
elif num2 > num1 and num2 > num3:
    print(num2, "é o maior numero")
else:
    print(num3, "é o maior numero")
