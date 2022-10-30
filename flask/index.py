from flask import Flask
from flask import send_from_directory
from flask import send_file
from flask import render_template
import database_coms as database

app = Flask(__name__, template_folder='../html')



@app.route('/')
def index():
    return send_file('../html/index.html')

@app.route('/maps.js')
def maps():
    return render_template('maps.js', helloworld="console.log(\'Hello\')")

@app.route('/findRovers.html')
def findRovers():
    db = database.DatabaseComs()
    co=db.getRover("3")
    db.close()
    return render_template('findRovers.html', coords=str(co[0][0]) + ", " + str(co[0][1]), battery=str(co[0][2]))

@app.route("/<path:name>")
def html(name):
    return send_from_directory('../html/', name)


# 98.00  *   x
# 100.00   500.0