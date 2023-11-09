#Modificando parámetros mutables

# Define una funcion llamada listalimpia que toma dos argumentos: "arg" y "result" con un valor por defecto de None
def listalimpia(arg, result=None):
    # Comprueba si el argumento "result" es None.
    if result is None:
        # Si "result" es None crea una nueva lista vacía y asigna esta lista a result
        result = []
    
    # Agrega el valor del argumento "arg" a la lista result
    result.append(arg)
    
    # Imprime la lista "result" despues de agregar "arg" a ella
    print(result)

# Llama a la funcion listalimpia con el valor "a" Como "result" no se proporciona, se creara una nueva lista y se agregara "a".
listalimpia("a")

# Llama a la funcion listalimpia con el valor "b" Nuevamente se crea una nueva lista y se agrega "b".
listalimpia("b")
