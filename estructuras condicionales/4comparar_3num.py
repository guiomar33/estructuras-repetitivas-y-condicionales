#Solicita tres números y muestra cuál es el mayor y cuál es el menor.

num = float(input("ingrese el primer numero "))
num2 = float(input("ingrese el segundo numero "))
num3 = float(input("ingrese el tercer numero "))

if num >= num2 and num >= num3:
    print("el numero mayor es ", num)
elif num2 >= num and num2 >= num3:
    print("el numero mayor es ", num2)
else:
    print("el numero mayor es ", num3)

if num <= num2 and num <= num3:
    print("el numero menor es ", num)
elif num2 <= num and num2 <= num3:
    print("el numero menor es ", num2)
else:
    print("el numero mayor es ", num3)