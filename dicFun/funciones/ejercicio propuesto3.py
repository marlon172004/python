#Funciones con Parámetros

# Define una funcion llamada calcular_suma_cuadrados que toma dos argumentos "x" "y"
def calcular_suma_cuadrados(x, y):
    # Calcula el resultado de x^2 + y^2
    resultado = x**2 + y**2
    # Devuelve el resultado calculado
    return resultado

# Define los valores de X e Y que se van a utilizar
x = 3
y = 5

# Llama a la funcion calcular_suma_cuadrados con los valores X e Y y almacena el resultado en resultado_final
resultado_final = calcular_suma_cuadrados(x, y)

# Imprime el resultado en un formato legible
print(f'El resultado de f({x}, {y}) = {resultado_final}')
