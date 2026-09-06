#Solicita al usuario las 3 longitudes de los lados de un triángulo. 
#Indica si es equilátero, isósceles o escaleno.

lado1 = float(input("ingrese el primer lado "))
lado2 = float(input("ingrese el segundo lado "))
lado3 = float(input("ingrese el tercer lado "))

if lado1 == lado2 and lado2 == lado3:
    print("el triangulo es equilatero")
elif lado1 == lado2 or lado1 == lado3 or lado2 == lado3:
    print("el triangulo es isosceles")
else:
    print("el triangulo es escaleno")
