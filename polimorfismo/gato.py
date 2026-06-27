try:
    from .animal import Animal
except ImportError:
    from animal import Animal

class Gato(Animal):
    def speak(self):
        print("Miau!")
