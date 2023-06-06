from conectar import *

db = conexion()
coleccion = db.Alumnos


documentos = coleccion.find({"rut":"xxxxxxxx-0"})


for documentos in documentos:
    print (documentos)