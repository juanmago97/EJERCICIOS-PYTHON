try:
    from .vehiculo import Vehiculo
except ImportError:
    from vehiculo import Vehiculo

class Coche(Vehiculo):
    def __init__(self, marca, modelo, puertas, placa, frenado, ley_C, velocidad
                 
                 ):
        super().__init__(marca, modelo, placa, frenado, ley_C, velocidad)
        self.puertas = puertas

    def describe(self):
        return f" Coche: {super().describe()} HIJO ({self.puertas} puertas)"
