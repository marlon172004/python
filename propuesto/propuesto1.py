# Declarar listas para almacenar la información de equipos y novedades
equipos = []  # Lista de equipos
novedades = []  # Lista de novedades

# Funcion para agregar un equipo
def agregarEquipo():
    id = input("Ingrese el ID del equipo: ")  # Solicitar al usuario el ID del equipo
    cargador = input("Ingrese el estado del cargador: ")  # Solicitar el estado del cargador
    mouse = input("Ingrese el estado del mouse: ")  # Solicitar el estado del mouse
    equipos.append({"ID": id, "Cargador": cargador, "Mouse": mouse, "Novedades": []})
    # Agregar un diccionario con la información del equipo a la lista de equipos
    # Inicializar la lista de novedades como vacia para cada equipo

# Función para buscar un equipo por su ID
def buscarEquipo(id):
    for equipo in equipos:
        if equipo["ID"] == id:
            return equipo  # Devolver el equipo si se encuentra
    return None  # Devolver None si el equipo no se encuentra

# Funcion para agregar una novedad
def agregarNovedad():
    id = input("Ingrese el ID del equipo: ")  # Solicitar al usuario el ID del equipo
    equipo = buscarEquipo(id)
    if equipo:
        fecha = input("Ingrese la fecha de la novedad: ")  # Solicitar la fecha de la novedad
        descripcion = input("Ingrese la descripción de la novedad: ")  # Solicitar la descripción de la novedad
        equipo["Novedades"].append({"Fecha": fecha, "Descripción": descripcion})
        # Agregar una nueva novedad al equipo encontrado en su lista de novedades
    else:
        print("Equipo no encontrado")  # Mensaje si el equipo no se encuentra

# Función para mostrar novedades
def mostrarNovedades():
    for equipo in equipos:
        for novedad in equipo["Novedades"]:
            print("ID del Equipo:", equipo["ID"])
            print("Fecha de la Novedad:", novedad["Fecha"])
            print("Descripción de la Novedad:", novedad["Descripción"])
            # Mostrar información de novedades para cada equipo
            print()  
            
# Función para mostrar equipos
def mostrarEquipos():
    for equipo in equipos:
        print("ID:", equipo["ID"])
        print("Cargador:", equipo["Cargador"])
        print("Mouse:", equipo["Mouse"])
        print("Novedades:", equipo["Novedades"])
        print()  # Mostrar información de cada equipo y sus novedades

# Función para modificar un equipo
def modificarEquipo():
    id = input("Ingrese el ID del equipo que desea modificar: ")  # Solicitar al usuario el ID del equipo
    equipo = buscarEquipo(id)
    if equipo:
        # Si el equipo se encuentra, solicitar al usuario la información que desea modificar
        campo = input("Ingrese el campo que desea modificar (Id,Cargador,Mouse): ")
        if campo == "ID":
            nuevoID = input("Ingrese el nuevo ID: ")
            equipo["ID"] = nuevoID
        elif campo == "Cargador":
            nuevoCargador = input("Ingrese el nuevo estado del cargador: ")
            equipo["Cargador"] = nuevoCargador
        elif campo == "Mouse":
            nuevoMouse = input("Ingrese el nuevo estado del mouse: ")
            equipo["Mouse"] = nuevoMouse
        else:
            print("El campo que desea modificar no es válido.")
    else:
        print("Equipo no encontrado")

# Funcion para eliminar un equipo
def eliminarEquipo():
    # Solicitar al usuario el ID del equipo
    id = input("Ingrese el ID del equipo que desea eliminar: ")  
    equipo = buscarEquipo(id)
    if equipo:
        # Si el equipo se encuentra, eliminarlo de la lista de equipos
        equipos.remove(equipo)
        print("Equipo eliminado correctamente")
    else:
        print("Equipo no encontrado")

# Bucle principal que me inidica la validacion segun lo que digite el usuario y ademas me muestra el menu
while True:
    print("\n    **  OPCIONES ** \n")
    print(" 1) Agregar equipo ")
    print(" 2) Agregar novedad ")
    print(" 3) Mostrar equipos ")
    print(" 4) Mostrar novedades ")
    print(" 5) Modificar un equipo")
    print(" 6) Eliminar un equipo")
    print(" 7) Salir \n")
    
    opcion = input("Ingrese una opción: ")  
    # Solicitar al usuario una opcion del menu
    
    if opcion == "1":
        agregarEquipo()  # Llama a la funcion para agregar un equipo
    elif opcion == "2":
        agregarNovedad()  # Llama a la funcion para agregar una novedad
    elif opcion == "3":
        mostrarEquipos()  # Llama a la funcion para mostrar equipos
    elif opcion == "4":
        mostrarNovedades()  # Llama a la funcion para mostrar novedades
    elif opcion == "5":
        modificarEquipo()  # Llama a la funcion para modificar un equipo
    elif opcion == "6":
        eliminarEquipo()  # Llama a la funcion para eliminar un equipo
    elif opcion == "7":
        break  # Salir del bucle principal si el usuario selecciona la opción "7"
    else:
        print("La opción que digitó no es válida. Intente de nuevo.")
        # Mostrar un mensaje de error si la opción no es valida 