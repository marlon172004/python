# Se crea un diccionario vacío llamado 'calificaciones'.
calificaciones = {}

# Se actualiza el diccionario 'calificaciones' con dos pares clave-valor.
calificaciones.update({"Laura": 3.7, "Sebastian": 4.5})

# Se crea un nuevo diccionario 'calificaciones' con un par clave-valor.
calificaciones = {
    'nombre': 'Marlon',  # Clave: 'nombre', Valor: 'Marlon'
    'notafinal': 5.0      # Clave: 'notafinal', Valor: 5.0
}

# Creación de un diccionario 'calificaciones' con varios pares clave-valor.
calificaciones = {
    'Marlon': 5.0,
    'Stievn': 5.0,
    'Sebastian': 4.5,
    'Stevan': 2.5
}

# Se itera sobre los elementos del diccionario y se imprime cada par clave-valor.
for i, j in calificaciones.items():
    print(i, j)

# Se imprime "Técnicas por clave" antes de iterar por las claves del diccionario.
print("Técnicas por clave")

# Se itera sobre las claves del diccionario y se imprime cada clave.
for i in calificaciones.keys():
    print(i)

# Se imprime "Iterar por valor" antes de iterar por los valores del diccionario.
print("Iterar por valor")

# Se itera sobre los valores del diccionario y se imprime cada valor.
for j in calificaciones.values():
    print(j)

