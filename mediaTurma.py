soma = 0
notas = []
i = 0
for x in range (5):
 notas.append(float(input("digite as notas:")))


for y in range(5):
 soma+=notas[y]

media = soma/5

for j in range(5):
  if notas[j]>=media:
     i+=1
print(i, "alunos na media")
