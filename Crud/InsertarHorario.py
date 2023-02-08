from pymongo import MongoClient

# crear las conexiones para establecer el enlace con mongo

cliente = MongoClient("localhost:27017")
db = cliente.PracticasPreprofecionales

# crear la funcion para guardar los ojetos creados


def insertarHorario():
    try:
        id = float(input("Ingrese el Id: "))
        fecha = input("Ingrese la fecha: ")
        hora_inicio = input("Ingrese la hora de inicio: ")
        hora_salida= input("Ingrese la hora de salida: ")
        detalle_actividad=input("Detalle la actividad: ")

        db.Horario.insert_one({
            "id": id,
            "fecha": fecha,
            "hora_inicio": hora_inicio,
            "hora_salida":hora_salida,
            "detalle_nacimienti":detalle_actividad
        })
        print("objeto guardado satisfactoriamente")
    except ImportError:
        print("Error de conexion con la base de datos")