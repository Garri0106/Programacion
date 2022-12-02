frase = "Antonio el platano me esta hablando"

def vocales_diferentes(frase):
    lista_vocales = []
    cant_vocales = 0
    for x in frase.lower():
        if (x=="a" or x=="e" or x=="i" or x=="o" or x=="u") and (x not in lista_vocales):
            cant_vocales += 1
            lista_vocales.append(x)

    return cant_vocales

print(f"La cantidad de vocales diferentes que hay en la cadena {frase} son {vocales_diferentes(frase)}")