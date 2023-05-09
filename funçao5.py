texto = "o raton roeu a roupa do rei de roma"
def vogais(texto):
    cont = 0
    for x in (texto):
        if x in "aeiouAEIOU":
            cont +=1
    print(f"o número de vogais é:{cont}")

vogais(texto)
