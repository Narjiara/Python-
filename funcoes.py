def somar (*num):
  print(sum(num))
def subtrair (num1, num2):
  print(num1-num2)
def multiplicar(num1, num2):
    print(num1*num2)
def dividir(num1, num2):
    print(num1/num2)

def num(n) :
  if n > 1:
    print("p")

  elif n < 0:
    print("n")

  else:
    print("z")


produto = []
pre = []
def inserir(prod,preco):

    produto.append(prod)
    pre.append(preco)

def textoInverso(palavra):
    cont = 0
    palavra_inverso = ""
    for x in palavra:
        if x not in " ":
         cont += 1
    for i in range(cont):
        palavra_inverso = palavra[i] + "" + palavra_inverso
    return cont, palavra_inverso


def numerosUnicos (a):
    nova_lsta=[]
    for x in a:
        if x not in nova_lsta:
            nova_lsta.append(x)

    print(nova_lsta)

def numero_primo (num):
    for x in range(2, num):
      if num  % x == 0 :
          return f"{num} nao é primo"
    return f"{num} é primo"




