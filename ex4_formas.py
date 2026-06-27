# Ejercicio 4 - Polimorfismo (duck typing): Formas y áreas
# Objetivo: usar el mismo método `area()` en clases distintas y tratarlas uniformemente.

import math

class Rectangulo:
    def __init__(self, ancho, alto):
        self.ancho = ancho
        self.alto = alto

    def area(self):
        return self.ancho * self.alto

class Circulo:
    def __init__(self, radio):
        self.radio = radio

    def area(self):
        return math.pi * self.radio * self.radio


def demo():
    formas = [Rectangulo(2, 3), Circulo(1)]
    areas = [f.area() for f in formas]
    for i, f in enumerate(formas, 1):
        print(f"Forma {i}: área = {areas[i-1]:.2f}")
    print(f"Área total: {sum(areas):.2f}")


if __name__ == "__main__":
    demo()
