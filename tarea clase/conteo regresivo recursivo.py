def conteo_regresivo_recursivo(numero):
    if numero == 0:
        return
    else:
        print(numero)
        conteo_regresivo_recursivo(numero - 1)

numero_inicial = 5
print(f"Conteo regresivo recursivo desde {numero_inicial} hasta 1:")
conteo_regresivo_recursivo(numero_inicial)
