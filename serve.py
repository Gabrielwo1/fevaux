import http.server, socketserver, os
os.chdir("/Users/syntax/Downloads/feeva")
PORT = 3000
Handler = http.server.SimpleHTTPRequestHandler
with socketserver.TCPServer(("", PORT), Handler) as httpd:
    httpd.serve_forever()
