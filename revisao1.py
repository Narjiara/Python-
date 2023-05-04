continuar = 's'
lista = []
while continuar == 's':
      nota1 = int(input("digite 1 nota:"))
      nota2 = int(input("digite 2 nota:"))
      media = nota1 + nota2 / 2
      lista.append(media)
      if media >= 7:
        print("aluno aprovado")
      elif media <= 4:
        print("aluno recuperacao")

      else:
         print("aluno reprovado")
      continuar = input("quer continuar:")

      print(lista9)



