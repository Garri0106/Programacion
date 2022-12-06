cadena = " He estudiado    mucho "

def contarPalabras(cadena):
    letraanterior = ""
    letraactual = ""
    acumulador = 1
    c = 0
    for i in range(len(cadena)):
        if cadena[i] == " " and letraanterior != " " and (i != 0 and i != len(cadena) -1):
            acumulador += 1
            
        letraanterior = cadena[i]
    return acumulador
print(f"La cadena: {cadena}")
print(f"Tiene un total de {contarPalabras(cadena)}")