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