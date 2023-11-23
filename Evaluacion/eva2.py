class Votacion:
    def __init__(self):
        # Inicialización de variables para almacenar información sobre la votación
        self.voceros = set()  # Conjunto de IDs de voceros registrados
        self.candidatos = {"Marlon": 0, "sandra": 0, "Stiwar": 0, "Blanco": 0}  # Diccionario para almacenar votos de cada candidato
        self.votosRealizados = set()  # Conjunto de IDs de votos ya registrados

    def registrarVocero(self, idVocero):
        # Método para registrar a un vocero
        self.voceros.add(idVocero)
        print(f"Vocero {idVocero} registrado exitosamente.")

    def votar(self, idVocero, candidato):
        # Método para procesar un voto
        if idVocero not in self.votosRealizados:
            if candidato in self.candidatos:
                # Incrementa el contador de votos para el candidato seleccionado
                self.candidatos[candidato] += 1
                # Registra el ID del votante para evitar votos duplicados
                self.votosRealizados.add(idVocero)
                print(f"Voto de {idVocero} registrado para {candidato}.")
            else:
                print("Candidato no válido.")
        else:
            print(f"{idVocero}, ya has votado.")

    def mostrarResultados(self):
        # Método para mostrar los resultados de la votación
        print("\nResultados de la votación:")
        for candidato, votos in self.candidatos.items():
            print(f"{candidato}: {votos} votos")

        # Determina al ganador y maneja empates
        ganador = max(self.candidatos, key=self.candidatos.get)
        empate = [candidato for candidato, votos in self.candidatos.items() if votos == self.candidatos[ganador] and candidato != "Blanco"]

        if len(empate) == 0:
            print(f"\nGanador: {ganador} con {self.candidatos[ganador]} votos.")
        else:
            print(f"\nEmpate entre {', '.join(empate)} con {self.candidatos[ganador]} votos cada uno!")

# Crear una instancia de la clase Votacion
votacion = Votacion()

# Registro de voceros
idVocero1 = input("Ingrese el ID del primer vocero: ")
votacion.registrarVocero(idVocero1)

idVocero2 = input("Ingrese el ID del segundo vocero: ")
votacion.registrarVocero(idVocero2)

idVocero3 = input("Ingrese el ID del tercer vocero: ")
votacion.registrarVocero(idVocero3)

# Proceso de votación
while True:
    idVocero = input("Ingrese su ID para votar (o 'fin' para terminar): ")
    if idVocero.lower() == 'fin':
        break

    if idVocero in votacion.voceros:
        candidato = input("Ingrese el nombre del candidato o 'Blanco': ")
        votacion.votar(idVocero, candidato)
    else:
        print("Vocero no registrado. Regístrese primero.")

# Mostrar resultados al finalizar la votación
votacion.mostrarResultados()

