# Se crean dos listas, 'nombres' y 'edades', con información correspondiente.
nombres = ['Laura', 'marlon', 'Alberto']
edades = ['17', '19', '30']

# Se utiliza la función zip para combinar las listas y luego se itera sobre las parejas de nombre y edad.
for n, e in zip(nombres, edades):
    print('Tú nombre es {0} y tu edad {1}.'.format(n, e))

# Se crea un diccionario llamado 'dicaleatorio' utilizando un dict comprehension.
# El diccionario tiene claves que son números pares y valores que son el cuadrado de esas claves.
dicaleatorio = {x: x**2 for x in (2, 4, 6)}

# Se imprime el diccionario resultante.
print(dicaleatorio)
