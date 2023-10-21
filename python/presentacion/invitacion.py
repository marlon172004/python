while True: # se ejecuta hasta que el usuario decide salir al elegir "no" en lugar de repetir el formulario. (un bucle controlado)
    print("\n***************************************************** INGRESO *****************************************************\n")
    nombre = input("Cual es tu nombre: ")

    # Asignamos los datos que no van a cambiar
    edadMinima = 18
    estaturaMinima = 155
    contraseñaCorrecta = "ADSO"
    tematicaValida = "terror"

    # Realizamos las restricciones
    # Restriccion de edad
    edad = int(input("Ingrese su edad: "))
    if edad < edadMinima:
        print(f"{nombre}, lo siento, no cumples con la edad mínima\n")
        continue  # Repite el ciclo desde el principio

    # Restriccion de estatura
    estatura = float(input("Ingrese su estatura en cm: "))
    if estatura < estaturaMinima:
        print(f"{nombre}, tu estatura no es suficiente\n")
        continue  # Repite el ciclo desde el principio

    # Restriccion de contraseña
    contraseña = input("Dime la contraseña: ").strip()
    if contraseña.lower() != contraseñaCorrecta.lower():
        print(f"{nombre}, la contraseña es incorrecta\n")
        continue  # Repite el ciclo desde el principio

    # Restriccion de tematica de disfraz
    temDisfraz = input("Ingrese la temática de su disfraz: ").strip().lower()
    if temDisfraz != tematicaValida:
        print(f"{nombre}, la temática de tu disfraz no es válida\n")
        continue  # Repite el ciclo desde el principio

    # Restriccion del cover (cantidad de dinero minimo permitido)
    cover = float(input("Digita la cantidad de dinero en pesos que tienes para el cover: "))
    if cover < 15000:
        print(f"{nombre}, no tienes suficiente dinero para el cover\n")
        continue  # Repite el ciclo desde el principio

    # Restriccion de alcohol
    alcohol = input("¿Traes alcohol? (Si o No): ").strip().lower()
    if alcohol != "si":
        print(f"{nombre}, no puedes ingresar sin alcohol\n")
    else:
        print(f"{nombre}, puedes ingresar\n")

    # Indicar si queremos repetir el formulario de ingreso a la fiesta
    repetir = input("¿Repetir formulario de ingreso? (Si o No): ").strip().lower()
    if repetir != "si":
        break  # Sale del ciclo si el usuario no quiere repetir el formulario