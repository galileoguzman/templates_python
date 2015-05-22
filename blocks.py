# -*- coding: utf-8 -*-
nombres = {('juanito', 'perez'), ('pedrito', 'martinez'), ('eufemio', 'fernandez')}

with open("templates/lista.html", "r") as archivo:
    plantilla = archivo.read()
html = plantilla.split("<!--block-->")
block = html[1]
html[1] = ''

for n in nombres:
	html[1] += block.format(nombre=n[0],apellido=n[1])


print html[1]
#print html[0] + block + html[2]