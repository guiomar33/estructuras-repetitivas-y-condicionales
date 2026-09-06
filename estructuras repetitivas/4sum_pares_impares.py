#Calcula por separado la suma de los pares 
# y de los impares hasta n.

n = int(input("ingresa un numero"))

sum_par = 0
sum_impar = 0

for i in range(1, n+1):
    if i % 2 == 0:
        sum_par = sum_par + i
    else:
        sum_impar = sum_impar + i

print("suma de pares", sum_par)
print("suma de impares", sum_impar)