class Usuario:

    nombre_banco = "Primer Dojo Nacional"	

    def __init__(self, name, correo):
        self.name = name
        self.email = correo
        self.cuenta = CuentaBancaria()


class CuentaBancaria:
    def __init__(self):
        self.balance_cuenta = 0

    def deposito(self, monto):
        self.balance_cuenta += monto
        return self

    def retiro(self,monto):
        if monto > self.balance_cuenta:
            print("SOBREGIRADO, NO SE PUEDE HACER RETIRO")
        else:
            self.balance_cuenta -= monto
        return self
    def balance(self):
        print("Balance: ", self.balance_cuenta)
        return self

    def transfer_dinero(self, cuenta_bancaria, monto):
        self.retiro(monto)
        cuenta_bancaria.deposito(monto)
        return self


pancho = Usuario("Francisco", "jajaja@jajaja.com")
pancho.cuenta.deposito(0).deposito(20).deposito(50).retiro(100).balance()

javier = Usuario("Javier", "jojo@jojojo.com")
javier.cuenta.deposito(50)
javier.cuenta.balance()

javier.cuenta.transfer_dinero(pancho.cuenta, 30)

pancho.cuenta.balance()
javier.cuenta.balance()