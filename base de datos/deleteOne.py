from conectar import *
db = conexion()
coleccion = db.Alumnos
filtro= {"rut":"xxxxxxxx-0"}


try:
    modificar = coleccion.delete_one(filtro)
    print("el documento se modifico ")
    documentos = coleccion.find({"rut":"xxxxxxxx-0"})
    for documentos in documentos:
        print(documentos)
except Exception as e:
    print(e)
