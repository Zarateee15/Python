####### Dev. Jorge Zárate

lista = []

def cargarLista(dato):
    lista.append(dato)

def imprimirLista():
    print(lista)

def quitarDatoLista(dato):
    lista.remove(dato)

if __name__ == "__main__":
    cargarLista("Jorge")
    cargarLista("Juan")
    cargarLista("Luis")
    imprimirLista()
    quitarDatoLista("Luis")
    imprimirLista()