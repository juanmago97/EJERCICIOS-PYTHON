class Empleado:
    def __init__(self, nombre, salario):
        self.nombre = nombre
        self.salario = salario

    def info(self):
        return f"{self.nombre} gana {self.salario}€"
