# Importamos dependencias
import string

def cifrar_mensaje_map(mensaje: str, desplazamientos: int) -> str:
    # Generamos un abecedario
    abecedario = string.ascii_lowercase
    total_letras = len(abecedario)

    # Comprension de diccionario,
    # donde desplazamos en base al abecedario original
    mapa_cifrado = {
        letra: abecedario[(indice + desplazamientos) % total_letras]
        for indice, letra in enumerate(abecedario)
    }

    # Utiizamos la funcion map, para cifrar el msj original
    mensaje_cifrado = map(lambda c: mapa_cifrado.get(c, c), mensaje.lower())

    # Unimos todo el resultado en un solo str
    return "".join(mensaje_cifrado)