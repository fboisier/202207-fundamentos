class Persona:
    def pagar_cuenta(self):
        raise NotImplementedError
# Millonario hereda de Persona
class Millonario(Persona):
    def pagar_cuenta(self):
        print("Aquí tienes. Quédate con el cambio.")
# Estudiante de posgrado también hereda de la clase Persona
class EstudiantePosgrado(Persona):
    def pagar_cuenta(self):
        print("¿Puedo deberle diez dólares o lavar los platos?")


lista_personas = []

for indice in range(20):
    if indice < 10:
        lista_personas.append(Millonario())
    else:
        lista_personas.append(EstudiantePosgrado())

print(lista_personas)


for persona in lista_personas:
    persona.pagar_cuenta()