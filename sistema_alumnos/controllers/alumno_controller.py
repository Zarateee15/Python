####### Dev Jorge Zárate
# CRUD: Create, Read, Update, Delete

class AlumnoController:
    alumnos = None  # Lista que contendrá los alumnos

    def __init__(self): # Constructor
        self.alumnos = []

    def save (self,alumno): # Guardar un alumno
        self.alumnos.append(alumno)

    def getAll (self):  # Ver todos los alumnos
        return self.alumnos
    
    def getAlumno (self, indice):   # Ver un alumno especifico
        # validar indice
        return self.alumnos[indice]

    def update(self, alumno, indice):   # Cambiar dato de un alumno
        self.alumnos[indice] = alumno

    def delete(self,indice):
        alumno = self.alumnos[indice]
        self.alumnos.remove(alumno)