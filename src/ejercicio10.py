def puntos_por_ronda(puntos):
    """
    Función que suma los puntos totales de los 3 jueces para cada participante.
    """
    puntos_totales={}
    for nombre, jueces in puntos.items():
        puntos_totales[nombre] = sum(jueces.values())
    return puntos_totales

def obtener_ganador(resultados):
    """
    Función que retorna al cocinero con el puntaje más alto obtenido
    """
    ganador = max(resultados, key=resultados.get)
    return ganador, resultados[ganador]
