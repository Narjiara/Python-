entre10e20 = 0
forade10e20 = 0
for x in range(10):
    num1 = int(input("digite 10 numeros:"))

    if num1 >= 10 and num1 <= 20:
        entre10e20 += 1
    elif num1 < 10 or num1 > 20:
        forade10e20 += 1

print ("foram", entre10e20, "no intervalo", "e", forade10e20, "fora do intervalo")
