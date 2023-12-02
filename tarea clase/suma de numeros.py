def suma_naturales(n):
    suma = 0
    for i in range(1, n + 1):
        suma += i
    return suma

# Ejemplo de uso
n = 3
resultado = suma_naturales(n)
print(f"La suma de los primeros {n} números naturales es: {resultado}")
