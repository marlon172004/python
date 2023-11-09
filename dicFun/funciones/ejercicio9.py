# Ejemplo 2 función Lambda

# Definimos un bucle anidado con dos bucles "for" para iterar sobre "i" y "j".
# Definimos la función lambda "operadorand" que toma dos argumentos "x" e "y" y realiza una operación lógica "AND" en ellos.
operadorand = lambda x, y: x & y

# Luego, ejecutamos los bucles y la impresión de la operación lógica.
for i in range(2):
    for j in range(2):
        print(f"{i} & {j} = {operadorand(i, j)}")

