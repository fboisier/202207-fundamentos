animales = []

while(True):
    print("Escoja una opcion:\n1: SALIR\n2: MOSTRAR\n3: AGREGAR")
    resultado = input("ESCRIBA UNA OPCION:")
    if resultado == "1":
        break
    elif resultado == "2":
        print(animales)
    else:
        animal = input("ESCRIBA EL ANIMAL A AGREGAR:")
        animales.append(animal)

