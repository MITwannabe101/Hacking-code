from http.server import HTTPServer, BaseHTTPRequestHandler
from io import BytesIO

class HTTPRequestHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        self.send_response(200)
        self.end_headers()
        self.wfile.write(b'<!DOCTYPE html><html><h3>This is a webpage i am making<hr> \
        <img src="https://theartsdevelopmentcompany.org.uk/wp-content/uploads/2019/02/Website-Building-Landscape-1280x640.jpg" style="size : 10%"></h3></html>')

httpd = HTTPServer(('', 8001), HTTPRequestHandler)
httpd.serve_forever()
