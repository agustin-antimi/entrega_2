def validar_email(email: str) -> bool:
    """
    Recibe un email y verifica las condiciones:
    - Contiene exactamente un @.
    - Tiene al menos un carácter antes del @.
    - Tiene al menos un punto (.) después del @.
    - No empieza ni termina con @ ni con ..
    - La parte después del último punto tiene al menos 2 caracteres.
    """
    if email.count("@") != 1:
        return False
    if email.startswith(("@", ".")) or email.endswith(("@", ".")):
        return False

    # Separamos el texto en usuario y dominio
    partes = email.split("@")
    usuario = partes[0]
    dominio = partes[1]

    # Verificamos que haya al menos un caracter antes del @
    if len(usuario) < 1:
        return False

    # Verificamos que haya al menos un punto en el dominio
    if "." not in dominio:
        return False

    # Verificamos que la extension final tenga 2 o mas caracteres
    partes_dominio = dominio.split(".")
    extension = partes_dominio[-1]
    if len(extension) < 2:
        return False

    return True
