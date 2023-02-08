from pymongo import MongoClient

# crear las conexiones para establecer el enlace con mongo

cliente = MongoClient("localhost:27017")
db = cliente.PracticasPreprofecionales

# crear la funcion para guardar los ojetos creados
def updateVisita():
    try:
        criteria = input ("\n Ingrese los datos para actualizar actualizar \n")

        id = input("Ingrese su id:")
        fecha = input("Ingrese la fecha:")
        tutor = input("Ingrese su tutor")
        id_estudiante = input("Ingrese su id de estudiante")
        comentario = input("Ingrese un comentario")
        calificacion = input("Ingrese su calificacion")
       

        db.Visita.update.one(
           {"_id":criteria },
           {
             "$set":{"id" : id,
                 "fecha": fecha,
                 "tutor" : tutor,
                 "id_estudiante" : id_estudiante,
                 "comentario": comentario,
                 "calificacion" : calificacion,
                }
            }
        )

        print("""¡¡¡¡¡¡¡¡¡¡¡¡¡¡¡¡¡¡¡¡¡¡¡¡¡¡¡¡¡¡¡¡¡¡
                Registro actualizado correctamente
                ???????????????????????????????????
             """)

    except ImportError:
     platform_specific_module = None
    print(str(e))
