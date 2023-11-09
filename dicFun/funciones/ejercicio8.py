# Se define una función lambda llamada 'numero_palabras' que toma un argumento 't'.
# La función cuenta el número de palabras en 't' después de eliminar espacios en blanco adicionales al principio y al final y dividir la cadena por espacios.
numero_palabras = lambda t: len(t.strip().split())

# Se imprime el resultado de llamar a la función lambda con la cadena dada.
print(numero_palabras("hola, esto es una prueba con lambda"))

