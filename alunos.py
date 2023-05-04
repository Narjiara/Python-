Nalunos = int(input("digite o numnero de alunos:"))
contador = 0
soma = 0
while contador < Nalunos:
    notaAlunos = float(input("digite a nota:"))
    soma = soma + notaAlunos
    contador +=1

media = soma/Nalunos

print("a media da turma é:", media)