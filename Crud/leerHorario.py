from pymongo import MongoClient

# crear las conexiones para establecer el enlace con mongo

cliente = MongoClient("localhost:27017")
db = cliente.PracticasPreprofecionales

def consultarHorario():
    try:
        horario=db.Horario.find()
        print("Presentamos los datos obtenidos de la base de datos")
        for horario in horario:
            print(horario)
    except ImportError:
        platform_specific_module= None
        print(str(e))       
