def exponente(n):
    i=0
    while 2**(i+1) <= n:
        i+=1
    return i

print(exponente(4))