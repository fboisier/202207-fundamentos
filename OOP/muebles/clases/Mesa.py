from .Mueble import Mueble

class Mesa(Mueble):
    def __init__(self):
        super().__init__('', 4, '', '')
        self.cantidad_puestos = 4
