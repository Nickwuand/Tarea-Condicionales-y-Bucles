def es_numero_entero(cadena):
    try:
        int(cadena)
        return True
    except ValueError:
        return False

def verificar_par_impar(numero):
    if numero % 2 == 0:
        return "par"
    else:
        return "impar"
    
def main():
    while True:
        entrada = input("ingresa un numero entero (o 'salir' para termianar):")

        if entrada.lower() == 'salir':
            break

        if es_numero_entero(entrada):
            numero = int(entrada)
            resultado= verificar_par_impar(numero)
            print(f"el numero {numero} es {resultado}.")
        
        else:
            print("error: ingresa un numero entero valido.")

if __name__== "__main__":
    main()
