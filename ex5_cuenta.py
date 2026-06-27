# Ejercicio 5 - Encapsulamiento: Cuenta bancaria simple
# Objetivo: proteger datos con atributos privados y exponer operaciones seguras.

class Cuenta:
    def __init__(self, titular, saldo=0):
        self.titular = titular
        self.__saldo = saldo  # atributo privado (name mangling)

    def depositar(self, cantidad):
        """Suma dinero si la cantidad es positiva."""
        if cantidad > 0:
            self.__saldo += cantidad

    def retirar(self, cantidad):
        """Resta dinero sólo si hay suficiente saldo. Devuelve True/False."""
        if 0 < cantidad <= self.__saldo:
            self.__saldo -= cantidad
            return True
        return False

    def ver_saldo(self):
        """Acceso controlado al saldo (lectura)."""
        return self.__saldo


def demo():
    c = Cuenta("Luis", 100)
    print("Saldo inicial:", c.ver_saldo())
    c.depositar(50)
    print("Después de depositar 50:", c.ver_saldo())
    exito = c.retirar(200)
    print("Intento retirar 200 ->", exito, "Saldo:", c.ver_saldo())
    exito = c.retirar(100)
    print("Retirar 100 ->", exito, "Saldo:", c.ver_saldo())


if __name__ == "__main__":
    demo()
