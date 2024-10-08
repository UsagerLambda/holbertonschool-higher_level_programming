import http.server
import socketserver
import json

PORT = 8000


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
            json_data = {"name": "John",
                         "age": 30,
                         "city": "New York"}
            json_bytes = json.dumps(json_data).encode("utf-8")
            self.wfile.write(json_bytes)

        elif self.path == '/info':
            self.send_response(200)
            self.send_header('Content-type', 'application/json')
            self.end_headers()
            json_data = {"version": "1.0",
                         "description": "A simple API built with http.server"}
            json_bytes = json.dumps(json_data).encode("utf-8")
            self.wfile.write(json_bytes)

        elif self.path == '/status':
            self.send_response(200)
            self.send_header('Content-type', 'text/plain')
            self.end_headers()
            self.wfile.write(b'OK')

        else:
            self.send_response(404)
            self.send_header('Content-type', 'text/plain')
            self.end_headers()
            self.wfile.write(b'Endpoint not found')


with socketserver.TCPServer(("", PORT), RequestHandler) as httpd:
    try:
        print(f"Server on port : {PORT}")
        httpd.serve_forever()
    except KeyboardInterrupt:
        httpd.shutdown()
        httpd.server_close
        print("\nServer stopped.")
