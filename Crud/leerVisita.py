from pymongo import MongoClient

# crear las conexiones para establecer el enlace con mongo

cliente = MongoClient("localhost:27017")
db = cliente.PracticasPreprofecionales

def consultarVisita():
    try:
        visita=db.Visita.find()
        print("Presentamos los datos obtenidos de la base de datos")
        for visita in visita:
            print(visita)
    except ImportError:
        platform_specific_module= None
        print(str(e))
