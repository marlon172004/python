class RegistroVotacion: # Declaramos la clase Regitro donde vamos a almacenar los datos del votante    
    def __init__(self): # Establecemos la funcion donde le esta la lista vacia de votante  
        self.votantes = [] # referenciasmo con el self para indicar que es de votantes

    def registrarVotante(self): # Declaramos los metodos que tiene el objeto y igualmente lo referenciasmo con el self
        nombre = input("\nIngrese el nombre del votante: ") # Aqui le pedimos los datos al votante
        apellidos = input("\nIngrese el apellido del votante: ")
        formacion = input("\nIngrese la formación del votante: ")
        
        print("\n   ***** Candidatos *****")
        print("\n     1) Adriana Lucia") # Motrar el numero junto al nombre del candidato para ser mas intuitivo
        print("     2) Marlon Lopez")
        print("     3) Sandra Milena")
        print("     4) Voto en blanco")
        
        voto = input("\nIngrese el numero del candidato al que desea votar 1) , 2), 3) o 4) Voto en blanco : ") # self es una referencia a la instancia de la clase pero es la lista donde le estamos agragando lo datos insertados con el .append y ps seria un diccionario
        
        self.votantes.append({"nombre": nombre, "apellidos": apellidos, "formacion": formacion, "voto": voto})
   
    def buscarVotante(self, nombre): # Metodo para buscar a la persona que voto por si realizo fraude y queremos identificar a la persona
        for votante in self.votantes: # Repite sobre cada vontante en la lista self.votantes 
            if votante["nombre"] == nombre: # Verifica si el valor de la clave "nombre" en el diccionario de nombre es igual al nombre proporcionado
                return votante # Si se encuentra el votante buscado, se devuelve ese diccionario de votantes
        return None # y ps si no se encuentra me muestra none que este no me retornaria nada
    
    def mostrarVotantes(self): # A diferencia del de buscar que ese metodo me busca por persona osea solo a una, este metodo me muestra todo los que han votado, por lo que estan en un ciclo while este se repito hasta que digitemos salir o control c en la terminal
        for votante in self.votantes: # Repite sobre cada vontante en la lista self.votantes
            print("Nombre:", votante["nombre"]) # Se muestran los datos
            print("Apellidos:", votante["apellidos"])
            print("Formación:", votante["formacion"])
            print("Voto:", votante["voto"])
            print()

    def eliminarVotante(self): # En este metodo lo cree al igual que el buscar votante pero yo cree el de buscar votantes para veificar si el votante esta registrado, pero yo cree el metod de eliminar por si un votante se equivoco o simplemente se desesa eliminar una votacion, tambien porque asi me ayude a guairme
        nombre = input("Ingrese el nombre del votante que desea eliminar: ") # pedimos nombre
        votante = self.buscarVotante(nombre) # me referecia a la funcion buscarVotante
        if votante:
            self.votantes.remove(votante)
            print("Votante eliminado correctamente") # y aqui si el nombre se encuentra, se elimina de la lista de votante y si no entonces no se encutra
        else:
            print("Votante no encontrado")

    def contarVotos(self): # Creamos el metodo de contarvoto 
        candidatos = {"1": 0, "2": 0, "3": 0, "4":0} # Creamos el arreglo donde digitamos el orden de nuemores que tienen los candidatos y cero para que cuando cuente empiece desde 0
        for votante in self.votantes: # me indica si vontantes esta dentro de self.votantes
            voto = votante["voto"]
            if voto in candidatos: #ys si voto esta en candidatos 
                candidatos[voto] += 1 # que se vaya incrementando de 1 en 1 de acuerdo a los usuarios que voten

        ganador = max(candidatos, key=candidatos.get) #Ahora en esta paerte utlice el max para que me muestre directamente le candidato con el valor mas grande ademas de establecer como llave a candidatos que de igual forma utilice el .get que lo que hace es obtener los datos del arreglo candidatos
        print("Resultados de la votacion:")
        for candidato, votos in candidatos.items(): # Entoces por ultimo en este metodo donde candidato me recorre votos dentro de los items por eso el .items, osea me recorre el arreglo
            print(f"Candidato {candidato}: {votos} votos") # Y ps el la forma de mostrar las variables y texto de una forma mas Elegante si señor

        print(f"\nEl ganador es el Candidato {ganador} con {candidatos[ganador]} votos")

# en esta parte esta la instancia de la clase RegistroVotacion
Registro = RegistroVotacion()

while True: # Este es el ciclo que me repite las preguntas de manera indefinida hasta que el propio usuario la detente por eso use el while
    print("\n    *  VOTACIONES * \n")
    print("      1) Registrarce ")
    print("      2) Mostrar votantes ")
    print("      3) Eliminar un votante")
    print("      4) Contar votos y mostrar ganador")
    print("      5) Salir \n")

    opcion = input("Ingrese una opción: ") # pedimos al votante que inserte un numero 

    if opcion == "1": # de esa manera comparamos el dato insertado con las opciones y si son iguales me muestre el metodo dependiendo de la registro que esta es la misma clase RegistroVotacion()
        Registro.registrarVotante() # de esta forma llamo al metodo
    elif opcion == "2":
        Registro.mostrarVotantes()
    elif opcion == "3":
        Registro.eliminarVotante()
    elif opcion == "4":
        Registro.contarVotos()
    elif opcion == "5":
        break # se utiliza el break para romper el ciclo
    else: # ulizamos el else si no se cumpla la variables entoncesnos mostrara este mensaje
        print("La opcion que digito no es correcta, Intente de nuevo")
        