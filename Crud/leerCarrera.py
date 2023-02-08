from pymongo import MongoClient

# crear las conexiones para establecer el enlace con mongo

cliente = MongoClient("localhost:27017")
db = cliente.PracticasPreprofecionales

def consultarCarrera():
    try:
        carrera=db. Carrera.find()
        print("Presentamos los datos obtenidos de la base de datos")
        for carrera in carrera:
            print(carrera)
    except ImportError:
        platform_specific_module= None
        print(str(e))
