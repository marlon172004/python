class Vehiculo:
    def obtener_velocidad(self):
        pass

class Coche(Vehiculo):
    def obtener_velocidad(self):
        return 120  # Velocidad en kilómetros por hora

class Bicicleta(Vehiculo):
    def obtener_velocidad(self):
        return 25  # Velocidad en kilómetros por hora

# Función que usa polimorfismo
def mostrar_velocidad(vehiculo):
    return vehiculo.obtener_velocidad()

# Crear instancias de las clases
mi_coche = Coche()
mi_bicicleta = Bicicleta()

# Llamar a la función usando polimorfismo
print(mostrar_velocidad(mi_coche))  # Salida esperada: 120
print(mostrar_velocidad(mi_bicicleta))  # Salida esperada: 25
