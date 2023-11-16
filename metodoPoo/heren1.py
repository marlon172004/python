# Definición de la clase Fruta
class Fruta:
    # Método de inicialización (__init__)
    def __init__(self, nombre):
        # Atributo para el nombre de la fruta
        self.nombre = nombre

    # Método para obtener el color de la fruta (implementación por defecto)
    def obtener_color(self):
        return "Desconocido"

# Definición de la clase Manzana, que hereda de Fruta
class Manzana(Fruta):
    # Método para obtener el color de la manzana (sobrescribe el método de Fruta)
    def obtener_color(self):
        return "Rojo"

# Definición de la clase Platano, que hereda de Fruta
class Platano(Fruta):
    # Método para obtener el color del plátano (sobrescribe el método de Fruta)
    def obtener_color(self):
        return "Amarillo"

# Uso de las clases
# Crear una instancia de la clase Fruta
fruta_generica = Fruta("Fruta")
# Imprimir el nombre y el color de la fruta (usando la implementación por defecto de Fruta)
print(f"{fruta_generica.nombre} tiene un color {fruta_generica.obtener_color()}")

# Crear una instancia de la clase Manzana
manzana = Manzana("Manzana")
# Imprimir el nombre y el color de la manzana (usando la implementación específica de Manzana)
print(f"{manzana.nombre} tiene un color {manzana.obtener_color()}")

# Crear una instancia de la clase Platano
platano = Platano("Plátano")
# Imprimir el nombre y el color del plátano (usando la implementación específica de Platano)
print(f"{platano.nombre} tiene un color {platano.obtener_color()}")


