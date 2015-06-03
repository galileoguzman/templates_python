# IMPLEMENTACIÓN DE PLANTILLAS EN PYTHON

Python <https://www.python.org/> es uno de los lenguajes más populares hoy en día, promoviendo el desarrollo ágil de proyectos con una sintaxis limpia.

![Python logo](https://www.python.org/static/img/python-logo@2x.png "Python Logo")


	#Renderizar una plantilla con Python y format
	
	with open("archivo.html") as archivo:
		plantilla = archivo.read()
	
	print plantilla.format(nombre="Juanito",apellidos="Juárez", edad=52)
	
El código anterior muestra el uso de como renderizar una plantilla en python.
