# Ejercicio 2 - Herencia: Empleado / Gerente
# Objetivo: extender comportamiento de una clase base en una subclase.

class Empleado:
    def __init__(self, nombre, salario):
        self.nombre = nombre
        self.salario = salario

    def info(self):
        """Devuelve información básica del empleado."""
        return f"{self.nombre} gana {self.salario}€"

class Gerente(Empleado):
    def __init__(self, nombre, salario, departamento):
        super().__init__(nombre, salario)
        self.departamento = departamento

    def informar(self):
        """Método extra que sólo tiene el gerente."""
        return f"{self.info()} y dirige {self.departamento}"


def demo():
    g = Gerente("Ana", 45000, "Ventas")
    print(g.informar())


if __name__ == "__main__":
    demo()
