eleitores = int(input("digite o numero de eleitores:"))
brancos = int(input("digite o numero de votos brancos:"))
nulos =  int(input("digite o numero de votos nulos:"))
validos =  int(input("digite o numero de votos validos:"))

percentualvv = (validos/eleitores) * 100
percentualvn=(nulos/eleitores) * 100
percentualvb=(brancos/eleitores) * 100
print("total de eleitores", eleitores)
print("total de validos", validos)
print("total de nulos", nulos)
print("total de brancos", brancos)