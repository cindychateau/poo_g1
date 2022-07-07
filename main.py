from Persona import Persona
from Estudiante import Estudiante

elena = Persona("Elena", "De Troya", 33) #EJECUTA INIT

juana = Persona("Juana", "De Arco", 20)

pablo = Persona("Pablo", "Picasso", 55)

pedro = Estudiante("Pedro", "Perez", 17, 1, "Fundamentos de la Web")

elena.cumpleanios()

juana.codificar(50)

elena.codificar(10)

juana.codificar(25)

print("----------")
pedro.codificar(150)
print(Persona.total_lineas_codigo)
pedro.informacion()

#elena.puede_descansar()
pedro.puede_descansar()

juana.nombre = "Juanita"

Persona.cambiar_pais("México")

print(juana.nombre)
print(elena.pais)

Persona.imprimePersonas()



