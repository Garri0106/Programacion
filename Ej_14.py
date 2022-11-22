cadena = ["Bocadillo xope", "Pan", "Jose Alfredo del Monte", "Narmalido", "Jose Carlos", "Soleado"]
def BuscarPalabraLarga(cadena):
    a= [""]
    palabra=""
    c=0
    for i in cadena:
        if len(i)>=len(palabra):
            contador=0
            for j in i:
                for k in i:
                    if k==j:
                        contador+=1
                    if c<contador:
                        c=contador
                        palabra=i
                        a.pop(0); a.append(i)
    return a

print(f"La palabra mas larga de la cadena es: {BuscarPalabraLarga(cadena)}")