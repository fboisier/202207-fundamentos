if __name__ == "__main__":
    from Mueble import Mueble
else:
    from .Mueble import Mueble

class Silla(Mueble):
    def __init__(self):
        super().__init__('', 4, '', '')
        self.tiene_respaldo = True

    def limpiar(self):
        super().limpiar()
        print("la silla se esta limpiando con articulo de silla para limpiar")


def saludar():
    print("HOLA")


if __name__ == '__main__':
    print("ESTOY EN LA SILLA")


