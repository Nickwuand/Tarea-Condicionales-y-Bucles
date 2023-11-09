precio_producto = float(input("Ingrese el precio del producto: "))
edad_usuario = int(input("Ingrese su edad: "))

if edad_usuario < 18:
    descuento = 0.10  
elif edad_usuario >= 65:
    descuento = 0.15  
else:
    descuento = 0  

precio_final = precio_producto - (precio_producto * descuento)
print(f"El precio final después del descuento es: ${precio_final:.2f}")
