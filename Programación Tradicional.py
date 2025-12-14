# Función para ingresar las temperaturas diarias de la semana (7 días)
def ingresar_temperaturas():
    """
    Solicita al usuario ingresar las temperaturas diarias para 7 días.
    Retorna una lista de temperaturas (floats).
    """
    temperaturas = []
    for dia in range(1, 8):  # Del día 1 al 7
        while True:
            try:
                temp = float(input(f"Ingrese la temperatura del día {dia} (en °C): "))
                temperaturas.append(temp)
                break
            except ValueError:
                print("Por favor, ingrese un número válido.")
    return temperaturas

# Función para calcular el promedio semanal de las temperaturas
def calcular_promedio_semanal(temperaturas):
    """
    Calcula el promedio de una lista de temperaturas.
    Parámetros:
    - temperaturas: lista de floats con las temperaturas diarias.
    Retorna: el promedio como float.
    """
    if not temperaturas:
        return 0.0  # Evita división por cero si la lista está vacía
    return sum(temperaturas) / len(temperaturas)

# Función principal que organiza el flujo del programa
def main():
    """
    Función principal: coordina la entrada de datos y el cálculo del promedio.
    """
    print("Programa para calcular el promedio semanal del clima (Versión Tradicional)")
    temperaturas = ingresar_temperaturas()
    promedio = calcular_promedio_semanal(temperaturas)
    print(f"El promedio semanal de temperaturas es: {promedio:.2f} °C")

# Ejecutar el programa si se corre este archivo
if __name__ == "__main__":
    main()