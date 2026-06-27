# Ejercicio 1 - Herencia: Vehículos
# Objetivo: mostrar cómo una clase base comparte atributos y métodos con subclases.

class Vehiculo:
    def __init__(self, marca, modelo):
        self.marca = marca
        self.modelo = modelo

    def describe(self):
        """Devuelve una descripción básica del vehículo."""
        return f"{self.marca} {self.modelo}"

class Coche(Vehiculo):
    def __init__(self, marca, modelo, puertas):
        super().__init__(marca, modelo)  # reutiliza inicialización de la clase base
        self.puertas = puertas

    def describe(self):
        return f"Coche: {super().describe()} ({self.puertas} puertas)"

class Camion(Vehiculo):
    def __init__(self, marca, modelo, capacidad_kg):
        super().__init__(marca, modelo)
        self.capacidad_kg = capacidad_kg

    def describe(self):
        return f"Camión: {super().describe()} (capacidad {self.capacidad_kg} kg)"


def demo():
    c = Coche("Toyota", "Corolla", 4)
    m = Camion("Volvo", "FH", 12000)
    print(c.describe())
    print(m.describe())


if __name__ == "__main__":
    demo()
