num = int(input("digite um numero:"))
i = 1
for x in range (num):
    for y in range (x):
        print(y,end=" ")
    i += 1
    print()
