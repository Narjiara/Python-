negativo = 0

for x in range(10):
    num1 = int(input("digite 10 numeros:"))
    if num1 < 0:
       negativo = negativo+1

print("foram", negativo , "numeros negativos")