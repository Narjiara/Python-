a = []
contador = 0
contador2 = 0
soma = 0

for x in range(5):
    a.append(int(input("digite um numero:")))
    soma=soma+a[x]

for i in range(5):
    if a[i]%2 == 0:
        contador=contador+1

media=soma/5

for y in range(5):
        if a[y]>media:
         contador2+=1

maior = a[0]
menor = a[0]

for j in range(5):
        if a[j]>maior:
           maior=a[j]
           

        elif a[j]<menor:
           menor = a[j]

print("existem", contador,"numeros pares")
print("maior numero", maior,"menor numero", menor)
print(contador2, "numeros acima da media")

