def fibonacci_iterativo(n):
    fib_sequence = [0, 1]
    for i in range(2, n):
        fib_sequence.append(fib_sequence[-1] + fib_sequence[-2])
    return fib_sequence[:n]

n = 8
resultado = fibonacci_iterativo(n)
print(f"Los primeros {n} números de la secuencia de Fibonacci son: {resultado}")
