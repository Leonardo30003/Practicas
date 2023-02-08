from pymongo import MongoClient

# crear las conexiones para establecer el enlace con mongo

cliente = MongoClient("localhost:27017")
db = cliente.PracticasPreprofecionales

# crear la funcion para guardar los ojetos creados
def updateCarrera():

    try:
        criteria = input ("\n Ingrese los datos para actualizar actualizar \n")

        id = input("Ingrese su id:")
        nombres = input("Ingrese sus nombres correctos:")
        descripcion = input("Ingrese su descripcion")

        db.Carrera.update.one(
           {"id":criteria },
           {
             "$set":{"id" : id,
                 "nombres": nombres,
                 "descripcion" : descripcion,
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
