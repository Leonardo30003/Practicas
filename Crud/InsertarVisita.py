from pymongo import MongoClient

# crear las conexiones para establecer el enlace con mongo

cliente = MongoClient("localhost:27017")
db = cliente.PracticasPreprofecionales

# crear la funcion para guardar los ojetos creados


def insertarVisita():
    try:
        id = float(input("Ingrese el Id: "))
        fecha = input("Ingrese la fecha: ")
        tutor = input("Ingrese el nombre del tutor: ")
        id_estudiante= input("Ingrese id del estudinate: ")
        comentario=input("Agrege un comentario: ")
        calificacion=input("Ingrese la calificacio: ")

        db.Visita.insert_one({
            "id": id,
            "fecha": fecha,
            "tutor": tutor,
            "id_estudiante":id_estudiante,
            "comentario":comentario,
            "calificacion":calificacion
        })
        print("objeto guardado satisfactoriamente")
    except ImportError:
        print("Error de conexion con la base de datos")