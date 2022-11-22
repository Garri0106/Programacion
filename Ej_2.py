lista = [3, 5, 3, 7]
print(lista)
a_borrar = 0
a_escribir = 0

for i in range(len(lista)):
    a_borrar = lista[(i+1)%len(lista)]
    lista[(i+1)%len(lista)] = a_escribir
    a_escribir = a_borrar


print(lista)