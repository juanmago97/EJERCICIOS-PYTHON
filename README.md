Ejercicios OOP (Herencia, Polimorfismo, Encapsulamiento)

Estructura ahora organizada por carpetas:

- herencia/
	- vehiculo.py
	- coche.py
	- camion.py
	- empleado.py
	- gerente.py
	- demo_vehiculos.py
	- demo_empleados.py
- polimorfismo/
	- animal.py
	- perro.py
	- gato.py
	- rectangulo.py
	- circulo.py
	- demo_animales.py
	- demo_formas.py
- encapsulamiento/
	- cuenta.py
	- demo_cuenta.py
	- persona.py
	- demo_persona.py
- runner.py  -> Ejecuta demos organizados por concepto

Cómo ejecutar (desde la carpeta `oop_ejercicios`):

```powershell
python runner.py
```

Notas:
- Cada módulo contiene clases con responsabilidades separadas para resaltar buenas prácticas (base vs. subclase, validación en setters, operaciones sobre datos privados).
- Usa los archivos `demo_*.py` para mostrar ejemplos en clase; `runner.py` ejecuta todos los demos en orden.
