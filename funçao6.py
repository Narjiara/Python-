def produtos(produto,quantidade,valorUnitario):
    return quantidade * valorUnitario,produto

p = produtos("fuba",40,3)
print(f"o produto {p[1]} custa: {p[0]}")
