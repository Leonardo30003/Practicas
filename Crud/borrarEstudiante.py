from pymongo import MongoClient

# crear las conexiones para establecer el enlace con mongo

cliente = MongoClient("localhost:27017")
db = cliente.PracticasPreprofecionales

def deleteEstudiante():
    try:
    
        criterio = input("\n Ingresa el id del registro a eliminar \n ")
        db.Estudiante.delete_many(
            {'id':float(criterio)}
        )
        print("Registro",criterio,"Eliminado correctamente")
        print(f"Registro{criterio} Eliminado correctamente")

    except ImportError:
         platform_specific_module = None
         print(str(e))