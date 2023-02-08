from pymongo import MongoClient

# crear las conexiones para establecer el enlace con mongo

cliente = MongoClient("localhost:27017")
db = cliente.PracticasPreprofecionales

# crear la funcion para guardar los ojetos creados


def insertarEmpresa():
    try:
        id = float(input("Ingrese el Id: "))
        nombre = input("Ingrese el nombre: ")
        direccion = input("Ingrese la direccion: ")
        telefono= input("Ingrese el numero de telefono: ")
        correoElectronico=input("Ingrese el correo electronico: ")

        db.Empresa.insert_one({
            "id": id,
            "marca": nombre,
            "precio": direccion,
            "telefono":telefono,
            "correoElectronico":correoElectronico
        })
        print("objeto guardado satisfactoriamente")
    except ImportError:
        print("Error de conexion con la base de datos")