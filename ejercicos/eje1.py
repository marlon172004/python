# Crear listas vacías
aprendices = []
edades = []

# Llenar las listas solicitando datos por teclado
n = int(input("Ingrese la cantidad de aprendices: "))
for i in range(n):
    nombre = input(f"Ingrese el nombre del aprendiz {i + 1}: ")
    edad = int(input(f"Ingrese la edad de {nombre}: "))
    aprendices.append(nombre)
    edades.append(edad)

# Imprimir las listas
print("Lista de aprendices:", aprendices)
print("Lista de edades:", edades)

# Encontrar el aprendiz con la mayor edad
mayorEdad = edades.index(max(edades))
print(f"El aprendiz con la mayor edad es {aprendices[mayorEdad]}")

# Insertar el nombre de la instructora en la posición 1
nombreInstructora = input("Ingrese el nombre de la instructora: ")
aprendices.insert(1, nombreInstructora)

# Contar cuántos aprendices tienen 18 años
conteoEdad_18 = edades.count(18)
print(f"Hay {conteoEdad_18} aprendices de 18 años")

# Agregar un aprendiz al final de la lista
nuevo_aprendiz = input("Ingrese el nombre del nuevo aprendiz: ")
aprendices.append(nuevo_aprendiz)

# Borrar el nombre de la instructora de la lista
if nombreInstructora in aprendices:
    aprendices.remove(nombreInstructora)

# Indicar un dato a buscar en la lista de aprendices
buscar = input("Ingrese el nombre de un aprendiz para buscar: ")
if buscar in aprendices:
    print(f"{buscar} se encuentra en la lista de aprendices.")
else:
    print(f"{buscar} no se encuentra en la lista de aprendices.")

# Mostrar los primeros 10 aprendices de la lista
print("Primeros 10 aprendices:", aprendices[:10])

# Mostrar los 10 últimos aprendices de la lista
print("Últimos 10 aprendices:", aprendices[-10:])

# Mostrar del elemento 10 al elemento 20
print("Elementos del 10 al 20:", aprendices[9:19])
