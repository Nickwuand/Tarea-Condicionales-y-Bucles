def potencia_numero(base,exponente):
    resultado = 1 
    for _ in range(exponente):
        resultado *= base
    return resultado 

resultado = potencia_numero(4, 3)
print(resultado)