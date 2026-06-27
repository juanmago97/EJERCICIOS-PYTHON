try:
    from .animal import Animal
except ImportError:
    from animal import Animal

class Perro(Animal):
    def speak(self):
        print("Guau!")
