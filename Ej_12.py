from random import randint 

lista = []
lista2 = []

for i in range (11):
    lista.append(randint(0,100))
for i in range (11):
    lista2.append(randint(0,100))

def unionListas(lista, lista2):
    union = []
    for i in lista:
        union.append(i)    
    for j in lista2:
        union.append(j)
    sinRepetidos=[]
    for i in union:
        if i not in sinRepetidos:
            sinRepetidos.append(i)
    return sinRepetidos
print(unionListas(lista, lista2))


print(f"Esta es la primera lista: {lista}")
print(f"Esta es la segunda lista: {lista2}")
print(f"Esta es la lista con todos los números: {unionListas(lista, lista2)}")