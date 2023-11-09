# Se define una función llamada 'saludar' que imprime un saludo.
def saludar():
    print("saludo")

# Se define una función llamada 'retornarnumero' que devuelve el número 1.
def retornarnumero():
    return 1

# Se llama a la función 'saludar', que imprime el saludo.
saludar()

# Se llama a la función 'retornarnumero', pero como no se captura el valor devuelto, no se imprime nada.
retornarnumero()

# Se verifica si la llamada a 'retornarnumero' devuelve 1, y se imprime el resultado correspondiente.
if retornarnumero() == 1:
    print("devolvio un uno")
else:
    print("No devolvio un uno")
