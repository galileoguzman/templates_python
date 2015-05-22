from BaseHTTPServer import BaseHTTPRequestHandler
import urlparse
import json

class GetHandler(BaseHTTPRequestHandler):
    
    def do_GET(self):
        #extraer plantilla y formatear con datos
        dicc = [{'a':'Variable A', 'b':123, 'c':('a', 'x', 'y','z'), 'nombre':'juanito'}]

        self.send_response(200)
        self.send_header("Content-type", "application/json")
        self.end_headers()
        self.wfile.write(dicc)
        return

if __name__ == '__main__':
    from BaseHTTPServer import HTTPServer
    server = HTTPServer(('localhost', 8000), GetHandler)
    print 'Starting server, use <Ctrl-C> to stop'
    server.serve_forever()
    