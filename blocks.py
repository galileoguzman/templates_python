# -*- coding: utf-8 -*-
nombres = {('juanito', 'perez'), ('pedrito', 'martinez'), ('eufemio', 'fernandez')}

with open("templates/lista.html", "r") as archivo:
    plantilla = archivo.read()
html = plantilla.split("<!--block-->")
block = ''

for n in nombres:
	block += html[1].format(nombre=n[0],apellido=n[1])


print html[0] + block + html[2]