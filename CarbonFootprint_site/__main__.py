from carbon import app
from waitress import serve

serve(app, host="localhost", port=5000)
