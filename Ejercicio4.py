# Lista de bolsas de harina vendidas
ventas = [200, 320, 55, 23, 96, 42, 11, 290]

# Variable para almacenar la suma total
total = 0

# Sumar e imprimir cada valor
for venta in ventas:
    print("Venta:", venta)
    total += venta

# Mostrar el total
print("\nTotal de bolsas vendidas:", total)
