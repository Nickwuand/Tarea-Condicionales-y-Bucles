import random

# Generar un número aleatorio entre 1 y 100
numero_secreto = random.randint(1, 100)

# Inicializar la variable de intentos
intentos = 0

print("¡Bienvenido al juego de adivinanzas!")

while True:
    # Solicitar al usuario que ingrese un número
    intento_usuario = int(input("Adivina el número (entre 1 y 100): "))
    
    # Incrementar el número de intentos
    intentos += 1

    # Comparar el número ingresado con el número secreto
    if intento_usuario == numero_secreto:
        print(f"¡Felicidades! Adivinaste el número en {intentos} intentos.")
        break
    elif intento_usuario < numero_secreto:
        print("Demasiado bajo. Intenta de nuevo.")
    else:
        print("Demasiado alto. Intenta de nuevo.")
