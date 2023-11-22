#Ejercicio propuesto

# Implemente el ejercicio del control de bitácoras de ambiente. Usando una clase que permita
# almacenar la información del computador y las novedades asociadas a él.
# Se debe definir las mismas operaciones o métodos definidos en el ejercicio anterior:
# Agregar información del pc
# Editar información del pc
# Eliminar información del pc
# Agregar novedad
# Mostrar equipos con las novedades registradas
# Buscar un equipo

class BitacoraAmbiente:
    def _init_(self):
        # Constructor (_init_): Se llama cuando se crea una nueva instancia de la clase
        # Declaramos las listas para alamecenar los equipos y novedades.
        self.equipos = []
        self.novedades = []

    # Método para agregar un equipo
    def agregarEquipo(self):
        # self: Es una referencia a la instancia de la clase
        id = input("Ingrese el ID del equipo: ")
        cargador = input("Ingrese el estado del cargador: ")
        mouse = input("Ingrese el estado del mouse: ")
        # Se agrega un diccionario con la información del equipo a la lista de equipos
        self.equipos.append({"ID": id, "Cargador": cargador, "Mouse": mouse, "Novedades": []}) # utilizamos el .append para agregar un elemento a la lista

# Metodo para buscar un equipo por su ID
def buscarEquipo(self, id):
    # Repite sobre cada diccionario de equipo en la lista self.equipos
    for equipo in self.equipos:
        # Verifica si el valor de la clave "ID" en el diccionario de equipo es igual al ID proporcionado
        if equipo["ID"] == id:
            # Si se encuentra un equipo con el ID buscado, se devuelve ese diccionario de equipo
            return equipo
    # Si no se encuentra ningún equipo con el ID buscado, se devuelve None
    return None

# Metodo para agregar una novedad
def agregarNovedad(self):
    id = input("Ingrese el ID del equipo: ")
    equipo = self.buscarEquipo(id)
    if equipo:
        fecha = input("Ingrese la fecha de la novedad: ")
        descripcion = input("Ingrese la descripción de la novedad: ")
        # Se agrega una nueva novedad al equipo encontrado en su lista de novedades.
        equipo["Novedades"].append({"Fecha": fecha, "Descripción": descripcion})
    else:
        print("Equipo no encontrado")

# Método para mostrar novedades
def mostrarNovedades(self):
    for equipo in self.equipos:
        for novedad in equipo["Novedades"]:
            print("ID del Equipo:", equipo["ID"])
            print("Fecha de la Novedad:", novedad["Fecha"])
            print("Descripción de la Novedad:", novedad["Descripción"])
            print()

# Método para mostrar equipos
def mostrarEquipos(self):
    for equipo in self.equipos:
        print("ID:", equipo["ID"])
        print("Cargador:", equipo["Cargador"])
        print("Mouse:", equipo["Mouse"])
        print("Novedades:", equipo["Novedades"])
        print()

# Método para modificar un equipo
def modificarEquipo(self):
    id = input("Ingrese el ID del equipo que desea modificar: ")
    equipo = self.buscarEquipo(id)
    if equipo:
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

# Método para eliminar un equipo
def eliminarEquipo(self):
    id = input("Ingrese el ID del equipo que desea eliminar: ")
    equipo = self.buscarEquipo(id)
    if equipo:
        # Si el equipo se encuentra, se elimina de la lista de equipos.
        self.equipos.remove(equipo)
        print("Equipo eliminado correctamente")
    else:
        print("Equipo no encontrado")
        
# Crear una instancia de la clase BitacoraAmbiente
bitacora = BitacoraAmbiente() # declamos varibale bitacoraAmbiente

# Bucle principal
while True: # utilizamos este bucle mientras mostramos las opciones para seleccionar
    print("\n    *  OPCIONES * \n")
    print(" 1) Agregar equipo ")
    print(" 2) Agregar novedad ")
    print(" 3) Mostrar equipos ")
    print(" 4) Mostrar novedades ")
    print(" 5) Modificar un equipo")
    print(" 6) Eliminar un equipo")
    print(" 7) Salir \n")
    
    opcion = input("Ingrese una opción: ") #nombramos la variable opcion
    
    if opcion == "1": # usamos la condicional if por si el usuario digita la opcion 1
        bitacora.agregarEquipo()
    elif opcion == "2":
        bitacora.agregarNovedad()# ustizamos el elif si el usuario no selecciona la opcion 1 
    elif opcion == "3":
        bitacora.mostrarEquipos()
    elif opcion == "4":
        bitacora.mostrarNovedades()
    elif opcion == "5":
        bitacora.modificarEquipo()
    elif opcion == "6":
        bitacora.eliminarEquipo()
    elif opcion == "7":
        break
    else: # ulizamos el else si no se cumpla la variables entoncesnos mostrara este mensaje
        print("La opción que digitó no es válida. Intente de nuevo.")