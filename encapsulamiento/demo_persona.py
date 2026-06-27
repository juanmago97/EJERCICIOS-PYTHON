try:
    from .persona import Persona
except ImportError:
    from persona import Persona


def demo():
    p = Persona("Marta", 30)
    print(p.nombre, "tiene", p.edad, "años")
    try:
        p.edad = -5
    except ValueError as e:
        print("Error al asignar edad inválida:", e)


if __name__ == "__main__":
    demo()
