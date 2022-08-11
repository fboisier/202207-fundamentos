class Motor:
    def __init__(self, año):
        self.motor = ''
        self.año = año
        self.cilidranda = ''


class Auto:
    def __init__(self, marca, color, año, modelo):
        self.motor = Motor(año)
        self.marca = marca
        self.color = color
        self.tipo_combustible = 'Bencinero'
        self.modelo = modelo
        self.kilometraje = 0

    @classmethod
    def nombreClase(cls):
        return "AUTO"

    def avanza(self, kilometros):
        self.kilometraje += kilometros

    def es0Kilometro(self):
        return self.kilometraje == 0

    @staticmethod
    def validaKilometro(kilometros):
        return str(kilometros).isdigit()


ojAuto1 = Auto("Suzuki", 'Gris', 2019, "Baleno")
print(ojAuto1.nombreClase())

print(ojAuto1.__dict__)
ojAuto1.avanza(100)
print(ojAuto1.__dict__)
print(ojAuto1.es0Kilometro())

print(ojAuto1.validaKilometro("199"))

print(Auto.nombreClase())

print(ojAuto1.motor.año)