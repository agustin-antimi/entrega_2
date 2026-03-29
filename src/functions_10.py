def inicializar_participante(participantes, name):
    """Inicializa el diccionario para un participante nuevo"""
    
    participantes[name] = {
        "total_score": 0,
        "max_points": 0,
        "wining_rounds": 0
    }

def actualizar_puntajes(participantes, name, suma):
    """Contador de puntaje total, y maximo del participante"""
    
    participantes[name]["total_score"] += suma
    
    # Compara y actualiza el record personal si es necesario
    if suma > participantes[name]["max_points"]:
        participantes[name]["max_points"] = suma

def procesar_ronda(ronda, participantes):
    """Procesa una ronda completa"""
    
    round_points = {}
    
    # Procesa todos los puntajes de una ronda especifica
    for name, judges in ronda["scores"].items():
        suma = sum(judges.values())
        
        if name not in participantes:
            inicializar_participante(participantes, name)
            
        actualizar_puntajes(participantes, name, suma)
        round_points[name] = suma
        
    return round_points

def registrar_ganador_ronda(participantes, round_winner, theme, round_points):
    """Encuentra al ganador usando max"""
    
    name_round_winner = max(round_points, key=round_points.get)
    
    # Suma la victoria y guarda el registro
    participantes[name_round_winner]["wining_rounds"] += 1
    round_winner[theme] = {name_round_winner: round_points[name_round_winner]}

def definir_promedios(points, rounds: int) -> float:
    """
    Determina un promedio en base a un total de puntos y 
    la cantidad de rondas
    """

    return points / rounds