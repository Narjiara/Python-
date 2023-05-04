quantidade = int(input("digite numeros de alunos:"))
alunos = []
for x in range (quantidade):
 alunos.append(input("digite o nome do aluno:"))

checarNome = input("digite um nome para checar na lista:")

for y in range (quantidade):
 if checarNome==alunos[y]:
     print(y, alunos[y])
 else:
     checarNome = input("nao esta na lista")