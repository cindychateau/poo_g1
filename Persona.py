class Persona:

    pais = "Colombia"
    total_lineas_codigo = 0
    listaPersonas = []

    #A traves de init INICIALIZAMOS nuestra instancia. 
    def __init__(self, nombre="John", apellido="Doe", edad=18): #SELF nos incluye toda la información del objeto individual
        #nombre = "Elena"; apellido = "De Troya"; edad = 33
        #self = pablo
        self.nombre = nombre #elena.nombre = "Elena"
        self.apellido = apellido #elena.apellido = "De Troya"
        self.edad = edad
        self.lineas_codigo = 0
        Persona.listaPersonas.append(self)

    def informacion(self):
        print("Nombre:"+self.nombre+" Apellido:"+self.apellido)
    
    def cumpleanios(self):
        self.edad += 1
        if(Persona.mayoria_edad(self.edad)):
            print("Wuju! Ya eres mayor de edad")
        else:
            print(":(")
        

    def codificar(self, cantidad_lineas):
        self.lineas_codigo += cantidad_lineas
        Persona.total_lineas_codigo += cantidad_lineas
        if Persona.es_experto(self.lineas_codigo):
            print("Expertísimo programador")
        else:
            print("Sigamos practicando!")

    @classmethod
    def cambiar_pais(cls, nuevo_pais):
        cls.pais = nuevo_pais

    @classmethod
    def imprimePersonas(cls):
        for persona in cls.listaPersonas:
            #persona = elena; #persona = juana; #persona = pablo
            persona.informacion()

    @staticmethod
    def mayoria_edad(edad):
        if edad > 18:
            return True
        else :
            return False

    @staticmethod
    def es_experto(lineas):
        if lineas > 50:
            return True
        else:
            return False

    #Polimorfismo: nos permite especificar funciones en un nivel "abstracto", lo implementamos en Clases Particulares. Y clases particulares PUEDEN tener distintos comportamientos
    def que_haces(self):
        raise NotImplementedError #No me va a marcar error por estar vacía
