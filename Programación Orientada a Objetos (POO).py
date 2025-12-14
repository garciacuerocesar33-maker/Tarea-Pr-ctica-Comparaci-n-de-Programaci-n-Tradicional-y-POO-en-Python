class ClimaDiario:
    """
    Clase que representa la información diaria del clima.
    Aplica encapsulamiento con atributos privados.
    """
    def __init__(self, dia, temperatura=None):
        """
        Inicializa un día de clima.
        Parámetros:
        - dia: int, número del día (1-7).
        - temperatura: float opcional, temperatura en °C.
        """
        self.__dia = dia  # Atributo privado
        self.__temperatura = temperatura  # Atributo privado

    # Getter para temperatura (encapsulamiento)
    def get_temperatura(self):
        return self.__temperatura

    # Setter para temperatura con validación
    def set_temperatura(self, temperatura):
        if isinstance(temperatura, (int, float)):
            self.__temperatura = float(temperatura)
        else:
            raise ValueError("La temperatura debe ser un número.")

    # Getter para día
    def get_dia(self):
        return self.__dia

    # Método para ingresar temperatura (interactivo)
    def ingresar_temperatura(self):
        """
        Solicita al usuario ingresar la temperatura para este día.
        """
        while True:
            try:
                temp = float(input(f"Ingrese la temperatura del día {self.__dia} (en °C): "))
                self.set_temperatura(temp)
                break
            except ValueError as e:
                print(f"Error: {e}. Intente de nuevo.")

class SemanaClima:
    """
    Clase que representa una semana de clima, conteniendo objetos ClimaDiario.
    Maneja el cálculo del promedio semanal.
    """
    def __init__(self):
        self.__dias = [ClimaDiario(dia) for dia in range(1, 8)]  # Lista privada de objetos

    # Método para ingresar temperaturas para todos los días
    def ingresar_temperaturas_semanales(self):
        """
        Itera sobre cada día y solicita la temperatura.
        """
        for dia in self.__dias:
            dia.ingresar_temperatura()

    # Método para calcular el promedio semanal (polimorfismo: puede ser sobrescrito)
    def calcular_promedio_semanal(self):
        """
        Calcula el promedio de las temperaturas de la semana.
        Retorna: float, el promedio.
        """
        temperaturas = [dia.get_temperatura() for dia in self.__dias if dia.get_temperatura() is not None]
        if not temperaturas:
            return 0.0
        return sum(temperaturas) / len(temperaturas)

    # Método para mostrar el promedio
    def mostrar_promedio(self):
        promedio = self.calcular_promedio_semanal()
        print(f"El promedio semanal de temperaturas es: {promedio:.2f} °C")

# Función principal para la versión POO
def main():
    """
    Función principal: crea una instancia de SemanaClima y ejecuta el proceso.
    """
    print("Programa para calcular el promedio semanal del clima (Versión POO)")
    semana = SemanaClima()
    semana.ingresar_temperaturas_semanales()
    semana.mostrar_promedio()

# Ejecutar el programa si se corre este archivo
if __name__ == "__main__":
    main()