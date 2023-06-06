from conectar import *

db = conexion.universidad
coleccion = db.Alumnos



rut= input("Ingrese el rut del alumno: ")
nombreAlumno= input("Ingrese el nombre del alumno: ")
apellidoAlumno= input("Ingrese el apellido del alumno: ")
correo= input("Ingrese el correo del alumno: ")
nota1= input("Ingrese la nota 1 del alumno: ")
nota2= input("Ingrese la nota 2 del alumno: ")
nota3= input("Ingrese la nota 3 del alumno: ")

# se crea un diccionario para insertar los datos
datos = {
    "rut": rut,
    "nombreAlumno": nombreAlumno,
    "apellidoAlumno": apellidoAlumno,
    "correo": correo,
    "nota1": nota1,
    "nota2": nota2,
    "nota3": nota3
}

# se inserta el diccionario en la coleccion
coleccion.insert_one(datos)

# se muestra el documento insertado
print(coleccion.find_one({"rut": rut}))
