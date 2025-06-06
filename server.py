import http.server
import socketserver
import os
import socket


class MyHandler(http.server.SimpleHTTPRequestHandler):
    def do_GET(self):
        # 获取本机的 hostname
        hostname = socket.gethostname()
        message_parts = [
            "<html>",
            "<head><title>Hello World</title></head>",
            "<body style=\"text-align:center;\">",
            "<h3>Hello World! <br/><br/>Hello Alauda! </h3>",
            f"<p>{hostname}</p>",
            "</body>",
            "<html>"
        ]
        html_content = '\r\n'.join(message_parts)
        # message = "New request arrived from %s:%d" % self.client_address
        self.send_response(200)
        self.send_header("Content-type", "text/html")
        self.end_headers()
        self.wfile.write(html_content.encode('utf-8'))

        # if self.path == "/alauda.jpg":
        # f = open(os.curdir + os.sep + self.path)
        # self.send_response(200)
        # self.send_header('Content-type', 'image/jpg')
        # self.end_headers()
        # self.wfile.write(f.read())
        # f.close()


if __name__ == "__main__":
    PORT = 80
    Handler = MyHandler
    with socketserver.TCPServer(("", PORT), Handler) as httpd:
        print(f"Serving at port {PORT}")
        httpd.serve_forever()
