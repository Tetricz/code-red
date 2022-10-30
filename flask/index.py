from flask import Flask
from flask import send_from_directory
from flask import send_file

app = Flask(__name__)

@app.route('/')
def index():
    return send_file('../html/index.html')



@app.route("/<path:name>")
def download_file(name):
    return send_from_directory('../html', name)
