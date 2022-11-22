def mostrarNombres(letra, lista):
    aux = []
    i=0
    for i in range(len(lista)):
        if lista[i][0] == letra:
            aux.append(lista[i])
    if len(aux) == 0:
        aux = f"No hay ninguna palabra en la lista con {letra}"
    return aux

palabras = ["Antonio", "Xope", "Bocadillo", "Juan", "Jose", "Miguel", "Ernesto Miguel", "Pepe", "Farrukita", "Unica", "Distinguida"]

letra = str(input("Introduzca la letra que desea:")).upper()
if letra.isdigit() == True:
    while letra.isdigit() == True:
        letra = input("Por favor, introduzca una letra:").upper()
print(mostrarNombres(letra, palabras))