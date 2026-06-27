try:
    from .rectangulo import Rectangulo
    from .circulo import Circulo
except ImportError:
    from rectangulo import Rectangulo
    from circulo import Circulo


def demo():
    formas = [Rectangulo(2, 3), Circulo(1)]
    for i, f in enumerate(formas, 1):
        print(f"Forma {i}: área = {f.area():.2f}")
    print(f"Área total: {sum(f.area() for f in formas):.2f}")


if __name__ == "__main__":
    demo()
