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