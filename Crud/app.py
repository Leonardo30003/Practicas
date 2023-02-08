# Llamar a los archivos creados y sus metodos
import InsertarCarrera
import InsertarEmpresa
import InsertarEstudiante
import InsertarHorario
import InsertarVisita
import actualizar_carrera
import actualizarEmpresa
import actualizarEstudiante
import actualizarHorario
import actualizarVisita
import borrarCarrera
import borraEmpresa
import borrarEstudiante
import borrarHorario
import borrarVisita
import leerCarrera
import leerEmpresa
import leerEstudiante
import leerHorario
import leerVisita
# crear la clase que permita llamar a todos lo metodos que se van a relacional con MongoDB


class Programa:
    def __init__(self):
        self.datoCarrera = 1
        self.datoEstudiante=2
        self.datoHorario=3
        self.datoVisita=4
        self.datoEmpresa=5

    def menu(self):
        while self.dato:
            seleccion = input("""
                        seleccione: 
                        1.Carrera
                        2.Estudiante
                        3.Horario
                        4.Visita
                        5.Empresa
                        """)
            if seleccion == "1":
                # llamar la seleccion insertar
                # print("Insertar")
                def menuCarrera(self):
                    while self.datoCarrera:
                        seleccionar = input("""
                        seleccione: 
                        1. Insertar
                        2. Actualizar
                        3.leer
                        4.Borrar
                        """)
                        if seleccionar == 1:
                            InsertarCarrera.insertarCarrera()

                        elif seleccionar == 2:
                            actualizar_carrera.updateCarrera

                        elif seleccionar == 3:
                            leerCarrera.consultarCarrera
                        elif seleccionar == 4:
                            borrarCarrera.deleteCarerra()

                        else:
                            print("error")
            elif seleccion == "2":
                # Llamar a la opcion actualizar
                # print("Actualizar")
                def menuEstudiante(self):
                    while self.datoEstudiante:
                        seleccionar = input("""
                        seleccione: 
                        1. Insertar
                        2. Actualizar
                        3.leer
                        4.Borrar
                        """)
                        if seleccionar == 1:
                            InsertarEstudiante.insertarEstudiante()
                        elif seleccionar == 2:
                            actualizarEstudiante.updateEstudiante()
                        elif seleccionar == 3:
                            leerEstudiante.consultarEstudiantes
                        elif seleccionar == 4:
                            borrarEstudiante.deleteEstudiante()
                        else:
                            print("error")
            elif seleccion == "3":
                def menuHorario(self):
                    while self.datoHorario:
                        seleccionar = input("""
                        seleccione: 
                        1. Insertar
                        2. Actualizar
                        3.leer
                        4.Borrar
                        """)
                        if seleccionar == 1:
                            InsertarHorario.insertarHorario()
                        elif seleccionar == 2:
                            actualizarHorario.updateHorario
                        elif seleccionar == 3:
                            leerHorario.consultarHorario
                        elif seleccionar == 4:
                            borrarHorario.deleteHorario
                        else:
                            print("error")

            elif seleccion == "4":
                def menuVisita(self):
                    while self.datoVisita:
                        seleccionar = input("""
                        seleccione: 
                        1. Insertar
                        2. Actualizar
                        3.leer
                        4.Borrar
                        """)
                        if seleccionar == 1:
                            InsertarVisita.insertarVisita()
                        elif seleccionar == 2:
                            actualizarVisita.updateVisita()
                        elif seleccionar == 3:
                            leerVisita.consultarVisita
                        elif seleccionar == 4:
                            borrarVisita.deleteVisita()

                        else:
                            print("error")
            elif seleccion == "5":
                # print("Borrar")
                def menuEmpresa(self):
                    while self.datoEmpresa:
                        seleccionar = input("""
                        seleccione: 
                        1. Insertar
                        2. Actualizar
                        3.leer
                        4.Borrar
                        """)
                        if seleccionar == 1:
                            InsertarEmpresa.insertarEmpresa()
                        elif seleccionar == 2:
                            actualizarEmpresa.updateEmpresa()
                        elif seleccionar == 3:
                            leerEmpresa.consultarEmpresa
                        elif seleccionar == 4:
                            borraEmpresa.deleteEmpresa()
                        else:
                            print("error")
            else:
                print("Error")


mongo = Programa()
mongo.menu()
mongo.menuCarrera()
mongo.menuEstudiante()
mongo.menuHorario()
mongo.menuEmpresa()
mongo.menuVisita()
