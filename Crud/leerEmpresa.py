from pymongo import MongoClient

# crear las conexiones para establecer el enlace con mongo

cliente = MongoClient("localhost:27017")
db = cliente.PracticasPreprofecionales

def consultarEmpresa():
    try:
        empresa=db.Empresa.find()
        print("Presentamos los datos obtenidos de la base de datos")
        for empresa in empresa:
            print(empresa)
    except ImportError:
        platform_specific_module= None
        print(str(e))
