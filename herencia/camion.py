try:
    from .vehiculo import Vehiculo
except ImportError:
    from vehiculo import Vehiculo

class Camion(Vehiculo):
    def __init__(self, marca, modelo, capacidad_kg,placa, frenado, ley_C, velocidad):
        super().__init__(marca, modelo,placa, frenado, ley_C, velocidad )
        self.capacidad_kg = capacidad_kg

    def describe(self):
        return f"Camión: {super().describe()} (capacidad {self.capacidad_kg} kg)"
    







    
