def imprimir_ascendente():
    numero = 1
    while numero <= 10:
        print(numero)
        numero += 1

def imprimir_descendente():
    numero = 10
    while numero >= 1:
        print(numero)
        numero -= 1

def main():
    print("Imprimiendo números del 1 al 10 en orden ascendente:")
    imprimir_ascendente()

    print("Imprimiendo números del 10 al 1 en orden descendente:")
    imprimir_descendente()

if __name__ == "__main__":
    main()
