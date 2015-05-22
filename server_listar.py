# -*- coding: utf-8 -*-
from BaseHTTPServer import BaseHTTPRequestHandler
import urlparse

class GetHandler(BaseHTTPRequestHandler):
    
    def do_GET(self):
    	#extraer plantilla y formatear con datos
    	nombres = {('juanito', 'perez'), ('pedrito', 'martinez'), ('eufemio', 'fernandez')}
    	with open("templates/lista.html", "r") as archivo:
    		plantilla = archivo.read()
		html = plantilla.split("<!--block-->")
		block = ''

		for n in nombres:
			block += html[1].format(nombre=n[0],apellido=n[1])


		salida = html[0] + block + html[2]

		#Escritora de cabeceras y entrega del server
        self.send_response(200)
        self.send_header("Content-type", "text/html")
        self.end_headers()
        self.wfile.write(salida)
        return

if __name__ == '__main__':
    from BaseHTTPServer import HTTPServer
    server = HTTPServer(('localhost', 8000), GetHandler)
    print 'Starting server, use <Ctrl-C> to stop'
    server.serve_forever()