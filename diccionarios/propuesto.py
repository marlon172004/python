# Creamos un diccionario para almacenar la información de los equipos.
equipos = {}

# Función para agregar un equipo.
def agregarEquipo(idEquipo, dispositivo, cargador, mouse):
    equipos[idEquipo] = {'dispositivo': dispositivo, 'cargador': cargador, 'mouse': mouse}
    print(f'Equipo con ID {idEquipo} agregado con éxito.')

# Función para agregar una novedad.
def agregarNovedad(idEquipo, fecha, descripcion):
    if idEquipo in equipos:
        if 'novedades' not in equipos[idEquipo]:
            equipos[idEquipo]['novedades'] = []
        equipos[idEquipo]['novedades'].append({'fecha': fecha, 'descripcion': descripcion})
        print(f'Novedad agregada al equipo con ID {idEquipo}.')
    else:
        print(f'El equipo con ID {idEquipo} no existe.')

# Función para buscar un equipo por su ID.
def buscarEquipo(idEquipo):
    if idEquipo in equipos:
        print(f'Información del equipo con ID {idEquipo}:')
        print(equipos[idEquipo])
    else:
        print(f'El equipo con ID {idEquipo} no existe.')

# Función para mostrar un reporte de equipos con novedades.
def mostrar_reporte_novedades():
    for idEquipo, equipo in equipos.items():
        if 'novedades' in equipo:
            print(f'ID del equipo: {idEquipo}')
            for novedad in equipo['novedades']:
                print(f'Fecha: {novedad["fecha"]}')
                print(f'Descripción: {novedad["descripcion"]}')
            print('---')

# Aquí puedes agregar más funciones para modificar y eliminar equipos, si lo necesitas.

# Ejemplo de uso:
agregarEquipo('001', 'Laptop', True, True)
agregarNovedad('001', '2023-11-07', 'Pantalla rota')
buscarEquipo('001')
mostrar_reporte_novedades()
