from BaseHTTPServer import BaseHTTPRequestHandler
import urlparse

class GetHandler(BaseHTTPRequestHandler):
    
    def do_GET(self):
        #extraer plantilla y formatear con datos
        with open("templates/usuarios.html", "r") as archivo:
            plantilla = archivo.read()
        salida = plantilla.format(nombre="juanito", apellidos="perez")
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