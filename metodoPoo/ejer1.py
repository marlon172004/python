# Definición de la clase Lampara
class Lampara:
    # Método de inicialización (__init__)
    def __init__(self):
        # Atributo para rastrear si la lámpara está encendida o apagada
        self.encendida = False

    # Método para encender la lámpara
    def encender(self):
        self.encendida = True
        return "Lámpara encendida."

    # Método para apagar la lámpara
    def apagar(self):
        self.encendida = False
        return "Lámpara apagada."

    # Método para obtener el estado actual de la lámpara
    def estado(self):
        return "Encendida" if self.encendida else "Apagada"

# Crear una instancia de la clase Lampara
mi_lampara = Lampara()

# Realizar acciones con la lámpara
print(mi_lampara.encender())  # Enciende la lámpara y muestra un mensaje
print(mi_lampara.estado())    # Muestra el estado actual de la lámpara (encendida)
print(mi_lampara.apagar())    # Apaga la lámpara y muestra un mensaje
print(mi_lampara.estado())    # Muestra el estado actual de la lámpara (apagada)

