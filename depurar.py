
# SOLUCION A
def multiplicar(num_list, num):
    print("Entrando a la funcion multiplicar")
    print("num_list",num_list)
    print("num",num)

    salida = []

    for x in num_list:
        print("la variable antes X:", x)
        x *= num
        salida.append(x)
        print("la variable despues X:", x)
    
    print("EL RETORNO ES:", salida)
    return salida

a = [2,4,10,16]
b = multiplicar(a,5)
print(a)
print(b)


# SOLUCIONA B
def multiplicar(num_list, num):
    print("Entrando a la funcion multiplicar")
    print("num_list",num_list)
    print("num",num)

    for x in range(len(num_list)):
        print("la variable antes X:", x)
        num_list[x] = num_list[x] *  num
    
    print("EL RETORNO ES:", num_list)
    return num_list

a = [2,4,10,16]
b = multiplicar(a,5)
print(a)
print(b)



def suma(num1_list, num2):
    num1_list[0] = num1_list[0] + num2

mnilista = [1] # mnilista ----> #81u8u1hjwhjbe
suma(mnilista,2)
print(mnilista)