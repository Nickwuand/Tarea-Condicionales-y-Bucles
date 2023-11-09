numero_ingresado = int(input("Ingrese un número entero: "))

suma_numeros_pares = 0

for i in range(2, numero_ingresado + 1, 2):
    suma_numeros_pares += i

print(f"La suma de los números pares desde 2 hasta {numero_ingresado} es: {suma_numeros_pares}")
