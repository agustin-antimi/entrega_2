def convert_to_time_format(seconds: float) -> str:
    """Recibe un total de segundos y devuelve un str
    representando al tiempo en formato [m:ss]"""
    minutes, seconds = divmod(seconds, 60)

    minutes = str(minutes)
    seconds = str(seconds)

    time = minutes + "m" + " " + seconds + "s"
    return time


def convert_to_seconds(time: str) -> int:
    """Recibe un tiempo en formato [m:ss] y
    retorna la cantidad de segundos totales"""
    time_splited = time.split(":")
    
    seconds = int(time_splited[1]) + int(time_splited[0]) * 60
    return seconds
