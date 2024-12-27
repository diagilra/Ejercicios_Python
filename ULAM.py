"""La siguiente se llama la conjetura de ULAM en honor del matemático S.Ulam:
• Comience con cualquier entero positivo
• Si es par, divídalo entre 2; si es impar, multiplíquelo por 3 y agréguele 1.
• Obtenga enteros sucesivamente repitiendo el proceso.
Al final, obtendrá el número 1, independientemente del entero inicial. Por ejemplo,
cuando el entero inicial es 26, la secuencia será: 26, 13, 40, 20, 10, 5, 16, 8, 4,
2, 1.
Escriba un programa que lea un entero positivo y obtenga e imprima
la sucesión de ULAM."""

num=0
try:
    num=int(input("Ingrese un número entero y positivo: "))

    if num>0:
        while num!=1:
            print(num, end=", ")
            if num%2==0:
                num=num//2
            else:
                num=num*3+1
        print(num)
    else:
        print("El número ingresado tiene que ser entero positivo")
except ValueError:
    print("Debes ingresar un número entero positivo")


