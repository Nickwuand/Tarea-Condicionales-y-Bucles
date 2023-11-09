
numero = int(input("Ingrese un número para obtener la tabla de multiplicar: "))

print(f"Tabla de multiplicar del {numero} es:")
for i in range(1, 11):
    resultado = numero * i
    print(f"{numero} x {i} = {resultado}")
