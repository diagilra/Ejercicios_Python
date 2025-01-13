# Divisor máximo while
def maximo_divisor(n):
    maximo_actual = 0
    i = 1

    while i < n:
        if n % i == 0:
            maximo_actual = i
        i+=1
    return maximo_actual

# Máximo divisor for
def max_divisor(n):
    maximo_actual = 0
    i = 1 
    for i in range(1,n):
        if n % i == 0:
            maximo_actual = i
    return maximo_actual

print(maximo_divisor(8))
print(max_divisor(8))



