from math import factorial

def parinpar():
    print("**** Ingrese dos numeros ****")
    print("")
    nu1 = 0

    nu1 = int(input("Ingrese un numero: "))
    if nu1 % 2 == 0:
        print("El numero " +str(nu1)+" es par.")
    else:
        print("El numero " +str(nu1)+" no es par.")
#parinpar()

def producdos():
    print("Ingrese dos numeros")
    print("")
    producto=0
    n1 = float(input("Ingrese el primer dato: "))
    n2 = float(input("Ingrese el segundo dato: "))
    producto = n1*n2
    print("El producto de los numeros es: " +str(producto))

#producdos()

def mayordos():
    print("Ingrese dos numeros para determinar cual es mayor")
    print("")
    n1 = float(input("Ingrese el primer dato: "))
    n2 = float(input("Ingrese el segundo dato: "))
    if n1>n2:
        print(str(n1) + " es el numero mayor")
    else:
        print(str(n2) + " es el numero mayor")
#mayordos()

def mayortres():
    print("Ingrese 3 numeros para determinar cual es mayor")
    print("")
    n1 = float(input("Ingrese el primer dato: "))
    n2 = float(input("Ingrese el segundo dato: "))
    n3 = float(input("Ingrese el segundo dato: "))
    if n1>n2 and n1>n3:
        print(str(n1) + " es el numero mayor")
    if n2>n1 and n2>n3:
        print(str(n2) + " es el numero mayor")
    if n3>n1 and n3>n2:
        print(str(n3) + " es el numero mayor")
#mayortres()

def tablamult():
    print("Generar tabla de multiplicar a partir de un Numero")
    print("")
    x= int(input("Ingrese un numero: "))
    print("")
    print("*** TABLA DEL " + str(x) + " ***")
    i=0
    for i in range(1,11):
        producto=x*i
        print(str(x)+"x"+str(i)+"="+str(producto))
#tablamult()

def sumamulti():
    print("**** Sumar y multiplicar los datos ****")
    print("")
    nu1 = 1
    cont = 0
    pro = 1
    sumat = 0
    while cont < 5:
        nu1 = float(input("Ingrese un numero: "))
        cont = cont + 1
        sumat = sumat + nu1
        pro = pro*nu1
    print("La suma es " + str(sumat))
    print("El producto es " + str(pro))
    print("")
#sumamulti()

def secuencia():
    print("**** Multiplicar todos lo numeros que se vayan ingresando, se sale presionando 1 ****")
    print("")
    num1=0
    total = 0
    while num1 >= 0:
        num1 = int(input("Introduzca un numero: "))
        if num1 >=0:
            total = total + num1
        else:
            total=total

    print("El resultado es: " + str(total))
    print("")

#secuencia()

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

#producto()

def division():
    print("***** Division de dos numeros mediante restas *****")
    print("")
    dividendo = int(input("Introduce el Dividendo: "))
    divisor = int(input("Introduce el Divisor: "))
    cociente=int(0)
    residuo=dividendo

    while residuo > divisor:
        residuo = residuo-divisor
        cociente=cociente+1

    print("El Residuo es: " + str(residuo))
    print("El Cociente es: " + str(cociente))
    print("")

#division()

def secuenciaf():
    print("**** Multiplicar todos lo numeros que se vayan ingresando ****")
    print("")
    num1=str(input("ingrese un valor"))
    total=str(input("ingrese otro numero"))
    while num1 != "F":
        total = float(total) * float(num1)
        num1 = str(input("Introduzca un numero: "))
    print("El resultado es: ", total)
    print("")

#secuenciaf()

def numMayor():
        print("**** Encontrar el Numero mayor de los datos ingresados ****")
        print("")
        lista = []
        mayor = 0
        i = 1
        while (i <= 15):
            numero = int(input("Numero " + str(i) + ":"))
            lista.append(numero)
            i = i + 1

        mayor = max(lista)

        print("Los datos ingresados fueron: ", lista)
        print("Y el numero mayor es: ", mayor)
        print("")


#numMayor()

def binary():
    print("Convertir de una numero Decimal a un Binario")
    print("")
    n=int(input("Ingrese el Numero: "))
    print("")
    print(bin(n))

#binary()

def generar():
    print("Sumar secuencia de numeros divisibles de 5")
    i=int(input("Cuantos datos desean ingresar? "))
    n=2
    cont=1
    suma=0
    while cont <= i:
        print(n)
        n=n+3
        cont=cont+1
        if 5%n==0:
            suma=suma+n
        else:
            n=n
    print("La suma de los divisores de 5 es: ", suma)
#generar()

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

#fibonacci()

def numMayor():
        print("**** Encontrar el Numero mayor de los datos ingresados ****")
        print("")
        lista = []
        mayor = 0
        numero = 0
        i = 1
        numero = float(input("Numero " + str(i) + ": "))
        while (numero%2== 0):
            lista.append(numero)
            numero = float(input("Numero " + str(i+1) + ": "))
            i = i + 1

        mayor = max(lista)
        menor = min(lista)

        print("El numero mayor es: " + str(mayor))
        print("El numero menor es: " + str(menor))
        print("")

#numMayor()

def generarpar():
    print("Sumar secuencia de numeros divisibles de 5")
    i=int(input("Cuantos datos desean ingresar? "))
    n=2
    cont=1
    suma=0
    while cont <= i:
        n=float(input("Ingrese un Numero: "))
        cont=cont+1
        if n%2==0:

            print(str(suma)+" + " + str(n) + "= " + str(suma+n))
            suma = suma + n

        else:
            n=n
    print("La suma de los pares es: ", suma)
#generarpar()

def leerpar():
    n = int(input("Cuantas cantidades desea ingresar?"))
    lista=[]
    cont=0
    total = 0
    while cont < n:
        n1 = int(input("Ingrese un numero: "))
        n = cont + 1
        if n1 % 2 == 0:
            lista.append(n1)
    if cont <=10:
        print("La lista de los pares es: ", lista[0:cont])
    else:
        print("La lista de los pares es: ", lista[0:10])

#leerpar()

def lectura():
    cant = int(input("Cuantas cantidades desea ingresar?"))
    lista = []
    cont = 0
    cont2=0
    total = 0
    while cont < cant:
        num1 = int(input("Ingrese un numero: "))
        cont = cont + 1
        if num1 % 2 == 0:
            if cont <= 30:
                cont2 +=1
                lista.append(num1)
    lista.append(0)
    if cont2 <= 30:
        for x in range(cont2):
            total += lista[x]
        print("La suma de los pares es: ", total)
    else:
        for x in range(30):
            total += lista[x]
        print("La suma de los pares es: ", total)
#lectura()

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
for i in range(1):

    i = int(input("Ingrese un numero: "))

    if primo(i):
        print("es primo")
    else:
        print("no es primo")


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
for i in range(5):

    i = int(input("Ingrese un numero: "))

    if primo(i):
        print("es primo")
        suma = suma + i
    else:
        suma = suma

print("La suma de los primos es:", str(suma))

def sumfac():
    lista= []
    factlista=[]
    factorial=1
    total=0
    x=0
    y=1
    for x in range(1,6):
        valor=float(input("Ingrese un numero para sumar su factorial"))
        lista.append(valor)
    lista.append(0)
    for x in range(5):
        while y <= lista[x]:
            factorial = factorial*(y)
            y +=1
        factlista.append(factorial)
    for x in range(len(factlista)):
        total += factlista[x]
    print(total)

sumfac()

from math import factorial


def euler():
    num1 = int(input("Entre mas grande el numero mas preciso es el valor de euler"))
    euler = 1
    for i in range(1, num1):
        euler = euler + 1 / factorial(i)

    print("Numero de euler es: ", (euler))


euler()


def formula():
    numero = int(input("Ingrese el numero"))
    i = int(input("Ingrese I"))
    resultado = factorial(numero) / (factorial(i) * factorial(numero - i))
    print("EL resultado es: ", (resultado))


formula()


