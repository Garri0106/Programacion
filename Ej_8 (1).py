lista = []
contador = 0
lista_primos = []
c = 0
n= int(input("Introduce un número positivo:"))
while n<0:
    n = int(input("Introduce un número válido"))
while n > 0:
    if n >= 0:
        lista.append(n)
    n = int(input("Introduce otro número (Negativo para terminar):"))
print(lista)
menu='''
    print("¿Qué opción deseas ejecutar con la lista?")
    print("a.-Ver los números primos")
    print("b.-El sumatorio de la lista")
    print("c.-La media de los números de la lista")
    print("d.-Otra lista con los factoriales de cada número")
'''
print(menu)

def suma(lista):
    sumaTotal = sum(lista)
    return sumaTotal
print(f"La suma de todos los números es: {suma(lista)}")

def media(lista):
    sumaTotal = sum(lista)
    media = sumaTotal/(len(lista))
    return media
print(f"La media de los númmeros es: {media(lista)}")

def factorial(lista):
    for i in range(len(lista)):
        fact=1
        aux = lista[i]
        while(aux>1):
            fact *= aux
            aux -= 1
        print(f"{lista[i]}! = {fact}")
print(f"El factorial es: {factorial(lista)}")

def es_primo(lista):
    divisores=0
    n=0
    contador=0
    primos=[]
    while contador!=len(lista):
        divisores=0
        for i in range(1,lista[n]):
            if lista[n]%i==0:
                divisores = divisores +1
        
        if divisores==1:
                primos.append(lista[n])
        n+=1
        contador+=1
    return primos
print(f"Los primos son: {es_primo(lista)}")
    
eleccion=""
while eleccion!="e":
    print(menu)
    eleccion = input("Opcion: ")
    if eleccion=="a":
        print(f"Los primos son: {es_primo(lista)}")
    elif eleccion=="b":
        print(f"La suma de todos los números es: {suma(lista)}")
    elif eleccion=="c":
        print(f"La media de todos los números es: {media(lista)}")
    elif eleccion=="d":
        print()
    elif eleccion=="e":
        print("Cerrando programa")
    else:
        print("Esa opción no es correcta")