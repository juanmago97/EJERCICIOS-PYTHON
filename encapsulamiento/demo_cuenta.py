try:
    from .cuenta import Cuenta
except ImportError:
    from cuenta import Cuenta


def demo():
    c = Cuenta("Luis", 100)
    print("Saldo inicial:", c.ver_saldo())
    c.depositar(50)
    print("Después de depositar 50:", c.ver_saldo())
    print("Intento retirar 200 ->", c.retirar(200), "Saldo:", c.ver_saldo())
    print("Retirar 100 ->", c.retirar(100), "Saldo:", c.ver_saldo())


if __name__ == "__main__":
    demo()
