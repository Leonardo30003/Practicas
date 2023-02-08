from pymongo import MongoClient

# crear las conexiones para establecer el enlace con mongo

cliente = MongoClient("localhost:27017")
db = cliente.PracticasPreprofecionales

# crear la funcion para guardar los ojetos creados


def insertarCarrera():
    try:
        id = float(input("Ingrese el Id: "))
        nombre = input("Ingrese el nombre: ")
        descripcion = input("Ingrese una descripcion: ")

        db.Carrera.insert_one({
            "id": id,
            "marca": nombre,
            "precio": descripcion,
        })
        print("objeto guardado satisfactoriamente")
    except ImportError:
        print("Error de conexion con la base de datos")