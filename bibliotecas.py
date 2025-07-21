####### Dev. Jorge Zárate

import os

while True:
    os.system("cls")
    print("1- Calculadora")
    print("2- Chrome")
    print("0- Salir")

    opcion = input("Ingrese una opcion: ")
    if (opcion == "1"):
        os.system("calc")
    elif (opcion == "2"):
        os.system("start chrome.exe")
    elif (opcion == "0"):
        break
    else:
        print("ERROR.")