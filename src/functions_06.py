def frecuencia_hashtag(text: str) -> dict:
    """
    Recibe un texto y retorna un diccionario con la cantidad
    de palabras con hashtag, ignorando signos de puntuacion.
    """
    palabras_hashtag = dict()
    palabras_separadas = text.split()

    for palabra in palabras_separadas:
        if palabra.startswith("#"):
            # Limpiamos signos al final de la palabra
            palabra_limpia = palabra.rstrip(".,;:!?")
            
            # Asignamos 0 por defecto si la clave no existe todavia
            palabras_hashtag[palabra_limpia] = palabras_hashtag.get(palabra_limpia, 0) + 1

    return palabras_hashtag