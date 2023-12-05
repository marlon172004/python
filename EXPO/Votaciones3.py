class Votaciones:
    def __init__(self):
        self.votantes = []
        self.candidatos = ["Adriana Lucia", "Marlon Lopez", "Sandra Milena"]

    def mostrarCandidatos(self):
        print("\n Selecione el candidato por el que desea votw")
        print("\n ---------------------------------------")
        print("|             CANDIDATOS                |")
        print(" ---------------------------------------")
        for i, candidato in enumerate(self.candidatos, start=1):
            print(f"|    {i}) {candidato: <{len(self.candidatos)}}  |")
        print(" ---------------------------------------\n")

    def registrarVotante(self):
        nombres = input("\nIngrese los nombres del votante: ")
        apellidos = input("\nIngrese los apellidos del votante: ")

        cc = input("\nIngrese su numero de identificacion de su documento de identidad: ")
        while not cc.isdigit():
            print("\nDatos no válidos. Por favor, ingrese un número de documento de identidad correctamente.")
            cc = input("Ingrese su numero de identificacion de su documento de identidad: ")

        formacion = input("\nIngrese el programa de formación del votante: ")

        self.mostrarCandidatos()

        while True:
            voto = input(f"Ingrese el número del candidato al que desea votar desde el 1) hasta el {len(self.candidatos)}) o 0 para el voto en blanco: ")
            if voto.isdigit() and 0 <= int(voto) <= len(self.candidatos):
                break
            else:
                print("Dato no válido. Por favor, ingrese un número válido.")

        self.votantes.append({"nombres": nombres, "apellidos": apellidos, "cc": cc, "formacion": formacion, "voto": voto})
        print("Voto registrado correctamente.")

    def buscarVotante(self, nombres):
        for votante in self.votantes:
            if votante["nombres"] == nombres:
                return votante
        return None

    def mostrarVotantes(self):
        for votante in self.votantes:
            print("\nNombres:", votante["nombres"])
            print("Apellidos:", votante["apellidos"])
            print("Numero de documento:", votante["cc"])
            print("Formación:", votante["formacion"])
            print("Voto:", votante["voto"])
            print()

    def eliminarVotante(self):
        identificarNombreApellidos = input("Ingrese tanto los nombres y apellidos completos del votante que desea eliminar: ").strip().lower()
        identificarNumero = input("Ingrese el numero de documento de identidad:")
        votante = next((v for v in self.votantes if f"{v['nombres']} {v['apellidos']}".strip().lower() == identificarNombreApellidos), None)
        votante = next((v for v in self.votantes if f"{v['cc']}" == identificarNumero), None)

        if votante:
            self.votantes.remove(votante)
            print("Votante eliminado correctamente.")
        else:
            print("Votante no encontrado.")

    def contarVotos(self):
        candidatos = {"1": 0, "2": 0, "3": 0, "0": 0}
        votoBlanco = 0

        for votante in self.votantes:
            voto = votante["voto"]
            if voto in candidatos:
                candidatos[voto] += 1
            elif voto == "0":
                votoBlanco += 1

        maxVotos = max(candidatos.values())
        ganadores = [candidato for candidato, votos in candidatos.items() if votos == maxVotos]

        print("\nResultados de la votacion:")
        for candidato, votos in candidatos.items():
            print(f"Candidato {candidato}: {votos} votos")

        if votoBlanco > maxVotos:
            print(f"Votos en blanco: {votoBlanco} votos")
            print(f"\nEl ganador es Voto en blanco con {votoBlanco} votos")
        elif len(ganadores) == 1:
            print(f"\nEl ganador es el Candidato {ganadores[0]} con {maxVotos} votos")
        else:
            print(f"\nHubo un empate entre los candidatos {', '.join(ganadores)} con {maxVotos} votos cada uno")

    def modoAdministrador(self):
        while True:
            print("\n ----------------------------------------")
            print("|             ADMINISTRADOR              |")
            print(" ----------------------------------------")
            print("|      1) Regresar                       |")
            print("|      2) Mostrar votantes               |")
            print("|      3) Eliminar un votante            |")
            print("|      4) Contar votos y mostrar ganador |")
            print("|      5) Salir                          |")
            print(" ----------------------------------------\n")

            admin_opcion = input("Ingrese una opción de administrador: ")

            if admin_opcion == "1":
                break
            elif admin_opcion == "2":
                self.mostrarVotantes()
            elif admin_opcion == "3":
                self.eliminarVotante()
            elif admin_opcion == "4":
                self.contarVotos()
            elif admin_opcion == "5":
                exit()
            else:
                print("La opción que digitó no es correcta. Intente de nuevo")


# Instancia de la clase Votaciones
Registro = Votaciones()

while True:
    print("\n ----------------------------------------")
    print("|             VOTACIONES                 |")
    print(" ----------------------------------------")
    print("|      1) Registrarse                    |")
    print("|      2) Modo Administrador             |")
    print("|      3) Salir                          |")
    print(" ----------------------------------------\n")

    opcion = input("Ingrese una opcion: ")

    if opcion == "1":
        Registro.registrarVotante()
    elif opcion == "2":
        contraseña_admin = input("Ingrese la contraseña de administrador: ")

        if contraseña_admin == "siseñor":
            Registro.modoAdministrador()
        else:
            print("Contraseña incorrecta. Volviendo al menú principal.")
    elif opcion == "3":
        break
    else:
        print("La opción que digitó no es correcta. Intente de nuevo")
