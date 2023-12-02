def calcular_potencia(base, exponente):
    resultado = 1
    for _ in range(exponente):
        resultado *= base
    return resultado

# Ejemplo de uso
base = 3
exponente = 3
resultado = calcular_potencia(base, exponente)
print(f"{base}^{exponente} = {resultado}")
