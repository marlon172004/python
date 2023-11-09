#Funciones con Parámetros

# Define una funcion llamada raiz que toma un argumento value
def raiz(value):
    # Calcula la raíz cuadrada de value elevando value a la potencia 1/2
    return value ** (1/2)

# Llama a la función "raiz" con el valor 4 e imprime el resultado
print(f'La raiz cuadrada es: {raiz(4)}')

# Define una funcion llamada validarsiexiste que toma un argumento obj
def validarsiexiste(obj):
    # Comprueba si obj verdadero (True) o falso (False) y muestra un mensaje en consecuencia
    if obj:
        print(f"{obj} is True")
    else:
        print(f"{obj} is False")

# Llama a la funcion validarsiexiste con el valor 1 e imprime el resultado
validarsiexiste(1)

