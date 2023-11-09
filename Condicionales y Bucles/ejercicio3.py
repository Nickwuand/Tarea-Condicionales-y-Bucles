numero = int(input("Ingrese un número: "))

es_primo = True

if numero > 1:
    for i in range(2, int(numero**0.5) + 1):
        if numero % i == 0:
            es_primo = False
            break

if es_primo and numero > 1:
    print(f"{numero} es un número primo.")
else:
    print(f"{numero} no es un número primo.")
