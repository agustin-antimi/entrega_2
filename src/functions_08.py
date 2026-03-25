import string

def cifrado_cesar(mensaje, desplazamientos):
    # Definimos un abaecedario para minusculas y para mayusculas
    abc_min = string.ascii_lowercase
    abc_may = string.ascii_uppercase
    
    # Hacemos el deplazamiento en ambos dicts
    mapa_min = {
        letra: abc_min[(indice + desplazamientos) % 26]
        for indice, letra in enumerate(abc_min)
    }
    mapa_may = {
        letra: abc_may[(indice + desplazamientos) % 26]
        for indice, letra in enumerate(abc_may)
    }
    
    # Unimos ambos diccionarios en uno solo usando el operador **
    mapa_completo = {**mapa_min, **mapa_may}
    
    # Hacemos un map sobre el mensaje, 
    # intercambiando las letras en caso de que sea necesario
    caracteres_cifrados = map(lambda c: mapa_completo.get(c, c), mensaje)
    
    return "".join(caracteres_cifrados)