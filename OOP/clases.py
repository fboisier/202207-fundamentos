class Perro:
    def __init__(self, nombre="Sin Nombre"):
        self.raza = ''
        self.color = ''
        self.nombre = nombre
        self.sexo = ''
        self.tamaño = 'Normal'
        self.patas = 4
        self.edad = 0
        self.estomago = 0

    def comer(self, comida=10):
        self.estomago += comida
        print(f"{self.nombre} esta comiendo!!")

    def dormir(self):
        self.estomago = 0
        print("El perro esta durmiendo")


cachupin = Perro("Cachupin")
print(cachupin.tamaño)
cachupin.comer(50)

firulay = Perro("Firulay")
firulay.tamaño = "Chico"
print(firulay.tamaño)

firulay.comer(100)


print(cachupin.estomago)
print(firulay.estomago)

firulay.dormir()








