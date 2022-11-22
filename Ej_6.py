lista = [2,4,5,8,25,5]

def estaOrdenada():
    ordenada = True
    for i in range(0, len(lista)-1,1):
        if lista[i]>lista[i+1]:
            ordenada=False
    return ordenada

if estaOrdenada() == False:
    print(f"La lista {lista} no esta ordenada")
if estaOrdenada() == True:
    print(f"La lista {lista} esta ordenada")