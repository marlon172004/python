#Funciones con Parámetros Posicionales

# Definicion de la funcion compra
# El codigo define una función llamada compra que toma tres parametros marca cantidad y valor
# La funcion devuelve un diccionario con las claves marca cantidad y valor
#return dict se utiliza para construir y devolver un diccionario con tres claves y sus respectivos valores
def compra(marca, cantidad, valor):
    return dict(
        marca=marca,
        cantidad=cantidad,
        valor=valor*cantidad
    )

# Luego se imprime el resultado de llamar a la funcion con los argumentos AMD 3 y 2500000
print(f' lo comprado fue:{compra("AMD",3,2500000)}')


#Funciones con Parametros Nominales

# Definicion de la funcion compra
# El codigo define una función llamada compra que toma tres parámetros marca cantidad y valor
# La funcion devuelve un diccionario con las claves marca cantidad y valor
#return dict se utiliza para construir y devolver un diccionario con tres claves y sus respectivos valores
def compra(marca, cantidad, valor):
    return dict(
        marca=marca,
        cantidad=cantidad,
        valor=valor*cantidad
    )

# Se imprime el resultado de llamar a la funcion con los argumentos AMD 3 y 2500000
print(f'Lo comprado fue: {compra(marca="AMD", cantidad=3, valor=2500000)}')


# Parametros por defecto
# Definicion de la funcion compra
# El parametro valor tiene un valor por defecto de 2500000
def compra(marca, cantidad, valor=2500000):
    return dict(
        marca=marca,
        cantidad=cantidad,
        valor=valor*cantidad
    )

# Luego se imprime el resultado de llamar a la funcion con los argumentos "AMD" y 3 Como no se proporciona el tercer argumento valor se utiliza el valor por defecto.
print(f' lo comprado fue:{compra("AMD",3)}')