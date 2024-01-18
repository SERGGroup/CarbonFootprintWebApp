from wsgi import curr_app
import waitress
import socket

hostname = socket.gethostname()
IPAddr = socket.gethostbyname(hostname)
#waitress.serve(curr_app, host=IPAddr, port=5000, url_scheme='http')
waitress.serve(curr_app, host='127.0.0.1', port=5001, url_scheme='http')
