#######
## Ejercicio 6 - Imprimir un cuadrado y un triángulo con asteriscos o cualquier otra letra usando la estructura de repetición for()

# Triangulo
longTriangulo = int(input("Ingrese la cantidad de filas del triangulo: "))
aux = 1
print("Imprimiendo Triangulo....")
for i in range (1,longTriangulo+1):
    espacio = longTriangulo - i
    print(" " * espacio,  end = " ")
    print("*" * aux)
    aux = aux + 2


# Cuadrado
longCuadrado = int(input("Ingrese la dimensión del cuadrado lleno: "))
print("\nImprimiendo Cuadrado Lleno....")
for i in range (1,longCuadrado+1):
    print("* " * longCuadrado)

# Cuadrado con centro vacio
longMarco = int(input("Ingrese la dimensión del cuadrado vacio: "))
print("\nImprimiendo Cuadrado Vacio....")
for i in range (1,longMarco+1):
    if (i != 1) and (i != longMarco):
        print("* " + "  " * (longMarco-2) + "* ")
    else:
        print("* " * longMarco)






"""  Otra forma de hacer
# Triangulo
longTriangulo = int(input("Ingrese la cantidad de filas del triangulo."))
print("Imprimiendo Triangulo....")
for i in range (1,longTriangulo+1):
    for j in range (1,i+1): 
        print("*", end = " ")
    print(" ")

# Cuadrado
longCuadrado = int(input("Ingrese la dimensión del cuadrado."))
print("\nImprimiendo Cuadrado....")
for i in range (1,longCuadrado+1):
    for j in range (1,longCuadrado+1): 
        print("*", end = " ")
    print(" ")
"""
