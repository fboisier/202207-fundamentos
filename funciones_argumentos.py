def fabricaZapatos(tela="Gamuza", color="Negro"):
    zapato = f" El zapato de tela: {tela} y color: {color}, esta listo."
    return zapato


print(fabricaZapatos(color="Rojo"))

# establece los valores predeterminados al declarar los parámetros
def sé_alegre(name='', repeat=2):
	print(f"buenos días {name}\n" * repeat)
sé_alegre()    # salida: buenos días (repetida en dos líneas)
sé_alegre("tim")    # salida: buenos días tim (repetida en dos líneas)
sé_alegre(name="john")    # salida: buenos días john (repetida en dos líneas)
sé_alegre(repeat=6)    # salida: buenos días (repetida en 6 líneas)
sé_alegre(name="michael", repeat=5)    # salida: buenos días michael (repetida en 5 líneas)
# NOTA: el nombre de los argumentos no importa si somos explícitos al enviarlos
sé_alegre(repeat=3, name="kb")    # salida: buenos días kb (repetida en 3 líneas)