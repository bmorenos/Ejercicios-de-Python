# EJERCICIO NUMERO 1: INGRESAR 2 DATOS Y SACAR EL PRODUCTO MEDIANTE SUMA
def producto():
    print("***** Sacar producto de dos numeros mediante sumas *****")
    print("")
    n1 = int(input("Introduce el primer numero: "))
    n2 = int(input("Introduce el primer numero: "))
    producto = 0

    for i in range(n1):
        producto = producto + n2

    print("El resultado es: " + str(producto))
    print("Fin del ejercicio")
    print("")

producto()


# EJERCICIO NUMERO 2: MULTIPLICAR CANTIDAD DE DATOS INDEFINIDOS Y SALIR DEL PROGRAMA AL PRESIONAR F (EN ESTE CASO SE SALE PRESIONANDO "1")
def secuencia():
    print("**** Multiplicar todos lo numeros que se vayan ingresando, se sale presionando 1 ****")
    print("")
    num1=0
    total = 1
    while num1 != 1:
        num1 = int(input("Introduzca un numero: "))
        total = total * num1

    print("El resultado es: " + str(total))
    print("")

secuencia()


# EJERCICIO NUMERO 3: ENCONTRAR EL NUMERO MAYOR DE LOS DATOS INGRESADOS
def numMayor():
        print("**** Encontrar el Numero mayor de los datos ingresados ****")
        print("")
        lista = []
        cantidad = int(input("Cuantos datos quiere ingresar: "))
        mayor = 0
        i = 1
        while (i <= cantidad):
            numero = int(input("Numero " + str(i) + ":"))
            lista.append(numero)
            i = i + 1

        mayor = max(lista)

        print("Los datos ingresados fueron: ", lista)
        print("Y el numero mayor es: ", mayor)
        print("")


numMayor()

# EJERCICIO NUMERO 4: NUMEROS DE LA SERIE DE FIBONACHI
def fibonacci():
    print("**** Elegir la cantidad de datos de la Serie de Fibonachi que deseo Ver ****")
    print("")
    contador=0
    a=0
    b=1
    c=0
    N= int(input("Ingrese la cantidad de datos de la serie que desea ver: "))

    while contador < N:
        a=b
        b=c
        c=a+b
        print(c)
        print("")
        contador=contador+1

fibonacci()



# EJERCICIO NUMERO 5: SUMAR SOLO LOS NUMEROS PARES.
def sumapares():
    print("**** Sumar solo los numeros pares de todos los ingresados ****")
    print("")
    nu1 = 0
    cont = 0
    total = 0
    while cont < 30:
        nu1 = float(input("Ingrese un numero: "))
        cont = cont + 1
        if nu1 % 2 == 0:
            total = total + nu1
        else:
            total = total
    print("La suma de los pares es: " + str(total))
    print("")


sumapares()


# EJERICIO 6: FACTORIAL DE UN NUMERO
def factorial(x, n):
    if (n > 0):
        x = factorial(x, n - 1)
        x = x * n
    else:
        x = 1
    return x

print("**** Encontrar el factorial de un Numero ****")
print("")
n = int(input("Ingrese un numero: "))
x = 1
x = factorial(x, n)
print("El factorial de ", n, "es: " + str(x))
print("")

factorial(x, n)

# EJERCICIO NUMERO 7: SUMA DE SOLO LOS NUMEROS PRIMOS
# -*- coding: UTF-8 -*-
def primo(num):

        cont = 0
        for i in range(1, num):
                if (num % i == 0):
                        cont += 1
                        if cont > 1:
                                return False
        return True


suma = 0

print("**** Sumar solo los numeros primos de todos los ingresados ****")
print("")
for i in range(30):

                i=int(input("Ingrese un numero: "))

                if primo(i):
                        print("es primo")
                        suma=suma+i
                else:
                        suma=suma


print("La suma de los primos es:", str(suma))



