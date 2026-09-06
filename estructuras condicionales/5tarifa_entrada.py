#Solicita la edad de una persona y muestra el costo de entrada a un parque:
# Menores de 12 años: $50 
# De 12 a 17 años: $80 Adultos 
# (18 en adelante): $120

edad = int(input("ingrese su edad "))

if edad < 12:
    print("el costo de su entrada es de $50")
elif edad >= 12 and edad <= 17:
    print("el costo de su boleto es de $80")
else:
    print("el costo de su boleto es de $120")