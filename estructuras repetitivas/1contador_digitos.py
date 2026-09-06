#Cuenta cuántos dígitos tiene un número entero.

nume=int(input("ingrese un numero entero: "))
contado_digits = 0

while nume > 0 :
    contado_digits = contado_digits +1
    nume = nume // 10

print ("el numero tiene", contado_digits, "digitos")