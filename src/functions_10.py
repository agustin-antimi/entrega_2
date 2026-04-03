def inicializar_participante(participantes, name):
    """
    Inicializa el diccionario para un participante nuevo
    """
    
    # Inicializamos al participante con su nombre como key
    participantes[name] = {
        "total_score": 0,
        "max_points": 0,
        "wining_rounds": 0
    }

def actualizar_puntajes(participantes, name, suma):
    """
    Contador de puntaje total, y maximo del participante
    """
    
    participantes[name]["total_score"] += suma
    
    # Compara y actualiza el record personal si es necesario
    if suma > participantes[name]["max_points"]:
        participantes[name]["max_points"] = suma

def procesar_ronda(ronda, participantes):
    """
    Procesa una ronda completa
    """
    
    # Estructura que nos permite alamacenar el total de puntos por participante
    round_points = {}
    
    # Procesa todos los puntajes de la ronda
    for name, judges in ronda["scores"].items():
        suma = sum(judges.values())
        
        # Si el participante aun no se encuentra registado, lo inicializamos
        if name not in participantes:
            inicializar_participante(participantes, name)
            
        # Actualizamos los campos del participante    
        actualizar_puntajes(participantes, name, suma)
        round_points[name] = suma
        
    return round_points

def registrar_ganador_ronda(participantes, round_winner, theme, round_points):
    """
    Encuentra al ganador usando max
    """
    
    # Obtenemos el nombre del ganador de la ronda
    name_round_winner = max(round_points, key=round_points.get)
    
    # Actualizamos la cantidad de rondas ganadas
    participantes[name_round_winner]["wining_rounds"] += 1
    round_winner[theme] = {name_round_winner: round_points[name_round_winner]}

def definir_promedios(points, rounds):
    """
    Determina un promedio en base a un total de puntos y 
    la cantidad de rondas
    """

    return points / rounds


def ordenar_participantes(participantes):
    """
    Ordena a los participantes en del diccionario por puntos de forma descendente
    """

    participantes_sorted = dict(sorted(
            participantes.items(),
            # x[1] accede al diccionario interno de cada participante
            key=lambda x: x[1]["total_score"],
            reverse=True 
        ))
    
    return participantes_sorted