#Toma de datos
#Declaro e inicializo variables
letter = input("Escriba un caracter y presione enter ")

nature = letter.isnumeric()

#Inicio del if
if (nature == True):
    print("This is not a letter")
#Operación si no
else:
    UpperLower = letter.isupper()
    if (UpperLower == True):
        print("This is a uppercase letter")
    else:
        print("This is a lowercase letter")