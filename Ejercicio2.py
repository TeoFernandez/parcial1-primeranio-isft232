# Crear una lista vacía para almacenar los nombres de los socios
socios = []

# Ingreso de 10 nombres
for i in range(10):
    nombre = input(f"Ingresá el nombre del socio {i + 1}: ")
    socios.append(nombre)

# Mostrar el listado de socios
print("\nListado de Socios")
for i in range(10):
    print(f"{i + 1} - {socios[i]}")
