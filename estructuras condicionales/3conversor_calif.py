#Pide una calificación numérica (0–100) y muestra la equivalencia en letra:
# 90–100: A 
# 80–89: B 
# 70–79: C 
# 60–69: D 
# Menor a 60: F

calf = float(input("ingrese la calificacion "))

if calf >= 90 and calf <= 100:
    print("A")
elif calf >= 80 and calf <= 89:
    print("B")
elif calf >= 70 and calf <= 79:
    print("C")
elif calf >= 60 and calf <= 69:
    print ("D")
else:
    print("F")