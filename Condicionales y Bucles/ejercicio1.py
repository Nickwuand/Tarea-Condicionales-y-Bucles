numero_ingresado = int(input("Ingrese un número: "))

suma_numeros_pares = 0

for i in range(1, numero_ingresado + 1):
    if i % 2 == 0:  
        suma_numeros_pares += i

print(f"La suma de los números pares desde 1 hasta {numero_ingresado} es: {suma_numeros_pares}")
