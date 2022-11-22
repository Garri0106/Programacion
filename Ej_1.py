from random import randint
lista = []

for i in range (101):
    lista.append(randint(0,1000))

print(lista)

def obtenerMayor(lista):
    mayor = lista[0]
    for i in range(len(lista)):
        if lista[i] > mayor:
            mayor = lista[i]
    return mayor
    
print(f"El mayor de esta lista es el: {obtenerMayor(lista)}")
''
def obtenerMenor(lista):
    menor = lista[0]
    for i in range(len(lista)):
        if lista[i] < menor:
            menor = lista[i]
    return menor

print(f"El menor esta lista es el: {obtenerMenor(lista)}")
''
def sumarNumerosLista():
    suma = 0
    for i in (lista):
        suma += i
    return suma

print(f"La suma de todos los elementos de la lista es igual a {sumarNumerosLista()}")
''
def obtenerMediaLista():
    suma = 0
    for i in (lista):
        suma += i
        media = suma/100
    return media
print(f"La media es {obtenerMediaLista()}")
''
def sustituirValor():
    n = int(input("¿Que número quieres sustituir?"))
    m = int(input("¿Por cuál número lo quieres sustituir?"))
    for i in range(len(lista)):
        if n == lista[i]: 
            lista[i] = m
    return lista

print(f"La nueva lista con los valores cambiados es la sigiente: {sustituirValor()}")