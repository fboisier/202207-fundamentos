from clases import Usuario

pancho = Usuario("Francisco", "jajaja@jajaja.com")
pancho.cuenta.deposito(0).deposito(20).deposito(50).retiro(100).balance()

javier = Usuario("Javier", "jojo@jojojo.com")
javier.cuenta.deposito(50)
javier.cuenta.balance()

javier.cuenta.transfer_dinero(pancho.cuenta, 30)

pancho.cuenta.balance()
javier.cuenta.balance()