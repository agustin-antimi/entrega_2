def imprimir_cant_elementos(lista_original: list, lista_limpia: list) -> None:
    """
    Recibe dos listas de alumnos  una original y otra limpia
    e imprime la cantidad de registros de cada una
    """
    print(f"Cantidad de alumnos en la lista original: {len(lista_original)}")
    print(f"Cantidad de alumnos en la lista limpia: {len(lista_limpia)}")


def comprobar_numero(registro: dict) -> bool:
    """
    Recibe un registro de diccionario y comprueba la key "grade"
    tiene un str que sea valido como dato numerico
    """

    ## Utilizamos una estructura try, que nos sirve para saber si podemos
    #  castear el str a un float, por lo que seria numerico, en es caso
    #  devolvemos True, si lanza un error entonces devolvemos un False.
    try:
        float(registro["grade"])
        return True
    
    except:
        return False
    

def eliminar_duplicados(estudiantes: list[dict]) -> list[dict]:
    """
    Recibe una lista de diccionarios donde cada dict es un alumno, eliminando
    alumnos con el campo ["name"] duplicado, quedandose con el valor mas alto
    en el campo ["nota"]
    """
    mejores_notas = {}

    for estudiante in estudiantes:
        nombre = estudiante.get("name")
        nota_actual = estudiante.get("grade", 0)

        # Si el nombre no esta registrado, o si encontramos una nota mayor
        if nombre not in mejores_notas or nota_actual > mejores_notas[nombre].get("grade", 0):
            mejores_notas[nombre] = estudiante

    # Convertimos los valores del diccionario de vuelta a una lista
    return list(mejores_notas.values())
