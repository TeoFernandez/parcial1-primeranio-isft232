# Inicializamos variables
cantidad_total = 0
suma_positivas = 0
cantidad_positivas = 0

# Ingreso de temperaturas
while True:
    temp = float(input("Ingresá una temperatura (9999 para finalizar): "))
    
    if temp == 9999:
        break

    cantidad_total += 1

    if temp > 0:
        suma_positivas += temp
        cantidad_positivas += 1

# Cálculo del promedio de temperaturas positivas
if cantidad_positivas > 0:
    promedio_positivas = suma_positivas / cantidad_positivas
else:
    promedio_positivas = 0

# Resultados
print("\n--- Resultado ---")
print("Cantidad total de temperaturas ingresadas:", cantidad_total)
print("Promedio de temperaturas positivas:", promedio_positivas)