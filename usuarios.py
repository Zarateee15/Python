####### Dev Jorge Zárate

cuentas = {"Jorge": "jorge123", "Victor": "victor123", "Beli": "beli123"}   # Usuario registrados.
intentos = 3

while (True):
    usuario = input("Ingrese su usuario: ")
    if (usuario in cuentas.keys()): # Pide ingresar el usuario hasta que se ingrese uno que exista.
        break
    else:
        print("Usuario es incorrecto o no existe.")

while (True):
    contraseña = input("Ingrese su contraseña: ")
    if (contraseña == cuentas[usuario]):    # Si ingresa la contraseña correcta sale del ciclo.
        print(f"Acceso correcto. Bienvenido!")
        break
    else:   
        intentos -= 1   # Cada vez que falla la contraseña disminuye el 1 la cantidad de intentos disponibles.
        if (intentos == 0):     # Si cantidad de intentos disponibles es 0, termina el programa.
            print(f"Muchos intentos fallidos. Intente nuevamente mas tarde.")
            break
        else:
            print(f"Contraseña incorrecta. Le quedan {intentos} intentos.")
        