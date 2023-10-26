aprendices = []
edades = []

nombres_edades = [
    ["Sebastian Tovar", 17],["Juan Mahecha", 17],["Maria Buenaventura", 17],["Mathew Guarnizo", 17],["Kevin Hernan", 17],["Melissa Lopez", 16],
    ["Vanesa Ladino", 17],["Stiven Ramirez", 18],["Esteban Prada", 17],["Kevin Botero", 17],["Sebastian Pinzon", 17],["Camila Alape", 18],["Kevin Londoño", 23],
    ["Nicolas Fierro", 18],["Santiago Gomez", 17],["Marlon Lopez", 19],["Stiwar Perez", 18],["Miguel Bernal", 17], ["Maria Molano", 18],["Nicolas Paulo", 17],
    ["Laura Benavides", 17],["Wilfrank", 18],["Dahiana", 18],["Lina Barrios", 18],["Maria jose", 18],["Nataly", 17],["Matias Guzman", 17],["cristian Peña", 17],
    ["Paula Garcia", 20]
]
#Indique un dato a buscar en la lista de aprendices

for nombre, edad in nombres_edades:
    aprendices.append(nombre)
    buscarA = "Laura Benavides"
if buscarA in aprendices:
    print(f"{buscarA} está en la lista de aprendices.")
else:
    print(f"{buscarA} no está en la lista de aprendices.")
