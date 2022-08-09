
# imprimir en consola textos
from curses.ascii import isdigit
from typing import Dict


print("HOLA MUNDO1")

print("HOLA MUNDO2")

print("HOLA MUNDO3")


# ejemplo de identación
x = 2

if x >= 2:
    print("ES MAYOR O IGUAL A 2")
    print("ALGO")
else:
    pass


# uso de boleanos True o False
esValido = True

if esValido:
    print("ES VALIDO")


# Numero en python
edad = 34
valorDolar = 956.45

print("LA EDAD ES:", edad, " y el valor dolar es", valorDolar)


# Texto 
nombre = "FRANCISCO"
apellido = 'Boisier'

nombre_completo = f'el nombre completo es: {nombre} - {apellido}'
print(nombre_completo)

# Listas es un arreglo

animales = ['perro', 'gato']
print(animales[0])

animales.append('tigre')
print(animales)



# Tupla es un arreglo

animales = ('perro', 'gato')
print(animales[0])

# animales.append('tigre') # esto da error
print(animales)
print(len(animales))

# Diccionarios (son como los objetos de js)
# key -- value

usuario = {
    'nombre': 'Francisco',
    'apellido': 'Boisier',
    'edad': 37
}

print(usuario)
print(usuario['edad'])

usuario['edad'] = 40
print(usuario)

print(edad)
print(type(edad))
print(type(usuario))

if type(usuario) == dict:
    print(f'el tipo de dato de usuario es un diccionario')


# conversion

numero = 4
print(type(numero))

decimal = float(numero)
print(type(decimal))

import random
rand_num = random.randint(2,5)
print(rand_num)


# interpolacion
first_name = "Zen"
last_name = "Coder"
age = 27
titulo = f"Mi nombre is {first_name} {last_name} and tengo {age} años de edad."

print(titulo.title())
print(titulo.lower())
print(titulo.upper())


autos = "toyota-suzuki-mazda-ford"
resultado = autos.split('-')
print(type(resultado))
print(resultado)

texto = "26"
if texto.isdigit():
    print("ES UN NUMERO")



# listas

x = [99,4,2,5,-3]
print(x[:])
# la salida sería [99,4,2,5,-3]
print(x[1:])
# la salida sería [4,2,5,-3];
print(x[:4])
# la salida sería [99,4,2,5]
print(x[2:4])
# la salida sería [2,5];
print(x[::-1])

marcas = {
    'bedidas' : {
        'c1': 'coca-cola',
        'p1': 'pepsi'
    },
    'autos' : {
        'a1': 'toyota',
        'l1': 'mazda'
    }
}

print(marcas)
print(marcas["autos"])
print(marcas["autos"]["a1"])

print(marcas.get("camisas", "ESTO NO EXISTE"))

if "autos" in marcas:
    print("LA TIENE")
else:
    print("NO LA TIENE")


# condicionales

x = 10

if (x != 1):
    if (x == 10):
        print("EXITO!!!")

if (x != 1) and (x == 10): # solo es verdadero si todas las condiciones son True
    print("EXITO!!!")

if (x!= 1) or (x == 10): # si al menos una condicion es verdadera se entra.
    print("EXITO!!!")

if not x != 10:
    print("ENTRO PORQUE NOT invierte el BOLEANO")


# bucles

# for x in range(inicio, final, incremento)
for x in range(2, 10, 3):
    print(x)

# for x in range(inicio, final, 1)
for x in range(2, 10):
    print(x)

# for x in range(0, final, 1)
for x in range(2):
    print(x)


autos = ['toyota', 'mazda']

for auto in autos:
    print(auto)

texto = "Esto es un texto"

for caracter in texto:
    print(caracter)


marcas = {
    'bedidas' : {
        'c1': 'coca-cola',
        'p1': 'pepsi'
    },
    'autos' : {
        'a1': 'toyota',
        'l1': 'mazda'
    }
}

for marca in marcas:
    print(marca)
    print(marcas[marca])

    for llave in marcas[marca]:
        print(llave)
        print(marcas[marca][llave])

for llave, valor in marcas.items():
    print(f"la llave es: {llave} y tiene como valor {valor}")

for llave in marcas.keys():
    print(llave)

for valor in marcas.values():
    print(valor)

print("*"*20)

for indice, dato in enumerate(marcas):
    print(indice, dato)


