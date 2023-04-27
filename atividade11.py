vetor = []
cont = 0
for x in range(10):
    vetor.append(int(input("digite um numero:")))
numeroQualquer=(int(input("informe o numero para pesquisar:")))

for i in range(10):
    if numeroQualquer==vetor[i]:
        cont+=1
print("o numero", numeroQualquer , "apareceu", cont, "vezes")
