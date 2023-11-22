def es_numero_entero(cadena):
    try:
        int(cadena)
        return True
    except ValueError:
        return False

def calcular_suma_pares_hasta(numero):
    suma = 0
    for i in range(1, numero + 1):
        if i % 2 == 0:
            suma += i
    return suma

def main():
    while True:
        entrada = input("Ingresa un número entero (o 'salir' para terminar): ")

        if entrada.lower() == 'salir':
            break

        if es_numero_entero(entrada):
            numero = int(entrada)
            if numero >= 1:
                resultado = calcular_suma_pares_hasta(numero)
                print(f"La suma de los números pares hasta {numero} es: {resultado}.")
            else:
                print("Ingresa un número entero mayor o igual a 1.")
        else:
            print("Error: Ingresa un número entero válido.")

if __name__ == "__main__":
    main()
