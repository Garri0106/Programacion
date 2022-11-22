from random import randint 

lista = []
lista2 = []

for i in range (11):
    lista.append(randint(0,100))
for i in range (11):
    lista2.append(randint(0,100))
    
def intersect(lista, lista2):
    lista_final = []
    for i in lista:
        if (i not in lista_final) and (i in lista2):
            lista_final.append(i)
    return lista_final

print(f"Esta es la primera lista: {lista}")
print(f"Esta es la segunda lista: {lista2}")
print(f"La lista final con los elementos en conjunto es: {intersect(lista, lista2)}")