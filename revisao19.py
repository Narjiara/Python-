a = []
cont = 0
impares = 0

while True:
    if cont % 2 != 0:
      a.append(cont)
      impares+=1

    if impares == 10:
        break
    cont +=1
print(a)