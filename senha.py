
contador = 0

while contador < 3:
 senha = input("digite a sua senha:")
 senhacerta = "123456789"
 if senha == senhacerta:
  print("bem vindo")
  break

 else:
    contador+=1
if contador == 3:
    print ("senha bloqueada")
