def conteo_regresivo(numero):
    for i in range(numero, 0, -1):
        print(i)

numero_inicial = 10
print(f"Conteo regresivo desde {numero_inicial} hasta 1:")
conteo_regresivo(numero_inicial)
