import http.server
import socketserver
import json


class HTTPRequest(http.server.BaseHTTPRequestHandler):
    def do_GET(self):
        request_path = self.path  # request_path est égal au chemin actuel
        if request_path == '/':  # Gestion de l'endpoint racine
            self.send_response(200)
            self.send_header("Content-type", "text/plain")
            self.end_headers()
            self.wfile.write(b"Hello, this is a simple API!")
        elif request_path == '/data':  # si request_path est /data
            dataset = {"name": "John", "age": 30, "city": "New York"}
            self.send_response(200)  # Envoie un code de succès 200

            # Définit le type de contenu à JSON
            self.send_header("Content-type", "application/json")
            self.end_headers()  # Termine les modifications des en-têtes

            # Convertie "dataset" en json, l'encode en octets,
            # et envoie la chaine dans la réponse HTTP
            self.wfile.write(json.dumps(dataset).encode())
        elif request_path == '/info':
            dataset = {"version": "1.0", "description": "A simple API built with http.server"}
            self.send_response(200)  # Envoie un code de succès 200

            # Définit le type de contenu à JSON
            self.send_header("Content-type", "application/json")
            self.end_headers()  # Termine les modifications des en-têtes

            # Convertie "dataset" en json, l'encode en octets,
            # et envoie la chaine dans la réponse HTTP
            self.wfile.write(json.dumps(dataset).encode())
        else:
            self.send_response(404)  # Renvoyer le code de statut 404
            self.send_header("Content-type", "text/plain")
            self.end_headers()
            self.wfile.write(b"404 Not Found")

PORT = 8000
with socketserver.TCPServer(("", PORT), HTTPRequest) as httpd:
    print("serving at port", PORT)
    httpd.serve_forever()
