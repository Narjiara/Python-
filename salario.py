nome = input("Digite o seu nome: ")
idade = input("Digite sua idade: ")
salariodigite = float(input("Digite o seu salario: "))
reajuste = float(input("Digite a porcentagem do seu reajuste: "))
reajustesoma = salariodigite * reajuste/100

print("Olá, ", nome, "\n Sua idade é: ", idade, "\n Seu salário é: ", salariodigite, " \n Seu novo salário é: ", salariodigite + reajustesoma )