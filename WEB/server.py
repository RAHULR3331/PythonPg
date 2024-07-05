import http.server
import socketserver
import mysql.connector
import cgi

PORT = 8000

# Database connection
db = mysql.connector.connect(
    host="localhost",
    user="root",  # default XAMPP username
    password="",  # default XAMPP password is empty
    database="test_db"  # replace with your database name
)

class MyHandler(http.server.SimpleHTTPRequestHandler):
    def do_GET(self):
        if self.path == '/':
            self.path = '/form.html'
        return http.server.SimpleHTTPRequestHandler.do_GET(self)
    
    def do_POST(self):
        if self.path == '/submit':
            form = cgi.FieldStorage(
                fp=self.rfile,
                headers=self.headers,
                environ={'REQUEST_METHOD': 'POST'}
            )
            
            name = form.getvalue('name')
            email = form.getvalue('email')
            age = form.getvalue('age')
            
            cursor = db.cursor()
            sql = "INSERT INTO users (name, email, age) VALUES (%s, %s, %s)"
            val = (name, email, age)
            cursor.execute(sql, val)
            db.commit()
            cursor.close()
            
            self.send_response(200)
            self.send_header('Content-type', 'text/html')
            self.end_headers()
            self.wfile.write(b'New record created successfully')
            return
        
        self.send_error(404)
        self.end_headers()

Handler = MyHandler

with socketserver.TCPServer(("", PORT), Handler) as httpd:
    print("serving at port", PORT)
    httpd.serve_forever()
