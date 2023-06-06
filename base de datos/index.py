from flask import *
from conectar import *


app = Flask(__name__)

@app.route("/")
#inicializa el home


def home():
    db = conexion()
    coleccion = db.Alumnos
    documentos = coleccion.find()

    return render_template('index.html',db=documentos)

if __name__ == '__main__':
    app.run(debug=True)