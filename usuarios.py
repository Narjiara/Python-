nomes = []
senhas = []
for x in range(2):
    nomes.append(input("digite o nome:"))
    senhas.append(int(input("digite a senha:")))

usuario = input("usuario para login:")
senha = input("senha para login:")

for y in range(2):
    if nomes[y]==usuario and senhas[y]==senha:
       print("login efetuado com sucesso")
    else:
       print("senha errada")






