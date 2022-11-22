from random import randint
ficha1 = []
ficha2 = []
for i in range(2):
    ficha1.append(randint(0,6))
    ficha2.append(randint(0,6))
print(f"La ficha 1 es: {ficha1} y la ficha 2 es: {ficha2}")

if ficha1[0] == ficha2[0]:
    print(f"El primer numero de la primera ficha ({ficha1[0]}) y el primero de la segunda ficha ({ficha2[0]}) encajan.")
elif ficha1[1] == ficha2[0]:
    print(f"El segundo numero de la primera ficha ({ficha1[1]}) y el primero de la segunda ficha ({ficha2[0]}) encajan.")
elif ficha1[0] == ficha2[1]:
    print(f"El primer numero de la primera ficha ({ficha1[0]}) y el segundo de la segunda ficha ({ficha2[1]}) encajan.")
elif ficha1[1] == ficha2[1]:
    print(f"El segundo numero de la primera ficha ({ficha1[1]}) y el segundo de la segunda ficha ({ficha2[1]}) encajan.")
else:
    print("No encajan ninguna de las 2 partes.")