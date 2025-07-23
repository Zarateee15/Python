import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from controllers.alumno_controller import AlumnoController
from models.alumno import Alumno


class TestAlumno:
    def __init__(self):
        self.ac = AlumnoController()
    
    def main(self):
        while True:
            os.system("cls")
            print("-------- Menu --------")
            print(f"1) Cargar Alumno")
            print(f"2) Ver Alumno")
            print(f"3) Actualizar Alumno")
            print(f"4) Borrar Alumno")
            print(f"5) Ver todo")
            print(f"0) Salir")

            resp = input("Opción: ")
            if resp == "1":
                nombre = input("Nombre: ")
                email = input ("Email: ")
                matricula = input ("Matricula: ")

                self.ac.save(Alumno(nombre,email,matricula))
            
            elif resp == "5":
                for alu in self.ac.getAll():
                    print(alu.getInformacion())

                input ("Presione ENTER para continuar....")
            
            elif resp == "0":
                print("Saliendo...")
                break

if __name__ == "__main__":
    vista = TestAlumno()
    vista.main()