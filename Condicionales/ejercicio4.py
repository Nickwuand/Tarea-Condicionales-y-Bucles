puntuacion = int(input("Ingrese la puntuación (de 0 a 100): "))

if 90 <= puntuacion <= 100:
    calificacion = "A (sobresaliente)"
elif 80 <= puntuacion <= 89:
    calificacion = "B (bueno)"
elif 70 <= puntuacion <= 79:
    calificacion = "C (satisfactorio)"
elif 60 <= puntuacion <= 69:
    calificacion = "D (necesita mejorar)"
else:
    calificacion = "F (reprobado)"

print(f"La calificación es: {calificacion}")
