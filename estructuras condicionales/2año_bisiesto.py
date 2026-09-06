#Solicita un año e indica si es bisiesto o no.
# (Un año es bisiesto si es divisible entre 4 pero no entre 100, o si es divisible entre 400).

añe = int(input("ingrese un año "))

if añe % 4 == 0 and añe % 100 != 0 or añe % 400 == 0:
    print("el año es bisiesto")
else:
    print("el año no es bisiesto")