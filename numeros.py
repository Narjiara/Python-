vetorA =[]
vetorM = []

for x in range(10):
    vetorA.append(int(input("digite um numero:")))

x = int(input("digite mais um numero:"))

for y in range(10):
    vetorM.append(vetorA[y]*x)

print(vetorA)
print(x)
print(vetorM)