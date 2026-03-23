def frecuencia_hashtag(posts: list[str]) -> dict:
    """
    Recibe una lista de textos y retorna un diccionario
    con la cantidad total de palabras con hashtag.
    """
    palabras_hashtag = dict()

    # Recorremos cada post dentro de la lista de posts
    for post in posts:
        palabras_separadas = post.split()

        # Recorremos cada palabra del post actual
        for palabra in palabras_separadas:
            if palabra.startswith("#"):
                # Limpiamos los signos de puntuacion
                palabra_limpia = palabra.rstrip(".,;:!?")

                # Actualizamos el contador usando get
                palabras_hashtag[palabra_limpia] = (
                    palabras_hashtag.get(palabra_limpia, 0) + 1
                )

    return palabras_hashtag
