# Se define un diccionario llamado 'calificaciones' con varios pares clave-valor.
calificaciones = {
    'Stiven': 5.0,
    'Nicolas': 4.5,
    'Stevan': 3.0,
    'Gerardo': 2.5
}

# Se verifica si 'rosa' está en las claves del diccionario.
if 'rosa' in calificaciones:
    # Si 'rosa' está en el diccionario, se elimina esa entrada.
    del calificaciones['Rosa']
    # Se imprime un mensaje indicando que 'Rosa' fue eliminado del diccionario.
    print("'Rosa' eliminado del diccionario")

# Se itera sobre los elementos del diccionario y se imprime cada par clave-valor.
for i, j in calificaciones.items():
    print(i, j)
