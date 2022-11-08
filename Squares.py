#numero = len(lista)

def squares(Dicto):
        
    for x in range(1, Quantity + 1):
        SquaresDictionary[x] = x**2
    return SquaresDictionary

def printResult(SquaresDictionary):
    result = squares(SquaresDictionary)
    print(result)

SquaresDictionary = {}
Quantity = int(input("¿Cuántos cuadrados desea conocer? "))

squares(Quantity)

printResult(SquaresDictionary)
#print(result)

