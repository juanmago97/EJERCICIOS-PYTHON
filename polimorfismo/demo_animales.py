try:
    from .perro import Perro
    from .gato import Gato
except ImportError:
    from perro import Perro
    from gato import Gato


def demo():
    animales = [Perro(), Gato()]
    for a in animales:
        a.speak()


if __name__ == "__main__":
    demo()
