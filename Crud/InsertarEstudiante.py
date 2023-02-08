from pymongo import MongoClient

# crear las conexiones para establecer el enlace con mongo

cliente = MongoClient("localhost:27017")
db = cliente.PracticasPreprofecionales

# crear la funcion para guardar los ojetos creados


def insertarEstudiante():
    try:
        id = float(input("Ingrese el Id: "))
        nombre = input("Ingrese el nombre: ")
        apellidos = input("Ingrese la apellidos: ")
        cedula= input("Ingrese el numero de cedula: ")
        correo_institucional=input("Ingrese el correo instutucional: ")
        direccion=input("Ingrese una dirreccion: ")
        telefono=input("Ingrese un telefono: ")
        fecha_nacimiento= input("Ingrese su fecha de nacimiento: ")

        db.Estudiante.insert_one({
            "id": id,
            "marca": nombre,
            "precio": apellidos,
            "telefono":cedula,
            "correoElectronico":correo_institucional,
            "direccion":direccion,
            "fecha_nacimeinto":fecha_nacimiento
        })
        print("objeto guardado satisfactoriamente")
    except ImportError:
        print("Error de conexion con la base de datos")