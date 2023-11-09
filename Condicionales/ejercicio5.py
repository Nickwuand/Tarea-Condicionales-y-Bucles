salario_anual = float(input("Ingrese su salario anual: "))

if salario_anual <= 10000:
    impuesto = 0
elif salario_anual <= 50000:
    impuesto = salario_anual * 0.10  
elif salario_anual <= 100000:
    impuesto = salario_anual * 0.20  
else:
    impuesto = salario_anual * 0.30  

print(f"El impuesto sobre la renta es: ${impuesto:.2f}")
