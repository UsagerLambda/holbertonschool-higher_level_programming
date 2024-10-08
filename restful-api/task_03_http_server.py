import http.server
import socketserver
import time
import json


PORT = 8000
address = ("", PORT)

class RequestHandler(http.server.BaseHTTPRequestHandler):
    def do_GET(self):
        if self.path == '/':
            self.send_response(200)
            self.send_header('Content-type', 'text/plain')
            self.end_headers()
            self.wfile.write(b'Hello, this is a simple API!')
        elif self.path == '/data':
            self.send_response(200)
            self.send_header('Content-type', 'application/json')
            self.end_headers()
            json_data = {"name": "John", "age": 30, "city": "New York"}
            json_bytes = json.dumps(json_data).encode("utf-8")
            self.wfile.write(json_bytes)
        elif self.path == '/info':
            self.send_response(200)
            self.send_header('Content-type', 'application/json')
            self.end_headers()
            json_data = {"version": "1.0", "description": "A simple API built with http.server"}
            json_bytes = json.dumps(json_data).encode("utf-8")
            self.wfile.write(json_bytes)
        elif self.path == '/status':
            self.send_response(200)
            self.send_header('Content-type', 'text/plain')
            self.end_headers()
            self.wfile.write(b'OK')
        else :
            self.send_response(404)
            self.send_header('Content-type', 'text/plain')
            self.end_headers()
            self.wfile.write(b'404 Not Found')

def run():
    httpd = None
    PORT = 8000  # Port du serveur
    address = ("", PORT)  # Adresse du serveur + Port (localhost:8000)

    while True:
        try:
            # Créer une instance avec l'adresse et le gestionnaire de requêtes
            httpd = socketserver.TCPServer(address, RequestHandler)
            print("Serving at port", PORT)
            # Commencer à servir les requêtes de manière indéfinie
            httpd.serve_forever()
        except KeyboardInterrupt:  # Gestion de l'interruption clavier (Ctrl+C)
            print("\nServeur close.")
            # Sortir de la boucle pour arrêter le serveur
            break
        except OSError as e:  # Capturer les erreurs OSError (comme le port déjà utilisé)
            print(f"Erreur : {e}. Attente de 10 secondes avant de réessayer...")
            time.sleep(10)
        finally:
            if httpd is not None:
            # Fermer le serveur proprement pour libérer le port
                httpd.server_close()

run()
