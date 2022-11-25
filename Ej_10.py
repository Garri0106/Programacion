a = int(input("Introduce el primer número:"))
b = int(input("Introduce el segundo número:"))
suma = 0

def numerosAmigos(a, b):
    x = 1
    suma = 0
    while x < a:
        if a%x ==0:
            suma = suma + x
        x = x+1
    
    if suma == b:
        return True
    else:
        return False

if numerosAmigos(a, b) == True:
    print(f"Los números {a} y {b} son amigos")
elif numerosAmigos(a, b) == False:
    print(f"Los números {a} y {b} no son amigos")