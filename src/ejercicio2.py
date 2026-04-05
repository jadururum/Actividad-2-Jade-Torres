def sexagesimal_a_segundos(tiempo_str):
    minutos,segundos=map(int,tiempo_str.split(":"))
    return(minutos*60)+segundos

def segundos_a_sexagesimal(total_segundos):
    minutos=total_segundos//60
    segundos=total_segundos%60
    return f"{minutos}m {segundos}s"

def analizar_playlist(lista_canciones):
    total_segundos=0
    larga=lista_canciones[0]
    corta=lista_canciones[0]

    for cancion in lista_canciones:
        actual_segundos=sexagesimal_a_segundos(cancion["duration"])
        total_segundos+=actual_segundos

        if actual_segundos > sexagesimal_a_segundos(larga["duration"]):
            larga = cancion
        if actual_segundos < sexagesimal_a_segundos(corta["duration"]):
            corta = cancion
    
    return total_segundos,larga,corta
