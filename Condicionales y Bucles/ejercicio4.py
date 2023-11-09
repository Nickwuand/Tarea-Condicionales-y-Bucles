import random

numero_secreto = random.randint(1, 100)

print("¡Bienvenido al juego de adivinanzas!")
intentos = 0

while True:

    intento_usuario = int(input("Adivina el número (entre 1 y 100): "))
    
    intentos += 1

    if intento_usuario == numero_secreto:
        print(f"¡Felicidades! Adivinaste el número en {intentos} intentos.")
        break
    elif intento_usuario < numero_secreto:
        print("Demasiado bajo. Intenta de nuevo.")
    else:
        print("Demasiado alto. Intenta de nuevo.")
