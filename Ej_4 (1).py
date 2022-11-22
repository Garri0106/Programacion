lista = []
lista_pares = []
mayor = 0
n = int(input("Introduce un número:"))
while n<0:
    n = int(input("El primer número debe ser positivo. Introduce un número:"))

def obtenerMayor(lista):
    mayor = lista[0]
    for i in range(len(lista)):
        if lista[i] > mayor:
            mayor = lista[i]
    return mayor
def obtenerPares(lista):
        if n >=0:
            if n %2 == 0:
                lista_pares.append(n)
                
while n > 0:
    if n >= 0:
        lista.append(n)
    n = int(input("Introduce otro número (Negativo para terminar):"))
    obtenerMayor(lista)
    obtenerPares(lista)
    
print(f"La lista es: {lista}")
print(f"El número mayor de la lista es {mayor} y los pares son {lista_pares}")