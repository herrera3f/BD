from conectar import *
db = conexion.universidad
coleccion = db.Alumnos
filtro= {"rut":"xxxxxxxx-0"}
update = {"$set":{"edad":"44"}}

try:
    modificar = coleccion.update_one(filtro,update)
    print("el documento se modifico ")
    documentos = coleccion.find({"rut":"323342342"})
    for documentos in documentos:
        print(documentos)
except Exception as e:
    print(e)