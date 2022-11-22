from random import randint 
lista = []
lista_multiplos = []
lista_mayores = []
lista_menores = []
for i in range (11):
    lista.append(randint(0,100))
    
n = int(input("Introduce un número:"))
print(f"La lista es: {lista}")
def menores(lista):
    for i in lista:
        if i < n:
            lista_menores.append(i)
    return lista_menores
print(f"Los menores son {menores(lista)}")
def mayores(lista):
    for i in lista:
        if n < i:
            lista_mayores.append(i)
    return lista_mayores
print(f"Los mayores son {mayores(lista)}")

def multiplos(lista):
    for i in lista:
        if n % i == 0:
            lista_multiplos.append(n)
    return lista_multiplos
print(f"Los múltiplos son {multiplos(lista)}")