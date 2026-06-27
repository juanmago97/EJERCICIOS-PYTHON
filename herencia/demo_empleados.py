try:
    from .gerente import Gerente
except ImportError:
    from gerente import Gerente


def demo():
    g = Gerente("Ana", 45000, "Ventas")
    print(g.informar())


if __name__ == "__main__":
    demo()
