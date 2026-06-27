class Vehiculo:
    def __init__(self, marca, modelo, placa, frenado, ley_C, velocidad):
        self.marca = marca
        self.modelo = modelo
        self.placa = placa
        self.frenado = frenado
        self.ley_C = ley_C
        self.velocidad = velocidad


    def describe(self):
        return f"METODO PADRE: {self.marca} {self.modelo} (Placa: {self.placa}, Frenado: {self.frenado}, Ley de Circulación: {self.ley_C}, Velocidad: {self.velocidad})"
