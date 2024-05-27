import BaseHTTPServer

HOST = "localhost"
PORT = 8000

class MyHTTPHandler(BaseHTTPServer.BaseHTTPRequestHandler):
    def do_GET(self):
        
        self.send_response(200)
        
        self.send_header("Content-type", "text/html")
        self.end_headers()

        
        self.wfile.write("<html><head><title>Our Web Title</title></head>")
        self.wfile.write("<body><p>This is our body. You wanted to visit <b>%s</b> page</p></body>" % self.path)
        self.wfile.write("</html>")

if __name__ == '__main__':
    server = BaseHTTPServer.HTTPServer((HOST, PORT), MyHTTPHandler)
    try:
        server.serve_forever()
    except KeyboardInterrupt:
        print('Exiting...')
        server.server_close()
