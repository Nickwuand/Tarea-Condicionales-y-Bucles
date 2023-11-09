cadena = input("Ingrese una cadena: ")

contador_vocales = 0

indice = 0
while indice < len(cadena):
    letra = cadena[indice]
    if letra.lower() in "aeiou":
        contador_vocales += 1
    indice += 1

print(f"La cantidad de vocales en la cadena es: {contador_vocales}")
