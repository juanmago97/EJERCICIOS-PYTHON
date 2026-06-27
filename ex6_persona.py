# Ejercicio 6 - Encapsulamiento: Persona con propiedad `edad`
# Objetivo: usar @property para exponer y validar un atributo privado.

class Persona:
    def __init__(self, nombre, edad):
        self.nombre = nombre
        self.__edad = None
        self.edad = edad  # usa el setter para validar

    @property
    def edad(self):
        """Getter que devuelve la edad privada."""
        return self.__edad

    @edad.setter
    def edad(self, valor):
        """Valida que la edad no sea negativa."""
        if valor < 0:
            raise ValueError("Edad no puede ser negativa")
        self.__edad = valor


def demo():
    p = Persona("Marta", 30)
    print(p.nombre, "tiene", p.edad, "años")
    try:
        p.edad = -5
    except ValueError as e:
        print("Error al asignar edad inválida:", e)


if __name__ == "__main__":
    demo()
