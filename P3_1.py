"""Realice un programa tal que dado como datos 20 números enteros, obtenga
la suma de los números impares y el promedio de los números pares.
"""
# Inicialización de variables
suma_impares=0
suma_pares=0
conteo_pares=0

# Introducción de valores
print("Introduce 20 números enteros:")
for i in range(20):
    numero=int(input(f"Introduzca el número entero {i+1}"))
    if numero%2==1:
        suma_impares+=numero
    else:
        suma_pares+=numero
        conteo_pares+=1

if conteo_pares>0:
    promedio_pares=suma_pares/conteo_pares
else:
    promedio_pares=0


print(f"La suma de los impares es: {suma_impares} y el promedio de los pares es: {promedio_pares}")
    


