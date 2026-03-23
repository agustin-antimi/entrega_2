# Funcion auxiliar
def calcular_costo_envio(peso: float, zona: str) -> str:
    """
    Recibe un peso y una zona ['local', 'regional', 'nacional'] y retorna
    un str espesificando el costo de envio.
    """
    zona = zona.lower().strip()
    
    # Diccionario de tarifas
    tarifas = {
        "local": [500, 1000, 2000],
        "regional": [1000, 2500, 5000],
        "nacional": [2000, 4500, 8000]
    }
    
    # Verificamos si la zona existe
    if zona not in tarifas:
        return "Error: La zona no es valida. Ingrese local, regional o nacional."
    
    # Determinamos el peso y en base a eso asignamos un indice
    if peso <= 1:
        indice_tarifa = 0
    elif 1 < peso <= 5:
        indice_tarifa = 1
    else:
        indice_tarifa = 2
        
    # Obtenemos el costo con el diccionario de tarifas
    costo = tarifas[zona][indice_tarifa]
            
    return f"El costo de envio para un paquete de {peso}kg a la zona {zona} es de ${costo}"

# Imprime el resultado y permite ingresar valores
def calculadora_precio_envio():
    """
    Sirve como entrada y salida para e usuario
    """
    print("--- Calculadora de Costo de Envio ---")
    try:
        peso_input = float(input("Ingrese el peso del paquete en kg: "))
        
        # Validamos que el peso no sea un numero negativo ni 0
        if peso_input <= 0:
            print("Error: El peso debe ser mayor a 0.")
            return

        zona_input = input("Ingrese la zona de destino (local, regional, nacional): ")
        
        resultado = calcular_costo_envio(peso_input, zona_input)
        print(resultado)
        
    except ValueError:
        print("Error: El peso debe ser un numero valido.")