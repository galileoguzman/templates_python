with open("templates/usuarios.html", "r") as archivo:
	plantilla = archivo.read()
print plantilla.format(nombre="juanito", apellidos="perez")