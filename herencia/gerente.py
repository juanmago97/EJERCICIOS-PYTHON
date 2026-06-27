try:
    from .empleado import Empleado
except ImportError:
    from empleado import Empleado

class Gerente(Empleado):
    def __init__(self, nombre, salario, departamento):
        super().__init__(nombre, salario)
        self.departamento = departamento

    def informar(self):
        return f"{self.info()} y dirige {self.departamento}"
