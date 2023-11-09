numero = int(input("Ingrese un número: "))

if numero % 2 == 0:
    print("*" * numero)
else:
    for i in range(numero):
        print("*" * (i + 1))
