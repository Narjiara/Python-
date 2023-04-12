nota1 = float(input("Digite a primeira nota: "));
nota2 = float(input("Digite a segunda nota: "));
nota3 = float(input("Digite a terceira nota: "));

media = ((nota1 + nota2 + nota3) /3);


if media >= 7:
    print("Aluno Aprovado!");

elif media >=4 and media <=6:
    print("Aluno em Recuperação");

else:
    print("Aluno Reprovado!");


print("Sua media é igual a: ", media);