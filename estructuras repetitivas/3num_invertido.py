#Invierte los dígitos de un número entero.

nume = int(input("ingresa un numero entero"))

invertide = 0
while nume > 0:
    digite = nume %10
    invertide = invertide * 10 + digite
    nume =nume // 10

print("el numero entero invertide es", invertide)