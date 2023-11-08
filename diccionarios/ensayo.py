# Creamos un diccionario para almacenar la información de los equipos.
equipos = {}

# Función para agregar un equipo.
def agregar_equipo(id_equipo, dispositivo, cargador, mouse):
    equipos[id_equipo] = {'dispositivo': dispositivo, 'cargador': cargador, 'mouse': mouse}
    print(f'Equipo con ID {id_equipo} agregado con éxito.')

# Función para agregar una novedad.
def agregar_novedad(id_equipo, fecha, descripcion):
    if id_equipo in equipos:
        if 'novedades' not in equipos[id_equipo]:
            equipos[id_equipo]['novedades'] = []
        equipos[id_equipo]['novedades'].append({'fecha': fecha, 'descripcion': descripcion})
        print(f'Novedad agregada al equipo con ID {id_equipo}.')
    else:
        print(f'El equipo con ID {id_equipo} no existe.')
