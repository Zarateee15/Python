####### Desarrollado por Jorge Zárate
### Promedio de notas

nota = 1    # Nota cargada del alumno
sumaNotas = 0   # Sumatoria total de las notas, necesario para calcular el promedio
cantNotas = 0   # Cantidad de notas cargadas

while (nota != 0):  # While porque no sabemos cuantas notas se cargaran
    nota = int(input(f"Ingrese la nota del alumno {cantNotas + 1}."))
    if nota != 0:   # El programa termina cuando se ingresa el numero 0
        if nota >= 1 and nota<= 5:  # Solo hará el conteo cuando se ingrese 1, 2, 3, 4, 5
            sumaNotas = sumaNotas + nota
            cantNotas = cantNotas + 1
        else:   # Si se ingresa un numero que no son los anteriores dará error y volverá a pedir el dato
            print("Dato invalido.")

print(f"El promedio general es {sumaNotas/cantNotas}.") # Se imprime el promedio general calculado


# Otra manera de resolver
"""  
while (True):  # While porque no sabemos cuantas notas se cargaran
    nota = int(input(f"Ingrese la nota del alumno {cantNotas + 1}."))
    if nota != 0:   # El programa termina cuando se ingresa el numero 0
        if nota >= 1 and nota<= 5:  # Solo hará el conteo cuando se ingrese 1, 2, 3, 4, 5
            sumaNotas = sumaNotas + nota
            cantNotas = cantNotas + 1
        else:   # Si se ingresa un numero que no son los anteriores dará error y volverá a pedir el dato
            print("Dato invalido.")
    else:
        break
"""