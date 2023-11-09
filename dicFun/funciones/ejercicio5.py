#Modificando parámetros mutables
# Define una función llamada lista que toma dos argumentos arg y result con un valor por defecto de una lista vacía
def lista(arg, result=[]):
    # Agrega el valor del argumento arg a la lista result
    result.append(arg)
    # Imprime la lista result despues de agregar arg a ella
    print(result)

# Llama a la funcion lista con el argumento domingo y una lista vacía [] como segundo argumento.
lista('sabado', [])
