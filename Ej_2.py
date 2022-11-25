'''
Created on Nov 22, 2022

@author: estudiante
'''
year = int(input("Introduce un año:"))
while year < 0 or year >9999:
    year = int(input("Introduce un año válido:"))

def isLeapYear():
    if year %4==0 and (year %100 != 0 or year %400==0):
        return True
    else:
        return False
print(isLeapYear())