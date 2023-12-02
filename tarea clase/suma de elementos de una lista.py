def suma_lista(lista):
    suma = 0
    for elemento in lista:
        suma += elemento
    return suma

mi_lista = [1, 2, 3, 4, 5]
resultado = suma_lista(mi_lista)
print(f"La suma de los elementos de la lista {mi_lista} es: {resultado}")
