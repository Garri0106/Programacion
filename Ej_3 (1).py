dia = int(input("Introduce el dia:"))
while dia <0 or dia >31:
    dia = int(input("Introduce un dia correcto:"))
    
mes = int(input("Inroduce el mes:"))
while mes <0 or mes >12:
    mes = int(input("Introduce un mes correcto:"))

año = int(input("Introduce el año:"))
while año <0 or año >9999:
    año = int(input("Introduce un año correcto:"))

lista_dia = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30]
lista_mes = ["Enero", "Febrero", "Marzo", "Abril", "Mayo", "Junio", "Julio", "Agosto", "Septiembre", "Octubre", "Noviembre", "Diciembre"]
diasMaximosMes = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

def escogerDia():
    for i in range(len(lista_dia)):
        dia = lista_dia[dia-1]
        
def escogerMes():
    for i in range(len(lista_mes)):
        mes_largo = lista_mes[mes-1]
    return mes_largo

print(f"La fecha en formato largo es {dia} de {escogerMes()} de {año}")