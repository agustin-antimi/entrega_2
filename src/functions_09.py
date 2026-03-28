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
        # Hacemos un casteo del elemento a tipo nuemerico
        float(registro["grade"])

        return True

    except:
        return False
