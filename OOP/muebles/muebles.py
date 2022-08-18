from clases import Silla, Mesa, saludar

objeto_silla1 = Silla()
objeto_silla1.color = "ROJA"
print(objeto_silla1.color)
print(objeto_silla1.tiene_respaldo)
objeto_silla1.limpiar()


objeto_mesa1 = Mesa()
objeto_mesa1.color = "NEGRO"
print(objeto_mesa1.color)
print(objeto_mesa1.cantidad_puestos)
objeto_mesa1.limpiar()

saludar()