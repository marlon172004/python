class Votacion:
    def __init__(self):
        self.voceros = set()
        self.candidatos = {"Marlon": 0, "sandra": 0, "Stiwar": 0, "Blanco": 0}
        self.votosRealizados = set()

    def registrarVocero(self, idVocero):
        self.voceros.add(idVocero)
        print(f"Vocero {idVocero} registrado exitosamente.")

    def votar(self, idVocero, candidato):
        if idVocero not in self.votosRealizados:
            if candidato in self.candidatos:
                self.candidatos[candidato] += 1
                self.votosRealizados.add(idVocero)
                print(f"Voto de {idVocero} registrado para {candidato}.")
            else:
                print("Candidato no válido.")
        else:
            print(f"{idVocero}, ya has votado.")

    def mostrarResultados(self):
        print("\nResultados de la votación:")
        for candidato, votos in self.candidatos.items():
            print(f"{candidato}: {votos} votos")

        ganador = max(self.candidatos, key=self.candidatos.get)
        empate = [candidato for candidato, votos in self.candidatos.items() if votos == self.candidatos[ganador] and candidato != "Blanco"]

        if len(empate) == 0:
            print(f"\nGanador: {ganador} con {self.candidatos[ganador]} votos.")
        else:
            print(f"\nEmpate entre {', '.join(empate)} con {self.candidatos[ganador]} votos cada uno!")

votacion = Votacion()

idVocero1 = input("Ingrese el ID del primer vocero: ")
votacion.registrarVocero(idVocero1)

idVocero2 = input("Ingrese el ID del segundo vocero: ")
votacion.registrarVocero(idVocero2)

idVocero3 = input("Ingrese el ID del segundo vocero: ")
votacion.registrarVocero(idVocero3)
while True:
    idVocero = input("Ingrese su ID para votar (o 'fin' para terminar): ")
    if idVocero.lower() == 'fin':
        break

    if idVocero in votacion.voceros:
        candidato = input("Ingrese el nombre del candidato o 'Blanco': ")
        votacion.votar(idVocero, candidato)
    else:
        print("Vocero no registrado. Regístrese primero.")

votacion.mostrarResultados()
