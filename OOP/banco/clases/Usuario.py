from .CuentaBancaria import CuentaBancaria

class Usuario:

    nombre_banco = "Primer Dojo Nacional"	

    def __init__(self, name, correo):
        self.name = name
        self.email = correo
        self.cuenta = CuentaBancaria()