#######  Desarrollado por Jorge Zárate
##  Ejercicio 5 - Imprimir todos los números pares que existen entre dos números leídos por teclado usando bucles for

aux = 0     # Variable que ayuda a que se ingresen los numeros correctamente (Numero Fin mayor a Numero Inicio)
while (aux != 1):   
    numIni = int(input("Ingrese el primer numero: "))
    numFin = int(input("Ingrese el ultimo numero: "))
    if (numFin > numIni):   # Si Numero Fin es mayor a Numero Inicio, se sale del ciclo
        aux = 1
    else:
        print(f"Numero fin debe ser mayor a Numero Inicio")


for i in range (numIni,numFin+1,1):
    if (i%2==0):
        print(f"|Numero Par {i}|", end=" ")
    #else:
    #    print(f"Numero Impar {i}")
