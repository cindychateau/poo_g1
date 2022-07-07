from Persona import Persona

class Estudiante(Persona):

    def __init__(self, nombre, apellido, edad, id, curso):
        super().__init__(nombre, apellido, edad)
        self.id = id
        self.curso = curso

    def puede_descansar(self):
        if(self.lineas_codigo > 50):
            print("Puede descansar")
        else:
            print("Sigue trabajando, falta poco!")
    
    #Anulacion o Sobre escritura
    def informacion(self):
        super().informacion()
        print("Curso:"+self.curso)
        #print("Nombre:"+self.nombre+" Apellido:"+self.apellido+" Curso:"+self.curso)

    def que_haces(self):
        print("Estoy estudiando en Coding Dojo y aprendiendo muchísimo")

    