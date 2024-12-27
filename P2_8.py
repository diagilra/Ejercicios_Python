"""En una tienda efectúan un descuento a los clientes dependiendo del monto de la
compra. El descuento se efectúa con base en el siguiente criterio:
-Si el monto es menor que $500 no hay descuento.
-Si el monto está comprendido entre $500 y $1 000
inclusive 5% de descuento.
Si el monto está comprendido entre $1 000 y $7 000
inclusive 11% de descuento.
Si el monto está comprendido entre $7 000 y $15 000
inclusive 18% de descuento.
Si el monto es mayor a $15 000 25% de descuento.
Construya un diagrama de flujo tal que dado el monto de la compra de un
cliente, determine lo que el mismo debe pagar.
"""
COMPRA=float(input("Ingrese el valor de su compra: "))
PAGAR=0

if COMPRA<500:
        PAGAR=COMPRA
elif COMPRA>=500 and COMPRA<=1000:
        PAGAR=COMPRA*0.95
elif COMPRA>1000 and COMPRA<=7000:
        PAGAR=COMPRA*0.89
elif COMPRA>7000 and COMPRA<=15000:
        PAGAR=COMPRA*0.82
elif COMPRA>15000:
        PAGAR=COMPRA*0.75

print("Usted debe pagar:", PAGAR)