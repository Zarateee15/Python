####### Dev Jorge Zárate

class Calculadora:
    numA = None # Atributos
    numB = None
    
    def __init__ (self):    # Constructor
        self.numA = 0
        self.numB = 0
    
    def sumar (self):
        return self.numA + self.numB
    
    def restar (self):
        return self.numA - self.numB
    
    def multiplicar (self):
        return self.numA * self.numB
        
if __name__ == "__main__":
    casio = Calculadora()
    casio.numA = 60
    casio.numB = 35

    print(f"La suma es: {casio.sumar()}")
    print(f"La resta es: {casio.restar()}")
    print(f"La multiplicacion es: {casio.multiplicar()}")