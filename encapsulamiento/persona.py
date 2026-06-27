class Persona:
    def __init__(self, nombre, edad):
        self.nombre = nombre
        self.__edad = None
        self.edad = edad

    @property
    def edad(self):
        return self.__edad

    @edad.setter
    def edad(self, valor):
        if valor < 0:
            raise ValueError("Edad no puede ser negativa")
        self.__edad = valor
