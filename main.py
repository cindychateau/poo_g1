from Persona import Persona

elena = Persona("Elena", "De Troya", 33)

juana = Persona("Juana", "De Arco", 20)

elena.cumpleanios()

juana.codificar(50)

elena.codificar(10)

juana.codificar(25)

juana.nombre = "Juanita"

Persona.cambiar_pais("México")

print(juana.nombre)
print(elena.pais)