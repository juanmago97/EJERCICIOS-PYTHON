try:
    from .coche import Coche
    from .camion import Camion
except ImportError:
    from coche import Coche
    from camion import Camion


def demo():
    c = Coche("Toyota", "Corolla", 4, "ABC123", 5, 100, 60)
    m = Camion("Volvo", "FH", 12000, "XYZ789", 10, 80, 40)
    print(c.describe())
    print(m.describe())


if __name__ == "__main__":
    demo()
