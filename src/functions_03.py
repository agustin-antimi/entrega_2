def remplazar_spoilers(spoilers: str, texto: str) -> str:
    '''Recibe una lista de palabras que son spoilers y devuelve el texto sin spoilers'''
    
    spoilers = [palabra.strip().lower() for palabra in spoilers.split(",")]

    palabras = texto.split()
    texto_censurado = []

    for palabra in palabras:
        if palabra.lower() in spoilers:
            texto_censurado.append("*" * len(palabra))
        else:
            texto_censurado.append(palabra)

    texto_censurado_str = " ".join(texto_censurado)

    return texto_censurado_str   