num = int(input("digite o valor:"))
vetorA = []
vetorB = []
vetorC = []

for x in range(num):
    vetorA.append(int(input("digite um numero:")))
    vetorB.append(int(input("digite um numero:")))

for i in range(num):
    vetorC.append(vetorA[i] + vetorB[i])

print(vetorA)
print(vetorB)
print(vetorC)
