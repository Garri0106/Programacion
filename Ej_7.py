cadena = ("Java es mejor que python")
cadena2 = "Java"
cadena3 = "JavaScript"

def reemplazarPalabra(cadena,cadena2,cadena3):
    nuevafrase = ""
    es = 0
    desplaza = 0
    control = 0
    if cadena2 in cadena:
        c = 0
        while c < len(cadena) and control == 0:
            if cadena[c] == cadena2[0]:
                while es < len(cadena2):
                    if cadena[c+desplaza] == cadena2[es]:
                        es+=1
                        desplaza += 1
                if es == len(cadena2) and cadena[c+len(cadena2)] == " ":
                    nuevafrase = nuevafrase + cadena3
                    c += len(cadena2)
                    es = 0
                else:
                    nuevafrase = "No esta la palabra que quieres sustituir"
                    es = 0
                    c += 1
                    control = 1
            else:
                nuevafrase += cadena[c]
                c += 1
    return nuevafrase

print(reemplazarPalabra(cadena,cadena2,cadena3))