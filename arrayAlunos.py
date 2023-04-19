quantidade = int(input("digite numeros de alunos:"))
alunos = []
for x in range (quantidade):
 alunos.append(input("digite o nome do aluno:"))

for y in range(quantidade):
 print(alunos[y],y)


print(alunos)