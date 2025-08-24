# Ingreso de datos
peso = int(input("Ingresá tu peso en kg (entero): "))
altura = float(input("Ingresá tu altura en metros (con decimales): "))

# Cálculo del IMC
imc = peso / (altura * altura)

# Mostrar el resultado del IMC
print(f"\nTu IMC es: {imc:.2f}")

if imc < 18.5:
    print("Delgado")
elif 18.5 <= imc <= 24.9:
    print("Peso Correcto")
else:
    print("Sobrepeso")

#sistema de calculo de peso
