

def saludar(nombre):
    print("HOLA", nombre)
    return "Hola" + nombre

resultado = saludar("FRANCISCO")
print(resultado)


def fabricaZapatos(tela, color):
    # programacion que crea el zapato.
    zapato = f" El zapato de tela: {tela} y color: {color}, está listo."
    return zapato


zapato1 = fabricaZapatos("Gamuza", "Negro")
zapato2 = fabricaZapatos("Polar", "Rojo")

print(zapato1, zapato2)


def multiplicar(valorA, valorB):
    return valorA * valorB

resultadoC = multiplicar(5,4)
print(resultadoC)