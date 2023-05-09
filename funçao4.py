def piramide(num1):
    for x in range(1,num1+1):
        for i in range(1, x+1):
            print(i, end=" ")
        print()
piramide(10)