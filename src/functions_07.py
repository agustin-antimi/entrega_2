import random


def definir_amigos_invisibles(lista: list) -> dict:
    """
    Recibe un str de elementos, separados por coma, y devuelve un diccionario
    donde cada elemento le pertenece a otro sin repetirse, y sin que un elemento
    se apunte a si mismo.
    """
    # Nos aseguramos que no haya elementos duplicados utilizando un set
    amigos = set(lista.split(","))
    amigos = {amigo.lower().rstrip(".,") for amigo in amigos}

    # Un return temprano en caso de no haber mas de 3 elementos
    if len(amigos) < 3:
        print("Debe haber al menos 3 amigos")
        return

    # Creamos una copia y los mezclamos
    amigos_mezclados = list(amigos)
    random.shuffle(amigos_mezclados)

    # Creamos un diccionario vacio donde guardaremos las asignaciones
    amigos_invisibles = dict()

    # iteramos
    for i in range(len(amigos_mezclados)):
        # La key sera el amigo mezcaldo
        key = amigos_mezclados[i]

        # Y para el value utilizamos este metodo para evitar errores de indice
        value = amigos_mezclados[(i + 1) % len(amigos_mezclados)]

        # Asignamos la key y el value a nuestro diccionario vacio
        amigos_invisibles[key] = value

    return amigos_invisibles
