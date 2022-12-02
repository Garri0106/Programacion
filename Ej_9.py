cadena = "curso de programacion"

def vocales_al_final(cadena):
    cadena_nueva = cadena
    cadena_nueva = cadena_nueva.replace("a","")
    cadena_nueva = cadena_nueva.replace("e","")
    cadena_nueva = cadena_nueva.replace("i","")
    cadena_nueva = cadena_nueva.replace("o","")
    cadena_nueva = cadena_nueva.replace("u","")
    for x in cadena.lower():
        if x=="a" or x=="e" or x=="i" or x=="o" or x=="u":
            cadena_nueva += x
    
    cadenita = cadena_nueva.replace(" ","")
    return cadenita

print(f"Esta es la cadena: {cadena}")
print(f"Y esta es la cadena con las vocales al final:")
print(vocales_al_final(cadena))