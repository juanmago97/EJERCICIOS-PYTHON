# Runner para demostrar los 6 ejercicios de OOP
# Ejecuta la función `demo()` de cada ejercicio para mostrar salidas simples.

from herencia.demo_vehiculos import demo as demo_vehiculos
from herencia.demo_empleados import demo as demo_empleados
from polimorfismo.demo_animales import demo as demo_animales
from polimorfismo.demo_formas import demo as demo_formas
from encapsulamiento.demo_cuenta import demo as demo_cuenta
from encapsulamiento.demo_persona import demo as demo_persona


def main():
    print("--- Herencia: Vehículos")
    demo_vehiculos()
    print()

    print("--- Herencia: Empleado/Gerente")
    demo_empleados()
    print()

    print("--- Polimorfismo: Animales")
    demo_animales()
    print()

    print("--- Polimorfismo: Formas")
    demo_formas()
    print()

    print("--- Encapsulamiento: Cuenta")
    demo_cuenta()
    print()

    print("--- Encapsulamiento: Persona")
    demo_persona()
    print()


if __name__ == "__main__":
    main()
