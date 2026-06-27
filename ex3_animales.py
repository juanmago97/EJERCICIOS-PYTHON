# Ejercicio 3 - Polimorfismo: Animales que hablan
# Objetivo: demostrar que el mismo método puede tener implementaciones diferentes.

class Animal:
    def speak(self):
        """Interfaz: las subclases deben implementar este método."""
        raise NotImplementedError("Subclase debe implementar speak")

class Perro(Animal):
    def speak(self):
        print("Guau!")

class Gato(Animal):
    def speak(self):
        print("Miau!")


def demo():
    animales = [Perro(), Gato()]
    for a in animales:
        a.speak()  # mismo llamado, comportamiento según la clase concreta


if __name__ == "__main__":
    demo()
