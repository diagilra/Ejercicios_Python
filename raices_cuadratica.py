A=float(input("Introduzca el coeficiente a del polinomio:"))
B=float(input("Introduzca el coeficiente b del polinomio:"))
C=float(input("Introduzca el coeficiente c del polinomio:"))

DIS=B**2-4*A*C

if DIS>=0:
    x1=((-B)+DIS**0.5)/(2*A)
    x2=((-B)-DIS**0.5)/(2*A)
    print(f"Las raíces reales del polinomio son: {x1} y {x2}")
else:
    print("Las raíces del polinomio no son reales")


