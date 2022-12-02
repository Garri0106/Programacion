frase = "shybaoxlna" #Esta es True
frase2 = "soybahxlna" #Esta es False
'''buscar = str(input("¿Que palabra deseas buscar?: "))'''

def buscar_palabra_escondida(frase, palabra_escondida):
    posicion = 0
    for letra in frase:
        if posicion<len(palabra_escondida) and palabra_escondida[posicion] == letra:
            posicion += 1
    return posicion == len(palabra_escondida)

print(buscar_palabra_escondida("shybaoxlnaaa", "hola"))
print(buscar_palabra_escondida("sybaoxlhna", "hola"))