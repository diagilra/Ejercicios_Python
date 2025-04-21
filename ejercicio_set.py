# Con esta lista de números repetidos
lista = [1,2,1,1,5,6,4,4,4,6,7,5,1,1,7,7,7,2,1,2]

# imprimir un diccionario que tenga como llave (key) a cada uno de los números de la lista,
#  y que su respectivo valor (value) sea la cantidad de veces que ese número se encuentra en la lista. 

d = dict()
for num in set(lista):
    d[num] = lista.count(num)
print(d)