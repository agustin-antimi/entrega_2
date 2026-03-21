import re

def contar_lineas(cadena: str) -> int:
    '''Retorna la cantidad de lineas de una cadena'''
    return len(cadena.split("\n"))

def contar_palabras(cadena: str) -> int:
    '''Retorna la cantidad de palabras filtrando solo letras'''
    # iteramos sobre todo la cadena para hallar chars que sean letras
    texto_limpio = ""
    for caracter in cadena:
        if caracter.isalpha():
            texto_limpio += caracter
        else:
            texto_limpio += " "
        
    return len(texto_limpio.split())

def prom_palabras(cadena: str) -> float:
    '''Retorna el promedio de palabras por linea de una cadena'''
    cant_lineas = contar_lineas(cadena)
    cant_palabras = contar_palabras(cadena)
    return cant_palabras / cant_lineas  

def encima_prom(cadena: str) -> list:
    '''Retorna una lista con las lineas por encima del promedio'''
    lineas = cadena.split("\n")
    promedio = prom_palabras(cadena)
    lineas_encima_prom = [x for x in lineas if contar_palabras(x) > promedio]
    return lineas_encima_prom