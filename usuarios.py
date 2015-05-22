#utilizando la lectura de un archivo como str le pasamos valores de variables como una plantilla
with open("templates/usuarios.html", "r") as archivo:
	plantilla = archivo.read()
print plantilla.format(nombre="juanito", apellidos="perez")