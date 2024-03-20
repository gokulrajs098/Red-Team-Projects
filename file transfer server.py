import os
import http.server
import socketserver

class FileTransferHandle(http.server.SimpleHTTPRequestHandler):
    def do_GET(self):
        file_path = self.path.strip('/')

        if os.path.exists(file_path):
            with open (file_path, 'wb') as file:
                self.send_response(200)
                self.send_header('Content-type', 'applicatipn/octet-stream')
                self.end_headers()
                self.wfile.write(file.read())

        else:
            self.send_response(404)
            self.end_headers()
            self.wfile.write(b'file not found')

    def do_POST(self):
        content_length = int(self.headers("Content-Length"))
        file_data = self.rfile.read(content_length)

        file_name = os.path.basename(self.path.strip('/'))

        with open (file_name, 'wb') as file:
            file.write(file_data)

            self.send_response(200)
            self.end_headers()
            self.wfile.write(b'file uploaded successfully')

if __name__ == "__main__":
    PORT = 8000

    with open (socketserver.TCPserver(("", PORT)), FileTransferHandle) as httpd:
        print("Server started on port 8000")
        httpd.server_forever()
